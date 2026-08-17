---
node_type: worklog
tool: channels-expansion
step: 3
title: "channels & expansion — the working"
updated: 2026-08-16
version: 0.1.0
---

# channels & expansion — the working

_Source of truth for `3-strategy.md#channels-expansion`. Lens: Bullseye (Weinberg/Mares) — brainstorm
≥8 candidates across ≥3 channel-type categories, score 1·3·5 on reach × cost-to-test × testability,
rank into outer/middle/inner rings (inner = the 3 highest, tested now). Channel = *where* we reach
them; the UVP (`uvp-cpv.md`) is *what* we say — kept separate._

## 1 · Brainstorm — ≥8 candidates across ≥3 categories

| # | Candidate | Category |
|---|-----------|----------|
| 1 | Founder-led design community (X/LinkedIn/design newsletters — the founder's taste/credibility is both moat and channel) | community |
| 2 | Content/SEO: comparison + intent pages ("editable AI PowerPoint", "Gamma alternative", "export deck to PowerPoint") | content/SEO |
| 3 | Paid search on competitor-alternative + intent keywords | paid |
| 4 | Product Hunt / launch platforms | community/launch |
| 5 | Paid social (LinkedIn) to agencies & sales teams | paid |
| 6 | Agency / consultancy partnerships & reseller | partnerships |
| 7 | Design-influencer / YouTube tutorial collabs | partnerships/community |
| 8 | "Made with Decksmith" assisted referral on shared decks | existing-base motion |
| 9 | Outbound to agencies | outbound |
| 10 | Design & sales Slack/Discord communities | community |
| 11 | PowerPoint/Slides add-in marketplace listing | marketplace |

11 candidates across 7 categories — clears the ≥8 / ≥3 floor.

## 2 · Score (1·3·5) and rank into rings

Reach = how many of *exactly* S1 sit there · Cost-to-test = one honest test, inverted (cheap = high)
· Testability = can we read a signal in days. A reach claim is an external claim — tagged below.

| Candidate | Reach | Cost-to-test | Testability | Σ | Ring |
|-----------|:---:|:---:|:---:|:---:|------|
| 1 Founder-led design community | 5 | 5 | 5 | 15 | **inner** |
| 3 Paid search (intent/competitor kw) | 3 | 3 | 5 | 11 | **inner** |
| 2 Content/SEO comparison+intent | 5 | 3 | 3 | 11 | **inner** |
| 4 Product Hunt launch | 3 | 5 | 5 | 13 | middle (one-shot event, not a repeatable channel) |
| 10 Slack/Discord communities | 3 | 5 | 3 | 11 | middle |
| 8 "Made with Decksmith" referral | 3 | 3 | 3 | 9 | middle (⚠ monetisation-trap caution, see §4) |
| 5 Paid social LinkedIn | 3 | 3 | 3 | 9 | middle |
| 7 Design-influencer collabs | 3 | 3 | 3 | 9 | middle |
| 9 Outbound to agencies | 3 | 3 | 3 | 9 | outer |
| 11 Add-in marketplace listing | 3 | 1 | 1 | 5 | outer |
| 6 Agency partnerships/reseller | 3 | 1 | 1 | 5 | outer (long cycle; revisit at expansion) |

Reach tags: #1 reach 5 `[assumption]` — founder's audience overlaps S1 but its *size* is unverified;
#2 reach 5 `[assumption]` — "Gamma alternative" / "editable export" intent demand is *plausible* but
**unverified** (no Step-2 keyword-demand source exists; a keyword-volume check is the cheapest way to
firm it — deferred to the channel test itself); the rest `[assumption]`. Losers kept, not deleted.

**Inner ring (test now):** 1 Founder-led community · 3 Paid search · 2 Content/SEO comparison.
Product Hunt is a middle-ring *event* — fire once at launch, not a standing channel.

## 3 · GTM motion — product-led (PLG), self-serve

The economics decide, not taste: Solo ~$24/mo and Team ~$45/seat (`pricing-strategy.md`) **cannot fund
a sales call** — a self-serve try→buy motion is the only one the price supports. S1 individuals and
small teams buy self-serve. The **Studio/agency** tier layers a light **partner/sales-assist** on top
*later* (its price can fund a touch); it does not change the launch motion.

**Coherence check (inner ring × motion):** all three inner channels start the PLG first step — land on
a self-serve trial. No mis-fit to record. (Outbound/partnerships would need a sales motion the price
can't fund — correctly in the outer ring.)

## 4 · Measurable test per inner-ring channel (metric · cost · threshold — set *before* running)

| Inner channel | Metric | Cost (test) | Success threshold (⚙️) |
|---------------|--------|-------------|------------------------|
| Founder-led community | trial signups per post / thread → trial→paid rate | founder time only | ≥ X qualified trials/week at trial→paid ≥ target; CAC ≈ $0 |
| Paid search (intent kw) | CPC → trial → paid CAC | ~$2–5k test budget | blended CAC < LTV ceiling from Step-4 unit-economics |
| Content/SEO comparison | organic trials from comparison pages (paired w/ paid to read fast) | content production time | ≥ N trials/mo within one quarter; ranking on ≥3 intent terms |

Thresholds are `[assumption]` placeholders until Step-4 `unit-economics` sets the LTV/CAC ceiling and
Step-5/6 design the actual tests.

**Monetisation-trap caution (`R-005`).** The "Made with Decksmith" referral footer is the classic
free-virality lever that killed Tome/Pitch when it ran *ahead* of monetisation. Kept in the middle
ring, **gated**: enabled only *after* the paid fences convert — assisted, not the growth engine.

## 5 · Expansion path (each step gated by a trigger)

| From → To | Trigger that unlocks it |
|-----------|-------------------------|
| S1 US → **adjacent US segments** (corporate comms / brand teams; consultant finance decks) | PLG CAC < LTV ceiling **and** brand-kit retention proven (the lock-in derivative starting to hold) |
| US → **non-English geographies** | localisation ships (design taste + templates travel); a real reach signal in a target locale |
| PLG → **enterprise (top-down)** | security/SSO + brand-governance shipped **and** ≥ N agency case studies exist (arena C from where-to-play, entered as expansion not launch) |

## 6 · Seeded registers

- **`H-011` (desirability/channel, NEW):** founder-led design-community distribution reaches S1 at a
  CAC that PLG economics support (near-zero for the warm audience). Minted in `bets.md`.
- **`R-008` (execution/GTM, NEW):** the founder-community channel doesn't scale past the founder's own
  audience → CAC explodes once it saturates. Seeded to the risk register (fully triaged in
  `pre-mortem.md`).

## Change log

### 2026-08-16 — channels & expansion worked and projected
- **From → To:** — → 11-candidate brainstorm (7 categories), 1·3·5 scoring ranked into rings, inner
  ring of 3 with measurable tests, PLG motion with the price-vs-touch reasoning + coherence check,
  gated expansion path; seeded `H-011`, `R-008`
- **Why:** Step 3 Act pass on `channels-expansion`; picks the channels to test now and the motion the
  plan inherits
- **Trigger:** Step 3 operating-loop pass, section `#channels-expansion`
