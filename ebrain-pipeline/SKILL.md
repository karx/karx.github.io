---
name: ebrain-pipeline
description: |
  Three-stage maintenance pipeline for the eBrain Obsidian vault (d:\src\ebrain).
  PROCESS (inbox triage) → TRIAGE (score + rank) → PUBLISH ACTION (enrich + gate).
  Extends the digital-gardener skill. Zero authority — every change requires approval.
  One suggestion at a time. Always cite a principle.
---

# eBrain Pipeline Skill

Maintain and grow the `d:\src\ebrain` vault through a structured three-stage pipeline.
This skill composes on top of **digital-gardener** — all its mandates apply here too.

## Vaults in Scope

| Vault | Path | Role |
|-------|------|------|
| eBrain | `d:\src\ebrain` | Private working vault (PARA structure) |
| karx.github.io | `d:\src\karx.github.io` | Public garden (publish target) |

The two vaults are separate. eBrain is the *input*; karx.github.io is the *output*.
Notes flow **one way**: eBrain → karx.github.io when `published: true` is set.

---

## Core Mandates (inherited + extended)

1. **Zero Authority** — no file is moved, edited, or deleted without explicit user approval.
2. **Atomic Suggestions** — exactly one suggestion per turn, unless user says "apply all" or "check for more".
3. **Principled Rationale** — every suggestion cites a principle from `GARDEN_GUIDELINES.md`, `PKM-Engineering-System-Prompt.md`, or this document.
4. **Pipeline Order** — always process before triaging, triage before publishing.
5. **Isolation Zero** — every note must leave processing with ≥ 2 WikiLinks.

---

## Stage 1: PROCESS (Capture → Structure)

**Trigger:** New notes in `Inbox/` or `0_Inbox/`

### Step 1 — Score the Inbox
Run the prioritisation script to surface highest-value notes first:
```powershell
cd d:\src\ebrain
python scripts/inbox_score.py --top 10
```
Score formula: `name_quality (×0.4) + frontmatter_bonus (×0.3) + maturity (×0.3)`

### Step 2 — Per-Note Processing (one note at a time)
For each note (highest score first):

1. **Read** the full content
2. **Classify:**
   - PARA bucket → `Pipeline | Area | SkillSurface | Crystallized`
   - Layer → `L4-Identity | L3-Principle | L2-System | L1-Instance`
   - Maturity → `STUB | SEED | BUDDING | EVERGREEN`
3. **Suggest** target folder in PARA structure
4. **Suggest** frontmatter block (fill every field you can infer):
   ```yaml
   ---
   published: false
   title: ""
   tags: []
   description: ""
   date: YYYY-MM-DD
   layer: ""
   maturity: ""
   para: ""
   ---
   ```
5. **Suggest** 2 WikiLinks to existing vault notes
6. **Wait** for approval before touching anything

### Suggestion Format
```
📋 PROCESS SUGGESTION

Note: [filename]
Action: Move to [target folder]

Frontmatter:
  title: "[inferred title]"
  tags: [tag1, tag2]
  description: "[1-2 sentence description]"
  layer: [L1–L4]
  maturity: [STUB|SEED|BUDDING|EVERGREEN]
  para: [Pipeline|Area|SkillSurface|Crystallized]

WikiLinks to add: [[NoteA]], [[NoteB]]

Rationale: [Why this classification]
Principle: [Citation]
```

---

## Stage 2: TRIAGE (Assess → Score → Prioritise)

**Trigger:** On demand, or after processing a batch of inbox notes.

### Run Full Triage
```powershell
cd d:\src\ebrain
python scripts/inbox_score.py --top 10 --output "1 Projects/Digital Garden/Triage Report.md"
```

### Triage Report Output
Saved to: `1 Projects/Digital Garden/Triage Report.md`

Review and surface:
- 🌳 EVERGREEN notes with no frontmatter → **immediate process candidates**
- Island notes (0 WikiLinks) → **link enrichment candidates**
- Notes with good frontmatter but `published: false` → **publish queue**
- `Untitled N` EVERGREEN notes → **name rescue candidates**

