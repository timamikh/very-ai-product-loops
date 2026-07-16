---
node_type: process-overview
title: very-ai-product-loops — Process Overview
status: draft
version: 0.2.0
updated: 2026-07-16
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
│                           segment-pains, concept-formation, CJM, JTBD, A/B test, brief,
│                           market-sizing, unit-economics… each = what / when / how / template
│
└─ Statuses (statuses/) ─── product stages as config: concept-viability · PMF · growth
                            (extensible): priority goals + goal type + its own tool set
```

**How the planes interlock — softly (per rule 5):**
- A **step** says "at this stage produce sections A, B, C and pass gate G" and *recommends*
  library tools per section.
- A **status** re-prioritizes goals and *highlights* the relevant tools, and sets the goal
  type (technical vs product).
- The **human** overrides anything. Nothing is hard-wired.
- **Registers** are the shared state that tools read and write.

> The step owns the **artifact skeleton** (which sections must exist, with stable IDs).
> Tools **fill** specific sections with their own method, mini-template, and interview.
> Method is swappable; skeleton is stable.

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
`development` · `growth` · `back-office`); the number of directions can change depending on
the product's specifics.

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
  `risk-mitigation`.
- **5 · Tactical Plan** — Goal: measurable period goals per direction, and which hypotheses
  to test. Selects **metric-tree** nodes to move; adds period blockers. The active status
  sets the goal type — e.g. `concept-viability` makes the period goals **technical**
  (build the prototype/MVP) rather than product/growth metrics.
- **6 · Sprint Plan** — Goal: turn period goals into sprint tasks per direction — a minimal
  **must** set + a prioritized backlog. Links tasks to metric nodes / hypotheses. Hands off
  to the team's development process.

> **Boundary 3 ↔ 4:** Step 3 = *choices and direction* (qualitative). Step 4 = *instruments
> and resources* (quantitative). If it is a choice → Step 3; if it is a number, a model, or a
> mitigation → Step 4.

---

## 5. The three vertical registers

Metrics, hypotheses, and risks are **not re-authored at each step** — living objects born
once and refined downward, with results flowing back up.

| Register | Born at | Refined at | Purpose |
|----------|---------|------------|---------|
| **Metric tree** | Step 4 | 5 (nodes to move) → 6 (task ↔ metric) | one canonical decomposition of the North Star |
| **Hypothesis register** | Step 1/3 | 4 (quantify) → 5 (test design) → 6 (experiment tasks) | bets get concrete downward; results feed back up |
| **Risk register** | Step 2 | 3 (product) → 4 (mitigation) → 5 (period blockers) | accumulates, never rewritten |

---

## 6. Statuses (product-stage plane)

A **status** is the product's current stage. It parameterizes the loops: which goals take
priority, whether goals are technical or product, and which tools are most relevant. Defaults
(extensible — see [`statuses/README.md`](../statuses/README.md)):

1. **concept-viability** — prototype/MVP to test that the product *can* be built and that
   there is *some* demand worth pursuing toward PMF. Goals are largely **technical**.
2. **PMF** — first clients; the product has a path to profit; validate repeatable value and
   monetization so it can be scaled.
3. **growth** — a working, profitable product to develop and expand.

Statuses (and their goals, rules, and tool sets) are **configurable per company/product**.
You can add stages without breaking the framework: the process core reads whatever status is
active and applies its parameters.

---

## 7. Library (method plane)

The [library](../library/README.md) is a catalog of product methods, each authored as a
**skill**: *what it is · when to apply it · how to do it · a template*. When a step needs a
section produced, or a status calls for a check (e.g. test a hypothesis), the agent picks the
right tool and follows it. The library is meant to grow and be adapted — it is where
company-specific or opinionated methods live, keeping the process core neutral.

---

## 8. Cross-cutting conventions

- **Dated entries + rationale everywhere.** Each artifact has a change log: date, from→to,
  why, trigger. Git history is secondary; the in-artifact log carries the motivation.
- **Confidence tags:** `assumption` · `sourced` · `validated` · `refuted` on every claim.
- **Source slots.** Each step and tool declares its inputs (git · metrics · KB · interview),
  so aggregation skills can later fill them automatically.
- **Typed links (GitMark-lite).** Artifacts link across steps: plan item → hypothesis →
  metric node → strategy bet. Gives graph + search for free.
- **Soft gates.** Each step has a "step is defended" checklist that reports open items but
  does not block descent.

---

## 9. The three anatomies

Defined in Phase 1; summarized here.

**Step** (`steps/N-name/`) — thin:
```
README.md   # goal · gate checklist · movement rules · register touchpoints ·
            # artifact skeleton (section IDs) · recommended tools · status notes ·
            # cadence + invalidation
```

**Tool** (`library/<tool>/`) — a skill:
```
SKILL.md            # what it is / when to apply / how to do it / anti-patterns
template-fragment.md # the section it produces, with source + confidence markers
questions.yaml      # the interview to gather inputs (renders to a fillable file too)
references/         # deeper method notes, examples
```
Declares which registers it reads/writes and which artifact section it fills.

**Status** (`statuses/<name>.md`) — config:
```
frontmatter: name · goal_type (technical|product) · priority_goals ·
             recommended_tools · gate_emphasis
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
