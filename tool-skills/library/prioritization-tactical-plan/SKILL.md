---
node_type: card
kind: method
name: prioritization-tactical-plan
steps: [5]
prerequisites: [candidate goals, the period gate/goal, available resources]
reads: [section:metric-tree, section:resources, section:market-bundles, register:metrics, register:hypotheses, register:features]
writes: [worklog, section:period-goals, register:features]
opinionated: false
method_basis: "RICE/ICE as a ranking aid, ranked by contribution to the period gate; capacity-bounded goal set"
evidence_standard: derived
volume_rule: "every candidate current for the period enters the ranking — none pre-cut; record the count N that entered"
selection_rule: "RICE/ICE as an ordering aid, re-ranked by contribution to the period gate; the goal set is capacity-bounded"
rejects_shown: required
status: draft
version: 0.2.2
updated: 2026-09-02
---
# Prioritization — Tactical Plan

Rank the period's candidate **goals** by their contribution to the gate of the period and keep only
what fits the period's capacity. Fills `{#period-goals}` (Step 5).

**Goal vs item — the boundary with `prioritization-sprint-plan`.** A *goal* is a period-level
outcome per direction — a measurable movement of an `M-…` or a Definition of Done, sized by
`goal-targets` — and is what this method ranks. An *item* is one sprint-level piece of work (a
Feature, Activity or Task carrying an `F-…`) that advances a goal; items are ranked at Step 6 by
[`prioritization-sprint-plan`](../prioritization-sprint-plan/SKILL.md), never here. Both cards run
the same ranking procedure — [`references/rice-procedure.md`](../references/rice-procedure.md) —
and neither restates it.

**Method basis.** RICE/ICE as a ranking aid, ordered by contribution to the period gate; the goal
set is the minimum without which the gate is unreachable, bounded by the capacity from
`resource-check`, not by wishful scope.

## When to apply
- Step 5, to rank the period's candidate goals per direction against the stage-gate.
- Whenever candidate goals exceed capacity and the period's set has to be drawn.

## Prerequisites
- **Candidate goals** — per direction. *Missing → generate them from the metric tree
  (`4#metric-tree`) and the hypothesis register, or run the upstream step.*
- **The period gate / goal** — the target each candidate is ranked against. *Missing → state the
  stage-gate of the period first (the status's learning goal / the metric node it must move).*
- **Available resources** — the capacity that bounds the goal set. *Missing → run `resource-check`
  (`5#resources`).*

## How to do it
1. **Run the ranking procedure on the goals** — gate stated, every candidate with N, RICE/ICE as
   the aid, rank by gate contribution, link check, capacity bound, every cut with its reason:
   [`rice-procedure.md`](../references/rice-procedure.md). The score inputs come from the
   artifact — reach from the metric register, impact from the node movement the goal names — ⚙️
   proposed, asked only where nothing on file answers ([`questions.yaml`](questions.yaml)).
2. **Keep the set at the gate's minimum.** The period holds the goals without which the gate is
   unreachable, and no more — a goal that fits capacity but does not move the gate is a cut, with
   the reason.
3. **Finalize the feature priorities.** With the period's goals set, re-weigh `priority` in
   `registers/features.md`: a `planned` row serving a goal of *this* period → `now`; structurally
   heavy (Step-4 seed) but not this period → `next`; the rest → `later`. Step 4 said what the model
   needs, this step says what of it happens now, so the Step-6 ranking starts from a weighted pool
   instead of a cold list. The method declares the write, the orchestrator writes the cells.

> **Boundary with `segment-cvp` (one mechanism, one way).** A market-entry bundle
> (`5#market-bundles`) arrives here **already scored for test-readiness** by `segment-cvp` — on a
> scale that includes speed to a signal, an axis RICE does not have. This method does **not**
> re-score it; it answers only whether the staged test fits this period's capacity against the
> period gate. One object, one scale each.

## Anti-patterns
The shared five are in the reference. This card's own:
- **Goals inflated past capacity.** A period plan that doesn't fit the available resources is a wish
  list, not a plan.
- **A bundle re-scored.** RICE run over a `B-…` that `segment-cvp` already gated — two scales on
  one object.
- **Feature priorities left cold.** The goal set signed with `priority` in the feature register
  untouched — Step 6 then ranks from an unweighted pool.

## Worklog & projection
Worklog: `5-tactical-plan/prioritization-tactical-plan.md` — the gate stated first, the full candidate list with N, the RICE/ICE scores, the re-rank by gate contribution, the goal set bounded at the capacity line, every cut with its reason. Projects `{#period-goals}`; face: the **Gate of the period** line, via [`template-fragment.md`](template-fragment.md). Path form, primary/contributing and revisit rules: [`worklog-resolution.md`](../../../process/reference/worklog-resolution.md).

## Output
Projects `{#period-goals}` (Step 5) via [`template-fragment.md`](template-fragment.md) from its
worklog; inputs via [`questions.yaml`](questions.yaml). The period's goals then feed
[`goal-targets`](../goal-targets/SKILL.md) (the target per goal) and Step 6's
[`prioritization-sprint-plan`](../prioritization-sprint-plan/SKILL.md) (the sprint's must/backlog).
