---
name: competitor-analysis
kind: method
produces: [competitors, competitor-strategy, pricing, competitor-dynamics]
reads_registers: []
writes_registers: [risks, hypotheses]
inputs: [analytics-search, kb, interview]
prerequisites: [product-concept, competitor-list-seed]
used_by_steps: [2]
opinionated: false
method_basis: "'What game are they playing' + moat comparison; pricing scan; growth-dynamics from public registries"
status: draft
version: 0.1.0
updated: 2026-07-16
---

# Competitor Analysis

Map the competition and, crucially, **what game each competitor plays and how well it's
working**. Fills `{#competitors}`, `{#competitor-strategy}`, `{#pricing}`, `{#competitor-dynamics}`.

**Method basis.** For each competitor: the *game* they play (revenue / profit / market share /
social capital — and how), compared against our moats; their **pricing**; and their **development
dynamics** over time.

## When to apply
- Step 2, after framing the market.
- When a competitor's move changes the landscape.

## Prerequisites
- **Product concept** — to judge relevance and moat overlap. *Missing → run `concept-formation`.*
- **Competitor list seed** — at least a few names to start. *Missing → derive from analytics-search.*

## How to do it
1. **List** direct + indirect competitors (substitutes are a separate tool).
2. **Name each one's game** — are they chasing revenue, profit, share, or social capital, and by
   what strategy? Compare on the Step-1 moat axes (who has data / distribution / brand …).
3. **Pricing scan.** Capture each competitor's pricing where findable — the competitor's own
   site, or a web search (Google/Yandex). This orients our pricing and feeds the Step-4 financial
   model. Tag `[sourced: …]`; if not public, `— to clarify —`.
4. **Development dynamics.** Capture how each competitor is trending (revenue, headcount, filings)
   to compare strategy effectiveness. For RU legal entities, `datanewton.ru` exposes this — e.g.
   `https://datanewton.ru/contragents/<OGRN>` (the trailing number is the company OGRN; you can
   also search by INN or name). Treat as one regional source among others; for non-RU firms use
   the appropriate registry / public financials. Record source + date.
5. **Conclude** into `{#opportunity}` (the step's synthesis): where the white space / threat is.
6. **Seed registers.** Competitive threats → `R-…`; assumptions about a rival's move → `H-…`.

## Anti-patterns
- **Feature checklist.** Comparing feature grids instead of the game each plays and why.
- **No dynamics.** A static snapshot with no trend — can't judge whose strategy is working.
- **Guessed pricing/financials.** Numbers with no source, stated as fact.

## Output
Fills the four sections via [`template-fragment.md`](template-fragment.md); inputs via
[`questions.yaml`](questions.yaml).
