---
published: true
title: "kaaroViewer Exploration Pipeline"
tags:
  - kaaro
  - architecture
  - pipeline
  - plan
description: "Architecture plan for the seed-to-canvas exploration pipeline — LLM-first narrative with parallel deterministic enrichment, NED++ entity resolution, and user-driven rewrite controls."
---

The exploration pipeline transforms a seed (topic, URL, name, text) into a live kaaroViewer intelligence brief. It combines LLM-generated narrative with deterministic enrichment adapters, unified through a multi-source entity resolution layer. The canvas renders immediately from Stage 1 output and refines as enrichment lands.

---

## The 5-Stage Pipeline

```
SEED
(topic / URL / name / text snippet)
        │
        ▼
┌─────────────────────────────────────────────┐
│  STAGE 1 — LLM EXPLORATION + NARRATIVE      │
├─────────────────────────────────────────────┤
│  Input:  seed + optional context            │
│  Output: working brief (renderable)         │
│                                             │
│  • Entity list with inferred relationships  │
│  • Confidence score per entity              │
│  • Story arc: beats, tension, climax        │
│  • Draft insights                           │
│  • Cluster hypotheses                       │
│  • Layout hints (spatial intent signals)    │
└──────────────────┬──────────────────────────┘
                   │  working brief fires to canvas immediately
                   ▼
┌─────────────────────────────────────────────┐
│  STAGE 2 — NED++ RESOLUTION                 │
├─────────────────────────────────────────────┤
│  Input:  entity list from Stage 1           │
│  Output: cross-source ID map per entity     │
│                                             │
│  Path A — high confidence                   │
│    OpenTapioca → Wikidata QID               │
│  Path B — source-specific                   │
│    heuristic match → YouTube ID /           │
│    Reddit handle / GitHub slug / etc.       │
│  Path C — ambiguous                         │
│    LLM picks from top-3 candidates          │
│    using seed context as tiebreaker         │
│                                             │
│  ID map cached permanently once resolved    │
└──────────────────┬──────────────────────────┘
                   │  resolved IDs fan out
                   ▼
┌─────────────────────────────────────────────┐
│  STAGE 3 — PARALLEL ENRICHMENT ENGINE       │
├─────────────────────────────────────────────┤
│  Input:  resolved entity ID map             │
│  Output: enriched node objects + delta flag │
│                                             │
│  Adapters run in parallel per entity:       │
│    wikidata   → facts, relationships, dates │
│    wikipedia  → prose context, key sections │
│    youtube    → metrics, videos, topics     │
│    reddit     → community signals, volume   │
│    github     → repo stats, activity        │
│    rss / web  → recent coverage             │
│                                             │
│  Common adapter output schema:              │
│    { source, metrics, links,                │
│      related_ids, raw_summary }             │
│                                             │
│  Adapters fail silently — isolated pure fns │
│  Canvas streams updates as adapters resolve │
│                                             │
│  Delta check on completion:                 │
│    → confirms story    : continue to S4     │
│    → node-level change : patch node only    │
│    → significant delta : surface to user    │
│      UI: [ EXPAND ] [ RETHINK ]             │
└──────────────────┬──────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────┐
│  STAGE 4 — COMPLETION + LAYOUT              │
├─────────────────────────────────────────────┤
│  4a  ENTITY COMPLETENESS                    │
│      Story references node X → X must exist │
│      Add any missing required nodes         │
│                                             │
│  4b  BACKGROUND ENRICHMENT                  │
│      Attach adapter data to each node:      │
│      metrics, descriptions, external links  │
│                                             │
│  4c  RELATIONSHIP GAP FILL                  │
│      Cross-check edges vs enriched data     │
│      Add edges surfaced by adapters         │
│      (e.g. YouTube collab, Reddit cross-post│
│      co-authorship, fork relationships)     │
│                                             │
│  4d  LAYOUT + PLACEMENT                     │
│      Spatial decisions:                     │
│      • Tier → radial distance from origin   │
│      • Cluster → spatial grouping zone      │
│      • Edge weight → proximity pull         │
│      • Spine nodes → canvas anchor points   │
│      • Layout hints from Stage 1 as signals │
│        (e.g. "these clusters should oppose" │
│         → place on opposite canvas sides)   │
│      Physics layer fine-tunes within these  │
│      constraints, not from scratch          │
└──────────────────┬──────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────┐
│  STAGE 5 — PLOT + VISUALIZE                 │
├─────────────────────────────────────────────┤
│  Input:  finalized brief + layout coords    │
│  Output: live canvas                        │
│                                             │
│  • Emit nodes incrementally to canvas       │
│  • Apply pre-computed layout positions      │
│  • Set initial camera to spine cluster      │
│  • Trigger narrative overlay if tour exists │
│  • Stream enrichment updates as they land   │
│                                             │
│  Stage 5 is emission only — no decisions.   │
│  Swappable: Three.js / SVG export /         │
│  shareable JSON URL — same upstream         │
└─────────────────────────────────────────────┘
```

---

## Design Decisions

### Rewrite Threshold — User Driven
There is no algorithmic threshold for triggering a story arc rewrite. When enrichment surfaces a significant delta, the system surfaces two user-facing controls:

**`[ EXPAND ]`** — add the new entities/relationships the enrichment found without changing the existing narrative. The story grows; the arc is preserved. Use when enrichment found more detail on the same story.

**`[ RETHINK ]`** — feed enriched data back into Stage 1 as new context and regenerate the narrative from scratch. Use when enrichment revealed the initial framing was wrong or incomplete.

