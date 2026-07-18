---
node_type: process-overview
title: very-ai-product-loops — Process Overview
status: draft
version: 0.4.0
updated: 2026-07-18
---

# very-ai-product-loops

A product-agnostic workflow that takes a product from **idea → sprint plan** through
**nested, gated loops**.

**One sentence:** the agent prepares every artifact from real sources; the human decides
at the forks; the loops refresh at their own pace and feed each other in both directions.

The framework separates **mechanism from content**: a thin, stable process skeleton, plus
pluggable methods (a **library**) and pluggable product stages (**statuses**). The rules of
the game stay fixed; *how* you define value, segment users, or test a hypothesis is swappable
and can be grown or adapted per company — without forking the framework.

---

## 1. Philosophy (the rules the agent lives by)

1. **Agent prepares, human decides.** The agent gathers facts, drafts artifacts, and
   proposes defaults (marked ⚙️). The human makes decisions at forks and approves.
2. **Facts only from sources.** Every field traces to a source (a document, a metric, a git
   artifact, or a dated human decision). Missing data is surfaced as "— to clarify —", never
   filled with a guess.
3. **Everything is dated, nothing is overwritten.** Every artifact — narrative included —
   keeps a dated change log: *how it was → what changed → why → what triggered it*. Agents
   must be able to read the history and understand the motivation, not just the current state.
4. **Confidence is explicit.** Every claim carries a tag: `assumption` · `sourced` ·
   `validated` · `refuted`. Early steps are mostly assumptions; lower steps harden them.
5. **Help, don't constrain.** Gates are checklists that report what is still open — they
   guide, they do not lock. You can descend with gaps; the framework flags them.

---

## 2. Architecture: four planes

```
┌─ Process core (steps/) ── thin skeleton: step goal, gate checklist, movement rules,
│                           register touchpoints, artifact structure (sections + IDs).
│                           NO methods inside.
│
├─ Registers ────────────── metrics · hypotheses · risks (vertical, living, shared state)
│
├─ Library (library/) ───── methods as skills: value-definition, segmentation,
│                           segment-pains, competitor-analysis, market-sizing, metric-tree,
│                           unit-economics, financial-model, jtbd… each = what / when / how / template
│
└─ Statuses (statuses/) ─── product stages as config: concept-viability · PMF · growth
                            (extensible): priority goals + its own tool set
```

Alongside the four planes, an **instance** also carries two supporting mechanisms, defined in
[`CONVENTIONS.md`](CONVENTIONS.md) and [`OPERATING-LOOP.md`](OPERATING-LOOP.md):
- **`sources/`** — external-data access notes and captured evidence, indexed in `sources/INDEX.md`
  (see *Raw data & access* in CONVENTIONS: captured values go to the registers, secrets never into
  artifacts, raw captures deleted once their values land).
- **`HANDOFF.md`** — session-to-session state transfer, written by the `handoff` library tool at a
  session boundary (it restores *state, not rules* — the reader still starts from `process/`).

**How the planes interlock — softly (per rule 5):**
- A **step** says "at this stage produce sections A, B, C and pass gate G" and *recommends*
  library tools per section.
- A **status** re-prioritizes goals and *highlights* the relevant tools for the current
  product stage.
- The **human** overrides anything. Nothing is hard-wired.
- **Registers** are the shared state that tools read and write.

> The step owns the **artifact skeleton** (which sections must exist, with stable IDs).
> Tools **fill** specific sections with their own method, mini-template, and interview.
> Method is swappable; skeleton is stable.

**How a single pass actually runs** — orient (status + step) → focus on a checklist item →
recommend the fitting tool → check the tool's prerequisites → fill gaps → clarify → act →
update the checklist/registers/change-log → loop. This runtime is
[`OPERATING-LOOP.md`](OPERATING-LOOP.md); everything below is data it consumes.

---

## 3. The loop model

