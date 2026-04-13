"""
text_stats.py
-------------
Script 1 of 3 — Text statistics per published note.

Outputs:
  • Per-note table: word count, sentence count, unique vocab,
    lexical density, avg sentence length, reading time (min),
    Flesch-Kincaid grade level, wikilink count.
  • Corpus-wide summary.

Run: python3 scripts/analysis/text_stats.py
"""

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from vault_loader import load_published_notes, VAULT_ROOT

import nltk
from tabulate import tabulate


# ─── helpers ────────────────────────────────────────────────────────────────

def count_syllables(word: str) -> int:
    """Rough English syllable count (works well enough for FK formula)."""
    word = word.lower().strip(".,!?;:'\"()")
    if not word:
        return 0
    vowels = "aeiouy"
    count = 0
    prev_vowel = False
    for ch in word:
        is_v = ch in vowels
        if is_v and not prev_vowel:
            count += 1
        prev_vowel = is_v
    # silent-e
    if word.endswith("e") and count > 1:
        count -= 1
    return max(1, count)


def flesch_kincaid_grade(words: list[str], sentences: list[str]) -> float:
    if not words or not sentences:
        return 0.0
    syllable_count = sum(count_syllables(w) for w in words)
    asl = len(words) / len(sentences)          # avg sentence length
    asw = syllable_count / len(words)           # avg syllables per word
    return 0.39 * asl + 11.8 * asw - 15.59


def wikilink_count(raw_body: str) -> int:
    return len(re.findall(r"\[\[", raw_body))


# ─── main ───────────────────────────────────────────────────────────────────

def analyse(notes: list[dict]) -> list[dict]:
    results = []
    for note in notes:
        text = note["clean_text"]
        if not text.strip():
            results.append(
                {
                    "slug": note["slug"],
                    "title": note["title"][:38],
                    "words": 0,
                    "sentences": 0,
                    "unique_vocab": 0,
                    "lex_density_%": 0,
                    "avg_sent_len": 0,
                    "read_min": 0,
                    "fk_grade": "—",
                    "wikilinks": wikilink_count(note["raw_body"]),
                    "status": "STUB",
                }
            )
            continue

        sentences = nltk.sent_tokenize(text)
        words_raw = nltk.word_tokenize(text)
        words = [w for w in words_raw if w.isalpha()]
        unique = set(w.lower() for w in words)
        content_words = [
            w for w in words
            if w.lower()
            not in nltk.corpus.stopwords.words("english")
        ]
        lex_density = (
            round(len(content_words) / len(words) * 100, 1) if words else 0
        )
        avg_sent = round(len(words) / len(sentences), 1) if sentences else 0
        read_min = round(len(words) / 200, 1)  # 200 wpm
        fk = flesch_kincaid_grade(words, sentences)

        # Classify note maturity by word count
        if len(words) < 50:
            status = "STUB"
        elif len(words) < 250:
            status = "SEED"
        elif len(words) < 700:
            status = "BUDDING"
        else:
            status = "EVERGREEN"

        results.append(
            {
                "slug": note["slug"],
                "title": note["title"][:38],
                "words": len(words),
                "sentences": len(sentences),
                "unique_vocab": len(unique),
                "lex_density_%": lex_density,
                "avg_sent_len": avg_sent,
                "read_min": read_min,
                "fk_grade": round(fk, 1),
                "wikilinks": wikilink_count(note["raw_body"]),
                "status": status,
            }
        )
    return results


def print_report(results: list[dict]) -> None:
    headers = [
        "Slug", "Title", "Words", "Sents", "Vocab",
        "LexDen%", "AvgSL", "Read(m)", "FK", "Links", "Maturity"
    ]
    rows = [
        [
            r["slug"],
            r["title"],
            r["words"],
            r["sentences"],
            r["unique_vocab"],
            r["lex_density_%"],
            r["avg_sent_len"],
            r["read_min"],
            r["fk_grade"],
            r["wikilinks"],
            r["status"],
        ]
        for r in results
    ]
    # Sort by word count descending
    rows.sort(key=lambda x: x[2], reverse=True)

    print("\n" + "═" * 90)
    print("  TEXT STATS — karx.github.io vault (published notes only)")
    print("═" * 90)
    print(tabulate(rows, headers=headers, tablefmt="rounded_outline"))

    # Summary
    total_words = sum(r["words"] for r in results)
    stubs = sum(1 for r in results if r["status"] == "STUB")
    seeds = sum(1 for r in results if r["status"] == "SEED")
    budding = sum(1 for r in results if r["status"] == "BUDDING")
    evergreen = sum(1 for r in results if r["status"] == "EVERGREEN")
    total_links = sum(r["wikilinks"] for r in results)

    print(f"\n  Notes analysed : {len(results)}")
    print(f"  Total words    : {total_words:,}")
    print(f"  Total wikilinks: {total_links}")
    print(f"\n  Maturity breakdown:")
    print(f"    STUB      (< 50 words) : {stubs}")
    print(f"    SEED      (50–249)     : {seeds}")
    print(f"    BUDDING   (250–699)    : {budding}")
    print(f"    EVERGREEN (700+)       : {evergreen}")
    print()


if __name__ == "__main__":
    print("Loading vault …")
    notes = load_published_notes()
    results = analyse(notes)
    print_report(results)