---

## Stage 3: PUBLISH ACTION (Approve → Enrich → Gate)

**Trigger:** User selects a note from Triage Report to publish.

### Steps (sequential, approval at each)

1. **Enrich frontmatter** — fill `title`, `tags`, `description`, `date`
2. **Add WikiLinks** — ≥ 2 outbound links to other published or in-vault notes
3. **Tag** — pick from taxonomy; suggest new tag if none fits (3+ uses → new cluster)
4. **Verify image** — if `image:` field, confirm path exists
5. **Set `published: true`** ← the gate
6. **Optional git commit** — ask user; do not auto-commit

### Suggestion Format
```
🌿 PUBLISH SUGGESTION

Note: [path]
Current state: [maturity, word count, WikiLinks]

Suggested frontmatter changes:
  title: "[title]"
  tags: [tag1, tag2]
  description: "[description]"
  published: true  ← GATE

WikiLinks to add: [[A]], [[B]]

Rationale: [Why this note is ready]
Principle: [Citation]
```

**Tag Taxonomy** *(ever-expanding — 3+ uses graduates a tag to named cluster)*

| Tag | Cluster |
|-----|---------|
| `streaming` | Real-time / data pipeline |
| `interface` | UI/UX, interaction design |
| `iot` | Hardware, physical computing |
| `knowledge-graph` | Graph DB, ontology, Wikidata |
| `maker` | 3D printing, fabrication |
| `startup` | Ventures, products |
| `reflection` | Essays, long-form thinking |
| `reference` | Links, resources |

---

## SOPs

### SOP-1: Weekly Garden Walk
```
1. Run: python scripts/inbox_score.py --top 10
2. Process 3–5 inbox notes (Stage 1)
3. Run full triage → update Triage Report
4. Pick 1 note to publish (Stage 3)
5. Log session in: 1 Projects/Digital Garden/Garden Log.md
```

### SOP-2: New Project Capture
```
1. Create: 1 Projects/[Name]/README.md
2. Add frontmatter (published: false, para: Pipeline)
3. Add to: 1 Projects/Digital Garden/List of Projects 2025.md
4. WikiLink → nearest Area
5. WikiLink → relevant Resource notes
```

### SOP-3: Crystallise a Closed Pipeline
```
1. Write crystallisation note: built / learned / reusable
2. Move: 1 Projects/[Name] → 4 Archive/[Name]
3. Update parent Area README with link
4. If reusable → extract SkillSurface note in 2 Resources/
5. Decide publish? → Stage 3
```

### SOP-4: Name Rescue (Untitled EVERGREEN)
```
1. Read full content of Untitled N.md
2. Infer title from H1 heading, first paragraph, or dominant theme
3. Suggest: new filename + PARA folder
4. Suggest: frontmatter with inferred title, tags, description
5. Wait for approval; then rename + move
```

---

## Reference Files

| File | Location | Purpose |
|------|----------|---------|
| `GARDEN_GUIDELINES.md` | `karx.github.io/` | Publish spec, frontmatter schema, build pipeline |
| `PKM-Engineering-System-Prompt.md` | `karx.github.io/` | PARA-for-Agent-Engineering-Era framework |
| `digital-gardener/SKILL.md` | `karx.github.io/` | Base gardener skill (mandates apply) |
| `digital-gardener/references/guidelines.md` | `karx.github.io/` | WikiLink rules, tag taxonomy |
| `scripts/inbox_score.py` | `d:\src\ebrain/` | Stage 1 prioritisation script |

---

## Principles Quick Reference

| Principle | Source |
|-----------|--------|
| Topology over Timeline | digital-gardener |
| Connections over Containers | digital-gardener |
| Zero Authority | digital-gardener |
| Atomic Suggestions | digital-gardener |
| Context is Surface Area | PKM-Engineering-System-Prompt |
| Isolation Zero | GARDEN_GUIDELINES |
| Published Gate | GARDEN_GUIDELINES |
| Pipeline Order | ebrain-pipeline |
