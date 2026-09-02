---
node_type: card
kind: method
name: channels-expansion
steps: [3]
prerequisites: [segments, uvp]
reads: [section:segments, section:uvp-cpv, section:pricing, register:hypotheses, register:risks, source:kb, source:research]
writes: [worklog, section:channels-expansion, register:hypotheses, register:risks]
opinionated: false
method_basis: "Bullseye framework (Traction, Weinberg/Mares) + GTM-motion choice + expansion-path thinking"
evidence_standard: external-sources
volume_rule: "≥8 candidate channels across ≥3 channel-type categories before any ring is assigned"
selection_rule: "reach × cost-to-test × testability (1/3/5); inner ring = the 3 highest, tested now"
rejects_shown: required
status: draft
version: 0.3.2
updated: 2026-09-02
---
# Channels & Expansion

Rank the **acquisition / communication channels** to test now, and lay out the **expansion path**
— the next segments, markets, and geographies. Fills `{#channels-expansion}`.

**Method basis.** Weinberg & Mares' Bullseye: brainstorm across all channel types, rank into
outer/middle/inner rings, then run cheap tests on the promising few before committing. Paired with
expansion-path thinking: sequence the segments/markets we grow into once the first channel works.

## When to apply
- Step 3, once segments and the UVP are set (a channel carries a message to a segment).
- When a channel saturates or a new segment/market comes into scope.

## Prerequisites
- **Segments** — who each channel must reach. *Missing → run `segmentation`.*
- **UVP** — the message the channel carries. *Missing → run `uvp-cpv`.*

## How to do it
1. **Brainstorm the full list — at least 8 candidates across at least 3 channel-type categories**
   (e.g. content/SEO · paid · communities · partnerships/resellers · outbound · events · marketplaces
   · existing-base motions). Don't pre-filter to what's familiar: the ring model does nothing if the
   only candidates are the two you already run. Fewer than 8, or all from one category, means the
   brainstorm has not happened yet.
2. **Score, then rank into rings.** Score each candidate **1 · 3 · 5** on **reach** (how many of this
   exact segment sit there), **cost to test** (what one honest test costs, inverted — cheap scores
   high), and **testability** (can we read a signal in days, not a quarter). The three highest go to
   the **inner ring** (test now); the next tier is **middle** (promising, revisit); the rest are
   **outer** — kept with the reason they lost, never deleted. **Source only the inner ring:** each
   of the three inner-ring channels gets **at most one sourced reach claim**, per
   [`../references/evidence-standards.md`](../references/evidence-standards.md); middle- and
   outer-ring reach stays `[assumption]` **by design** — sourcing a channel you will not test is
   research with no read. A channel already running takes its `state` from a filed channel report
   (`source:kb`), never from intention.
3. **Choose the GTM motion — how this segment buys.** `product-led` (self-serve: try → buy) ·
   `sales-led` (a human sells: demo → contract) · `partner-led` (someone else's channel sells) ·
   `community-led` (adoption spreads through a shared space). The economics decide, not taste:
   the price per account must cover the cost of the motion's touch — a $30/mo tier cannot fund a
   sales call, a $50k contract will not close self-serve (read `{#pricing}` if it exists). Then
   check the inner ring against the motion: a channel that cannot start the motion's first step is
   a mis-fit however well it scored — record the conflict, don't silently re-rank. The motion is a
   choice the whole plan inherits: Step-5 bundles (`segment-cvp` offers) and Step-6 activities are
   staged inside it.
4. **Define a measurable test per inner-ring channel.** For each, state the metric, the cost, and
   the success threshold *before* running it. A channel you can't measure isn't a test.
5. **Keep channel separate from message.** The channel is *where* you reach them; the UVP is
   *what* you say. Name both, don't conflate them.
6. **Map the expansion path.** Sequence the next segments / markets / geographies and the
   trigger that unlocks each (e.g. "expand to segment B once channel X hits CAC < …").
7. **Seed registers.** Channel bets → `H-…`; expansion or dependency risks (saturation,
   regulatory, localization) → `R-…`.

## Anti-patterns
- **All channels at once.** Spreading thin instead of testing the inner ring first.
- **Sourcing the outer ring.** Reach evidence gathered for channels nobody will test this period.
- **No way to measure.** A channel with no metric or threshold — spend with no read.
- **Channel = message.** Confusing the medium with the value proposition it carries.
- **Expansion with no trigger.** A wish-list of markets with nothing gating the next step.

## Worklog & projection
Worklog: `3-strategy/channels-expansion.md` — the ≥8 candidates scored and ringed with every loser's reason, one sourced reach claim per inner-ring channel (the other rings `[assumption]`), the GTM motion with its price-vs-touch reasoning and coherence check, the measurable test per inner-ring channel, the expansion path with its triggers. Projects `{#channels-expansion}`; face: the **Channel read** line, via [`template-fragment.md`](template-fragment.md). Path form, primary/contributing and revisit rules: [`worklog-resolution.md`](../../../process/reference/worklog-resolution.md).

## Output
Projects `{#channels-expansion}` via [`template-fragment.md`](template-fragment.md) from the worklog;
inputs via [`questions.yaml`](questions.yaml).
