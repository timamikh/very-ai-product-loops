---
node_type: worklog
tool: financial-model
step: 4
title: "financial model — the working"
updated: 2026-08-16
version: 0.1.0
---

# financial model — the working

_Source of truth for `4-strategic-plan.md#financial-model`. A simple driver-based projection off the
metric-tree nodes; churn as a scenario axis; capacity caps first-class. **Pre-launch, no run-rate → an
illustrative shape, not a forecast** — every number `[assumption]`/`⚙️`. At concept-viability the model
is deliberately ~10 lines, 3 scenarios, 12 months (not a spreadsheet empire)._

## 1 · Drivers (from the metric tree; today's value = 0, pre-launch)

| Driver | Node | Base value ⚙️ | Assumption |
|--------|------|---------------|------------|
| New paying accounts / mo | `M-activated`→`M-paid-conv` | ramp 20 → 120 over 12 mo | founder-community + content inner ring; [assumption] |
| Churn / mo | (scenario axis) | **5%** base (3% / 7%) | from `retention-analysis` benchmark |
| ARPPU | `M-arppu` | ~$33/mo | mix assumption |
| COGS / payer | `M-cogs-per-export` (+infra) | ~$3.5/mo | inference trivial |
| CAC (blended) | `M-cac` | ~$150 community → ~$400 if paid leans in | directional |
| Fixed costs / mo | — | ~$40–80k ⚙️ (small team + founder) | [assumption] |

## 2 · Churn honesty + recursion

No instrumented churn → **scenario axis**, never a single constant.
`MRR_{t+1} = MRR_t × (1 − churn) + new_payers × ARPPU`.

## 3 · 12-month shape, 3 scenarios (illustrative)

| Scenario | Churn | Paying accts @ mo-12 ⚙️ | MRR @ mo-12 ⚙️ | Read |
|----------|-------|-------------------------|----------------|------|
| Conservative | 7%/mo | ~400 | ~$13k | churn eats the ramp; retained core thin |
| **Base** ⚙️ | 5%/mo | ~600 | ~$20k | community CAC pays back ~5mo; compounding starts |
| Stretch (activation fixed) | 3%/mo | ~850 | ~$28k | tied to `H-003`/`M-w4-retention` — if the switch sticks |

Numbers are shape, not commitments — the point is the **spread** (churn axis ~2× the outcome), not the
decimals (precision theatre avoided).

## 4 · Capacity ceiling — the founder, not the servers

API compute scales elastically, so **compute is not the cap**. The binding ceilings are human:
- **Founder-community channel saturation** (`R-008`) — the near-zero-CAC engine runs out of warm
  audience; the cap binds when community-sourced new-payers plateau (watch `M-cac` rising).
- **Founder-as-corpus/taste bottleneck** (`R-010`) — curation + design-review throughput caps how
  fast quality (`M-design-acceptance`) scales. This is the real "slot cap" of the model.

Saying *when* the human cap binds (community plateau, ~mo 6–9 ⚙️) is the model's main output, not the
MRR line.

## 5 · Both cost bases → breakeven

Single basis (API compute). Breakeven ≈ fixed_costs ÷ contribution/payer = $60k ÷ $29.5 ≈ **~2,000
paying accounts** ⚙️ — well beyond the 12-month base ramp: **this is a fund-and-prove-fit phase, not a
self-funding one**, consistent with the `concept-viability` status. Honest and expected.

## 6 · Invalidation triggers (→ cadence)

Revisit this model when: actual churn diverges >2pp from the scenario; community CAC rises past ~$300
(the paid-blend line); or trial→paid (`M-paid-conv`) lands outside the WTP threshold band (`H-010`).

## Change log

### 2026-08-16 — financial model worked and projected
- **From → To:** — → driver-based 12-mo projection, 3 churn scenarios (spread ~2×), the human
  capacity ceiling (founder/community, not compute) as the binding cap, breakeven ~2,000 accts
  (fund-to-prove-fit), invalidation triggers
- **Why:** Step 4 ties a projection to the tree so targets can be read off a named scenario; kept an
  illustrative shape because there is no run-rate yet
- **Trigger:** Step 4 pass, section `#financial-model`
