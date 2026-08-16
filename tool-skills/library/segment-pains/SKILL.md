---
name: segment-pains
kind: method
produces: problems
reads_registers: []
writes_registers: [hypotheses]
inputs: [interview, metrics, kb]
prerequisites: [segments, evidence-source]
used_by_steps: [1]
opinionated: false
method_basis: "Jobs-to-be-Done + Value Proposition Canvas (jobs/pains/gains), scored by severity × frequency, cost of inaction named per pain, classified differentiator vs table-stakes"
evidence_standard: primary-research
volume_rule: "≥5 candidate pains per segment before any is ranked"
selection_rule: "severity × frequency; differentiator vs table-stakes; the top 3 carry forward, the rest stay ranked in the table"
rejects_shown: required
status: draft
version: 0.2.1
updated: 2026-08-16
---

# Segment Pains

Surface the **problems** each segment has — the jobs they're trying to get done and where those
jobs hurt. Fills `{#problems}`. Good problems are the bridge from *who* (segments) to *how*
(solution): get them wrong and the solution solves nothing.

**Method basis.** Jobs-to-be-Done + the Value Proposition Canvas (jobs → pains → gains). Each
pain is scored **severity × frequency** and classified **differentiator vs table-stakes**.

## When to apply

- Step 1, after segments — for the lead segment first.
- Whenever usage data or interviews reveal a pain you were not solving for.

## Prerequisites

- **Segments** — from `{#segments}`. *Missing → run `segmentation` first.*
- **Evidence source** — interviews (early stages) and/or product metrics (later stages). At
  `concept-viability` these are thin, so pains stay `[assumption]`; the status tells you which
  source to lean on. *Missing → offer `interview` (prep the guide) or a scoped desk-research pass
  (`loops-research` brief per `references/evidence-standards.md`).*

## How to do it

1. **State the job.** For the lead segment, what are they really trying to get done (the JTBD)?
   Pains are obstacles to *that job*, not generic complaints.
2. **List at least 5 candidate pains per segment, then score** each on **severity** (how much it
   hurts) × **frequency** (how often). Lead with high×high. Five is the floor because two or three
   pains are always the ones the team already talks about — the ranking has nothing to do and the
   result is the starting opinion with a table around it. **The top 3 carry forward** into the CVP
   and the bundle; the rest stay in the table with their rank, never deleted — a pain ranked low this
   quarter is the cheapest thing to re-check next quarter, and the most expensive to re-derive.
3. **Name the cost of inaction per pain** — what the segment does about it today:
   `nice-to-have` / `recurring irritation` / `already paying or improvising`. This is the same
   gradation `hypothesis-test-design` §Scales uses for pain acuteness, so the column feeds the
   Step-3 CVP (`uvp-cpv`) and the Step-5 priority score without translation. Severity says how much
   it hurts; cost of inaction says what they *do* about it — a vivid pain nobody pays or improvises
   around sells nothing, and it is cheaper to learn that here than at Step 5.
4. **Classify each pain: `differentiator` or `table-stakes`.** Table-stakes must be met but
   won't win anyone; differentiators are where you actually compete. (This distinction is why a
   pain can also be a baseline requirement baked into the concept.)
5. **Tag confidence & source — and say what the evidence actually was.** `[sourced: metrics …]` /
   `[sourced: interview …]` / `[assumption]`. For an interview-sourced pain, name **how many people**
   and **who** (the sample and its bias: five power users is not five customers), and prefer evidence
   of **past behaviour** — what they did, paid for, or built around — over what they said would be
   nice. A stated complaint with no behaviour behind it is `[assumption]`, however vivid the quote.
6. **Seed hypotheses.** Each unproven pain → `H-…` with `type: desirability` (does this pain
   exist and matter enough).

## Anti-patterns

- **Feature-in-disguise.** "They need our button" is a solution, not a pain.
- **Unranked list.** Every pain equal → no focus. Score and order.
- **Table-stakes as the pitch.** Leading on a pain everyone already solves.
- **Guessed severity.** Numbers with no source, tagged as fact.

## Worklog & projection

The working is done in the step's **worklog** `<step-folder>/segment-pains.md` (`node_type: worklog`,
e.g. `1-concept/segment-pains.md`): the stated job, the ≥5 candidate pains per segment each scored
**severity × frequency**, its **cost of inaction** (nice-to-have / recurring irritation / already
paying or improvising) and classified **differentiator vs table-stakes**, and the ranking — the top
3 carried forward, the rest kept in the table with their rank. That worklog is the **source of
truth**; the artifact section `{#problems}` is its **projection** into the fixed shape of
[`template-fragment.md`](template-fragment.md) — it holds nothing the worklog does not, and the step's
change-log history lives in the worklog, not the section
(`process/CONVENTIONS.md` → *Step folders & worklogs*). External inputs arrive here dispatched from
`sources/` by `source-intake`, cited in the worklog, never linked from the artifact.

## Output

Projects `{#problems}` via [`template-fragment.md`](template-fragment.md) from the worklog; inputs via
[`questions.yaml`](questions.yaml).
