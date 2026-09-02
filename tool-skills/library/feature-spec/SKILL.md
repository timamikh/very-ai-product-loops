---
node_type: card
kind: method
name: feature-spec
steps: [6]
prerequisites: [period-goals]
reads: [section:period-goals, register:hypotheses, register:metrics, register:risks, register:features]
writes: [worklog, section:must, section:backlog, register:features]
opinionated: false
method_basis: "Feature description at grooming altitude (Description / Scope / Acceptance criteria / Business value / User value / User stories) + the register thread: the F-… it advances, a pre-registered Expected impact with a check-by, an S/M/L estimate"
evidence_standard: decision
volume_rule: n/a
selection_rule: n/a
rejects_shown: n/a
status: draft
version: 0.4.1
updated: 2026-09-02
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

- **Feature** — the `F-…` register row this item advances. Check `registers/features.md` first: an
  existing `planned` row is picked up, not duplicated; a genuinely new candidate mints a `planned`
  row (the method declares the write, the orchestrator mints — with `direction`, `surface`,
  `serves`).
- **Description** — what the feature is.
- **Scope** — the list of tasks to implement it.
- **Acceptance criteria** — binary, checkable criteria for "the feature is done", each answerable
  yes/no. Distinct from Scope: Scope is what we build; acceptance criteria are how we know it's
  done.
- **Business value** — value to the business (link the `M-…` it moves / `H-…` it tests).
- **User value** — value to the user.
- **User stories** — related stories, if applicable ("As a … I want … so that …").
- **Expected impact** — pre-registered, before the sprint runs: the `M-…` it moves (baseline →
  expected, from `metrics.csv`), the `R-…` it closes, or the `H-…` it tests — plus a **check-by**
  (the sprint/date the claim becomes readable). `[assumption]` by definition. Read at the next
  Step-5 gate by `impact-readout`; softened after the numbers land, it is a negotiation, not a read.
- **Estimate** — a size class **S/M/L + a range**, `[assumption]` until the readout records the
  actual; repeated misses in one class recalibrate how that class is sized.

## Anti-patterns
- **Sub-task soup.** Dropping below feature altitude into implementation steps.
- **Orphan feature.** No link to a goal, metric, or hypothesis — a candidate to cut.
- **Impact-free shipping.** No pre-registered Expected impact / check-by — the item ships, and
  nothing can ever say whether it worked; the V stays open.
- **Register bypass.** Speccing an item without naming its `F-…` — the work loses its cross-sprint
  identity and the backlog dies with the sprint again.
- **Value-free.** Missing business or user value.
- **Unverifiable done.** Acceptance criteria you can't answer yes/no to ("works well", "is fast") —
  or a Scope list restated as criteria; done stays negotiable.

## Worklog & projection
Worklog: `6-sprint-plan/feature-spec.md` — one block per development item with every field of the format. Projects item blocks into the Features subsections of `{#must}` / `{#backlog}` (primary of their marker; the ranking comes from `prioritization-sprint-plan`, the Groom line from `feature-grooming`); no card slot — the section's face is the ranking's, via [`template-fragment.md`](template-fragment.md). Path form, primary/contributing and revisit rules: [`worklog-resolution.md`](../../../process/reference/worklog-resolution.md).

## Output
Projects one block per feature into the Features subsections of `{#must}` / `{#backlog}` via
[`template-fragment.md`](template-fragment.md) from the worklog; inputs via
[`questions.yaml`](questions.yaml). Hands off to the team's development process.
