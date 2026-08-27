<!--
  template-fragment: product-surface → fills {#product-surface}
  Follow process/CONVENTIONS.md. ⚙️ = agent proposal.
-->

## Product surface {#product-surface}

| Surface | Type | Purpose | Instrumentation (what we measure + how) | Gap? | Confidence |
|---------|------|---------|-----------------------------------------|------|------------|
| e.g. Landing | landing | acquisition | visits, signups (analytics) | — | [assumption] |
| e.g. Reactivation email | mailing | retention | opens, clicks, return (email + analytics) | — to clarify — | [assumption] |
| e.g. Admin panel | admin | ops + data | usage, revenue exports | — | [assumption] |

**Behavior-study tools:** … (analytics / session capture / surveys / funnels)
**Infra implications (→ Step 4 costs):** …

<!-- card -->
**Surface read:** <one sentence — where the product meets the user first, and the widest
instrumentation gap (the surface we own but cannot see into)>.

**Decided:** <!--d:date--> <YYYY-MM-DD> · **by:** <!--d:by--> <who — prefix ⚙️ while the agent's
proposal is unconfirmed> · **alternatives considered:** <!--d:alts--> <at least one alternative
actually weighed and why it lost — or what makes the choice forced; a bare "none" is a defect.
Weighed none? Order a refutation — `operations/orchestration` → *The two lenses of a `verify`*>
