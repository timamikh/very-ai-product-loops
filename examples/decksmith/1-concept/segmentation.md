---
node_type: worklog
tool: segmentation
step: 1
title: "segmentation — the working"
updated: 2026-08-23
version: 0.1.0
---

# segmentation — the working

_Source of truth for `1-concept.md#segments`; that section is the projection of this file._

## Inputs dispatched from sources {#intake}

_Routed here by `source-intake` from `../sources/`. Each row is a fact the method works from; the
analysis and conclusions are worked below and projected into the artifact section — never here._

| From source | What it gives this method | Value / claim | Captured | Confidence |
|-------------|---------------------------|---------------|----------|------------|
| `../sources/originals/founder-brief.md` | The founder's lead-segment bet | Lead with **salespeople & marketers** — highest frequency × stakes, and usually a **company budget** behind the purchase. | 2026-07-16 | [assumption] |
| `../sources/originals/founder-brief.md` | Who feels the pain | "People who make client-facing decks often (sales, marketing)" regenerate AI output by hand. | 2026-07-16 | [sourced: founder brief] |

## The working

### 1 · Candidate cuts (≥3 on different bases) — and which predicts different needs

| # | Cutting basis | What it predicts | Verdict |
|---|---------------|------------------|---------|
| A | **Job + stakes/context of the deck** — who regularly makes *client-facing, credibility-critical* decks vs internal/throwaway ones | The whole need bundle: client-facing → design polish + editability + on-brand + right story all matter at once; internal decks tolerate ugly | **Chosen** ⚙️ — predicts the need most sharply and is the job the concept is built on |
| B | Role / function (sales · marketing · consultant · founder · teacher) | Some difference, but "marketer" spans both a throwaway internal update and a high-stakes pitch — role blurs the need | Rejected as primary — a facet; used to name segments *within* cut A |
| C | Company size (SMB vs enterprise) | Procurement, brand governance, seat count | Rejected — the org-structure reflex; predicts *how you sell*, not the core need (editable+designed). Least likely to predict need |
| D | Willingness/ability to design (in-house design vs none) | Strength of the pull | Rejected as primary — hard to reach as a group; overlaps cut A |
| E | Buying trigger / cadence (recurring vs one-off decks) | Frequency, repeat usage | Rejected as primary — a facet of cut A (frequency), folded into the ranking grounds |

**Why cut A wins:** the product must deliver editable **and** designed **and** on-brand **and**
well-structured *simultaneously* — that full bundle is demanded only when the deck faces an external
audience with stakes. Cut A isolates exactly the people for whom every axis of the value matters;
the demographic cuts (B, C) split people who share a need or lump people who don't.

### 2 · Segments on cut A (named within, using role as a facet)

- **S1 (lead): sales & marketing professionals producing client-facing decks** — pitches, sales
  proposals, QBRs, campaign/brand decks. **Buyer/user:** often the same person; in larger orgs the
  buyer is a sales-enablement / marketing-ops lead with a team budget, the user is the IC. [assumption]
  **Why it matters:** highest **frequency × stakes**, and usually a **company budget** behind the
  purchase. [assumption] (founder bet) **Reach:** LinkedIn; sales/marketing communities (RevGenius,
  Pavilion, r/sales, marketing Slack/Discord); sales-enablement ecosystems; PLG via
  templates/SEO ("pitch deck template"). [assumption]
- **S2: independent consultants / agencies / freelancers** who build client-facing decks for others.
  **Buyer = user** (self-funded). **Why:** extreme design sensitivity and editability is essential
  (client handoff), frequent work — but smaller per-seat volume and price-sensitive. **Reach:**
  consultant/agency communities, Upwork/Contra, design-adjacent channels. [assumption]
- **S3: startup founders raising / pitching.** **Buyer = user.** **Why:** extreme stakes
  (fundraising), but **bursty / low-frequency** and skews toward done-for-you (a designer or agency).
  **Reach:** accelerators, VC networks, founder communities. [assumption]

Held to three — more early is false precision. All three sit on cut A; role names them apart.

### 3 · Priority ranking — grounds

Grounds per the method: **need-difference × reachability × fit-with-the-moat**. The moat
(`#value-defensibility`) is stated *later in this step*, so on this first pass I rank on the first
two grounds only, mark the order **⚙️**, and will revisit once the moat is set.

| Priority | Segment | Need-difference | Reachability | Decided by |
|----------|---------|-----------------|--------------|------------|
| 1 (lead) | S1 sales & marketing | recurring, high-stakes, on-brand + volume → best fit for a *product* (repeat usage) not a one-off | multiple named channels, PLG-able | **frequency + budget + reachability** |
| 2 | S2 consultants/agencies | sharpest design + editability need (client handoff) | reachable but niche, price-sensitive | need-difference high, but lower volume/willingness at scale |
| 3 | S3 founders | highest stakes but one-shot; skews done-for-you | reachable but bursty | low frequency → weak product fit; kept, not led |

**Lead = S1** ⚙️ — matches the founder's stated bet, and is the only segment whose need *recurs*
often enough to make a self-serve product (rather than a one-off service) the right shape.

*Revisit note (moat fit):* once `#value-defensibility` names the corpus/taste moat, re-check whether
S2 (design-native buyers) is the sharper early proving ground for design quality even if S1 is the
scale bet. Recorded as an open item, not a change to the lead yet.

### 4 · Evidence basis & seeded hypotheses

This segmentation rests on the **founder brief + desk reasoning**, not customer interviews or usage
data — there are none yet. Every segment is `[assumption]`. Candidate hypotheses carried to the
register at step 7:

- **Beachhead viability:** S1 is a reachable beachhead with a recurring, company-budgeted need
  (`type: viability`, `tags: segment`).

## Change log

### 2026-08-23 — confidence-tag grammar normalized
- **From → To:** compound tags (`[sourced, fact — high]`, `[assumption: …]`, bare `[sourced]`) →
  canon grammar (`[sourced: <where>]` / `[assumption]`), qualifiers moved into notes
- **Why:** the tag vocabulary check (lint D2) is promoted to ERROR; the shipped example must model
  the grammar it teaches
- **Trigger:** run-2 hardening — the local model copied the example's compound-tag style

### 2026-08-19 — sources layout migrated
- **From → To:** `../sources/founder-brief.md` → `../sources/originals/founder-brief.md`
- **Why:** reorganized sources layout into originals/ · snapshots/ · access/ subfolders
- **Trigger:** framework 0.10 boundary layer

### 2026-08-16 — segments worked and projected
- **From → To:** intake only → `#segments` worked (5 candidate cuts, 3 segments on cut A, ⚙️ ranking) and projected
- **Why:** Step 1 Act pass on `segmentation`; names the beachhead the rest of the concept leads with
- **Trigger:** Step 1 operating-loop pass, section `#segments`

### 2026-08-16 — created (intake)
- **From → To:** — → founder-brief facts dispatched into the intake block
- **Why:** seed the segmentation worklog with its evidence before the Step 1 Act pass
- **Trigger:** `source-intake` at instance setup
