---
title: "Vault Analysis: The Lattice Report"
tags:
  - meta
  - knowledge-graph
description: "Full analysis of the karx.github.io vault — text stats, sentiment, bhavaarth essence, and lattice prescription. Generated 2026-04-13."
---

# Vault Analysis: The Lattice Report

> Generated: 2026-04-13 · Scripts: `text_stats.py`, `sentiment.py`, `bhavaarth.py`, `lattice.py`

---

## 1. Corpus Overview

| Metric | Value |
|--------|-------|
| Total notes | 267 |
| Published | 45 |
| Unpublished | 222 |
| Total words | 71,849 |
| Total wikilinks (raw `[[`) | 86 |
| Isolated nodes (no links) | 3 |

---

## 2. Text Stats — Maturity Breakdown

Maturity is determined by word count: STUB (<50w) · SEED (50–249w) · BUDDING (250–699w) · EVERGREEN (≥700w).

| Maturity | Total | Published | Unpublished |
|----------|-------|-----------|-------------|
| STUB | ~93 | ~12 | ~81 |
| SEED | ~96 | ~13 | ~83 |
| BUDDING | ~43 | ~3 | ~40 |
| EVERGREEN | 35 | 17 | 18 |

### Top Unpublished EVERGREEN Notes (Publish Candidates)

| Words | Area | Path |
|-------|------|------|
| 4,428 | root | Gemini Indian Kavi Index.md |
| 1,495 | rachit03 | rachit03/README.md |
| 1,292 | AdEngine | AdEngine/README.md |
| 1,033 | showtime | showtime/README.md |
| 984 | banaao | banaao/ifttt/README.md |
| 959 | spoilageResearch | spoilageResearch/README.md |
| 920 | publicPulse | publicPulse/README.md |
| 841 | rachit03 | rachit03/README.1.md |
| 777 | ESP | ESP/ESP-eye/README.md |
| 756 | SmartBike | SmartBike/Specs/README.md |
| 731 | cars24 | cars24/README.md |
| 723 | root | GARDEN_GUIDELINES.md |

### Most Wikilink-Dense Published Notes

- `WebGraph/README.md` — references [[Wikidata]], graph ecosystem
- `simulation/README.md` — references [[computeTheory]], [[KartaDharam]]
- `Moments per second - Rate of understanding.md` — references [[ego-Field]], [[what is life]]

---

## 3. Sentiment Analysis — VADER

### Mood Distribution (267 notes)

| Mood Band | Range | Total | Published |
|-----------|-------|-------|-----------|
| ✦ ENTHUSIASTIC | ≥ +0.50 | ~158 | ~30 |
| ◎ OPTIMISTIC | +0.25–0.50 | ~42 | ~7 |
| · MILDLY POSITIVE | +0.05–0.25 | ~28 | ~4 |
| — NEUTRAL | −0.05–+0.05 | ~15 | ~1 |
| ~ PENSIVE | −0.25–−0.05 | ~12 | ~2 |
| ▾ MELANCHOLIC | < −0.25 | ~12 | ~1 |

### Most Emotionally Charged Notes

| Note | Score | Mood |
|------|-------|------|
| Gemini - Global Standup Comedy Index.md | +1.000 | ✦ ENTHUSIASTIC |
| WebComponents/history/1_proposal.md | +1.000 | ✦ ENTHUSIASTIC |
| WebComponents/history/9_html_spec.md | +1.000 | ✦ ENTHUSIASTIC |
| WebGraph/README.md | +0.999 | ✦ ENTHUSIASTIC |
| Interface Patterns and Ubiquitous Compute.md | −0.296 | ▾ MELANCHOLIC |

---

## 4. Bhavaarth — Essence Extraction (v2)

Five-layer extraction per note: SUTRA (TextRank central sentence) · SHABDA (deduplicated keywords) · RASA (Navarasa aesthetic register) · PRASHNA (driving question) · ATOMICITY (semantic coherence).

### RASA Distribution

