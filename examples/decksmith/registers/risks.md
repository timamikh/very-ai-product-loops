---
node_type: register
register: risks
title: Risk register — Decksmith
updated: 2026-08-16
version: 0.1.0
---

# Risk register

Living risks, born at Step 2 (niche) and refined at 3 (product) / 4 (capability gaps + mitigation) /
5 (period blockers). Never re-authored per step. Schema:
[`process/REGISTERS.md`](../../../process/REGISTERS.md). One `category` per row; cross-cutting themes
go in `tags`. Carried risks are ranked by likelihood × impact on the 5/3/1 tiers.

| ID <!--c:id--> | Description <!--c:description--> | Category <!--c:category--> | Tags <!--c:tags--> | Likelihood <!--c:likelihood--> | Impact <!--c:impact--> | Mitigation <!--c:mitigation--> | Owner <!--c:owner--> | Due <!--c:due--> | Status <!--c:status--> | Source <!--c:source--> |
|----|-------------|----------|------|------------|--------|------------|-------|-----|--------|--------|
| R-001 | Well-funded incumbents accelerating into the space — Gamma (~$2.1B, ~$100M ARR 3× YoY) and Canva (~$42B, B2B ARR ~2×) racing on the same "replace PowerPoint" pitch. | market | rivalry | H | H | Ship the editable+designed wedge in the narrow S1 niche where incumbents are conflicted; don't fight broad | founder ⚙️ | quarterly | mitigating | `2-analysis.md#niche-risks` (competitor-dynamics) |
| R-002 | Bundled substitutes — Microsoft Copilot / Google Gemini put deck-gen inside suites users already pay for ("free, already-here, native"). | market | bundling, substitution | H | H | Position on taste, not price, vs the bundle; target S1 the bundle won't satisfy | acting PO ⚙️ | quarterly | mitigating | `2-analysis.md#niche-risks` (substitutes) |
| R-003 | Low entry barriers — AI deck-gen is cheap to clone; the moat is thin unless the corpus/taste edge (`H-007`) actually holds and shows fast (commoditization). | product | moat, commoditization | H | H | Convert wedge → data + lock-in moat on the `H-012` trajectory; instrument early | founder ⚙️ | quarterly | mitigating | `2-analysis.md#niche-risks` |
| R-004 | Supplier power — generation depends on foundation-model providers; price / rate-limit / access changes hit unit economics and capability. | dependency | model-provider | M | M | Provider-abstraction layer + multi-provider fallback; monitor COGS/export | eng ⚙️ | on provider change | mitigating | `2-analysis.md#niche-risks` |
| R-005 | Monetization trap — the category punishes free-user virality without monetization (Tome, Pitch both died of it); buyers expect a free/bundled option. | financial | monetization | M | H | Paid fences + tight trial from day one; measure `M-paid-conv`; never free-first-unlimited | acting PO ⚙️ | monthly (post-launch) | mitigating | `2-analysis.md#niche-risks` (competitor-dynamics) |
| R-006 | Platform dependency — output targets `.pptx`/`.key`/Slides formats owned by Microsoft/Apple/Google; a format or API change can break the native-export promise. (worklog grades L–M; recorded at L.) | dependency | platform, format | L | M | Export-fidelity test suite across PPT/Keynote versions; watch format/API changes | eng ⚙️ | on Office/macOS release | open | `2-analysis.md#niche-risks` |
| R-007 | Timing / moat-erosion — an incumbent closes the export gap (Gamma/Canva ship real native `.pptx`, or Microsoft bundles it) before the edit-behaviour data loop + brand-kit lock-in take hold, erasing the wedge. Twin of bet `H-012`. | market | timing, moat-erosion | H | H | Race the data-loop + brand-kit lock-in before the gap closes; close `R-012` first | founder ⚙️ | quarterly | mitigating | `3-strategy.md#product-risks` (pre-mortem f2) |
| R-008 | GTM channel doesn't scale — founder-led community distribution saturates past the founder's own audience and CAC explodes. Twin of bet `H-011`. | execution | gtm, channel | M | H | Validate a 2nd inner-ring channel early; don't over-rely on the founder audience; watch `M-cac` | acting PO ⚙️ | monthly | mitigating | `3-strategy.md#product-risks` (pre-mortem f5) |
| R-009 | Taste doesn't travel — the curated corpus produces samey/off-brand decks across diverse content; the "designed" claim fails at scale *even if* `H-001` holds. | product | taste, quality | M | H | Corpus breadth + per-vertical style tests; a design-acceptance gate before scaling | founder / design ⚙️ | design gate + monthly | mitigating | `3-strategy.md#product-risks` (pre-mortem f6) |
| R-010 | Key-person dependency — the strategy leans on the founder's taste/credibility; the founder becomes the moat *and* the bottleneck (bus factor). | execution | key-person | M | M | Codify taste into labelled rubrics (reduce founder-in-loop); document the system; train a 2nd curator | founder ⚙️ | +6 mo | mitigating | `3-strategy.md#product-risks` (pre-mortem f8) |
| R-011 | WTP overestimated — S1 won't pay the premium; forced discounting to bundle/free levels breaks the model. Twin of bet `H-010`. | financial | pricing, wtp | M | H | WTP survey + price test in pilot before scaling; hold premium, measure `M-arppu`/`M-paid-conv` | acting PO ⚙️ | pilot readout | mitigating | `3-strategy.md#product-risks` (pre-mortem f7) |
| R-012 | Instrumentation gap — the design-acceptance / edit-behaviour signal behind the North Star (and the data-loop moat) is only a proxy / not-instrumented; without it the promise can't be measured and the moat can't be built. | execution | instrumentation | M | H | Build the design-acceptance proxy + edit-behaviour capture in the first release; prioritise North-Star instrumentation | eng ⚙️ | launch gate | mitigating | `4-strategic-plan.md#capabilities` (capabilities-systems) |
| R-013 | Corpus IP / licensing — the curated design corpus (the `H-007` moat) could embed scraped or copyrighted client decks; a licensing/copyright challenge would force a corpus rebuild and damage trust. | legal | ip, corpus, brand | M | H | Corpus content licensed or original only (a Period-1 red line); provenance log per corpus item; legal review before scale (trigger: an item's provenance unclear/challenged) | acting PO / legal ⚙️ | before corpus scale | mitigating | `5-tactical-plan.md#guardrails` (guardrails, Period-1 red line 3) |

## Change log

### 2026-08-16 — Step 5 (Period 1): `R-013` born (corpus IP/licensing, from a guardrail red line)
- **From → To:** R-012 → added `R-013` (legal/IP: the design corpus could embed copyrighted client
  decks), surfaced by the Period-1 guardrail red line "corpus content licensed or original only"
- **Why:** the guardrails method logs a red line's breach as a risk-not-to-realize; no existing risk
  covered copyright exposure of the corpus, so it was minted (R-009 is taste-travel, R-004 is the
  model provider — neither is IP/licensing). Other guardrail breaches reused `R-009`/`R-008`/`R-011`/
  `R-005`, **not re-minted**.
- **Trigger:** Step 5 pass, section `#guardrails`; seeded to this register by `guardrails`

### 2026-08-16 — Step 4: `R-012` born (capability gap) + all carried risks made managed
- **From → To:** added `R-012` (execution: instrumentation gap behind the North Star + data-loop
  moat), seeded by `capabilities-systems`. `risk-mitigation` then upserted **mitigation · owner ·
  trigger · due · status** into every carried row (R-001…R-012): 11 → `mitigating`, 1 → `open`
  (R-006 platform, awaiting a format-change trigger; R-006 review on OS/Office release).
- **Why:** Step 4 makes each risk actionable before the plan is signed; capability gaps that have no
  close date become tracked execution risks. Scores travel from the Step-3 triage — not re-scored.
- **Trigger:** Step 4 pass — `#capabilities` (`R-012`) + `#risk-mitigation` (owner/trigger/due upsert)

### 2026-08-16 — R-007…R-011 born (Step 3 pre-mortem), open & unmanaged
- **From → To:** R-006 → added `R-007` (timing/moat-erosion), `R-008` (GTM channel doesn't scale),
  `R-009` (taste doesn't travel), `R-010` (key-person dependency), `R-011` (WTP overestimated)
- **Why:** the Step-3 pre-mortem surfaced 11 failure modes against the *chosen* strategy; 5 were new
  and carried, 5 folded onto existing entries — `H-001` (the core feasibility bet — a hypothesis, not
  a risk), `R-002`, `R-004`, `R-005`, `R-006` (re-confirmed, **not duplicated**) — 1 parked (inverse
  of `H-005`). Carried set ranked by likelihood × impact. (`R-001` was not a target of any surfaced
  failure mode.)
- **Trigger:** Step 3 pass, section `#product-risks`. Mitigation/owner/trigger deliberately **left
  empty** — handed to Step-4 `risk-mitigation`, which extends these same entries.

### 2026-08-16 — R-001…R-006 born (Step 2 niche risks)
- **From → To:** empty → `R-001` (rivalry: funded incumbents), `R-002` (bundling substitute),
  `R-003` (low entry barriers / thin moat), `R-004` (model-supplier power), `R-005` (monetization
  trap), `R-006` (platform/format dependency)
- **Why:** the Step 2 light-Five-Forces read turns each structural niche risk into a tracked entry;
  likelihood × impact on the 5/3/1 tiers orders them (R-001/R-002/R-003 are the H×H top)
- **Trigger:** Step 2 operating-loop pass, section `#niche-risks`; evidence from `loops-research`

### 2026-08-16 — created
- **From → To:** — → empty register scaffolded
- **Why:** instance setup; risks are born in the Step 2 pass, not at scaffold time
- **Trigger:** `product-setup` scaffolding of the Decksmith sample instance
