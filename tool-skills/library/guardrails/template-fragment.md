<!--
  template-fragment: guardrails → fills {#guardrails}
  Follow process/CONVENTIONS.md.
-->

## Guardrails {#guardrails}

<!-- card -->
**Guardrail read:** <one sentence — the protected metric most exposed to this period's goals, its
floor or ceiling, and where it is watched>.

**Protected metrics** (must not cross the threshold while hitting goals):

| Guardrail (`M-…`) | Must stay | Red line | Why | Confidence |
|-------------------|-----------|----------|-----|------------|
| e.g. `M-retention-d30` | ≥ 35 % | < 30 % for two weeks | the goal's acquisition push must not buy churn | [sourced: …] |

_**Must stay** is the floor / ceiling the metric holds; the **red line** is the crossing that stops the
work. Qualitative red lines ("never a dark pattern") take a row with `—` in the metric cell._

**Watched where / how often:** <guardrail → dashboard or query · cadence>, one line each.

**Breach = risk:** logged as `R-…`.

**Considered, not guardrailed** — every break-category checked that did not become a guardrail. A
category nobody looked at and one that was looked at and cleared are indistinguishable afterwards.

| Category | What was checked | Why not a guardrail |
|----------|------------------|---------------------|
| retention · unit economics · CAC · quality · brand/trust · support load · churn | … | no metric node yet (→ instrumentation task) · no plausible mechanism this period · already covered by <other guardrail> |

**Decided:** <!--d:date--> <YYYY-MM-DD> · **by:** <!--d:by--> <who — prefix ⚙️ while unconfirmed> ·
**alternatives considered:** <!--d:alts--> <one alternative weighed and why it lost, or what makes
the choice forced — a bare "none" is a defect>
