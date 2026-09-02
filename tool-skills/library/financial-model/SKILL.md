---
node_type: card
kind: method
name: financial-model
steps: [4]
prerequisites:
  - metric tree exists (drivers are the model's inputs — no tree, no model)
  - unit economics computed (ARPPU, contribution, both bases)
  - current run-rate (MRR/revenue/cost lines) from the metric register
  - capacity constraints (slot caps, registration caps, compute limits) — explicit
reads: [section:market-sizing, section:pricing, section:metric-tree, section:unit-economics, register:metrics, register:hypotheses]
writes: [worklog, section:financial-model]
opinionated: true
method_basis: "Driver-based modeling; churn as scenario axis; capacity caps as first-class constraint"
evidence_standard: derived
volume_rule: n/a
selection_rule: n/a
rejects_shown: n/a
status: draft
version: 0.2.4
updated: 2026-09-02
---
# Financial model — a simple projection off the metric tree

The projection's inputs are the metric tree's driver nodes (new paying, churn, ARPPU,
cost-per-usage), never a hand-drawn revenue curve. At pmf the model is 10 lines, 2–4 scenarios,
12 months — not a spreadsheet empire.

## When to apply
- Step 4, once the metric tree and unit economics exist — the drivers are the model's inputs.

## Prerequisites
- **Metric tree** (`{#metric-tree}`) — drivers are the model's inputs; no tree, no model.
- **Unit economics** (`{#unit-economics}`) — ARPPU per tier (`3#pricing`), contribution, both bases.
- **Current run-rate** — MRR/revenue/cost lines from the metric register.
- **Capacity constraints** — slot caps, registration caps, compute limits, made explicit.

## How to do it
1. **State the drivers** with today's values from `metrics.csv` and the assumption tag for each
   projected one (new paying/mo · churn %/mo · ARPPU · usage-linked COGS · fixed costs).
2. **Churn honesty rule:** no instrumented product churn → churn is a SCENARIO AXIS (e.g.
   3/5/10%), never a single guessed constant.
3. **Compound monthly, 12 months, 2–4 scenarios** (conservative / base ⚙️ / stretch tied to a
   named `H-…` from the hypothesis register — e.g. "activation fixed").
   MRR_{t+1} = MRR_t × (1 − churn) + new × ARPPU.
4. **Apply capacity constraints** — slot caps, registration caps, compute ceilings, and the SOM
   from `2#market-sizing` as the outer ceiling. If a scenario hits a cap, SAY WHEN: "the cap binds
   in month N" is often the model's main output.
5. **Carry both cost bases** (operational / honest) to breakeven lines.
6. **Declare invalidation triggers:** which actual-vs-model divergence forces a revisit
   (feeds the step's cadence rules).

## Anti-patterns
- Growth extrapolated from one hot month.
- Churn invented as a constant.
- Ignoring own caps/capacity (the model promises revenue the slots can't hold).
- Precision theatre (kopecks in a model whose churn axis spans 3×).
- A model detached from the tree's node IDs.

## Worklog & projection
Worklog: `4-strategic-plan/financial-model.md` — the driver values from `metrics.csv`, the churn scenario axis, the 12-month projection per scenario, where each cap binds, break-even per basis, the invalidation triggers. Projects `{#financial-model}`; face: the **Break-even** line, via [`template-fragment.md`](template-fragment.md). Path form, primary/contributing and revisit rules: [`worklog-resolution.md`](../../../process/reference/worklog-resolution.md).

## Output
Projects `{#financial-model}` via [`template-fragment.md`](template-fragment.md) from the worklog; inputs
via [`questions.yaml`](questions.yaml).
