---
node_type: process-overview
title: very-ai-product-loops — Process Overview
status: draft
version: 0.9.1
updated: 2026-08-16
---

# very-ai-product-loops

A product-agnostic workflow that takes a product from **idea → sprint plan** through
**nested, gated loops**.

**One sentence:** the agent prepares every artifact from real sources; the human decides
at the forks; the loops refresh at their own pace and feed each other in both directions.

The framework separates **mechanism from content**: a thin, stable process skeleton, plus
pluggable methods (a **library**) and pluggable product stages (**statuses**). The rules of
the game stay fixed; the methods themselves — and how each product stage prioritizes them —
are swappable and extensible per company, without forking the framework.

---

## 1. Philosophy (the rules the agent lives by)

1. **Agent prepares, human decides.** The agent gathers facts, drafts artifacts, and
   proposes defaults (marked ⚙️). The human makes decisions at forks and approves.
2. **Facts only from sources.** Every field traces to a source (a document, a metric, a git
   artifact, or a dated human decision). Missing data is surfaced as "— to clarify —", never
   filled with a guess.
3. **Everything is dated, nothing is overwritten.** Every artifact — narrative included —
   keeps a dated change log: *how it was → what changed → why → what triggered it*. Read the
   history and understand the motivation, not just the current state.
4. **Confidence is explicit.** Every claim carries a tag: `assumption` · `sourced` ·
   `validated` · `refuted`. Early steps are mostly assumptions; lower steps harden them.
5. **Help, don't constrain.** Gates are checklists that report what is still open — they
   guide, they do not lock. You can descend with gaps; the framework flags them.
6. **One writer of the canon, many readers.** The **orchestrator** — the agent holding the human's
   session — is the only agent that writes the **shared canon**: the artifact sections, the registers,
   `state.yaml`, the gate ticks and the change log. Subagents **return text** and are accepted against
   a passport, never on trust; the one exception is a `draft` subagent, which writes **only its own
   worklog** (the draft the orchestrator then projects). The contract is
   [`OPERATING-LOOP.md`](OPERATING-LOOP.md) → *Delegation*.

---

## 2. Architecture: four planes

```
┌─ Process core (steps/) ── thin skeleton: step goal, gate checklist, movement rules,
│                           register touchpoints, artifact structure (sections + IDs).
│                           NO methods inside.
├─ Registers ────────────── metrics · hypotheses · risks (vertical, living, shared state)
├─ Library (tool-skills/library/) ─ product methods as skills (segmentation, pricing-strategy, jtbd-concept…)
└─ Statuses (statuses/) ─── product stages as config: concept-viability · PMF · growth
```

The **fixed core** (`steps/` · `registers/` · `statuses/` and the rules in `process/`) is opposed by the
**pluggable skills** under [`tool-skills/`](../tool-skills/README.md), in three planes: `library/`
(product methods), `operations/` (runtime skills — `handoff`, `metrics-capture`, `source-intake`,
`orchestration`, `theses`), and `outputs/` (the output layer, §10). Companies swap or extend any
tool-skill without forking the core; which dial to turn is [`EXTENDING.md`](../EXTENDING.md).

**How the planes interlock — softly (per rule 5):** a **step** says "produce sections A, B, C and pass
gate G" and *recommends* library tools per section; a **status** re-prioritizes goals and *highlights*
the tools for the current stage; the **human** overrides anything; the **registers** are the shared
state tools read and write. The step owns the **artifact skeleton** (which sections exist, with stable
IDs); tools **fill** sections with their own method. Method is swappable; skeleton is stable.

---

## 3. The document model: three homes

The work a step produces is not one file but three homes, and a value lives in **exactly one** of them:

- **Worklog** (`<step-folder>/<tool>.md`) — the **source of truth**: where a method's inputs, reasoning
  and numbers are worked out. One per method (`node_type: worklog`).
- **Registers** (`registers/`) — the canon for the shared ids `H-`/`R-`/`M-`: vertical state that flows
  across steps (§6). A value referenced from many places lives here once, by id.
- **Artifact** (`<n>-<slug>.md`) — the **projection of the worklog** into the step template's fixed
  shape: the thesis a human reads and signs. It holds nothing the worklog does not.

