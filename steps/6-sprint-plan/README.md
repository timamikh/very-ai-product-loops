---
node_type: step
step: 6
name: sprint-plan
title: "Step 6 — Sprint Plan"
output: sprint-plan.md
cadence: "~1–2 wk; every sprint"
method_basis: "minimal must-set + prioritized backlog per direction · prioritization by contribution to the period goal · explicit handoff"
status: draft
version: 0.1.0
updated: 2026-07-16
---

# Step 6 — Sprint Plan

**Goal.** Turn the period's goals into **sprint tasks per direction** — a minimal **must** set
(without which the period goal is unreachable) plus a **prioritized backlog** for the rest — and
hand off to the team's development process.

## Inputs (source slots)
The tactical plan (`[[tactical-plan]]`), backlog export, the hypothesis & metric registers.

## Output
`sprint-plan.md`.

## Artifact skeleton
| Section (ID) | What | Recommended tool |
|--------------|------|------------------|
| `must` | Minimal mandatory tasks, grouped by direction | `prioritization` |
| `backlog` | The rest, prioritized, grouped by direction | `prioritization` |
| `handoff` | What goes to the development process, and how | — |

## Register touchpoints
- **Hypotheses / Metrics** — each task links to the `H-…` it tests or the `M-…` it moves
  (a task that moves neither is a candidate to cut).

## Gate checklist (soft) — each item ↔ artifact section
- [ ] a minimal must-set exists per direction → `sprint-plan#must`
- [ ] the rest is prioritized, not a flat list → `sprint-plan#backlog`
- [ ] every task links to a metric node or a hypothesis → `sprint-plan#must` / `#backlog`
- [ ] handoff to the dev process is explicit → `sprint-plan#handoff`

## Cadence & invalidation
- **Cadence:** every sprint (~1–2 wk).
- **From below:** sprint outcomes feed results back up — a refuted hypothesis or a missed goal
  bubbles to the Tactical Plan (5), and further up if a strategic bet is affected.

## The human's role
Draw the must/backlog line and approve the sprint; the agent ranks by contribution to the gate
and prepares the handoff. Downstream, work proceeds in the team's own development flow.
