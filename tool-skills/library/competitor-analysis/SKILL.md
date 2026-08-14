---
name: competitor-analysis
kind: method
produces: [competitors, competitor-strategy, competitor-pricing, competitor-dynamics]
reads_registers: []
writes_registers: [risks, hypotheses]
inputs: [analytics-search, kb, interview]
prerequisites: [product-concept, competitor-list-seed]
used_by_steps: [2]
opinionated: false
method_basis: "'What game are they playing' + moat comparison; pricing scan; growth-dynamics from public registries"
evidence_standard: external-sources
volume_rule: "≥5 named players, including ≥1 the team did not name first (registry/search/app-store sweep)"
selection_rule: "the players sharing our segment AND our job enter the detailed table; the rest are listed and excluded"
rejects_shown: required
status: draft
version: 0.1.6
updated: 2026-08-09
---

# Competitor Analysis

Map the competition and, crucially, **what game each competitor plays and how well it's
working**. Fills `{#competitors}`, `{#competitor-strategy}`, `{#competitor-pricing}`, `{#competitor-dynamics}`.

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
1. **List** direct + indirect competitors (substitutes are a separate tool). **At least 5 named
   players, of which at least one is a player the team did not name first** — found by a registry,
   search, app-store or community sweep, not from memory. The failure this prevents is the two-rival
   analysis: the incumbents everyone already worries about get studied, and the entrant that actually
   takes the segment is not on the page. Then say which players enter the detailed table (they share
   our segment **and** our job) and **list the ones excluded with the reason** — an excluded player
   with no reason is indistinguishable from one nobody thought of.
2. **Name each one's game** — are they chasing revenue, profit, share, or social capital, and by
   what strategy? Compare on the Step-1 moat axes (who has data / distribution / brand …).
3. **Competitor pricing scan.** Capture each competitor's pricing where findable — the
   competitor's own site, or a web search. Record the **date you read it**: published pricing is the
   fastest-ageing fact in this table, and an undated price is a claim about an unknown month. This is an **input** to our own pricing
   decision (the `pricing` tool at Step 3) and feeds the Step-4 financial model — it is not our
   price. Tag `[sourced: …]`; if not public, `— to clarify —`.
4. **Development dynamics.** Capture how each competitor is trending (revenue, headcount, filings)
   to compare strategy effectiveness. These are **external claims about other companies**, which is
   where sourcing goes wrong most often: judge each source *per fact type* — a company's own filing is
   authoritative for its own revenue and worthless for a rival's share — stay out of the forbidden
   zone, record `as_of`, and give any number that reaches a conclusion a second independent source
   before you draw it. The rules are in
   [`../references/evidence-standards.md`](../references/evidence-standards.md). Use public company registries, filings, and financial press
   appropriate to the company's jurisdiction. Region-specific registry integrations (a national
   business registry, a paid data provider) belong in a **regional/company adapter**, not the base
   framework — keep this tool jurisdiction-neutral. Record source + date.
5. **Conclude** into `{#opportunity}` (the step's synthesis): where the white space / threat is.
6. **Seed registers.** Competitive threats → `R-…`; assumptions about a rival's move → `H-…`.

## Anti-patterns
- **Feature checklist.** Comparing feature grids instead of the game each plays and why.
- **No dynamics.** A static snapshot with no trend — can't judge whose strategy is working.
- **Guessed pricing/financials.** Numbers with no source, stated as fact.

## Worklog & projection
The working is done in the step's **worklog** `<step-folder>/competitor-analysis.md`
(`node_type: worklog`, e.g. `2-analysis/competitor-analysis.md`): the competitor list (≥5 named,
including one the team did not name first), the excluded players each with its reason, each player's
*game* and moat comparison, the dated pricing scan, the development-dynamics with source + `as_of`,
and the white-space / threat conclusion. This method keeps **one** worklog, and all four sections
`{#competitors}`, `{#competitor-strategy}`, `{#competitor-pricing}`, `{#competitor-dynamics}` are its
**projections** into the fixed shape of [`template-fragment.md`](template-fragment.md) — the worklog is
the **source of truth**, the sections hold nothing it does not, and the step's change-log history lives
in the worklog, not the sections (`process/CONVENTIONS.md` → *Step folders & worklogs*). External
figures arrive here dispatched from `sources/` by `source-intake`, cited in the worklog, never linked
from the artifact.

## Output
Projects `{#competitors}`, `{#competitor-strategy}`, `{#competitor-pricing}`, `{#competitor-dynamics}`
via [`template-fragment.md`](template-fragment.md) from the single worklog; inputs via
[`questions.yaml`](questions.yaml).