Not a waterfall — nested loops that refresh at different cadences. The lower the loop, the
more often it runs and the more it leans on aggregated data (git, metrics, KB) over interview.

```
Idea / Analysis (1–2)      revisited on pivot / market shift      — rarely
  └ Strategy (3–4)         ~3–12 mo horizon, reviewed ~quarterly
      └ Tactics (5)        ~1–3 mo, stage-gate ~monthly
          └ Sprint (6)     ~1–2 wk, every sprint
```

**All timeframes are indicative (`~`), not limits — each team moves at its own pace.**

**Loops feed each other both ways.** A sprint can refute a hypothesis → a trigger to rework
tactics. Tactics hitting a metric ceiling → a trigger to revisit strategy. Each step declares
its cadence and what it **invalidates** up and down when it changes. This bidirectional
trigger keeps the cascade alive instead of stale.

---

## 4. The six steps (essence only)

Steps hold only the essence: goal, output, register touchpoints, and *recommended* tools.
The "how" of each method lives in the [library](../library/README.md); the goal shape and
tool emphasis are set by the active [status](../statuses/README.md).

| # | Step | Horizon (~) | Cadence (~) | Output |
|---|------|-------------|-------------|--------|
| 1 | **Idea / Concept** | product lifetime | on pivot / major learning | `passport.md` |
| 2 | **Analysis** | ~6–12 mo view | ~quarterly / on market shift | `analysis.md` |
| 3 | **Strategy** | ~3–12 mo | reviewed ~quarterly | `strategy.md` |
| 4 | **Strategic Plan** | ~3–12 mo | with strategy / on shift | `strategic-plan.md` |
| 5 | **Tactical Plan** | ~1–3 mo | ~monthly | `tactical-plan.md` |
| 6 | **Sprint Plan** | ~1–2 wk | every sprint | `sprint-plan.md` |

Strategy (3–4) is organized around **goals / bets / metrics** — never org structure.
Execution (5–6) is organized around **directions**, an editable instance config (default:
`development` · `go-to-market` · `back-office`); the number of directions can change depending on
the product's specifics. (The direction is named `go-to-market`, not `growth`, to avoid colliding
with the `growth` **status** — a stage of maturity, not a stream of work.)

- **1 · Idea / Concept** — Goal: capture the concept — who it's for, their problems, how the
  product solves them, and its value/defensibility hypothesis. Seeds the **hypothesis
  register**. Recommended tools: `concept-formation`, `segmentation`, `segment-pains`,
  `value-definition`.
- **2 · Analysis** — Goal: understand market and competition and conclude *where the
  opportunity/threat is* (analysis without a "so what" is inert). Seeds the **risk register**.
  Recommended tools: `market-sizing`, `competitor-analysis`, `substitutes`.
- **3 · Strategy** — Goal (qualitative choices): where to play, how to win, and the bets we
  make. Seeds strategy bets into the **hypothesis register** and product risks. Recommended
  tools: `where-to-play-how-to-win`, `uvp-cpv`, `value-definition` (revisited — derivative
  values surface here, as they need a customer or scale), `channels-expansion`.
- **4 · Strategic Plan** — Goal (quantitative instruments): make the strategy measurable,
  financed, and de-risked. Builds the **metric tree**, quantifies hypotheses, adds risk
  mitigation. Recommended tools: `metric-tree`, `unit-economics`, `financial-model`,
  `risk-mitigation` (+ refined `architecture-c4` / `product-surface`; the step README is
  canonical when the two lists drift).
- **5 · Tactical Plan** — Goal: measurable period goals per direction, and which hypotheses
  to test. Selects **metric-tree** nodes to move; adds period blockers. The active status
  sets which goals take priority — e.g. `concept-viability` prioritizes building a testable
  prototype/MVP over product/growth metrics.
- **6 · Sprint Plan** — Goal: turn period goals into sprint tasks per direction — a minimal
  **must** set + a prioritized backlog. Links tasks to metric nodes / hypotheses. Hands off
  to the team's development process.

