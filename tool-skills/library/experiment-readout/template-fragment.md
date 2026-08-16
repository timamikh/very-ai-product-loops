<!--
  template-fragment: experiment-readout → fills {#readouts} (Step 5)
  Follow process/CONVENTIONS.md. ⚙️ = agent proposal awaiting approval.
  Read strictly against the pre-registered rule from {#hypotheses-to-test} — no post-hoc re-thresholding.
-->

## Readouts {#readouts}

_Verdicts of tests that finished this period, read against their pre-registered rules;
signal/decision flow to the hypothesis register._

| `H-…` | Test | Result vs rule | Signal | Decision | Follow-up | Confidence |
|-------|------|----------------|--------|----------|-----------|------------|
| H-… | <the test as designed> | measured … vs rule "≥ … / < …" → `validated` / `refuted` / `inconclusive` [sourced: metrics.csv] | weak / medium / strong | scale / iterate / reject / research | research → named learning item; refuted → names the section it invalidates | [sourced: …] |

_The rule is restated from the design, not reconstructed; the inconclusive zone is exactly as wide
as the design said. A readout with no decision is not finished; a `research` decision must produce a
named learning item for the next period's goals._

**Written back:** each row → hypothesis register (`status`, `signal`, `decision`). A refuted `H-…`
bubbles up — it names the section whose confirmation it invalidates.
