---
name: financial-model
kind: method
produces: financial-model
reads_registers: [metrics, hypotheses, risks]
writes_registers: [metrics]
inputs: [metrics]
prerequisites:
  - metric tree exists (drivers are the model's inputs — no tree, no model)
  - unit economics computed (ARPPU, contribution, both bases)
  - current run-rate (MRR/revenue/cost lines) from the metric register
  - capacity constraints (slot caps, registration caps, compute limits) — explicit
used_by_steps: [4]
opinionated: true
method_basis: "Driver-based modeling; churn as scenario axis; capacity caps as first-class constraint"
evidence_standard: derived
volume_rule: n/a
selection_rule: n/a
rejects_shown: n/a
status: draft
version: 0.2.2
updated: 2026-08-09
---

# Financial model — a simple projection off the metric tree

The projection's inputs are the metric tree's driver nodes (new paying, churn, ARPPU,
cost-per-usage), never a hand-drawn revenue curve. At pmf the model is 10 lines, 2–4 scenarios,
12 months — not a spreadsheet empire.

## When to apply
- Step 4, once the metric tree and unit economics exist — the drivers are the model's inputs.

## Prerequisites
- **Metric tree** — drivers are the model's inputs; no tree, no model.
- **Unit economics** — ARPPU, contribution, both bases.
- **Current run-rate** — MRR/revenue/cost lines from the metric register.
- **Capacity constraints** — slot caps, registration caps, compute limits, made explicit.

## How to do it
1. **State the drivers** with today's values from `metrics.csv` and the assumption tag for each
   projected one (new paying/mo · churn %/mo · ARPPU · usage-linked COGS · fixed costs).
2. **Churn honesty rule:** no instrumented product churn → churn is a SCENARIO AXIS (e.g.
   3/5/10%), never a single guessed constant.
3. **Compound monthly, 12 months, 2–4 scenarios** (conservative / base ⚙️ / stretch tied to a
   named hypothesis — e.g. "activation fixed"). MRR_{t+1} = MRR_t × (1 − churn) + new × ARPPU.
4. **Apply capacity constraints** — slot caps, registration caps, compute ceilings. If a
   scenario hits a cap, SAY WHEN: "the cap binds in month N" is often the model's main output.
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
The working is done in the step's **worklog** `<step-folder>/financial-model.md` (`node_type: worklog`,
e.g. `4-strategic-plan/financial-model.md`): the driver values pulled from `metrics.csv`, the churn
scenario axis, the compounded 12-month projection across 2–4 scenarios, where each capacity cap binds,
both cost bases carried to breakeven, and the invalidation triggers. That worklog is the **source of
truth**; the artifact section `{#financial-model}` is its **projection** into the fixed shape of
[`template-fragment.md`](template-fragment.md) — it holds nothing the worklog does not, and the step's
change-log history lives in the worklog, not the section
(`process/CONVENTIONS.md` → *Step folders & worklogs*). External figures arrive here dispatched from
`sources/` by `source-intake`, cited in the worklog, never linked from the artifact.

## Output
Projects `{#financial-model}` via [`template-fragment.md`](template-fragment.md) from the worklog; inputs
via [`questions.yaml`](questions.yaml).
