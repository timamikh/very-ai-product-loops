---
node_type: card
kind: method
name: competitor-analysis
steps: [2]
prerequisites: [product-concept, competitor-list-seed]
reads: [source:research, source:kb, source:interview]
writes: [worklog, section:competitors, section:competitor-strategy, register:risks, register:hypotheses]
opinionated: false
method_basis: "'What game are they playing' + moat comparison (pricing scan and growth-dynamics are separate methods)"
evidence_standard: external-sources
volume_rule: "≥5 named players, including ≥1 the team did not name first (registry/search/app-store sweep)"
selection_rule: "the players sharing our segment AND our job enter the detailed table; the rest are listed and excluded"
rejects_shown: required
status: draft
version: 0.2.1
updated: 2026-08-16
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
- **Competitor list seed** — at least a few names to start. *Missing → gather it yourself: a scoped
  desk-research pass (a `loops-research` brief), discipline per
  [`../references/evidence-standards.md`](../references/evidence-standards.md), findings landing in
  this method's worklog.*

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
The working is done in the step's **worklog** `<step-folder>/competitor-analysis.md`
(`node_type: worklog`, e.g. `2-analysis/competitor-analysis.md`): the competitor list (≥5 named,
including one the team did not name first), the excluded players each with its reason, each player's
*game* and moat comparison, and the white-space / threat conclusion. This method keeps **one**
worklog, and both sections `{#competitors}` and `{#competitor-strategy}` are its **projections** into
the fixed shape of [`template-fragment.md`](template-fragment.md) — the worklog is the **source of
truth**, the sections hold nothing it does not, and the step's change-log history lives in the
worklog, not the sections (`process/CONVENTIONS.md` → *Step folders & worklogs*). External figures
arrive here dispatched from `sources/` by `source-intake`, cited in the worklog, never linked from
the artifact.

## Output
Projects `{#competitors}` and `{#competitor-strategy}` via
[`template-fragment.md`](template-fragment.md) from the single worklog; inputs via
[`questions.yaml`](questions.yaml).
