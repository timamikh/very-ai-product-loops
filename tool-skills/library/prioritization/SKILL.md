---
name: prioritization
kind: method
produces: [period-goals, must, backlog]
prerequisites: [candidate items, the period gate/goal, available resources]
reads_registers: [metrics, hypotheses]
writes_registers: []
inputs: []
used_by_steps: [5, 6]
opinionated: false
method_basis: "RICE/ICE, ranked by contribution to the period gate; capacity-bounded must/backlog line"
evidence_standard: derived
volume_rule: "every candidate current for the period enters the ranking — none pre-cut; record the count N that entered"
selection_rule: "RICE/ICE, re-ranked by contribution to the period gate; the must/backlog line is capacity-bounded"
rejects_shown: required
status: draft
version: 0.1.2
updated: 2026-08-09
---

# Prioritization

Rank the candidate items by their **contribution to the gate of the period** — not by an abstract
score — and draw the **must / backlog line by capacity**. Fills `{#period-goals}` (Step 5) and
`{#must}` / `{#backlog}` (Step 6).

**Method basis.** RICE/ICE scoring (Reach · Impact · Confidence · Effort) used as a *ranking* aid,
not an oracle: the ordering key is how much each item moves the period gate. The must-set is the
minimum without which the period goal is unreachable; the line between must and backlog is set by
the available capacity from `resource-check`, not by wishful scope.

## When to apply
- Step 5, to rank the period's goals per direction against the stage-gate.
- Step 6, to split the sprint's items into a minimal **must** set and a prioritized **backlog**.
- Whenever candidate items exceed capacity and the line has to be drawn.

## Prerequisites
- **Candidate items** — the goals/features/activities/tasks to rank. *Missing → generate them from
  the metric tree and hypothesis register, or run the upstream step.*
- **The period gate / goal** — the target each item is ranked against. *Missing → run the Step 5
  gate (`period-goals` / `goal-targets`).*
- **Available resources** — the capacity that sets the must/backlog line. *Missing → run
  `resource-check`.*

## How to do it
1. **State the gate first.** Name the goal of the period (a metric node to move or a Definition of
   Done). Every item is ranked against *this*, not against a generic score.
2. **List the candidates.** All of them, per direction — don't pre-cut before ranking. **Record the
   count that entered the ranking (N).** A list with no N cannot be audited later: a candidate quietly
   dropped before scoring is invisible, and "we prioritized" reads the same whether ten items competed
   or three did.
3. **Score each (RICE or ICE).** Reach · Impact · Confidence · (Effort). Use the score to *order*
   candidates; keep the number honest with a confidence tag, and remember it is an aid, not the
   verdict.
4. **Re-rank by gate contribution.** Sort by how much each item moves the period gate. A high score
   that doesn't move the gate ranks below a lower score that does.
5. **Check the link.** Each item must move a metric node (`M-…`) or test a hypothesis (`H-…`). An
   item that does neither is a candidate to cut — and a cut item is **recorded with its reason**, not
   deleted. Backlog is the visible reject of the must-set; an item excluded outright (no `M-…`/`H-…`
   link, out of scope, superseded) has nowhere else to be seen, so it gets its own line.
6. **Pick the must-set.** The minimum without which the period goal is unreachable — nothing more.
7. **Draw the line by capacity.** Fit the must-set inside the capacity from `resource-check`;
   everything past the line is backlog, ordered. If the must-set overflows capacity, cut scope or
   renegotiate the gate — do not inflate must.

> **Boundary with `segment-cvp` (one mechanism, one way).** A market-entry bundle arrives here
> **already scored for test-readiness** by `segment-cvp` — which bet is worth learning about first,
> on a scale that includes speed to a signal, an axis RICE does not have. This method does **not**
> re-score it. It answers the other question: does the staged test fit this period's capacity against
> the period gate. One object, one scale each; scoring a bundle twice on two scales is the drift the
> canon forbids.

## Anti-patterns
- **Flat list, no rank.** A pile of items with no ordering — the line can't be drawn.
- **Must inflated past capacity.** A "must" that doesn't fit the available resources; it's a wish
  list, not a plan.
- **Score for score's sake.** Ranking by RICE/ICE number with no tie back to the gate.
- **Orphan items.** Items with no `M-…` / `H-…` link — they move nothing and test nothing.

## Output
Fills `{#period-goals}` (Step 5) and `{#must}` / `{#backlog}` (Step 6) via
[`template-fragment.md`](template-fragment.md); inputs via [`questions.yaml`](questions.yaml).
