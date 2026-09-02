---
node_type: card
kind: method
name: pre-mortem
steps: [3]
prerequisites: [strategy-choices]
reads: [section:where-to-play, section:how-to-win, section:channels-expansion, section:bets, register:risks, source:interview]
writes: [worklog, section:product-risks, register:risks]
opinionated: false
method_basis: "Pre-mortem (Klein) on the chosen strategy + risk-register triage (probability × impact); disposition of every candidate"
evidence_standard: decision
volume_rule: "≥8 named failure modes across ≥4 categories (market · competitor · channel/GTM · pricing/viability · tech dependency · team/key-person · regulatory · runway) before any triage"
selection_rule: "probability × impact; every candidate carried · parked · dropped, each with the reason"
rejects_shown: required
status: draft
version: 0.2.2
updated: 2026-09-02
---
# Pre-mortem

Surface the risks to the **chosen strategy** via a **pre-mortem**, triage them by probability ×
impact, and seed the carried ones into the R- register. Fills `{#product-risks}` at Step 3.

**Method basis.** Klein's pre-mortem ("it's 12 months from now and the strategy failed — why?") to
elicit risks before they bite, then risk-register triage by probability × impact, with an explicit
disposition — carried · parked · dropped — for every failure mode surfaced.

> **Boundary with `risk-mitigation` (Step 4) — one mechanism, one way.** This skill *surfaces and
> triages*; it does **not** manage. Mitigation, owner, and trigger are Step 4's `risk-mitigation`,
> which takes the carried `R-…` set from here and makes each one *managed*. Choices are being made
> at Step 3 — mitigations don't exist yet, and writing them here would fake a plan the step hasn't
> earned. If you find yourself assigning owners, you're in the wrong step.

## When to apply
- **Step 3, after the strategy choices are made — before betting on them.** The pre-mortem is run
  against the chosen where-to-play / how-to-win / channels, not against the product in the abstract.
- Whenever the strategy materially changes (a new arena, a new channel commitment) — the failure
  stories change with it.

## Prerequisites
- **Strategy choices** — the where-to-play / how-to-win / channels we're pressure-testing.
  *Missing → run `where-to-play-how-to-win` (and related Step-3 tools) first.*

## How to do it
1. **Run the pre-mortem — to at least 8 named failure modes across at least 4 categories.** Assume
   it's 12 months out and the strategy failed. Ask *why* — force concrete failure stories, not
   abstract worries. In the worklog, tag each story with one category from the fixed list: **market ·
   competitor · channel/GTM · pricing/viability · tech dependency · team/key-person · regulatory ·
   runway**. Fewer than four categories means the session stayed in one room — the first three
   stories are always the ones already being discussed. Stories from a team session arrive as filed
   notes (`source:interview`); the owner's own answers are the questionnaire.
2. **Pull existing risks.** Read the R- register for risks already logged — e.g. journey risks
   seeded by `cjm-strategy` — and fold them into the triage; don't re-invent them, and don't mint a
   duplicate `R-` for a failure the register already carries.
3. **Triage — and record the disposition of every risk you surfaced.** Score each on probability ×
   impact, then mark it **carried · parked · dropped**, each with a one-line reason. Rank the carried
   set by the product. A risk that simply fails to reappear in the next table is indistinguishable
   from one nobody raised, and the pre-mortem's whole value is that somebody did raise it.
4. **Write to the register — and stop there.** Upsert each carried risk into R- with its score and
   `status: open`. **Do not assign mitigation, owner, or trigger** — that is `risk-mitigation` at
   Step 4, which extends these same register entries. Note in the section that the carried set is
   handed to Step 4 unmanaged, on purpose.

## The scale
**Likelihood × impact — H/M/L, backed 5/3/1**, defined in [`process/reference/scales.md`](../../../process/reference/scales.md). The
tiers stay human-readable, the triage ranks by the **product on the 5/3/1 backing** (H=5 · M=3 ·
L=1): five "high"s with no numbers behind them is not an ordering. The lifecycle scale is written
from Step 4 — everything carried from here enters the register as `open`.

## Anti-patterns
- **Stopping at three.** The first three failure modes are the ones already being discussed; the
  volume rule (≥8) exists because the killer is rarely among them.
- **One room.** Eight stories from one or two categories — market and competitor — while team,
  runway, tech dependency and regulatory go unasked; usually where the plan actually sinks.
- **Mitigations at Step 3.** Assigning a mitigation/owner/trigger here — that fakes management the
  step hasn't earned and duplicates `risk-mitigation`'s job at Step 4.
- **Severity theatre.** Scoring everything high so nothing is prioritized.
- **Silent drops.** A surfaced risk that vanishes without a recorded disposition — indistinguishable
  from one nobody raised.
- **Register drift.** Risks triaged here but never written back to R-.

## Worklog & projection
Worklog: `3-strategy/pre-mortem.md` — the ≥8 failure modes each tagged with its category (≥4 covered), the likelihood × impact triage, the disposition of every risk with its reason, the ranked carried set. Projects `{#product-risks}`; face: the **Death read** line, via [`template-fragment.md`](template-fragment.md). Path form, primary/contributing and revisit rules: [`worklog-resolution.md`](../../../process/reference/worklog-resolution.md).

## Output
Projects `{#product-risks}` via [`template-fragment.md`](template-fragment.md) from the worklog;
inputs via [`questions.yaml`](questions.yaml). Carried risks → `R-…` (`status: open`), handed to
Step 4's `risk-mitigation` for mitigation · owner · trigger.
