---
node_type: worklog
tool: segment-cvp
step: 5
title: "segment–CVP market-entry bundles — Period 1"
updated: 2026-08-17
version: 0.1.1
---

# segment–CVP bundles — the working (Period 1)

_Source of truth for `5-tactical-plan.md#market-bundles`. **Composes** (does not re-derive) the outputs
of `1#segments`, `1-concept/segment-pains.md`, `3#uvp-cpv`, `3#channels-expansion` into testable
market-entry bundles: segment · situation · pain · CVP · offer · channel · signal. Volume rule: **≥3
distinct situations for the priority segment and ≥8 bundles total before any is staged.** Then the
**6-filter readiness gate** (binary), the **1·3·5 priority score** over the ready ones, stage the top
3–5, seed `H-…` (`type: desirability`). Cut bundles are kept with their reason._

## 1 · Bundles composed (N = 9; S1 across 7 situations + one adjacent segment + one deliberate reject)

Priority segment **S1** = sales & marketing client-facing deck makers (`1#segments`). Situations are
the unit of generation, not the segment.

| ID | Segment · situation | Pain (cost of inaction) | CVP (result, not feature) | Offer | Channel (named) | Signal · tier |
|----|---------------------|-------------------------|---------------------------|-------|-----------------|---------------|
| B-01 | S1 agency · **client pitch on deadline** | rebuild AI output by hand → hours lost the night before | "client-ready, on-brand native deck — zero rebuild" | free design-partner trial | founder's **design community** (warm) | pilot use + price-talk · **strong** |
| B-02 | S1 consultant · **recurring monthly QBR/report deck** | re-skinning the same report every month | "productise your report deck — on-brand, editable, every month" | diagnostic + trial | a **named consulting community** (e.g. consulting-focused Slack / r/consulting) | trial + repeat use · **strong** |
| B-03 | S1 in-house marketer · **rebrand rollout across the deck library** | re-skinning hundreds of slides by hand | "re-skin your whole deck library to the new brand — still editable" | brand-kit demo | **LinkedIn design-content + SEO** ("on-brand editable AI deck") | demo → meeting · **medium** |
| B-04 | S1 sales rep · **per-prospect deck customisation at volume** | rebuilding the pitch for each prospect | "personalise every pitch without rebuilding slides" | trial | **sales-enablement community** | seat expansion · **strong** |
| B-05 | S1 freelance designer · **multi-SMB-client deck work** | deck volume caps billable clients | "10× your deck output and keep *your* taste" | trial | founder's **design community** (warm) | paid subscription · **strong** |
| B-07 | S1 agency · **RFP response deck overnight** | turning an RFP brief into a deck under time pressure | "the RFP brief → an on-brand editable deck by morning" | trial | **agency-owner Slack/Circle** | pilot · **strong** |
| B-09 | S1 marketer · **conference/speaker deck** | speaker deck must be on-brand but is a one-off | "an on-brand, editable speaker deck in an afternoon" | template + trial | event/community | trial · **medium** |
| B-06 | **S2 (adjacent)** startup founder · **investor deck** | investor deck is a locked image or an ugly editable | "investor-ready, editable — not a locked PDF" | template + trial | IndieHackers / accelerator | trial · **medium** |
| B-08 | **"SMB owners who make their own decks"** (mass) | — | "make better decks with AI" | trial | "online" | "interest" · weak |

Seven S1 situations (multi-SMB-client work · deadline pitch · monthly QBR · rebrand rollout ·
per-prospect · RFP · conference) → volume rule met. B-06 is an adjacent segment kept for contrast; B-08
is composed **to be rejected** — a real gate needs something to fail (the "four survivors" anti-pattern
guard). Bundle count: 7 S1 + 1 adjacent (B-06) + 1 reject (B-08) = 9.

## 2 · 6-filter readiness gate (binary — every filter must pass)

| ID | Find | Recognize | Pain | Alternative | CVP | Action | Verdict |
|----|------|-----------|------|-------------|-----|--------|---------|
| B-01 | ✓ warm community | ✓ | ✓ acute | ✓ Gamma+rebuild | ✓ | ✓ pilot | **ready** |
| B-02 | ✓ named community | ✓ | ✓ | ✓ manual/VA | ✓ | ✓ trial | **ready** |
| B-03 | ✓ LinkedIn/SEO | ✓ | ✓ | ✓ manual | ✓ | ✓ demo | **ready** |
| B-04 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **ready** |
| B-05 | ✓ warm community | ✓ | ✓ acute | ✓ manual | ✓ | ✓ subscription | **ready** |
| B-07 | ✓ agency Slack | ✓ | ✓ | ✓ | ✓ | ✓ pilot | **ready** |
| B-09 | ✓ | ✓ | ~ low pain | ✓ | ✓ | ✓ | **ready** (low pain, will score low) |
| B-06 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **ready** (off-beachhead — not S1) |
| B-08 | ✗ "online" | ✗ "everyone" | ✗ "would be nice" | ✗ | ✗ "better decks" | ✗ "interest" | **not-ready** — fails 6/6; mass audience, kept as the reference reject |

## 3 · Priority score over the ready bundles (1·3·5 × 5 criteria → 5–25) ⚙️

