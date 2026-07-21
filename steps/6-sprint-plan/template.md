---
node_type: artifact-template
artifact: sprint-plan
step: 6
title: "Sprint Plan — <Product> · Sprint <n> (<dates>)"
status: template
version: 0.2.0
updated: 2026-07-20
---

<!--
  6-sprint-plan.md assembly shell. Filled per steps/6-sprint-plan/README.md. Keep section IDs stable.
  Follow process/CONVENTIONS.md. Items are grouped by DIRECTION, each in its own format
  (dev = Feature · go-to-market = Activity · back-office = Task+DoD). The minimal level of detail
  is one feature/activity/task — not sub-tasks. Every item links to an H-… or M-….
  ⚙️ marks agent-proposed defaults awaiting human approval.
-->

# Sprint Plan — <Product> · Sprint <n> (<dates>)

> Status: <concept-viability | pmf | growth> · Owner: <name> · Capacity: <n features / n activities / …>
> Inputs: [[tactical-plan]] · registers. Hands off to: the team's development process.

> ⚠️ **Fill each section through its method — not from this shell.** Every `{#section}` names its
> library method in a `<!-- tool: … -->` note: open that method's `SKILL.md` under
> `tool-skills/library/`, check its prerequisites, clarify real forks as options, then fill. Filling
> straight from this template bypasses the method (see `CLAUDE.md` → "Read the tool before filling").
> The shell is for structure and stable IDs only.

## Must {#must}
_Minimal mandatory items — without which the period goal is unreachable. Grouped by direction._

### Development — Features
<!-- tool: feature-spec, prioritization -->
**F-1 · <feature name>** — links: `H-…` / `M-…`
- **Description:** what the feature is
- **Scope:** the tasks to implement it
- **Business value:** value to the business
- **User value:** value to the user
- **User stories:** (if applicable)

### Go-to-market — Activities
<!-- tool: activity-spec, prioritization -->
**A-1 · <activity name>** — links: `H-…` it tests / `M-…` it moves
- **Description:** what the activity is
- **Scope:** the steps to run it
- **Business value:** the metric/hypothesis it moves
- **Audience value:** why the audience cares

### Back-office — Tasks
<!-- tool: prioritization -->
**T-1 · <task name>** — links: `M-…` / `R-…`
- **Description:** what needs doing
- **Definition of Done:** the concrete DoD
- **Why:** the business reason

## Backlog {#backlog}
_The rest, prioritized (not a flat list), grouped by direction. Same item formats as above._

| Rank | Direction | Item | Format | Links (`H-…`/`M-…`) | Est. | Confidence |
|------|-----------|------|--------|---------------------|------|------------|
| 1 | development | … | Feature | H-… / M-… | … | [assumption] |
| 2 | go-to-market | … | Activity | H-… / M-… | … | [assumption] |
| 3 | back-office | … | Task+DoD | M-… / R-… | … | [assumption] |

## Handoff {#handoff}
_What goes to the development process, and how (the framework ends here; work proceeds in the team's own flow)._

- Handed off: … (which items, to which board/process)
- Acceptance / how results flow back: … (a refuted `H-…` or missed `M-…` bubbles up to [[tactical-plan]])

## Change log

### <date> — created
- **From → To:** — → initial sprint-plan draft for Sprint <n>
- **Why:** …
- **Trigger:** …
