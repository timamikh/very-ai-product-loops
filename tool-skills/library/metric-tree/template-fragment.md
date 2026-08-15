<!--
  template-fragment: metric-tree → fills {#metric-tree} (Step 4)
  Follow process/CONVENTIONS.md. Node DEFINITIONS live in registers/metric-tree.md and VALUES in
  registers/metrics.csv — this section is the shape + rationale, not a value store. ⚙️ = agent proposal.
-->

## Metric tree {#metric-tree}
_Method: North Star Framework. Nodes live in the metric register (`registers/metric-tree.md` —
definitions; `registers/metrics.csv` — values). This section is the shape + rationale, not a value store._

**North Star:** `M-…` — <formula> · [decision: ⚙️ / approved <who, when>]
_Why this one: leading · value-repeating · strategy-encoding (one line each)._

| Driver | Node | Inputs (nodes) | Instrumentation |
|--------|------|----------------|-----------------|
| acquisition / activation | `M-…` | `M-…` | instrumented / proxy / not-instrumented |
| conversion | … | … | … |
| deepening (strategy axis) | … | … | … |
| retention | `M-…` | … | … |

**Guardrails:** `M-…` — <what must not drop and why>.
**Not instrumented (→ Steps 5–6):** list of nodes + how to close each.

**North Star candidates considered** — including the ones that lost, and on which filter. This is the
most re-litigated decision in the tree; without it the same argument restarts next quarter from a
blank page.

| Candidate | Leading? | Value-repeating? | Strategy-encoding? | Verdict |
|-----------|----------|------------------|--------------------|---------|
| `M-…` | ✅/❌ | ✅/❌ | ✅/❌ | chosen · rejected: <which filter and why> |

**Decided:** <YYYY-MM-DD> · **by:** <who> · **alternatives considered:** <what lost, and why> · ⚙️ if the agent proposed it and the human has not confirmed.
