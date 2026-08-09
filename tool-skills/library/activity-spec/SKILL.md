---
name: activity-spec
kind: template
produces: [must, backlog]
reads_registers: [hypotheses, metrics]
writes_registers: []
inputs: [interview, kb]
prerequisites: [period-goals]
used_by_steps: [6]
opinionated: false
method_basis: "Go-to-market activity at the same altitude as a feature (Description / Scope / Business value / Audience value / Links)"
evidence_standard: decision
volume_rule: n/a
selection_rule: n/a
rejects_shown: n/a
status: draft
version: 0.2.2
updated: 2026-08-09
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
- **Description** — what the activity is.
- **Scope** — the steps to run it (draft copy, pick audience, schedule, publish, measure).
- **Business value** — the `M-…` it moves or the `H-…` it tests.
- **Audience value** — why the audience cares (not spam).
- **Links** — `H-…` tested / `M-…` moved; the surface it runs on (from `product-surface`).

## Anti-patterns
- **Activity without a metric.** A campaign that moves no known node — a candidate to cut.
- **Channel-first, value-last.** Running a channel with no reason the audience benefits.
- **No measurement step.** An activity with no way to tell if it worked (attribution first).

## Output
One block per activity via [`template-fragment.md`](template-fragment.md); inputs via
[`questions.yaml`](questions.yaml).
