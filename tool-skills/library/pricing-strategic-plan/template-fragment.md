<!--
  template-fragment: pricing-strategic-plan → re-projects {#pricing} (the Step-3 section, revisited at
  Step 4 against unit economics). Same form as pricing-strategy's — one section, one form: the value
  metric, the tiers, the anchor table and the Decided line travel with the re-projection; the margin
  revisit block is what this pass adds. Re-projection drops the section's confirmed: marker.
  Follow process/CONVENTIONS.md. ⚙️ = agent proposal awaiting approval.
-->

## Pricing & Packaging {#pricing}

_What we charge and how we package it — anchored to value vs the alternative, not to cost. Decided at
Step 3 (`pricing-strategy`); this Step-4 revisit reads the decision against unit economics and either
confirms it or proposes a change — never re-decides it silently._

**Value metric:** … (as decided at Step 3 — restated verbatim, tags carried) [sourced: 3-strategy/pricing-strategy.md | assumption]

**Packaging (tiers & fences)**

| Tier | For which segment | Included | Fence (why this segment picks it) | Price point | Model | Confidence |
|------|-------------------|----------|-----------------------------------|-------------|-------|------------|
| … (good) | … | … | … | … $/… | subscription / usage / hybrid / one-off | [assumption] |
| … (better) | … | … | … | … | … | [assumption] |
| … (best) | … | … | … | … | … | [assumption] |

**Anchor to the alternative** _(numbers in the buyer's currency per the value metric — a price that
cannot be placed on the scale next to ours is `— to clarify —`, not a prose cell)_

| Segment | Next-best alternative (what they'd pay/do) | Their price | Our price | Value gap that justifies the delta | Confidence |
|---------|--------------------------------------------|-------------|-----------|------------------------------------|------------|
| … | … | … | … | … | [assumption] |

**Margin revisit (Step 4)** — the decision above read against `{#unit-economics}`, per tier:

| Tier | Price | Contribution margin (per payer) | Inference COGS (per payer) | Fence caps usage-cost? | Read |
|------|-------|--------------------------------|----------------------------|------------------------|------|
| … | … | … $/mo · … % | … $/mo | yes / no / partially | clears / thin / underwater |

**Free-tier burn:** … $/mo at current volume · converts at … % · funded by paid margin? yes / no.

**Verdict:** **holds** — which margins clear, under which assumptions: … · **or ⚙️ proposed change** —
<new price point / moved fence / usage cap / re-metered value metric> · why the margin forces it: …
_(a proposal re-opens the Step-3 decision for the human and flags `financial-model`'s revenue lines)._

**Assumptions the verdict rests on:** … → each margin-critical one seeds `H-…` (`type: viability`).

<!-- card -->
**Price stance:** <one sentence — the price point per value metric, the anchor it stands against, and
the margin verdict (holds / ⚙️ change proposed) — the same slot `pricing-strategy` declares>.

**Seeded registers:** margin-critical assumptions → hypothesis register (`H-…`, `type: viability`).

**Decided:** <!--d:date--> <the Step-3 decision date on *holds*; the date the change is confirmed on a
change> · **by:** <!--d:by--> <who — ⚙️ while a proposed change is unconfirmed> · **alternatives
considered:** <!--d:alts--> <the Step-3 alternatives carried verbatim, plus the price the margin check
would have forced and why it was or was not taken — never a bare "none">
