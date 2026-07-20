<!--
  template-fragment: risk-mitigation → fills {#product-risks}
  Follow process/CONVENTIONS.md. ⚙️ = agent proposal awaiting approval.
-->

## Product Risks {#product-risks}
_Pre-mortem: it's 12 months out and the strategy failed — why? Cover execution & key-person risks,
not only external ones. Pull existing risks from the R- register before inventing new ones._

**Step 3 — light triage** (choices are being made; mitigations don't exist yet):

| ID | Risk (concrete failure story) | Category | Likelihood | Impact | Confidence |
|----|-------------------------------|----------|------------|--------|------------|
| R-… | … | market / product / execution / … (key-person → execution) | H/M/L | H/M/L | [assumption] |

**Step 4 — extend each carried risk** with the columns that make it *managed*:

| ID | Score (P×I) | Mitigation | Owner | Trigger (act-now signal) | Status |
|----|-------------|------------|-------|--------------------------|--------|
| R-… | … | … | … | … | open / mitigating / … |

_Ranked by P×I. At Step 4 every carried risk gets an owner and a trigger, or it isn't managed.
Upsert each into the R- register (one row per risk — the Step-4 columns fill in the same register entry)._
