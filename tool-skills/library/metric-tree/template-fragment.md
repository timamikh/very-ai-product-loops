<!--
  template-fragment: metric-tree → fills {#metric-tree} (Step 4)
  Follow process/CONVENTIONS.md. Node DEFINITIONS live in registers/metric-tree.md and VALUES in
  registers/metrics.csv — this section is the shape + rationale, not a value store. ⚙️ = agent proposal.
-->

## Metric tree {#metric-tree}
_Method: North Star Framework. Nodes live in the metric register (`registers/metric-tree.md` —
definitions; `registers/metrics.csv` — values). This section is the shape + rationale, not a value store._

<!-- card -->
**North Star:** `M-…` — <formula> · [decision: ⚙️ / approved <who, when>]
_Why this one: leading · value-repeating · strategy-encoding (one line each)._

| Driver | Node | Inputs (nodes) | Instrumentation |
|--------|------|----------------|-----------------|
| activation | `M-…` | `M-…` | instrumented / proxy / not-instrumented |
| revenue | … | … | … |
| engagement | … | … | … |
| retention | `M-…` | … | … |

_The **Driver** cell carries exactly one family token — `acquisition · activation · engagement ·
retention · referral · revenue · quality · cost` — the metric's role in the growth loop (AARRR, plus
the behavioural `engagement`, product-health `quality` and COGS `cost` families that AARRR has no slot
for). One token, read literally onto the console's family grouping; a qualifier ("proves the concept",
"risk #1") lives in the node's rationale or the worklog, never compounded into the cell. Cohorts and
funnels are **views** of these families, not families — a cohort is retention read by join period, a
funnel is acquisition→revenue in order; neither is a driver token._

**Not instrumented (→ Steps 5–6):** nodes + how to close each — `instrumentation-plan`'s per-surface
status (`{#architecture-instrumentation}`) projected onto the nodes that read from those surfaces.

**North Star candidates considered** — including the ones that lost, and on which filter. This is the
most re-litigated decision in the tree; without it the same argument restarts next quarter from a
blank page.

| Candidate | Leading? | Value-repeating? | Strategy-encoding? | Verdict |
|-----------|----------|------------------|--------------------|---------|
| `M-…` | ✅/❌ | ✅/❌ | ✅/❌ | chosen · rejected: <which filter and why> |

**Decided:** <!--d:date--> <YYYY-MM-DD> · **by:** <!--d:by--> <who — prefix ⚙️ while unconfirmed> ·
**alternatives considered:** <!--d:alts--> <one alternative weighed and why it lost, or what makes
the choice forced — a bare "none" is a defect>
