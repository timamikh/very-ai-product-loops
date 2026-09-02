---
node_type: card
kind: method
name: unit-economics
steps: [4]
prerequisites:
  - revenue and paying-customer counts by tariff (billing)
  - cost lines incl. LLM inference (fact external spend AND own-compute cost: server + hardware depreciation)
  - acquisition channel costs (or an explicit CAC≈0 claim with its source)
  - churn/retention if instrumented — otherwise model as scenarios, never as a guessed constant
reads: [section:pricing, section:retention, section:architecture-instrumentation, register:metrics]
writes: [worklog, section:unit-economics, register:metrics]
opinionated: true
method_basis: "Contribution margin; LLM inference as explicit COGS; dual basis operational/honest own-compute"
evidence_standard: internal-data
volume_rule: n/a
selection_rule: n/a
rejects_shown: n/a
status: draft
version: 0.2.6
updated: 2026-09-02
---
# Unit economics — does one customer pay for themselves?

**Method basis:** contribution-margin unit economics with **LLM inference as an explicit COGS
line** (the 2026 baseline: for an AI product, inference is COGS, not overhead). Where the product
runs on its own GPUs, compute the economics in **two bases side by side** — `operational` (what
the P&L shows under internal transfer pricing) and `honest` (adding hardware depreciation /
market compute price) — so a segment can't look profitable only because the metal is "free".
**The dual basis is optional:** on third-party / API compute (no own hardware) the two collapse —
compute a single basis and say so.

## When to apply
- Step 4, when you need to know whether a single customer pays for themselves before scaling.

## Prerequisites
- **Revenue and paying-customer counts by tariff** (billing).
- **Cost lines incl. LLM inference** — fact external spend AND own-compute cost (server + hardware
  depreciation).
- **Acquisition channel costs** — or an explicit CAC≈0 claim with its source.
- **Churn/retention if instrumented** — otherwise model as scenarios, never as a guessed constant.

*Any of these missing as a number rather than as a source → [`metrics-capture`](../../operations/metrics-capture/SKILL.md)
(operations) is the pass that lands it in the register; this tool reads the register, it does not query.*

## How to do it
1. **State the window first, then revenue per paying account.** Name the period every figure below
   is read over (trailing 30 days, last full month, the quarter) — revenue, COGS and CAC read over
   different windows do not divide into each other, and nothing on the page says so afterwards. Then:
   revenue per paying account, blended AND by tariff (price ≠ ARPPU when one-time/PAYG mix in).
2. **COGS per paying account** in both bases. Allocate inference by actual usage share (tokens),
   not headcount; state the allocation rule as an `[assumption]`. Non-paying usage (free tier,
   grants) is a real cost — decide explicitly who "carries" it and write that down.
3. **Contribution margin** = revenue − COGS, per account and %; both bases.
4. **CAC & payback** — per channel; CAC≈0 must be sourced, not assumed.
5. **LTV only if churn is honest.** No instrumented product churn → LTV as scenarios
   (e.g. 3/5/10%/mo), marked ⚙️, with the instrumentation gap flagged to the metric register.
6. **Register:** unit metrics become `M-…` nodes (ARPPU, contribution, CAC) with basis column
   in `metrics.csv`.

## Anti-patterns
- One blended number hiding a money-losing segment.
- Inference cost averaged per user when usage is power-law (top accounts eat the budget — check
  the distribution).
- LTV from an invented churn constant.
- Ignoring free-tier burn because "they don't pay".

## Worklog & projection
Worklog: `4-strategic-plan/unit-economics.md` — the reading window, revenue per payer blended and by tariff, COGS per basis with the allocation rule, contribution, CAC and payback per channel, the LTV scenarios. Projects `{#unit-economics}`; face: the **Contribution read** line, via [`template-fragment.md`](template-fragment.md). Path form, primary/contributing and revisit rules: [`worklog-resolution.md`](../../../process/reference/worklog-resolution.md).

## Output
Projects `{#unit-economics}` via [`template-fragment.md`](template-fragment.md) from the worklog;
inputs via [`questions.yaml`](questions.yaml); unit metrics become `M-…` nodes (ARPPU, contribution,
CAC) with a basis column in `metrics.csv`.
