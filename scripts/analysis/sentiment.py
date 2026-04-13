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
from vault_loader import load_published_notes

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
    if not text.strip():
        return {
            "slug": note["slug"],
            "title": note["title"][:36],
            "compound": 0.0,
            "pos": 0.0,
            "neu": 1.0,
            "neg": 0.0,
            "mood": "— NEUTRAL",
            "peak_sentence": "(stub — no content)",
        }

    # Overall document score
    doc_scores = analyser.polarity_scores(text)

    # Per-sentence — find the single most emotionally charged sentence
    sentences = nltk.sent_tokenize(text)
    scored_sents = [
        (analyser.polarity_scores(s)["compound"], s)
        for s in sentences
        if len(s.split()) >= 5
    ]
    if scored_sents:
        peak_score, peak_sent = max(scored_sents, key=lambda x: abs(x[0]))
    else:
        peak_score, peak_sent = 0.0, sentences[0] if sentences else ""

    # Trim peak sentence for display
    peak_display = peak_sent[:90].replace("\n", " ")
    if len(peak_sent) > 90:
        peak_display += "…"

    return {
        "slug": note["slug"],
        "title": note["title"][:36],
        "compound": round(doc_scores["compound"], 3),
        "pos": round(doc_scores["pos"], 3),
        "neu": round(doc_scores["neu"], 3),
        "neg": round(doc_scores["neg"], 3),
        "mood": mood_label(doc_scores["compound"]),
        "peak_sentence": peak_display,
        "peak_score": round(peak_score, 3),
    }


def print_report(results: list[dict]) -> None:
    # Sort by compound score descending
    results_sorted = sorted(results, key=lambda r: r["compound"], reverse=True)

    print("\n" + "═" * 95)
    print("  SENTIMENT ANALYSIS — karx.github.io vault (VADER, published notes)")
    print("═" * 95)

    summary_rows = [
        [
            r["slug"],
            r["title"],
            f"{r['compound']:+.3f}",
            f"{r['pos']:.2f}",
            f"{r['neu']:.2f}",
            f"{r['neg']:.2f}",
            r["mood"],
        ]
        for r in results_sorted
    ]
    print(
        tabulate(
            summary_rows,
            headers=["Slug", "Title", "Compound", "Pos", "Neu", "Neg", "Mood"],
            tablefmt="rounded_outline",
        )
    )

    # Charged sentences section
    print("\n  ── PEAK EMOTIONAL SENTENCES ──────────────────────────────────────")
    charged = sorted(results, key=lambda r: abs(r["compound"]), reverse=True)[:8]
    for r in charged:
        bar_val = int(abs(r["compound"]) * 20)
        bar = ("█" * bar_val).ljust(20)
        sign = "+" if r["compound"] >= 0 else "-"
        print(f"\n  [{r['slug']}]  compound={r['compound']:+.3f}  {r['mood']}")
        print(f"  |{bar}| {sign}")
        print(f'  "{r["peak_sentence"]}"')

    # Distribution summary
    enthusiastic = sum(1 for r in results if r["compound"] >= 0.50)
    optimistic   = sum(1 for r in results if 0.25 <= r["compound"] < 0.50)
    mild_pos     = sum(1 for r in results if 0.05 <= r["compound"] < 0.25)
    neutral      = sum(1 for r in results if -0.05 < r["compound"] < 0.05)
    pensive      = sum(1 for r in results if -0.25 <= r["compound"] <= -0.05)
    melancholic  = sum(1 for r in results if r["compound"] < -0.25)

    print("\n  ── CORPUS MOOD DISTRIBUTION ──────────────────────────────────────")
    for label, count in [
        ("✦ ENTHUSIASTIC  (≥ +0.50)", enthusiastic),
        ("◎ OPTIMISTIC    (+0.25–0.50)", optimistic),
        ("· MILDLY POS    (+0.05–0.25)", mild_pos),
        ("— NEUTRAL       (−0.05–+0.05)", neutral),
        ("~ PENSIVE       (−0.25–−0.05)", pensive),
        ("▾ MELANCHOLIC   (< −0.25)", melancholic),
    ]:
        bar = "█" * count
        print(f"  {label:40s} {bar}  ({count})")
    print()


if __name__ == "__main__":
    print("Loading vault …")
    notes = load_published_notes()
    analyser = SentimentIntensityAnalyzer()
    results = [analyse_note(n, analyser) for n in notes]
    print_report(results)
