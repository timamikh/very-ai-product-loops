---
node_type: process-overview
title: very-ai-product-loops — Process Overview
status: draft
version: 0.10.0
updated: 2026-08-18
---

# very-ai-product-loops

A product-agnostic workflow that takes a product from **idea → sprint plan** through **nested,
gated loops**. **One sentence:** the agent prepares every artifact from real sources; the human
decides at the forks; the loops refresh at their own pace and feed each other in both directions.
The framework separates **mechanism from content**: a thin, stable process skeleton plus pluggable
methods (a **library**) and pluggable product stages (**statuses**).

## 1. Philosophy (the rules the agent lives by)

1. **Agent prepares, human decides.** The agent gathers facts, drafts artifacts, and proposes
   defaults (marked ⚙️). The human makes decisions at forks and approves.
2. **Facts only from sources.** Every field traces to a source (a document, a metric, a git
   artifact, or a dated human decision). Missing data is surfaced as `— to clarify —`, never filled
   with a guess.
3. **Everything is dated, nothing is overwritten.** Every artifact keeps a dated change log:
   *how it was → what changed → why → what triggered it*.
4. **Confidence is explicit.** Every claim carries a tag: `assumption` · `sourced` · `validated` ·
   `refuted`. Early steps are mostly assumptions; lower steps harden them.
5. **Help, don't constrain.** Gates are checklists that report what is still open — they guide,
   they do not lock. You can descend with gaps; the framework flags them.
6. **One writer of the canon, many readers.** The **orchestrator** — the agent holding the human's
   session — is the only agent that writes the shared canon: artifact sections, registers,
   `state.yaml`, ticks, change log. Subagents return text, accepted against a passport, never on
   trust; the one exception is a `draft` writing only its own worklog. The contract is
   [`OPERATING-LOOP.md`](OPERATING-LOOP.md) → *Delegation*.

## 2. Architecture: four planes

```
┌─ Process core (steps/) ── thin skeleton: step goal, gate checklist, movement rules,
│                           register touchpoints, artifact structure. NO methods inside.
├─ Registers ────────────── metrics · hypotheses · risks (vertical, living, shared state)
├─ Library (tool-skills/library/) ─ product methods as skills
└─ Statuses (statuses/) ─── product stages as config: concept-viability · PMF · growth
```

**How the planes interlock — softly (rule 5):** a **step** names the sections and gate and
*recommends* a tool per section; a **status** re-prioritizes goals and *highlights* tools for the
stage; the **human** overrides anything; the **registers** are the shared state tools read and write.
Method is swappable, skeleton is stable. The pluggable skills live under
[`tool-skills/`](../tool-skills/README.md) (`library/` · `operations/` · `outputs/`); which dial to
turn is [`EXTENDING.md`](../EXTENDING.md).

## 3. The document model: three homes

A value lives in **exactly one** of three homes:

- **Worklog** (`<step-folder>/<tool>.md`) — the **source of truth**: where a method's inputs,
  reasoning and numbers are worked out. One per method.
- **Registers** (`registers/`) — the canon for the shared ids `H-`/`R-`/`M-`: vertical state that
  flows across steps ([`REGISTERS.md`](REGISTERS.md)).
- **Artifact** (`<n>-<slug>.md`) — the **projection of the worklog** into the step template's fixed
  shape: the thesis a human reads and signs. It holds nothing the worklog does not.

The projection runs **worklog → artifact**; the registers sit **alongside**, cited by id from both.
This split is why the console can drill from a signed section back to where it was worked, and why
a number has exactly one place to change.

## 4. The loop model

Nested loops refreshing at different cadences — the lower, the more often, the more it leans on
aggregated data over interview. All timeframes are indicative (`~`), not limits.

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

## 5. The rest of the map — canonical elsewhere

- **The six steps** (`steps/N-*/README.md`) own each step's goal, gate, skeleton and tools. One
  orientation rule: Step 3 = *choices and direction* (qualitative), Step 4 = *instruments and
  resources* (quantitative).
- **Statuses** (`concept-viability` · `PMF` · `growth`) parameterize the loops —
  [`statuses/README.md`](../statuses/README.md); an empty `per_step` never blocks.
- **The library** of methods — [`tool-skills/library/README.md`](../tool-skills/library/README.md);
  the **consumers** of the structure (outputs, the read-only console, the linter) read the folders
  directly, so structure is the only contract.
- **Vocabulary and on-demand canon** — [`reference/GLOSSARY.md`](reference/GLOSSARY.md) and
  [`process/reference/`](reference/README.md), read at named moments.
