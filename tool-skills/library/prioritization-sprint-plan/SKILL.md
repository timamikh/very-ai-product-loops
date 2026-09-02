---
node_type: card
kind: method
name: prioritization-sprint-plan
steps: [6]
prerequisites: [candidate items, the period gate/goal, available resources]
reads: [section:period-goals, section:goal-targets, section:resources, register:metrics, register:hypotheses, register:features]
writes: [worklog, section:must, section:backlog, section:excluded]
opinionated: false
method_basis: "RICE/ICE as a ranking aid, ranked by contribution to the period gate; capacity-bounded must/backlog line"
evidence_standard: derived
volume_rule: "every candidate current for the sprint enters the ranking — none pre-cut; record the count N that entered"
selection_rule: "RICE/ICE as an ordering aid, re-ranked by contribution to the period gate; the must/backlog line is capacity-bounded"
rejects_shown: required
status: draft
version: 0.3.2
updated: 2026-09-02
---
# Prioritization — Sprint Plan

Rank the sprint's candidate **items** by their contribution to the gate of the period and draw the
**must / backlog line by capacity**. Fills `{#must}` / `{#backlog}` / `{#excluded}` (Step 6).

**Item vs goal — the boundary with `prioritization-tactical-plan`.** An *item* is one sprint-level
piece of work — a Feature, Activity or Task carrying an `F-…`, a pre-registered `Expected impact`
and an `Estimate` — and is what this method ranks and lines. A *goal* is the period-level outcome
the item advances (`5#period-goals`, sized in `5#goal-targets`); goals are ranked at Step 5 by
[`prioritization-tactical-plan`](../prioritization-tactical-plan/SKILL.md), never here. Both cards
run the same ranking procedure — [`references/rice-procedure.md`](../references/rice-procedure.md)
— and neither restates it.

**One notion of estimate.** The spec's `Estimate` field — a size class S/M/L plus a range,
`[assumption]` until `impact-readout` reads the actual. This method sums those classes against the
capacity carried from `5#resources` to draw the line; it never re-estimates an item, and the
backlog's `Est.` column repeats the spec's class.

**Method basis.** RICE/ICE as a ranking aid, ordered by contribution to the period gate; the
must-set is the minimum without which the period goal is unreachable, and the line between must and
backlog is set by capacity, not by wishful scope.

## When to apply
- Step 6, to split the sprint's items into a minimal **must** set, a prioritized **backlog**, and a
  visible **excluded** list.
- Whenever candidate items exceed capacity and the line has to be drawn.

## Prerequisites
- **Candidate items** — the features/activities/tasks to rank. The standing pool is the feature
  register's `planned` rows — a candidate cut last sprint is still there, by id. *Missing → generate
  them from `5#period-goals`, the hypothesis register and the `planned` rows.*
- **The period gate / goal** — `5#period-goals` / `5#goal-targets`. *Missing → run the Step 5 gate.*
- **Available resources** — `5#resources`. *Missing → run `resource-check` (Step 5) or state the
  sprint's capacity explicitly.*

## How to do it
1. **State the sprint's contribution to the gate.** The gate is the period's (`5#period-goals`);
   name what *this sprint* must move or prove toward it — the ordering key for items.
2. **List the candidates — the weighted pool first.** The feature register's `planned` rows lead, in
   `priority` order: `now` rows (Step 4's structural seed re-weighed by Step 5's period fit) come
   first, and a `now` row left out of the must-set owes a written reason. Then the new ideas.
   Record N.
3. **Run the ranking procedure on the items** — RICE/ICE per item as the aid, rank by gate
   contribution, link check, every cut with its reason:
   [`rice-procedure.md`](../references/rice-procedure.md). Reach, impact, confidence and effort are
   asked per item ([`questions.yaml`](questions.yaml)) — items are new work nothing on file scores.
4. **Pick the must-set.** The minimum without which the period goal is unreachable — nothing more.
5. **Draw the line by capacity.** Sum the must-set's estimate classes against `5#resources`;
   everything past the line is backlog, ordered. If must overflows, cut scope or renegotiate the
   gate — do not inflate must.
6. **Place the rejects.** Backlog is the visible reject of the must-set. An item excluded outright
   (no `M-…`/`H-…` link, out of scope, superseded) has nowhere else to be seen, so it gets its own
   line in `{#excluded}` — and its `F-…` row **stays `planned`** in the register with the cut noted,
   so the pool never silently shrinks.

> **Boundary with the item specs (one mechanism, one way).** This method decides the *order* and
> the *line*; what each item **is** comes from its spec — [`feature-spec`](../feature-spec/SKILL.md)
> · [`activity-spec`](../activity-spec/SKILL.md) · [`task-spec`](../task-spec/SKILL.md). This method
> does not re-describe items, and the specs do not re-rank them.

## Anti-patterns
The shared five are in the reference. This card's own:
- **Must inflated past capacity.** A "must" that doesn't fit the available resources is a wish list,
  not a plan.
- **Silent exclusion.** An item cut from the ranking with no `{#excluded}` line — the next sprint
  re-proposes it and the selection can't be audited.
- **Re-estimated in the ranking.** An `Est.` that differs from the spec's class — two estimates for
  one item, and the readout can calibrate neither.
- **A `now` row skipped without a word.** The feature register's weighting ignored — Step 5's
  period pass wasted.

## Worklog & projection
Worklog: `6-sprint-plan/prioritization-sprint-plan.md` — the gate stated first, the full candidate list with N, the RICE/ICE scores, the re-rank by gate contribution, the must-set at the capacity line, the ordered backlog, every excluded item with its reason. Projects `{#must}` (face: **Gate of the period**), `{#backlog}` (face: **Backlog read**) and `{#excluded}` (face: **Excluded read**) via [`template-fragment.md`](template-fragment.md). In `{#must}`'s per-direction subsections the spec named first owns the item blocks; the ranking and the line live here. Path form, primary/contributing and revisit rules: [`worklog-resolution.md`](../../../process/reference/worklog-resolution.md).

## Output
Projects `{#must}` / `{#backlog}` / `{#excluded}` (Step 6) via
[`template-fragment.md`](template-fragment.md) from its worklog; inputs via
[`questions.yaml`](questions.yaml). Item descriptions come from `feature-spec` / `activity-spec` /
`task-spec`.
