---
name: unit-economics
kind: method
produces: strategic-plan#unit-economics
prerequisites:
  - revenue and paying-customer counts by tariff (billing)
  - cost lines incl. LLM inference (fact external spend AND own-compute cost: server + hardware depreciation)
  - acquisition channel costs (or an explicit CAC≈0 claim with its source)
  - churn/retention if instrumented — otherwise model as scenarios, never as a guessed constant
reads_registers: [metrics, hypotheses]
writes_registers: [metrics]
inputs: [metrics]
used_by_steps: [4]
status: draft
version: 0.1.0
updated: 2026-07-17
---

# Unit economics — does one customer pay for themselves?

**Method basis:** contribution-margin unit economics with **LLM inference as an explicit COGS
line** (the 2026 baseline: for an AI product, inference is COGS, not overhead). Where the product
runs on its own GPUs, compute the economics in **two bases side by side** — `operational` (what
the P&L shows under internal transfer pricing) and `honest` (adding hardware depreciation /
market compute price) — so a segment can't look profitable only because the metal is "free".

**How to do it (thin):**
1. **Revenue per paying account** — blended AND by tariff (price ≠ ARPPU when one-time/PAYG mix in).
2. **COGS per paying account** in both bases. Allocate inference by actual usage share (tokens),
   not headcount; state the allocation rule as an `[assumption]`. Non-paying usage (free tier,
   grants) is a real cost — decide explicitly who "carries" it and write that down.
3. **Contribution margin** = revenue − COGS, per account and %; both bases.
4. **CAC & payback** — per channel; CAC≈0 must be sourced, not assumed.
5. **LTV only if churn is honest.** No instrumented product churn → LTV as scenarios
   (e.g. 3/5/10%/mo), marked ⚙️, with the instrumentation gap flagged to the metric register.
6. **Register:** unit metrics become `M-…` nodes (ARPPU, contribution, CAC) with basis column
   in `metrics.csv`.

**Anti-patterns:** one blended number hiding a money-losing segment · inference cost averaged
per user when usage is power-law (top accounts eat the budget — check the distribution) ·
LTV from an invented churn constant · ignoring free-tier burn because "they don't pay".
