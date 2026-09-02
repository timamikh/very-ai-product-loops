---
node_type: card
kind: method
name: pricing-strategic-plan
steps: [4]
prerequisites: [the step-3 pricing decision, unit economics]
reads: [register:hypotheses, register:metrics, source:metrics, source:kb, section:pricing, worklog:3-strategy/pricing-strategy, worklog:4-strategic-plan/unit-economics, worklog:4-strategic-plan/financial-model]
writes: [worklog, section:pricing, register:hypotheses]
opinionated: true
method_basis: "Margin revisit of a value-based pricing decision: chosen price vs contribution margin, inference COGS per tier, free-tier burn; outcome is 'holds' or a proposed change to the Step-3 decision — never a silent re-decision"
evidence_standard: derived
volume_rule: n/a
selection_rule: n/a
rejects_shown: n/a
status: draft
version: 0.2.0
updated: 2026-08-19
---
# Pricing — Strategic-Plan Revisit

Re-read the **Step-3 pricing decision against the numbers that now exist**: once `unit-economics`
is built, check the chosen price and packaging against **contribution margin**, **inference COGS
per tier**, and **free-tier burn**. The outcome is binary and explicit: the decision **holds** (log
why), or a **proposed change to `3-strategy.md#pricing`** — marked ⚙️, which triggers that
section's re-confirmation. The price is never silently re-decided at Step 4.

**Method basis.** Value-based pricing decides the price at Step 3 (`pricing-strategy`); cost is a floor, not
the method. This revisit checks the floor: with real (or modeled) unit economics on the table, does
each tier still clear its margin once inference COGS and free-tier burn are counted? A price that
was strategically right and economically underwater is a finding — routed back to the decision's
home, not patched locally.

> **Relation to neighbours (one mechanism, one way).**
> - `pricing-strategy` (Step 3) is **the only place the price and packaging are decided**. This method
>   *checks* the decision against margin; if it fails, the change is proposed *there* (⚙️ on
>   `3-strategy.md#pricing`), re-confirmed by the human — never enacted here.
> - `unit-economics` supplies the contribution margin and COGS lines this revisit reads; this
>   method does not recompute them.
> - `financial-model` projects the (held or changed) price forward; a proposed change flags the
>   model's revenue lines too.

## When to apply
- **Step 4**, immediately after `unit-economics` exists — before the financial model is signed on
  top of a price nobody has margin-checked.
- When COGS shift materially (a model/provider change, a usage-pattern surprise) or free-tier burn
  outgrows its plan — re-run the revisit against the same Step-3 decision.

## Prerequisites
- **The Step-3 pricing decision** — value metric, tiers/fences, price points
  (`3-strategy.md#pricing`). *Missing → run `pricing-strategy` (Step 3) first; there is nothing to revisit.*
- **Unit economics** — contribution margin and the explicit LLM-inference COGS line
  (`{#unit-economics}`). *Missing → run `unit-economics` first; a revisit without margin numbers is
  the Step-3 argument repeated.*

## How to do it
1. **Restate the decision under test.** The value metric, tiers, fences, and price points as
   decided at Step 3 — verbatim, with their `[sourced: …]`/`[assumption]` tags. This is the object
   being checked, not re-derived.
2. **Read contribution margin per tier.** From `unit-economics`: revenue per payer minus COGS per
   payer, per tier. Name the tier(s) where the margin is thin or negative.
3. **Trace inference COGS per tier.** What each tier's usage pattern costs in LLM inference (and
   other usage-scaling COGS). A flat price over a usage-scaling cost is where margins silently
   invert — say per tier whether the fence caps the cost or not.
4. **Price the free tier's burn.** What free usage costs per month, what it converts at, and
   whether the paid margin funds it. Free-tier burn is a COGS line, not marketing dust.
5. **Deliver the verdict — holds or a proposed change.** If the decision **holds**, log why (which
   margins clear, under which assumptions). If not, write the **proposed change** — new price
   point, moved fence, usage cap, or a re-metered value metric — as a ⚙️ proposal against
   `3-strategy.md#pricing`, which triggers that section's re-confirmation by the human.
6. **Seed hypotheses where the check rests on assumptions.** A margin verdict built on assumed
   usage or conversion → `H-…` (`type: viability`) so the assumption is tested, not enshrined.

## Anti-patterns
- **Re-deciding the price here.** Changing a number at Step 4 because the margin failed — the
  change is *proposed* to the Step-3 section and re-confirmed, never enacted locally.
- **Cost-plus relapse.** Turning the margin check into the pricing method — cost stays a floor; the
  revisit verifies the floor holds, it does not set the price from it.
- **Ignoring the free tier.** Margin computed on payers only, while free usage burns inference
  underneath — the burn is part of the verdict.
- **Blended-tier margin.** One averaged margin across tiers hides the tier that is underwater —
  read per tier, against its own usage pattern.
- **A verdict with no log.** "Holds" with no stated assumptions — when COGS shift, nobody knows
  what the verdict rested on.

## Worklog & projection
This method owns **no Step-4 section**; it is reached through the `{#pricing}` marker
(`<!-- tool: pricing-strategy, pricing-strategic-plan -->`, second tool) and works in **its own
worklog** `3-strategy/pricing-strategic-plan.md` (`node_type: worklog`) — the restated Step-3
decision, the per-tier margin and inference-COGS read, the free-tier burn, and the verdict with its
assumptions. The step-4 economics workings it re-reads are **declared worklog inputs**
(`worklog:4-strategic-plan/unit-economics` · `worklog:4-strategic-plan/financial-model` in `reads`) —
read, never written: this method writes no other method's worklog (the write rule, N6). The section
it `writes` is `{#pricing}`, homed at Step 3: a **holds** verdict logs there as a confirmation note;
a **change** lands there as a ⚙️ proposal in the fixed shape of
[`template-fragment.md`](template-fragment.md), triggering the section's re-confirmation
(`process/CONVENTIONS.md` → *Step folders & worklogs*).

## Output
Verdict on the Step-3 pricing decision: **holds** (logged with its assumptions) or a **⚙️ proposed
change to `3-strategy.md#pricing`** projected via [`template-fragment.md`](template-fragment.md);
inputs via [`questions.yaml`](questions.yaml). Margin-critical assumptions seed `H-…`
(`type: viability`); a proposed change also flags `financial-model`'s revenue lines.
