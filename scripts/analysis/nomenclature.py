"""
nomenclature.py
---------------
Structural analysis using folder paths and naming conventions as primary signals.
Content is intentionally ignored — the shape of the vault reveals the taxonomy.

Naming format → semantic layer signal:
  PascalCase   → L3 Principle / named concept  (WebGraph, KartaDharam, Wikidata)
  camelCase    → L2 System / product            (homeSwitch, publicPulse, AdEngine)
  kebab-case   → L2 System / tech artefact      (face-demo, rf-proto, web-bash)
  lowercase    → L3 Principle / concept         (computeTheory, simulation, banaao)
  UPPER/ABBREV → L3 Principle / shorthand       (ESP, DRI, mqtt)
  NumberPrefix → Cohort / event-bound           (91Boys, 91noida, 15Aug)
  DatePattern  → Archival / temporal            (2024-07-22, Summer19, mozfest21)
  PersonName   → Identity / reference           (rachit03, ashtam, Zsolt, kaaro)
  SentenceCase → L1 Essay / reflection          (Interface Patterns.md, Age of Empires.md)

Run: python3 scripts/analysis/nomenclature.py
"""

import re
import os
from pathlib import Path
from collections import defaultdict

sys_path_parent = str(Path(__file__).parent)
import sys
sys.path.insert(0, sys_path_parent)
from vault_loader import VAULT_ROOT, _SKIP_DIRS

# ── Naming format classifiers ────────────────────────────────────────────────

def _name_format(name: str) -> str:
    """Classify a folder/file stem by its naming convention."""
    # Remove extension
    stem = re.sub(r"\.(md|html)$", "", name)
    if not stem:
        return "empty"
    # Date patterns
    if re.match(r"^\d{4}-\d{2}-\d{2}$", stem):
        return "ISO-date"
    if re.match(r"^(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\w*\d*$", stem, re.I):
        return "month-name"
    if re.match(r"^\d{2}[A-Z][a-z]+", stem):
        return "DateName"  # 15Aug, 26January
    # Number prefix (cohort/series)
    if re.match(r"^\d{2}[A-Za-z]", stem):
        return "NumberPrefix"  # 91Boys, 91noida
    # ALL CAPS / abbreviation
    if stem.isupper() and len(stem) <= 5:
        return "ABBREV"
    # camelCase (starts lower, has upper inside)
    if re.match(r"^[a-z]+[A-Z]", stem):
        return "camelCase"
    # PascalCase (starts upper, mix of case)
    if re.match(r"^[A-Z][a-z]+[A-Z]", stem):
        return "PascalCase"
    # Title case single word
    if re.match(r"^[A-Z][a-z]+$", stem):
        return "Proper"
    # kebab-case
    if "-" in stem and stem.islower():
        return "kebab-case"
    # underscore_case
    if "_" in stem:
        return "snake_case"
    # Space-separated (file names)
    if " " in stem:
        return "SentenceCase"
    # Pure lowercase
    if stem.islower():
        return "lowercase"
    # Mixed / other
    return "mixed"


def _layer_from_format(fmt: str) -> str:
    """Map naming format to likely vertical layer."""
    return {
        "ISO-date":    "L1-Archival",
        "DateName":    "L1-Archival",
        "month-name":  "L1-Archival",
        "NumberPrefix":"L1-Cohort",
        "ABBREV":      "L3-Principle",
        "camelCase":   "L2-System",
        "PascalCase":  "L3-Principle",
        "kebab-case":  "L2-System",
        "snake_case":  "L2-System",
        "SentenceCase":"L1-Essay",
        "lowercase":   "L3-Principle",
        "Proper":      "L3-Principle",
        "mixed":       "L1-Instance",
        "empty":       "L1-Instance",
    }.get(fmt, "L1-Instance")


# ── Prefix / suffix family detection ────────────────────────────────────────

_PREFIX_FAMILIES: dict[str, list[str]] = {}

