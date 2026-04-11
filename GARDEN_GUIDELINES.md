# Garden Maintainer Guidelines

This document defines the conventions for maintaining the `karx.github.io` vault so it publishes correctly as an interactive 3D knowledge graph on the homepage at `/garden/`.

The build script (`homepage/scripts/build-garden.mjs`) walks this vault, parses frontmatter and `[[WikiLink]]` edges, and emits `garden-graph.json`. Everything in this document determines what ends up in that graph.

**Current graph state (as of 2026-04-12):** 20 published notes · 4 edges · target: 40+ notes, 80+ edges.

---

## 1. What Gets Published

Only notes with `published: true` in their frontmatter appear in the graph. All other notes are invisible to the build script — the vault stays private-first.

```yaml
---
published: true
---
```

That's the minimum. All other fields below enrich the node but are optional.

---

## 2. Frontmatter Spec

```yaml
---
published: true                   # required — gate for public graph
title: "Kaaro Stream"             # optional — fallback order: H1 → folder name → filename
date: 2025-11-02                  # optional — ISO 8601, shown in detail panel
tags:                             # optional — drives cluster grouping and colour
  - streaming
  - mqtt
description: "Notes on the real-time content pipeline bridging speech to knowledge graph."
                                  # optional — fallback: first non-heading paragraph
image: images/kaaro-stream.png    # optional — thumbnail, relative to vault root
---
```

| Field | Type | Missing behaviour |
|-------|------|-------------------|
| `published` | boolean | Note excluded entirely |
| `title` | string | H1 heading → folder name → filename |
| `date` | ISO date | No date shown |
| `tags` | string list | Placed in "untagged" periphery |
| `description` | string | First non-heading paragraph (up to 280 chars) |
| `image` | relative path | No thumbnail on node |

---

## 3. File and Folder Conventions

Two layouts work:

**Single-file note:**
```
MyTopic.md          → slug: "mytopic"
```

**Folder note** (topic with supporting assets):
```
MyTopic/
  README.md         → slug: "mytopic"  (canonical)
  diagram.png
  sub-thought.md    → slug: "mytopic--sub-thought"  (separate node if published)
```

**Special case:** `README.md` at vault root → slug `"about"`.

**Nested notes** get double-dash slugs: `Foo/Bar.md` → `foo--bar`. These are valid graph nodes but rarely show up well in the graph — prefer flat structure or folder notes for content worth publishing.

**Avoid publishing:**
- `Untitled.md`, temp scratch notes
- Folders containing `node_modules/` (build script skips them but sub-notes inside are still walked)
- Notes that are only image dumps (`Pasted Image 20240...`)
- Private context: people's contact details, finances, addresses

---

## 4. WikiLinks — How Edges Are Built

Graph edges come from WikiLinks in note bodies:

```markdown
This builds on [[WebGraph]] and connects to [[kaaroStream]].
```

