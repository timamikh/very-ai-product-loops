---
name: competitor-dynamics
kind: research
produces: competitor-dynamics
reads_registers: []
writes_registers: [risks]
inputs: [research, kb]
prerequisites: [competitor-list]
used_by_steps: [2]
opinionated: false
method_basis: "growth-dynamics per competitor from public sources — per-fact-type sourcing, as_of on every number, jurisdiction-neutral"
evidence_standard: external-sources
volume_rule: "one trend row per player in the {#competitors} detailed table (metric · trend · period · dated source), or an explicit '— to clarify —'"
selection_rule: "only numbers that survive the per-fact-type source test enter the table; sources consulted and failed go to the reject table with the reason"
rejects_shown: required
status: draft
version: 0.1.0
updated: 2026-08-16
---

# Competitor Dynamics

Capture how each competitor is **trending over time** (revenue, headcount, filings) so strategy
effectiveness can be compared — a static snapshot cannot say whose game is working. Fills
`{#competitor-dynamics}`.

**Method basis.** These are **external claims about other companies** — the place sourcing goes
wrong most often. Every number is judged *per fact type*, carries an `as_of`, and any number that
reaches a conclusion gets a second independent source. The rules live in
[`../references/evidence-standards.md`](../references/evidence-standards.md).

## When to apply

- Step 2, once the `{#competitors}` detailed table exists — the trend read runs over that list.
- When a competitor's visible move (funding, layoffs, a pivot) suggests the trend has turned.

## Prerequisites

- **Competitor list** — the detailed-table players from `competitor-analysis`. *Missing → run
  `competitor-analysis` first.*

## How to do it

1. **One trend row per detailed-table player.** Metric (revenue / headcount / …), the trend with
   its period, the source with its date. Nothing findable → `— to clarify —`, never a blank.
2. **Judge each source per fact type.** A company's own filing is authoritative for its own revenue
   and worthless for a rival's market share; a press release is a claim about the company's
   interest. Stay out of the forbidden zone in
   [`../references/evidence-standards.md`](../references/evidence-standards.md).
3. **Record `as_of` on every number.** A 2023 headcount is not evidence about this year's momentum.
4. **Second source before a conclusion.** Any figure a conclusion leans on gets an independent
   confirmation; single-sourced numbers stay flagged and go to the reject table if none is found.
5. **Stay jurisdiction-neutral.** Use public company registries, filings, and financial press
   appropriate to each company's jurisdiction. Region-specific registry integrations (a national
   business registry, a paid data provider) belong in a **regional/company adapter**, not the base
   framework.
6. **Seed the risk register.** A competitor accelerating into our segment is a threat → `R-…`.

## Anti-patterns

- **No dynamics.** A static snapshot with no trend — can't judge whose strategy is working.
- **Guessed financials.** Numbers with no source, stated as fact.
- **Cross-fact-type sourcing.** Taking a rival's share from the competitor's own deck.
- **Momentum from one point.** A single dated number narrated as a trend.

## Worklog & projection

The working is done in the step's **worklog** `<step-folder>/competitor-dynamics.md`
(`node_type: worklog`, e.g. `2-analysis/competitor-dynamics.md`): the trend read per player with
source + `as_of`, the sources consulted and rejected with reasons, and the seeded `R-…`. That
worklog is the **source of truth**; the artifact section `{#competitor-dynamics}` is its
**projection** into the fixed shape of [`template-fragment.md`](template-fragment.md), holding
nothing the worklog does not, and the step's change-log history lives in the worklog, not the
section (`process/CONVENTIONS.md` → *Step folders & worklogs*). External figures arrive here
dispatched from `sources/` by `source-intake`, cited in the worklog, never linked from the artifact.

## Output

Projects `{#competitor-dynamics}` via [`template-fragment.md`](template-fragment.md) from the
worklog; inputs via [`questions.yaml`](questions.yaml).
