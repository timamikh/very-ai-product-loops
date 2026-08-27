---
node_type: card
kind: method
name: channels-expansion
steps: [3]
prerequisites: [segments, uvp]
reads: [section:segments, section:uvp-cpv, register:hypotheses, register:risks, source:interview, source:kb, source:research]
writes: [worklog, section:channels-expansion, register:hypotheses, register:risks]
opinionated: false
method_basis: "Bullseye framework (Traction, Weinberg/Mares) + GTM-motion choice + expansion-path thinking"
evidence_standard: external-sources
volume_rule: "≥8 candidate channels across ≥3 channel-type categories before any ring is assigned"
selection_rule: "reach × cost-to-test × testability (1/3/5); inner ring = the 3 highest, tested now"
rejects_shown: required
status: draft
version: 0.3.0
updated: 2026-08-27
---
# Channels & Expansion

Rank the **acquisition / communication channels** to test now, and lay out the **expansion path**
— the next segments, markets, and geographies. Fills `{#channels-expansion}`.

**Method basis.** Weinberg & Mares' Bullseye: brainstorm across all channel types, rank into
outer/middle/inner rings, then run cheap tests on the promising few before committing. Paired with
expansion-path thinking: sequence the segments/markets we grow into once the first channel works.

**No external source, no settled verdict.** This method declares `evidence_standard:
external-sources`: if by pass time nothing external has arrived (no dispatched research, no dated
capture in `sources/`), the section is written as an **explicit gap report** — load-bearing values
`— to clarify —`, each naming the source that would settle it — and the move-5 note names the
missing input. It is never delivered as settled analysis; the linter (check L2) flags a worked
section that shows no `[sourced: …]` and declares no gap.

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
   **outer** — kept with the reason they lost, never deleted. A claim about a channel's reach is an
   external claim: source it per
   [`../references/evidence-standards.md`](../references/evidence-standards.md), or tag it
   `[assumption]` and say so.
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
- **No way to measure.** A channel with no metric or threshold — spend with no read.
- **Channel = message.** Confusing the medium with the value proposition it carries.
- **Expansion with no trigger.** A wish-list of markets with nothing gating the next step.

## Worklog & projection
The working is done in the step's **worklog** `<step-folder>/channels-expansion.md`
(`node_type: worklog`, e.g. `3-strategy/channels-expansion.md`): the full brainstorm (≥8 candidates
across ≥3 channel-type categories), the 1·3·5 reach × cost-to-test × testability scores ranked into
outer / middle / inner rings with every loser kept and its reason, the chosen GTM motion with the
price-vs-touch reasoning and the coherence check against the inner ring, the measurable test (metric,
cost, threshold) per inner-ring channel, and the sequenced expansion path with the trigger gating each
step.
That worklog is the **source of truth**; the artifact section `{#channels-expansion}` is its
**projection** into the fixed shape of [`template-fragment.md`](template-fragment.md) — it holds nothing
the worklog does not, and the step's change-log history lives in the worklog, not the section
(`process/CONVENTIONS.md` → *Step folders & worklogs*). External figures arrive here dispatched from
`sources/` by `source-intake`, cited in the worklog, never linked from the artifact.

## Output
Projects `{#channels-expansion}` via [`template-fragment.md`](template-fragment.md) from the worklog;
inputs via [`questions.yaml`](questions.yaml).
