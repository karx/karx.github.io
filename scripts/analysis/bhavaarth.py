"""
bhavaarth.py
------------
Script 3 of 3 — भावार्थ (Bhavaarth): the essential meaning / soul of each note.

"भाव" (bhaav)  = feeling, essence, spirit
"अर्थ" (arth)  = meaning, purpose

This script extracts three layers per note:

  1. TATTVA  (तत्त्व — essence)
     The single sentence from the note that best captures its core idea,
     selected via TF-IDF cosine similarity against the full document vector.

  2. SHABDA  (शब्द — words)
     Top-5 corpus-distinctive keywords for this note (TF-IDF scores),
     filtered by the note's own vocabulary.  These are the words that
     make *this* note unique in the vault.

  3. BHAV    (भाव — feeling / intent)
     A synthesised one-line label combining the dominant mood (from VADER)
     and the inferred intent bucket:
       • EXPLORE  — open-ended thinking, questions, experiments
       • BUILD    — system design, architecture, tools
       • REFLECT  — personal essays, retrospectives, philosophy
       • ARCHIVE  — completed project logs, reference material
       • COMMIT   — SOW / contractual / action-oriented

Run: python3 scripts/analysis/bhavaarth.py
"""

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from vault_loader import load_all_notes, load_published_notes

import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from tabulate import tabulate
import numpy as np


# ─── intent detection ────────────────────────────────────────────────────────

EXPLORE_SIGNALS = {
    "experiment", "explore", "theory", "think", "wonder", "question",
    "maybe", "perhaps", "imagine", "what if", "could", "might",
    "observe", "hypothesis", "idea", "concept", "propose",
}
BUILD_SIGNALS = {
    "build", "system", "architecture", "deploy", "stack", "api",
    "function", "component", "service", "backend", "frontend",
    "database", "pipeline", "engine", "code", "script", "tool",
    "implement", "design", "schema",
}
REFLECT_SIGNALS = {
    "feel", "learn", "experience", "journey", "lesson", "memory",
    "personal", "failure", "success", "growth", "life", "story",
    "believe", "understand", "meaning", "philosophy",
}
ARCHIVE_SIGNALS = {
    "completed", "history", "previously", "finished", "released",
    "deprecated", "archived", "former", "old", "was", "had", "used",
}
COMMIT_SIGNALS = {
    "sow", "scope", "contract", "deliverable", "milestone", "sprint",
    "todo", "task", "action", "requirement", "specification",
    "objective", "kpi", "target", "deadline",
}


def infer_intent(text: str) -> str:
    words = set(re.findall(r"\b\w+\b", text.lower()))
    scores = {
        "EXPLORE": len(words & EXPLORE_SIGNALS),
        "BUILD":   len(words & BUILD_SIGNALS),
        "REFLECT": len(words & REFLECT_SIGNALS),
        "ARCHIVE": len(words & ARCHIVE_SIGNALS),
        "COMMIT":  len(words & COMMIT_SIGNALS),
    }
    # Tie-break: BUILD > EXPLORE > REFLECT > ARCHIVE > COMMIT
    order = ["BUILD", "EXPLORE", "REFLECT", "ARCHIVE", "COMMIT"]
    best = max(order, key=lambda k: scores[k])
    if scores[best] == 0:
        return "REFLECT"  # default for philosophical personal vaults
    return best


def mood_brief(compound: float) -> str:
    if compound >= 0.50:  return "Energised"
    if compound >= 0.25:  return "Optimistic"
    if compound >= 0.05:  return "Calm-positive"
    if compound >= -0.05: return "Neutral"
    if compound >= -0.25: return "Contemplative"
    return "Critical"


# ─── core extraction ─────────────────────────────────────────────────────────

def extract_tattva(clean_text: str, tfidf_matrix, note_idx: int,
                   vectorizer: TfidfVectorizer) -> str:
    """
    Select the sentence most similar to the document's TF-IDF vector.
    Falls back to the first non-trivial sentence for short notes.
    """
    sentences = [
        s.strip() for s in nltk.sent_tokenize(clean_text)
        if len(s.split()) >= 6
    ]
    if not sentences:
        return "(too short to extract tattva)"

    doc_vec = tfidf_matrix[note_idx]           # sparse (1, vocab)
    sent_vecs = vectorizer.transform(sentences) # sparse (n, vocab)
    sims = cosine_similarity(doc_vec, sent_vecs)[0]
    best_idx = int(np.argmax(sims))
    tattva = sentences[best_idx]
    # Trim to 120 chars
    return tattva[:120] + ("…" if len(tattva) > 120 else "")


def extract_shabda(note_idx: int, tfidf_matrix,
                   feature_names: list[str], top_n: int = 5) -> list[str]:
    """Top-N TF-IDF keywords for this note across the corpus."""
    row = tfidf_matrix[note_idx].toarray()[0]
    top_indices = row.argsort()[-top_n:][::-1]
    return [feature_names[i] for i in top_indices if row[i] > 0]


# ─── main ────────────────────────────────────────────────────────────────────

