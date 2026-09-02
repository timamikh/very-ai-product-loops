---
node_type: card
kind: method
name: competitor-analysis
steps: [2]
prerequisites: [product-concept, competitor-list-seed]
reads: [section:idea, section:segments, section:market-sizing, register:risks, register:hypotheses, source:research, source:kb]
writes: [worklog, section:competitors, section:competitor-strategy, register:risks, register:hypotheses]
opinionated: false
method_basis: "'What game are they playing' + moat comparison (pricing scan and growth-dynamics are separate methods)"
evidence_standard: external-sources
volume_rule: "≥5 named players, including ≥1 the team did not name first; one bounded sweep per channel type (registry · app store · search · community), stopped when the last three finds are already listed or fail segment ∧ job"
selection_rule: "the players sharing our segment AND our job enter the detailed table; the rest are listed and excluded"
rejects_shown: required
status: draft
version: 0.3.2
updated: 2026-09-02
---
# Competitor Analysis

Map the competition and, crucially, **what game each competitor plays and how well it's
working**. Fills `{#competitors}` and `{#competitor-strategy}`. Two follow-on scans run over the
same competitor list as separate methods: the dated pricing scan is
[`competitor-pricing`](../competitor-pricing/SKILL.md), the development dynamics is
[`competitor-dynamics`](../competitor-dynamics/SKILL.md).

**Method basis.** For each competitor: the *game* they play (revenue / profit / market share /
social capital — and how), compared against our moats.

## When to apply
- Step 2, after framing the market.
- When a competitor's move changes the landscape.

## Prerequisites
- **Product concept** — to judge relevance and moat overlap. *Missing → run `concept-formation`.*
- **The sized arena** — `{#market-sizing}`'s SAM cut names *where* to sweep for players; a list
  drawn without it hunts in a market nobody sized. *Missing → run `market-sizing` first; it comes
  earlier in this step.*
- **Competitor list seed** — at least a few names to start. *Missing → gather it yourself: a scoped
  desk-research pass (a `loops-research` brief), discipline per
  [`../references/evidence-standards.md`](../references/evidence-standards.md), findings landing in
  this method's worklog.*

## How to do it
1. **List** direct + indirect competitors (substitutes are a separate tool). **At least 5 named
   players, of which at least one is a player the team did not name first** — found by a sweep, not
   from memory. **Bound the sweep: one pass per channel type** — one registry, one app store, one
   search, one community — and **stop when the last three finds are already listed or fail
   segment ∧ job**; record in the worklog where each sweep stopped. Then say which players enter the
   detailed table (they share our segment **and** our job) and **list the ones excluded with the
   reason** — an excluded player with no reason is indistinguishable from one nobody thought of.
2. **Name each one's game** — are they chasing revenue, profit, share, or social capital, and by
   what strategy? Read it from **observable moves**, recorded beside the game in the worklog:
   share → free tier, land-grab discounting · revenue → upsell, tier proliferation · profit → price
   rises, feature cuts · social capital → OSS, community, thought leadership. Compare on the Step-1
   moat axes.
3. **Hand the list on.** The detailed-table players are the input to the two scans:
   [`competitor-pricing`](../competitor-pricing/SKILL.md) (dated pricing, feeds `market-sizing`'s
   price input, Step-3 `pricing-strategy`, and the Step-4 financial model) and
   [`competitor-dynamics`](../competitor-dynamics/SKILL.md) (trend per player from public sources).
4. **Conclude** into `{#opportunity}` (the step's synthesis): where the white space / threat is.
5. **Seed registers.** Competitive threats → `R-…`; assumptions about a rival's move → `H-…`.

## Anti-patterns
- **Feature checklist.** Comparing feature grids instead of the game each plays and why.
- **The two-rival analysis.** Studying only the incumbents everyone already worries about; the
  entrant that takes the segment is not on the page.
- **A game with no evidence.** Asserting what a competitor is chasing without a move that shows it.

## Worklog & projection
Worklog: `2-analysis/competitor-analysis.md` — one worklog for two sections: the ≥5 players with the excluded ones and why, where each sweep stopped, each player's game with the move that shows it and the moat comparison, the white-space / threat read. Projects `{#competitors}` (face: **Field read**) and `{#competitor-strategy}` (face: **Strategy read**) via [`template-fragment.md`](template-fragment.md). Path form, primary/contributing and revisit rules: [`worklog-resolution.md`](../../../process/reference/worklog-resolution.md).

## Output
Projects `{#competitors}` and `{#competitor-strategy}` via
[`template-fragment.md`](template-fragment.md) from the single worklog; inputs via
[`questions.yaml`](questions.yaml).