> **Boundary 3 ↔ 4:** Step 3 = *choices and direction* (qualitative). Step 4 = *instruments
> and resources* (quantitative). If it is a choice → Step 3; if it is a number, a model, or a
> mitigation → Step 4.

---

## 5. The three vertical registers

Metrics, hypotheses, and risks are **not re-authored at each step** — living objects born
once and refined downward, with results flowing back up. Field schemas and the hard rules are in
[`REGISTERS.md`](REGISTERS.md).

| Register | Born at | Refined at | Purpose |
|----------|---------|------------|---------|
| **Metric register** | Step 4 | 5 (nodes to move) → 6 (task ↔ metric) | one canonical decomposition of the North Star |
| **Hypothesis register** | Step 1/3 | 4 (quantify) → 5 (test design) → 6 (experiment tasks) | bets get concrete downward; results feed back up |
| **Risk register** | Step 2 | 3 (product) → 4 (mitigation) → 5 (period blockers) | accumulates, never rewritten |

> **Metric register = one split, always** (per *One mechanism, one way*): node **definitions** live
> in `metric-tree.md`, dated **values** live in `metrics.csv` (append-only:
> `id,period_start,period_end,measured_at,value,basis,source,note`). A captured value goes to the
> csv at capture time — even before Step 4 builds the tree; a `sources/` snapshot is *evidence*, not
> its home. A changed definition mints a **new id**; every id in the csv must be defined in the md.

---

## 6. Statuses (product-stage plane)

A **status** is the product's current stage. It parameterizes the loops **per step**: which
goals take priority (optionally by direction) and which tools to lean on — the same section can
call for different methods at different stages (pains from interviews early, from internal
metrics later). Defaults
(extensible — see [`statuses/README.md`](../statuses/README.md)):

1. **concept-viability** — prototype/MVP to test that the product *can* be built and that
   there is *some* demand worth pursuing toward PMF.
2. **PMF** — first clients; the product has a path to profit; validate repeatable value and
   monetization so it can be scaled.
3. **growth** — a working, profitable product to develop and expand.

Statuses (and their goals, rules, and tool sets) are **configurable per company/product**.
You can add stages without breaking the framework: the process core reads whatever status is
active and applies its parameters.

> **A status may not yet define `per_step` for a given step.** That does not block: the loop
> works by the step defaults, and at *Update state* the agent proposes filling that status's
> `per_step` from what the pass just learned — so statuses complete as a by-product of the first
> run through each stage, never left as standing stubs.

---

## 7. Library (method plane)

The [library](../library/README.md) is a catalog of product methods, each authored as a
**skill**: *what it is · when to apply it · how to do it · a template*. When a step needs a
section produced, or a status calls for a check (e.g. test a hypothesis), the agent picks the
right tool and follows it. The library is meant to grow and be adapted — it is where
company-specific or opinionated methods live, keeping the process core neutral.

---

## 8. Cross-cutting conventions

The authority is [`CONVENTIONS.md`](CONVENTIONS.md); this is the map. Conventions are **not
uniform across file types** — the *Which conventions apply where* matrix (by `node_type`) says
which apply to an artifact vs a register vs a source vs a handoff. Omitting a convention the
matrix marks n/a is correct, not a lapse.

- **Dated change logs + rationale.** Artifacts, sources, registers, and framework files carry a
  change log (date · from→to · why · trigger). Narrative artifacts included. Not source files'
  raw captures.
- **Confidence tags** (`assumption` · `sourced` · `validated` · `refuted`) on every non-trivial
  claim **in artifacts** — *but not in registers*, where confidence is a table column instead
  (per the matrix). A missing tag reads as `assumption`.
- **One mechanism, one way.** Framework mechanics have exactly one canonical form (where values
  live, file formats, ids, anchors) — no dual formats or migration thresholds. Product decisions
  fork; mechanics must not.