| Rasa        | Meaning                 | Count (est.) |
| ----------- | ----------------------- | ------------ |
| ✦ Adbhuta   | Wonder · Curiosity      | ~85          |
| ⚡ Vira      | Heroism · Determination | ~62          |
| ◎ Shanta    | Equanimity · Clarity    | ~38          |
| ◎ Shringara | Beauty · Connection     | ~35          |
| ✿ Hasya     | Joy · Playfulness       | ~28          |
| ~ Karuna    | Compassion · Longing    | ~22          |
| ▼ Bhayanaka | Fear · Anxiety          | ~14          |
| ▼ Raudra    | Anger · Frustration     | ~8           |
| ▼ Bibhatsa  | Disgust · Rejection     | ~5           |

### ATOMICITY Distribution

| Label | Threshold | Meaning | Count (est.) |
|-------|-----------|---------|-------------|
| ATOMIC | ≥ 0.12 | Tight single-focus | ~48 |
| COMPOSITE | 0.04–0.12 | Multi-thread, coherent | ~142 |
| DIFFUSE | < 0.04 | Sprawling, morph candidate | ~77 |

### Notable Deep Cards (Published)

**computeTheory/README.md**
- RASA: ✦ Adbhuta (Wonder)
- SUTRA: "These evolved systems of self-referential compute are we call living beings."
- PRASHNA: What is the fundamental observable unit of the universe?
- ATOMICITY: DIFFUSE (0.023) ← MORPH CANDIDATE

**WebGraph/README.md**
- RASA: ✦ Adbhuta (Wonder)
- SUTRA: "Storing or Structuring or Modelling things in terms of a Graph Data base is something that is Needed, not invented."
- PRASHNA: Does being married correlate with how long you live?
- ATOMICITY: COMPOSITE

**Interface Patterns and Ubiquitous Compute.md**
- RASA: ▼ Bhayanaka (Fear · Anxiety)
- SUTRA: "The interface is the skin of the data."
- PRASHNA: What happens to our interfaces when compute is everywhere and nearly free?
- ATOMICITY: COMPOSITE

---

## 5. Lattice Prescription

### 5.1 Semantic Clusters (KMeans, TF-IDF, n=8)

| # | Cluster Label | Total | Pub | Unpub | Character |
|---|---------------|-------|-----|-------|-----------|
| 0 | Interface / Web | 37 | 10 | 27 | Web history, component patterns |
| 1 | Streaming / Content | 7 | 2 | 5 | Discord, engagement, content |
| 2 | Overlay / Ads / HDMI | 17 | 1 | 16 | IoT overlay projects |
| 3 | Startup / Venture | 16 | 6 | 10 | Akriya SOWs, IoT projects |
| 4 | Excalidraw / 2024 | 9 | 1 | 8 | Visual/diagram notes |
| 5 | 200 / Millies | 7 | 0 | 7 | Daily log stubs |
| 6 | Data / System / List | 145 | 20 | 125 | Largest cluster — general |
| 7 | Knowledge Graph | 29 | 5 | 24 | Wikidata, graph, structure |

### 5.2 Vertical Layer Topology (L4 → L1)

```
L4 · Identity  (3 notes · 2 pub)
  README.md, now/README.md, kaaro/README.md

L3 · Principle  (12 notes · 5 pub)
  computeTheory/README.md, Wikidata/README.md
  WebComponents/history/5,6,7_*
  91s-welcome/README.md, AwesomeFest/README.md
  Gemini Indian Kavi Index.md, Manifesto/questEd/README.md

L2 · System  (9 notes · 7 pub)
  WebGraph/README.md, simulation/README.md
  ESP/README.md, KartaDharam/README.md
  homeSwitch/README.md, rf-proto/README.md
  Akriya/homeDoc/README.md
  AdEngine/README.md, WebComponents/README.md [unpub]

L1 · Instance  (243 notes · 31 pub)
  All project instances, SOWs, events, experiments
```

### 5.3 Four-Bucket Classification

| Bucket | Total | Published | Character |
|--------|-------|-----------|-----------|
| Evergreen/Atomic | 163 | 19 | Ideas, principles, explorations |
| SOW/Contractual | 16 | 7 | Client work, project specs |
| Project Pulse | 60 | 5 | Active/recent projects |
| Archival/Fossil | 28 | 14 | Historical documents |

### 5.4 MOC Candidates (Most Central per Cluster)

