---
published: false
title: "Agent Runtime Diagram — Spec"
tags:
  - design
  - agents
description: "Visual specification for the opinionated Agent/Skill/Context runtime loop diagram used in the LinkedIn post."
---

# Agent Runtime Diagram — Spec

## Purpose

A single diagram that makes the Agent/Skill/Context model immediately legible. 

---

## Core Concept to Convey

Three distinct things. One dynamic relationship.

- **Skill** is static. Encoded once. Lives outside the loop.
- **Agent** is the loop. It runs, perceives, acts, reflects.
- **Context** is the output of the loop — not a container, an expansion. It grows with each iteration.

The diagram must show **directionality** (the loop moves), **hierarchy** (Skill is above/outside, Context is below/expanding), and **growth** (Context visibly expands across iterations).

---

## Layout

### Orientation
Vertical. Top to bottom.

```
        [ SKILL ]
            |
          invoke
            |
            ▼
    ┌───────────────┐
    │               │
    │  perceive     │
    │     ↓         │  ← AGENT
    │   act         │
    │     ↓         │
    │  reflect      │
    │               │
    └───────┬───────┘
            |
          creates
            |
            ▼
    ░░░░░░░░░░░░░░░
  ░░               ░░
░░    C O N T E X T  ░░  ← grows outward each loop
  ░░               ░░
    ░░░░░░░░░░░░░░░
          ↓
    ░░░░░░░░░░░░░░░░░░░
  ░░                   ░░  ← larger after next loop
░░                       ░░
  ░░                   ░░
    ░░░░░░░░░░░░░░░░░░░
```

---

## Elements

### SKILL (top)
- Shape: clean rectangle or pill
- Label: `SKILL`
- Sublabel (small, below): `encoded knowledge · static · invoked`
- Color: cool — slate blue or muted teal
- Feel: crystallized, contained, not alive
- Arrow pointing DOWN into the Agent loop labeled: `invoke`

### AGENT (middle)
- Shape: rounded rectangle, slightly glowing border
- Label: `AGENT`
- Internal loop visible — three steps arranged in a cycle:
  - `perceive`
  - `act`
  - `reflect`
- Arrows between the three steps showing the cycle (clockwise)
- Color: warmer — amber or soft white glow against dark background
- Feel: alive, in motion, the active center

### Context (bottom)
- Shape: expanding soft blob / radial haze — NOT a rectangle
- Two states shown: smaller (loop 1) → larger (loop 2)
- Label: `CONTEXT`
- Sublabel: `surface area · grows each loop`
- Color: warm gradient — amber fading to dark, or a soft orange fog
- Feel: organic, expanding, created not given
- Arrow from Agent loop pointing DOWN labeled: `creates`

### Connecting labels
- SKILL → AGENT: `invoke`
- AGENT → CONTEXT: `creates`
- Optional loop-back arrow from CONTEXT edge back up to AGENT labeled: `informs next perceive`

---

## Typography

- All caps for section labels: `SKILL`, `AGENT`, `CONTEXT`
- Lowercase for sublabels and internal steps: `perceive`, `act`, `reflect`
- Font: monospace or clean geometric sans (matches technical audience)
- Background: dark — near black (#0d0d0d or similar)
- Text: high contrast white or near-white

---

## Color Palette

| Element   | Color                        | Feel          |
|-----------|------------------------------|---------------|
| Background| #0d0d0d                      | Dark canvas   |
| Skill     | #4a90d9 (slate blue)         | Cold, encoded |
| Agent     | #f5a623 (amber)              | Warm, alive   |
| Context   | #f5a623 → transparent (fade) | Expanding fog |
| Labels    | #ffffff                      | Clean         |
| Sublabels | #888888                      | Quiet         |

---

## Mood / Reference

- Close to: circuit diagram meets organic growth
- Not: corporate flowchart
- Not: academic graph
- Closest visual reference: a glowing node graph on a dark canvas — like kaaroViewer but simpler, one focused thing

---

## Format

- Export: PNG, 1200×1400px (portrait for LinkedIn)
- Also export: 1:1 square crop (1200×1200) for carousel slide
- Tool: Excalidraw preferred (matches vault aesthetic), or Figma

---

## What to Avoid

- No hard boxy flowchart aesthetic
- No color-coded arrows that need a legend
- No text-heavy callouts — the diagram should work with minimal reading
- Context must NOT look like a container — it must look like something being created and expanding

---

## Validation

The diagram works if someone can look at it for 5 seconds and understand:
1. Skill is accessible to Agent
2. The Agent loops
3. Something grows below it

The label `Context is the surface area the agent creates in the run` should appear as a caption beneath the diagram, not inside it.
