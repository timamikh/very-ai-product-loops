---
node_type: worklog
tool: unit-economics
step: 4
title: "unit economics — the working"
updated: 2026-08-16
version: 0.1.0
---

# unit economics — the working

_Source of truth for `4-strategic-plan.md#unit-economics`. Contribution margin with **LLM inference
as an explicit COGS line**. **Single basis** — Decksmith runs on third-party API compute (no own
GPUs), so operational and honest collapse to one (the dual basis is own-compute only; stated per the
skill). Product is pre-launch → every figure is modelled `[assumption]`/`⚙️`, with inference and
churn anchored to the Step-4 research digest (as_of 2026-08-16). Also carries the
`pricing-strategic-plan` margin verdict._

## 0 · Window

There is no billing history. The window is a **modelled month** — one steady-state month at the
pricing of `3-strategy.md#pricing`. All figures are per-payer-per-month unless noted.

## 1 · Revenue per paying account (blended + by tariff)

From `3#pricing` (⚙️ price points): Solo ~$24/mo · Team ~$45/seat/mo · Studio ~$90/seat/mo.
**Mix assumption ⚙️** (early beachhead, weighted to Solo/Team): 60% Solo · 35% Team · 5% Studio.
Blended ARPPU = 0.6×24 + 0.35×45 + 0.05×90 = 14.4 + 15.75 + 4.5 = **~$33/mo** `[assumption: mix]`
→ `M-arppu`. (Annual-billing discounts would trim this ~10–15%; ignored at this precision.)

## 2 · COGS per paying account (LLM inference explicit)

**Inference:** anchor **~$0.17/deck** (GPT-4.1 base; band $0.07–$0.42) `[sourced: OpenAI pricing +
token-budget assumption, as_of 2026-08-16]`. Allocation rule `[assumption]`: **by decks generated per
account** (usage share), *not* headcount — and the distribution is **power-law** (agencies generate
many; the anti-pattern is averaging inference over users when the top tail eats the budget).

| Item | Value | Note |
|------|-------|------|
| Decks / active payer / mo ⚙️ | ~10 (blended); power-user tail 30–50 | assumption; the tail is the cost risk, not the mean |
| Inference COGS / payer / mo | ~10 × $0.17 = **~$1.70** (tail: 40 × $0.30 = ~$12) | → `M-cogs-per-export` |
| Non-inference infra (export/render, storage, analytics, email) | **~$1.50/payer/mo** ⚙️ | [assumption] |
| **Total COGS / payer / mo** | **~$3–4 blended** (tail payer ~$13) | single basis |

## 3 · Contribution margin

Blended: $33 − $3.5 = **~$29.5/payer/mo (~89%)** → `M-contribution`. Even a heavy-usage tail payer
($33 − $13) = ~$20 (~61%). **Finding: at these prices inference is NOT the margin threat** — a $33
subscription dwarfs $0.17/deck. The margin risks are (a) the power-user tail (capped by the Solo
fair-use limit and by Team/Studio pricing), and (b) CAC/payback, below.

## 4 · CAC & payback (per channel)

CAC `[assumption — directional; report-mill sources only, no primary; flagged `— to clarify —` for an
OpenView/KeyBanc primary or own-funnel read]`:

| Channel | CAC ⚙️ | Payback = CAC ÷ ~$29.5 contribution | Read |
|---------|--------|-------------------------------------|------|
| Founder-community / content | **~$150** | ~**5 months** | well under the ≤12-mo gate → supports `H-011` |
| Paid-search blended | **~$400** | ~**14 months** | **breaches** the ≤12-mo payback ceiling → paid must run efficiently or stay secondary (ties `R-008`) |

→ `M-cac`. Payback ceiling **≤12 months** `[sourced: Skok/Bessemer heuristic, as_of 2026-08-16]`.

## 5 · LTV (churn is honest → scenarios, never a constant)

No instrumented churn → LTV as scenarios on the `retention-analysis` axis (contribution basis):

| Churn/mo ⚙️ | Avg lifetime | LTV (≈ $29.5 × life) | LTV/CAC (community $150) | LTV/CAC (paid $400) |
|-------------|--------------|----------------------|-------------------------|---------------------|
| 3% (best) | ~33 mo | ~$975 | 6.5× | 2.4× |
| **5% (base)** | ~20 mo | **~$590** | **3.9×** | 1.5× |
| 7% (worst) | ~14 mo | ~$415 | 2.8× | 1.0× |

Community CAC clears the >3× LTV/CAC rule in base and best; **paid-search is thin-to-underwater** —
the economics say the same thing the channel ring did (community inner, paid a fast-read secondary).

## 6 · Free-tier burn (a COGS line, not marketing dust)

Trial = a few full-export decks (`3#pricing`). Burn ≈ 5 decks × $0.17 = **~$0.85/trial**. At a 10%
trial→paid ⚙️, inference burn to acquire a payer ≈ $8.50 — **negligible**. Note: Tome/Pitch did not
die of *inference* burn but of unmonetised **scale** without conversion — so the R-005 discipline is
**conversion + fences**, not capping inference. This sharpens why `R-005`'s mitigation is monetisation
mechanics, not cost control.

## 7 · `pricing-strategic-plan` verdict — the Step-3 price under the margin

**Decision under test:** value metric per-seat; Solo $24 / Team $45 / Studio $90; premium-above-cluster.
**Per-tier margin:** all three clear **~85–90% contribution** even on the high inference band; no tier
is underwater; the fence (Solo fair-use cap) caps the tail. Free-tier burn negligible (§6).
**Verdict: HOLDS.** Logged, not re-decided. Assumptions it rests on: mix (§1), ~10 decks/payer (§2),
GPT-4.1-class model. The binding viability constraint is **WTP (`H-010`) and CAC (`H-011`), not COGS**
— exactly where the bets already point. No ⚙️ change proposed to `3-strategy.md#pricing`.

## Register

Nodes minted/owned here: `M-arppu`, `M-contribution`, `M-cogs-per-export`, `M-cac` (defined in
`registers/metric-tree.md`). No `metrics.csv` values (pre-launch). Margin-critical assumptions
(decks/payer, mix, churn) are already carried by `H-010`; no duplicate `H-` minted.

## Change log

### 2026-08-16 — unit economics worked and projected (+ pricing verdict)
- **From → To:** — → single-basis contribution model (ARPPU ~$33, COGS ~$3–4, contribution ~89%),
  CAC/payback per channel (community ~5mo, paid ~14mo), LTV scenarios (3/5/7% → 6.5×/3.9×/2.8×
  community), free-tier burn negligible; `pricing-strategic-plan` verdict = **holds**
- **Why:** Step 4 checks whether one customer pays for themselves before scaling; the headline is that
  COGS is trivial and the real constraint is CAC/WTP
- **Trigger:** Step 4 pass, section `#unit-economics` (+ `pricing-strategic-plan` contributing here);
  inference/churn/CAC anchored to the Step-4 `loops-research` digest
