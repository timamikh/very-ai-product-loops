---
name: risk-mitigation
kind: method
produces: [product-risks]
reads_registers: [risks]
writes_registers: [risks]
inputs: [interview, kb]
prerequisites: [strategy-choices]
used_by_steps: [3, 4]
opinionated: false
method_basis: "Pre-mortem (Klein) + risk register triage (prob × impact) + mitigation/owner"
evidence_standard: decision
volume_rule: "≥8 named failure modes from the pre-mortem before any triage"
selection_rule: "probability × impact; carried · parked · dropped, each with the reason"
rejects_shown: required
status: draft
version: 0.3.0
updated: 2026-08-13
---

# Risk & Mitigation

Surface the risks to the strategy via a **pre-mortem**, triage them into the R- register, and
give each a **mitigation, owner, and trigger**. Fills `{#product-risks}` at Step 3, and is reused
at Step 4 to attach mitigations to the plan.

**Method basis.** Klein's pre-mortem ("it's 12 months from now and the strategy failed — why?")
to elicit risks before they bite, then risk-register triage by probability × impact, and a named
mitigation + owner + trigger for each risk worth carrying.

## When to apply
- Step 3, after the strategy choices are made — before betting on them.
- Step 4, to add mitigations and owners to the plan's risks.
- Whenever a new risk surfaces or a live risk changes probability/impact.

## Prerequisites
- **Strategy choices** — the where-to-play / how-to-win / channels we're pressure-testing.
  *Missing → run `where-to-play-how-to-win` (and related Step-3 tools) first.*

## How to do it
1. **Run the pre-mortem — to at least 8 named failure modes.** Assume it's 12 months out and the
   strategy failed. Ask *why* — force concrete failure stories, not abstract worries. Cover execution
   and key-person risks, not just external/market ones. Stopping at three is the pre-mortem's
   characteristic failure: the first three are always the ones already being discussed, and the risk
   that kills the plan is rarely among them.
2. **Pull existing risks.** Read the R- register for risks already logged (e.g. seeded by earlier
   tools); don't re-invent them.
3. **Triage — and record the disposition of every risk you surfaced.** Score each on probability ×
   impact, then mark it **carried · parked · dropped**, each with a one-line reason. Rank the carried
   set by the product. A risk that simply fails to reappear in the next table is indistinguishable
   from one nobody raised, and the pre-mortem's whole value is that somebody did raise it.
4. **Assign mitigation + owner + trigger.** For each carried risk: what we'll do about it, *who*
   owns it, and the *trigger* (the observable signal that says "act now"). A risk with no owner or
   trigger is not managed.
5. **Write to the register.** Upsert each into R- with score, mitigation, owner, trigger, status.

## Scales — the shared gradations

Two ordinal scales travel with a risk. They are **gradations**, orthogonal to the confirmation marker
a human signs (see `process/CONVENTIONS.md` → *Gradation vs confirmation*).

- **Likelihood × impact — H/M/L, backed 5/3/1.** The tiers stay human-readable (`H`/`M`/`L`), but the
  triage ranks by the **product on the 5/3/1 backing** (H=5 · M=3 · L=1): five "high"s with no numbers
  behind them is not an ordering. Rank the carried set by likelihood × impact, top-product first.
- **Lifecycle — `open` → `mitigating` → `contained` → `realized` → `closed`, plus `accepted`.**
  `contained` = a live risk whose mitigation is in place; `realized` = it fired (the mitigation and the
  fallout are now the story); `closed` = no longer credible. `accepted` is **off-cycle** — a decision
  to carry the risk un-mitigated on purpose, not a stage. Written back to the register's `status`.

## Anti-patterns
- **No owner / no trigger.** A risk logged but unassigned, with nothing that says when to act.
- **Only external risks.** Listing market/competitor risks while ignoring execution and
  key-person risks — usually the ones that actually sink it.
- **Severity theatre.** Scoring everything high so nothing is prioritized.
- **Register drift.** Risks captured here but never written back to R-.

## Worklog & projection
The working is done in the step's **worklog** `<step-folder>/risk-mitigation.md` (`node_type: worklog`,
e.g. `3-strategy/risk-mitigation.md`): the pre-mortem's ≥8 named failure modes, the likelihood × impact
triage with every surfaced risk's disposition (carried · parked · dropped) and reason, the ranked
carried set, and each carried risk's mitigation, owner, and trigger. That worklog is the **source of
truth**; the artifact section `{#product-risks}` is its **projection** into the fixed shape of
[`template-fragment.md`](template-fragment.md) — it holds nothing the worklog does not, and the step's
change-log history lives in the worklog, not the section
(`process/CONVENTIONS.md` → *Step folders & worklogs*). External figures arrive here dispatched from
`sources/` by `source-intake`, cited in the worklog, never linked from the artifact.

## Output
Projects `{#product-risks}` via [`template-fragment.md`](template-fragment.md) from the worklog; inputs
via [`questions.yaml`](questions.yaml).
