"""
bhavaarth.py  (v2)
------------------
भावार्थ — the essential meaning / soul of each note.

v1 problems fixed:
  • TATTVA → SUTRA  : TextRank sentence graph replaces TF-IDF centroid.
                      Now finds the sentence all other sentences orbit,
                      not the one with the most TF-IDF-heavy words.
  • SHABDA v2       : MMR-style deduplication removes redundant bigrams
                      ("domain name" + "domain names" → one kept).
                      Noise filter removes numbers, URLs, placeholder text.
  • RASA  (new)     : Classical Navarasa (नवरस) mapping from compound
                      score × intent × vocabulary cues.  Richer than a
                      two-word mood label.
  • PRASHNA (new)   : Extracts the driving question from the note body.
                      Falls back to an implicit-inquiry marker when no
                      explicit question sentence exists.
  • ATOMICITY (new) : Mean pairwise cosine similarity of sentence vectors.
                      High = one idea (ATOMIC); Low = many ideas (DIFFUSE).
                      DIFFUSE notes are morph/split candidates.

Five layers per note:
  SUTRA     (सूत्र)   — the thread: most central sentence via TextRank
  SHABDA    (शब्द)    — the words: corpus-distinctive, deduplicated keywords
  RASA      (रस)     — the flavour: one of the 9 classical emotional registers
  PRASHNA   (प्रश्न) — the question: the driving inquiry, explicit or implicit
  ATOMICITY          — ATOMIC / COMPOSITE / DIFFUSE (coherence score)

Usage:
  python3 scripts/analysis/bhavaarth.py              # full vault
  python3 scripts/analysis/bhavaarth.py published    # published only
  python3 scripts/analysis/bhavaarth.py all deep     # full note cards
  python3 scripts/analysis/bhavaarth.py all deep "path/to/note.md"
"""

import re
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from vault_loader import load_all_notes, load_published_notes

import nltk
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from tabulate import tabulate
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


# ═══════════════════════════════════════════════════════════════════════
# STOP WORDS
# ═══════════════════════════════════════════════════════════════════════

_BASE_STOPS = set(nltk.corpus.stopwords.words("english"))
_DOMAIN_STOPS = {
    "also", "one", "two", "three", "use", "used", "using", "like", "well",
    "get", "make", "need", "time", "way", "thing", "things", "really",
    "just", "even", "back", "first", "since", "much", "many", "new",
    "work", "working", "project", "note", "see", "know", "would", "could",
    "com", "org", "http", "www", "png", "jpg", "gif", "svg", "readme",
}
_ALL_STOPS = sorted(_BASE_STOPS | _DOMAIN_STOPS)


# ═══════════════════════════════════════════════════════════════════════
# INTENT SIGNALS
# ═══════════════════════════════════════════════════════════════════════

_INTENT_SIGNALS = {
    "EXPLORE":  {"experiment","explore","theory","wonder","question","maybe",
                 "perhaps","imagine","concept","propose","observe","hypothesis"},
    "BUILD":    {"build","system","architecture","deploy","stack","api",
                 "function","component","service","backend","pipeline",
                 "engine","code","script","tool","implement","design","schema",
                 "firmware","database"},
    "REFLECT":  {"feel","learn","experience","journey","lesson","memory",
                 "personal","failure","success","growth","life","story",
                 "believe","understand","meaning","philosophy","consciousness"},
    "ARCHIVE":  {"completed","history","previously","finished","released",
                 "deprecated","archived","former","old","was","had"},
    "COMMIT":   {"sow","scope","contract","deliverable","milestone","sprint",
                 "todo","task","action","requirement","specification",
                 "objective","kpi","target","deadline"},
}
_INTENT_ORDER = ["BUILD", "EXPLORE", "REFLECT", "ARCHIVE", "COMMIT"]

_CURIOUS_WORDS = {"what","why","how","wonder","curious","explore","question",
                  "imagine","theory","propose","hypothesis","perhaps","maybe"}


