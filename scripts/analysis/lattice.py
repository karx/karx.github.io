"""
lattice.py
----------
Script 4 of 4 — The Structural Prescription Engine.

An intelligence system finds latent topology, not just statistics.
This script moves from description → action by answering five questions:

  1. CLUSTERS    What are the natural semantic groups in this vault?
                 (KMeans on TF-IDF vectors, named by top terms)

  2. TOPOLOGY    Which of the four vertical layers does each note belong to?
                 L4 Identity → L3 Principle → L2 System → L1 Instance

  3. BUCKETS     What is each note's temporal weight?
                 SOW/Contractual · Project Pulse · Evergreen/Atomic · Archival/Fossil

  4. LINKS       Which pairs of notes should be connected by WikiLinks?
                 (cosine similarity above threshold, cross-cluster preferred)

  5. ACTIONS     Ranked publishing queue, MOC candidates, Morph splits.

Run: python3 scripts/analysis/lattice.py
     python3 scripts/analysis/lattice.py published   ← published notes only
"""

import re
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from vault_loader import load_all_notes, load_published_notes

import nltk
import numpy as np
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from tabulate import tabulate
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


# ═══════════════════════════════════════════════════════════════════════════
# CONFIG
# ═══════════════════════════════════════════════════════════════════════════

N_CLUSTERS       = 8      # mirrors the 8 established tags in GARDEN_GUIDELINES
LINK_THRESHOLD   = 0.12   # min cosine sim to suggest a wikilink
TOP_LINKS        = 3      # max suggested links per note
TOP_CLUSTER_TERMS= 6      # terms used to label each cluster
MATURITY_WORDS   = {"STUB": 0, "SEED": 1, "BUDDING": 2, "EVERGREEN": 3}

# Cluster-name hints: if these terms dominate a cluster centroid, use this label
CLUSTER_HINTS = {
    frozenset(["iot", "esp", "mqtt", "sensor", "arduino", "firmware"]):      "IoT / Hardware",
    frozenset(["graph", "wikidata", "knowledge", "sparql", "rdf", "neo4j"]): "Knowledge Graph",
    frozenset(["interface", "compute", "web", "components", "browser"]):     "Interface / Web",
    frozenset(["stream", "twitch", "discord", "content", "youtube"]):        "Streaming / Content",
    frozenset(["startup", "akriya", "product", "market", "venture"]):        "Startup / Venture",
    frozenset(["print", "3d", "maker", "design", "fabrication"]):            "Making / 3D",
    frozenset(["compute", "consciousness", "awareness", "moments", "ego"]):  "Philosophy / Mind",
    frozenset(["sow", "deliverable", "scope", "milestone", "requirement"]):  "SOW / Contractual",
}


# ═══════════════════════════════════════════════════════════════════════════
# HELPERS
# ═══════════════════════════════════════════════════════════════════════════

_STOP = set(nltk.corpus.stopwords.words("english")) | {
    "also", "one", "two", "use", "used", "like", "well", "get", "make",
    "need", "time", "way", "thing", "just", "even", "back", "first",
    "since", "much", "many", "new", "work", "project", "see", "know",
    "would", "could", "using", "working", "note",
}

EXPLORE_W = {"experiment","explore","theory","wonder","question","maybe",
             "imagine","concept","propose","observe","hypothesis","idea"}
BUILD_W   = {"build","system","architecture","deploy","stack","api",
             "function","component","service","backend","pipeline","engine",
             "code","script","tool","implement","design","schema","firmware"}
REFLECT_W = {"feel","learn","experience","journey","lesson","memory",
             "personal","failure","success","growth","life","story",
             "believe","understand","meaning","philosophy","consciousness"}
ARCHIVE_W = {"completed","history","previously","finished","released",
             "deprecated","archived","former","old","was","had"}
COMMIT_W  = {"sow","scope","contract","deliverable","milestone","sprint",
             "todo","task","action","requirement","specification","objective"}


def _word_set(text: str) -> set[str]:
    return set(re.findall(r"\b[a-z]{3,}\b", text.lower()))