def _detect_families(names: list[str]) -> dict[str, list[str]]:
    """Group names that share a 3+-char prefix."""
    families: dict[str, list[str]] = defaultdict(list)
    # Explicit known families
    known = {
        "kaaro":  "kaaro-brand",
        "wendor": "wendor-brand",
        "91":     "91-cohort",
        "web":    "web-tech",
        "smart":  "smart-devices",
        "hack":   "hackathon",
        "stream": "streaming",
        "Wikidata": "wikidata-community",
    }
    for name in names:
        for prefix, family in known.items():
            if name.lower().startswith(prefix.lower()):
                families[family].append(name)
    return dict(families)


# ── Hindi / cultural vocabulary detection ───────────────────────────────────

_HINDI_STEMS = {
    "banaao":       ("बनाओ", "imperative: build / make"),
    "kaaro":        ("करो",  "imperative: do / make"),
    "KartaDharam":  ("कर्तव्य", "duty of the doer"),
    "Akriya":       ("अक्रिया", "action / agency"),
    "dlfmoi":       ("DLFMOI", "Delhi For Makers of India (acronym)"),
    "holi":         ("होली", "cultural festival"),
    "neelaneel":    ("नीलनील", "personal name (deep blue)"),
    "ashtam":       ("अष्टम", "personal name (eighth)"),
    "ego-Field":    ("ego-क्षेत्र", "concept from Indian philosophy"),
}


# ── Internal structure pattern detection ────────────────────────────────────

_STRUCTURAL_PATTERNS = {
    r"Week-\d+|Week-n":   "week-sprint",      # homeSwitch, YTKrta
    r"day-\d+|day\d":     "day-intensive",     # dlfmoi
    r"status-\d+|status-n":"status-update",    # AdEngine
    r"update-[A-Z\d]+":   "versioned-update",  # YTKrta/update-A
    r"v\d+":              "versioned-release",  # homeSwitch/v2
    r"sow$":              "SOW-leaf",           # face-demo/events/sow
    r"TR$":               "tech-report",        # YTKrta/TR, wendorEvents/TR
    r"history$":          "archival-timeline",  # WebComponents/history
    r"mail/to-":          "correspondence",     # kaaro/mail/to-*
    r"requirements$|specs$|Specs$": "spec-doc",# SmartBike/Specs, /requirements
    r"delivery$":         "delivery-doc",       # SmartBike/delivery
    r"hire/":             "recruitment",        # hire/frontend, /graphic
    r"sharable|sharable": "shareable-asset",    # minecraft/sharable
}


def _detect_structural_pattern(path_str: str) -> str | None:
    for pattern, label in _STRUCTURAL_PATTERNS.items():
        if re.search(pattern, path_str):
            return label
    return None


# ── Cluster definitions from naming alone ───────────────────────────────────