def _intent_scores(text: str) -> dict[str, int]:
    words = set(re.findall(r"\b[a-z]{3,}\b", text.lower()))
    return {k: len(words & v) for k, v in _INTENT_SIGNALS.items()}


def _dominant_intent(scores: dict[str, int]) -> str:
    best = max(_INTENT_ORDER, key=lambda k: scores[k])
    return best if scores[best] > 0 else "REFLECT"


# ═══════════════════════════════════════════════════════════════════════
# NAVARASA  (नवरस — nine aesthetic emotional registers)
# ═══════════════════════════════════════════════════════════════════════

_RASA_DEF = {
    "Adbhuta":   ("Wonder · Curiosity",     "✦"),
    "Vira":      ("Heroism · Making",        "⚡"),
    "Shringara": ("Beauty · Love of Ideas",  "◎"),
    "Hasya":     ("Joy · Enthusiasm",        "☀"),
    "Shanta":    ("Peace · Equanimity",      "—"),
    "Karuna":    ("Compassion · Longing",    "◇"),
    "Bhayanaka": ("Urgency · Concern",       "▽"),
    "Raudra":    ("Passion · Frustration",   "▼"),
    "Bibhatsa":  ("Revision · Letting Go",   "×"),
}


def compute_rasa(compound: float, intent: str,
                 text: str) -> tuple[str, str, str]:
    """
    Return (rasa_name, description, glyph).
    Maps VADER compound × dominant intent × curiosity cues to one of the 9 rasas.
    """
    words = set(re.findall(r"\b\w+\b", text.lower()))
    has_curiosity = bool(words & _CURIOUS_WORDS)

    # Wonder overrides when curiosity cues are present and note is not negative
    if has_curiosity and compound > -0.1:
        name = "Adbhuta"
    elif compound >= 0.50:
        name = {"BUILD": "Vira", "REFLECT": "Shringara",
                "EXPLORE": "Adbhuta"}.get(intent, "Hasya")
    elif compound >= 0.05:
        name = "Shanta" if intent in ("REFLECT", "EXPLORE") else "Vira"
    elif compound >= -0.05:
        name = "Shanta"
    elif compound >= -0.30:
        name = {"REFLECT": "Karuna", "BUILD": "Bhayanaka"}.get(intent, "Shanta")
    else:
        name = "Raudra" if intent == "COMMIT" else "Bibhatsa"

    desc, glyph = _RASA_DEF[name]
    return name, desc, glyph


# ═══════════════════════════════════════════════════════════════════════
# SUTRA  — TextRank sentence extraction
# ═══════════════════════════════════════════════════════════════════════

def _textrank(sentences: list[str], damping: float = 0.85,
              iterations: int = 10) -> list[float]:
    """
    PageRank over a sentence similarity graph.
    Returns a score per sentence; higher = more central.
    """
    n = len(sentences)
    if n == 1:
        return [1.0]

    vect = TfidfVectorizer(stop_words=_ALL_STOPS, min_df=1)
    try:
        mat  = vect.fit_transform(sentences)
        sim  = cosine_similarity(mat)
        np.fill_diagonal(sim, 0)

        # Row-normalise to get a transition matrix
        row_sums = sim.sum(axis=1, keepdims=True)
        row_sums[row_sums == 0] = 1
        T = sim / row_sums

        scores = np.ones(n) / n
        for _ in range(iterations):
            scores = damping * T.T @ scores + (1 - damping) / n
        return scores.tolist()
    except Exception:
        return [1.0 / n] * n


def extract_sutra(clean_text: str, max_chars: int = 140) -> str:
    """
    The single most central sentence — the thread that holds the note together.
    Falls back gracefully for short / stub notes.
    """
    sentences = [s.strip() for s in nltk.sent_tokenize(clean_text)
                 if len(s.split()) >= 6]
    if not sentences:
        short = [s.strip() for s in nltk.sent_tokenize(clean_text)
                 if len(s.split()) >= 3]
        return short[0][:max_chars] if short else "(stub — no sutra)"

    scores = _textrank(sentences)
    best   = sentences[int(np.argmax(scores))]
    return best[:max_chars] + ("…" if len(best) > max_chars else "")


