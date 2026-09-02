---
node_type: artifact-template
artifact: sprint-plan
step: 6
title: "Sprint Plan — <Product> · Sprint <n> (<dates>)"
status: template
version: 0.5.0
updated: 2026-08-23
---

<!--
  6-sprint-plan.md assembly shell. Filled per steps/6-sprint-plan/README.md. Keep section IDs stable.
  Follow process/CONVENTIONS.md. Items are grouped by DIRECTION, each in its own format
  (dev = Feature · go-to-market = Activity · back-office = Task+DoD). Items are numbered 1, 2, 3
  within their direction subsection — sprint-local, no letters: the cross-sprint identity is the
  feature register's F-…, which every item names in its Feature line. The minimal level of detail
  is one feature/activity/task — not sub-tasks. Every item pre-registers its Expected impact
  (the M-… it moves / R-… it closes / H-… it tests, with a check-by) — read at the next Step-5
  gate by impact-readout; an activity that runs a Step-5 market-entry bundle also names its B-….
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
<!-- rests-on: 5#period-goals -->
_One or two lines: what this sprint must prove or move — ties to the period gate and the status's
learning goal._

- …

## Must {#must}
<!-- rests-on: 5#period-goals, 5#hypotheses-to-test -->
_Minimal mandatory items — without which the period goal is unreachable. Grouped by direction._

### Development — Features
<!-- tool: feature-spec, prioritization-sprint-plan, feature-grooming -->
**1 · <feature name>** — links: `H-…` / `M-…`
- **Feature:** `F-…` (the register row this item advances; a new candidate mints a `planned` row)
- **Description:** what the feature is
- **Scope:** the tasks to implement it
- **Acceptance criteria:** binary, checkable — how we know it's done (each answerable yes/no)
- **Business value:** value to the business
- **User value:** value to the user
- **User stories:** (if applicable)
- **Expected impact:** `M-…` <baseline → expected> / closes `R-…` / tests `H-…` · check-by <sprint/date> [assumption]
- **Owner:** who is accountable for it landing
- **Estimate:** class S/M/L + range — [assumption] until the readout reads the actual
- **Groom:** spec-ready | blocked: <fork> — `6-sprint-plan/feature-grooming.md` (when groomed;
  the spec itself is authored by `outputs/feature-to-spec` into `export-files/<feature>-spec.md`)

### Go-to-market — Activities
<!-- tool: activity-spec, prioritization-sprint-plan -->
**1 · <activity name>** — links: `H-…` it tests / `M-…` it moves / `B-…` it launches
- **Feature:** `F-…` (the campaign/content line it advances; the shipped artifact's external id — a post, a mailing — lands here after the run)
- **Description:** what the activity is
- **Scope:** the steps to run it
- **Business value:** the metric/hypothesis it moves
- **Audience value:** why the audience cares
- **Surface:** `S-…` it runs on
- **Expected impact:** `M-…` <baseline → expected> / tests `H-…` · check-by <sprint/date> [assumption]
- **Owner:** who is accountable for it landing
- **Estimate:** class S/M/L + range — [assumption] until the readout reads the actual

### Back-office — Tasks
<!-- tool: task-spec, prioritization-sprint-plan -->
**1 · <task name>** — links: `M-…` / `R-…` / `H-…`
- **Feature:** `F-…` (the capability it advances; `— to clarify —` for a one-off with no lasting row)
- **Description:** what needs doing
- **Why:** the business reason (the `M-…` it moves / `R-…` it mitigates / `H-…` it serves)
- **Definition of Done:** binary — answerable yes/no at sprint end
- **Expected impact:** `M-…` <baseline → expected> / `R-…` → <status> · check-by <sprint/date> [assumption]
- **Owner:** who is accountable for it landing
- **Estimate:** class S/M/L + range — [assumption] until the readout reads the actual

## Backlog {#backlog}
<!-- tool: prioritization-sprint-plan, feature-spec, activity-spec, task-spec, feature-grooming -->
_The rest, prioritized (not a flat list), grouped by direction. Same item formats as above._

| Rank <!--c:rank--> | Direction <!--c:direction--> | Item <!--c:item--> | Format <!--c:format--> | Feature <!--c:feature--> | Links (`H-…`/`M-…`/`B-…`) <!--c:links--> | Est. <!--c:est--> | Confidence <!--c:conf--> |
|------|-----------|------|--------|---------|---------------------|------|------------|
| 1 | development | … | Feature | F-… | H-… / M-… | … | [assumption] |
| 2 | go-to-market | … | Activity | F-… | H-… / B-… | … | [assumption] |
| 3 | back-office | … | Task+DoD | F-… | M-… / R-… | … | [assumption] |

## Excluded {#excluded}
<!-- tool: prioritization-sprint-plan -->
_Candidates that entered the ranking (N = …) but left it entirely — cut before backlog, shown with why (a rejected item is not silently dropped). Backlog is the visible reject of the must-set; this is the reject of the ranking itself._

| Item <!--c:item--> | Direction <!--c:direction--> | Why excluded <!--c:why--> |
|------|-----------|--------------|
| … | … | no `M-…`/`H-…` link · out of period scope · superseded by <item> |

## Delivery {#delivery}
<!-- synthesis -->
_What goes to the development process, and how (the framework ends here; work proceeds in the team's own flow)._

- Handed off: … (which items, to which board/process; a groomed feature hands off as its written
  instruction — `export-files/<feature>-spec.md`, authored by `outputs/feature-to-spec`)
- Acceptance / how results flow back: … (shipped items are read at the next Step-5 gate by
  `impact-readout` against their pre-registered Expected impact — `F-…` rows flip `planned → live`;
  a refuted `H-…` or missed expectation bubbles up to `5-tactical-plan.md`)

## To clarify {#to-clarify}
<!-- open -->
_Unresolved sprint questions; resolved by deleting the line._

- … — *the human chooses* · *nobody knows yet* · *a later step owns it* (name the step):
  keep exactly one (`process/CONVENTIONS.md` → the `open` bullet)

## Change log

### <date> — created
- **From → To:** — → initial sprint-plan draft for Sprint <n>
- **Why:** …
- **Trigger:** …
