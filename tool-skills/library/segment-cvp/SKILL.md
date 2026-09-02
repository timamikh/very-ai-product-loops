---
node_type: card
kind: method
name: segment-cvp
steps: [5]
prerequisites: [segments, segment-pains]
reads: [section:segments, section:problems, section:uvp-cpv, section:channels-expansion, register:hypotheses, source:interview, source:research]
writes: [worklog, section:market-bundles, register:hypotheses]
opinionated: true
method_basis: "Market-entry bundle (segment · situation · pain · CVP · offer · first action · channel · signal) with a 6-filter readiness gate and a qualified-action signal scale; one bundle = one testable go-to-market hypothesis"
evidence_standard: derived
volume_rule: "≥3 distinct situations per priority segment and ≥8 bundles in total before any is staged"
selection_rule: "6-filter readiness gate (binary) → among the ready, 5 criteria × 1/3/5 = 5–25 → top 3–5 staged"
rejects_shown: required
status: draft
version: 0.3.2
updated: 2026-09-02
---
# Segment–CVP bundle

Assemble the **testable market-entry bundle**: for one segment in one situation with one pain,
state the **CVP** (the promise), the **offer** (the first concrete step), the **channel** (where
exactly we reach them) and the **signal** (the qualified action that proves interest). One row =
one falsifiable go-to-market hypothesis. Fills `{#market-bundles}` and seeds the hypothesis register.

**Method basis.** A segment is not an answer — the same segment has several *entries* (situation ×
pain), each a separate bet. A bundle is ready to test only if you can immediately write the ad
message, build the landing/offer and hand sales a first-contact script. Success is read on the
**signal scale** of [`process/reference/scales.md`](../../../process/reference/scales.md) — a click
diagnoses the *channel*, not the *fit*.

> **Relation to neighbours (one mechanism, one way).** `segmentation` cuts *who*, `segment-pains`
> ranks the *pains*, `uvp-cpv` states *value vs an alternative* per situation, `channels-expansion`
> maps *channels*. This tool re-derives none of them — it **composes** `{#segments}`, `{#problems}`,
> `{#uvp-cpv}` and `{#channels-expansion}` into one testable entry and gates it on readiness. It
> does **not** design the test (`hypothesis-test-design` / `ab-test` do), and it scores *which bet is
> worth learning about first* — `prioritization-tactical-plan` decides *what fits the period's
> capacity* and never re-scores a staged bundle.

## When to apply
- **Step 5 — owns `{#market-bundles}`.** Refresh the bundle set for the period, gate each on
  readiness, score the ready ones, stage the top 3–5.
- Whenever positioning feels generic ("for everyone, convenient, with AI").

## Prerequisites
- **Segments** — the who, cut by situation not demographics. *Missing → run `segmentation`.*
- **Segment pains** — the pain with a cost of inaction. *Missing → run `segment-pains`.*
- *(Helpful, not required)* an articulated value (`uvp-cpv`) and candidate channels
  (`channels-expansion`); if absent, draft them inside the bundle as `[assumption]` and flag the
  gap, don't block.

## How to do it
1. **Compose one bundle per entry — and compose enough of them.** For a segment, pick one
   *situation/trigger* and one *pain*, then state the **CVP** (a result, not a feature), the
   **offer** (demo · diagnostic · trial · calculation · pilot), the **channel** (a named community /
   base / partner) and the **signal**. **Volume rule: at least 3 distinct situations per priority
   segment, and at least 8 bundles in total, before any bundle is staged.** The unit of generation
   is the situation, not the segment: the same buyer in a different trigger is a different bet.
   Fewer than three situations for a segment is a finding — record it, don't pad.
2. **Run the 6-filter readiness gate** — Find · Recognize · Pain · Alternative · CVP · Action,
   pass/fail, defined in `scales.md`. A failing bundle is `not-ready: <filter>` — kept, never staged.
3. **Apply the three-things test.** Ad message, landing/offer, sales first-contact script — all
   three writable from the row now. If not → back to `segment-pains` / `uvp-cpv`, not staged.
4. **Set the signal and its tier** — `weak` / `medium` / `strong` per `scales.md`. The success
   signal is a medium or strong qualified action; a weak signal is channel diagnostics.
5. **Score the ready bundles and stage the top 3–5.** The gate says which bundles are *testable*,
   not which deserve a test slot. Score each ready bundle on the **priority score** of `scales.md` —
   **1 · 3 · 5** on its five criteria (pain acuteness · reachability · deliverability · willingness
   to pay · speed to a signal), sum **5–25** — and stage the top 3–5. A score is ⚙️ until confirmed;
   a criterion you cannot judge is `— to clarify —`, not a 3. The evidence behind a score is what
   the composed sections carry; a claim new to this pass is sourced (`source:interview` /
   `source:research`) or `[assumption]`. *Speed to a signal* is why the score lives here and not in
   RICE, which has no axis for how fast a bet can be falsified.
6. **Seed the register.** Each ready bundle → an `H-…` (`type: desirability`) whose statement
   carries the whole bundle.
7. **Fix the decision commitment.** Note the decision each outcome triggers — `scale` · `iterate` ·
   `reject` · `research`, the decision scale of `scales.md`.
8. **Show what you cut, and why.** Every bundle that failed a filter and every ready bundle that
   lost on score stays in the output with its filter or score — otherwise the next pass re-proposes
   it, and nobody can tell a filter applied from one never reached.

## Anti-patterns
- **Mass audience as a segment.** "Small business" can't have a channel or a message built for it.
- **CVP = feature.** "Convenient, fast, with AI" promises no result.
- **No first action.** A promise with no demo / diagnostic / trial can't be offered or measured.
- **Clicks as success.** A weak signal read as fit.
- **Re-deriving the parts here.** Re-cutting segments or re-ranking pains instead of composing.
- **Four bundles, four survivors.** Only as many bundles as you intend to stage — nothing selected.
- **Padding to hit the number.** The floor is on *distinct situations*, not rows.
- **Scoring the same bundle twice.** Re-ranking staged bundles on RICE downstream.
- **A 3 for "I don't know".** An unknown is `— to clarify —`; a bundle scored on shrugs is not staged.

## Worklog & projection
Worklog: `5-tactical-plan/segment-cvp.md` — every bundle composed, its 6-filter verdict with the reason, the 1·3·5 scores of the ready ones, the staged top 3–5, every not-ready or lost-on-score bundle with its filter or score. Projects `{#market-bundles}`; face: the **Staged for test this period** line, via [`template-fragment.md`](template-fragment.md). Path form, primary/contributing and revisit rules: [`worklog-resolution.md`](../../../process/reference/worklog-resolution.md).

## Output
Projects `{#market-bundles}` (Step 5) via [`template-fragment.md`](template-fragment.md) from the
worklog; inputs via [`questions.yaml`](questions.yaml). The value half of an entry — segment ·
situation · pain · CVP — is articulated by `uvp-cpv` at Step 3; this tool composes it into the
testable bundle here.
