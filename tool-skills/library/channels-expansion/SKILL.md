---
name: channels-expansion
kind: method
produces: channels-expansion
reads_registers: []
writes_registers: [hypotheses, risks]
inputs: [interview, kb, analytics-search]
prerequisites: [segments, uvp]
used_by_steps: [3]
opinionated: false
method_basis: "Bullseye framework (Traction, Weinberg/Mares) + expansion-path thinking"
evidence_standard: external-sources
volume_rule: "≥8 candidate channels across ≥3 channel-type categories before any ring is assigned"
selection_rule: "reach × cost-to-test × testability (1/3/5); inner ring = the 3 highest, tested now"
rejects_shown: required
status: draft
version: 0.1.1
updated: 2026-08-09
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
1. **Brainstorm the full list.** Consider every channel type, not just the obvious two — don't
   pre-filter to what's familiar.
2. **Rank into rings.** Sort into inner (test now), middle (promising), outer (unlikely). Bet the
   first tests on the inner ring; keep the rest as backlog.
3. **Define a measurable test per inner-ring channel.** For each, state the metric, the cost, and
   the success threshold *before* running it. A channel you can't measure isn't a test.
4. **Keep channel separate from message.** The channel is *where* you reach them; the UVP is
   *what* you say. Name both, don't conflate them.
5. **Map the expansion path.** Sequence the next segments / markets / geographies and the
   trigger that unlocks each (e.g. "expand to segment B once channel X hits CAC < …").
6. **Seed registers.** Channel bets → `H-…`; expansion or dependency risks (saturation,
   regulatory, localization) → `R-…`.

## Anti-patterns
- **All channels at once.** Spreading thin instead of testing the inner ring first.
- **No way to measure.** A channel with no metric or threshold — spend with no read.
- **Channel = message.** Confusing the medium with the value proposition it carries.
- **Expansion with no trigger.** A wish-list of markets with nothing gating the next step.

## Output
Fills `{#channels-expansion}` via [`template-fragment.md`](template-fragment.md); inputs via
[`questions.yaml`](questions.yaml).
