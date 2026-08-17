---
node_type: worklog
tool: hypothesis-thresholds
step: 4
title: "hypothesis thresholds — the working"
updated: 2026-08-16
version: 0.1.0
---

# hypothesis thresholds — the working

_Source of truth for `4-strategic-plan.md#global-hypotheses`. Takes each bet carried from
`3-strategy.md#bets` and binds it to an **existing** `M-…` node, then sets a **success bar** and a
**failure bar** read against that node — never a number invented for the test. The gap between the
bars is a **conscious inconclusive zone**, stated on purpose. Bars set here are the **single source
of truth**; Step-5 `hypothesis-test-design` sizes the smallest sufficient test to reach them and
**never re-decides them**. Upserted into the same `registers/hypotheses.md` rows (`test` column)._

## 1 · The seven bets, bound to nodes with bars

| `H-…` | Bet (one line) | Node (`M-…`) | Success | Failure | Inconclusive zone | Provenance of the numbers |
|-------|----------------|--------------|---------|---------|-------------------|---------------------------|
| H-001 | Engine does editable-AND-designed **at scale** (the enabler) | `M-design-acceptance` | ≥ **70%** kept without a full restyle | < **40%** | 40–70% (wide) | ambition-anchored: below ~40% the restyle tax is *not* removed (the whole wedge fails `H-003`); ≥70% = "designed enough" clears table stakes. Wide zone = feasibility genuinely unproven while the corpus matures. Node is proxy-only today (`R-012`). |
| H-003 | S1 **switches** from "Gamma/Canva + manual rebuild" | `M-w4-retention` | ≥ **30%** week-4 value-export retention, curve flattening | < **10%** | 10–30% (wide) | benchmark-anchored: 30% floor = the `strategic-targets` commitment (a flattening core is the fit signal); <10% = no core, the switch didn't stick. Wide zone: retention is censored pre-launch. |
| H-006 | S1 US is a **reachable, budgeted** beachhead | `M-activated` | meets the **base** activation ramp (→ ~120 new paying accts/mo by mo-12; `financial-model` §3) | below the **conservative** ramp (~stalls under ~40/mo) | conservative–base band | model-anchored: reachability shows as activated accounts flowing at the base scenario. Shares evidence with `M-cac` (`H-011`) — reach that costs too much isn't reach. |
| H-007 | Taste corpus + founder credibility is a **compounding** moat | `M-design-acceptance` (trajectory proxy) | acceptance edge **holds or widens** as corpus + rivals grow | edge **flat/declining** as rivals match | — (trajectory, not a single-shot bar) | **trajectory bet** — no one-readout bar; the proxy is design-acceptance *sustained over time* vs a matching competitor. Proxy-only (`R-012`); a true read needs the edit-behaviour loop built. |
| H-010 | S1 **pays a premium** (~$40/seat/mo) for editable-AND-designed | `M-paid-conv` | ≥ **8%** trial→paid at the premium price | < **3%** | 3–8% | economics-anchored: `strategic-targets` commits ≥8% at premium for the model to hold; <3% = discounting forced, `R-011` fires. Zone = "premium works but thin, revisit price." |
| H-011 | Founder-led community reaches S1 at **PLG-viable CAC** | `M-cac` | ≤ **$150** blended / payback ≤ ~5 mo | > **$300** (the paid-blend line) / payback > ~14 mo | $150–$300 | economics-anchored to `unit-economics` payback math. **CAC inputs are directional (report-mill proxy) — bars provisional until an own-funnel read exists: `— to clarify —`.** $300 trigger twins `R-008`. |
| H-012 | Wedge converts to a **durable moat before** the export gap closes | `M-w4-retention` (trajectory proxy) + brand-kit adoption | retention + lock-in signals **rise before** an incumbent ships native-export parity | incumbent parity ships **first**, or lock-in signals flat | — (trajectory + timing gate) | **trajectory/timing bet** — not a single metric crossing a line but a *race*: the proxy is retention/lock-in rising against a dated external event. Twins `R-007`. Instrumentation to see it is itself the `R-012` gap. |

## 2 · Why two of the seven have no single-shot bar (kept, not hidden)

`H-007` and `H-012` are **trajectory bets**: they resolve over time against a moving competitor, not
at one readout. Forcing a single number on them would be false precision. Each is bound to a **proxy
node** (`M-design-acceptance`, `M-w4-retention`) read as a *slope*, with the failure condition being
an external event (a rival matches / ships parity). Both depend on the `R-012` instrumentation being
built before the slope is even observable — flagged, not papered over.

## 3 · Boundary held with Step 5

The bars above are the source of truth. Step-5 `hypothesis-test-design` will **reference** them and
size the smallest sufficient test to reach each bar — it will **not** re-decide a bar. If a bar
proves wrong, the fix is a ⚙️ change *here* (and in the register), visible in this change log — never
a quiet adjustment inside a test design.

## Change log

### 2026-08-16 — thresholds set and projected; register upserted
- **From → To:** the 7 bets from `3-strategy.md#bets` (no bars) → each bound to an existing `M-…`
  node with a success bar, a failure bar, and a stated inconclusive zone; `H-007`/`H-012` kept as
  trajectory bets (proxy slope + external-event failure, no single-shot bar); `H-011`'s bars flagged
  provisional (`— to clarify —`) on directional CAC data
- **Why:** Step 4 quantifies the strategy's bets before any spend/build, pre-registered so no result
  gets spun; the bars become the single source of truth Step 5's test design reads
- **Trigger:** Step 4 pass, section `#global-hypotheses`; upserted into `registers/hypotheses.md`
  (`test` column, each `H-…`)
