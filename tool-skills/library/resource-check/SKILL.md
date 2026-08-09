---
name: resource-check
kind: research
produces: resources
reads_registers: []
writes_registers: []
inputs: [interview]
prerequisites: []
used_by_steps: [5]
opinionated: false
method_basis: "Lightweight capacity survey (people · budget · time); full resource planning is a future integration"
evidence_standard: decision
volume_rule: n/a
selection_rule: n/a
rejects_shown: n/a
status: draft
version: 0.2.1
updated: 2026-08-09
---

# Resource Check

Assess **what resources are actually available this period** before committing to goals. Fills
`{#resources}`. For now this is a **simple survey of the user** — proper resource/capacity
planning is a future integration; don't fake precision we don't have.

**Method basis.** Lightweight capacity survey.

## When to apply
- Step 5, before drawing the must/backlog line — capacity bounds the plan.

## How to do it
1. **People** — who's available per direction (dev / go-to-market / back-office) and at what capacity.
2. **Budget** — spend available this period (and what it's earmarked for).
3. **Time** — the period length and any fixed dates/constraints.
4. **Flag the binding constraint** — the resource most likely to cap the plan.
5. Feed into `prioritization` so the must-set fits the capacity.

## Anti-patterns
- **Fake precision.** Inventing capacity numbers instead of asking.
- **Ignoring the constraint.** Planning goals the resources can't support.

## Output
Fills `{#resources}` via [`template-fragment.md`](template-fragment.md) — a short capacity
summary (people per direction · budget · time · the binding constraint) — with inputs from
[`questions.yaml`](questions.yaml).
