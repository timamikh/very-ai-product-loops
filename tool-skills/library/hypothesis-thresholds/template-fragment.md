<!--
  template-fragment: hypothesis-thresholds → fills {#global-hypotheses}
  Follow process/CONVENTIONS.md. ⚙️ = agent proposal awaiting approval.
-->

## Global hypotheses {#global-hypotheses}

**Quantified bets** — one row per `H-…` carried from `3-strategy.md#bets`. Each bar is read against
an existing `M-…` node from the metric tree, never a number invented for the test. The gap between
success and failure is the conscious inconclusive zone.

<!-- card -->
**Bars read:** <one sentence — how many bets now carry both bars against a node, the widest inconclusive
zone and why it is that wide, and any bet still without a node>.

| Bet (what it claims) | `H-…` | Metric node (`M-…`) | Success threshold | Failure threshold | Why these numbers | Confidence |
|----------------------|-------|---------------------|-------------------|-------------------|-------------------|------------|
| <the strategy bet, in one line> | H-… | M-… | ≥ … | < … | <where each bar comes from: economics / benchmark / ambition> | [assumption] |

_Thresholds set here are the single source of truth — Step 5's test design (`hypothesis-test-design`)
references them and never re-decides them. A bet whose metric node doesn't exist yet is a gap for
`metric-tree`, flagged as `— to clarify —`, not a bespoke number._

**Seeded registers:** each `H-…` → hypothesis register (metric node link, success bar, failure bar,
rationale), ready for Step 5 to attach the smallest sufficient test.

**Decided:** <!--d:date--> <YYYY-MM-DD> · **by:** <!--d:by--> <who — prefix ⚙️ while unconfirmed> ·
**alternatives considered:** <!--d:alts--> <the bar values weighed and not taken, and why these —
never a bare "none">
