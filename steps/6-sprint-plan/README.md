---
node_type: step
step: 6
name: sprint-plan
title: "Step 6 — Sprint Plan"
output: sprint-plan.md
cadence: "~1–2 wk; every sprint"
method_basis: "minimal must-set + prioritized backlog per direction · items in a per-direction format (dev = Feature; go-to-market = Activity; back-office = Task+DoD) · prioritization by contribution to the goal · explicit handoff"
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
`sprint-plan.md`. The active [status](../../statuses/README.md) shapes the must-set:
`concept-viability` favors prototype/learning items (validate the bet); `pmf` favors items that
prove repeatable value and monetization; `growth` favors scale-and-defend items.

## Artifact skeleton
| Section (ID) | What | Recommended tool |
|--------------|------|------------------|
| `must` | Minimal mandatory items, grouped by direction, each in its per-direction format | `prioritization`, `feature-spec`, `activity-spec` |
| `backlog` | The rest, prioritized, grouped by direction | `prioritization`, `feature-spec`, `activity-spec` |
| `handoff` | What goes to the development process, and how | — |

## Item formats by direction

The **minimal level of detail** for this framework is one **feature / activity / task** — not
sub-tasks. Each direction describes its items in its own format:

- **Development → Feature**
  - **Description** — what the feature is
  - **Scope** — the list of tasks to implement it
  - **Business value** — value to the business
  - **User value** — value to the user
  - **User stories** — related stories (if applicable)
- **Go-to-market → Activity** (same altitude; e.g. "launch a reactivation mailing", "publish a TG post on LLM pitfalls")
  - **Description** — what the activity is
  - **Scope** — the steps to run it
  - **Business value** — the metric/hypothesis it moves
  - **Audience value** — why the audience cares
  - **Links** — the `H-…` it tests / `M-…` it moves
- **Back-office → Task**
  - **Description** — what needs doing
  - **Definition of Done** — the concrete DoD
  - **Why** — the business reason

## Register touchpoints
- **Hypotheses / Metrics** — each task links to the `H-…` it tests or the `M-…` it moves
  (a task that moves neither is a candidate to cut).

## Gate checklist (soft) — each item ↔ artifact section
- [ ] a minimal must-set exists per direction → `sprint-plan#must`
- [ ] the rest is prioritized, not a flat list → `sprint-plan#backlog`
- [ ] dev items follow the **Feature** format; go-to-market items the **Activity** format; back-office items have a **DoD** → `sprint-plan#must` / `#backlog`
- [ ] every item links to a metric node or a hypothesis → `sprint-plan#must` / `#backlog`
- [ ] handoff to the dev process is explicit → `sprint-plan#handoff`

## Cadence & invalidation
- **Cadence:** every sprint (~1–2 wk).
- **Invalidates downward:** — (this is the bottom of the cascade; the handoff feeds the team's
  own development flow, which is outside the framework).
- **From below:** sprint outcomes feed results back up — a refuted hypothesis or a missed goal
  bubbles to the Tactical Plan (5), and further up if a strategic bet is affected.

## The human's role
Draw the must/backlog line and approve the sprint; the agent ranks by contribution to the gate
and prepares the handoff. Downstream, work proceeds in the team's own development flow.
