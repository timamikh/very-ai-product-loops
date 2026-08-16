---
node_type: artifact-template
artifact: sprint-plan
step: 6
title: "Sprint Plan — <Product> · Sprint <n> (<dates>)"
status: template
version: 0.3.0
updated: 2026-08-16
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
> Inputs: `5-tactical-plan.md` · registers. Hands off to: the team's development process.

> ⚠️ **Fill each section through its method — not from this shell.** Every `{#section}` names its
> library method in a `<!-- tool: … -->` note: open that method's `SKILL.md` under
> `tool-skills/library/`, check its prerequisites, clarify real forks as options, then fill. Filling
> straight from this template bypasses the method (see the repo's agent rules `AGENTS.md` → "Read the tool before filling").
> The shell is for structure and stable IDs only.

## Sprint goal {#sprint-goal}
<!-- synthesis -->
_One or two lines: what this sprint must prove or move — ties to the period gate and the status's
learning goal._

- …

## Must {#must}
_Minimal mandatory items — without which the period goal is unreachable. Grouped by direction._

### Development — Features
<!-- tool: feature-spec, prioritization-sprint-plan -->
**F-1 · <feature name>** — links: `H-…` / `M-…`
- **Description:** what the feature is
- **Scope:** the tasks to implement it
- **Acceptance criteria:** binary, checkable — how we know it's done (each answerable yes/no)
- **Business value:** value to the business
- **User value:** value to the user
- **User stories:** (if applicable)
- **Owner:** who is accountable for it landing
- **Estimate:** the capacity it consumes

### Go-to-market — Activities
<!-- tool: activity-spec, prioritization-sprint-plan -->
**A-1 · <activity name>** — links: `H-…` it tests / `M-…` it moves
- **Description:** what the activity is
- **Scope:** the steps to run it
- **Business value:** the metric/hypothesis it moves
- **Audience value:** why the audience cares
- **Owner:** who is accountable for it landing
- **Estimate:** the capacity it consumes

### Back-office — Tasks
<!-- tool: task-spec, prioritization-sprint-plan -->
**T-1 · <task name>** — links: `M-…` / `R-…` / `H-…`
- **Description:** what needs doing
- **Why:** the business reason (the `M-…` it moves / `R-…` it mitigates / `H-…` it serves)
- **Definition of Done:** binary — answerable yes/no at sprint end
- **Owner:** who is accountable for it landing
- **Estimate:** the capacity it consumes

## Backlog {#backlog}
<!-- tool: prioritization-sprint-plan -->
_The rest, prioritized (not a flat list), grouped by direction. Same item formats as above._

| Rank <!--c:rank--> | Direction <!--c:direction--> | Item <!--c:item--> | Format <!--c:format--> | Links (`H-…`/`M-…`) <!--c:links--> | Est. <!--c:est--> | Confidence <!--c:conf--> |
|------|-----------|------|--------|---------------------|------|------------|
| 1 | development | … | Feature | H-… / M-… | … | [assumption] |
| 2 | go-to-market | … | Activity | H-… / M-… | … | [assumption] |
| 3 | back-office | … | Task+DoD | M-… / R-… | … | [assumption] |

## Excluded {#excluded}
<!-- tool: prioritization-sprint-plan -->
_Candidates that entered the ranking (N = …) but left it entirely — cut before backlog, shown with why (a rejected item is not silently dropped). Backlog is the visible reject of the must-set; this is the reject of the ranking itself._

| Item <!--c:item--> | Direction <!--c:direction--> | Why excluded <!--c:why--> |
|------|-----------|--------------|
| … | … | no `M-…`/`H-…` link · out of period scope · superseded by <item> |

## Delivery {#delivery}
<!-- synthesis -->
_What goes to the development process, and how (the framework ends here; work proceeds in the team's own flow)._

- Handed off: … (which items, to which board/process)
- Acceptance / how results flow back: … (a refuted `H-…` or missed `M-…` bubbles up to `5-tactical-plan.md`)

## To clarify {#to-clarify}
<!-- open -->
_Unresolved sprint questions; resolved by deleting the line._

- …

## Change log

### <date> — created
- **From → To:** — → initial sprint-plan draft for Sprint <n>
- **Why:** …
- **Trigger:** …
