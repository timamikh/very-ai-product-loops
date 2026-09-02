<!--
  template-fragment: segment-cvp → fills {#market-bundles} (Step 5)
  Follow process/CONVENTIONS.md. ⚙️ = agent proposal awaiting approval.
  One row = one testable go-to-market entry. A row that fails a filter is kept but not staged.
-->

## Market-entry bundles {#market-bundles}

_One row = one testable go-to-market hypothesis: a segment, in a situation, with a pain, met by a
CVP + offer through a channel, proven by a qualified-action signal. Bundles seed the hypothesis
register (`type: desirability`)._

| ID | Segment | Situation (trigger) | Pain (cost of inaction) | CVP (promised result) | Offer (first step) | Channel (where, exactly) | Signal · tier | Readiness | `H-…` | Confidence |
|----|---------|---------------------|-------------------------|-----------------------|--------------------|--------------------------|---------------|-----------|-------|------------|
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

**Test-readiness score** — ready bundles only, 1 · 3 · 5 per criterion, sum 5–25. Top 3–5 are staged.
A criterion that cannot be judged is `— to clarify —`, never a 3. Scores are ⚙️ until confirmed.

| Bundle | Pain acuteness | Reachability | Deliverability | Willingness to pay | Speed to a signal | Sum | Staged? |
|--------|----------------|--------------|----------------|--------------------|-------------------|-----|---------|
| B-01 | 5 | 3 | 5 | 1 | 5 | 19 | ✅ ⚙️ |

**Cut, and why** — every bundle that did not get staged, kept for the next pass. Without this the
same entry is re-proposed next period and nobody can tell a filter that was applied from one that was
never reached.

| Bundle | Cut at | Reason | Revisit when |
|--------|--------|--------|--------------|
| B-07 | readiness gate — **Find** | no named place this segment is reachable | a partner/community is identified |
| B-04 | score 11 of 25 | slow to a signal (needs a 3-week pilot to learn anything) | the offer can be cut down to a 2-day diagnostic |

<!-- card -->
**Staged for test this period** (top 3–5 by the score above; `prioritization-tactical-plan` then
decides whether they fit the period's capacity and does not re-score them; test designed by
`hypothesis-test-design`): B-…, B-…

**Seeded registers:** each `ready` bundle → hypothesis register (`H-…`, `type: desirability`,
statement = the whole bundle). Decision after test is one of **scale · iterate · reject ·
research** — a bundle without a recorded decision is not tested.
