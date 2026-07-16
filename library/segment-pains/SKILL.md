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
method_basis: "Jobs-to-be-Done + Value Proposition Canvas (jobs/pains/gains), scored by severity × frequency, classified differentiator vs table-stakes"
status: draft
version: 0.1.0
updated: 2026-07-16
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
  source to lean on. *Missing → offer `interview` / `analytics-search`.*

## How to do it

1. **State the job.** For the lead segment, what are they really trying to get done (the JTBD)?
   Pains are obstacles to *that job*, not generic complaints.
2. **List pains,** each scored **severity** (how much it hurts) × **frequency** (how often).
   Lead with high×high.
3. **Classify each pain: `differentiator` or `table-stakes`.** Table-stakes must be met but
   won't win anyone; differentiators are where you actually compete. (This distinction is why a
   pain can also be a baseline requirement baked into the concept.)
4. **Tag confidence & source.** `[sourced: metrics …]` / `[sourced: interview …]` / `[assumption]`.
5. **Seed hypotheses.** Each unproven pain → `H-…` with `type: desirability` (does this pain
   exist and matter enough).

## Anti-patterns

- **Feature-in-disguise.** "They need our button" is a solution, not a pain.
- **Unranked list.** Every pain equal → no focus. Score and order.
- **Table-stakes as the pitch.** Leading on a pain everyone already solves.
- **Guessed severity.** Numbers with no source, tagged as fact.

## Output

Fills `{#problems}` via [`template-fragment.md`](template-fragment.md); inputs via
[`questions.yaml`](questions.yaml).
