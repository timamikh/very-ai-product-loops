---
name: analytics-search
kind: research
produces: product/sources/<topic>-research.md
prerequisites: [the market/arena to research, the questions the research must answer]
reads_registers: []
writes_registers: [hypotheses, risks]
inputs: [kb]
used_by_steps: [1, 2, 4]
opinionated: false
method_basis: "Triangulated desk research — analyst reviews · articles · indicators/statistics · named-expert opinion; multiple independent sources per claim"
evidence_standard: external-sources
volume_rule: "≥2 independent sources per load-bearing claim; ≥3 for any number that reaches a conclusion"
selection_rule: "prefer primary over secondary per fact type; on >20% divergence report both as [CONFLICT], never average"
rejects_shown: required
status: draft
version: 0.1.1
updated: 2026-08-09
---

# Market Research (desk research)

Run a **desk-research pass** and distil a **sourced market digest**: pull analyst reviews,
articles, official indicators, and named-expert opinion, and turn them into a dated, sourced read
of **market size · dynamics · trends · barriers · risks & drivers · main players**. Produced as a
dated, sourced **digest file** in `product/sources/` (indexed in `sources/INDEX.md`), not an
artifact section.

**Method basis.** Triangulated desk research: every claim rests on **multiple independent
sources**, prefer primary over secondary, and each number carries a **source and a date** so its
freshness and bias can be judged.

**Relation to neighbours (one mechanism, one way).** This tool **gathers and distils**; the
rigorous *structuring* is downstream. `market-sizing` turns size signals into a bottom-up
TAM/SAM/SOM; `competitor-analysis` turns the player list into the game/pricing/dynamics table;
`substitutes` covers non-obvious competition; `risk-mitigation` triages the barriers/risks. Don't
compute the final TAM or build the competitor table here — produce the sourced raw material they
consume. It fills the `analytics-search` **input slot** those tools list.

## When to apply
- **Step 2**, the gathering front-end for the whole analysis (feeds sizing, competitors, substitutes, risks).
- **Step 1**, to sanity-check that a market and a problem plausibly exist before going deep.
- **Step 4**, to source an external benchmark a financial-model assumption rests on.

## Prerequisites
- **The market/arena to research** — the scope of the search. *Missing → run `segmentation` /
  `where-to-play-how-to-win` to bound the arena first.*
- **The questions the research must answer** — size? a trend? a barrier? *Missing → an open-ended
  "research the market" returns noise; name the questions first.*

## How to do it
1. **Fix the questions.** What must this research answer — the size, a specific trend, a barrier?
   Scope the search before opening a tab.
2. **Cast a triangulated net.** Analyst/industry reviews, articles, official indicators and
   statistics, and named-expert opinion. Prefer primary sources and several independent ones.
3. **Distil into the digest buckets.** Size signals · dynamics (growth/decline) · trends ·
   barriers to entry · risks & drivers · main players. Every claim carries a source and a date.
4. **Triangulate every number.** One source → `[assumption]`; two independent sources →
   `[sourced]`. Surface conflicts, don't average them into a false middle.
5. **Flag freshness.** Mark stale data — a three-year-old market size can mislead pricing. Prefer
   the most recent credible read.
6. **Hand off and seed registers.** Size signals → `market-sizing`; players → `competitor-analysis`;
   barriers/risks/drivers → risk register (`R-…`) and hypotheses (`H-…`). The digest lives in
   `product/sources/`, indexed in `sources/INDEX.md`.

## Anti-patterns
- **One source stated as fact.** No triangulation, so one stale or biased number drives strategy.
- **Scope creep into structuring.** Computing the TAM or the competitor table here instead of
  feeding `market-sizing` / `competitor-analysis`.
- **Undated evidence.** A number with no date can't be judged for staleness.
- **Averaging conflicting sources.** Hiding a real disagreement instead of surfacing it.
- **"Research the market" with no question.** A pile of links that answers nothing.

## Output
Produced from [`template-fragment.md`](template-fragment.md) as a digest file in `product/sources/`;
inputs via [`questions.yaml`](questions.yaml). The digest lives in `product/sources/` (indexed in
`sources/INDEX.md`) and feeds `market-sizing`, `competitor-analysis`, `substitutes`,
`risk-mitigation`; seeds the hypotheses and risk registers.
