---
published: true
title: kaaroViewer Vision
tags:
  - kaaro
  - vision
  - knowledge-graph
  - spatial-computing
description: The long-term vision for kaaroViewer as a spatial intelligence platform — bridging open knowledge, personal memory, and multimodal input into a live cognitive canvas.
excalidraw-plugin:
---

kaaroViewer is not a graph viewer. It is a **cognitive interface** — a spatial layer over knowledge that lets a person navigate, query, and sense-make in three dimensions rather than in lists and documents.

---

## The Core Thesis

Most knowledge tools are **flat and passive**: search returns documents, feeds return content, notes return text. They surface information but don't reveal structure. The relationships between things — causality, opposition, influence, precedence — are hidden in prose.

kaaroViewer makes those relationships **first-class and spatial**. A report isn't read linearly; it's entered. Entities orbit each other by importance. Causal chains become visible geometry. Story tension has a physical arc.

The long-term aspiration: a single canvas that holds everything you know and everything the world knows, navigable by voice, touch, and attention.

---

## The Three Layers

### 1. Open Knowledge (already wired)
- Wikidata SPARQL enrichment — any named entity resolves to a QID with properties, labels, linked concepts
- OpenTapioca NER — free text instantly extracts entities and maps them to the knowledge graph
- Open Graph metadata — URLs resolve to structured descriptions

### 2. Encoded Intelligence (active)
- The `visualize` skill encodes documents into structured briefs: nodes, edges, story, insights, clusters
- Each brief is a permanent, queryable knowledge object — not a one-time render
- Cross-document entity linking: the same QID in two briefs creates inter-document edges

### 3. Personal Memory (future)
- The canvas should reflect *your* knowledge graph, not just a document's
- Personal notes, decisions, projects, relationships — encoded in the same node/edge schema
- Memory surfaces contextually: when you view a node about Git, your personal note about a merge conflict you fixed last year appears as a connected node
- Obsidian vault as a data source: PKM notes → encoded into the graph on load

---

## Input Philosophy

The system should be queryable in any modality without friction:

- **Voice** → MQTT controller → same entity pipeline as text
- **Text** → hotkey G → NER → graph update
- **Spatial click** → entity focus → detail panel → drill-down
- **Future:** gaze tracking, proximity-based entity expansion, gesture-driven camera

The goal is **zero-friction access**: you should be able to ask "what do I know about trunk-based development?" and have the graph reorganize around that entity in under 2 seconds.

---

## Design Principles

1. **Space encodes meaning** — node size = importance, distance = relationship strength, cluster position = topic family. Layout is never arbitrary.
2. **Every entity is a first-class object** — not a row in a table. It has geometry, color, an aura, connections, a story.
3. **Narrative is infrastructure** — the story arc is not decoration. It is the primary cognitive path through a complex graph. The 3D canvas is the exploration layer; the story is the guided path.
4. **Personal context beats general knowledge** — a fact from Wikidata is less valuable than a fact from your own experience. Personal memory nodes should visually dominate when present.
5. **The graph is always live** — it should update as you speak, type, or navigate. No save/load cycle. No manual refresh.

---

## Long-Term Capabilities

- **Cross-document entity graph** — all library entries share a unified entity space; the same person/concept across multiple briefs becomes a persistent node with aggregated edges
- **Temporal navigation** — scrub through a knowledge graph as it evolves over time (events as waypoints)
- **Spatial memory palace** — assign entities to physical locations; the 3D layout becomes a mnemonic architecture
- **Collaborative canvas** — multiple users sharing the same graph space, seeing each other's focus points as presence indicators
- **Export to brief** — any subgraph can be exported as a shareable intelligence brief

---

## Related
[[kaaroViewer]] · [[kaaroViewer Roadmap]] · [[kaaroCatalogue]]
