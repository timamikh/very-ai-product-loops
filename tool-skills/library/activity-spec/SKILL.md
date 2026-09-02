---
node_type: card
kind: method
name: activity-spec
steps: [6]
prerequisites: [period-goals]
reads: [section:period-goals, section:market-bundles, register:hypotheses, register:metrics, register:features, register:surfaces]
writes: [worklog, section:must, section:backlog, register:features, register:surfaces]
opinionated: false
method_basis: "Go-to-market activity at the same altitude as a feature (Description / Scope / Business value / Audience value / Links) + the register thread: the F-… (campaign/content line) it advances on an S-… surface, a pre-registered Expected impact with a check-by, an S/M/L estimate"
evidence_standard: decision
volume_rule: n/a
selection_rule: n/a
rejects_shown: n/a
status: draft
version: 0.5.1
updated: 2026-09-02
---
# Activity Spec (go-to-market direction)

Describe a **go-to-market** item as an **Activity** — the go-to-market-direction counterpart of a
feature, at the same altitude (e.g. "launch a reactivation mailing", "publish a TG post on LLM
pitfalls"). Fills go-to-market items in `{#must}` / `{#backlog}`. Mirrors `feature-spec` so both
directions read the same way and plug into the same must/backlog.

**Method basis.** Activity described at feature altitude, tied to the metric/hypothesis it serves.

## When to apply
- Step 6, for every go-to-market item in the sprint plan.

## Prerequisites
- **Period goals** — an activity must trace to a go-to-market goal / metric node / hypothesis.

## The format
- **Feature** — the `F-…` register row this activity advances: the campaign or content line, at
  feature altitude ("the AI content line" is the row; "post id 123" is this item — its external id
  lands in Links after the run). An existing `planned` row is picked up; a new one is minted
  `planned`.
- **Description** — what the activity is.
- **Scope** — the steps to run it (draft copy, pick audience, schedule, publish, measure).
- **Business value** — the `M-…` it moves or the `H-…` it tests.
- **Audience value** — why the audience cares (not spam).
- **Links** — `H-…` tested / `M-…` moved; the **surface** it runs on (`S-…`,
  `registers/surfaces.md` — an activity opening a surface the register does not hold, a new
  community or channel, declares a new `planned` `S-…` row: the same mint discipline as features); the `B-…` bundle it launches when the activity runs a Step-5
  market-entry bundle — without the link, the sprint doesn't say which bundle it is testing;
  the shipped artifact's external id (post, mailing) after the run.
- **Expected impact** — pre-registered: the `M-…` it moves (baseline → expected) or the `H-…` it
  tests, plus a **check-by**. Read at the next Step-5 gate by `impact-readout`.
- **Owner** — who runs it.
- **Estimate** — a size class **S/M/L + a range**, `[assumption]` until the readout records the
  actual (the must-set must fit the capacity).

## Anti-patterns
- **Activity without a metric.** A campaign that moves no known node — a candidate to cut.
- **Channel-first, value-last.** Running a channel with no reason the audience benefits.
- **No measurement step.** An activity with no way to tell if it worked (attribution first).

## Worklog & projection
Worklog: `6-sprint-plan/activity-spec.md` — one block per go-to-market item with every field of the format. Projects item blocks into the Activities subsections of `{#must}` / `{#backlog}` (primary of their marker; the ranking comes from `prioritization-sprint-plan`); no card slot — the section's face is the ranking's, via [`template-fragment.md`](template-fragment.md). Path form, primary/contributing and revisit rules: [`worklog-resolution.md`](../../../process/reference/worklog-resolution.md).

## Output
Projects one block per activity into the Activities subsections of `{#must}` / `{#backlog}` via
[`template-fragment.md`](template-fragment.md) from the worklog; inputs via
[`questions.yaml`](questions.yaml).
