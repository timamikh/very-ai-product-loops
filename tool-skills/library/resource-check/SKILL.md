---
node_type: card
kind: method
name: resource-check
steps: [5]
prerequisites: []
reads: [source:interview]
writes: [worklog, section:resources]
opinionated: false
method_basis: "Lightweight capacity survey (people · budget · time); full resource planning is a future integration"
evidence_standard: decision
volume_rule: n/a
selection_rule: n/a
rejects_shown: n/a
status: draft
version: 0.2.3
updated: 2026-08-09
---
# Resource Check

Assess **what resources are actually available this period** before committing to goals. Fills
`{#resources}`. For now this is a **simple survey of the user** — proper resource/capacity
planning is a future integration; don't fake precision we don't have.

**Method basis.** Lightweight capacity survey.

## When to apply
- Step 5, before drawing the must/backlog line — capacity bounds the plan.

## How to do it
1. **People** — who's available per direction (dev / go-to-market / back-office) and at what capacity.
2. **Budget** — spend available this period (and what it's earmarked for).
3. **Time** — the period length and any fixed dates/constraints.
4. **Flag the binding constraint** — the resource most likely to cap the plan.
5. **Record it as a commitment, not an observation.** Capacity is not measured here, it is *stated*
   by the people who own it — so the number is only worth the name attached to it. Write who
   confirmed each figure and when, and name the alternative that was declined ("two engineers, not
   three; the third stays on support"). An unattributed capacity number is the one everyone
   remembers differently at the end of the period, which is why this method is a `decision` and not a
   reading.
6. Feed into `prioritization-tactical-plan` so the period goals fit the capacity.

## Anti-patterns
- **Fake precision.** Inventing capacity numbers instead of asking.
- **Ignoring the constraint.** Planning goals the resources can't support.

## Worklog & projection
The working is done in the step's **worklog** `<step-folder>/resource-check.md` (`node_type: worklog`,
e.g. `5-tactical-plan/resource-check.md`): the people/budget/time survey per direction, who confirmed
each figure and when, the declined alternative behind each number, and the flagged binding constraint.
That worklog is the **source of truth**; the artifact section `{#resources}` is its **projection** into
the fixed shape of [`template-fragment.md`](template-fragment.md) — it holds nothing the worklog does
not, and the step's change-log history lives in the worklog, not the section
(`process/CONVENTIONS.md` → *Step folders & worklogs*). External figures arrive here dispatched from
`sources/` by `source-intake`, cited in the worklog, never linked from the artifact.

## Output
Projects `{#resources}` via [`template-fragment.md`](template-fragment.md) from the worklog — a short
capacity summary (people per direction · budget · time · the binding constraint) — with inputs from
[`questions.yaml`](questions.yaml).