def run(mode: str = "all") -> None:
    print(f"Loading vault ({mode}) …")
    notes = load_published_notes() if mode == "published" else load_all_notes()
    if not notes:
        print("No published notes found.")
        return

    pub_count = sum(1 for n in notes if n["published"])
    print(f"  {len(notes)} notes loaded  ({pub_count} published · "
          f"{len(notes)-pub_count} unpublished)")

    texts = [n["clean_text"] for n in notes]

    # Build corpus TF-IDF matrix
    print("Building TF-IDF model …")
    stop_words_list = nltk.corpus.stopwords.words("english")
    # Add domain-specific stops that appear in almost every note
    domain_stops = [
        "also", "one", "two", "three", "use", "using", "used",
        "like", "well", "get", "make", "need", "time", "way",
        "thing", "things", "really", "just", "even", "back",
        "first", "since", "much", "many", "new", "work", "working",
        "project", "note", "see", "know", "would", "could",
    ]
    all_stops = stop_words_list + domain_stops

    vectorizer = TfidfVectorizer(
        stop_words=all_stops,
        ngram_range=(1, 2),
        min_df=1,
        max_df=0.85,
        sublinear_tf=True,
    )
    # Replace empty texts with placeholder so vectorizer doesn't crash
    safe_texts = [t if t.strip() else "placeholder empty note" for t in texts]
    tfidf_matrix = vectorizer.fit_transform(safe_texts)
    feature_names = vectorizer.get_feature_names_out().tolist()

    analyser = SentimentIntensityAnalyzer()

    print("\n" + "═" * 100)
    print("  BHAVAARTH  —  भावार्थ  —  the essential meaning of each note")
    print("  karx.github.io vault · published notes only")
    print("═" * 100)

    rows = []
    detail_blocks = []

    for i, note in enumerate(notes):
        text = note["clean_text"]
        compound = analyser.polarity_scores(text)["compound"] if text.strip() else 0.0
        intent = infer_intent(text)
        mood = mood_brief(compound)
        shabda = extract_shabda(i, tfidf_matrix, feature_names)
        tattva = extract_tattva(text, tfidf_matrix, i, vectorizer)
        bhav = f"{mood} · {intent}"
        pub_flag = "✓" if note["published"] else " "

        rows.append([
            pub_flag,
            note["path"][:40],
            note["title"][:30],
            note["area"],
            ", ".join(shabda) if shabda else "—",
            bhav,
        ])

        detail_blocks.append({
            "pub": pub_flag,
            "path": note["path"],
            "title": note["title"],
            "area": note["area"],
            "tattva": tattva,
            "shabda": shabda,
            "bhav": bhav,
            "compound": compound,
        })

    # Summary table
    pub_count = sum(1 for d in detail_blocks if d["pub"] == "✓")
    print("\n" + "═" * 110)
    print(f"  BHAVAARTH  —  भावार्थ  —  essential meaning")
    print(f"  {len(detail_blocks)} notes  ({pub_count} published · "
          f"{len(detail_blocks)-pub_count} unpublished)")
    print("  P = published in garden")
    print("═" * 110)
    print(tabulate(
        rows,
        headers=["P", "Path", "Title", "Area", "SHABDA (keywords)", "BHAV (mood·intent)"],
        tablefmt="rounded_outline",
    ))

    # Tattva — only show unpublished notes (published already analysed)
    unpub_details = [d for d in detail_blocks if d["pub"] == " " and d["tattva"] != "(too short to extract tattva)"]
    print("\n" + "─" * 110)
    print("  TATTVA — core sentence · UNPUBLISHED notes only (these are the hidden gems)")
    print("─" * 110)
    for d in unpub_details:
        print(f"\n  [ ] {d['path']}")
        print(f"    {d['tattva']}")

    # Intent distribution — published vs unpublished breakdown
    print("\n" + "─" * 110)
    print("  INTENT DISTRIBUTION")
    print("─" * 110)
    intent_totals: dict[str, list] = {}
    for d in detail_blocks:
        intent = d["bhav"].split(" · ")[1]
        intent_totals.setdefault(intent, [0, 0])
        if d["pub"] == "✓":
            intent_totals[intent][0] += 1
        else:
            intent_totals[intent][1] += 1
    for intent, (pub, unpub) in sorted(intent_totals.items(), key=lambda x: -(x[1][0]+x[1][1])):
        total = pub + unpub
        bar_p = "▓" * pub
        bar_u = "░" * unpub
        print(f"  {intent:10s} {bar_p}{bar_u}  ({total} total · {pub} pub · {unpub} unpub)")
    print("  ▓ = published  ░ = unpublished")

    # Extreme sentiment notes
    by_compound = sorted(detail_blocks, key=lambda d: d["compound"])
    print("\n  ── Most CONTEMPLATIVE (lowest compound) ─────────────────")
    for d in by_compound[:5]:
        print(f"  [{d['pub']}] {d['compound']:+.3f}  {d['path']}")
    print("\n  ── Most ENERGISED (highest compound) ────────────────────")
    for d in by_compound[-5:]:
        print(f"  [{d['pub']}] {d['compound']:+.3f}  {d['path']}")

    # Areas with deep unpublished content
    from collections import Counter
    area_words: dict[str, int] = {}
    for d in detail_blocks:
        if d["pub"] == " ":
            area_words[d["area"]] = area_words.get(d["area"], 0) + 1
    print("\n  ── Areas richest in unpublished notes ───────────────────")
    for area, count in sorted(area_words.items(), key=lambda x: -x[1])[:10]:
        bar = "█" * count
        print(f"  {area:25s} {bar}  ({count})")
    print()


if __name__ == "__main__":
    import sys
    mode = sys.argv[1] if len(sys.argv) > 1 else "all"
    run(mode)