def _intent_scores(text: str) -> dict[str, int]:
    ws = _word_set(text)
    return {
        "EXPLORE":  len(ws & EXPLORE_W),
        "BUILD":    len(ws & BUILD_W),
        "REFLECT":  len(ws & REFLECT_W),
        "ARCHIVE":  len(ws & ARCHIVE_W),
        "COMMIT":   len(ws & COMMIT_W),
    }


def _dominant_intent(scores: dict[str, int]) -> str:
    order = ["BUILD","EXPLORE","REFLECT","ARCHIVE","COMMIT"]
    best = max(order, key=lambda k: scores[k])
    return best if scores[best] > 0 else "REFLECT"


def _maturity(word_count: int) -> str:
    if word_count < 50:   return "STUB"
    if word_count < 250:  return "SEED"
    if word_count < 700:  return "BUDDING"
    return "EVERGREEN"


def _word_count(text: str) -> int:
    return len([w for w in text.split() if w.isalpha()])


def _wikilink_slug(path: str) -> str:
    """Convert a vault path to the wikilink name the build script expects."""
    p = Path(path)
    parts = list(p.parts)
    if parts[-1].lower() == "readme.md":
        parts = parts[:-1]
    else:
        parts[-1] = parts[-1][:-3]
    # Use only the leaf name for the wikilink (matches build-garden.mjs logic)
    leaf = parts[-1] if parts else "about"
    return leaf


def _bucket(path: str, intent: str, maturity: str, title: str) -> str:
    """Assign one of the four Zettelkasten temporal-weight buckets."""
    title_low = title.lower()
    path_low  = path.lower()

    # SOW / Contractual
    if (intent == "COMMIT"
            or "sow" in title_low
            or "statement of work" in title_low
            or re.search(r"week[-_\s]?\d", path_low)
            and "status" in path_low):
        return "SOW/Contractual"

    # Archival / Fossil
    if (intent == "ARCHIVE"
            or "history" in path_low
            or re.search(r"\d{4}-\d{2}-\d{2}", path_low)
            or any(x in path_low for x in ["week-", "/log-", "delivery", "status-"])):
        return "Archival/Fossil"

    # Project Pulse (transient)
    if (intent == "BUILD"
            and maturity in ("STUB", "SEED")
            and not any(x in title_low for x in ["theory","pattern","principle","manifesto"])):
        return "Project Pulse"

    # Evergreen / Atomic
    if intent in ("EXPLORE", "REFLECT") or maturity in ("BUDDING", "EVERGREEN"):
        return "Evergreen/Atomic"

    return "Project Pulse"  # default


def _layer(path: str, intent: str, maturity: str, title: str) -> str:
    """Assign one of L1–L4 in the vertical hierarchy."""
    path_low  = path.lower()
    title_low = title.lower()

    # L4 Identity — the "who" layer
    if any(x in path_low for x in ["readme.md", "now/", "kaaro/"]) and \
       path_low in ("readme.md", "now/readme.md", "kaaro/readme.md"):
        return "L4 · Identity"

    # L3 Principle — timeless ideas, philosophies, mental models
    if (intent in ("EXPLORE", "REFLECT")
            and maturity in ("BUDDING", "EVERGREEN")
            and not any(x in path_low for x in ["sow", "delivery", "week", "status"])):
        return "L3 · Principle"

    # L2 System — reusable frameworks, SDKs, platforms
    if (intent == "BUILD"
            and maturity in ("BUDDING", "EVERGREEN")
            and any(x in title_low for x in
                    ["framework","sdk","platform","system","engine",
                     "toolkit","catalogue","graph","stream","component"])):
        return "L2 · System"

    # L1 Instance — specific projects, deliverables, experiments
    return "L1 · Instance"


def _cluster_label(centroid_vec, feature_names: list[str],
                   existing_labels: set[str]) -> str:
    """Name a cluster by its top TF-IDF terms, with hint matching."""
    top_idx  = centroid_vec.argsort()[-20:][::-1]
    top_terms = [feature_names[i] for i in top_idx]
    top_set   = set(top_terms[:8])

    best_hint, best_overlap = "Misc", 0
    for hint_keys, label in CLUSTER_HINTS.items():
        if label in existing_labels:
            continue
        overlap = len(top_set & hint_keys)
        if overlap > best_overlap:
            best_overlap, best_hint = overlap, label

    if best_overlap == 0:
        label = " / ".join(top_terms[:3]).title()
    else:
        label = best_hint

    # Deduplicate
    if label in existing_labels:
        label = label + f" ({top_terms[0]})"
    return label


