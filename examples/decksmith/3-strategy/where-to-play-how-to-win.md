---
node_type: worklog
tool: where-to-play-how-to-win
step: 3
title: "where-to-play / how-to-win — the working"
updated: 2026-08-23
version: 0.1.0
---

# where-to-play / how-to-win — the working

_Source of truth for `3-strategy.md#winning-aspiration`, `#where-to-play`, `#how-to-win`. Lens:
Lafley & Martin's Playing-to-Win cascade (opinionated — a company that frames strategy differently
can swap the method). `value-definition-strategy` contributes the moats to `#how-to-win` **here**
(this worklog owns that section — first tool in the marker). Status: `concept-viability` → the
aspiration is **find fit**, not scale._

## 1 · Winning aspiration

**Win the "editable-AND-designed" corner for client-facing sales & marketing decks — be the tool S1
switches to when a deck must be *both* on-brand-beautiful and a real, natively-editable file, and
prove that switch is repeatable in the US beachhead before an incumbent closes the export gap.**

Not "be a player in AI slides" (a slogan). The concrete outcome, this horizon: a reachable slice of
S1 (sales & marketing client-facing deck-makers) reliably choosing Decksmith over "generate in
Gamma/Canva, then rebuild by hand" — measured as repeatable paid pull in that niche, not raw signups.
Because the status is `concept-viability`, winning = **evidence of fit** (`H-001` holds, S1 switches,
they pay), not market share.

## 2 · Candidate cascades considered (≥3 distinct whole cascades)

A possibility is a whole arena **with** the winning logic that fits it — not three shadings of the
arena already assumed. The losers are kept with *why* they lose (the first question a board asks).

