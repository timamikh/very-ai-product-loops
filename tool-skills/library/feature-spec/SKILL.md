---
node_type: card
kind: method
name: feature-spec
steps: [6]
prerequisites: [period-goals]
reads: [register:hypotheses, register:metrics, source:interview, source:kb]
writes: [worklog, section:must, section:backlog]
opinionated: false
method_basis: "Feature description at grooming altitude (Description / Scope / Acceptance criteria / Business value / User value / User stories)"
evidence_standard: decision
volume_rule: n/a
selection_rule: n/a
rejects_shown: n/a
status: draft
version: 0.3.0
updated: 2026-08-16
---
# Feature Spec (development direction)

Describe a **development** item as a **Feature** — the minimal level of detail this framework
works at (a feature, not sub-tasks). Fills items in `{#must}` / `{#backlog}` for the development
direction. This is the handoff altitude: enough for the team's development process to pick up and
groom deeper downstream.

**Method basis.** Feature description at grooming altitude.

## When to apply
- Step 6, for every development item in the sprint plan.

## Prerequisites
- **Period goals** — a feature must trace to a goal / metric node / hypothesis. *Missing → Step 5.*

## The format
Each feature has exactly these fields (keep them tight):

- **Description** — what the feature is.
- **Scope** — the list of tasks to implement it.
- **Acceptance criteria** — binary, checkable criteria for "the feature is done", each answerable
  yes/no. Distinct from Scope: Scope is what we build; acceptance criteria are how we know it's
  done.
- **Business value** — value to the business (link the `M-…` it moves / `H-…` it tests).
- **User value** — value to the user.
- **User stories** — related stories, if applicable ("As a … I want … so that …").

## Anti-patterns
- **Sub-task soup.** Dropping below feature altitude into implementation steps.
- **Orphan feature.** No link to a goal, metric, or hypothesis — a candidate to cut.
- **Value-free.** Missing business or user value.
- **Unverifiable done.** Acceptance criteria you can't answer yes/no to ("works well", "is fast") —
  or a Scope list restated as criteria; done stays negotiable.

## Worklog & projection
The working is done in the step's **worklog** `<step-folder>/feature-spec.md` (`node_type: worklog`,
e.g. `6-sprint-plan/feature-spec.md`): for each development item, its Description, Scope, Acceptance
criteria, Business value (the `M-…` it moves / `H-…` it tests), User value, and User stories. That
worklog is the **source of truth** for this method's rows; the Features subsections of `{#must}` /
`{#backlog}` (`### … Features <!-- tool: feature-spec, prioritization-sprint-plan -->`) are its
**projection** into the fixed shape of [`template-fragment.md`](template-fragment.md) — those
sections are co-filled (the ranking comes from `prioritization-sprint-plan`), but this method owns
its worklog for its own feature rows. The
projection holds nothing the worklog does not, and the step's change-log history lives in the worklog,
not the section (`process/CONVENTIONS.md` → *Step folders & worklogs*). External figures arrive here
dispatched from `sources/` by `source-intake`, cited in the worklog, never linked from the artifact.

## Output
Projects one block per feature into the Features subsections of `{#must}` / `{#backlog}` via
[`template-fragment.md`](template-fragment.md) from the worklog; inputs via
[`questions.yaml`](questions.yaml). Hands off to the team's development process.
