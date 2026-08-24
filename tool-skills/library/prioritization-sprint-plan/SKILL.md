---
node_type: card
kind: method
name: prioritization-sprint-plan
steps: [6]
prerequisites: [candidate items, the period gate/goal, available resources]
reads: [register:metrics, register:hypotheses, register:features]
writes: [worklog, section:must, section:backlog, section:excluded]
opinionated: false
method_basis: "RICE/ICE as a ranking aid, ranked by contribution to the period gate; capacity-bounded must/backlog line"
evidence_standard: derived
volume_rule: "every candidate current for the sprint enters the ranking — none pre-cut; record the count N that entered"
selection_rule: "RICE/ICE as an ordering aid, re-ranked by contribution to the period gate; the must/backlog line is capacity-bounded"
rejects_shown: required
status: draft
version: 0.3.0
updated: 2026-08-24
---
# Prioritization — Sprint Plan

Rank the sprint's candidate items by their **contribution to the gate of the period** — not by an
abstract score — and draw the **must / backlog line by capacity**. Fills `{#must}` / `{#backlog}` /
`{#excluded}` (Step 6). The period-level ranking of goals is the sibling method
[`prioritization-tactical-plan`](../prioritization-tactical-plan/SKILL.md) (Step 5) — one step, one
skill.

**Method basis.** RICE/ICE scoring (Reach · Impact · Confidence · Effort) used as a *ranking* aid,
not an oracle: the ordering key is how much each item moves the period gate. The must-set is the
minimum without which the period goal is unreachable; the line between must and backlog is set by
the available capacity from `resource-check` (as carried into the tactical plan), not by wishful
scope.

## When to apply
- Step 6, to split the sprint's items into a minimal **must** set, a prioritized **backlog**, and a
  visible **excluded** list.
- Whenever candidate items exceed capacity and the line has to be drawn.

## Prerequisites
- **Candidate items** — the features/activities/tasks to rank. The standing pool is the feature
  register's `planned` rows — a candidate cut last sprint is still there, by id. *Missing → generate
  them from the period goals, the metric tree, the hypothesis register and the `planned` rows.*
- **The period gate / goal** — the target each item is ranked against. *Missing → run the Step 5
  gate (`period-goals` / `goal-targets`).*
- **Available resources** — the capacity that sets the must/backlog line. *Missing → run
  `resource-check` (Step 5) or state the sprint's capacity explicitly.*

## How to do it
1. **State the gate first.** Name the goal of the period (a metric node to move or a Definition of
   Done) and the sprint's contribution to it. Every item is ranked against *this*, not against a
   generic score.
2. **List the candidates.** All of them, per direction — the feature register's `planned` rows
   first (the pool that survives between sprints, **already weighted**: its `priority` column
   carries Step 4's structural seed re-weighed by Step 5's period fit — `now` rows lead, and a
   `now` row left out of the must-set owes a written reason), then the new ideas. Don't pre-cut before ranking. **Record the
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
   link, out of scope, superseded) has nowhere else to be seen, so it gets its own line in
   `{#excluded}` — and its `F-…` row **stays `planned`** in the register (with the cut noted), so
   the pool never silently shrinks.
6. **Pick the must-set.** The minimum without which the period goal is unreachable — nothing more.
7. **Draw the line by capacity.** Fit the must-set inside the available capacity; everything past
   the line is backlog, ordered. If the must-set overflows capacity, cut scope or renegotiate the
   gate — do not inflate must.

> **Boundary with the item specs (one mechanism, one way).** This method decides the *order* and
> the *line*; what each item **is** comes from its spec: a development item follows
> [`feature-spec`](../feature-spec/SKILL.md), a go-to-market item
> [`activity-spec`](../activity-spec/SKILL.md), a back-office item
> [`task-spec`](../task-spec/SKILL.md). This method does not re-describe items, and the specs do
> not re-rank them.

## Anti-patterns
- **Flat list, no rank.** A pile of items with no ordering — the line can't be drawn.
- **Must inflated past capacity.** A "must" that doesn't fit the available resources; it's a wish
  list, not a plan.
- **Score for score's sake.** Ranking by RICE/ICE number with no tie back to the gate.
- **Orphan items.** Items with no `M-…` / `H-…` link — they move nothing and test nothing.
- **Silent exclusion.** An item cut from the ranking with no `{#excluded}` line — the next sprint
  re-proposes it and the selection can't be audited.

## Worklog & projection
The working is done in the step's **worklog** `<step-folder>/prioritization-sprint-plan.md`
(`node_type: worklog`, e.g. `6-sprint-plan/prioritization-sprint-plan.md`): the period gate stated
first, the full candidate list **with N recorded**, the RICE/ICE scores, the re-rank by gate
contribution, the must-set drawn at the capacity line, the ordered backlog, and every **excluded
item with its reason**. That worklog is the **source of truth** — this method is a full primary with
its own worklog, same mechanics as every skill; the artifact sections `{#must}` / `{#backlog}` /
`{#excluded}` are its **projection** into the fixed shape of
[`template-fragment.md`](template-fragment.md), holding nothing the worklog does not, with the
change-log history in the worklog (`process/CONVENTIONS.md` → *Step folders & worklogs*).

In `{#must}`'s per-direction subsections this method is co-marked with the item specs
(`<!-- tool: feature-spec, prioritization-sprint-plan -->` etc.) — the spec named first is the
subsection's primary for the item blocks; the ranking and the line still live in **this** method's
worklog.

## Output
Projects `{#must}` / `{#backlog}` / `{#excluded}` (Step 6) via
[`template-fragment.md`](template-fragment.md) from its worklog; inputs via
[`questions.yaml`](questions.yaml). Item descriptions come from `feature-spec` / `activity-spec` /
`task-spec`.
