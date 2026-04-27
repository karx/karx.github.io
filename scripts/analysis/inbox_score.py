#!/usr/bin/env python3
"""
inbox_score.py — eBrain Inbox Prioritisation
=============================================
Scores notes found in Inbox/ and 0_Inbox/ folders using a
three-dimensional quality signal:

  score = name_quality (×0.4) + frontmatter_bonus (×0.3) + maturity (×0.3)

  name_quality:
    "Untitled" / "Untitled N"           → 0.0  (no signal whatsoever)
    Single generic word                  → 0.3
    Multi-word descriptive name          → 0.7
    Named + date or context marker       → 1.0

  frontmatter_bonus:
    Has frontmatter with published field → 1.0  (already partially processed)
    Has frontmatter, no published field  → 0.7
    No frontmatter at all               → 0.0

  maturity (word count, excluding frontmatter block):
    STUB      < 50w   → 0.1
    SEED      50–249w → 0.4
    BUDDING   250–699w→ 0.7
    EVERGREEN ≥700w   → 1.0

Usage:
  python inbox_score.py --vault d:/src/ebrain
  python inbox_score.py --vault d:/src/ebrain --output report.md
  python inbox_score.py --vault d:/src/ebrain --top 10
"""

import argparse
import re
import sys
from collections import Counter
from dataclasses import dataclass, field
from datetime import date, datetime
from pathlib import Path


# ── Weights ───────────────────────────────────────────────────────────────────
W_NAME        = 0.4
W_FRONTMATTER = 0.3
W_MATURITY    = 0.3

# ── Maturity word-count thresholds ────────────────────────────────────────────
STUB_MAX    = 50
SEED_MAX    = 249
BUDDING_MAX = 699
# ≥ 700 → EVERGREEN

# ── ANSI colours (disabled on Windows if not supported) ──────────────────────
try:
    import colorama
    colorama.init()
    GREEN  = '\033[92m'
    YELLOW = '\033[93m'
    CYAN   = '\033[96m'
    DIM    = '\033[2m'
    RESET  = '\033[0m'
    BOLD   = '\033[1m'
except ImportError:
    GREEN = YELLOW = CYAN = DIM = RESET = BOLD = ''


# ─────────────────────────────────────────────────────────────────────────────
# Data model
# ─────────────────────────────────────────────────────────────────────────────

@dataclass
class NoteScore:
    path: Path
    words: int
    has_frontmatter: bool
    has_published: bool
    name_quality: float
    frontmatter_score: float
    maturity_score: float
    total: float
    maturity_label: str

    @property
    def name(self) -> str:
        return self.path.name


# ─────────────────────────────────────────────────────────────────────────────
# Scoring functions
# ─────────────────────────────────────────────────────────────────────────────

def count_words(text: str) -> int:
    """Count words, stripping the YAML frontmatter block first."""
    text = re.sub(r'^---\s*\n.*?\n---\s*\n', '', text, flags=re.DOTALL)
    return len(text.split())


def score_name(filename: str) -> float:
    """
    Derive a quality signal from the filename alone.
    The stem is what matters — extension is ignored.
    """
    stem = Path(filename).stem.strip()

    # Untitled variants → no signal
    if re.match(r'^[Uu]ntitled(\s*\d+)?$', stem):
        return 0.0

    words = re.split(r'[\s\-_]+', stem)
    words = [w for w in words if w]  # drop empties

    # Single-token → weak signal
    if len(words) <= 1:
        return 0.3

    # Contains a date-like token → strong signal (structured capture)
    if re.search(r'\d{4}[-/]\d{2}[-/]\d{2}|\d{4}-\d{2}|\d{8}', stem):
        return 1.0

    # Multi-word descriptive name → good signal
    return 0.7


def score_frontmatter(text: str) -> tuple[bool, bool, float]:
    """
    Detect YAML frontmatter and the presence of a `published:` field.
    Returns (has_frontmatter, has_published, score).
    """
    has_frontmatter = bool(re.match(r'^---\s*\n', text))
    has_published   = bool(re.search(r'^published\s*:', text, re.MULTILINE))

    if has_frontmatter and has_published:
        score = 1.0
    elif has_frontmatter:
        score = 0.7
    else:
        score = 0.0

    return has_frontmatter, has_published, score


