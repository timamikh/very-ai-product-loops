---
name: feature-spec
kind: template
produces: [must, backlog]
reads_registers: [hypotheses, metrics]
writes_registers: []
inputs: [interview, kb]
prerequisites: [period-goals]
used_by_steps: [6]
opinionated: false
method_basis: "Feature description at grooming altitude (Description / Scope / Business value / User value / User stories)"
status: draft
version: 0.2.0
updated: 2026-07-18
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
- **Business value** — value to the business (link the `M-…` it moves / `H-…` it tests).
- **User value** — value to the user.
- **User stories** — related stories, if applicable ("As a … I want … so that …").

## Anti-patterns
- **Sub-task soup.** Dropping below feature altitude into implementation steps.
- **Orphan feature.** No link to a goal, metric, or hypothesis — a candidate to cut.
- **Value-free.** Missing business or user value.

## Output
One block per feature via [`template-fragment.md`](template-fragment.md); inputs via
[`questions.yaml`](questions.yaml). Hands off to the team's development process.
