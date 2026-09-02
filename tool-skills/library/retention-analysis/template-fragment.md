<!--
  template-fragment: retention-analysis → fills {#retention} (Step 4)
  Follow process/CONVENTIONS.md. ⚙️ = agent proposal awaiting approval.
  Readings themselves go to registers/metrics.csv (dated rows); this section is the read + drivers.
-->

## Retention {#retention}

_Does value repeat? The cohort curve, its flattening floor, the retained core, and the engagement
loop. Supplies the retention/churn input to `unit-economics` (LTV) and `financial-model`._

**"Active" definition:** what counts as a retained active action, and the natural frequency
(daily / weekly / monthly). … [sourced: …]

**Observation window:** how long after joining the outcome becomes countable — and therefore who is
**censored** at each period. Cells below are read over the observed only. … [sourced: …]

**Cohort retention curve** (`n` = observed at that period, never the whole cohort; `—` = not
observable yet)

| Cohort (join period) | Cohort n | P1 | P2 | P3 | P6 | P12 | Flattens at | Shape read | Confidence |
|----------------------|----------|----|----|----|----|-----|-------------|------------|------------|
| … | … | …% (n=…) | …% (n=…) | …% (n=…) | — | — | …% floor / decays to 0 | flattening (value recurs) / decaying | [sourced: metrics …] |

**Headline:** <one sentence — does the curve flatten above zero (value recurs) or decay to zero, at what
floor, and for which cohort>. <!-- card -->

**By segment / plan / channel** — the cohort that retains best (often the real target):

| Split | Retained floor | Note | Confidence |
|-------|----------------|------|------------|
| … | …% | … | [sourced: …] |

**Engagement loop (retained core):** trigger → action → reward → investment. … · **Drop-off
point:** where the curve bends down and what those users never reached. · **Resurrection:** the
path back for churned users, if any.

**Fed to economics:** retention/churn → `unit-economics` (LTV) · churn scenario →
`financial-model`. Readings appended to `registers/metrics.csv` against `M-…`.

**Seeded registers:** each driver we'd act on → hypothesis register (`H-…`,
`type: desirability`/`usability` — will *this* bend the curve), tested via `hypothesis-test-design`.
