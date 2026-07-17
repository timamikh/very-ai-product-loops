---
name: metric-tree
kind: method
produces: strategic-plan#metric-tree
prerequisites:
  - strategy exists (how-to-win logic — the tree must encode it, not generic SaaS)
  - metric register seeded with captured readings (metrics.csv) and instrumentation status per node
  - the product's paying/value base numbers (who pays, what they do)
reads_registers: [metrics, hypotheses]
writes_registers: [metrics]
inputs: [metrics, kb]
used_by_steps: [4]
status: draft
version: 0.1.0
updated: 2026-07-17
---

# Metric tree — North Star → drivers → inputs

**Method basis:** North Star Framework (Amplitude). One metric the whole team steers by; a small
tree of drivers that explain and predict it; guardrails that must not degrade while chasing it.

**How to do it (thin, in order):**
1. **Candidate North Stars — as a fork.** 2–4 candidates, each tested against three filters:
   *leading* (moves before revenue), *value-repeating* (counts customers getting value again,
   not once), *strategy-encoding* (optimizing it strengthens how you win — check against
   `strategy#how-to-win`). Revenue is never the North Star; it is the outcome.
   **Do not reject a candidate because it isn't measured yet** — the gap between the right
   metric and today's instrumentation becomes the work plan (the lamppost trap).
2. **Pick drivers (3–5, not more):** acquisition-side (new accounts reaching value), conversion,
   deepening (the strategy's engagement axis), retention. Every driver is a register node with
   `parent` = the North Star.
3. **Attach inputs** under each driver — the operational metrics teams can move weekly.
4. **Declare guardrails** (finance/cost/quality metrics that cap the pursuit): margin on honest
   costs, product churn, unit cost levers.
5. **Mark every node** `instrumented | proxy | not-instrumented`. The not-instrumented list is a
   first-class output of Step 4 — it feeds Steps 5–6 as instrumentation tasks.
6. **Update the register:** new nodes get IDs + definitions in `metric-tree.md`; parents set;
   targets ⚙️ where the human hasn't decided.

**Anti-patterns:** revenue as North Star · a "tree" that is a flat KPI list · more than ~12 nodes
at pmf · picking the measurable-but-wrong metric over the right-but-uninstrumented one · a tree
that would fit any SaaS (it must smell of this product's strategy).
