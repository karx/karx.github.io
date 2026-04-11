# Garden Maintainer Guidelines

This document defines the conventions for maintaining the `karx.github.io` vault so it can be published as an interactive knowledge graph on the homepage.

The vault is mounted as a **git submodule** inside `homepage/_notes/`. A build script walks this directory, parses frontmatter and WikiLinks, and emits `garden-graph.json` — the data file that powers the 3D Garden page. Everything in this document affects what ends up in that graph.

---

## 1. What Gets Published

**Only notes with `published: true` in their frontmatter are included in the public graph.** Notes without this field are ignored entirely. This means the vault stays private-first: you write freely, and selectively surface what's ready.

```yaml
---
published: true
---
```

That's the minimum required field. The rest of the frontmatter below enriches the graph node — but `published: true` is the gate.

---

## 2. Frontmatter Spec

```yaml
---
published: true                   # required — omit to keep private
title: "Kaaro Stream"             # optional — falls back to filename/folder name
date: 2025-11-02                  # optional — ISO 8601, used for "last updated" display
tags:                             # optional — drives cluster grouping in the graph
  - streaming
  - mqtt
  - real-time
description: "Notes on the real-time content pipeline bridging speech to knowledge graph." 
                                  # optional — shown in detail panel on hover/click
image: images/kaaro-stream.png    # optional — node thumbnail, relative to vault root
---
```

### Field rules

| Field | Type | Behaviour when missing |
|-------|------|------------------------|
| `published` | boolean | Note is excluded from graph |
| `title` | string | Derived from: H1 heading → folder name → filename (in that order) |
| `date` | ISO date | Node shows no date; not sorted |
| `tags` | list of strings | Node placed in "untagged" cluster |
| `description` | string | First non-heading paragraph used as fallback |
| `image` | relative path | No thumbnail shown on node |

---

## 3. File and Folder Structure

The vault supports two layouts. Both work.

**Single-file note:**
```
MyTopic.md
```

**Folder note** (when a topic has supporting files like images or sub-notes):
```
MyTopic/
  README.md      ← this is the note
  diagram.png
  sub-thought.md ← treated as a separate note if it has published: true
```

The build script uses `README.md` as the canonical file for a folder. Other `.md` files inside a folder are treated as independent notes only if they carry their own `published: true`.

---

## 4. WikiLinks — How Graph Edges Are Built

Links between notes in the graph come from **Obsidian-style WikiLinks** in your note body:

```markdown
This connects to [[kaaro]] and the [[WebGraph]] project.
```

The build script scans all published notes for `[[...]]` patterns. Each WikiLink becomes a directed edge from the source note to the target note — **if the target is also published**. Links to unpublished or non-existent notes are silently dropped (no broken edges in the graph).

### Rules for WikiLinks
- Use the folder/file name, not the full path: `[[kaaro]]` not `[[kaaro/README]]`
- Case-insensitive matching: `[[Kaaro]]` and `[[kaaro]]` resolve to the same node
- Aliases are ignored for graph purposes: `[[kaaro|the stream project]]` → edge to `kaaro`, display name ignored
- External URLs in `[text](url)` format are **not** graph edges

---

## 5. Tags and Cluster Grouping

Tags drive the visual clusters in the 3D graph. Notes with the same tag are pulled into the same cluster region by the force-directed layout.

**Recommended tag taxonomy** (use these consistently — the graph layout responds to tag volume):

| Tag | Intended cluster |
|-----|-----------------|
| `streaming` | Real-time / data pipeline work |
| `interface` | UI/UX and interaction experiments |
| `iot` | Hardware, microcontrollers, physical computing |
| `knowledge-graph` | Wikidata, ontology, graph DB work |
| `maker` | 3D printing, fabrication, tools |
| `startup` | Ventures, products, business experiments |
| `reflection` | Personal essays and longer-form thinking |
| `reference` | Notes that are primarily links and resources |

You can use multiple tags per note. The graph assigns the node to the **first tag** as its primary cluster color, and lists all tags in the detail panel.

---

## 6. Images

Place images in the vault-root `images/` folder:

```
images/
  kaaro-stream-diagram.png
  webgraph-sketch.jpg
```

Reference them in frontmatter as:
```yaml
image: images/kaaro-stream-diagram.png
```

The build script copies referenced images to `homepage/assets/garden/images/` during the build. Images embedded inline in note bodies (`![alt](images/foo.png)`) are **not** automatically copied — only frontmatter `image:` values are processed.

---

## 7. Note Quality for Graph Display

The 3D garden renders each node as a point in space. When a user clicks a node, the **detail panel** shows:
1. Title
2. Description (from frontmatter, or first paragraph)
3. Tags as pills
4. WikiLink neighbors as "connected notes"
5. "Open note" link — to the full Jekyll-rendered note page

For nodes to feel meaningful in the graph, aim for:
- A clear `title` (or a strong H1 as the first line)
- A `description` of 1–3 sentences
- At least 1–2 WikiLinks to other published notes
- At least 1 tag

Notes with no WikiLinks and no tags will appear as isolated nodes at the graph periphery.

---

## 8. Keeping the Vault Healthy

The homepage repo includes a build-time health report. After running `npm run build:garden`, you'll see:

```
Garden build complete
  Published notes:  42
  Edges:            87
  Isolated nodes:   6   ← these have no WikiLinks
  Missing targets:  3   ← WikiLinks pointing to unpublished/missing notes
  Untagged nodes:   4
```

**Aim to keep isolated nodes and untagged nodes near zero** — these are the notes that get "lost" at the edge of the graph and rarely get explored.

---

## 9. What NOT to Publish

The following should stay unpublished (no `published: true`):

- Project scaffolding files (`Untitled.md`, temp notes)
- Notes with `node_modules/` or tooling content inside the folder
- Image dump notes (just a pile of `Pasted Image...` files)
- Notes that are purely private context (people's names, addresses, private finances)
- Drafts where the thinking is incomplete and would mislead

When in doubt, leave `published:` out. You can always add it later.

---

## 10. Git Workflow

The vault is an independent repository (`karx/karx.github.io`). The homepage references it as a submodule at `_notes/`.

**Your vault workflow doesn't change.** Write, commit, push as you normally do in Obsidian or your editor.

To surface changes on the homepage:
```bash
# Inside homepage repo
cd _notes && git pull         # pull latest vault changes
cd .. && git add _notes
git commit -m "chore: update garden submodule"
```

The homepage CI/CD will automatically run `npm run build:garden` on each deploy, so the graph stays in sync with whatever submodule commit is pinned.

---

*This document is maintained alongside the homepage integration. If the build script changes its behaviour, this file is updated to match.*
