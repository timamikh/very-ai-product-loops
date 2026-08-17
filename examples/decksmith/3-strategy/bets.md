---
node_type: worklog
tool: bets
step: 3
title: "strategic bets — the working"
updated: 2026-08-16
version: 0.1.0
---

# strategic bets — the working

_Source of truth for `3-strategy.md#bets`. Lens: the JTBD switching model applied to strategy — a bet
is "we bet `<segment>` will hire us over `<status quo>` for `<job>` because pull > anxiety + habit",
each tied to a **named moat** (the *because*). One bet = one typed hypothesis. `bets` is the primary
of the `<!-- tool: bets, value-definition-strategy -->` marker, so the moat contribution lands here.
Reconciled against the register first — **no duplicate `H-` for a claim already seeded.**_

## 1 · Candidate bets (drafted on the job, not on features)

| # | Bet (segment · status quo · job · why pull>anxiety+habit) | Type | Moat leaned on | Disposition |
|---|-----------------------------------------------------------|------|----------------|-------------|
| b1 | S1 will hire Decksmith over **"Gamma/Canva + manual rebuild"** for making client-ready decks, because the restyle tax removed (pull) beats trusting the AI's taste (anxiety) + owning PowerPoint already (habit). | desirability | taste corpus (`H-007`) + engine (`H-001`) | **carry → reuses `H-003`/`H-001`** (sharpen, don't re-mint) |
| b2 | The **engine** can do editable-AND-designed at scale on arbitrary content — the enabler the whole how-to-win rests on. | feasibility | engine capability | **carry → `H-001`** (reused; riskiest) |
| b3 | **S1 US** is a reachable, recurring, company-budgeted beachhead. | viability | — (a where-to-play bet) | **carry → `H-006`** (reused, sharpened by where-to-play) |
| b4 | The **taste corpus + founder credibility** is a real, compounding differentiation moat. | viability | itself | **carry → `H-007`** (reused) |
| b5 | S1 will **pay a premium (~$40/seat/mo)** for editable-AND-designed, not discount to bundle/free. | viability | taste corpus (differentiation lets us hold price) | **carry → mint `H-010`** (pricing — genuinely new) |
| b6 | **Founder-led design-community** distribution reaches S1 at a **PLG-viable CAC** (near-zero for the warm audience). | desirability | founder credibility (channel = moat) | **carry → mint `H-011`** (channel — new) |
| b7 | The export **wedge converts to a durable moat** (edit-behaviour data loop + brand-kit lock-in) **before** Gamma/Canva ship real native export or Microsoft bundles it away. | viability | derivative moats (data + lock-in) | **carry → mint `H-012`** (moat-trajectory/timing — new) |
| c1 | "Users will love the generation UI" | — | none | **cut** — feature bet, no segment/status-quo/forces. Belongs in a spec, not the strategy. |
| c2 | "We'll win because we use a frontier LLM" | — | none (commodity) | **cut** — the model is everyone's input; already killed as a feature-moat at Step 1. |

## 2 · Register reconciliation (no duplicate ids)

- **b1** restates the desirability switch already carried by `H-003` (restyle-tax pain) + gated by
  `H-005` (editability). **Sharpened, not re-minted** — the switch is the pain made into a wager; its
  evidence must accumulate on `H-003`, not split across a new id.
- **b2 → `H-001`**, **b3 → `H-006`**, **b4 → `H-007`** — reused as-is (the cascade's load-bearing
  assumptions `where-to-play-how-to-win.md` already pointed at).
- **b5/b6/b7 → new `H-010`/`H-011`/`H-012`** — pricing, channel, and moat-trajectory are claims no
  prior step seeded. New ids are correct here.

Carried: **6 bets** (b1–b7 collapsing b1 onto `H-003`/`H-001`) — within the 3–7 rule. Two candidates
cut, kept visible.

## 3 · value-definition-strategy contribution (moats, revisited at strategy)

The moat picture the bets lean on — the Step-3 revisit of the Step-1 base moats (full working +
re-projection in `../1-concept/value-definition-concept.md`, per the skill: one moat story, one
section, updated in place):

- **Base moats re-tested in the chosen arena:** taste corpus + founder credibility **hold** (survive
  the post-AI rebuild — a clone gets the model, not the curation or reputation); the **native-export
  engineering is a *wedge*, not a durable moat** — it erodes as OOXML-generation commoditises.
- **Derivatives now nameable (with dependencies):** (i) **edit-behaviour data loop** — proprietary
  data on which slides get kept vs restyled; *dependency:* edit instrumentation ships + usage scale;
  (ii) **brand-kit lock-in / switching cost** — *dependency:* brand-kit + deck-library storage ships
  and a customer embeds their brand system.
- **Moat trajectory:** enter on **taste corpus + founder distribution** (exist now) → build the
  **data loop** (needs scale) → build **brand-kit lock-in** (needs product + customer embed). The
  export wedge buys time; it must be converted before it erodes — exactly bet **b7 / `H-012` / `R-007`**.

## Change log

### 2026-08-16 — strategic bets worked and projected
- **From → To:** — → 7 candidate bets + 2 cuts, register reconciliation (reuse `H-001`/`H-003`/`H-006`/
  `H-007`, mint `H-010`/`H-011`/`H-012`), value-definition-strategy moat contribution (re-tested base
  moats, derivatives with dependencies, trajectory)
- **Why:** Step 3 Act pass on `bets` (+ `value-definition-strategy` as second tool); restates the
  strategy choices as falsifiable, moat-backed wagers
- **Trigger:** Step 3 operating-loop pass, section `#bets`