def score_maturity(word_count: int) -> tuple[str, float]:
    """Map word count to (maturity_label, score)."""
    if word_count < STUB_MAX:
        return 'STUB', 0.1
    elif word_count <= SEED_MAX:
        return 'SEED', 0.4
    elif word_count <= BUDDING_MAX:
        return 'BUDDING', 0.7
    else:
        return 'EVERGREEN', 1.0


def score_note(path: Path) -> NoteScore:
    """Score a single .md file and return a NoteScore."""
    try:
        text = path.read_text(encoding='utf-8', errors='replace')
    except Exception:
        text = ''

    words         = count_words(text)
    name_q        = score_name(path.name)
    has_fm, has_pub, fm_score = score_frontmatter(text)
    maturity_label, mat_score = score_maturity(words)

    total = round(
        (name_q * W_NAME) + (fm_score * W_FRONTMATTER) + (mat_score * W_MATURITY),
        3,
    )

    return NoteScore(
        path=path,
        words=words,
        has_frontmatter=has_fm,
        has_published=has_pub,
        name_quality=name_q,
        frontmatter_score=fm_score,
        maturity_score=mat_score,
        total=total,
        maturity_label=maturity_label,
    )


# ─────────────────────────────────────────────────────────────────────────────
# Discovery
# ─────────────────────────────────────────────────────────────────────────────

INBOX_FOLDERS = ['Inbox', '0_Inbox', 'inbox', '_inbox']

def find_inbox_notes(vault: Path) -> list[Path]:
    """Find all .md files inside any recognised inbox folder in the vault."""
    notes: list[Path] = []
    for folder_name in INBOX_FOLDERS:
        folder = vault / folder_name
        if folder.exists() and folder.is_dir():
            for f in sorted(folder.glob('**/*.md')):
                notes.append(f)
    return notes


# ─────────────────────────────────────────────────────────────────────────────
# Rendering
# ─────────────────────────────────────────────────────────────────────────────

MATURITY_ICON = {
    'EVERGREEN': '🌳',
    'BUDDING':   '🌿',
    'SEED':      '🌱',
    'STUB':      '🪨',
}

def maturity_colour(label: str) -> str:
    return {
        'EVERGREEN': GREEN,
        'BUDDING':   CYAN,
        'SEED':      YELLOW,
        'STUB':      DIM,
    }.get(label, '')


def render_markdown_table(scores: list[NoteScore], vault: Path) -> str:
    """Render a GitHub-Flavoured Markdown table."""
    header = (
        "| Score | File | Words | Maturity | FM | Published |\n"
        "|------:|------|------:|----------|----|-----------|"
    )
    rows = []
    for s in scores:
        rel     = s.path.relative_to(vault)
        fm_tick = '✓' if s.has_frontmatter else '✗'
        pb_tick = '✓' if s.has_published  else '✗'
        icon    = MATURITY_ICON.get(s.maturity_label, '')
        rows.append(
            f"| {s.total:.2f} | `{rel}` | {s.words} "
            f"| {icon} {s.maturity_label} | {fm_tick} | {pb_tick} |"
        )
    return header + '\n' + '\n'.join(rows)


def print_console_table(scores: list[NoteScore], vault: Path) -> None:
    """Print a coloured summary table to stdout."""
    col_w = 48
    header = (
        f"{'SCORE':>6}  {'MATURITY':<10}  {'FM':>2}  {'WDS':>5}  FILE"
    )
    print(BOLD + header + RESET)
    print('─' * 78)
    for s in scores:
        rel    = str(s.path.relative_to(vault))
        colour = maturity_colour(s.maturity_label)
        icon   = MATURITY_ICON.get(s.maturity_label, '')
        fm     = '✓' if s.has_frontmatter else '✗'
        trunc  = (rel[:col_w - 3] + '...') if len(rel) > col_w else rel
        print(
            f"{colour}{s.total:6.2f}  "
            f"{icon} {s.maturity_label:<9}  {fm:>2}  "
            f"{s.words:>5}  {trunc}{RESET}"
        )