# ═══════════════════════════════════════════════════════════════════════
# SHABDA  — Deduplicated corpus-distinctive keywords
# ═══════════════════════════════════════════════════════════════════════

_NOISE_RE = re.compile(r"^[\d\s\-_\.]+$")
_NOISE_TERMS = {"placeholder", "empty", "readme", "null", "none", "http",
                "www", "com", "org", "png", "jpg", "gif", "svg", "pdf"}


def _is_noise(kw: str) -> bool:
    return (bool(_NOISE_RE.match(kw))
            or len(kw) < 3
            or any(n in kw for n in _NOISE_TERMS))


def _is_redundant(candidate: str, selected: list[str],
                  overlap_thresh: float = 0.7) -> bool:
    c_words = set(candidate.split())
    for kept in selected:
        k_words = set(kept.split())
        # Subsumption: candidate is entirely contained in an existing bigram
        if c_words <= k_words:
            return True
        # Heavy word overlap
        if k_words and len(c_words & k_words) / max(len(c_words), 1) >= overlap_thresh:
            return True
    return False


def extract_shabda(note_idx: int, tfidf_matrix,
                   feature_names: list[str], top_n: int = 5) -> list[str]:
    """
    Corpus-distinctive keywords, deduplicated.
    Prefers bigrams over their component unigrams.
    """
    row = tfidf_matrix[note_idx].toarray()[0]
    # Take a generous pool to filter from
    pool_idx = row.argsort()[-(top_n * 5):][::-1]
    candidates = [(feature_names[i], float(row[i]))
                  for i in pool_idx if row[i] > 0]

    # Filter noise
    candidates = [(kw, sc) for kw, sc in candidates if not _is_noise(kw)]

    # Prefer bigrams: sort so that longer terms come first at equal score
    candidates.sort(key=lambda x: (-x[1], -len(x[0].split())))

    selected: list[str] = []
    for kw, _ in candidates:
        if len(selected) >= top_n:
            break
        if not _is_redundant(kw, selected):
            selected.append(kw)

    return selected


# ═══════════════════════════════════════════════════════════════════════
# PRASHNA  — driving question
# ═══════════════════════════════════════════════════════════════════════

_QUESTION_STARTERS = ("what ", "how ", "why ", "when ", "where ", "who ",
                      "which ", "can ", "should ", "could ", "would ",
                      "is ", "are ", "does ", "do ")


def extract_prashna(clean_text: str) -> str:
    """
    Find the first explicit question sentence.
    Falls back to the first sentence that reads like an implicit question.
    Returns a brief marker if no question is found.
    """
    sentences = nltk.sent_tokenize(clean_text)

    # 1. Explicit question mark
    for s in sentences:
        stripped = s.strip()
        if stripped.endswith("?") and len(stripped.split()) >= 4:
            return stripped[:130]

    # 2. Interrogative opener without question mark (informal writing)
    for s in sentences:
        low = s.strip().lower()
        if any(low.startswith(p) for p in _QUESTION_STARTERS):
            if len(s.split()) >= 6:
                return s.strip()[:130]

    # 3. Sentences containing key question-signal words
    for s in sentences:
        words = set(s.lower().split())
        if words & {"wonder", "curious", "question", "explore", "why", "how"}:
            if len(s.split()) >= 6:
                return s.strip()[:130]

    return "(implicit — no question stated)"


# ═══════════════════════════════════════════════════════════════════════
# ATOMICITY  — semantic coherence of the note
# ═══════════════════════════════════════════════════════════════════════

