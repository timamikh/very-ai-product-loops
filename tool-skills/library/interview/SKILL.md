---
name: interview
kind: research
produces: product/sources/<slug>-interview-guide.md
prerequisites: [the decision or hypothesis the interview must inform, a candidate segment/persona to talk to]
reads_registers: [hypotheses]
writes_registers: [hypotheses]
inputs: []
used_by_steps: [1, 2]
opinionated: false
method_basis: "Continuous discovery (Torres) + The Mom Test (Fitzpatrick) — non-leading questions, past behaviour over hypotheticals"
evidence_standard: primary-research
volume_rule: n/a
selection_rule: "screen-in/screen-out criteria tied to the target behaviour — never availability or convenience"
rejects_shown: required
status: draft
version: 0.1.2
updated: 2026-08-09
---

# Interview (prep)

Prepare an interview that actually produces learning: name the **goal** (which decision or
hypothesis it must inform), draw the **interviewee portrait** (who to recruit and how to screen
them), write **non-leading questions**, and hand the interviewer a short **guide** for running it.
Produced as a **standalone file** in `product/sources/` (indexed in `sources/INDEX.md`), not an
artifact section.

**Method basis.** Torres' continuous discovery + Fitzpatrick's *The Mom Test*: ask about the
person's **life and past behaviour**, not your idea; specifics ("tell me about the last time…"),
not hypotheticals ("would you…"); never pitch — the moment you sell, you stop learning.

**Relation to neighbours.** This tool **prepares and gathers**; the *analysis* of what comes back
lands downstream — `segment-pains`, `jtbd`, `cjm`, `segmentation`. It fills the `interview`
**input slot** those tools consume. Don't draw conclusions here; produce the instrument and the
raw notes.

## When to apply
- **Step 1**, the primary discovery method when there's little or no usage data yet.
- **Step 2**, to get the "why" behind an analytics signal.
- Whenever a bet rests on an assumption about what people *do* that only they can tell you.

## Prerequisites
- **The decision or hypothesis the interview must inform** — the `H-…` or choice it will move.
  *Missing → there's no interview to run yet; frame the question first.*
- **A candidate segment/persona to talk to** — who the interviewee should be.
  *Missing → run `segmentation` to name who's worth talking to.*

## How to do it
1. **Fix the goal.** The one decision or `H-…` this interview must inform. No goal → a pleasant
   chat that decides nothing.
2. **Draw the interviewee portrait.** Exactly who — segment, role, behaviours — plus the
   **screening questions** that qualify or disqualify a candidate. Recruit for the behaviour, not
   for who's easy to reach.
3. **Write non-leading questions.** Ask about **past specific behaviour** ("walk me through the
   last time you…"), not hypotheticals. No pitching, no leading. Order broad → specific.
4. **Add follow-up probes.** The "why / tell me more / what did you do next" that get past the
   first, rehearsed answer.
5. **Write a one-page interviewer guide.** How to open, length, recording/consent, what to avoid
   (pitching, leading, interrupting), how to close.
6. **Record who you actually talked to, and who you did not.** Names of the screens applied, how
   many candidates were screened out and on which criterion, and the bias you know the sample has
   ("all inbound users, so nobody who evaluated us and left"). A conclusion drawn from five people is
   a conclusion about five people until the sample is stated — and the people who were screened *out*
   are the cheapest thing to lose and the most expensive to notice missing.
7. **Seed the register.** Each assumption the interview is testing → `H-…`, so the notes can flip
   its confidence later.

## Anti-patterns
- **No goal.** A friendly conversation that changes no decision.
- **Leading questions.** You hear your own idea echoed back and call it validation.
- **Hypotheticals.** "Would you pay?" predicts nothing — ask what they actually did.
- **Pitching.** Selling the idea instead of learning about their life.
- **Recruiting for convenience.** Talking to the wrong people, confidently.

## Output
Produced from [`template-fragment.md`](template-fragment.md) as a file in `product/sources/`; inputs
via [`questions.yaml`](questions.yaml). The guide and raw notes live in `product/sources/` (indexed in
`sources/INDEX.md`) and feed `segment-pains`, `jtbd`, `cjm`, `segmentation`. Raw notes are deleted
once their signal lands in the registers (CONVENTIONS: no PII in artifacts).
