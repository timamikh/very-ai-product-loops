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
version: 0.1.3
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
> - It scores **which bet is worth learning about first**; `prioritization` scores **what fits this
>   period's capacity**. Two questions, two scales, one object each — a staged bundle is not
>   re-scored downstream (see step 5).

## When to apply
- **Step 1 — as a lens (no passport section).** Once segments and pains exist, turn them into a
  first set of market-entry bundles to seed the hypothesis register with **desirability** bets.
  It sharpens which entries are even worth carrying forward; it does not own a passport section.
- **Step 3 — as a lens (no strategy section).** Sharpen each strategic `{#bets}` entry into a
  concrete, testable market-entry shape (segment + situation + pain + CVP + offer + channel +
  signal) so the bet is specific enough to test. It informs `{#bets}`; the full bundle table +
  readiness gate is composed at Step 5.
- **Step 5 — owns `{#market-bundles}`.** Refresh/expand the bundle set for the period, gate each on
  readiness, score the ready ones and stage the top 3–5. `prioritization` then decides whether those
  fit the period's capacity — it does not re-score them; `hypothesis-test-design` designs the chosen
  ones.
- Whenever positioning feels generic ("for everyone, convenient, with AI") — the bundle forces a
  specific who/where/promise/first-step.

## Prerequisites
- **Segments** — the who, cut by situation not demographics. *Missing → run `segmentation`.*
- **Segment pains** — the pain with a cost of inaction. *Missing → run `segment-pains`.*
- *(Helpful, not required)* an articulated value (`uvp-cpv`) and candidate channels
  (`channels-expansion`); if absent, draft them inside the bundle as `[assumption]` and flag the
  gap, don't block.

## How to do it
1. **Compose one bundle per entry — and compose enough of them.** For a segment, pick one
   *situation/trigger* and one *pain*, then state: **CVP** (the result promised, not a feature),
   **offer** (the first concrete step — demo · diagnostic · trial · calculation · pilot),
   **channel** (where this exact segment is reachable — a named community/base/partner, not
   "somewhere online"), and **signal** (the qualified action that would prove interest).

   **Volume rule: at least 3 distinct situations per priority segment, and at least 8 bundles in
   total, before any bundle is staged.** The unit of generation is not the segment — `segmentation`
   deliberately caps those at 1–3 — it is the **situation**: the same buyer in a different trigger
   is a different bet, with a different message and often a different channel. Four polite bundles,
   all of them survivors, is not a selection; it is the first idea written out four ways. If you
   cannot find three situations for a segment, that is a finding about the segment — record it and
   say so, rather than padding.
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
5. **Score the ready bundles and stage the top 3–5.** The 6-filter gate is binary — it says which
   bundles are *testable at all*. It does not say which are worth a test slot, and with eight or more
   ready bundles that question does not answer itself. Score each ready bundle **1 · 3 · 5** on five
   criteria, sum to **5–25**, stage the top 3–5:

   | Criterion | 1 | 3 | 5 |
   |-----------|---|---|---|
   | **Pain acuteness** — the cost of inaction | nice-to-have | recurring irritation | they are already paying or improvising to avoid it |
   | **Reachability** — can we actually get in front of them | no named place | a place we could get into | a named community/base/partner we can reach this week |
   | **Deliverability** — can we serve them if they say yes | needs a product we don't have | needs work we could do | we can deliver today, even manually |
   | **Evidence of willingness to pay** | none | they pay for something adjacent | they pay for this problem today |
   | **Speed to a signal** — how fast we learn | > 2 weeks | about a week | 1–2 days |

   **Speed to a signal is why this scoring lives here and not in `prioritization`.** The two answer
   different questions and must not be merged: this rubric asks *which bet is worth learning about
   first*, and `prioritization` asks *what fits this period's capacity against the period gate* on
   RICE/ICE. RICE has no axis for how fast a bet can be falsified — Effort is build cost, which for a
   bundle that needs a landing page and ad copy is nearly constant across candidates and therefore
   discriminates nothing. `prioritization` does **not** re-score bundles: it takes the staged 3–5 and
   decides whether they fit the period. Scoring the same objects twice on two scales is exactly the
   drift "one mechanism, one way" forbids, which is why the boundary is stated in both files.

   A score is `⚙️` until the human confirms it, and a criterion you cannot judge is a `— to clarify —`,
   not a 3.
6. **Tag confidence & source, then seed the register.** Each ready bundle → an `H-…`
   (`type: desirability`) whose statement carries the whole bundle. Bundles are the register's
   go-to-market entries; a validated bundle is a proven positioning, a refuted one is a guard.
7. **Fix the decision commitment.** A bundle is not "tested" until it has a recorded decision:
   **scale · iterate · reject · back-to-research**. Note the intended decision rule; the actual
   test design is handed to `hypothesis-test-design`.
8. **Show what you cut, and why.** Every bundle that failed a filter, and every ready bundle that
   lost on score, stays in the output with the filter it failed or its score. A cut bundle is the
   cheapest thing this method produces and the most expensive to re-derive: without it the next pass
   re-proposes the same entry, and nobody can tell a filter that was applied and passed from one that
   was never reached.

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
- **Four bundles, four survivors.** Generating only as many bundles as you intend to stage. Nothing
  was selected; the first idea was written out four ways and the gate had nothing to reject.
- **Padding to hit the number.** The volume rule is a floor on *distinct situations*, not on rows —
  the same entry reworded three times fails it more expensively than eight honest ones would.
- **Scoring the same bundle twice.** Running the readiness score here and then re-ranking the staged
  bundles on RICE downstream. Two scales over one object is drift; `prioritization` capacity-bounds
  what this method staged, it does not re-judge it.
- **A 3 for "I don't know".** The middle of a 1/3/5 scale is a judgement, not a shrug — an unknown is
  `— to clarify —`, and a bundle scored mostly on shrugs should not be staged.

## Worklog & projection
The working is done in the step's **worklog** `<step-folder>/segment-cvp.md` (`node_type: worklog`,
e.g. `5-tactical-plan/segment-cvp.md`): every bundle composed (segment · situation · pain · CVP ·
offer · channel · signal), its verdict on the 6-filter readiness gate with the reason, the 1·3·5
scores on the five criteria for the ready ones, the top 3–5 staged, and every not-ready or
lost-on-score bundle kept with the filter it failed or its score. That worklog is the **source of
truth**; the artifact section `{#market-bundles}` is its **projection** into the fixed shape of
[`template-fragment.md`](template-fragment.md) — it holds nothing the worklog does not, and the step's
change-log history lives in the worklog, not the section
(`process/CONVENTIONS.md` → *Step folders & worklogs*). External figures arrive here dispatched from
`sources/` by `source-intake`, cited in the worklog, never linked from the artifact.

## Output
At Step 5, projects `{#market-bundles}` via [`template-fragment.md`](template-fragment.md) from the
worklog; inputs via [`questions.yaml`](questions.yaml). At Steps 1 and 3 it produces no artifact
section — it acts as a lens: at Step 1 it seeds the hypothesis register (desirability bets) and informs
`segments`/`problems`; at Step 3 it sharpens `{#bets}` into concrete, testable market-entry shapes.