def compute_atomicity(clean_text: str) -> tuple[float, str]:
    """
    Mean pairwise cosine similarity across sentence vectors.

      ≥ 0.12   → ATOMIC     (one strong idea, self-consistent)
      0.04–0.12 → COMPOSITE  (2–3 related ideas, manageable)
      < 0.04   → DIFFUSE    (many topics, split candidate)

    Notes with fewer than 3 sentences are returned as ATOMIC (too short to measure).
    """
    sentences = [s.strip() for s in nltk.sent_tokenize(clean_text)
                 if len(s.split()) >= 4]
    if len(sentences) < 3:
        return 1.0, "ATOMIC"

    vect = TfidfVectorizer(stop_words=_ALL_STOPS, min_df=1)
    try:
        mat  = vect.fit_transform(sentences)
        sim  = cosine_similarity(mat)
        n    = len(sentences)
        upper = [sim[i, j] for i in range(n) for j in range(i + 1, n)]
        score = float(np.mean(upper)) if upper else 0.0

        if score >= 0.12:   label = "ATOMIC"
        elif score >= 0.04: label = "COMPOSITE"
        else:               label = "DIFFUSE"

        return round(score, 4), label
    except Exception:
        return 0.0, "ATOMIC"


# ═══════════════════════════════════════════════════════════════════════
# PER-NOTE ANALYSIS
# ═══════════════════════════════════════════════════════════════════════

def analyse_note(note: dict, idx: int, tfidf_matrix,
                 feature_names: list[str],
                 vader: SentimentIntensityAnalyzer) -> dict:
    text = note["clean_text"]
    pub  = note["published"]
    wc   = len([w for w in text.split() if w.isalpha()])

    if not text.strip():
        return {
            "pub": pub, "path": note["path"], "title": note["title"],
            "area": note["area"], "wc": 0,
            "sutra": "(stub)",
            "shabda": [],
            "rasa_name": "Shanta", "rasa_desc": "Peace · Equanimity", "rasa_glyph": "—",
            "prashna": "(stub)",
            "atomicity_score": 1.0, "atomicity_label": "ATOMIC",
            "intent": "REFLECT", "compound": 0.0,
            "bhav": "Neutral · REFLECT · ATOMIC",
        }

    compound = vader.polarity_scores(text)["compound"]
    iscores  = _intent_scores(text)
    intent   = _dominant_intent(iscores)

    sutra    = extract_sutra(text)
    shabda   = extract_shabda(idx, tfidf_matrix, feature_names)
    rasa_name, rasa_desc, rasa_glyph = compute_rasa(compound, intent, text)
    prashna  = extract_prashna(text)
    at_score, at_label = compute_atomicity(text)

    # Mood brief for BHAV headline
    if compound >= 0.50:   mood = "Energised"
    elif compound >= 0.25: mood = "Optimistic"
    elif compound >= 0.05: mood = "Calm-positive"
    elif compound >= -0.05:mood = "Neutral"
    elif compound >= -0.25:mood = "Contemplative"
    else:                  mood = "Critical"

    bhav = f"{mood} · {intent} · {at_label}"

    return {
        "pub": pub, "path": note["path"], "title": note["title"],
        "area": note["area"], "wc": wc,
        "sutra": sutra,
        "shabda": shabda,
        "rasa_name": rasa_name, "rasa_desc": rasa_desc, "rasa_glyph": rasa_glyph,
        "prashna": prashna,
        "atomicity_score": at_score, "atomicity_label": at_label,
        "intent": intent, "compound": compound,
        "bhav": bhav,
    }


# ═══════════════════════════════════════════════════════════════════════
# OUTPUT
# ═══════════════════════════════════════════════════════════════════════

_W = 110


def _pub_flag(r: dict) -> str:
    return "✓" if r["pub"] else " "


