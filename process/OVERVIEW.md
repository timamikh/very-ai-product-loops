---
node_type: process-overview
title: very-ai-product-loops — Process Overview
status: draft
version: 0.12.0
updated: 2026-09-02
---

# very-ai-product-loops

A product-agnostic workflow that takes a product from **idea → sprint plan** through **nested,
gated loops**. **One sentence:** the agent prepares every artifact from real sources; the human
decides at the forks; the loops refresh at their own pace and feed each other in both directions.
The framework separates **mechanism from content**: a thin, stable process skeleton plus pluggable
methods (a **library**) and pluggable product stages (**statuses**).

This file is the **concept**. The rules are the non-negotiables in [`AGENTS.md`](../AGENTS.md),
each pointing at its one home; the procedure is [`OPERATING-LOOP.md`](OPERATING-LOOP.md); the
notation is [`CONVENTIONS.md`](CONVENTIONS.md).

## 1. Architecture: four planes

```
┌─ Process core (steps/) ── thin skeleton: goal · gate · touchpoints · artifact structure.
│                           NO methods inside.
├─ Registers ────────────── vertical, living, shared state — enumerated in REGISTERS.md
├─ Library (tool-skills/library/) ─ product methods as skills
└─ Statuses (statuses/) ─── product stages as config: concept-viability · PMF · growth
```

**How the planes interlock — softly.** A **step** names the sections and gate and *recommends* a
tool per section; a **status** re-prioritizes goals and *highlights* tools for the stage; the
**human** overrides anything; the **registers** are the shared state tools read and write. Gates
are checklists that report what is still open — they guide, they do not lock: you can descend with
gaps, and the framework flags them. The pluggable skills live under
[`tool-skills/`](../tool-skills/README.md) (`library/` · `operations/` · `outputs/`); which dial to
turn is [`EXTENDING.md`](../EXTENDING.md).

## 2. The document model: three homes

A value lives in **exactly one** of three homes:

- **Worklog** (`<step-folder>/<tool>.md`) — the **source of truth**, where a method's working is
  done. One per method.
- **Registers** (`registers/`) — the canon for the shared ids, vertical state that flows across
  steps ([`REGISTERS.md`](REGISTERS.md)).
- **Artifact** (`<n>-<slug>.md`) — the **projection of the worklog** into the step template's fixed
  shape: the thesis a human reads and signs. It holds nothing the worklog does not.

The projection runs **worklog → artifact**; the registers sit **alongside**, cited by id from both —
so a number has exactly one place to change, and a signed section drills back to where it was worked.

## 3. The loop model

Nested loops refreshing at different cadences — the lower, the more often, the more it leans on
aggregated data over interview; early steps are mostly assumptions, lower steps harden them.
Timeframes are indicative (`~`).

```
Concept / Analysis (1–2)   revisited on pivot / market shift      — rarely
  └ Strategy (3–4)         ~3–12 mo horizon, reviewed ~quarterly
      └ Tactics (5)        ~1–3 mo, stage-gate ~monthly
          └ Sprint (6)     ~1–2 wk, every sprint
```

**Loops feed each other both ways.** A sprint can refute a hypothesis → a trigger to rework
tactics; a metric ceiling → a trigger to revisit strategy. Each step declares its cadence and what
it invalidates up and down. The single-pass runtime is [`OPERATING-LOOP.md`](OPERATING-LOOP.md);
everything else is data it consumes.

## 4. The rest of the map — canonical elsewhere

- **The six steps** (`steps/N-*/README.md`) own each step's goal, gate, skeleton and tools. One
  orientation rule: Step 3 = *choices and direction* (qualitative), Step 4 = *instruments and
  resources* (quantitative).
- **Statuses** (`concept-viability` · `PMF` · `growth`) parameterize the loops —
  [`statuses/README.md`](../statuses/README.md).
- **The library** of methods — [`tool-skills/library/README.md`](../tool-skills/library/README.md);
  the consumers (outputs, console, linter) read the folders directly — structure is the only contract.
- **Vocabulary and on-demand canon** — [`reference/GLOSSARY.md`](reference/GLOSSARY.md) and
  [`process/reference/`](reference/README.md), read at named moments.