NAMING_CLUSTERS = {
    "kaaro-brand": {
        "anchor": "kaaro/README.md",
        "members": ["kaaroCatalogue.md", "kaaroClips/README.md",
                    "kaaroGazette", "kaaroStream/README.md"],
        "description": "Personal brand identity — the 'kaaro' product family",
        "wiki_hub": "[[kaaro]]",
    },
    "wendor-brand": {
        "anchor": "wendorMandir/README.md",
        "members": ["wendorEvents/TR/README.md", "wendorWorkshop/README.md"],
        "description": "Client brand family — wendor platform products",
        "wiki_hub": "[[wendorMandir]]",
    },
    "91-cohort": {
        "anchor": "91s-welcome/README.md",
        "members": ["91Boys/README.md", "91noida/DS/README.md"],
        "description": "91springboard ecosystem — community, cohort, NCR events",
        "wiki_hub": "[[91s-welcome]]",
    },
    "IoT-stack": {
        "anchor": "ESP/README.md",
        "members": ["homeSwitch/README.md", "SmartBike/README.md",
                    "rf-proto/README.md", "GymVym/README.md",
                    "KartaDharam/README.md", "mqtt/convention/README.md",
                    "platform.io/README.md"],
        "description": "Hardware + firmware ecosystem anchored on ESP32",
        "wiki_hub": "[[ESP]]",
    },
    "face-vision": {
        "anchor": "face-demo/events/sow/README.md",
        "members": ["facebox/box.md", "hands/hand-1142/README.md",
                    "vision-aid/final/README.md", "ESP/ESP-eye/README.md"],
        "description": "Computer vision product family (face, hands, accessibility)",
        "wiki_hub": "[[face-demo]]",
    },
    "streaming-content": {
        "anchor": "YTKrta/README.md",
        "members": ["kaaroStream/README.md", "kaaroClips/README.md",
                    "streaming/README.md", "twitch/lookups/README.md",
                    "vidiyo/README.md", "Contentx22/README.md"],
        "description": "Streaming, content creation, and IoT merchandise for creators",
        "wiki_hub": "[[YTKrta]]",
    },
    "knowledge-graph": {
        "anchor": "WebGraph/README.md",
        "members": ["Wikidata/README.md", "computeTheory/README.md",
                    "simulation/README.md", "dbpedia/README.md",
                    "digital-gardener/references/guidelines.md"],
        "description": "Structured data, semantic web, and personal knowledge graph",
        "wiki_hub": "[[WebGraph]]",
    },
    "wikidata-community": {
        "anchor": "Wikidata/README.md",
        "members": ["Wikidata/WikidataIndia/README.md",
                    "Wikidata/devConf/README.md",
                    "Wikidata/pyDelhi/README.md",
                    "advocates/moz-cohort/README.md",
                    "advocates/fdp-IoT/README.md",
                    "mozfest21/README.md"],
        "description": "Open data advocacy events and community contributions",
        "wiki_hub": "[[Wikidata]]",
    },
    "manifesto-ideas": {
        "anchor": "Manifesto/README.md",
        "members": ["Manifesto/dapp/README.md", "Manifesto/questEd/README.md",
                    "Manifesto/shareuniverse/README.md", "Manifesto/opposite/README.md"],
        "description": "Philosophical experiments and speculative tech ideas",
        "wiki_hub": "[[Manifesto]]",
    },
    "venture-portfolio": {
        "anchor": "Akriya/homeDoc/README.md",
        "members": ["rachit03/README.md", "AdEngine/README.md",
                    "publicPulse/README.md", "showtime/README.md",
                    "cars24/README.md", "spoilageResearch/README.md",
                    "banaao/ifttt/README.md"],
        "description": "Akriya client work and startup ventures",
        "wiki_hub": "[[Akriya]]",
    },
}


# ── Main analysis ────────────────────────────────────────────────────────────

def analyse_structure() -> dict:
    """Walk vault collecting naming metadata for each folder."""
    results: list[dict] = []

    for root, dirs, files in os.walk(VAULT_ROOT):
        dirs[:] = sorted(
            d for d in dirs
            if not d.startswith(".") and d not in _SKIP_DIRS
        )
        rpath = Path(root)
        rel = rpath.relative_to(VAULT_ROOT)
        parts = list(rel.parts)
        depth = len(parts)

        if depth == 0:
            # Root .md files
            for fname in files:
                if not fname.endswith(".md"):
                    continue
                if fname in {"CODE_OF_CONDUCT.md", "Gemfile"}:
                    continue
                stem = fname[:-3]
                fmt = _name_format(fname)
                results.append({
                    "path": fname,
                    "depth": 0,
                    "name": stem,
                    "format": fmt,
                    "layer": _layer_from_format(fmt),
                    "struct": None,
                    "type": "loose-file",
                })
        else:
            # Record the folder itself
            folder_name = parts[-1]
            fmt = _name_format(folder_name)
            struct = _detect_structural_pattern(str(rel))
            results.append({
                "path": str(rel),
                "depth": depth,
                "name": folder_name,
                "format": fmt,
                "layer": _layer_from_format(fmt),
                "struct": struct,
                "type": "folder",
            })

    return results