Three internal delta levels determine whether these controls appear:
- **Node-level patch** — enrichment updates metrics or description on an existing node. Silent update, no prompt to user.
- **Structural delta** — enrichment adds a new high-weight entity or removes an unresolvable one. Show `[ EXPAND ]` / `[ RETHINK ]`.
- **Sentiment flip** — enrichment reverses the sentiment of a spine or primary node (e.g. LLM assumed positive, Reddit data shows highly negative community). Always show `[ RETHINK ]` with a specific callout.

### Layout Hints from Stage 1
The LLM outputs a `layout_hints` block alongside the brief. This is a signal, not a command — the layout engine uses it as a soft constraint:

```json
"layout_hints": {
  "oppose": [["cluster-A", "cluster-B"]],
  "anchor": ["node-spine-1"],
  "timeline_axis": ["event-1", "event-2", "event-3"],
  "push_peripheral": ["node-context-1"]
}
```

The physics engine receives pre-computed anchor positions derived from these hints. It fine-tunes from there rather than computing layout from scratch. Layout hints do not override tier/cluster rules — they augment them.

### No Quality Gate on Stage 1
Stage 1 renders immediately regardless of brief completeness. A 3-node stub with 1 beat is a valid renderable state. The canvas is always live; enrichment fills it in. This keeps the feedback loop tight — the user sees something instantly and can steer via `[ EXPAND ]` / `[ RETHINK ]` rather than waiting for a fully-formed brief.

---

## NED++ Resolution Detail

Named Entity Disambiguation, extended to multi-source canonical ID resolution.

One entity resolves to a **cross-source ID map**:
```json
{
  "label": "Lex Fridman",
  "ids": {
    "wikidata": "Q59735",
    "youtube": "UCnUYZLuoy1rq1aVMwx4wneg",
    "reddit": "lexfridman",
    "twitter": "lexfridman",
    "github": "lexfridman"
  },
  "confidence": { "wikidata": 0.97, "youtube": 0.91 }
}
```

Resolution paths:
1. **OpenTapioca** → Wikidata QID (existing pipeline, extend hop depth)
2. **Source-type heuristics** → if entity type is `channel`: YouTube search API → top result above 0.85 name similarity
3. **LLM disambiguation** → for ambiguous cases, prompt: *"Given these 3 Wikidata candidates and this context, which is correct?"*

ID maps are cached permanently. Once "Lex Fridman" is resolved, every future brief that mentions him uses the cached map — no re-resolution.

---

## Adapter Registry

Each adapter is a pure isolated function:
```
(entity_id: string, source: AdapterSource) → AdapterResult
```

Adapters fail silently. Failures log to the structured logger but do not block the pipeline.

| Adapter | Input | Key Outputs |
|---|---|---|
| `wikidata` | QID | facts, P-statements, related QIDs, dates |
| `wikipedia` | QID or title | prose summary, key sections, infobox |
| `youtube` | channel/video ID | subscriber count, video titles, top topics, collaborators |
| `reddit` | subreddit/user | subscriber count, posting volume, top linked domains, sentiment signal |
| `github` | repo/user slug | stars, forks, language, recent commits, contributors |
| `rss` | feed URL | recent article titles, publication dates, linked entities |

**Adapter priority on conflict:** `wikidata` facts take precedence for canonical properties (birth date, nationality). Source-specific metrics (subscriber count, star count) are non-conflicting — they live in separate metric keys. Prose summaries: `wikipedia` preferred, `raw_summary` from other adapters appended.

---

## Stage 1 LLM Output Schema

Stage 1 produces a partial brief — same schema as the library JSON, with additions:

```json
{
  "meta": { ... },
  "nodes": [ { ...standard node, "confidence": 0.0–1.0 } ],
  "edges": [ { ...standard edge } ],
  "story": [ { ...standard beat } ],
  "insights": [ { ...standard insight } ],
  "clusters": [ { ...standard cluster } ],
  "report_card": { ... },
  "layout_hints": {
    "oppose": [],
    "anchor": [],
    "timeline_axis": [],
    "push_peripheral": []
  },
  "enrichment_targets": [
    { "node_id": "...", "priority": "high|medium|low" }
  ]
}
```

`confidence` on nodes drives visual treatment in Stage 5 — low-confidence nodes render with dimmed aura until NED++ resolves or enrichment confirms.

`enrichment_targets` tells Stage 3 which nodes to prioritize when adapter slots are limited. Spine and primary nodes are always high priority.

---

## Implementation Order

**Phase 1 — Foundation**
- [ ] Adapter interface + common schema
- [ ] Wikidata deep adapter (extend existing SPARQL, configurable hop depth)
- [ ] Wikipedia prose adapter
- [ ] NED++ resolution module (extend OpenTapioca, add cache layer)

**Phase 2 — Enrichment Engine**
- [ ] Parallel fetch coordinator (fan-out + merge + incremental stream)
- [ ] Delta detection (node-level / structural / sentiment-flip)
- [ ] `[ EXPAND ]` / `[ RETHINK ]` UI controls wired to pipeline

**Phase 3 — High-Signal Adapters**
- [ ] YouTube Data API adapter
- [ ] Reddit API adapter
- [ ] GitHub adapter

**Phase 4 — Stage 1 LLM Prompt**
- [ ] Exploration + narrative prompt (structured output: nodes + story + layout_hints)
- [ ] Confidence scoring per entity
- [ ] Layout hints schema

**Phase 5 — Layout Engine**
- [ ] Stage 4d: pre-compute anchor positions from tier + cluster + layout_hints
- [ ] Physics constraint layer (hints as soft forces, not hard positions)
- [ ] Stage 5 incremental emission to canvas

---

## Related
[[kaaroViewer]] · [[kaaroViewer Roadmap]] · [[kaaroViewer Vision]]