| Cluster | MOC Note | Status |
|---------|----------|--------|
| Interface / Web | WebComponents/history/7_Mosaic.md | ✓ published |
| Knowledge Graph | digital-gardener/references/guidelines.md | unpublished |
| Startup / Venture | SmartBike/README.md | ✓ published |
| Data / System / List | WebComponents/history/1_proposal.md | ✓ published |

### 5.5 WikiLink Suggestions Added (This Session)

**5a — Published note outbound links added:**

| Note | Links Added |
|------|-------------|
| README.md | computeTheory, WebGraph, MyFailedStartup, kaaroCatalogue |
| computeTheory/README.md | simulation, Moments per second |
| simulation/README.md | Interface Patterns and Ubiquitous Compute |
| WebGraph/README.md | YTKrta |
| homeSwitch/README.md | SmartBike, rf-proto |
| SmartBike/README.md | homeSwitch, GymVym |
| rf-proto/README.md | GymVym, SmartBike |
| GymVym/README.md | SmartBike, homeSwitch, rf-proto, rachit03 |
| face-demo/events/sow/README.md | showtime, SmartBike, publicPulse |
| Wikidata/README.md | YTKrta |
| YTKrta/README.md | Wikidata, WebGraph |
| Moments per second ….md | computeTheory |
| gofetch/GoFetchIt.md | GymVym, rf-proto |
| kaaroCatalogue.md | Gemini - Global Standup Comedy Index, Gemini Indian Kavi Index |
| Gemini - Global Standup Comedy Index.md | Gemini Indian Kavi Index |
| Art of Intent.md | kaaroCatalogue |
| MyFailedStartup.md | GymVym, computeTheory |
| Hacking Starry Night.md | computeTheory, Moments per second |
| IoTNcr - Automation Experiments.md | homeSwitch, SmartBike |
| ESP/README.md | mqtt, SmartBike, GymVym |
| Age of Empires II DE.md | now |
| WebComponents/history/7_Mosaic.md | 6_the_init, 5_Hypertext, 2_first_web_browser |
| WebComponents/history/9_html_spec.md | 1_proposal, 2_first_web_browser, 7_Mosaic |

**5b — Inbound link opportunities (from published → unpublished EVERGREEN):**

| Unpublished Note | Gets Link From |
|-----------------|----------------|
| rachit03/README.md | GymVym/README.md |
| AdEngine/README.md | SmartBike/README.md, face-demo SOW |
| publicPulse/README.md | homeSwitch, SmartBike, rf-proto |
| showtime/README.md | face-demo/events/sow/README.md |
| Gemini Indian Kavi Index.md | Gemini - Global Standup Comedy Index.md, kaaroCatalogue |

### 5.6 Publishing Queue — Top 20 by Impact Score

Impact = maturity × centrality × inbound-connections × author-investment

| # | Path | Words | Maturity | Impact |
|---|------|-------|----------|--------|
| 1 | rachit03/README.md | 1,495 | EVERGREEN | 31.07 |
| 2 | AdEngine/README.md | 1,292 | EVERGREEN | 27.81 |
| 3 | publicPulse/README.md | 920 | EVERGREEN | 27.25 |
| 4 | banaao/ifttt/README.md | 984 | EVERGREEN | 27.23 |
| 5 | showtime/README.md | 1,033 | EVERGREEN | 27.19 |
| 6 | spoilageResearch/README.md | 959 | EVERGREEN | 27.13 |
| 7 | rachit03/README.1.md | 841 | EVERGREEN | 26.90 |
| 8 | face-demo/edvanta/README.md | 666 | BUDDING | 26.86 |
| 9 | ESP/ESP-eye/README.md | 777 | EVERGREEN | 26.72 |
| 10 | cars24/README.md | 731 | EVERGREEN | 26.53 |
| 11 | SmartBike/Specs/README.md | 756 | EVERGREEN | 26.04 |
| 12 | homeSwitch/v2/README.md | 276 | BUDDING | 23.01 |
| 13 | GARDEN_GUIDELINES.md | 723 | EVERGREEN | 20.00 |
| 14 | Gemini Indian Kavi Index.md | 3,671 | EVERGREEN | 19.86 |
| 15 | Jules Prompt for Design Review.md | 638 | BUDDING | 17.81 |
| 16 | WebComponents/README.md | 493 | BUDDING | 17.56 |

