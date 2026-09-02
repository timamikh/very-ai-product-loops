---
node_type: card
kind: method
name: competitor-dynamics
steps: [2]
prerequisites: [competitor-list]
reads: [section:competitors, register:risks, source:research, source:kb]
writes: [worklog, section:competitor-dynamics, register:risks]
opinionated: false
method_basis: "growth-dynamics per competitor from public sources — per-fact-type sourcing, as_of on every number, jurisdiction-neutral"
evidence_standard: external-sources
volume_rule: "one trend row per player in the {#competitors} detailed table (metric · trend · period · dated source), or an explicit '— to clarify —'"
selection_rule: "only numbers that survive the per-fact-type source test enter the table; ≤2 sources tried per player — if neither lands, '— to clarify —' naming the proxy that would settle it; single-sourced rows stay, labelled; sources consulted and failed go to the reject table with the reason"
rejects_shown: required
status: draft
version: 0.2.2
updated: 2026-09-02
---
# Competitor Dynamics

Capture how each competitor is **trending over time** (revenue, headcount, filings) so strategy
effectiveness can be compared — a static snapshot cannot say whose game is working. Fills
`{#competitor-dynamics}`.

**Method basis.** External claims about other companies — where sourcing goes wrong most often.
The rules live in [`../references/evidence-standards.md`](../references/evidence-standards.md).

## When to apply

- Step 2, once the `{#competitors}` detailed table exists — the trend read runs over that list.
- When a competitor's visible move (funding, layoffs, a pivot) suggests the trend has turned.

## Prerequisites

- **Competitor list** — the detailed-table players from `competitor-analysis`. *Missing → run
  `competitor-analysis` first.*

## How to do it

1. **One trend row per detailed-table player.** Metric (revenue / headcount / …), the trend with
   its period, the source with its date. Nothing findable → `— to clarify —`, never a blank.
2. **Walk the proxy ladder for private firms**, top down: registry filings / headcount · job-posting
   count · funding rounds · app-store review velocity · pricing-page history via a web archive.
   **Stop rule: at most two sources tried per player.** If neither lands, write `— to clarify —`
   naming the proxy that would settle it; the worklog records the rungs tried per player.
3. **Judge each source per fact type.** A company's own filing is authoritative for its own revenue
   and worthless for a rival's market share; a press release is a claim about the company's
   interest. Stay out of the forbidden zone in
   [`../references/evidence-standards.md`](../references/evidence-standards.md).
4. **Record `as_of` on every number.** A 2023 headcount is not evidence about this year's momentum.
5. **Second source before a conclusion.** Any figure a conclusion leans on gets an independent
   confirmation; a single-sourced row **stays in the table, labelled single-sourced** — it may not
   carry a conclusion on its own.
6. **Stay jurisdiction-neutral.** Registries, filings and press fit each company's jurisdiction;
   a region-specific registry integration or paid data provider belongs in a **regional/company
   adapter**, not the base framework.
7. **Seed the risk register.** A competitor accelerating into our segment is a threat → `R-…`.

## Anti-patterns

- **No dynamics.** A static snapshot with no trend — can't judge whose strategy is working.
- **Guessed financials.** Numbers with no source, stated as fact.
- **Cross-fact-type sourcing.** Taking a rival's share from the competitor's own deck.
- **Momentum from one point.** A single dated number narrated as a trend.

## Worklog & projection
Worklog: `2-analysis/competitor-dynamics.md` — the trend per player with source and `as_of`, the proxy rungs tried per player, the single-sourced labels, the sources rejected with reasons, the seeded `R-…`. Projects `{#competitor-dynamics}`; face: the **Momentum read** line, via [`template-fragment.md`](template-fragment.md). Path form, primary/contributing and revisit rules: [`worklog-resolution.md`](../../../process/reference/worklog-resolution.md).

## Output

Projects `{#competitor-dynamics}` via [`template-fragment.md`](template-fragment.md) from the
worklog; inputs via [`questions.yaml`](questions.yaml).