# ═══════════════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════════════

def run(mode: str = "all") -> None:
    print(f"Loading vault ({mode}) …")
    notes = load_published_notes() if mode == "published" else load_all_notes()
    print(f"  {len(notes)} notes loaded")

    # ── Build TF-IDF corpus ──────────────────────────────────────────────
    print("Building TF-IDF model …")
    safe_texts = [n["clean_text"] if n["clean_text"].strip()
                  else "placeholder" for n in notes]

    vectorizer = TfidfVectorizer(
        stop_words=list(_STOP),
        ngram_range=(1, 2),
        min_df=1,
        max_df=0.80,
        sublinear_tf=True,
        max_features=4000,
    )
    tfidf = vectorizer.fit_transform(safe_texts)
    feat  = vectorizer.get_feature_names_out().tolist()

    # ── Per-note metadata ────────────────────────────────────────────────
    print("Computing per-note metadata …")
    vader = SentimentIntensityAnalyzer()
    meta  = []
    for i, n in enumerate(notes):
        wc     = _word_count(n["clean_text"])
        mat    = _maturity(wc)
        iscores = _intent_scores(n["clean_text"])
        intent = _dominant_intent(iscores)
        bucket = _bucket(n["path"], intent, mat, n["title"])
        layer  = _layer(n["path"], intent, mat, n["title"])
        comp   = vader.polarity_scores(n["clean_text"])["compound"] \
                 if n["clean_text"].strip() else 0.0
        meta.append({
            "idx":     i,
            "note":    n,
            "wc":      wc,
            "mat":     mat,
            "intent":  intent,
            "iscores": iscores,
            "bucket":  bucket,
            "layer":   layer,
            "compound":comp,
            "pub":     n["published"],
        })

    # ── KMeans clustering ────────────────────────────────────────────────
    print(f"Clustering into {N_CLUSTERS} semantic groups …")
    tfidf_dense = tfidf.toarray()
    km = KMeans(n_clusters=N_CLUSTERS, random_state=42, n_init=15)
    labels = km.fit_predict(tfidf_dense)

    # Name each cluster
    cluster_labels: dict[int, str] = {}
    used_names: set[str] = set()
    for c in range(N_CLUSTERS):
        label = _cluster_label(km.cluster_centers_[c], feat, used_names)
        cluster_labels[c] = label
        used_names.add(label)

    for m in meta:
        m["cluster"]    = labels[m["idx"]]
        m["cluster_lbl"]= cluster_labels[labels[m["idx"]]]

    # Distance to cluster centroid → centrality (lower = more central)
    for m in meta:
        c     = m["cluster"]
        vec   = tfidf_dense[m["idx"]]
        dist  = np.linalg.norm(vec - km.cluster_centers_[c])
        m["dist_to_centroid"] = dist

    # ── Cosine similarity → link suggestions ─────────────────────────────
    print("Computing similarity matrix …")
    sim = cosine_similarity(tfidf)
    np.fill_diagonal(sim, 0)          # no self-links

    # For every published note, find top similar notes (cross-cluster preferred)
    link_suggestions: dict[int, list[dict]] = defaultdict(list)
    for m in meta:
        if not m["pub"]:
            continue
        i   = m["idx"]
        row = sim[i].copy()

        # Boost cross-cluster similarities slightly (diversity of links)
        for j, other in enumerate(meta):
            if other["cluster"] != m["cluster"]:
                row[j] *= 1.15

        top_js = row.argsort()[-20:][::-1]
        added  = 0
        for j in top_js:
            if added >= TOP_LINKS:
                break
            if row[j] < LINK_THRESHOLD:
                break
            other = meta[j]
            # Skip if already linked (rough check: wikilink slug in raw body)
            slug = _wikilink_slug(other["note"]["path"])
            if slug.lower() in notes[i]["raw_body"].lower():
                continue
            link_suggestions[i].append({
                "target_path":  other["note"]["path"],
                "target_title": other["note"]["title"],
                "target_pub":   other["pub"],
                "sim":          round(float(row[j] / 1.15), 3),  # un-boost
                "wikilink":     f"[[{slug}]]",
                "bucket":       other["bucket"],
            })
            added += 1

    # Reverse map: for unpublished notes, which published notes should link TO them
    inbound_suggestions: dict[int, list[dict]] = defaultdict(list)
    for m in meta:
        if m["pub"]:
            continue
        i   = m["idx"]
        row = sim[i].copy()
        top_js = row.argsort()[-10:][::-1]
        for j in top_js:
            if row[j] < LINK_THRESHOLD:
                break
            if meta[j]["pub"]:
                inbound_suggestions[i].append({
                    "source_path":  notes[j]["path"],
                    "source_title": notes[j]["title"],
                    "sim":          round(float(row[j]), 3),
                    "wikilink":     f"[[{_wikilink_slug(notes[i]['path'])}]]",
                })

    # ── Impact score for publishing queue ────────────────────────────────
    for m in meta:
        if m["pub"]:
            m["impact"] = 0
            continue
        mat_w   = MATURITY_WORDS.get(m["mat"], 0)
        # centrality: invert distance (closer to centroid = more representative)
        centrality = 1.0 / (1.0 + m["dist_to_centroid"])
        # inbound connections = how many published notes already want to link here
        inbound    = len(inbound_suggestions[m["idx"]])
        # compound sentiment as a proxy for author investment
        invest     = abs(m["compound"])
        m["impact"] = round(
            mat_w * 2.0
            + centrality * 5.0
            + inbound * 3.0
            + invest * 1.0
            + (m["wc"] / 500)
        , 2)

    # ── Morph detection ──────────────────────────────────────────────────
    morph_candidates = []
    for m in meta:
        sc = m["iscores"]
        total = sum(sc.values())
        if total < 3:
            continue
        # A note morphs when it has two strong competing intents
        sorted_intents = sorted(sc.items(), key=lambda x: -x[1])
        top1_k, top1_v = sorted_intents[0]
        top2_k, top2_v = sorted_intents[1]
        if top1_v > 0 and top2_v > 0:
            ratio = top2_v / top1_v
            if ratio >= 0.55:      # second intent is ≥55% as strong as first
                morph_candidates.append({
                    "path":    m["note"]["path"],
                    "title":   m["note"]["title"],
                    "pub":     "✓" if m["pub"] else " ",
                    "intent1": f"{top1_k}({top1_v})",
                    "intent2": f"{top2_k}({top2_v})",
                    "ratio":   round(ratio, 2),
                    "bucket":  m["bucket"],
                    "action":  _morph_action(top1_k, top2_k),
                })
    morph_candidates.sort(key=lambda x: -x["ratio"])


    # ═══════════════════════════════════════════════════════════════════
    # OUTPUT
    # ═══════════════════════════════════════════════════════════════════

    W = 110

    # ── 1. CLUSTER MAP ──────────────────────────────────────────────────
    print("\n" + "═" * W)
    print("  1 · SEMANTIC CLUSTERS  (KMeans, TF-IDF, n=8)")
    print("═" * W)
    cluster_rows = []
    for c in range(N_CLUSTERS):
        members = [m for m in meta if m["cluster"] == c]
        pub_n   = sum(1 for m in members if m["pub"])
        top_terms = [feat[i] for i in km.cluster_centers_[c].argsort()[-TOP_CLUSTER_TERMS:][::-1]]
        cluster_rows.append([
            c,
            cluster_labels[c],
            len(members),
            pub_n,
            len(members) - pub_n,
            "  ·  ".join(top_terms),
        ])
    print(tabulate(cluster_rows,
        headers=["#", "Cluster Label", "Total", "Pub", "Unpub", "Top Terms"],
        tablefmt="rounded_outline"))

    # ── 2. VERTICAL LAYER TOPOLOGY ──────────────────────────────────────
    print("\n" + "═" * W)
    print("  2 · VERTICAL LAYER TOPOLOGY")
    print("  Shows where each note sits in the L4→L1 hierarchy")
    print("═" * W)
    for layer_name in ["L4 · Identity", "L3 · Principle", "L2 · System", "L1 · Instance"]:
        members = [m for m in meta if m["layer"] == layer_name]
        pub_n   = sum(1 for m in members if m["pub"])
        print(f"\n  {layer_name}  ({len(members)} notes · {pub_n} pub · {len(members)-pub_n} unpub)")
        print("  " + "─" * 80)
        rows = sorted(members, key=lambda m: (-int(m["pub"]), m["note"]["path"]))
        for m in rows[:20]:
            flag = "✓" if m["pub"] else " "
            print(f"  [{flag}] {m['bucket']:20s}  {m['note']['path']}")
        if len(rows) > 20:
            print(f"  … and {len(rows)-20} more")

    # ── 3. FOUR-BUCKET CLASSIFICATION ───────────────────────────────────
    print("\n" + "═" * W)
    print("  3 · FOUR-BUCKET CLASSIFICATION  (all notes)")
    print("═" * W)
    for bucket_name in ["Evergreen/Atomic", "SOW/Contractual",
                         "Project Pulse", "Archival/Fossil"]:
        members = [m for m in meta if m["bucket"] == bucket_name]
        pub_n   = sum(1 for m in members if m["pub"])
        print(f"\n  ── {bucket_name}  ({len(members)} · {pub_n} pub) " + "─" * 40)
        rows = sorted(members, key=lambda m: (-int(m["pub"]), -m["wc"]))
        for m in rows[:18]:
            flag = "✓" if m["pub"] else " "
            mat  = m["mat"]
            print(f"  [{flag}] {mat:10s}  {m['note']['path']}")
        if len(rows) > 18:
            print(f"  … and {len(rows)-18} more")

    # ── 4. MOC CANDIDATES ────────────────────────────────────────────────
    print("\n" + "═" * W)
    print("  4 · MAP OF CONTENT (MOC) CANDIDATES")
    print("  Most semantically central node per cluster → natural hub notes")
    print("═" * W)
    moc_rows = []
    for c in range(N_CLUSTERS):
        members = [m for m in meta if m["cluster"] == c
                   and m["mat"] in ("BUDDING","EVERGREEN")]
        if not members:
            members = [m for m in meta if m["cluster"] == c]
        if not members:
            continue
        # Most central = lowest distance to centroid
        best = min(members, key=lambda m: m["dist_to_centroid"])
        moc_rows.append([
            cluster_labels[c],
            "✓" if best["pub"] else "UNPUB",
            best["note"]["path"],
            best["note"]["title"][:40],
            best["mat"],
            f"[[{_wikilink_slug(best['note']['path'])}]]",
        ])
    print(tabulate(moc_rows,
        headers=["Cluster", "Status", "Path", "Title", "Maturity", "WikiLink"],
        tablefmt="rounded_outline"))

    # ── 5. LINK SUGGESTIONS ──────────────────────────────────────────────
    print("\n" + "═" * W)
    print("  5a · WIKILINKS TO ADD — published notes (top cross-cluster suggestions)")
    print("  Copy-paste these directly into the note body")
    print("═" * W)
    pub_meta = [m for m in meta if m["pub"] and link_suggestions[m["idx"]]]
    pub_meta.sort(key=lambda m: m["note"]["path"])
    for m in pub_meta:
        print(f"\n  ▸ {m['note']['path']}")
        for sug in link_suggestions[m["idx"]]:
            pflag = "✓" if sug["target_pub"] else "UNPUB"
            print(f"    + {sug['wikilink']:45s}  sim={sug['sim']:.3f}  [{pflag}]  {sug['bucket']}")

    print("\n" + "═" * W)
    print("  5b · INBOUND LINK OPPORTUNITIES — unpublished EVERGREEN notes")
    print("  Which published notes should grow a link pointing to these")
    print("═" * W)
    unpub_eg = [m for m in meta
                if not m["pub"]
                and m["mat"] in ("BUDDING","EVERGREEN")
                and inbound_suggestions[m["idx"]]]
    unpub_eg.sort(key=lambda m: -m["impact"])
    for m in unpub_eg[:15]:
        print(f"\n  [ ] {m['note']['path']}  ({m['wc']}w · {m['mat']})")
        for sug in inbound_suggestions[m["idx"]][:2]:
            print(f"    ← {sug['source_path']}  should add  {sug['wikilink']}")

    # ── 6. MORPH CANDIDATES ──────────────────────────────────────────────
    print("\n" + "═" * W)
    print("  6 · MORPH CANDIDATES — notes doing two jobs (split for atomicity)")
    print("═" * W)
    morph_rows = [[
        m["pub"], m["path"][:50], m["intent1"],
        m["intent2"], m["ratio"], m["action"]
    ] for m in morph_candidates[:12]]
    print(tabulate(morph_rows,
        headers=["P","Path","Intent-1","Intent-2","Ratio","Suggested Split"],
        tablefmt="rounded_outline"))

    # ── 7. PUBLISHING QUEUE ──────────────────────────────────────────────
    print("\n" + "═" * W)
    print("  7 · PUBLISHING QUEUE — ranked by impact score")
    print("  Impact = maturity × centrality × inbound-connections × author-investment")
    print("═" * W)
    queue = [m for m in meta if not m["pub"] and m["mat"] != "STUB"]
    queue.sort(key=lambda m: -m["impact"])
    q_rows = []
    for rank, m in enumerate(queue[:20], 1):
        inb = len(inbound_suggestions[m["idx"]])
        slug = _wikilink_slug(m["note"]["path"])
        q_rows.append([
            rank,
            m["note"]["path"][:50],
            m["note"]["title"][:30],
            m["wc"],
            m["mat"],
            m["bucket"][:12],
            m["cluster_lbl"][:20],
            inb,
            m["impact"],
            f"[[{slug}]]",
        ])
    print(tabulate(q_rows,
        headers=["#","Path","Title","Words","Mat","Bucket",
                 "Cluster","InLinks","Impact","WikiLink"],
        tablefmt="rounded_outline"))

    # ── 8. GRAPH HEALTH PROJECTION ───────────────────────────────────────
    current_edges  = sum(len(v) for v in link_suggestions.values())
    current_pub    = sum(1 for m in meta if m["pub"])
    top10_queue    = queue[:10]
    projected_pub  = current_pub + len(top10_queue)
    projected_edges= current_edges + sum(len(inbound_suggestions[m["idx"]])
                                         for m in top10_queue)
    isolated_now   = sum(1 for m in meta if m["pub"]
                         and not link_suggestions[m["idx"]]
                         and sum(1 for v in link_suggestions.values()
                                 for s in v if s["target_path"] == m["note"]["path"]) == 0)

    print("\n" + "═" * W)
    print("  8 · GRAPH HEALTH PROJECTION")
    print("═" * W)
    rows = [
        ["Published notes",  current_pub,  projected_pub,   "≥ 40"],
        ["New edge suggestions", "—",      current_edges,   "≥ 80"],
        ["Projected edges",  "~34 (now)", projected_edges,  "≥ 80"],
        ["Isolated nodes",   isolated_now, "< 5",           "0"],
    ]
    print(tabulate(rows,
        headers=["Metric","Now","After top-10 queue","Target"],
        tablefmt="rounded_outline"))
    print()


def _morph_action(intent1: str, intent2: str) -> str:
    pairs = frozenset({intent1, intent2})
    if pairs == {"REFLECT", "BUILD"}:
        return "Extract principle → new Evergreen note; keep BUILD as Project Pulse"
    if pairs == {"EXPLORE", "COMMIT"}:
        return "Extract open questions → new Evergreen; move action items to Project Pulse"
    if pairs == {"REFLECT", "COMMIT"}:
        return "Split: philosophy stays Evergreen; task list → Project Pulse"
    if pairs == {"BUILD", "ARCHIVE"}:
        return "Add retrospective section; mark implementation as Archival/Fossil"
    if pairs == {"EXPLORE", "BUILD"}:
        return "Keep theory as L3 Principle; extract system design to L2 System note"
    return f"Split {intent1} layer from {intent2} layer into two separate notes"


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "all"
    run(mode)
