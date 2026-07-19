---
node_type: readme
title: very-ai-product-loops — README
status: draft
version: 0.5.0
updated: 2026-07-19
---

# very-ai-product-loops

A product-agnostic workflow that takes a product from **idea → sprint plan** through
**nested, gated loops**.

> The agent prepares every artifact from real sources; the human decides at the forks;
> the loops refresh at their own pace and feed each other in both directions.

## For agents — start here

Before doing ANY work in this repo (or in a product instance built on it), read the rules in
this order — they are normative, not descriptive:

1. [`process/OVERVIEW.md`](process/OVERVIEW.md) — the model **and the rules the agent lives by** (§1 Philosophy).
2. [`process/OPERATING-LOOP.md`](process/OPERATING-LOOP.md) — the runtime: how one pass of a step runs, incl. register updates.
3. [`process/CONVENTIONS.md`](process/CONVENTIONS.md) — notation: confidence tags, sources, IDs, forks, change logs.
4. [`process/REGISTERS.md`](process/REGISTERS.md) — register schemas (hypotheses / risks / metric tree).
5. Then the instance: its `HANDOFF.md` (if present) → `sources/INDEX.md` → the artifacts your task needs.

Skipping 1–4 and working from a handoff or task description alone is how rules get violated
silently — the handoff restores *state*, not *rules*.

The framework separates **mechanism from content**: a thin, stable process skeleton, plus
pluggable methods (a **library**) and pluggable product stages (**statuses**). The rules of
the game stay fixed; the methods themselves — and how each product stage prioritizes them —
are swappable and extensible per company, without forking the framework.

## Architecture — a fixed core + pluggable tool-skills

**The fixed core** — the rules and the board; it changes rarely:

- **Process core** (`steps/`) — thin skeleton per step: goal, gate checklist, movement rules, register touchpoints, artifact structure. No methods inside.
- **Registers** — three living, vertical objects: metrics · hypotheses · risks.
- **Statuses** (`statuses/`) — product stages as config (concept-viability · PMF · growth, extensible). See [`statuses/README.md`](statuses/README.md).
- **Rules** (`process/`) — the normative model, loop, conventions, register schemas.

**The pluggable skills** — instruction skills the agent picks up and runs, grouped under [`tool-skills/`](tool-skills/README.md) and swappable per company without forking the core:

- **Library** (`tool-skills/library/`) — product methods as skills: what / when / how / template. See [`tool-skills/library/README.md`](tool-skills/library/README.md).
- **Operations** (`tool-skills/operations/`) — runtime skills for how the agent works across sessions (e.g. `handoff`). See [`tool-skills/operations/README.md`](tool-skills/operations/README.md).
- **Adapters** (`tool-skills/adapters/`) — the output layer: `to-table` · `to-document` · `to-deck`. Base adapters ship here (neutral); company-specific formats stay external and specialize them. See [`tool-skills/adapters/README.md`](tool-skills/adapters/README.md).

To find a skill for a task, pick the category by phase (produce a section → `library`; render a deliverable → `adapters`; carry state across a restart → `operations`); [`tool-skills/README.md`](tool-skills/README.md) has the discovery rule.

## The six steps

| # | Step | Horizon (~) | Output |
|---|------|-------------|--------|
| 1 | Idea / Concept | product lifetime | `passport.md` |
| 2 | Analysis | ~6–12 mo | `analysis.md` |
| 3 | Strategy | ~3–12 mo | `strategy.md` |
| 4 | Strategic Plan | ~3–12 mo | `strategic-plan.md` |
| 5 | Tactical Plan | ~1–3 mo | `tactical-plan.md` |
| 6 | Sprint Plan | ~1–2 wk | `sprint-plan.md` |

Timeframes are indicative — each team moves at its own pace. See
[`process/OVERVIEW.md`](process/OVERVIEW.md) for the full model.

## Status

Early draft, building in phases:

- **Phase 0 — Process foundation** → [`process/OVERVIEW.md`](process/OVERVIEW.md) · [operating loop](process/OPERATING-LOOP.md) · [conventions](process/CONVENTIONS.md) _(merged)_
- **Phase 1 — Step/tool/status anatomy + golden exemplar (Step 1, all 4 tools)** _(merged)_
- **Phase 2 — Steps 2–6 skeletons + [register schemas](process/REGISTERS.md) + artifact templates + library fully authored** _(templates + full library done; run-hardening continues)_
- **Onboarding — [`product-setup`](.claude/skills/product-setup/SKILL.md) + [install](install/README.md)** _(merged)_
- **Phase 3 — Agent rules ([CLAUDE.md](CLAUDE.md)), examples, contribution + versioned branching** _(CLAUDE.md merged; contribution/branching next)_
- **Phase 4 — base [adapters](tool-skills/adapters/README.md) (shipped) · aggregators, automation** _(base adapters done; aggregators/automation later)_

## Change log

### 2026-07-19 — `tool-skills/` umbrella
- **From → To:** the architecture section now frames a **fixed core** vs **pluggable tool-skills**;
  `library/` and `adapters/` moved under `tool-skills/`, and `handoff` relocated to a new
  `tool-skills/operations/` plane. Added the skill-discovery rule.
- **Why:** the three pluggable planes are one kind of thing (skills the agent runs) and belong
  together, opposite the fixed core; enables a single discovery rule.
- **Trigger:** restructure discussion, 2026-07-19.

### 2026-07-19 — clarified the mechanism/content one-liner
- **From → To:** replaced the "*how* you define value, segment users, or test a hypothesis …"
  example list with the universal "the methods themselves — and how each product stage prioritizes
  them — are swappable and extensible per company …" (mirrors `process/OVERVIEW.md`).
- **Trigger:** user review, 2026-07-19.
