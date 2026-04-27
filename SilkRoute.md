---
title: SilkRoute
type: project
status: scaffolding
tags: [hyperlocal, gig-economy, community, governance, bengaluru]
created: 2026-04-20
---

# SilkRoute

> A hyperlocal economy platform where skill meets community need — enabling individuals, funding shared roles, and growing governance from the ground up.

---

## The Problem

Neighborhoods have unmet micro-needs (parking management, wiring, traffic flow) and underutilized human potential. The formal economy can't touch these at this granularity. The gig economy extracts value without returning it to the community.

---

## The Flywheel

```
Learn Skill (SilkRoute upskilling)
    ↓
Pick up local Work (marketplace)
    ↓
Complete → Earn Tokens + Reputation
    ↓
Tokens accumulate → Shared Fund grows
    ↓
Shared Fund enables Community Roles
    ↓
Community Roles create more local opportunity
    ↓ (repeat)
```

---

## Core Entities

| Entity             | Description                                                                                                     |
| ------------------ | --------------------------------------------------------------------------------------------------------------- |
| **Member**         | Anyone in the locality. Has a skill profile, time availability, reputation score                                |
| **Skill**          | Learned or verified capability. Unlocks job eligibility                                                         |
| **Job**            | A discrete work item posted by a member or the community. Has skill requirements + time estimate + token reward |
| **Claim**          | Member picks up a job. Proof of completion unlocks token release                                                |
| **Token**          | Unit of exchange. Earned by doing work. Spendable locally or convertible                                        |
| **Shared Fund**    | Pool fed by a % of every completed job. Governed by contribution weight                                         |
| **Community Role** | Ongoing local public-good job (parking attendant, traffic manager) funded by Shared Fund                        |
| **Skill Module**   | Learning unit inside SilkRoute. Completion unlocks eligibility for related jobs                                 |

---

## Product Layers

### 1. Profile & Skill Layer
- Onboarding: locality, available hours, existing skills
- Skill modules: short, mobile-first, practical (reduces skill gap fast)
- Skill verification: peer review, auto-test, or completed job count threshold

### 2. Work Marketplace
- Job posting: any member can post a need
- Smart matching: Skill + Time availability → suggested volunteers
- Claim flow: Accept → Do → Submit proof → Peer confirm → Token release
- Job types:
  - **One-off**: fix a leak, set up wifi router
  - **Recurring**: weekly parking management shift
  - **Community Role**: ongoing funded position

### 3. Token & Reward Layer
- Earning: complete verified work
- Spending: post jobs, access premium skill modules, convert to cash
- Shared Fund contribution: X% of every job payout auto-routes to community pool

### 4. Governance Layer (emergent)
- Governance weight = cumulative community contribution (jobs enabled + completed)
- Fund allocation proposals: any member with threshold weight can propose
- Voting: weighted by contribution, not just stake
- Community Roles are funded via approved proposals

---

## Bengaluru Pilot: Target Work Items

| Work Item | Job Type | Skill Required |
|---|---|---|
| Shared parking coordination | Recurring | Communication, scheduling |
| Internet / wiring setup | One-off | Basic networking |
| Traffic Management Employee | Community Role (funded) | Traffic awareness, communication |
| CCTV maintenance | One-off | Basic electronics |
| Common area cleaning roster | Recurring | None (entry-level) |

---

## MVP Scope (Phase 1)

**Goal**: One locality, real transactions, shared fund seeded and growing.

- [ ] Member onboarding (locality + skills + time)
- [ ] Job posting + claiming flow
- [ ] Proof of completion (photo/text)
- [ ] Peer confirmation (2-of-3 neighbours)
- [ ] Token ledger (can be simple points to start)
- [ ] Shared Fund counter (visible, transparent)
- [ ] 3–5 seed skill modules

**Out of scope for Phase 1**: governance voting, token convertibility, multi-locality

---

## Shared Fund: Seeding & Sustainability

**Seeding sources (bootstrap only):**
| Source | What they give | What they get |
|---|---|---|
| RWA | Portion of maintenance budget | Platform manages community roles on their behalf |
| Local Vendors | Cash contribution | Access to verified local talent pool, visibility to members |
| Open Fund | Public/crowdfunded contributions | Governance weight proportional to contribution |

**Sustainability principle**: After bootstrap, the fund must be self-replenishing.
- X% of every completed job auto-routes to Shared Fund
- Community Role salaries are funded from this pool
- Platform takes 0 cut — the community is the platform

**Vendor entity (new):**
- Local businesses can join as Vendor members
- Post jobs (just like residents), contribute to fund
- Cannot hold governance weight above a cap (prevents vendor capture)

---

## Open Questions

- [x] **Fund seeding**: RWA + local vendor contributions + open fund *(resolved)*
- [x] **Token convertibility**: Cash-out (fiat off-ramp) available from Phase 1. 1 SilkCoin = ₹10 fixed rate. Real ₹ held in Shared Fund, SilkCoins are the interface. *(resolved)*
- [ ] **Shared Fund %**: What % of each job goes to the fund? Too high kills worker incentive, too low starves community roles.
- [ ] **Job dispute resolution**: Who arbitrates a rejected proof-of-completion?
- [ ] **Skill verification**: Self-declared → peer-verified → job-count verified. Minimum bar to claim a job?
- [ ] **Community Role hiring**: Open bid, or governance vote on a specific person?
- [ ] **Vendor governance cap**: What's the max weight a vendor can hold?

---

## Analogues & Differentiators

| Platform | What they do | What SilkRoute does differently |
|---|---|---|
| TaskRabbit / Urban Company | Gig marketplace | Community keeps the value, not a platform |
| Timebanks | Time-for-time exchange | Allows money + token hybrid, has upskilling |
| DAOs | Token governance | Hyperlocal, physical, real-world work |
| RWA (Resident Welfare Assoc.) | Neighbourhood governance | Bottom-up, contribution-weighted, not elected |

---

## Next Steps

1. Answer open questions (fund seeding priority)
2. Define token mechanics precisely
3. Sketch the member onboarding flow
4. Identify pilot locality in Bengaluru + founding member group