def render_report(scores: list[NoteScore], vault: Path) -> str:
    """Produce the full markdown triage report."""
    dist  = Counter(s.maturity_label for s in scores)
    table = render_markdown_table(scores, vault)

    top_section = '\n'.join(
        f"{i}. **`{s.path.relative_to(vault)}`** "
        f"— score `{s.total:.2f}` · {s.maturity_label} · {s.words}w"
        for i, s in enumerate(scores[:10], 1)
    )

    return f"""---
title: "Inbox Triage Report"
date: {date.today()}
tags: [reference]
description: "Scored inbox queue for eBrain vault. Generated by inbox_score.py."
---

# Inbox Triage Report

> **Vault:** `{vault}`  
> **Notes scored:** {len(scores)}  
> **Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}

---

## Score Formula

```
score = name_quality (×0.4) + frontmatter_bonus (×0.3) + maturity (×0.3)
```

| Dimension | Signal | Score |
|-----------|--------|-------|
| name_quality | Untitled → 0.0 · single-word → 0.3 · descriptive → 0.7 · dated → 1.0 | ×0.4 |
| frontmatter_bonus | none → 0.0 · has FM → 0.7 · has published: → 1.0 | ×0.3 |
| maturity | STUB → 0.1 · SEED → 0.4 · BUDDING → 0.7 · EVERGREEN → 1.0 | ×0.3 |

---

## Maturity Distribution

| Maturity | Count |
|----------|-------|
| 🌳 EVERGREEN | {dist.get('EVERGREEN', 0)} |
| 🌿 BUDDING   | {dist.get('BUDDING', 0)} |
| 🌱 SEED      | {dist.get('SEED', 0)} |
| 🪨 STUB      | {dist.get('STUB', 0)} |

---

## Full Scored Queue

{table}

---

## Top 10 — Process These First

{top_section}
"""


# ─────────────────────────────────────────────────────────────────────────────
# CLI
# ─────────────────────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(
        description='Score eBrain inbox notes for triage priority.',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument('--vault',  required=True, help='Path to vault root')
    parser.add_argument('--output', help='Save full report to this .md file')
    parser.add_argument('--top',    type=int, default=5,
                        help='How many top notes to highlight (default: 5)')
    args = parser.parse_args()

    vault = Path(args.vault).resolve()
    if not vault.exists():
        print(f'ERROR: vault not found: {vault}', file=sys.stderr)
        sys.exit(1)

    notes = find_inbox_notes(vault)
    if not notes:
        print(f'No inbox notes found in {vault}')
        print(f'Looked in: {", ".join(INBOX_FOLDERS)}')
        sys.exit(0)

    scores = sorted(
        [score_note(p) for p in notes],
        key=lambda s: s.total,
        reverse=True,
    )

    # ── Console output ────────────────────────────────────────────────────
    dist = Counter(s.maturity_label for s in scores)
    print(f'\n{BOLD}🌱 eBrain Inbox Score — {vault.name}{RESET}')
    print(f'   {len(scores)} notes across: {", ".join(INBOX_FOLDERS)}\n')

    for label in ['EVERGREEN', 'BUDDING', 'SEED', 'STUB']:
        count  = dist.get(label, 0)
        colour = maturity_colour(label)
        bar    = '█' * count
        icon   = MATURITY_ICON.get(label, '')
        print(f'  {colour}{icon} {label:<10} {bar} ({count}){RESET}')
    print()

    print_console_table(scores, vault)

    print(f'\n{BOLD}🎯 Top {args.top} — Process These First:{RESET}')
    for i, s in enumerate(scores[:args.top], 1):
        rel    = s.path.relative_to(vault)
        colour = maturity_colour(s.maturity_label)
        print(f'  {i}. {colour}[{s.total:.2f}]{RESET}  {rel}  '
              f'{DIM}({s.maturity_label}, {s.words}w){RESET}')

    # ── Optional report file ──────────────────────────────────────────────
    if args.output:
        out = Path(args.output)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(render_report(scores, vault), encoding='utf-8')
        print(f'\n📄 Report saved → {out}')


if __name__ == '__main__':
    main()