The build script extracts all `[[...]]` patterns from every published note and attempts to resolve them against the published slug set. Resolved links become directed edges. Unresolved links (target not published or doesn't exist) are silently dropped — no broken edges in the graph.

### Matching rules

| Pattern | Resolves to |
|---------|------------|
| `[[kaaro]]` | slug `kaaro` |
| `[[Kaaro]]` | slug `kaaro` (case-insensitive) |
| `[[kaaro stream]]` | slug `kaaro-stream` (spaces → dashes) |
| `[[kaaro\|the stream project]]` | edge to `kaaro`, alias ignored |
| `[[kaaro#section]]` | edge to `kaaro`, anchor ignored |
| `[text](url)` | not an edge (standard Markdown link) |

Use the folder or file name, not a full path: `[[kaaro]]` not `[[kaaro/README]]`.

### What makes a good graph

The graph is only interesting when nodes have connections. Target:
- Every published note links to at least **2 other published notes**
- Every published note is linked to by at least **1 other published note**
- Average degree ≥ 3 (each node has 3+ connections)

A note with zero links will sit at the periphery of the graph and never get explored.

---

## 5. Tags and Clusters

Tags group nodes into visual clusters in the 3D layout. The graph places same-tag nodes near each other spatially. Use one primary tag that names the cluster, then additional tags for cross-cutting context.

**Established tag taxonomy:**

| Tag | Cluster theme |
|-----|--------------|
| `streaming` | Real-time pipelines, MQTT, event-driven systems |
| `interface` | UI/UX, interaction patterns, web components |
| `iot` | Hardware, microcontrollers, physical computing |
| `knowledge-graph` | Wikidata, ontology, graph databases, structured data |
| `maker` | 3D printing, fabrication, tools, physical builds |
| `startup` | Ventures, products, business experiments |
| `reflection` | Personal essays, longer-form thinking |
| `reference` | Notes that are primarily links and resources |

The primary tag (first in the list) determines the node's cluster colour. All tags appear as pills in the detail panel.

Add new tags sparingly — each new tag creates a new cluster region. Fewer, denser clusters make a better graph than many sparse ones.

---

## 6. Images

Node thumbnails come from the `image:` frontmatter field, pointing to a path relative to the vault root:

```yaml
image: images/kaaro-stream-diagram.png
```

The build script copies this file to `homepage/assets/garden/images/` and rewrites the path to `/assets/garden/images/kaaro-stream-diagram.png`.

Keep image files in the vault-root `images/` folder. Inline Markdown images (`![alt](images/foo.png)`) in the note body are not copied — only `image:` frontmatter values are processed.

---

## 7. What the Detail Panel Shows

When a visitor clicks a node in the 3D graph, they see:

1. **Slug** — the note's ID in the graph
2. **Title** — from `title:` frontmatter or H1
3. **Image** — if `image:` is set
4. **Description** — from `description:` or first paragraph
5. **Tags** — as coloured pills
6. **Last updated** — from `date:` frontmatter
7. **Linked notes** — neighbours via WikiLinks (click to navigate)
8. **"Read full note ↗"** — links to the Jekyll-rendered note page at `/notes/<slug>/`

For a node to feel meaningful:
- Clear `title` or H1 as first line
- `description` of 1–3 sentences
- At least 1 `image:` if the note has a diagram or screenshot worth showing
- 2+ WikiLinks to other published notes

---

## 8. Health Report

After running `npm run build:garden` from the homepage repo, the terminal prints:

```
[garden] Build complete
  Published notes : 42
  Edges           : 87
  Isolated nodes  : 3  ← slug-a, slug-b, slug-c
  Missing targets : 2  ← target-x, target-y
  Untagged nodes  : 1  ← slug-z
  Output          : assets/garden/garden-graph.json
```

**Targets to aim for:**

| Metric | Minimum | Good |
|--------|---------|------|
| Published notes | 20 | 40+ |
| Edges | 30 | 80+ |
| Isolated nodes | < 5 | 0 |
| Missing targets | < 5 | 0 |
| Untagged nodes | 0 | 0 |

**Missing targets** are WikiLinks that point to notes not yet published (or with a typo in the link). Fix by either publishing the target note or correcting the link.

---

## 9. Slug Reference

The build script derives slugs deterministically from file paths. Reference this table if you need to know what ID a note will get in the graph:

| Vault path | Graph slug |
|-----------|-----------|
| `README.md` (vault root) | `about` |
| `WebGraph/README.md` | `webgraph` |
| `kaaroStream/README.md` | `kaarostream` |
| `Manifesto/index.md` → treated as `README.md`? No — only README.md is canonical | `manifesto--index` |
| `Wikidata.md` | `wikidata` |
| `kaaro/README.md` | `kaaro` |
| `WebGraph/rdf-notes.md` | `webgraph--rdf-notes` |

Rules:
1. Lowercase everything
2. Spaces → `-`
3. Non-alphanumeric characters stripped
4. Folder separator → `--`
5. `README.md` at end of path dropped (folder name used instead)
6. Empty result → `about` (for vault root README only)

When writing WikiLinks, use the slug: `[[webgraph]]` links to `WebGraph/README.md`.

---

## 10. Git Workflow

The vault is an independent repository. The homepage pins it as a submodule at `_notes/`. Your Obsidian/writing workflow is unchanged.

To surface new notes on the homepage:

```bash
# 1. In the vault repo — commit and push your changes as normal
git add . && git commit -m "publish: add notes on knowledge graphs"
git push

# 2. In the homepage repo — update the submodule pin and rebuild
cd _notes && git pull && cd ..
npm run build:all
git add _notes assets/garden
git commit -m "chore: update garden — N notes, M edges"
```

The homepage CI/CD runs `npm run build:all` on every deploy, so the graph reflects whatever submodule commit is pinned.

**During local development** (when `_notes/` submodule is not available due to disk space): the build script automatically falls back to the sibling repo at `../karx.github.io`. No config needed.

---

*This document is maintained alongside the integration. Changes to `build-garden.mjs` behaviour are reflected here.*
*See also: `kaaroViewer/GARDEN_INTEGRATION.md` for the viewer-side implementation details.*
