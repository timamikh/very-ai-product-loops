---
node_type: process-overview
title: very-ai-product-loops — Process Overview
status: draft
version: 0.1.0
updated: 2026-07-16
---

# very-ai-product-loops

A product-agnostic workflow that takes a product from **idea → sprint plan** through
**nested, gated loops**. Sibling to `very-ai-framework`: that one runs the *development*
loop (idea → production); this one runs the *product* loops that sit above it and feed it.

**One sentence:** the agent prepares every artifact from real sources; the human decides
at the forks; the whole thing is a set of loops that refresh at different speeds and feed
each other in both directions.

---

## 1. Philosophy (the rules the agent lives by)

1. **Agent prepares, human decides.** The agent gathers facts, drafts artifacts, and
   proposes defaults (marked ⚙️). The human only makes decisions at forks and approves.
2. **Facts only from sources.** Every field traces to a source (a document, a metric, a
   git artifact, or a dated human decision). No plausible-sounding invention. Missing data
   is surfaced as "— to clarify —", never filled with a guess.
3. **Everything is dated, nothing is overwritten.** Every artifact — narrative included —
   keeps a dated change log: *how it was → what changed → why → what triggered it*. Agents
   must be able to read the history and understand the motivation behind past decisions,
   not just the current state.
4. **Confidence is explicit.** Every claim carries a tag: `assumption` · `sourced` ·
   `validated` · `refuted`. Early steps are mostly assumptions; lower steps harden them.
5. **Help, don't constrain.** Gates are checklists that tell the human what is still open —
   they guide, they do not lock. While we pilot, you can descend with gaps; the framework
   flags them rather than blocking.

---

## 2. The loop model

This is **not a waterfall**. It is nested loops that refresh at different cadences. The
lower the loop, the more often it runs and the more it relies on aggregated data (git,
metrics, KB) rather than interview.

```
Idea / Analysis (1–2)      revisited on pivot / market shift        — rarely
  └ Strategy (3–4)         horizon 3–12 mo, reviewed quarterly
      └ Tactics (5)        horizon 1–3 mo, stage-gate monthly
          └ Sprint (6)     horizon 1–2 wk, every sprint
```

**Loops feed each other in both directions.** A sprint can refute a hypothesis → that is a
trigger to rework tactics. Tactics hitting a metric ceiling → a trigger to revisit strategy.
Each step declares (a) its **cadence** and (b) what it **invalidates** up and down when it
changes. This bidirectional trigger is what keeps the cascade alive instead of stale.

---

## 3. The six steps

| # | Step | Horizon | Cadence | Output artifact |
|---|------|---------|---------|-----------------|
| 1 | **Idea / Concept** | product lifetime | on pivot / major learning | `passport.md` |
| 2 | **Analysis** | 6–12 mo view | quarterly / on market shift | `analysis.md` |
| 3 | **Strategy** | 3–12 mo | reviewed quarterly | `strategy.md` |
| 4 | **Strategic Plan** | 3–12 mo | with strategy / on financial or metric shift | `strategic-plan.md` |
| 5 | **Tactical Plan** | 1–3 mo | monthly | `tactical-plan.md` |
| 6 | **Sprint Plan** | 1–2 wk | every sprint | `sprint-plan.md` |

Strategy (3–4) is organized around **goals / bets / metrics — never org structure**.
Execution (5–6) is organized around **directions**, which are an editable instance config
(default: `development` · `growth` · `back-office`; may become 2 or 5 over time).

### Step 1 — Idea / Concept
Concept · user segments · segment problems (severity × frequency) · how the product solves
them · **value & defensibility through a post-AI lens**.

Post-AI premise: the software itself is no longer a moat — anyone can rebuild it with an
LLM. Value lives in the *position*, not the *thing*. Two layers:

- **Base (primitive) values**
  - *Hard (durable):* unique data · unique algorithms/IP · exclusive access/integrations/rights
  - *Soft (barriers):* audience/distribution · brand/trust · expertise · processes (speed & precision) · product complexity/depth
- **Derivative values** (emerge when a base value meets a customer or scale)
  - lock-in / switching costs ← exclusive access/integration **+ existing customer**
  - network effects ← audience
  - economies of scale / cost advantage ← audience/scale

Every problem and segment is an `assumption` until evidenced — this is where the
**hypothesis register** is seeded.