def print_summary_table(results: list[dict]) -> None:
    rows = []
    for r in sorted(results, key=lambda x: x["path"]):
        at_bar = "█" * int(r["atomicity_score"] * 20)
        rows.append([
            _pub_flag(r),
            r["path"][:42],
            r["title"][:28],
            f"{r['rasa_glyph']} {r['rasa_name']:<10}",
            ", ".join(r["shabda"][:3]) or "—",
            r["atomicity_label"],
            r["bhav"][:30],
        ])
    pub_n = sum(1 for r in results if r["pub"])
    print("\n" + "═" * _W)
    print(f"  BHAVAARTH  —  भावार्थ  v2  —  {len(results)} notes  "
          f"({pub_n} pub · {len(results)-pub_n} unpub)")
    print("  P=published  |  RASA=aesthetic register  |  SHABDA=top-3 keywords  "
          "|  ATOMICITY=coherence")
    print("═" * _W)
    print(tabulate(rows,
        headers=["P", "Path", "Title", "RASA", "SHABDA (top 3)", "ATOM.", "BHAV"],
        tablefmt="rounded_outline"))


def print_deep_cards(results: list[dict], filter_path: str | None = None) -> None:
    """Detailed per-note cards. If filter_path given, show only that note."""
    targets = results
    if filter_path:
        targets = [r for r in results if filter_path in r["path"]]
    if not targets:
        print(f"  No notes matching '{filter_path}'")
        return

    print("\n" + "═" * _W)
    print("  DEEP CARDS  —  full five-layer bhavaarth per note")
    print("═" * _W)

    for r in targets:
        pub_mark = "✓ PUBLISHED" if r["pub"] else "  unpublished"
        at_bar = ("█" * int(r["atomicity_score"] * 20)).ljust(20)

        print(f"\n  ┌─ [{pub_mark}]  {r['path']}")
        print(f"  │  {r['title']}")
        print(f"  │")
        print(f"  │  RASA     {r['rasa_glyph']}  {r['rasa_name']:12s} — {r['rasa_desc']}")
        print(f"  │")
        print(f"  │  SUTRA    {r['sutra']}")
        print(f"  │")
        print(f"  │  SHABDA   {' · '.join(r['shabda']) if r['shabda'] else '—'}")
        print(f"  │")
        print(f"  │  PRASHNA  {r['prashna']}")
        print(f"  │")
        at_label = r["atomicity_label"]
        at_score = r["atomicity_score"]
        split_hint = ""
        if at_label == "DIFFUSE":
            split_hint = "  ← MORPH CANDIDATE: split this note"
        elif at_label == "COMPOSITE":
            split_hint = "  ← consider extracting secondary thread"
        print(f"  │  ATOMIC   |{at_bar}| {at_score:.3f}  {at_label}{split_hint}")
        print(f"  │")
        print(f"  └─ BHAV     {r['bhav']}")


def print_rasa_distribution(results: list[dict]) -> None:
    print("\n" + "═" * _W)
    print("  RASA DISTRIBUTION  —  vault-wide aesthetic register")
    print("═" * _W)

    by_rasa: dict[str, list] = defaultdict(list)
    for r in results:
        by_rasa[r["rasa_name"]].append(r)

    for rasa_name in ["Adbhuta", "Vira", "Shringara", "Hasya",
                      "Shanta", "Karuna", "Bhayanaka", "Raudra", "Bibhatsa"]:
        members = by_rasa.get(rasa_name, [])
        if not members:
            continue
        pub_n   = sum(1 for r in members if r["pub"])
        unpub_n = len(members) - pub_n
        desc, glyph = _RASA_DEF[rasa_name]
        bar_p = "▓" * pub_n
        bar_u = "░" * unpub_n
        print(f"  {glyph} {rasa_name:12s} {desc:28s} {bar_p}{bar_u}  "
              f"({len(members)} · {pub_n} pub)")

    print("  ▓ = published  ░ = unpublished")


