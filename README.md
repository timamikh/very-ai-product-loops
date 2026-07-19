---
node_type: readme
title: very-ai-product-loops — README
status: draft
version: 0.6.0
updated: 2026-07-19
---

# very-ai-product-loops

**A product-strategy workflow you run *with* an AI agent — from a raw idea to a concrete sprint
plan, without hand-waving.**

The agent does the heavy lifting (research, drafting, bookkeeping) from *your real materials*.
You make the calls at every fork. Nothing is invented; every claim is tagged with where it came
from and how sure we are.

> Idea → Analysis → Strategy → Strategic plan → Tactical plan → Sprint plan — as **nested loops**
> that keep feeding back into each other, not a one-way waterfall.

---

## What is this, in one minute

Most "strategy" lives in slide decks that go stale the day after the offsite. This framework makes
strategy a **living, versioned working area in your repo** that an agent maintains alongside you.

- **Six steps**, from the product's whole-lifetime concept down to the next two-week sprint. Each
  step produces one artifact (a markdown file).
- **Three living registers** — your hypotheses, your risks, your metrics — that are born at the
  step where they first matter and get sharpened as you descend. They are the product's memory.
- **The agent prepares, you decide.** The agent drafts from sources and asks you concise
  questions (2–4 options + a recommended default) at genuine product decisions. It never fills a
  blank with a guess — a gap stays visibly marked `— to clarify —`.
- **Everything is dated and nothing is overwritten.** Every file keeps a change log: how it was →
  what changed → why. You can always see the reasoning, not just the current state.

Who it's for: a PM / founder / CPO who wants to move a product forward with an agent and keep a
trustworthy paper trail — instead of a folder of disconnected docs.

## How you actually work with it

You don't fill templates alone. A working session looks like this:

1. You tell the agent what you want to move (e.g. "let's firm up the strategy").
2. The agent orients — reads where the product is, picks the right method, checks it has the
   inputs it needs. If something's missing, it asks you or offers to go get it (draft an interview
   guide, pull metrics).
3. It drafts the section from your real materials, tags every claim with a source and a confidence
   level, and marks its own proposals with ⚙️.
4. At each real product fork it stops and asks you — with options and a recommendation — and waits.
5. It records what changed (the artifact, the registers, the change log) and suggests what's next.

You descend step by step; when something downstream disproves something upstream (a refuted
hypothesis, a changed segment), that signal bubbles back up. That's the "loops" part.

## The six steps

| # | Step | Horizon (~) | You end up with |
|---|------|-------------|-----------------|
| 1 | Idea / Concept | product lifetime | `passport.md` — what it is, for whom, why it wins |
| 2 | Analysis | ~6–12 mo | `analysis.md` — market, competitors, substitutes, sizing |
| 3 | Strategy | ~3–12 mo | `strategy.md` — where to play, how to win, pricing, channels |
| 4 | Strategic Plan | ~3–12 mo | `strategic-plan.md` — metric tree, unit economics, risks |
| 5 | Tactical Plan | ~1–3 mo | `tactical-plan.md` — the bets for this quarter, guardrails |
| 6 | Sprint Plan | ~1–2 wk | `sprint-plan.md` — the prioritized items for the next sprint |

Timeframes are indicative — each team moves at its own pace.

## Quickstart

You add the framework to a repository through an AI agent (Claude Code / Claude Desktop), the same
way you'd add any agent framework — point the agent at this repo and ask:

> "Add the very-ai-product-loops framework from
> https://github.com/timamikh/very-ai-product-loops to this repository and run product setup."

The agent then **vendors** the framework (read-only, pinned to a version), asks for your existing
materials, and **scaffolds a `product/` working area** — pre-filled from whatever you have, with
gaps clearly marked. It hands back a placement report and the first step to work on. See
[`install/README.md`](install/README.md) for the details.

Your product docs live in `product/`, kept **separate from your code** so they never interfere with
development. The framework files stay read-only and are updated by bumping the version.

## Architecture — a fixed core + pluggable tool-skills

The framework separates **mechanism from content**. The rules of the game stay fixed; the methods
and how each stage prioritizes them are swappable per company, without forking the framework.

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

## How the agent reads the repo (for the curious)

An agent working here boots in a fixed order — the environment auto-loads the root
[`CLAUDE.md`](CLAUDE.md), which sends it through the rules first:

1. [`process/OVERVIEW.md`](process/OVERVIEW.md) — the model and the philosophy it lives by.
2. [`process/OPERATING-LOOP.md`](process/OPERATING-LOOP.md) — the runtime: how one pass of a step runs.
3. [`process/CONVENTIONS.md`](process/CONVENTIONS.md) — notation: confidence tags, sources, IDs, forks, change logs.
4. [`process/REGISTERS.md`](process/REGISTERS.md) — register schemas (hypotheses / risks / metric tree).
5. Then the instance: its `HANDOFF.md` (if present) → `sources/INDEX.md` → only the artifacts the task needs.

`CLAUDE.md` is the enforced version of this list — skipping the rules and working from a task
description alone is how they get violated silently.

## Status

Early draft, building in phases:

- **Phase 0 — Process foundation** → [`process/OVERVIEW.md`](process/OVERVIEW.md) · [operating loop](process/OPERATING-LOOP.md) · [conventions](process/CONVENTIONS.md) _(merged)_
- **Phase 1 — Step/tool/status anatomy + golden exemplar (Step 1, all 4 tools)** _(merged)_
- **Phase 2 — Steps 2–6 skeletons + [register schemas](process/REGISTERS.md) + artifact templates + library fully authored** _(templates + full library done; run-hardening continues)_
- **Onboarding — [`product-setup`](.claude/skills/product-setup/SKILL.md) + [install](install/README.md)** _(merged)_
- **Phase 3 — Agent rules ([CLAUDE.md](CLAUDE.md)), examples, contribution + versioned branching** _(CLAUDE.md merged; contribution/branching next)_
- **Phase 4 — base [adapters](tool-skills/adapters/README.md) (shipped) · aggregators, automation** _(base adapters done; aggregators/automation later)_

## Change log

### 2026-07-19 — human-first rewrite
- **From → To:** the README now opens for a *human* landing on the framework (what it is, who it's
  for, how a working session goes, a quickstart); the agent reading-order moved into a clearly-labeled
  "How the agent reads the repo" section (`CLAUDE.md` remains the enforced version).
- **Why:** the previous top was agent-facing ("For agents — start here") and read as internal spec,
  not an entry point for a person evaluating the framework.
- **Trigger:** user request, 2026-07-19.

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