### Step 2 — Analysis
Market sizing (TAM/SAM/SOM, with method and source) · competitors (direct, indirect, and
**substitutes / "do nothing / do it manually"**) · what game each competitor plays (revenue
/ profit / share / social capital — and how), compared on the Step-1 moat axes · niche
risks (→ **risk register**). Ends with a **"so what"**: where the white space / the threat
is. Analysis without a conclusion is inert.

### Step 3 — Strategy (qualitative choices)
Winning aspiration · where to play (segments/markets) · how to win (UVP/CPV + which moats
we leverage) · product context beyond the app (channels, expansion) · bets (PMF/growth
hypotheses) · product risks. **Mode flag lives here:** `pre-PMF` (find fit — validate
problem/solution) vs `growth` (scale) — the two shape goals and metrics differently.

### Step 4 — Strategic Plan (quantitative instrumentation)
The measurable, financed, de-risked backbone of Step 3: the **metric tree** (North Star →
drivers → inputs) · unit economics + financial model · risk mitigation plan · global
hypotheses (quantified, tied to metric nodes) · open questions.

> **Boundary 3 ↔ 4:** Step 3 = *choices and direction* (qualitative). Step 4 = *instruments
> and resources* (quantitative). If it is a choice, it is Step 3; if it is a number, a model,
> or a mitigation, it is Step 4.

**2026 financial baseline:** unit economics (CAC, LTV, payback, contribution margin) with
**LLM inference cost per active user as an explicit COGS line**, burn/runway, and a simple
projection tied to the metric tree. A full P&L is a product-specific adapter, not the base.

### Step 5 — Tactical Plan (1–3 mo)
A stage-gate for the period with measurable goals per **direction**. Selects which
**metric-tree nodes** to move this period, picks which **hypotheses** to test + their test
design, and lists blockers/risks with mitigation.

### Step 6 — Sprint Plan (1–2 wk)
Per-direction task lists: a minimal **must** set + a prioritized backlog for the rest.
Hands off to the development loop (`very-ai-framework` / the team's tracker).

---

## 4. The three vertical registers

Metrics, hypotheses, and risks are **not re-authored at each step** — they are living objects
born once and refined downward, with results flowing back up.

| Register | Born at | Refined at | Purpose |
|----------|---------|------------|---------|
| **Metric tree** | Step 4 | 5 (nodes to move) → 6 (task ↔ metric) | one canonical decomposition of the North Star |
| **Hypothesis register** | Step 3 (bets) | 4 (quantify) → 5 (test design) → 6 (experiment tasks) | bets get concrete downward; results feed back up |
| **Risk register** | Step 2 (market) | 3 (product) → 4 (mitigation) → 5 (period blockers) | accumulates, never rewritten |

---

## 5. Cross-cutting conventions

- **Dated entries + rationale everywhere.** Each artifact has a change log: date, from→to,
  why, trigger. Git history is secondary; the in-artifact log carries the *motivation*.
- **Confidence tags:** `assumption` · `sourced` · `validated` · `refuted` on every claim.
- **Source slots.** Each step declares its inputs (git · metrics · KB · human interview),
  so aggregation skills can later fill them automatically.
- **Typed links (GitMark-lite).** Artifacts link across steps: plan item → hypothesis →
  metric node → strategy bet. Gives graph + search for free.
- **PMF/Growth mode flag** (set at Step 3) changes the shape of goals and metrics.
- **Directions are instance config** (Step 5–6 only), editable per product.
- **Soft gates.** Each step has a "step is defended" checklist that reports open items but
  does not block descent during piloting.

---

## 6. Anatomy of a step (defined in Phase 1)

Each step is a folder under `steps/` with a uniform shape:

```
steps/1-idea/
  README.md         # goal, inputs (source slots), output, gate checklist, human's role, cadence + invalidation
  instructions.md   # rules for the agent (what to do / anti-patterns) = the skill body
  template.md       # the artifact form: sections with stable IDs, source + confidence markers
  questions.yaml    # the survey: questions for the task author, each with 2–4 options + default ⚙️
```

`questions.yaml` is the single source for the "form": it renders to a fillable file **or**
drives an LLM interview — same questions either way.

---

## 7. What this is not (yet)

Deferred to later phases, by design:
- **Adapters** that reshape base artifacts into a company's own formats (steering-committee
  cards, traction cards, R&D process docs).
- **Aggregators** that pull and merge product data from git, metrics, and the KB.
- **Automation** of bottom-up refresh across loops.

The base artifacts are kept structured (stable IDs, source slots, typed links) precisely so
these can be added on top without rework.
