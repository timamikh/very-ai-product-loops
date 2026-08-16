---
node_type: step
step: 6
name: sprint-plan
title: "Step 6 — Sprint Plan"
output: 6-sprint-plan.md
cadence: "~1–2 wk; every sprint"
method_basis: "sprint goal tied to the period gate · minimal must-set + prioritized backlog per direction · items in a per-direction format (dev = Feature; go-to-market = Activity; back-office = Task+DoD) · prioritization by contribution to the goal · explicit delivery"
status: draft
version: 0.3.0
updated: 2026-08-16
---

# Step 6 — Sprint Plan

**Goal.** Turn the period's goals into **sprint tasks per direction** — a minimal **must** set
(without which the period goal is unreachable) plus a **prioritized backlog** for the rest — and
hand off to the team's development process.

## Inputs (source slots)
The tactical plan (`5-tactical-plan.md`), backlog export, the hypothesis & metric registers.

## Output
`6-sprint-plan.md` — assembled from the section skeleton below. Template: [`template.md`](template.md).
The active [status](../../statuses/README.md) shapes the must-set:
`concept-viability` favors prototype/learning items (validate the bet); `pmf` favors items that
prove repeatable value and monetization; `growth` favors scale-and-defend items.

## Artifact skeleton
| Section (ID) | What | Recommended tool |
|--------------|------|------------------|
| `sprint-goal` | One or two lines: what this sprint must prove or move — ties to the period gate and the status's learning goal | — (synthesis) |
| `must` | Minimal mandatory items, grouped by direction, each in its per-direction format | `prioritization-sprint-plan`, `feature-spec`, `activity-spec`, `task-spec` |
| `backlog` | The rest, prioritized, grouped by direction | `prioritization-sprint-plan`, `feature-spec`, `activity-spec`, `task-spec` |
| `excluded` | Candidates that entered the ranking but were cut before backlog, each with why | `prioritization-sprint-plan` |
| `delivery` | What goes to the development process, and how | — (synthesis) |
| `to-clarify` | Unresolved sprint questions; resolved by deleting the line | — |

## Item formats by direction

The **minimal level of detail** for this framework is one **feature / activity / task** — not
sub-tasks. Each direction describes its items in its own format:

- **Development → Feature** (`feature-spec`)
  - **Description** — what the feature is
  - **Scope** — the list of tasks to implement it
  - **Acceptance criteria** — binary, checkable — how we know it's done (each answerable yes/no)
  - **Business value** — value to the business
  - **User value** — value to the user
  - **User stories** — related stories (if applicable)
  - **Owner** — who is accountable for it landing
  - **Estimate** — the capacity it consumes
- **Go-to-market → Activity** (`activity-spec`; same altitude; e.g. "launch a reactivation mailing", "publish a TG post on LLM pitfalls")
  - **Description** — what the activity is
  - **Scope** — the steps to run it
  - **Business value** — the metric/hypothesis it moves
  - **Audience value** — why the audience cares
  - **Links** — the `H-…` it tests / `M-…` it moves
  - **Owner** — who is accountable for it landing
  - **Estimate** — the capacity it consumes
- **Back-office → Task** (`task-spec`)
  - **Description** — what needs doing
  - **Why** — the business reason (the `M-…` it moves / `R-…` it mitigates / `H-…` it serves)
  - **Definition of Done** — binary: answerable yes/no at sprint end
  - **Owner** — who is accountable for it landing
  - **Estimate** — the capacity it consumes

## Register touchpoints
- **Hypotheses / Metrics** — each task links to the `H-…` it tests or the `M-…` it moves
  (a task that moves neither is a candidate to cut).

## Gate checklist (soft) — each item ↔ artifact section
- [ ] a minimal must-set exists per direction → `sprint-plan#must`
- [ ] the rest is prioritized, not a flat list → `sprint-plan#backlog`
- [ ] dev items follow the **Feature** format; go-to-market items the **Activity** format; back-office items have a **DoD** → `sprint-plan#must` + `#backlog` · tick-id `item-format`
- [ ] every item links to a metric node or a hypothesis → `sprint-plan#must` + `#backlog` · tick-id `item-links`
- [ ] cut candidates are shown with a reason, not silently dropped → `sprint-plan#excluded` · tick-id `rejects-shown`
- [ ] delivery to the dev process is explicit → `sprint-plan#delivery`

## Cadence & invalidation
- **Cadence:** every sprint (~1–2 wk).
- **Invalidates downward:** — (this is the bottom of the cascade; the delivery feeds the team's
  own development flow, which is outside the framework).
- **From below:** sprint outcomes feed results back up — a refuted hypothesis or a missed goal
  bubbles to the Tactical Plan (5), and further up if a strategic bet is affected.

## The human's role
Draw the must/backlog line and approve the sprint; the agent ranks by contribution to the gate
and prepares the delivery. Downstream, work proceeds in the team's own development flow.
