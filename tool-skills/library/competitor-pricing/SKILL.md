---
node_type: card
kind: method
name: competitor-pricing
steps: [2]
prerequisites: [competitor-list]
reads: [section:competitors, source:research, source:kb]
writes: [worklog, section:competitor-pricing]
opinionated: false
method_basis: "dated pricing scan per competitor — published price with a read-date, never a guess"
evidence_standard: external-sources
volume_rule: "one row per player in the {#competitors} detailed table — a price not found is '— to clarify —', never a silently skipped row"
selection_rule: "only comparable, dated prices enter the table; a price that can't anchor a comparison goes to the reject table with the reason"
rejects_shown: required
status: draft
version: 0.2.0
updated: 2026-08-27
---
# Competitor Pricing

Capture each competitor's **published pricing with the date you read it**. Fills
`{#competitor-pricing}`. This is an **input** to three downstream reads — `market-sizing`'s
*units × price*, the Step-3 [`pricing-strategy`](../pricing-strategy/SKILL.md) decision, and the
Step-4 financial model — it is **not our price**.

**Method basis.** A per-competitor pricing scan from the competitor's own site or a web search,
every figure dated: published pricing is the fastest-ageing fact in the analysis, and an undated
price is a claim about an unknown month.

**No external source, no settled verdict.** This method declares `evidence_standard:
external-sources`: if by pass time nothing external has arrived (no dispatched research, no dated
capture in `sources/`), the section is written as an **explicit gap report** — load-bearing values
`— to clarify —`, each naming the source that would settle it — and the move-5 note names the
missing input. It is never delivered as settled analysis; the linter (check L2) flags a worked
section that shows no `[sourced: …]` and declares no gap.

## When to apply

- Step 2, once the `{#competitors}` detailed table exists — the scan runs over that list.
- Re-run when a competitor repackages or repricing is announced; the old rows keep their dates.

## Prerequisites

- **Competitor list** — the detailed-table players from `competitor-analysis`. *Missing → run
  `competitor-analysis`; scanning prices of players nobody vetted wastes the scan.*

## How to do it

1. **One row per detailed-table player.** Plan / model / price / source, straight from the
   competitor's site or a search hit. Not public → `— to clarify —`, tagged as such; never a guess
   and never a silently missing row.
2. **Date every price.** Record the day you read it. A pricing page is a snapshot, not a fact about
   today.
3. **Keep only comparable prices.** A price you cannot anchor a comparison on — enterprise
   "contact us", a reseller's markup, an out-of-region plan — goes to the **reject table** with the
   reason, not into the comparison.
4. **Note the model, not just the number.** Per-seat vs usage vs flat changes what the number
   means; a naked price without its model misleads the sizing and the Step-3 decision.
5. **Feed the readers.** `market-sizing` takes a price anchor from here; `pricing-strategy` (Step 3)
   positions against it; the financial model (Step 4) stress-tests with it.

## Anti-patterns

- **Guessed pricing.** Numbers with no source, stated as fact.
- **Undated prices.** "Their Pro is $29" — read when? Repricing is routine; the date is the claim.
- **Averaging models.** Blending a per-seat and a usage price into one "market price" — the models
  are not commensurable.

## Worklog & projection

The working is done in the step's **worklog** `<step-folder>/competitor-pricing.md`
(`node_type: worklog`, e.g. `2-analysis/competitor-pricing.md`): the dated scan per player, the
prices found but rejected as inputs with reasons, and the not-public `— to clarify —` list. That
worklog is the **source of truth**; the artifact section `{#competitor-pricing}` is its
**projection** into the fixed shape of [`template-fragment.md`](template-fragment.md), holding
nothing the worklog does not, and the step's change-log history lives in the worklog, not the
section (`process/CONVENTIONS.md` → *Step folders & worklogs*). External figures arrive here
dispatched from `sources/` by `source-intake`, cited in the worklog, never linked from the artifact.

## Output

Projects `{#competitor-pricing}` via [`template-fragment.md`](template-fragment.md) from the
worklog; inputs via [`questions.yaml`](questions.yaml).
