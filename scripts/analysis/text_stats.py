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
from vault_loader import load_all_notes, load_published_notes, VAULT_ROOT

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
    stopwords = set(nltk.corpus.stopwords.words("english"))
    results = []
    for note in notes:
        text = note["clean_text"]
        wlinks = wikilink_count(note["raw_body"])
        pub_flag = "✓" if note["published"] else " "

        if not text.strip():
            results.append(
                {
                    "pub": pub_flag,
                    "path": note["path"][:45],
                    "title": note["title"][:34],
                    "area": note["area"],
                    "words": 0,
                    "sentences": 0,
                    "unique_vocab": 0,
                    "lex_density_%": 0,
                    "avg_sent_len": 0,
                    "read_min": 0.0,
                    "fk_grade": "—",
                    "wikilinks": wlinks,
                    "maturity": "STUB",
                }
            )
            continue

        sentences = nltk.sent_tokenize(text)
        words_raw = nltk.word_tokenize(text)
        words = [w for w in words_raw if w.isalpha()]
        unique = set(w.lower() for w in words)
        content_words = [w for w in words if w.lower() not in stopwords]
        lex_density = (
            round(len(content_words) / len(words) * 100, 1) if words else 0
        )
        avg_sent = round(len(words) / len(sentences), 1) if sentences else 0
        read_min = round(len(words) / 200, 1)
        fk = flesch_kincaid_grade(words, sentences)

        if len(words) < 50:
            maturity = "STUB"
        elif len(words) < 250:
            maturity = "SEED"
        elif len(words) < 700:
            maturity = "BUDDING"
        else:
            maturity = "EVERGREEN"

        results.append(
            {
                "pub": pub_flag,
                "path": note["path"][:45],
                "title": note["title"][:34],
                "area": note["area"],
                "words": len(words),
                "sentences": len(sentences),
                "unique_vocab": len(unique),
                "lex_density_%": lex_density,
                "avg_sent_len": avg_sent,
                "read_min": read_min,
                "fk_grade": round(fk, 1),
                "wikilinks": wlinks,
                "maturity": maturity,
            }
        )
    return results


def print_report(results: list[dict]) -> None:
    rows_sorted = sorted(results, key=lambda r: r["words"], reverse=True)

    headers = [
        "P", "Path", "Title", "Area",
        "Words", "Sents", "Vocab", "LexDen%",
        "AvgSL", "Read(m)", "FK", "Links", "Maturity"
    ]
    rows = [
        [
            r["pub"], r["path"], r["title"], r["area"],
            r["words"], r["sentences"], r["unique_vocab"],
            r["lex_density_%"], r["avg_sent_len"], r["read_min"],
            r["fk_grade"], r["wikilinks"], r["maturity"],
        ]
        for r in rows_sorted
    ]

    pub_count = sum(1 for r in results if r["pub"] == "✓")
    print("\n" + "═" * 110)
    print(f"  TEXT STATS — karx.github.io vault  "
          f"({len(results)} notes total · {pub_count} published · "
          f"{len(results)-pub_count} unpublished)")
    print("  P = published in garden  |  sorted by word count desc")
    print("═" * 110)
    print(tabulate(rows, headers=headers, tablefmt="rounded_outline"))

    total_words = sum(r["words"] for r in results)
    total_links = sum(r["wikilinks"] for r in results)
    for maturity in ("STUB", "SEED", "BUDDING", "EVERGREEN"):
        subset = [r for r in results if r["maturity"] == maturity]
        pub_in = sum(1 for r in subset if r["pub"] == "✓")
        print(f"  {maturity:10s}: {len(subset):3d} notes  "
              f"({pub_in} published, {len(subset)-pub_in} unpublished)")

    # Areas with the most unpublished EVERGREEN content
    unpub_eg = [r for r in results if r["maturity"] == "EVERGREEN" and r["pub"] == " "]
    if unpub_eg:
        print(f"\n  ── Unpublished EVERGREEN notes (publish candidates) ──")
        for r in sorted(unpub_eg, key=lambda x: x["words"], reverse=True)[:15]:
            print(f"    {r['words']:5d}w  [{r['area']:20s}]  {r['path']}")

    print(f"\n  Total words    : {total_words:,}")
    print(f"  Total wikilinks: {total_links}")
    print()


if __name__ == "__main__":
    import sys
    mode = sys.argv[1] if len(sys.argv) > 1 else "all"
    print(f"Loading vault ({mode}) …")
    notes = load_published_notes() if mode == "published" else load_all_notes()
    results = analyse(notes)
    print_report(results)
