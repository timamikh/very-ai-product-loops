---
node_type: card
kind: method
name: task-spec
steps: [6]
prerequisites: [period-goals]
reads: [section:period-goals, section:goal-targets, register:hypotheses, register:metrics, register:risks, register:features]
writes: [worklog, section:must, section:backlog, register:features]
opinionated: false
method_basis: "Back-office task description (Description / Why with an M-…/R-…/H-… link / binary DoD / Owner / Estimate) + the register thread: the F-… (capability) it advances, a pre-registered Expected impact with a check-by, an S/M/L estimate"
evidence_standard: decision
volume_rule: n/a
selection_rule: n/a
rejects_shown: n/a
status: draft
version: 0.2.2
updated: 2026-09-02
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

## Inputs
`5#period-goals` for the goal the task serves; `5#goal-targets` for that goal's Definition of Done
(back-office goals map to a DoD, and the task's DoD is one yes/no piece of it); the metric, risk and
hypothesis registers for the `M-…` / `R-…` / `H-…` the **Why** links; the feature register for the
`F-…` capability.

## How to do it
1. **Start from the goal.** Pick the period goal (`5#period-goals`) the task serves and the `M-…` /
   `R-…` / `H-…` behind it — the **Why** is that link, not an assertion. A task with none is a cut
   candidate.
2. **Find or mint the `F-…` row** — the lasting capability ("automated ticket triage", not the
   migration script that builds it). A genuine one-off with no lasting row keeps `— to clarify —`
   here — legal for tasks; a run of such one-offs is a hint a capability row is hiding.
3. **Fill the block, field for field** — the form is [`template-fragment.md`](template-fragment.md).
   The **Definition of Done** is binary — answerable yes/no at sprint end — and rolls up to the
   goal's DoD in `5#goal-targets`.
4. **Pre-register the Expected impact** — the `M-…` baseline → expected or the `R-…` → target
   status, plus a **check-by**. `impact-readout` reads exactly this at the next Step-5 gate.
5. **Estimate as a class + range** — S/M/L, `[assumption]` until the readout records the actual.
   Name the **Owner** and close the block with the decision line.

## The format
Field for field, the `{#must}` block of the step template: **Feature** (the `F-…` capability, or
`— to clarify —` for a one-off) · **Description** (what needs doing) · **Why** (the `M-…` it moves /
`R-…` it mitigates / `H-…` it serves) · **Definition of Done** (binary) · **Expected impact** ·
**Owner** · **Estimate**.

## Anti-patterns
- **A DoD you can't answer yes/no to.** "Improve the onboarding docs" is a direction, not a DoD —
  done is undecidable, so the task never closes and never fails.
- **A task with no link.** No `M-…` / `R-…` / `H-…` — it moves nothing, mitigates nothing, tests
  nothing; a candidate to cut.
- **Sub-task soup.** Dropping below task altitude into implementation steps.
- **Ownerless task.** No named owner — "the team" delivers nothing on time.

## Worklog & projection
Worklog: `6-sprint-plan/task-spec.md` — one block per back-office item with every field of the format. Projects item blocks into the Tasks subsections of `{#must}` / `{#backlog}` (primary of their marker; the ranking comes from `prioritization-sprint-plan`); no card slot — the section's face is the ranking's, via [`template-fragment.md`](template-fragment.md). Path form, primary/contributing and revisit rules: [`worklog-resolution.md`](../../../process/reference/worklog-resolution.md).

## Output
Projects one block per task into the Tasks subsections of `{#must}` / `{#backlog}` via
[`template-fragment.md`](template-fragment.md) from the worklog; inputs via
[`questions.yaml`](questions.yaml). Hands off to the team's own process.
