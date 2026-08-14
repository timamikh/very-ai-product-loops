---
name: metric-tree
kind: method
produces: metric-tree
reads_registers: [metrics, hypotheses]
writes_registers: [metrics]
inputs: [metrics, kb]
prerequisites:
  - strategy exists (how-to-win logic — the tree must encode it, not generic SaaS)
  - metric register seeded with captured readings (metrics.csv) and instrumentation status per node
  - the product's paying/value base numbers (who pays, what they do)
used_by_steps: [4, 5]
opinionated: true
method_basis: "North Star Framework (Amplitude); anti-lamppost — right metric over measurable"
evidence_standard: decision
volume_rule: "2–4 candidate North Stars, each run through all three filters (leading · value-repeating · strategy-encoding)"
selection_rule: "the candidate passing all three filters becomes the North Star; 3–5 drivers under it, not more"
rejects_shown: required
status: draft
version: 0.2.4
updated: 2026-08-09
---

# Metric tree — North Star → drivers → inputs

**Method basis:** North Star Framework (Amplitude). One metric the whole team steers by; a small
tree of drivers that explain and predict it; guardrails that must not degrade while chasing it.

## When to apply
- Step 4, to build the North Star → drivers → inputs tree once strategy exists.
- Step 5, to select the nodes to steer by for the period.

## Prerequisites
- **Strategy exists** — how-to-win logic; the tree must encode it, not generic SaaS.
- **Metric register seeded** with captured readings (metrics.csv) and instrumentation status per node.
  *Missing → run [`metrics-capture`](../../operations/metrics-capture/SKILL.md) (operations) — it is the
  pass that produces the rows this tool reads.*
- **The product's paying/value base numbers** — who pays, what they do.

## How to do it
Thin, in order:
1. **Candidate North Stars — as a fork.** 2–4 candidates, each tested against three filters:
   *leading* (moves before revenue), *value-repeating* (counts customers getting value again,
   not once), *strategy-encoding* (optimizing it strengthens how you win — check against
   `strategy#how-to-win`). Revenue is never the North Star; it is the outcome.
   **Do not reject a candidate because it isn't measured yet** — the gap between the right
   metric and today's instrumentation becomes the work plan (the lamppost trap).
   **Record the candidates that lost, and which filter they failed.** A North Star is the most
   re-litigated decision in the tree; without the losing candidates and their reason, the same
   argument is had again next quarter from a blank page.
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

## Anti-patterns
- Revenue as North Star.
- A "tree" that is a flat KPI list.
- More than ~12 nodes at pmf.
- Picking the measurable-but-wrong metric over the right-but-uninstrumented one.
- A tree that would fit any SaaS (it must smell of this product's strategy).

## Worklog & projection
The working is done in the step's **worklog** `<step-folder>/metric-tree.md` (`node_type: worklog`):
the 2–4 candidate North Stars each run through the three filters (leading / value-repeating /
strategy-encoding), the losing candidates and which filter each failed, the chosen North Star, the
3–5 drivers and their inputs, the guardrails, and each node's instrumentation status
(instrumented / proxy / not-instrumented). That worklog is the **source of truth**; the artifact
section `{#metric-tree}` is its **projection** into the fixed shape of
[`template-fragment.md`](template-fragment.md) — it holds nothing the worklog does not, and the
step's change-log history lives in the worklog, not the section
(`process/CONVENTIONS.md` → *Step folders & worklogs*). External figures arrive here dispatched from
`sources/` by `source-intake`, cited in the worklog, never linked from the artifact.

## Output
Projects `{#metric-tree}` via [`template-fragment.md`](template-fragment.md) from the worklog; inputs
via [`questions.yaml`](questions.yaml); new nodes get IDs, parents and targets in the metric register
(`metrics.csv`).
