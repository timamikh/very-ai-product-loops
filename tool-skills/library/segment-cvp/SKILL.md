---
name: segment-cvp
kind: method
produces: market-bundles
prerequisites: [segments, segment-pains]
reads_registers: [hypotheses]
writes_registers: [hypotheses]
inputs: [interview, kb, analytics-search]
used_by_steps: [1, 3, 5]
opinionated: true
method_basis: "Market-entry bundle (segment · situation · pain · CVP · offer · first action · channel · signal) with a 6-filter readiness gate and a qualified-action signal scale; one bundle = one testable go-to-market hypothesis"
evidence_standard: derived
volume_rule: "≥3 distinct situations per priority segment and ≥8 bundles in total before any is staged"
selection_rule: "6-filter readiness gate (binary) → among the ready, 5 criteria × 1/3/5 = 5–25 → top 3–5 staged"
rejects_shown: required
status: draft
version: 0.1.2
updated: 2026-08-09
---

# Segment–CVP bundle

Assemble the **testable market-entry bundle**: for one segment in one situation with one pain,
state the **CVP** (the promise), the **offer** (the first concrete step), the **channel** (where
we reach them), and the **signal** (the qualified action that proves interest). One row = one
falsifiable go-to-market hypothesis. Fills `{#market-bundles}` and seeds the hypothesis register.

**Method basis.** A segment is not an answer — the same segment has several *entries* (situation ×
pain), each a separate bet. A bundle is only ready to test if you can immediately (1) write the ad
message, (2) build the landing/offer, and (3) hand sales a first-contact script. If you can't do
those three, the bundle is too abstract and does not enter the register. Success is read on a
**qualified-action signal scale** (weak = click/like; medium = lead/reply/registration; strong =
meeting with a real decision-maker / trial / price talk / pilot / payment) — clicks diagnose the
*channel*, not the *fit*.

> **Relation to neighbours (one mechanism, one way).**
> - `segmentation` cuts *who*; `segment-pains` ranks the *pains* within a segment; `jtbd` frames
>   the *job and forces*; `uvp-cpv` articulates *value vs an alternative*; `channels-expansion`
>   maps *channels*. **`segment-cvp` does none of these from scratch** — it *composes* their
>   outputs into a single testable entry (segment + situation + pain + CVP + offer + channel +
>   signal) and gates it on test-readiness. If a pain isn't ranked yet, run `segment-pains`; if the
>   value isn't articulated, run `uvp-cpv`. This tool is the assembler, not a re-derivation.
> - It does **not** design the test's statistics — once a bundle is picked, `hypothesis-test-design`
>   (or `ab-test`) sets the metric · threshold · sample · decision rule. `segment-cvp` produces the
>   *candidate*; those produce the *experiment*.

## When to apply
- **Step 1 — as a lens (no passport section).** Once segments and pains exist, turn them into a
  first set of market-entry bundles to seed the hypothesis register with **desirability** bets.
  It sharpens which entries are even worth carrying forward; it does not own a passport section.
- **Step 3 — as a lens (no strategy section).** Sharpen each strategic `{#bets}` entry into a
  concrete, testable market-entry shape (segment + situation + pain + CVP + offer + channel +
  signal) so the bet is specific enough to test. It informs `{#bets}`; the full bundle table +
  readiness gate is composed at Step 5.
- **Step 5 — owns `{#market-bundles}`.** Refresh/expand the bundle set for the period, gate each on
  readiness, and stage the strongest for testing. `prioritization` then scores which 3–5 go to
  test this period; `hypothesis-test-design` designs the chosen ones.
- Whenever positioning feels generic ("for everyone, convenient, with AI") — the bundle forces a
  specific who/where/promise/first-step.

## Prerequisites
- **Segments** — the who, cut by situation not demographics. *Missing → run `segmentation`.*
- **Segment pains** — the pain with a cost of inaction. *Missing → run `segment-pains`.*
- *(Helpful, not required)* an articulated value (`uvp-cpv`) and candidate channels
  (`channels-expansion`); if absent, draft them inside the bundle as `[assumption]` and flag the
  gap, don't block.

## How to do it
1. **Compose one bundle per entry.** For a segment, pick one *situation/trigger* and one *pain*,
   then state: **CVP** (the result promised, not a feature), **offer** (the first concrete step —
   demo · diagnostic · trial · calculation · pilot), **channel** (where this exact segment is
   reachable — a named community/base/partner, not "somewhere online"), and **signal** (the
   qualified action that would prove interest). The same segment usually yields several bundles.
2. **Run the 6-filter readiness gate.** A bundle is test-ready only if every filter passes:
   - **Find** — where *exactly* do we reach this segment? (bad: "somewhere in SMB")
   - **Recognize** — would the person recognize themselves in the wording? (bad: "for everyone who wants AI")
   - **Pain** — is there a cost of inaction? (bad: "would be nice")
   - **Alternative** — how do they solve it today? (bad: "no idea / nohow")
   - **CVP** — do we promise a concrete result? (bad: "become more efficient")
   - **Action** — what signal will we get? (bad: "interest / reactions")
   A bundle failing any filter is marked `not-ready` with the reason — it stays for reference but
   is not staged.
3. **Apply the three-things test.** Can you, right now, write the ad message, build the
   landing/offer, and give sales a first-contact script from this bundle? If not, it's too
   abstract — send it back to `segment-pains`/`uvp-cpv`, don't stage it.
4. **Set the signal on the scale.** State the target signal *and its strength tier* (weak/medium/
   strong). Prefer a strong or medium qualified action as the success signal; clicks/likes are
   channel diagnostics, never the result.
5. **Tag confidence & source, then seed the register.** Each ready bundle → an `H-…`
   (`type: desirability`) whose statement carries the whole bundle. Bundles are the register's
   go-to-market entries; a validated bundle is a proven positioning, a refuted one is a guard.
6. **Fix the decision commitment.** A bundle is not "tested" until it has a recorded decision:
   **scale · iterate · reject · back-to-research**. Note the intended decision rule; the actual
   test design is handed to `hypothesis-test-design`.

## Anti-patterns
- **Mass audience as a segment.** "Small business" / "everyone with AI" can't have a channel or a
  message built for it — not a segment, not a bundle.
- **CVP = feature.** "Convenient, fast, with AI" promises no result. State the outcome the segment
  gets.
- **No first action.** A bundle with a promise but no concrete first step (demo/diagnostic/trial)
  can't be offered or measured.
- **Clicks as success.** Reading a weak signal (clicks, likes, page views) as fit — it's channel
  diagnostics. Success is a *qualified* action.
- **Re-deriving the parts here.** Re-cutting segments or re-ranking pains inside this tool instead
  of composing the outputs of `segmentation`/`segment-pains` — that's the neighbours' job.
- **Test with no decision.** Running a bundle and never recording scale/iterate/reject — the test
  isn't finished.

## Output
At Step 5, fills `{#market-bundles}` via [`template-fragment.md`](template-fragment.md); inputs via
[`questions.yaml`](questions.yaml). At Steps 1 and 3 it produces no artifact section — it acts as a
lens: at Step 1 it seeds the hypothesis register (desirability bets) and informs `segments`/`problems`;
at Step 3 it sharpens `{#bets}` into concrete, testable market-entry shapes.
