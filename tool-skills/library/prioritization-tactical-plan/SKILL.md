---
node_type: card
kind: method
name: prioritization-tactical-plan
steps: [5]
prerequisites: [candidate items, the period gate/goal, available resources]
reads: [register:metrics, register:hypotheses, register:features]
writes: [worklog, section:period-goals, register:features]
opinionated: false
method_basis: "RICE/ICE as a ranking aid, ranked by contribution to the period gate; capacity-bounded goal set"
evidence_standard: derived
volume_rule: "every candidate current for the period enters the ranking — none pre-cut; record the count N that entered"
selection_rule: "RICE/ICE as an ordering aid, re-ranked by contribution to the period gate; the goal set is capacity-bounded"
rejects_shown: required
status: draft
version: 0.2.0
updated: 2026-08-24
---
# Prioritization — Tactical Plan

Rank the period's candidate goals by their **contribution to the gate of the period** — not by an
abstract score — and keep only what **fits the period's capacity**. Fills `{#period-goals}` (Step 5).
The sprint-level split of items into must/backlog is the sibling method
[`prioritization-sprint-plan`](../prioritization-sprint-plan/SKILL.md) (Step 6) — one step, one skill.

**Method basis.** RICE/ICE scoring (Reach · Impact · Confidence · Effort) used as a *ranking* aid,
not an oracle: the ordering key is how much each candidate moves the period gate. The goal set is
the minimum without which the period gate is unreachable, bounded by the available capacity from
`resource-check`, not by wishful scope.

## When to apply
- Step 5, to rank the period's candidate goals per direction against the stage-gate.
- Whenever candidate goals exceed capacity and the period's set has to be drawn.

## Prerequisites
- **Candidate items** — the candidate goals per direction to rank. *Missing → generate them from
  the metric tree and hypothesis register, or run the upstream step.*
- **The period gate / goal** — the target each candidate is ranked against. *Missing → state the
  stage-gate of the period first (the status's learning goal / the metric node it must move).*
- **Available resources** — the capacity that bounds the goal set. *Missing → run
  `resource-check`.*

## How to do it
1. **State the gate first.** Name the gate of the period (a metric node to move or a Definition of
   Done). Every candidate is ranked against *this*, not against a generic score.
2. **List the candidates.** All of them, per direction — don't pre-cut before ranking. **Record the
   count that entered the ranking (N).** A list with no N cannot be audited later: a candidate quietly
   dropped before scoring is invisible, and "we prioritized" reads the same whether ten items competed
   or three did.
3. **Score each (RICE or ICE).** Reach · Impact · Confidence · (Effort). Use the score to *order*
   candidates; keep the number honest with a confidence tag, and remember it is an aid, not the
   verdict.
4. **Re-rank by gate contribution.** Sort by how much each candidate moves the period gate. A high
   score that doesn't move the gate ranks below a lower score that does.
5. **Check the link.** Each candidate must move a metric node (`M-…`) or test a hypothesis (`H-…`).
   A candidate that does neither is a candidate to cut — and a cut candidate is **recorded with its
   reason**, not deleted: without the visible reject the next pass re-proposes the same goal.
6. **Bound the set by capacity.** Keep the goals that fit inside the capacity from `resource-check`;
   what doesn't fit is cut for the period, with the reason recorded. If the minimum set overflows
   capacity, cut scope or renegotiate the gate — do not inflate the period.
7. **Finalize the feature priorities.** With the period's goals set, re-weigh `priority` in
   `registers/features.md`: a `planned` row serving a goal of *this* period → `now`; structurally
   heavy (Step-4 seed) but not this period → `next`; the rest → `later`. This is the cascade's
   period pass — Step 4 said what the model needs, this step says what of it happens now, so the
   Step-6 ranking starts from a weighted pool instead of a cold list. The method declares the
   write, the orchestrator writes the cells.

> **Boundary with `segment-cvp` (one mechanism, one way).** A market-entry bundle arrives here
> **already scored for test-readiness** by `segment-cvp` — which bet is worth learning about first,
> on a scale that includes speed to a signal, an axis RICE does not have. This method does **not**
> re-score it. It answers the other question: does the staged test fit this period's capacity against
> the period gate. One object, one scale each; scoring a bundle twice on two scales is the drift the
> canon forbids.

## Anti-patterns
- **Flat list, no rank.** A pile of goals with no ordering — the set can't be bounded.
- **Goals inflated past capacity.** A period plan that doesn't fit the available resources; it's a
  wish list, not a plan.
- **Score for score's sake.** Ranking by RICE/ICE number with no tie back to the gate.
- **Orphan goals.** Goals with no `M-…` / `H-…` link — they move nothing and test nothing.
- **Invisible cuts.** A candidate dropped before or after the ranking with no recorded reason — the
  next pass re-derives it and no one can audit the selection.

## Worklog & projection
The working is done in the step's **worklog** `<step-folder>/prioritization-tactical-plan.md`
(`node_type: worklog`, e.g. `5-tactical-plan/prioritization-tactical-plan.md`): the period gate
stated first, the full candidate list **with N recorded**, the RICE/ICE scores, the re-rank by gate
contribution, the goal set bounded at the capacity line, and every **cut candidate with its
reason**. That worklog is the **source of truth**; the artifact section `{#period-goals}` is its
**projection** into the fixed shape of [`template-fragment.md`](template-fragment.md), holding
nothing the worklog does not, with the change-log history in the worklog
(`process/CONVENTIONS.md` → *Step folders & worklogs*).

## Output
Projects `{#period-goals}` (Step 5) via [`template-fragment.md`](template-fragment.md) from its
worklog; inputs via [`questions.yaml`](questions.yaml). The period's goals then feed
[`goal-targets`](../goal-targets/SKILL.md) (the target per goal) and Step 6's
[`prioritization-sprint-plan`](../prioritization-sprint-plan/SKILL.md) (the sprint's must/backlog).