The projection runs **worklog → artifact**; the registers sit **alongside**, referenced by id from both.
The artifact does **not** grow out of the registers — it is the worklog made presentable, with register
ids cited in it. This split is why the console can drill from a signed section back to where it was
worked, and why a number has exactly one place to change. One id threads the chain: the same `<tool>`
names the section marker, the skill folder and the worklog file.

---

## 4. The loop model

Not a waterfall — nested loops that refresh at different cadences. The lower the loop, the
more often it runs and the more it leans on aggregated data (git, metrics, KB) over interview.

```
Concept / Analysis (1–2)   revisited on pivot / market shift      — rarely
  └ Strategy (3–4)         ~3–12 mo horizon, reviewed ~quarterly
      └ Tactics (5)        ~1–3 mo, stage-gate ~monthly
          └ Sprint (6)     ~1–2 wk, every sprint
```

**All timeframes are indicative (`~`), not limits — each team moves at its own pace.**

**Loops feed each other both ways.** A sprint can refute a hypothesis → a trigger to rework
tactics. Tactics hitting a metric ceiling → a trigger to revisit strategy. Each step declares
its cadence and what it **invalidates** up and down when it changes.

**How a single pass runs** — orient (status + step) → focus on a checklist item → recommend the fitting
tool → check prerequisites **and size the pass** (split across subagents, or solo — decided aloud) →
fill gaps → clarify → act, directly or through briefed subagents → update the
checklist/registers/change-log → loop. This runtime is [`OPERATING-LOOP.md`](OPERATING-LOOP.md);
everything below is data it consumes.

---

## 5. The six steps (essence only)

Steps hold only the essence: goal, output, register touchpoints, and *recommended* tools. The "how" of
each method lives in the [library](../tool-skills/library/README.md); the goal shape and tool emphasis
are set by the active [status](../statuses/README.md). Each step's goal, gate checklist, register
touchpoints and tools are **canonical in its own** `steps/N-*/README.md`, not restated here (a second
copy is where the lists drift).

| # | Step | Horizon (~) | Cadence (~) | Output |
|---|------|-------------|-------------|--------|
| 1 | **Concept** | product lifetime | on pivot / major learning | `1-concept.md` |
| 2 | **Analysis** | ~6–12 mo view | ~quarterly / on market shift | `2-analysis.md` |
| 3 | **Strategy** | ~3–12 mo | reviewed ~quarterly | `3-strategy.md` |
| 4 | **Strategic Plan** | ~3–12 mo | with strategy / on shift | `4-strategic-plan.md` |
| 5 | **Tactical Plan** | ~1–3 mo | ~monthly | `5-tactical-plan.md` |
| 6 | **Sprint Plan** | ~1–2 wk | every sprint | `6-sprint-plan.md` |

Strategy (3–4) is organized around **goals / bets / metrics** — never org structure. Execution (5–6) is
organized around **directions**, an editable instance config (default: `development` · `go-to-market` ·
`back-office`; the direction is `go-to-market`, not `growth`, to avoid colliding with the `growth`
**status**). One boundary is crossed most often:

> **Boundary 3 ↔ 4:** Step 3 = *choices and direction* (qualitative). Step 4 = *instruments
> and resources* (quantitative). If it is a choice → Step 3; a number, a model, or a mitigation → Step 4.

---

## 6. The three vertical registers

Metrics, hypotheses and risks are **living objects** — born once, refined downward, results flowing back
up, **not re-authored per step**. They are the shared state tools read and write, and the canon for the
`H-`/`R-`/`M-` ids cited across artifacts. The field schemas, the metric-tree split (`metric-tree.md`
definitions + append-only `metrics.csv` values), the id discipline and what earns a *fourth* register
live in [`REGISTERS.md`](REGISTERS.md) — not restated here.

| Register | Born at | Refined at |
|----------|---------|------------|
| **Metrics** | Step 4 | 5 (nodes to move) → 6 (task ↔ metric) |
| **Hypotheses** | Step 1/3 | 4 (quantify) → 5 (test design) → 6 (experiment tasks) |
| **Risks** | Step 2 | 3 (product) → 4 (mitigation) → 5 (period blockers) |

---

## 7. Statuses (product-stage plane)

A **status** is the product's current stage. It parameterizes the loops **per step**: which goals take
priority (optionally by direction) and which tools to lean on — the same section can call for different
methods at different stages (pains from interviews early, from internal metrics later). Defaults
(extensible — anatomy and how to add one in [`statuses/README.md`](../statuses/README.md)):