def print_atomicity_report(results: list[dict]) -> None:
    print("\n" + "═" * _W)
    print("  ATOMICITY REPORT  —  semantic coherence by note")
    print("═" * _W)

    diffuse   = [r for r in results if r["atomicity_label"] == "DIFFUSE"]
    composite = [r for r in results if r["atomicity_label"] == "COMPOSITE"]
    atomic    = [r for r in results if r["atomicity_label"] == "ATOMIC"]

    for label, group, advice in [
        ("DIFFUSE",   diffuse,   "✂ Split into 2+ atomic notes"),
        ("COMPOSITE", composite, "→ Consider extracting a secondary thread"),
        ("ATOMIC",    atomic,    "✓ Well-focused"),
    ]:
        pub_n = sum(1 for r in group if r["pub"])
        print(f"\n  {label:12s} ({len(group)} notes · {pub_n} pub)  —  {advice}")
        shown = sorted(group, key=lambda r: r["atomicity_score"])[:10]
        for r in shown:
            flag = "✓" if r["pub"] else " "
            bar  = ("█" * int(r["atomicity_score"] * 20)).ljust(20)
            print(f"  [{flag}] |{bar}| {r['atomicity_score']:.3f}  {r['path']}")


def print_rasa_clusters(results: list[dict]) -> None:
    """Group published notes by RASA — useful for graph cluster colouring."""
    print("\n" + "═" * _W)
    print("  RASA CLUSTERS  —  published notes grouped by aesthetic register")
    print("  (use these as secondary tag hints in frontmatter)")
    print("═" * _W)
    pub_results = [r for r in results if r["pub"]]
    by_rasa: dict[str, list] = defaultdict(list)
    for r in pub_results:
        by_rasa[r["rasa_name"]].append(r)

    for rasa_name, members in sorted(by_rasa.items(), key=lambda x: -len(x[1])):
        if not members:
            continue
        desc, glyph = _RASA_DEF[rasa_name]
        print(f"\n  {glyph} {rasa_name} — {desc}")
        for r in sorted(members, key=lambda x: x["path"]):
            print(f"    • {r['path']}  [{', '.join(r['shabda'][:2])}]")


# ═══════════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════════

def run(mode: str = "all", deep: bool = False,
        filter_path: str | None = None) -> None:

    print(f"Loading vault ({mode}) …")
    notes = load_published_notes() if mode == "published" else load_all_notes()
    if not notes:
        print("No notes found.")
        return

    pub_n = sum(1 for n in notes if n["published"])
    print(f"  {len(notes)} notes  ({pub_n} published · {len(notes)-pub_n} unpublished)")

    # ── Corpus TF-IDF model (shared across all notes for SHABDA) ────────
    print("Building corpus TF-IDF model …")
    safe_texts = [n["clean_text"] if n["clean_text"].strip()
                  else "placeholder" for n in notes]
    vectorizer = TfidfVectorizer(
        stop_words=_ALL_STOPS,
        ngram_range=(1, 2),
        min_df=1,
        max_df=0.82,
        sublinear_tf=True,
        max_features=5000,
    )
    tfidf_matrix = vectorizer.fit_transform(safe_texts)
    feature_names = vectorizer.get_feature_names_out().tolist()

    vader = SentimentIntensityAnalyzer()

    # ── Analyse ──────────────────────────────────────────────────────────
    print("Analysing notes …")
    results = [
        analyse_note(notes[i], i, tfidf_matrix, feature_names, vader)
        for i in range(len(notes))
    ]

    # ── Output ───────────────────────────────────────────────────────────
    print_summary_table(results)
    print_rasa_distribution(results)
    print_atomicity_report(results)
    print_rasa_clusters(results)

    if deep or filter_path:
        # Deep mode: only BUDDING/EVERGREEN notes (or the filtered one)
        if filter_path:
            print_deep_cards(results, filter_path)
        else:
            wc_threshold = 100
            deep_targets = [r for r in results if r["wc"] >= wc_threshold]
            print_deep_cards(deep_targets)


if __name__ == "__main__":
    args = sys.argv[1:]
    mode        = args[0] if args else "all"
    deep        = "deep" in args
    filter_path = args[2] if len(args) >= 3 and args[1] == "deep" else None
    run(mode, deep, filter_path)
