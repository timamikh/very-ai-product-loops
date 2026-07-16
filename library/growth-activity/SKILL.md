---
name: growth-activity
kind: template
produces: must
reads_registers: [hypotheses, metrics]
writes_registers: []
inputs: [interview, kb]
prerequisites: [period-goals]
used_by_steps: [6]
opinionated: false
method_basis: "Growth activity at the same altitude as a feature (Description / Scope / Business value / Audience value / Links)"
status: draft
version: 0.1.0
updated: 2026-07-16
---

# Growth Activity (growth direction)

Describe a **growth** item as an **Activity** — the growth-direction counterpart of a feature,
at the same altitude (e.g. "launch a reactivation mailing", "publish a TG post on LLM pitfalls").
Fills growth items in `{#must}` / `{#backlog}`. Mirrors `feature-spec` so both directions read
the same way and plug into the same must/backlog.

**Method basis.** Activity described at feature altitude, tied to the metric/hypothesis it serves.

## When to apply
- Step 6, for every growth item in the sprint plan.

## Prerequisites
- **Period goals** — an activity must trace to a growth goal / metric node / hypothesis.

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
