<!--
  template-fragment: instrumentation-plan → fills {#architecture-instrumentation}
  Follow process/CONVENTIONS.md. ⚙️ = agent proposal awaiting approval.
-->

## Architecture & instrumentation {#architecture-instrumentation}
_Step 3's `#architecture` + `#product-surface`, refined into one measurability map. One row per
component; every future metric-tree node traces to a row here or carries an explicit gap._

<!-- card -->
**Measurability read:** <one sentence — how much of the surface is instrumented today (n of N
components), the widest gap, and the infra cost driver that dominates>.

| Surface / component | Instrumentation (instrumented / proxy / not) | Data it produces | Infra cost driver (↔ unit-economics COGS line) | Confidence |
|---------------------|----------------------------------------------|------------------|------------------------------------------------|------------|
| <from architecture / surface> | instrumented / proxy / not-instrumented | <events / measures> | <cost + the COGS line it reconciles with, or a flag> | [assumption] |

**Proxies — what each actually measures** (proxy rows only):

| Component | Proxy | What it actually measures | Where it lies |
|-----------|-------|---------------------------|---------------|
| … | … | … | … |

**Explicit gaps** — metric needs with no data source (a node wanted, no component emits it):
- `M-…` / <need> → gap: … · `— to clarify —`

**Not-instrumented → Steps 5–6 work items** (first-class output, incl. proxies worth upgrading):
- <component> → <what to instrument, and what it unlocks>

**Reconciliation check:** every infra cost driver above appears as a `unit-economics` COGS line and
vice versa — mismatches flagged, not smoothed.

**Decided:** <!--d:date--> <YYYY-MM-DD> · **by:** <!--d:by--> <who — prefix ⚙️ while unconfirmed> ·
**alternatives considered:** <!--d:alts--> <one alternative weighed and why it lost, or what makes
the choice forced — a bare "none" is a defect>
