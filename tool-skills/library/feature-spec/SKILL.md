---
node_type: card
kind: method
name: feature-spec
steps: [6]
prerequisites: [period-goals]
reads: [section:period-goals, register:hypotheses, register:metrics, register:risks, register:features]
writes: [worklog, section:must, section:backlog, register:features]
opinionated: false
method_basis: "Feature description at grooming altitude (Description / Scope / Acceptance criteria / Business value / User value / User stories / Owner) + the register thread: the F-… it advances, a pre-registered Expected impact with a check-by, an S/M/L estimate; the Groom line is feature-grooming's"
evidence_standard: decision
volume_rule: n/a
selection_rule: n/a
rejects_shown: n/a
status: draft
version: 0.4.2
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

## How to do it
1. **Start from the goal.** Pick the period goal (`5#period-goals`) the item advances and the
   `M-…` / `H-…` / `R-…` behind it; an item that names none is an orphan — cut, not specced.
2. **Find or mint the `F-…` row.** Read `registers/features.md`: an existing `planned` row is picked
   up, never duplicated; a genuinely new candidate mints one (`direction` · `surface` · `serves`) —
   the method declares the write, the orchestrator mints.
3. **Fill the block, field for field** — the form is [`template-fragment.md`](template-fragment.md).
   Scope is what we build; acceptance criteria are how we know it is done, each answerable yes/no.
4. **Pre-register the Expected impact** before the sprint runs: the `M-…` baseline → expected from
   `metrics.csv`, the `R-…` it closes or the `H-…` it tests, plus a **check-by** (the sprint/date the
   claim becomes readable). `[assumption]` by definition; `impact-readout` reads exactly this at the
   next Step-5 gate — softened after the numbers land, it is a negotiation, not a read.
5. **Estimate as a class + range** — S/M/L, `[assumption]` until the readout records the actual;
   repeated misses in one class recalibrate how that class is sized.
6. **Close the block with the decision line.** The ranking is `prioritization-sprint-plan`'s, the
   **Groom** line `feature-grooming`'s — this card writes neither.

## The format
Field for field, the `{#must}` block of the step template: **Feature** (the `F-…`) · **Description**
· **Scope** (the tasks to implement it) · **Acceptance criteria** (binary — how we know it's done,
not what we build) · **Business value** (the `M-…` it moves / `H-…` it tests) · **User value** ·
**User stories** (if applicable: "As a … I want … so that …") · **Expected impact** · **Owner** (who
is accountable for it landing) · **Estimate** · **Groom** (spec-ready | blocked: <fork>, written by
`feature-grooming` when groomed).

## Anti-patterns
- **Sub-task soup.** Dropping below feature altitude into implementation steps.
- **Orphan feature.** No link to a goal, metric, or hypothesis — a candidate to cut.
- **Impact-free shipping.** No pre-registered Expected impact / check-by — the item ships, and
  nothing can ever say whether it worked.
- **Register bypass.** Speccing an item without naming its `F-…` — the work loses its cross-sprint
  identity and the backlog dies with the sprint again.
- **Value-free.** Missing business or user value.
- **Unverifiable done.** Acceptance criteria you can't answer yes/no to ("works well", "is fast") —
  or a Scope list restated as criteria; done stays negotiable.
- **Ownerless feature.** No named owner — "the team" lands nothing on time.

## Worklog & projection
Worklog: `6-sprint-plan/feature-spec.md` — one block per development item with every field of the format. Projects item blocks into the Features subsections of `{#must}` / `{#backlog}` (primary of their marker; the ranking comes from `prioritization-sprint-plan`, the Groom line from `feature-grooming`); no card slot — the section's face is the ranking's, via [`template-fragment.md`](template-fragment.md). Path form, primary/contributing and revisit rules: [`worklog-resolution.md`](../../../process/reference/worklog-resolution.md).

## Output
Projects one block per feature into the Features subsections of `{#must}` / `{#backlog}` via
[`template-fragment.md`](template-fragment.md) from the worklog; inputs via
[`questions.yaml`](questions.yaml). Hands off to the team's development process.