- **Forks & options — triage first.** The agent escalates only consequential + not-defaultable
  decisions, each as 2–4 options with trade-offs + a ⚙️ recommendation; everything reversible and
  cheap it decides itself, marks ⚙️, and logs — it does not ask. `— to clarify —` is never
  standing debt.
- **Source slots + Raw data & access.** Each step and tool declares its inputs (git · metrics ·
  KB · interview). External-data access lives in a `sources/` file (indexed in `sources/INDEX.md`);
  captured values go to the registers; raw captures are deleted once landed; secrets are never
  written into artifacts, only where they live and how to rotate them.
- **Talking to the human.** In chat, never a bare id/anchor/link — decode what stands behind it
  in the same sentence.
- **Typed links (GitMark-lite).** Artifacts link across steps: plan item → hypothesis →
  metric node → strategy bet. Gives graph + search for free.
- **Soft gates.** Each step has a "step is defended" checklist that reports open items but
  does not block descent.

---

## 9. The three anatomies

Defined in Phase 1; summarized here. (`template-fragment.md` is part of **every** tool, including
survey-style ones; the `handoff` tool follows the same tool anatomy and writes the instance's
`HANDOFF.md` at session boundaries — see §2 and OPERATING-LOOP.)

**Step** (`steps/N-name/`) — thin:
```
README.md   # goal · gate checklist · movement rules · register touchpoints ·
            # artifact skeleton (section IDs) · recommended tools · status notes ·
            # cadence + invalidation
```

**Tool** (`library/<tool>/`) — a skill:
```
SKILL.md            # what it is / when to apply / PREREQUISITES / how to do it / anti-patterns
template-fragment.md # the section it produces, with source + confidence markers
questions.yaml      # the interview to gather inputs (renders to a fillable file too)
references/         # deeper method notes, examples
```
Declares which registers it reads/writes, which section it fills, and a **prerequisites
checklist** (info/artifacts/access) the loop verifies — asking for, or helping obtain, whatever
is missing.

**Status** (`statuses/<order>-<name>.md`, numbered by maturity) — config:
```
frontmatter: name · order · gate_emphasis · per_step{ <n>: { goals, tools } }
body: description + change log
```

---

## 10. What this is not (yet)

Deferred by design, kept out of the neutral core:
- **Adapters** that reshape base artifacts into a company's own formats and into downstream
  dev processes (e.g. an adapter for an external development framework, steering-committee
  cards, traction cards). These live outside the base and reference external tools there.
- **Aggregators** that pull and merge product data from git, metrics, and the KB.
- **Automation** of bottom-up refresh across loops.

The base artifacts are kept structured (stable IDs, source slots, typed links) precisely so
these can be added on top without rework.

---

## Change log

### 2026-07-18 — realign OVERVIEW with the 0.3–0.4 rules (audit fix)
- **From → To:** OVERVIEW had drifted at 0.2.1 while the other process files reached 0.4.0 →
  pulled in the rules it was missing or contradicting: *One mechanism, one way*; fork triage
  (agent closes reversible forks itself); *Talking to the human*; *Raw data & access* + the
  `sources/` instance mechanism; the *node_type × conventions* matrix (§8 no longer claims tags
  "on every claim everywhere" — registers use a column, not prose tags); the metric-register
  split (`metric-tree.md` defs + `metrics.csv` values, csv⊆md); the `handoff` tool + `HANDOFF.md`;
  empty-`per_step` fallback. Renamed the **direction** `growth` → `go-to-market` (the `growth`
  **status** is unchanged); unified the register's name to **Metric register**; refreshed the
  library examples to tools that actually exist.
- **Why:** a full 6-step run surfaced that the master overview no longer matched the canon it
  summarizes — the audit traced most process-plane discrepancies back to this drift.
- **Trigger:** framework audit, 2026-07-18.
