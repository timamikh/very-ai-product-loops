<!--
  template-fragment: impact-readout → fills {#item-readouts} (Step 5)
  Read strictly against the expectations pre-registered on the items in 6#must — no post-hoc
  re-goaling; a check-by not reached is `pending`, never skipped. An H-… verdict is cited from
  experiment-readout, never re-judged here.
  Follow process/CONVENTIONS.md. ⚙️ = agent proposal awaiting approval.
-->

## Item readouts {#item-readouts}

_Shipped items of the last period, read against their pre-registered expectations; verdicts flip
the feature register._

<!-- card -->
**Impact read:** <one sentence — of the items shipped, how many confirmed vs missed vs pending, and
the miss that names a section>.

| Item (sprint · №) | Feature | Expected (verbatim) | Fact | Verdict | Estimate: est → actual | Follow-up | Confidence |
|-------------------|---------|---------------------|------|---------|------------------------|-----------|------------|
| S<N> · 1 | `F-…` | `M-…` <baseline → expected> · check-by <…> | <reading> [sourced: metrics.csv] | confirmed / missed / inconclusive / pending | M (~…) → … | missed → names the section/row it invalidates | [sourced: …] |
| S<N> · 3 | `F-…` | closes `R-…` · check-by <…> | `R-…` status: … | … | S → … | … | [sourced: …] |

_An item shipped without a pre-registered expectation gets a row saying exactly that — its impact
can only be narrated, and the gap is the finding. `pending` rows re-read at the next gate._

**Written back:** shipped `F-…` → `state: live` (state and verdict are orthogonal — shipped is
shipped); the verdict lands on the row's `serves` confidence (`[validated: sprint-N, …]` /
`[refuted: sprint-N, …]`). Estimate misses feed the sizing calibration the specs use next sprint.
A `missed` impact bubbles up — it names the section whose assumption it breaks.
