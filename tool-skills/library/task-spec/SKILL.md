---
name: task-spec
kind: template
produces: [must, backlog]
prerequisites: [period-goals]
reads_registers: [hypotheses, metrics, risks]
writes_registers: []
inputs: [interview, kb]
used_by_steps: [6]
opinionated: false
method_basis: "Back-office task description (Description / Why with an M-…/R-…/H-… link / binary DoD / Owner / Estimate)"
evidence_standard: decision
volume_rule: n/a
selection_rule: n/a
rejects_shown: n/a
status: draft
version: 0.1.0
updated: 2026-08-16
---

# Task Spec (back-office direction)

Describe a **back-office** item as a **Task** — the minimal level of detail this framework works at
(a task, not sub-tasks). Fills items in `{#must}` / `{#backlog}` for the back-office direction. A
task is done when its DoD answers **yes** — nothing softer.

**Method basis.** Task description at handover altitude: what needs doing, why the business needs
it (linked, not asserted), a binary Definition of Done, who owns it, and what it costs.

## When to apply
- Step 6, for every back-office item in the sprint plan (an ops fix, a compliance step, a data
  migration, a hiring task).

## Prerequisites
- **Period goals** — a task must trace to a goal / metric node / risk / hypothesis. *Missing → Step 5.*

## The format
Each task has exactly these fields (keep them tight):

- **Description** — what needs doing.
- **Why** — the business reason, as a link: the `M-…` it moves, the `R-…` it mitigates, or the
  `H-…` it serves.
- **Definition of Done** — binary: answerable yes/no at sprint end.
- **Owner** — who is accountable for it landing.
- **Estimate** — the capacity it consumes.

## Anti-patterns
- **A DoD you can't answer yes/no to.** "Improve the onboarding docs" is a direction, not a DoD —
  done is undecidable, so the task never closes and never fails.
- **A task with no link.** No `M-…` / `R-…` / `H-…` — it moves nothing, mitigates nothing, tests
  nothing; a candidate to cut.
- **Sub-task soup.** Dropping below task altitude into implementation steps.
- **Ownerless task.** No named owner — "the team" delivers nothing on time.

## Worklog & projection
The working is done in the step's **worklog** `<step-folder>/task-spec.md` (`node_type: worklog`,
e.g. `6-sprint-plan/task-spec.md`): for each back-office item, its Description, Why (the `M-…` /
`R-…` / `H-…` link), binary Definition of Done, Owner, and Estimate. That worklog is the **source
of truth** for this method's rows; the Tasks subsection of `{#must}` / `{#backlog}`
(`### … Tasks <!-- tool: task-spec, prioritization-sprint-plan -->`) is its **projection** into the
fixed shape of [`template-fragment.md`](template-fragment.md) — those sections are co-filled (the
ranking comes from `prioritization-sprint-plan`), but this method owns its worklog for its own task
rows. The projection holds nothing the worklog does not, and the step's change-log history lives in
the worklog, not the section (`process/CONVENTIONS.md` → *Step folders & worklogs*). External
figures arrive here dispatched from `sources/` by `source-intake`, cited in the worklog, never
linked from the artifact.

## Output
Projects one block per task into the Tasks subsections of `{#must}` / `{#backlog}` via
[`template-fragment.md`](template-fragment.md) from the worklog; inputs via
[`questions.yaml`](questions.yaml). Hands off to the team's own process.
