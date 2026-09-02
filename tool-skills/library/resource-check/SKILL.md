---
node_type: card
kind: method
name: resource-check
steps: [5]
prerequisites: [the period's dates, the candidate goals in draft, the capacity owners — a roster or the human — available to answer]
reads: [section:period-goals, source:interview, source:kb]
writes: [worklog, section:resources]
opinionated: false
method_basis: "Lightweight capacity survey (people · budget · time); full resource planning is a future integration"
evidence_standard: decision
volume_rule: n/a
selection_rule: n/a
rejects_shown: n/a
status: draft
version: 0.2.5
updated: 2026-09-02
---
# Resource Check

Assess **what resources are actually available this period** before committing to goals. Fills
`{#resources}`. For now this is a **simple survey of the user** — proper resource/capacity
planning is a future integration; don't fake precision we don't have.

**Method basis.** Lightweight capacity survey.

## When to apply
- Step 5, before drawing the must/backlog line — capacity bounds the plan.

## Prerequisites
- **The period's dates.** *Missing → confirm the cadence with the owner.*
- **Candidate goals in draft** — `{#period-goals}` as a candidate set per direction, so capacity
  is surveyed against something. *Missing → survey per the instance's directions, figures ⚙️.*
- **The capacity owners** — a roster filed in `sources/` (`source:kb`), the leads' answers
  (`source:interview`), or the owner on the questionnaire. *Missing → the survey cannot run.*

## How to do it
1. **People** — who's available per direction (dev / go-to-market / back-office) and at what capacity.
   A filed roster is `source:kb`; a survey of the leads whose answers return as filed notes is
   `source:interview`; the owner's own answers are the questionnaire.
2. **Budget** — spend available this period (and what it's earmarked for).
3. **Time** — the period length and any fixed dates/constraints.
4. **Flag the binding constraint** — the resource most likely to cap the plan.
5. **Record it as a commitment, not an observation.** Capacity is *stated* by the people who own
   it, so a number is worth the name attached to it: write who confirmed each figure and when, and
   the alternative declined ("two engineers, not three; the third stays on support"). That is why
   this method is a `decision`, not a reading.
6. Feed into `prioritization-tactical-plan` so the period goals fit the capacity.

## Anti-patterns
- **Fake precision.** Inventing capacity numbers instead of asking.
- **Ignoring the constraint.** Planning goals the resources can't support.

## Worklog & projection
Worklog: `5-tactical-plan/resource-check.md` — people / budget / time per direction, who confirmed each figure and when, the declined alternative behind each number, the binding constraint. Projects `{#resources}`; face: the **Binding constraint** line, via [`template-fragment.md`](template-fragment.md). Path form, primary/contributing and revisit rules: [`worklog-resolution.md`](../../../process/reference/worklog-resolution.md).

## Output
Projects `{#resources}` via [`template-fragment.md`](template-fragment.md) from the worklog — a short
capacity summary (people per direction · budget · time · the binding constraint) — with inputs from
[`questions.yaml`](questions.yaml).
