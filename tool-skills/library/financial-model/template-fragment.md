<!--
  template-fragment: financial-model → fills {#financial-model} (Step 4)
  Follow process/CONVENTIONS.md. ⚙️ = agent proposal awaiting approval.
-->

## Financial model {#financial-model}
_Method: driver-based, off the metric-tree nodes. Horizon 12 mo, monthly compounding._

**Drivers** — today's value from `metrics.csv`, the projected assumption, its tag:

| Driver | Base | Assumption | Confidence |
|--------|------|------------|------------|
| new payers / mo (`M-…`) | … | … | [sourced: metrics.csv] / [assumption] |
| churn % / mo | … | scenario axis: X / Y / Z % ⚙️ | [assumption] |
| ARPPU (`M-…`) | … | … | [sourced: …] |
| COGS per usage · fixed costs | … | … | [assumption] |

**Scenarios** (12 months, monthly compounding):

| Scenario | Assumptions | MRR at 12 mo | When it hits a cap | Profit (both bases) |
|----------|-------------|--------------|--------------------|---------------------|
| Conservative | | | | |
| Base ⚙️ | | | | |
| Stretch (⟵ hypothesis `H-…`) | | | | |

**Capacity limits:** <slot / registration / compute caps and the month they bind>.

**Break-even:** operational … $/mo · honest … $/mo (now: …) — <one clause: which scenario reaches it and
when, or that none does inside the horizon>. <!-- card -->

**Revisit triggers:** actuals diverge from base by >X% for two months running → revisit Step 4.