| # | Possibility (arena + winning logic) | Verdict | Why it loses / wins |
|---|-------------------------------------|---------|---------------------|
| **A (CHOSEN)** | **S1 client-facing sales/marketing deck-makers, US, PLG + founder-led design community; win by the taste-corpus moat + a native-editable-and-designed engine no incumbent prioritises** | **chosen** | The one arena where *both* halves of the value are non-negotiable (client-facing ⇒ must look designed **and** be handed over/edited natively). Our moat (taste corpus + founder credibility) applies; incumbents are structurally conflicted (see how-to-win). Meets the `concept-viability` aspiration — cheap, fast to read. |
| B | **Horizontal "AI PowerPoint for everyone" — students, internal decks, anyone; win on breadth + generation speed** | rejected | *No moat we hold applies here.* Breadth is exactly where Gamma, Canva and Microsoft outspend and out-distribute; taste doesn't differentiate for a student's one-off. We'd be a feature in a commoditised field, not a position. |
| C | **Enterprise brand-compliance decks — top-down sales to F500 brand/marketing-ops teams; win on governance + brand lock** | rejected | *Reachable but not winnable now.* Needs SSO/DLP/security, brand-governance workflows, and a sales org we don't have; the buyer is bought by Canva Enterprise / Microsoft distribution, not by taste. Also fails the aspiration: long cycles, capital-heavy — the opposite of a cheap fit-finding bet. Revisit as an *expansion* once the moat and case studies exist. |
| D | **Investor pitch-deck niche (Tome/Pitch's old arena); win on beautiful auto-generated fundraising decks** | rejected | *Wins the wrong game.* Episodic (one deck per raise), thin recurring budget, and it is the exact niche whose free-virality-without-monetisation killed Tome and Pitch (`R-005`). A recurring, company-budgeted *client-deck* job (S1) beats it on every viability axis. |

Two more shadings were folded rather than listed as full cascades: "design-native consultants/
agencies only" (the `#to-clarify` open item from Step 1) is **inside** arena A as the sharpest early
*proving ground*, not a separate arena; "freelance deck designers" likewise sit inside S1.

## 3 · Where to play (arena A) — with explicit exclusions

| Dimension | We play in | We deliberately exclude | Confidence |
|-----------|------------|-------------------------|------------|
| **Segments** | S1: sales & marketing client-facing deck-makers — agencies/consultancies, in-house sales/marketing deck teams, freelance deck designers. Sharpest proving ground: design-native agencies/consultants. | Students & education; internal-only / throwaway decks; investors making a one-off pitch deck; "everyone who makes slides". | [assumption] |
| **Geographies / markets** | US-first (English; where the SAM was sized and WTP is highest). | Non-English markets until localisation ships (an expansion trigger, not a launch arena). | [assumption] |
| **Channels** | Self-serve PLG + founder-led design community (see `channels-expansion.md`). | Top-down enterprise field sales; long-cycle procurement. | [assumption] |
| **Product scope / value-chain stage** | AI generation → **native, fully-editable `.pptx`/`.key`** with on-brand design; brand-kit reuse. | Real-time collaboration; non-slide formats [sourced: founder brief out-of-scope, as_of 2026-08-16]; a locked web-only editor [assumption] (our own differentiation stance, not in the brief). | mixed (see cell) |

A where-to-play with nothing excluded is not a choice — the exclusions above are the choice.

## 4 · How to win (the coherent logic + the moats it leverages)

**Winning logic.** Own the one corner where editable **and** designed are both mandatory, for the one
segment that will not accept either sacrifice. Beat the two halves of the field on the axis each is
structurally unable to prioritise:

| Winning move | Moat it leverages (from `value-definition-strategy`) | Why a rival can't cheaply copy it | Confidence |
|--------------|------------------------------------------------------|-----------------------------------|------------|
| **Out-design the native-export tools** (Plus AI, Copilot, MagicSlides): match their native editability, beat them on taste. | Curated design corpus + **founder taste/credibility** (differentiation / brand moat). | Taste is judgment encoded as a curated, labelled corpus + reputation — a rival gets the model, not the curation or the credibility. Slow, compounding. | [assumption] |
| **Out-export the design-led tools** (Gamma, Canva, Beautiful.ai): match their polish, beat them on a real native-editable file. | The native-editable-and-designed **engine** (`H-001`) — a capability/process edge. | The design leaders' *core business is the locked web editor*; truly native export cannibalises their lock-in — the incumbent's dilemma slows them, it isn't a skill gap. | [assumption] |
| **Convert the head-start into a durable moat before the wedge erodes.** | **Edit-behaviour data loop** + **brand-kit lock-in** (derivative moats — see value-definition-strategy revisit). | Which generated slides get kept vs restyled is proprietary behavioural data no clone has; a customer's embedded brand system is a switching cost. Both need scale — dependency-gated. | [assumption] |

**Cascade check (⚙️).** Does this how-to-win actually win in this where-to-play, given this
aspiration? Yes, *conditionally*: it wins **iff** `H-001` holds (the engine truly does both) and the
wedge converts to the data/lock-in moat before Gamma/Canva ship real native export or Microsoft
bundles it away. The aspiration (prove repeatable fit in S1 fast) is served by the PLG + founder-
community motion, which is cheap enough to read a signal in the `concept-viability` window. The one
load-bearing fragility is **timing** — carried as `H-012` / `R-007`.

## 5 · Seeded hypotheses (→ register)

The cascade's load-bearing assumptions, reconciled against the register (no duplicate ids):
- **`H-001`** (reused) — the engine does editable-AND-designed at scale: the enabler the whole
  how-to-win rests on.
- **`H-006`** (reused) — S1 US is the reachable, budgeted beachhead (the where-to-play bet).
- **`H-007`** (reused) — taste corpus + founder credibility is the compounding differentiation moat.
- **`H-012`** (new, minted in `bets.md`) — the wedge converts to the data + lock-in moat *before*
  the export gap closes (the timing bet the cascade check exposed).

## Change log

### 2026-08-23 — confidence-tag grammar normalized
- **From → To:** compound tags (`[sourced, fact — high]`, `[assumption: …]`, bare `[sourced]`) →
  canon grammar (`[sourced: <where>]` / `[assumption]`), qualifiers moved into notes
- **Why:** the tag vocabulary check (lint D2) is promoted to ERROR; the shipped example must model
  the grammar it teaches
- **Trigger:** run-2 hardening — the local model copied the example's compound-tag style

### 2026-08-16 — cascade worked and projected
- **From → To:** — → winning aspiration, ≥4 candidate cascades (1 chosen, 3+ rejected with reasons),
  where-to-play with explicit exclusions, how-to-win logic naming the moats, cascade integration check
- **Why:** Step 3 Act pass on `where-to-play-how-to-win`; chooses the arena and the winning logic
- **Trigger:** Step 3 operating-loop pass, sections `#winning-aspiration`, `#where-to-play`, `#how-to-win`
