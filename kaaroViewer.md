---
published: true
title: "kaaroViewer"
tags:
  - kaaro
  - project
  - visualization
  - knowledge-graph
description: "A spatial intelligence platform that renders knowledge graphs as immersive 3D canvases — encoding reports, documents, and entities into navigable visual briefs."
---

kaaroViewer is a personal spatial intelligence system. It takes documents, reports, and knowledge sources and encodes them into interactive 3D graph visualizations — nodes, edges, story arcs, insights, and cluster maps — rendered in a Three.js canvas with a report panel alongside.

[GitHub Repo ↗](https://github.com/karx/kaaroViewer)

---

## Core Concept

The viewer treats every document as an **intelligence brief**: a structured object with entities (nodes), relationships (edges), a narrative arc (story beats), analytical insights, and entity clusters. The 3D canvas makes the graph spatially navigable. The report panel renders the full brief alongside.

Input → Entity extraction → Knowledge graph → 3D canvas + report

---

## Current Stack

- **Rendering:** Three.js canvas (migrating from A-Frame)
- **Pipeline:** Vanilla JS ESM modules, no build step
- **Data:** Wikidata SPARQL, OpenTapioca NER, local library JSONs
- **Input:** Text (hotkey G), Voice (MQTT controller), Spatial click
- **Controller:** MQTT speech-to-text (separate controller page)
- **Library format:** structured JSON — `nodes[]`, `edges[]`, `story[]`, `insights[]`, `clusters[]`, `report_card`

## Key Modules

| File | Role |
|---|---|
| `kaaro.js` | Entry point, input handling, pipeline orchestration |
| `entity_matching.mjs` | Text → QIDs via OpenTapioca NER |
| `fetch_knowledge.mjs` | QIDs → SPARQL data (Wikidata) |
| `pipeline/local-graph.mjs` | LIBRARY registry + graph enrichment (centrality, clusters, tension curve) |
| `canvas/report.mjs` | Intelligence brief dashboard renderer |
| `canvas/narrative.mjs` | Guided tour / story beat overlay |
| `canvas/detail.mjs` | Node detail sidebar (click-to-expand) |
| `ontology.mjs` | Entity type → geometry + colour mapping |
| `logger.mjs` | Structured event logger, ring buffer 500, `window.kaaroLogs` |

---

## Library

The local library is a collection of encoded intelligence briefs. Each entry is a JSON file in `library/` registered in `pipeline/local-graph.mjs`.

| ID | Title | Domain |
|---|---|---|
| `gig-worker-projects` | Algorithmic Panopticon: Gig Economy India | Labour / Technology |
| `aoe-2-redbull-april-2026` | Red Bull Wololo: Londinium | Esports |
| `poker-tooling-2026` | The Modern Poker Player's Toolkit | Gaming / Technology |
| `art-of-intent` | Art of Intent: Codebase Intelligence Brief | Software |
| `minecraft-redstone-computation` | The Digital Bedrock | Technology |
| `kaaro-viewer` | KaaroViewer: Immersive Cognitive Interface | Software |
| `advanced-git-workflows` | Advanced Version Control Dynamics | Engineering / DevOps |

---

## Related
[[kaaroViewer Roadmap]] · [[kaaroViewer Vision]] · [[kaaroViewer Exploration Pipeline]] · [[kaaroCatalogue]] · [[Advanced Git Workflows]]