def print_report(results: list[dict]) -> None:
    from tabulate import tabulate

    # ── Section 1: Naming format distribution ──────────────────────────────
    print("\n" + "═" * 110)
    print("  NOMENCLATURE ANALYSIS — karx.github.io vault")
    print("  Primary signal: folder/file names  ·  Content intentionally ignored")
    print("═" * 110)

    fmt_counts: dict[str, int] = defaultdict(int)
    for r in results:
        fmt_counts[r["format"]] += 1

    layer_counts: dict[str, int] = defaultdict(int)
    for r in results:
        layer_counts[r["layer"]] += 1

    print("\n  ── FORMAT DISTRIBUTION ───────────────────────────────────────────────")
    rows = sorted(fmt_counts.items(), key=lambda x: -x[1])
    for fmt, cnt in rows:
        bar = "█" * cnt
        layer = _layer_from_format(fmt)
        print(f"  {fmt:20s}  {bar:40s}  {cnt:3d}  →  {layer}")

    # ── Section 2: Layer signal from naming ──────────────────────────────
    print("\n  ── LAYER SIGNALS FROM NAME FORMAT ────────────────────────────────────")
    for layer, cnt in sorted(layer_counts.items(), key=lambda x: -x[1]):
        bar = "█" * min(cnt, 50)
        print(f"  {layer:20s}  {bar}  ({cnt})")

    # ── Section 3: Naming family clusters ────────────────────────────────
    print("\n  ── NAMING FAMILY CLUSTERS ────────────────────────────────────────────")
    all_names = [r["name"] for r in results]
    families = _detect_families(all_names)
    for family, members in families.items():
        print(f"\n  [{family}]  ({len(members)} members)")
        for m in members[:10]:
            print(f"    · {m}")

    # ── Section 4: Structural patterns ───────────────────────────────────
    print("\n  ── STRUCTURAL PATTERNS INSIDE PROJECTS ──────────────────────────────")
    struct_counts: dict[str, list[str]] = defaultdict(list)
    for r in results:
        if r["struct"]:
            struct_counts[r["struct"]].append(r["path"])
    for pattern, paths in sorted(struct_counts.items(), key=lambda x: -len(x[1])):
        print(f"\n  {pattern}  ({len(paths)} occurrences)")
        for p in paths[:8]:
            print(f"    · {p}")

    # ── Section 5: Hindi/cultural vocabulary ─────────────────────────────
    print("\n  ── HINDI / CULTURAL VOCABULARY LAYER ────────────────────────────────")
    print("  These names carry intentional cultural framing — not arbitrary labels\n")
    for stem, (devanagari, meaning) in _HINDI_STEMS.items():
        print(f"  {stem:20s}  {devanagari:12s}  {meaning}")

    # ── Section 6: Naming cluster prescriptions ───────────────────────────
    print("\n" + "═" * 110)
    print("  NAMING CLUSTER PRESCRIPTIONS")
    print("  WikiLinks that should exist based purely on naming family membership")
    print("═" * 110)
    for cluster_name, cluster in NAMING_CLUSTERS.items():
        print(f"\n  [{cluster_name.upper()}]  {cluster['description']}")
        print(f"  Anchor: {cluster['anchor']}   Hub: {cluster['wiki_hub']}")
        print(f"  Members:")
        for m in cluster["members"]:
            print(f"    → {m}")

    # ── Section 7: Deep folder projects (structure as signal) ─────────────
    print("\n  ── PROJECTS WITH RICH INTERNAL STRUCTURE (≥ 4 sub-paths) ───────────")
    folder_children: dict[str, int] = defaultdict(int)
    for r in results:
        parts = r["path"].split("/")
        if len(parts) >= 2:
            folder_children[parts[0]] += 1
    deep = [(k, v) for k, v in folder_children.items() if v >= 4]
    deep.sort(key=lambda x: -x[1])
    for folder, count in deep:
        print(f"  {folder:30s}  {count:3d} sub-paths")

    # ── Section 8: Anomalies (naming inconsistencies) ─────────────────────
    print("\n  ── NAMING ANOMALIES ──────────────────────────────────────────────────")
    # Files/folders at root that have unusual formats compared to peers
    root_items = [r for r in results if r["depth"] == 0 or r["depth"] == 1]
    anomalies = [r for r in root_items if r["format"] in ("ISO-date", "DateName", "mixed", "empty")]
    for r in anomalies[:20]:
        print(f"  [{r['format']:15s}] {r['path']}")

    print()


if __name__ == "__main__":
    results = analyse_structure()
    print_report(results)
