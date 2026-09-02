<!--
  template-fragment: product-surface → fills {#product-surface}
  Follow process/CONVENTIONS.md. ⚙️ = agent proposal.
-->

## Product surface {#product-surface}

| Surface | Purpose | Instrumentation (what/where data comes from) | Confidence |
|---------|---------|----------------------------------------------|------------|
| e.g. Landing (`S-…`) | acquisition | visits, signups (analytics) | [assumption] |
| e.g. Reactivation email (`S-…`) | retention | opens, clicks, return (email + analytics) — return: — to clarify — | [assumption] |
| e.g. Admin panel (`S-…`) | ops + data | usage, revenue exports | [assumption] |

_A gap is written into the instrumentation cell as `— to clarify —`, never smoothed; the surface's
type (landing · mailing · admin · in-product · integration) lives on its `S-…` register row._

**Behavior-study tools:** … (analytics / session capture / surveys / funnels)
**Infra implications (→ Step 4 costs):** …

<!-- card -->
**Surface read:** <one sentence — where the product meets the user first, and the widest
instrumentation gap (the surface we own but cannot see into)>.

**Decided:** <!--d:date--> <YYYY-MM-DD> · **by:** <!--d:by--> <who — prefix ⚙️ while unconfirmed> ·
**alternatives considered:** <!--d:alts--> <one alternative weighed and why it lost, or what makes
the choice forced — a bare "none" is a defect>