| ID | Pain acuteness | Reachability | Deliverability | WTP evidence | Speed to signal | **Sum** |
|----|----------------|--------------|----------------|--------------|-----------------|---------|
| **B-05** | 5 | 5 (warm) | 3 | 5 (designers pay for tools) | 5 (1–2 days) | **23** |
| **B-01** | 5 | 5 (warm) | 3 | 3 (pay for adjacent) | 5 | **21** |
| **B-02** | 5 | 3 | 3 | 5 (consultants pay VAs) | 3 | **19** |
| B-07 | 5 | 3 | 3 | 3 | 3 | 17 |
| B-04 | 3 | 3 | 3 | 3 | 3 | 15 |
| B-06 | 3 | 3 | 3 | 1 (off-beachhead) | 3 | 13 |
| B-03 | 3 | 3 | 1 (needs brand-kit, backlogged) | 3 | 1 (SEO slow) | 11 |
| B-09 | 1 (low pain) | 3 | 3 | 1 | 3 | 11 |

All scores ⚙️ (acting PO, awaiting human). Deliverability caps at 3 across the board — the prototype
isn't built yet (`G-D1`); no bundle scores 5 there, honestly.

## 4 · Staged — top 3 by readiness (capacity thins the test set further)

**Staged: B-05, B-01, B-02.** Three distinct situations, two channels (warm design community × named
consulting community). **Tested this period:** only B-01/B-05 — they ride the `H-011` founder-community
recruit push (`hypothesis-test-design`). **B-02's test (`H-013`) is deferred** to a later period on
founder capacity (0.3 FTE g2m, `prioritization` §2) — staged in the *ranking*, not run this period.
B-07/B-04 are the next in line; B-03/B-09/B-06 sit below the line with their scores; B-08 is the
recorded reject.

## 5 · Seed the hypothesis register (each staged bundle → a `desirability` bet; instances reuse ids)

- **B-01** (agency deadline, warm community) → **instantiates `H-011`** (founder-community channel) +
  **`H-003`** (the switch). One claim, one id — **not re-minted**.
- **B-05** (freelance designer, warm community) → **also an instance of `H-011`** — same channel, a
  different situation on it. Recorded under `H-011`, **not re-minted**.
- **B-02** (consultant, a *named consulting community*) → a **genuinely new go-to-market claim** (a
  different channel/audience than the founder's design community) → **mints `H-013`**
  (`desirability`): *a named consulting community reaches S1 consultants at a qualified-action signal.*

Decision commitment per staged bundle (the test design itself is handed to `hypothesis-test-design`,
not designed here):

- **B-01** — on the `H-011` readout: qualified pilot signal at/above the bar → **scale** the warm
  push into more agency situations; recruits sign up but don't pilot → **iterate** the offer (the
  deadline-pitch framing, not the channel); the warm audience yields no reachable S1 agency buyers →
  **reject** this channel-situation pair.
- **B-05** — same readout, freelance-designer situation: pilot + willingness to pay a subscription →
  **scale**; pilots but balks at paying → **iterate** pricing/packaging toward `H-010`'s price-talk;
  no pilot uptake → **reject** the situation, keep the channel (it still carries B-01).
- **B-02** — **research**: staged in the ranking but deferred on founder capacity; no decision falls
  this period — it enters `hypothesis-test-design` (`H-013`) when it gets a period slot.

## 6 · What was cut and why (kept — the cheapest output, the most expensive to re-derive)

- B-08 → **not-ready**, fails all 6 filters (mass audience) — the reference reject.
- B-03 → ready but scored 11 (deliverability 1: depends on brand-kit storage, backlogged C4; SEO slow).
- B-09 → ready but scored 11 (pain acuteness 1 — a one-off deck).
- B-06 → ready but off-beachhead (S2, WTP 1) — parked; the beachhead is S1.
- B-04, B-07 → ready, scored 15/17 — **next in line**, not staged only for founder capacity (0.3 FTE).

## Change log

### 2026-08-17 — human review pass: situation count corrected, staged decisions written out
- **From → To:** (1) "6 S1 situations" → **7** in §1's heading and the change log below — §1 itself
  listed seven (multi-SMB-client · deadline pitch · monthly QBR · rebrand rollout · per-prospect ·
  RFP · conference) and the artifact projected seven, so the headline number was the odd one out;
  (2) §5's claim that per-bundle decision commitments were "recorded" → the three commitments
  (B-01 scale/iterate/reject on the `H-011` readout, B-05 likewise with the `H-010` price fork,
  B-02 research/deferred) are now actually written
- **Why:** a worklog that contradicts its own table invites the next reader to trust neither; a
  claimed-but-absent record is worse than no claim — review returned both
- **Trigger:** human review of the finished run (tactics lens)

### 2026-08-16 — Period-1 bundles composed, gated, scored; `H-013` seeded
- **From → To:** — → 9 bundles (7 S1 situations + 1 adjacent + 1 deliberate reject), 6-filter gate
  (B-08 fails all six), 1·3·5 score over 8 ready bundles, **top 3 staged (B-05/B-01/B-02)**; B-01/B-05
  recorded as `H-011`/`H-003` instances, **B-02 mints `H-013`**; 5 bundles kept below the line with
  reasons
- **Why:** a segment is not an answer — each situation is a separate go-to-market bet; the gate needs
  real rejects, so a mass-audience bundle was composed to fail
- **Trigger:** Step 5 pass, section `#market-bundles`; `H-013` seeded to `registers/hypotheses.md`
