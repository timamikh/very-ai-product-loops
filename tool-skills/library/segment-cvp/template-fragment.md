<!--
  template-fragment: segment-cvp → fills {#market-bundles} (Step 5)
  Follow process/CONVENTIONS.md. ⚙️ = agent proposal awaiting approval.
  One row = one testable go-to-market entry. A row that fails a filter is kept but not staged.
-->

## Market-entry bundles {#market-bundles}

_One row = one testable go-to-market hypothesis: a segment, in a situation, with a pain, met by a
CVP + offer through a channel, proven by a qualified-action signal. Bundles seed the hypothesis
register (`type: desirability`)._

| ID | Segment | Situation / trigger | Pain (cost of inaction) | CVP (promised result) | Offer (first step) | Channel (where, exactly) | Target signal · tier | Readiness | `H-…` | Confidence |
|----|---------|---------------------|-------------------------|-----------------------|--------------------|--------------------------|----------------------|-----------|-------|------------|
| B-01 | … | … | … | … | demo / diagnostic / trial / pilot | named community / base / partner | e.g. trial request · **strong** | ready / `not-ready: <filter>` | H-… | [assumption] |

**6-filter readiness gate** (a bundle is `ready` only if all pass):

| Bundle | Find (where exactly) | Recognize (self-recognition) | Pain (cost of inaction) | Alternative (today's way) | CVP (concrete result) | Action (signal we'll get) |
|--------|----------------------|------------------------------|-------------------------|---------------------------|-----------------------|---------------------------|
| B-01 | ✅/❌ … | ✅/❌ … | ✅/❌ … | ✅/❌ … | ✅/❌ … | ✅/❌ … |

**Three-things test** (must be true for a staged bundle): from this row we can write ① the ad
message, ② the landing/offer, ③ the sales first-contact script. If not → back to
`segment-pains`/`uvp-cpv`, not staged.

**Signal scale** — weak = click · like · page view (channel diagnostics, not fit) · medium =
lead · registration · outreach reply · diagnostic completed · strong = meeting with a real
decision-maker · trial · price talk · pilot · prepayment · sale.

**Staged for test this period** (top 3–5 by `prioritization`, test designed by
`hypothesis-test-design`): B-…, B-…

**Seeded registers:** each `ready` bundle → hypothesis register (`H-…`, `type: desirability`,
statement = the whole bundle). Decision after test is one of **scale · iterate · reject ·
back-to-research** — a bundle without a recorded decision is not tested.
