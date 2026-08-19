---
node_type: card
kind: output
name: interview
output_kind: authored
prerequisites: [the decision or hypothesis the interview must inform, a candidate segment/persona to talk to]
reads: [register:hypotheses]
writes: [file:product-loops/export-files/<slug>-interview-guide.md]
surfaces: [file:export-files/*]
opinionated: false
method_basis: "Continuous discovery (Torres) + The Mom Test (Fitzpatrick) — non-leading questions, past behaviour over hypotheticals"
evidence_standard: primary-research
volume_rule: n/a
selection_rule: "screen-in/screen-out criteria tied to the target behaviour — never availability or convenience"
rejects_shown: required
status: draft
version: 0.2.0
updated: 2026-08-16
---
# Interview (prep)

Prepare an interview that actually produces learning: name the **goal** (which decision or
hypothesis it must inform), draw the **interviewee portrait** (who to recruit and how to screen
them), write **non-leading questions**, and hand the interviewer a short **guide** for running it.
The guide is an **authored deliverable** — `product-loops/export-files/<slug>-interview-guide.md`
(`node_type: deliverable`), a file the product person takes and uses **outside the framework**. The
interviews themselves happen out there; what comes **back** — the notes — is external material the
user adds to `sources/`, and it enters the framework the one standard way (see *Output*).

**Method basis.** Torres' continuous discovery + Fitzpatrick's *The Mom Test*: ask about the
person's **life and past behaviour**, not your idea; specifics ("tell me about the last time…"),
not hypotheticals ("would you…"); never pitch — the moment you sell, you stop learning.

**Relation to neighbours.** This tool **prepares the instrument**; the *analysis* of what comes back
lands downstream — `segment-pains`, `jtbd`, `cjm`, `segmentation` consume the returned notes through
their `interview` **input slot**. Don't draw conclusions here; produce the instrument, and let the
notes travel the standard source path.

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
7. **Name the register entries it informs.** The guide lists the `H-…` each question block is built
   to move, so the notes can flip its confidence later. An assumption with no `H-…` yet is seeded
   **before** the guide is finalised — by the method that surfaced the bet, ids minted by the
   orchestrator; this skill writes no register itself.

## Anti-patterns
- **No goal.** A friendly conversation that changes no decision.
- **Leading questions.** You hear your own idea echoed back and call it validation.
- **Hypotheticals.** "Would you pay?" predicts nothing — ask what they actually did.
- **Pitching.** Selling the idea instead of learning about their life.
- **Recruiting for convenience.** Talking to the wrong people, confidently.

## Output
Produced from [`template-fragment.md`](template-fragment.md) as
`product-loops/export-files/<slug>-interview-guide.md` (`node_type: deliverable`); inputs via
[`questions.yaml`](questions.yaml).

**The return path is the standard source path, not this skill.** The conducted interviews' notes are
external material: the user adds them to `sources/` (indexed in `sources/INDEX.md`, citing the guide
they were run against), `source-intake` dispatches them into the worklogs of the consuming methods
(`segment-pains`, `jtbd`, `cjm`, `segmentation`), and the orchestrator writes any register change
during those methods' passes. Raw notes are deleted once their signal lands in the worklogs and
registers (CONVENTIONS: no PII in artifacts).
