---
node_type: worklog
tool: pricing-strategy
step: 3
title: "pricing & packaging — the working"
updated: 2026-08-16
version: 0.1.0
---

# pricing & packaging — the working

_Source of truth for `3-strategy.md#pricing`. Lens: value-based pricing (price anchors to value vs
the next-best alternative; cost is a floor, not the method). The decision is made here (qualitative +
first numbers); Step 4's `pricing-strategic-plan` firms the numbers up and runs them through
`unit-economics` (incl. LLM inference COGS) + `financial-model`. Competitor anchors are the dated
Step-2 scan (`2-analysis/competitor-pricing.md`, as_of 2026-08-16), not our price._

## 0 · The anchors we price against (from Step 2, dated 2026-08-16)

- Comparable prosumer/business AI-deck tier clusters **~$8–20/mo/seat** (Gamma Plus $8 / Pro $18,
  Plus AI $10–20, Presentations.ai Pro $20, Chronicle Plus $25, Beautiful.ai Pro $12).
- Business/team tiers **~$20–40/seat/mo** (Beautiful.ai Team $40, Plus AI Team $30).
- **Microsoft Copilot $18/seat/mo *on top of* an M365 licence** — the bundle is the real WTP pressure
  ("it's already in PowerPoint").

## 1 · Value metric

**Per active seat (per deck-maker)** — primary. Rationale: S1 is a professional, recurring tool used
by individuals and small teams; value scales with each deck-maker using it, and per-seat is the
metric this market already prices on (all anchors above are per-seat). A **fair-use generation cap
(credits)** rides on the entry tier only, as a fence — *not* as the primary meter.

- **Considered and rejected as primary: per-deck / pure usage.** S1's best-fit customers make *many*
  client decks; metering per deck punishes exactly the power users we most want and caps growth. Kept
  only as a soft cap on the entry tier.

## 2 · Packaging — good / better / best (fences)

| Tier | For which segment | Included | Fence (why they pick it) | Price point (⚙️) | Model | Conf |
|------|-------------------|----------|--------------------------|------------------|-------|------|
| **Solo** (good) | Freelance / individual deck-maker | AI generation, native `.pptx`/`.key` export, core design styles, 1 brand kit, fair-use generation cap | Single seat; enough to feel the editable-AND-designed value | **~$24/mo** | subscription (annual/monthly) | [assumption] |
| **Team** (better) | Agency / sales team needing brand consistency | Multiple seats, shared brand kits, brand-lock, priority generation, no soft cap | Teams that must stay on-brand across people | **~$45/seat/mo** | subscription per seat | [assumption] |
| **Studio** (best) | Agencies producing client decks at volume | Unlimited brand kits, client workspaces, white-label export, bulk/API | Volume + client-management; the agency's production line | **~$90/seat/mo or custom** | subscription / hybrid | [assumption] |

## 3 · Anchoring to the next-best alternative

- **Solo vs Gamma/Canva + rebuild:** priced a deliberate **premium above the $8–20 cluster** (~$24).
  The value gap justifying the delta = the eliminated restyle tax (hours per deck) + no export
  breakage. We are *not* the cheapest; we are the one that removes the rebuild.
- **Team vs Beautiful.ai Team ($40) / Plus AI Team ($30):** at/just above, on the same editable-AND-
  designed differentiation.
- **vs the Copilot bundle ($18 on top of M365):** we do not win on price against "already in
  PowerPoint"; we win on design taste. The premium is the tell that we are a different product, not a
  cheaper Copilot.

## 4 · Willingness-to-pay — evidence status

**All price points `[assumption]` at Step 3** — no pilot, no WTP survey behind a fictional product.
That is expected at this step; `pricing-strategic-plan` (Step 4) firms them up (van Westendorp / direct
WTP / pilot behaviour) and `unit-economics` checks whether ~$24–45/seat survives the LLM inference
COGS. If the margin check fails, the iteration returns **here** — the value metric and packaging are
this tool's call, not Step 4's.

## 5 · Monetisation discipline (guards `R-005`, the Tome/Pitch trap)

Deliberately **not** free-first-unlimited. A **tight, time-boxed free trial** (a small number of
full-export decks, or 14 days) that converts to a paid action fast; **native export + brand kits are
paid fences from day one.** The category punished free virality without monetisation — we meter and
fence from launch. This is a strategy choice, logged; the free/trial mechanics get numbers at Step 4.

## 6 · Seeded hypotheses (→ register)

- **`H-010` (viability, pricing, NEW):** S1 will pay a **premium (~$40/seat/mo blended)** for
  editable-AND-designed — above the $8–20 prosumer cluster — rather than discount to bundle/free
  levels. The monetisation bet; the whole model's viability rests on it. Minted in `bets.md`.

## Change log

### 2026-08-16 — pricing & packaging worked and projected
- **From → To:** — → value metric (per seat), good/better/best tiers with fences and first price
  points, anchoring to each alternative, WTP evidence status ([assumption]), monetisation discipline
  vs `R-005`; seeded `H-010`
- **Why:** Step 3 Act pass on `pricing-strategy`; the price is a strategic choice, decided here
- **Trigger:** Step 3 operating-loop pass, section `#pricing`