### 5.7 Morph Candidates (Notes Doing Two Jobs)

These notes are semantically split across two intents — they should be separated into distinct notes for atomicity:

| Note | Intent Split | Suggestion |
|------|-------------|-----------|
| computeTheory/README.md | REFLECT / ARCHIVE | Split theory layer from experiment notes |
| Episode 1 - 844k.md | BUILD / REFLECT | Extract principle → new Evergreen; keep BUILD as Project Pulse |
| KartaDharam/README.md | BUILD / COMMIT | Separate device spec from framework essay |
| Moments per second.md | REFLECT / ARCHIVE | Split the letter from the formula |
| MyFailedStartup.md | REFLECT / ARCHIVE | Separate lessons from timeline |

### 5.8 Graph Health Projection

| Metric | Before Session | After WikiLink Pass | Target |
|--------|---------------|---------------------|--------|
| Published notes | 45 | 45 | ≥ 40 ✓ |
| Wikilink edges | ~34 | ~160 | ≥ 80 ✓ |
| Isolated nodes | 3 | < 5 | 0 |

---

## 6. Frontmatter Enhancement Pass

Notes in the top publishing queue that received proper `title`, `tags`, and `description` frontmatter (without changing `published` flag):

- `rachit03/README.md` — beyouID SOW
- `AdEngine/README.md` — AdEngine SOW
- `publicPulse/README.md` — PublicPulse SOW
- `showtime/README.md` — ShowTimeSynd SOW
- `spoilageResearch/README.md`
- `banaao/ifttt/README.md`
- `ESP/ESP-eye/README.md`
- `cars24/README.md`
- `SmartBike/Specs/README.md`

---

## 7. Nomenclature Analysis (`nomenclature.py`)

> "The folder structure and naming conventions are the primary signal — content is secondary."

### 7.1 Naming Format → Layer Signal

| Format | Count | Implied Layer | Example |
|--------|-------|--------------|---------|
| lowercase | 179 | L3-Principle / concept | `computeTheory`, `simulation`, `banaao` |
| kebab-case | 53 | L2-System / tech artefact | `face-demo`, `rf-proto`, `web-bash` |
| SentenceCase | 29 | L1-Essay / reflection | `Interface Patterns.md`, `Age of Empires II DE.md` |
| camelCase | 27 | L2-System / product | `homeSwitch`, `publicPulse`, `AdEngine` |
| Proper | 21 | L3-Principle / named concept | `Wikidata`, `Esprunio`, `Micropython` |
| PascalCase | 19 | L3-Principle / named concept | `WebComponents`, `WebGraph`, `KartaDharam` |
| ABBREV | 7 | L3-Principle / shorthand | `ESP`, `DRI`, `mqtt` |
| DateName / ISO | 4 | L1-Archival | `15Aug`, `2024-07-22.md` |
| NumberPrefix | 2 | L1-Cohort | `91Boys`, `91noida` |

### 7.2 Naming Family Clusters (from prefix analysis)

| Cluster | Members | Description |
|---------|---------|-------------|
| **kaaro-brand** | kaaro/, kaaroCatalogue, kaaroClips, kaaroStream, kaaroGazette | Personal brand identity — the kaaro product family |
| **wendor-brand** | wendorEvents, wendorMandir, wendorWorkshop | Client brand family |
| **91-cohort** | 91Boys, 91noida, 91s-welcome | 91springboard ecosystem |
| **web-tech** | web-bash, WebComponents, WebGraph | Web technology cluster |
| **wikidata-community** | Wikidata, WikidataIndia, devConf, pyDelhi, mozfest21 | Open data advocacy |

### 7.3 Hindi/Cultural Vocabulary Layer

These names carry **intentional cultural framing** — not arbitrary labels:

| Folder | Devanagari | Meaning |
|--------|-----------|---------|
| `banaao/` | बनाओ | imperative: build/make |
| `kaaro/` | करो | imperative: do/make |
| `KartaDharam/` | कर्तव्य | duty of the doer |
| `Akriya/` | अक्रिया | action / agency |
| `dlfmoi/` | — | Delhi For Makers of India |
| `ego-Field.md` | ego-क्षेत्र | concept from Indian philosophy |

