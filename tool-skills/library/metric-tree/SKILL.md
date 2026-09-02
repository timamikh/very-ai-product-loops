---
node_type: card
kind: method
name: metric-tree
steps: [4]
prerequisites:
  - strategy exists (how-to-win logic — the tree must encode it, not generic SaaS)
  - metric register seeded with captured readings (metrics.csv)
  - the product's paying/value base numbers (who pays, what they do)
reads: [section:how-to-win, section:bets, section:architecture-instrumentation, register:metrics, register:hypotheses]
writes: [worklog, section:metric-tree, register:metric-tree, register:metrics]
opinionated: true
method_basis: "North Star Framework (Amplitude); anti-lamppost — right metric over measurable"
evidence_standard: decision
volume_rule: "2–4 candidate North Stars, each run through all three filters (leading · value-repeating · strategy-encoding)"
selection_rule: "the candidate passing all three filters becomes the North Star; 3–5 drivers under it, not more"
rejects_shown: required
status: draft
version: 0.4.2
updated: 2026-09-02
---
# Metric tree — North Star → drivers → inputs

**Method basis:** North Star Framework (Amplitude). One metric the whole team steers by; a small
tree of drivers that explain and predict it. Guardrails are set at Step 5 by `guardrails`, against
the period goals — this tree only names candidate protected nodes in its worklog.

## When to apply
- Step 4, to build the North Star → drivers → inputs tree once strategy exists.
- Period selection: see `goal-targets` (Step 5).

## Prerequisites
- **Strategy exists** — how-to-win logic; the tree must encode it, not generic SaaS.
- **Metric register seeded** with captured readings (metrics.csv).
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
3. **Attach inputs** under each driver — the operational metrics teams can move weekly. Then read
   the hypothesis register: every `H-…` carried from `3#bets` needs a node here for
   `hypothesis-thresholds` to bind its bars to — a bet no node can measure is a gap this tree
   closes now, not one Step 4's thresholds discover later.
4. **Mark every node** `instrumented | proxy | not-instrumented` — a node carries the status of
   the surface its data comes from, read off `instrumentation-plan`'s per-surface status in
   `{#architecture-instrumentation}`, never asserted here. The **Not instrumented** list is that
   status projected onto nodes; the surface-level work list stays with `instrumentation-plan`.
5. **Update the register:** new nodes get IDs + definitions in `registers/metric-tree.md`; parents
   set; targets ⚙️ where the human hasn't decided.

## Anti-patterns
- Revenue as North Star.
- A "tree" that is a flat KPI list.
- More than ~12 nodes at pmf.
- Picking the measurable-but-wrong metric over the right-but-uninstrumented one.
- A tree that would fit any SaaS (it must smell of this product's strategy).

## Worklog & projection
Worklog: `4-strategic-plan/metric-tree.md` — the 2–4 candidates through the three filters with the losers and the filter each failed, the drivers and inputs, the candidate protected nodes for Step-5 `guardrails`, the instrumentation status per node. Projects `{#metric-tree}`; face: the **North Star** line, via [`template-fragment.md`](template-fragment.md). Node definitions land in `registers/metric-tree.md`, values in `metrics.csv` — the section is shape and rationale only. Path form, primary/contributing and revisit rules: [`worklog-resolution.md`](../../../process/reference/worklog-resolution.md).

## Output
Projects `{#metric-tree}` via [`template-fragment.md`](template-fragment.md) from the worklog; inputs
via [`questions.yaml`](questions.yaml); new nodes get IDs, parents and definitions in
`registers/metric-tree.md`, readings in `metrics.csv`.
