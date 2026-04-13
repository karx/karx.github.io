"""
sentiment.py
------------
Script 2 of 3 — Sentiment analysis per published note.

Uses VADER (Valence Aware Dictionary and sEntiment Reasoner),
which handles informal writing, emojis, and sentence fragments
better than bag-of-words classifiers.

Outputs:
  • Per-note: compound score, positive/neutral/negative ratios,
    dominant mood label, and the single most emotionally charged sentence.
  • Corpus heatmap sorted by compound score.

Run: python3 scripts/analysis/sentiment.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from vault_loader import load_all_notes, load_published_notes

import nltk
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from tabulate import tabulate


MOOD_MAP = [
    (+0.50,  "✦ ENTHUSIASTIC"),
    (+0.25,  "◎ OPTIMISTIC"),
    (+0.05,  "· MILDLY POSITIVE"),
    (-0.05,  "— NEUTRAL"),
    (-0.25,  "~ PENSIVE"),
    (-0.50,  "▾ MELANCHOLIC"),
    (-1.00,  "▼ CRITICAL"),
]


def mood_label(compound: float) -> str:
    for threshold, label in MOOD_MAP:
        if compound >= threshold:
            return label
    return "▼ CRITICAL"


def analyse_note(note: dict, analyser: SentimentIntensityAnalyzer) -> dict:
    text = note["clean_text"]
    pub_flag = "✓" if note["published"] else " "

    if not text.strip():
        return {
            "pub": pub_flag,
            "path": note["path"][:48],
            "title": note["title"][:34],
            "area": note["area"],
            "compound": 0.0,
            "pos": 0.0,
            "neu": 1.0,
            "neg": 0.0,
            "mood": "— NEUTRAL",
            "peak_sentence": "(stub — no content)",
            "peak_score": 0.0,
        }

    doc_scores = analyser.polarity_scores(text)

    sentences = nltk.sent_tokenize(text)
    scored_sents = [
        (analyser.polarity_scores(s)["compound"], s)
        for s in sentences
        if len(s.split()) >= 5
    ]
    if scored_sents:
        peak_score, peak_sent = max(scored_sents, key=lambda x: abs(x[0]))
    else:
        peak_score, peak_sent = 0.0, (sentences[0] if sentences else "")

    peak_display = peak_sent[:95].replace("\n", " ")
    if len(peak_sent) > 95:
        peak_display += "…"

    return {
        "pub": pub_flag,
        "path": note["path"][:48],
        "title": note["title"][:34],
        "area": note["area"],
        "compound": round(doc_scores["compound"], 3),
        "pos": round(doc_scores["pos"], 3),
        "neu": round(doc_scores["neu"], 3),
        "neg": round(doc_scores["neg"], 3),
        "mood": mood_label(doc_scores["compound"]),
        "peak_sentence": peak_display,
        "peak_score": round(peak_score, 3),
    }


def print_report(results: list[dict]) -> None:
    results_sorted = sorted(results, key=lambda r: r["compound"], reverse=True)
    pub_count = sum(1 for r in results if r["pub"] == "✓")

    print("\n" + "═" * 110)
    print(f"  SENTIMENT — karx.github.io vault  "
          f"({len(results)} notes · {pub_count} published · "
          f"{len(results)-pub_count} unpublished)  |  VADER")
    print("  P = published   |  sorted highest → lowest compound score")
    print("═" * 110)

    summary_rows = [
        [
            r["pub"], r["path"], r["title"], r["area"],
            f"{r['compound']:+.3f}",
            f"{r['pos']:.2f}", f"{r['neu']:.2f}", f"{r['neg']:.2f}",
            r["mood"],
        ]
        for r in results_sorted
    ]
    print(tabulate(
        summary_rows,
        headers=["P", "Path", "Title", "Area", "Compound", "Pos", "Neu", "Neg", "Mood"],
        tablefmt="rounded_outline",
    ))

    # Most charged sentences across the full vault
    print("\n  ── PEAK EMOTIONAL SENTENCES (top 10 by |compound|) ──────────────")
    charged = sorted(results, key=lambda r: abs(r["compound"]), reverse=True)[:10]
    for r in charged:
        bar_val = int(abs(r["compound"]) * 20)
        bar = ("█" * bar_val).ljust(20)
        sign = "+" if r["compound"] >= 0 else "-"
        print(f"\n  [{r['pub']}] {r['path']}")
        print(f"  |{bar}| {r['compound']:+.3f}  {r['mood']}")
        print(f'  "{r["peak_sentence"]}"')

    # Mood distribution — separate published vs unpublished
    print("\n  ── MOOD DISTRIBUTION ─────────────────────────────────────────────")
    bands = [
        ("✦ ENTHUSIASTIC  (≥ +0.50)", lambda c: c >= 0.50),
        ("◎ OPTIMISTIC    (+0.25–0.50)", lambda c: 0.25 <= c < 0.50),
        ("· MILDLY POS    (+0.05–0.25)", lambda c: 0.05 <= c < 0.25),
        ("— NEUTRAL       (−0.05–+0.05)", lambda c: -0.05 < c < 0.05),
        ("~ PENSIVE       (−0.25–−0.05)", lambda c: -0.25 <= c <= -0.05),
        ("▾ MELANCHOLIC   (< −0.25)", lambda c: c < -0.25),
    ]
    for label, pred in bands:
        total = sum(1 for r in results if pred(r["compound"]))
        pub   = sum(1 for r in results if pred(r["compound"]) and r["pub"] == "✓")
        bar = "█" * total
        print(f"  {label:40s} {bar:30s} ({total} total · {pub} pub)")
    print()


if __name__ == "__main__":
    import sys
    mode = sys.argv[1] if len(sys.argv) > 1 else "all"
    print(f"Loading vault ({mode}) …")
    notes = load_published_notes() if mode == "published" else load_all_notes()
    analyser = SentimentIntensityAnalyzer()
    results = [analyse_note(n, analyser) for n in notes]
    print_report(results)
