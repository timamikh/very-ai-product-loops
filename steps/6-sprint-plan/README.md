---
node_type: card
kind: step
name: sprint-plan
step: 6
title: "Step 6 — Sprint Plan"
output: 6-sprint-plan.md
prerequisites: [the tactical plan `5-tactical-plan.md` exists]
reads: [file:5-tactical-plan.md, file:3-strategy.md, register:hypotheses, register:metrics, register:risks, register:features, register:surfaces, source:kb]
writes: [section:*]
surfaces: [ticks, register:hypotheses, register:metrics, register:features, register:surfaces, sign-off, change-log]
cadence: "~1–2 wk; every sprint"
method_basis: "sprint goal tied to the period gate · minimal must-set + prioritized backlog per direction · items in a per-direction format (dev = Feature; go-to-market = Activity; back-office = Task+DoD) · every item advances an F-… and pre-registers its Expected impact with a check-by · prioritization by contribution to the goal · explicit delivery"
status: draft
version: 0.5.1
updated: 2026-09-02
---
# Step 6 — Sprint Plan

**Goal.** Turn the period's goals into **sprint tasks per direction** — a minimal **must** set
(without which the period goal is unreachable) plus a **prioritized backlog** for the rest — and
hand off to the team's development process.

## Inputs (the cards' read perimeter)
The tactical plan (`5-tactical-plan.md`: `{#period-goals}`, `{#goal-targets}`, `{#resources}`,
`{#market-bundles}`); the feature register (`planned` rows are the standing backlog, weighted by
`priority`) and the hypothesis, metric, risk and surface registers; for grooming, Step-3
`{#product-surface}` and `{#value-defensibility}` and inputs filed in `sources/` (`source:kb`).
Each card's `reads` names its subset.

## Output
`6-sprint-plan.md` — assembled from the skeleton below. Template: [`template.md`](template.md). The
active [status](../../statuses/README.md) shapes the must-set: `concept-viability` favors
prototype/learning items; `pmf` items that prove repeatable value and monetization; `growth`
scale-and-defend items.

## Artifact skeleton
| Section (ID) | What | Recommended tool |
|--------------|------|------------------|
| `sprint-goal` | One or two lines: what this sprint must prove or move — ties to the period gate and the status's learning goal | — (synthesis) |
| `must` | Minimal mandatory items, grouped by direction, each in its per-direction format | `prioritization-sprint-plan`, `feature-spec`, `activity-spec`, `task-spec`, `feature-grooming` |
| `backlog` | The rest, prioritized, grouped by direction | `prioritization-sprint-plan`, `feature-spec`, `activity-spec`, `task-spec`, `feature-grooming` |
| `excluded` | Candidates that entered the ranking but were cut before backlog, each with why | `prioritization-sprint-plan` |
| `delivery` | What goes to the development process, and how | — (synthesis) |
| `to-clarify` | Unresolved sprint questions; resolved by deleting the line | — |

## Item formats by direction

The **minimal level of detail** is one **feature / activity / task** — not sub-tasks. The form of
record per direction is the `{#must}` block of [`template.md`](template.md): **Development →
Feature** ([`feature-spec`](../../tool-skills/library/feature-spec/SKILL.md)), **Go-to-market →
Activity** ([`activity-spec`](../../tool-skills/library/activity-spec/SKILL.md)), **Back-office →
Task** ([`task-spec`](../../tool-skills/library/task-spec/SKILL.md)). Items are numbered `1, 2, 3`
within their direction subsection — sprint-local; the cross-sprint identity is the `F-…` every item
names. `**Feature:**`, `**Expected impact:**`, `**Estimate:**` and `**Groom:**` are fixed
machine-read literals ([`column-keys.md`](../../process/reference/column-keys.md)).

## From feature to development instruction (the dev handoff chain)

A development item hands off at one of two altitudes. Default: **feature altitude** — the
`feature-spec` block goes to the team's own grooming. When the team implements **from a written
instruction**, the chain continues inside the step: `feature-spec` describes the item →
[`feature-grooming`](../../tool-skills/library/feature-grooming/SKILL.md) closes every product/UX/business
fork with the product owner, records the technical forks for the tech lead and picks the document
type (an open product fork = not spec-ready) →
[`outputs/feature-to-spec`](../../tool-skills/outputs/feature-to-spec/SKILL.md) authors the
instruction (BRD/PRD or tech spec) at `export-files/<feature>-spec.md`, scope-faithful, WHAT-not-HOW.
`{#delivery}` names the file per handed-off feature.

## Register touchpoints
- **Hypotheses / Metrics** — each item links to the `H-…` it tests or the `M-…` it moves; one that
  moves neither is a candidate to cut.
- **Features & surfaces** — each item names the `F-…` it advances; a new candidate mints a `planned`
  row, an activity opening a new channel mints a `planned` `S-…` (the specs declare the write, the
  orchestrator mints). A cut candidate stays `planned` — the backlog no longer dies between sprints.
  Shipped items are read at the next Step-5 gate (`impact-readout`), which flips `planned → live`.

## Gate checklist (soft) — each item ↔ artifact section
- [ ] a minimal must-set exists per direction → `sprint-plan#must`
- [ ] the rest is prioritized, not a flat list → `sprint-plan#backlog`
- [ ] dev items follow the **Feature** format; go-to-market items the **Activity** format; back-office items have a **DoD** → `sprint-plan#must` + `#backlog` · tick-id `item-format`
- [ ] every item links to a metric node or a hypothesis → `sprint-plan#must` + `#backlog` · tick-id `item-links`
- [ ] every must item names its `F-…` and pre-registers an Expected impact with a check-by → `sprint-plan#must` · tick-id `item-feature`
- [ ] cut candidates are shown with a reason, not silently dropped → `sprint-plan#excluded` · tick-id `rejects-shown`
- [ ] delivery to the dev process is explicit → `sprint-plan#delivery`
- [ ] open questions logged for the human to resolve → `sprint-plan#to-clarify`

## Cadence & invalidation
- **Cadence:** every sprint (~1–2 wk).
- **Invalidates downward:** — (the bottom of the cascade; delivery feeds the team's own flow,
  outside the framework).
- **From below:** shipped items are read against their pre-registered expectations at the next
  Step-5 gate (`impact-readout`); a refuted hypothesis or a missed expectation bubbles to the
  Tactical Plan (5), and further up if a strategic bet is affected.

## The human's role
Draw the must/backlog line and approve the sprint; the agent ranks by contribution to the gate
and prepares the delivery. Downstream, work proceeds in the team's own development flow.
