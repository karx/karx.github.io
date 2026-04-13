"""
vault_loader.py
---------------
Shared utility: walks the vault, parses frontmatter + body.
Returns ALL notes by default; optionally filtered to published-only.

Skipped always:
  - Hidden directories (.git, .obsidian, .gemini, …)
  - node_modules/
  - _site/ build output
  - *.excalidraw.md  (Excalidraw drawing files — binary-ish, not prose)
  - Abbreviations/trends/ (npm package READMEs from a dependency)
"""

import os
import re
from pathlib import Path

VAULT_ROOT = Path(__file__).resolve().parents[2]  # karx.github.io/

# Directories to always skip (matched against each dir name)
_SKIP_DIRS: set[str] = {"node_modules", "_site", "Abbreviations"}

# Strip YAML frontmatter block
_FM_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
# Strip YAML list items (tags block)
_YAML_LIST_RE = re.compile(r"^\s*-\s+", re.MULTILINE)
# First H1 heading
_H1_RE = re.compile(r"^#\s+(.+)$", re.MULTILINE)
# Obsidian WikiLinks [[target|alias]] → alias or target
_WIKI_RE = re.compile(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]")
# Standard Markdown links / images
_MD_LINK_RE = re.compile(r"!?\[([^\]]*)\]\([^)]*\)")
# HTML tags
_HTML_RE = re.compile(r"<[^>]+>")
# Fenced code blocks
_CODE_RE = re.compile(r"```.*?```", re.DOTALL)
_INLINE_CODE_RE = re.compile(r"`[^`]+`")
# Markdown syntax punctuation (headings, bold, italic, etc.)
_MD_SYNTAX_RE = re.compile(r"[#*_>~`|\\]")
# Bare URLs
_URL_RE = re.compile(r"https?://\S+")


def _parse_frontmatter(text: str) -> tuple[dict, str]:
    """Return (frontmatter_dict, body_text).

    Handles simple scalar values AND YAML list blocks like:
        tags:
          - foo
          - bar
    For list fields the returned value is the raw multi-line string;
    callers that need a list can split on newlines / dashes themselves.
    """
    m = _FM_RE.match(text)
    if not m:
        return {}, text

    fm: dict = {}
    current_key: str | None = None
    list_lines: list[str] = []

    for line in m.group(1).splitlines():
        if re.match(r"^\s*-\s+", line):
            # List continuation
            if current_key:
                list_lines.append(re.sub(r"^\s*-\s+", "", line).strip())
        elif ":" in line and not line.startswith(" "):
            # Flush previous list
            if current_key and list_lines:
                fm[current_key] = list_lines
                list_lines = []
            k, _, v = line.partition(":")
            current_key = k.strip()
            val = v.strip().strip('"').strip("'")
            if val:
                fm[current_key] = val
                current_key = None  # scalar — done
        else:
            list_lines = []
            current_key = None

    if current_key and list_lines:
        fm[current_key] = list_lines

    return fm, text[m.end():]


def _infer_title(fm: dict, body: str, path_parts: list[str]) -> str:
    """Best-effort title: frontmatter → first H1 → last path component."""
    if "title" in fm:
        return str(fm["title"])
    h1 = _H1_RE.search(body)
    if h1:
        return h1.group(1).strip()
    return path_parts[-1] if path_parts else "untitled"


def _clean_body(body: str) -> str:
    """Strip all markup; return plain text suitable for NLP."""
    text = _CODE_RE.sub(" ", body)
    text = _INLINE_CODE_RE.sub(" ", text)
    text = _HTML_RE.sub(" ", text)
    text = _URL_RE.sub(" ", text)
    text = _WIKI_RE.sub(lambda m: m.group(2) or m.group(1), text)
    text = _MD_LINK_RE.sub(r"\1", text)
    text = _MD_SYNTAX_RE.sub(" ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def _build_slug(parts: list[str]) -> str:
    """Mirror the slug logic in build-garden.mjs."""
    return "--".join(
        re.sub(r"[^a-z0-9]+", "-", p.lower()).strip("-")
        for p in parts
    ) or "about"


def _should_skip_file(fpath: Path) -> bool:
    """True for files that carry no prose worth analysing."""
    name = fpath.name
    if name.endswith(".excalidraw.md"):
        return True
    if name in {"CODE_OF_CONDUCT.md", "Gemfile"}:
        return True
    return False


def _note_from_path(fpath: Path) -> dict | None:
    """Parse a single file and return a note dict, or None on failure."""
    try:
        raw = fpath.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return None

    if not raw.strip():
        return None  # skip truly empty files

    fm, body = _parse_frontmatter(raw)
    published = str(fm.get("published", "false")).lower() == "true"

    rel = fpath.relative_to(VAULT_ROOT)
    parts = list(rel.parts)

    # Slug-building: drop README.md suffix, strip .md from leaf
    slug_parts = list(parts)
    if slug_parts[-1].lower() == "readme.md":
        slug_parts = slug_parts[:-1]
    else:
        slug_parts[-1] = slug_parts[-1][:-3]

    # Human-readable path parts for title inference
    display_parts = list(slug_parts)

    title = _infer_title(fm, body, display_parts)

    # Tags: may be scalar string or list
    raw_tags = fm.get("tags", [])
    if isinstance(raw_tags, list):
        tags = raw_tags
    elif raw_tags:
        tags = [raw_tags]
    else:
        tags = []

    clean = _clean_body(body)

    # Infer project / area from top-level folder
    area = parts[0] if len(parts) > 1 else "root"

    return {
        "slug": _build_slug(slug_parts),
        "path": str(rel),
        "area": area,
        "title": title,
        "tags": tags,
        "description": str(fm.get("description", "")),
        "date": str(fm.get("date", "")),
        "published": published,
        "raw_body": body,
        "clean_text": clean,
    }


# ── public API ──────────────────────────────────────────────────────────────

def load_all_notes() -> list[dict]:
    """Return every prose .md file in the vault, published or not."""
    notes = []
    for root, dirs, files in os.walk(VAULT_ROOT):
        # Prune skipped directories in-place (affects os.walk descent)
        dirs[:] = sorted(
            d for d in dirs
            if not d.startswith(".") and d not in _SKIP_DIRS
        )
        for fname in files:
            if not fname.endswith(".md"):
                continue
            fpath = Path(root) / fname
            if _should_skip_file(fpath):
                continue
            note = _note_from_path(fpath)
            if note:
                notes.append(note)

    notes.sort(key=lambda n: n["path"])
    return notes


def load_published_notes() -> list[dict]:
    """Return only notes with published: true (backwards-compat shim)."""
    return [n for n in load_all_notes() if n["published"]]


if __name__ == "__main__":
    import sys
    mode = sys.argv[1] if len(sys.argv) > 1 else "all"
    notes = load_published_notes() if mode == "published" else load_all_notes()
    pub = sum(1 for n in notes if n["published"])
    unpub = sum(1 for n in notes if not n["published"])
    print(f"Found {len(notes)} notes  ({pub} published · {unpub} unpublished)")
    for n in notes:
        flag = "✓" if n["published"] else " "
        print(f"  [{flag}] {n['area']:20s}  {n['path']}")
