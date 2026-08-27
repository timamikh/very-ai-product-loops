<!--
  template-fragment: pre-mortem → fills {#product-risks} (Step 3)
  Surface & triage only — mitigation/owner/trigger belong to Step 4's risk-mitigation,
  which extends these same R- register entries.
  Follow process/CONVENTIONS.md. ⚙️ = agent proposal awaiting approval.
-->

## Product Risks {#product-risks}
_Pre-mortem: it's 12 months out and the chosen strategy failed — why? Cover execution & key-person
risks, not only external ones. Pull existing risks from the R- register (e.g. `cjm-strategy`'s
journey risks) before inventing new ones._

**Carried risks — light triage** (choices are being made; mitigations don't exist yet — they are
assigned at Step 4 by `risk-mitigation`, on these same register entries):

| ID | Risk (concrete failure story) | Category | Likelihood | Impact | Confidence |
|----|-------------------------------|----------|------------|--------|------------|
| R-… | … | market / product / execution / … (key-person → execution) | H/M/L | H/M/L | [assumption] |

_Ranked by likelihood × impact on the 5/3/1 backing (H=5 · M=3 · L=1). Likelihood and Impact cells
carry exactly `H`, `M` or `L` — one letter, no prose: the cell is read literally onto a 2×2, and a
hedged cell lands nowhere. Each carried risk is upserted into the R- register with `status: open` —
handed to Step 4 unmanaged, on purpose._

<!-- card -->
**Death read:** <one sentence — the single most probable cause of death (its R-…), the quadrant it
sits in (likelihood × impact), and whether anything in the chosen strategy currently answers it —
"nothing does" is a legal and load-bearing answer>.

**Disposition of every risk surfaced** — including the ones not carried. A risk that simply fails to
reappear in the next table is indistinguishable from one nobody raised, and the pre-mortem's whole
value is that somebody did.

| Risk | P × I | Disposition | Reason |
|------|-------|-------------|--------|
| … | H×M | carried · parked · dropped | … |

**Decided:** <!--d:date--> <YYYY-MM-DD> · **by:** <!--d:by--> <who — prefix ⚙️ while the agent's
proposal is unconfirmed> · **alternatives considered:** <!--d:alts--> <at least one alternative
actually weighed and why it lost — or what makes the choice forced; a bare "none" is a defect.
Weighed none? Order a refutation — `operations/orchestration` → *The two lenses of a `verify`*>
