<!--
  template-fragment: instrumentation-plan → fills {#architecture-instrumentation}
  Follow process/CONVENTIONS.md. ⚙️ = agent proposal awaiting approval.
-->

## Architecture & instrumentation {#architecture-instrumentation}
_Step 3's `#architecture` + `#product-surface`, refined into one measurability map. One row per
component; every future metric-tree node traces to a row here or carries an explicit gap._

| Component (from architecture / surface) | Instrumentation | What a proxy actually measures | Data it yields | Infra cost driver (↔ unit-economics COGS line) | Confidence |
|-----------------------------------------|-----------------|--------------------------------|----------------|------------------------------------------------|------------|
| … | instrumented / proxy / not-instrumented | <proxy rows only — and where it lies> | <events / measures> | <cost + the COGS line it reconciles with, or a flag> | [assumption] |

**Explicit gaps** — metric needs with no data source (a node wanted, no component emits it):
- `M-…` / <need> → gap: … · `— to clarify —`

**Not-instrumented → Steps 5–6 work items** (first-class output, incl. proxies worth upgrading):
- <component> → <what to instrument, and what it unlocks>

**Reconciliation check:** every infra cost driver above appears as a `unit-economics` COGS line and
vice versa — mismatches flagged, not smoothed.
