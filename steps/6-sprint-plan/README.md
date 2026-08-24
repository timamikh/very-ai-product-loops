---
node_type: card
kind: step
name: sprint-plan
step: 6
title: "Step 6 — Sprint Plan"
output: 6-sprint-plan.md
prerequisites: [the tactical plan `5-tactical-plan.md` exists]
reads: [file:5-tactical-plan.md, register:hypotheses, register:metrics, register:features]
writes: [section:*]
surfaces: [ticks, register:hypotheses, register:metrics, register:features, sign-off, change-log]
cadence: "~1–2 wk; every sprint"
method_basis: "sprint goal tied to the period gate · minimal must-set + prioritized backlog per direction · items in a per-direction format (dev = Feature; go-to-market = Activity; back-office = Task+DoD) · every item advances an F-… and pre-registers its Expected impact with a check-by · prioritization by contribution to the goal · explicit delivery"
status: draft
version: 0.5.0
updated: 2026-08-23
---
# Step 6 — Sprint Plan

**Goal.** Turn the period's goals into **sprint tasks per direction** — a minimal **must** set
(without which the period goal is unreachable) plus a **prioritized backlog** for the rest — and
hand off to the team's development process.

## Inputs (source slots)
The tactical plan (`5-tactical-plan.md`), the feature register (`planned` rows are the standing backlog), the hypothesis & metric registers.

## Output
`6-sprint-plan.md` — assembled from the section skeleton below. Template: [`template.md`](template.md).
The active [status](../../statuses/README.md) shapes the must-set:
`concept-viability` favors prototype/learning items (validate the bet); `pmf` favors items that
prove repeatable value and monetization; `growth` favors scale-and-defend items.

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

The **minimal level of detail** for this framework is one **feature / activity / task** — not
sub-tasks. Each direction describes its items in its own format:

Items are numbered `1, 2, 3` within their direction subsection — sprint-local; the cross-sprint
identity is the feature register's `F-…`, which every item names. Three fields are shared by all
three formats: **Feature** (the `F-…` the item advances — a new candidate mints a `planned` row),
**Expected impact** (pre-registered: the `M-…` it moves with baseline → expected, the `R-…` it
closes, or the `H-…` it tests — plus a `check-by`; read at the next Step-5 gate by
`impact-readout`), and **Estimate** (class S/M/L + range, `[assumption]` until the readout reads
the actual — misses calibrate the sizing). These three labels are **fixed machine-read literals**
(`reference/column-keys.md`): in any documentation language the label carries verbatim — only the
value after it is written in the instance's language.

- **Development → Feature** (`feature-spec`)
  - **Feature** — the `F-…` it advances
  - **Description** — what the feature is
  - **Scope** — the list of tasks to implement it
  - **Acceptance criteria** — binary, checkable — how we know it's done (each answerable yes/no)
  - **Business value** — value to the business
  - **User value** — value to the user
  - **User stories** — related stories (if applicable)
  - **Expected impact** — pre-registered, with a check-by
  - **Owner** — who is accountable for it landing
  - **Estimate** — class S/M/L + range
- **Go-to-market → Activity** (`activity-spec`; same altitude; e.g. "launch a reactivation mailing", "publish a TG post on LLM pitfalls")
  - **Description** — what the activity is
  - **Scope** — the steps to run it
  - **Business value** — the metric/hypothesis it moves
  - **Audience value** — why the audience cares
  - **Feature / Surface** — the `F-…` (campaign/content line) it advances, on which `S-…`
  - **Links** — the `H-…` it tests / `M-…` it moves / `B-…` it launches
  - **Expected impact** — pre-registered, with a check-by
  - **Owner** — who is accountable for it landing
  - **Estimate** — class S/M/L + range
- **Back-office → Task** (`task-spec`)
  - **Feature** — the `F-…` (capability) it advances; `— to clarify —` for a one-off
  - **Description** — what needs doing
  - **Why** — the business reason (the `M-…` it moves / `R-…` it mitigates / `H-…` it serves)
  - **Definition of Done** — binary: answerable yes/no at sprint end
  - **Expected impact** — pre-registered, with a check-by
  - **Owner** — who is accountable for it landing
  - **Estimate** — class S/M/L + range

## From feature to development instruction (the dev handoff chain)

A development item can hand off at two altitudes. The default is **feature altitude**: the
`feature-spec` block goes to the team's own grooming. When the team implements **from a written
instruction**, the chain continues inside the step:

1. **`feature-spec`** — describes the item (Description / Scope / Acceptance criteria / Business
   value / User value / User stories).
2. **`feature-grooming`** — closes every **product/UX/business fork with the product owner**
   before anything is written for developers; records **technical forks** for the tech lead; picks
   the document type. A feature with an open product fork is not spec-ready.
3. **[`outputs/feature-to-spec`](../../tool-skills/outputs/feature-to-spec/SKILL.md)** — authors
   the instruction itself (BRD/PRD or tech spec) as a deliverable at
   `export-files/<feature>-spec.md`: scope-faithful, WHAT-not-HOW, product decisions fixed, only
   technical forks open. `{#delivery}` names the file per handed-off feature.

## Register touchpoints
- **Hypotheses / Metrics** — each task links to the `H-…` it tests or the `M-…` it moves
  (a task that moves neither is a candidate to cut).
- **Features & surfaces** — each item names the `F-…` it advances; a new candidate mints a
  `planned` row (the specs declare the write, the orchestrator mints). A cut candidate stays a
  `planned` row — the backlog no longer dies between sprints. Shipped items are read at the next
  Step-5 gate (`impact-readout`), which flips `planned → live`.

## Gate checklist (soft) — each item ↔ artifact section
- [ ] a minimal must-set exists per direction → `sprint-plan#must`
- [ ] the rest is prioritized, not a flat list → `sprint-plan#backlog`
- [ ] dev items follow the **Feature** format; go-to-market items the **Activity** format; back-office items have a **DoD** → `sprint-plan#must` + `#backlog` · tick-id `item-format`
- [ ] every item links to a metric node or a hypothesis → `sprint-plan#must` + `#backlog` · tick-id `item-links`
- [ ] every must item names its `F-…` and pre-registers an Expected impact with a check-by → `sprint-plan#must` · tick-id `item-feature`
- [ ] cut candidates are shown with a reason, not silently dropped → `sprint-plan#excluded` · tick-id `rejects-shown`
- [ ] delivery to the dev process is explicit → `sprint-plan#delivery`

## Cadence & invalidation
- **Cadence:** every sprint (~1–2 wk).
- **Invalidates downward:** — (this is the bottom of the cascade; the delivery feeds the team's
  own development flow, which is outside the framework).
- **From below:** sprint outcomes feed results back up — shipped items are read against their
  pre-registered expectations at the next Step-5 gate (`impact-readout`); a refuted hypothesis or
  a missed expectation bubbles to the Tactical Plan (5), and further up if a strategic bet is
  affected.

## The human's role
Draw the must/backlog line and approve the sprint; the agent ranks by contribution to the gate
and prepares the delivery. Downstream, work proceeds in the team's own development flow.