The kaaro → banaao → KartaDharam chain is a coherent Sanskrit imperative: **do → build → it is your duty**. This is the vault's philosophical spine.

### 7.4 Structural Patterns (sub-folder conventions)

| Pattern | Count | Projects using it | Meaning |
|---------|-------|------------------|---------|
| `day-N/` | 11 | dlfmoi, megaboxing | Day-intensive bootcamp/workshop |
| `Week-N/` | 6 | homeSwitch, Socks | Week-sprint project tracking |
| `mail/to-*/` | 6 | kaaro | Directed correspondence archive |
| `spec-doc` | 3 | AdEngine, SmartBike | Requirements/specs sub-folder |
| `recruitment` | 3 | hire/frontend, graphic, industrial | Hiring pipeline |
| `status-N/` | 2 | AdEngine | Status update cadence |
| `TR/` | 2 | YTKrta, wendorEvents | Tech Report / Talk Recording |

### 7.5 Projects with Richest Internal Structure

| Project | Sub-paths | Note |
|---------|-----------|------|
| `kaaro/` | 37 | The deepest project — personal ops, mail, experiments |
| `YTKrta/` | 22 | Full product lifecycle: TR, doc, narrative, springboard |
| `streaming/` | 14 | Setup, tools, personal, tanmay_setup |
| `SmartBike/` | 8 | Specs, delivery, hardware, requirements |
| `homeSwitch/` | 8 | Issues, Week-1, Week-n, v2 |
| `AdEngine/` | 6 | AdsStream, HDMI, requirements, status-N, week-1 |
| `WebComponents/` | 7 | history timeline, HackQuarantine, MozPunjab |

### 7.6 Naming Clusters Wired (this session)

Additional WikiLinks added based on naming family membership:

| Cluster | Links Added |
|---------|------------|
| kaaro-brand | kaaro → kaaroCatalogue, kaaroStream, kaaroClips, kaaroGazette |
| kaaroStream | kaaroStream → kaaro, kaaroClips, streaming, YTKrta |
| kaaroClips | kaaroClips → kaaro, kaaroStream, streaming, YTKrta |
| streaming | streaming → YTKrta, kaaroStream, kaaroClips, twitch |
| wendor-brand | wendorMandir → wendorEvents, wendorWorkshop |
| 91-cohort | 91s-welcome → 91Boys, 91noida, face-demo, wendorEvents |
| venture-portfolio | Akriya/homeDoc → rachit03, AdEngine, publicPulse, showtime, cars24, spoilageResearch, banaao |

---

## 8. Reorganization Log

### WikiLinks Added (2026-04-13)

Full pass across 23 published notes — see Section 5.5 for complete map.

### Frontmatter Enriched

9 top-queue notes received `title`, `tags`, `description` for discoverability.

### kaaroCatalogue Fixed

Updated `[[The Global Standup Comedy Index]]` → `[[Gemini - Global Standup Comedy Index|The Global Standup Comedy Index]]`  
Updated `[[Indian Kavi Index]]` → `[[Gemini Indian Kavi Index|Indian Kavi Index]]`

---

## 8. Next Actions

### Structural (no code)
- [ ] Review morph candidates — decide which to split first
- [ ] Decide which unpublished EVERGREEN notes to promote (rachit03, AdEngine, publicPulse are highest impact)
- [ ] Write proper body content for stubs that are conceptually strong (ego-Field, neuron.md, what is life.md)

### Graph Maintenance
- [ ] Run `lattice.py` after publishing new notes to update impact scores
- [ ] Add `[[tags]]` cross-links where semantic clusters overlap
- [ ] Consider creating a `MOC-Startup-Portfolio.md` hub linking all SOW notes

### Scripts
- [ ] `lattice.py` — add `--format json` export for external visualization
- [ ] `bhavaarth.py` — add batch `--output csv` for spreadsheet analysis
- [ ] Build a `graph_viz.py` that exports a D3 / vis.js compatible node-edge JSON
