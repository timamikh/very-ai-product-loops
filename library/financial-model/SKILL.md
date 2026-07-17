---
name: financial-model
kind: method
produces: strategic-plan#financial-model
prerequisites:
  - metric tree exists (drivers are the model's inputs — no tree, no model)
  - unit economics computed (ARPPU, contribution, both bases)
  - current run-rate (MRR/revenue/cost lines) from the metric register
  - capacity constraints (slot caps, registration caps, compute limits) — explicit
reads_registers: [metrics, hypotheses, risks]
writes_registers: [metrics]
inputs: [metrics]
used_by_steps: [4]
status: draft
version: 0.1.0
updated: 2026-07-17
---

# Financial model — a simple projection off the metric tree

**Method basis:** driver-based modeling. The projection's inputs are the metric tree's driver
nodes (new paying, churn, ARPPU, cost-per-usage), never a hand-drawn revenue curve. At pmf the
model is 10 lines, 2–4 scenarios, 12 months — not a spreadsheet empire.

**How to do it (thin):**
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

**Anti-patterns:** growth extrapolated from one hot month · churn invented as a constant ·
ignoring own caps/capacity (the model promises revenue the slots can't hold) · precision theatre
(kopecks in a model whose churn axis spans 3×) · a model detached from the tree's node IDs.