1. **concept-viability** — prototype/MVP to test that the product *can* be built and that there is
   *some* demand worth pursuing toward PMF.
2. **PMF** — first clients; validate repeatable value and monetization so it can be scaled.
3. **growth** — a working, profitable product to develop and expand.

> **A status may not yet define `per_step` for a step.** That does not block: the loop works by the step
> defaults, and at *Update state* the agent proposes filling that status's `per_step` from what the pass
> just learned — so statuses complete as a by-product of the first run, never left as standing stubs.

---

## 8. Library (method plane)

The [library](../tool-skills/library/README.md) is a catalog of product methods, each authored as a
**skill**: *what it is · when to apply it · how to do it · a template-fragment · an interview*. When a
step needs a section produced, the agent picks the right tool and follows it. The library is meant to
grow and be adapted — it is where company-specific or opinionated methods live, keeping the core neutral.

---

## 9. Cross-cutting conventions

The authority is [`CONVENTIONS.md`](CONVENTIONS.md); this is the map. Conventions are **not uniform
across file types** — a file's `node_type` selects which apply (the matrix is
[`reference/node-type-matrix.md`](reference/node-type-matrix.md)). The load-bearing notation:

- **Confidence tags** (`assumption`·`sourced`·`validated`·`refuted`) on every non-trivial claim in an
  artifact; a register uses a `confidence` column instead. Missing = `assumption`.
- **Stable handles** — a section `{#anchor}`, a table column `<!--c:key-->` (read instead of header
  prose, language-safe), an item id `H-`/`R-`/`M-`. Cross-artifact links are a relative path + the
  target `{#anchor}` — the one link canon.
- **Worklog → projection** — every method section is projected from its worklog (§3); one id threads the
  section marker, the skill folder and the worklog file.
- **Confirmation & gradation — two axes.** A human signs a section with `<!-- confirmed: date -->`
  (dropped on re-projection); a `rests-on` marker flags a signed thesis standing on unsigned ground. This
  is orthogonal to a **gradation** (a hypothesis's signal/decision, a risk's likelihood × impact) —
  never folded into one.
- **Dated change logs** on instance files (from→to·why·trigger); framework files log to `CHANGELOG.md`.
- **One mechanism, one way** · **forks: triage first** (2–4 options + ⚙️ default) · **no bare id/link in
  chat** · **soft gates** that report open items and never block descent.

---

## 10. Consumers of the structure — and what's deferred

The base artifacts are kept structured (stable IDs, column keys, source slots, typed links) for one
reason: **structure is the contract**, so anything that reads a folder can be a consumer without
per-instance wiring.

- **Outputs** ([`tool-skills/outputs/`](../tool-skills/outputs/README.md)) are the **output layer** —
  renderers read the structured instance and render views (`to-table` · `to-document` · `to-deck`);
  authored deliverables (`brief`, `interview`) write documents for use outside. Everything lands in the
  instance's `export-files/` — the mirror of `sources/` (in ↔ out). Company outputs stay **outside** the
  base and re-skin a base one into a house format; they don't fork it. Rendered views regenerate from
  source instead of being hand-maintained; authored documents are themselves the signed source.
- **The local console** ([`tools/ui/`](../tools/ui/README.md)) renders one instance as an interactive
  local view (cycle position, gate ticks, registers, metric series, open `— to clarify —`, change-log
  timeline). It is a **lens, not a home for values and not an interface to the process** — no write path.
  The human asks an agent, the agent runs the loop and writes the files, the console shows what the files
  now say.
- **The linter** ([`tools/lint.py`](../tools/lint.py)) is the other reader of the same structure — it
  holds a section's *shape* (the human holds its *meaning*), and it is the gate a change passes before it
  is done.

Still deferred by design, kept out of the base: **aggregators** that pull and merge product data from
git/metrics/KB, and **automation** of bottom-up refresh across loops — both can be added on top without
rework, precisely because the structure is the contract.

---

**Vocabulary and on-demand canon.** The entity names used above are defined once in
[`reference/GLOSSARY.md`](reference/GLOSSARY.md); the canon read at a named moment (column keys, the
config schema, the node_type matrix, worked examples) lives in
[`process/reference/`](reference/README.md), not in the always-loaded reading order.
