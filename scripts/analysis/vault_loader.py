"""
vault_loader.py
---------------
Shared utility: walks the vault, parses frontmatter + body,
returns only published notes.  Used by all three analysis scripts.
"""

import os
import re
from pathlib import Path

VAULT_ROOT = Path(__file__).resolve().parents[2]  # karx.github.io/

# Strip YAML frontmatter block
_FM_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
# Strip Obsidian WikiLinks [[target|alias]] → alias or target
_WIKI_RE = re.compile(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]")
# Strip markdown images / standard links
_MD_LINK_RE = re.compile(r"!?\[([^\]]*)\]\([^)]*\)")
# Strip HTML tags
_HTML_RE = re.compile(r"<[^>]+>")
# Strip code blocks
_CODE_RE = re.compile(r"```.*?```", re.DOTALL)
_INLINE_CODE_RE = re.compile(r"`[^`]+`")
# Strip headings markers, bold/italic punctuation
_MD_SYNTAX_RE = re.compile(r"[#*_>~`|\\]")


def _parse_frontmatter(text: str) -> tuple[dict, str]:
    """Return (frontmatter_dict, body_text)."""
    m = _FM_RE.match(text)
    if not m:
        return {}, text
    fm: dict = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, _, v = line.partition(":")
            fm[k.strip()] = v.strip().strip('"').strip("'")
    body = text[m.end():]
    return fm, body


def _clean_body(body: str) -> str:
    """Strip all markup; return plain text suitable for NLP."""
    text = _CODE_RE.sub(" ", body)
    text = _INLINE_CODE_RE.sub(" ", text)
    text = _HTML_RE.sub(" ", text)
    text = _WIKI_RE.sub(lambda m: m.group(2) or m.group(1), text)
    text = _MD_LINK_RE.sub(r"\1", text)
    text = _MD_SYNTAX_RE.sub(" ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def load_published_notes() -> list[dict]:
    """
    Yield dicts with keys:
        slug, path, title, tags, description, date,
        raw_body, clean_text
    for every note with published: true.
    """
    notes = []
    for root, dirs, files in os.walk(VAULT_ROOT):
        # Skip hidden dirs and node_modules
        dirs[:] = [
            d for d in dirs
            if not d.startswith(".") and d != "node_modules"
        ]
        for fname in files:
            if not fname.endswith(".md"):
                continue
            fpath = Path(root) / fname
            try:
                text = fpath.read_text(encoding="utf-8", errors="replace")
            except Exception:
                continue
            fm, body = _parse_frontmatter(text)
            if fm.get("published", "").lower() != "true":
                continue

            # Build slug the same way build-garden.mjs does
            rel = fpath.relative_to(VAULT_ROOT)
            parts = list(rel.parts)
            if parts[-1].lower() == "readme.md":
                parts = parts[:-1]
            else:
                parts[-1] = parts[-1][:-3]  # strip .md
            slug = "--".join(
                re.sub(r"[^a-z0-9]+", "-", p.lower()).strip("-")
                for p in parts
            ) or "about"

            clean = _clean_body(body)
            notes.append(
                {
                    "slug": slug,
                    "path": str(fpath.relative_to(VAULT_ROOT)),
                    "title": fm.get("title", parts[-1] if parts else slug),
                    "tags": fm.get("tags", ""),
                    "description": fm.get("description", ""),
                    "date": fm.get("date", ""),
                    "raw_body": body,
                    "clean_text": clean,
                }
            )
    notes.sort(key=lambda n: n["slug"])
    return notes


if __name__ == "__main__":
    notes = load_published_notes()
    print(f"Found {len(notes)} published notes")
    for n in notes:
        print(f"  [{n['slug']}]  {n['path']}")
