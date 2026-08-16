<!--
  template-fragment: prioritization-tactical-plan → fills {#period-goals} (Step 5)
  Follow process/CONVENTIONS.md. ⚙️ = agent proposal awaiting approval.
-->

## Period Goals {#period-goals}

_Measurable goals for the period, grouped by direction, ranked by contribution to the gate._

**Gate of the period:** … (metric node to move `M-…`, or a Definition of Done) [assumption]
**Capacity (from `resource-check`):** … (people · budget · time) [sourced: tactical-plan#resources]
**Candidates that entered the ranking:** N = …

**Ranking**
| Direction | Goal (measurable) | Contribution to the gate | Score (RICE or ICE) | In the period? | Moves / tests |
|-----------|-------------------|--------------------------|---------------------|----------------|---------------|
| development | … | how it moves the period gate | e.g. RICE 8.4 · [assumption] | yes ⚙️ | M-… / H-… |
| go-to-market | … | … | e.g. ICE 6 · [assumption] | yes ⚙️ | H-… |

_Rank is by gate contribution; the score only aids ordering. A goal with no `M-…`/`H-…` is a cut
candidate. The set is bounded by capacity — if the minimum overflows, cut scope or renegotiate the
gate._

**Cut, and why** — every candidate that entered the ranking and did not make the period, with the
reason. Without this the same goal is re-proposed next period.

| Candidate | Direction | Why cut |
|-----------|-----------|---------|
| … | … | no `M-…`/`H-…` link · over capacity (ranked below the line) · out of period scope · superseded by <goal> |
