---
name: uvp-cpv
kind: method
produces: uvp-cpv
reads_registers: []
writes_registers: [hypotheses]
inputs: [interview, kb]
prerequisites: [segments, segment-pains, where-to-play]
used_by_steps: [3]
opinionated: false
method_basis: "Dunford positioning + Value Proposition Canvas + customer-perceived value; CVP stated per situation (segment · situation · pain · CVP) for the lead segment before the one-liner"
evidence_standard: primary-research
volume_rule: n/a
selection_rule: n/a
rejects_shown: n/a
status: draft
version: 0.2.0
updated: 2026-08-16
---

# UVP & Customer-Perceived Value

Articulate the **unique value proposition** — for whom, what job, versus which alternative, and
why us — and the **customer-perceived value** behind it. For the lead segment the value is worked
**per situation** — segment · situation · pain (cost of inaction) · CVP — before it is compressed
into the one-liner. Fills `{#uvp-cpv}`.

**Method basis.** Dunford's positioning (value is relative to a chosen *alternative*, for a *best-fit*
customer), the Value Proposition Canvas (fit between our offer and the customer's jobs / pains /
gains), and customer-perceived value (what the customer believes they get, not what we shipped).
A segment is not an answer — the same segment meets the product in several *situations* (trigger ×
pain), and the CVP that lands in one situation says nothing in another; the one-liner is honest only
when it compresses situational CVPs that were actually written out.

> **Boundary with `segment-cvp` (Step 5) — one mechanism, one way.** This skill articulates the
> *value*: the per-situation CVPs and the one-liner. `segment-cvp` *composes the testable
> market-entry bundle* around them — offer · channel · signal, the 6-filter readiness gate, the
> scoring and staging. Don't gate, score, or stage here; don't re-articulate value there.

## When to apply
- Step 3, once segments, their pains, and the arena (where-to-play) are set.
- When entering a new segment or repositioning against a new alternative.

## Prerequisites
- **Segments** — who the value is for. *Missing → run `segmentation`.*
- **Segment pains** — the jobs/pains the value addresses. *Missing → run `segment-pains`.*
- **Where to play** — the chosen arena the UVP must fit. *Missing → run `where-to-play-how-to-win`.*

## How to do it
1. **Pick the best-fit customer.** From the where-to-play segments, name who this UVP is *for* —
   the customer for whom our value is most obvious.
2. **Name the alternative.** What do they do today (a rival, a substitute, or do-nothing)? Value
   is always *relative to an alternative* — positioning against nothing says nothing.
3. **Work the lead segment per situation.** Enumerate the situations/triggers in which this
   customer meets the problem, and for each state: **segment · situation · pain (with its cost of
   inaction) · CVP** (the concrete outcome we promise *in that situation*). The same buyer in a
   different trigger perceives a different value — a CVP written above the situations is a slogan.
   If a pain has no cost of inaction, say so; that situation carries no CVP.
4. **State the value, not the features.** For the top jobs/pains, say what outcome the customer
   gets and why it beats the alternative. Map to the Value Proposition Canvas: our pain-relievers
   and gain-creators against their pains and gains.
5. **Capture customer-perceived value.** Phrase it as the customer would — the benefit they
   believe they receive. Back it with a signal and say what the signal was: a quote is evidence of one
   person (name the sample), and **money beats words** — what they pay for today, or agreed to pay,
   outranks what they said they would value. Absent a signal, tag `[assumption]`; "customers tell us
   they love it" with no behaviour behind it is one.
6. **Write the one-liner.** "For [best-fit customer] who [job/pain], we [value] — unlike
   [alternative], because [why us / moat]." It compresses the situational CVPs — if it doesn't
   survive being read against each situation in the table, it isn't the one-liner yet.
7. **Seed hypotheses.** Each unproven value claim → `H-…` for the register.

## Anti-patterns
- **Feature-listing.** Cataloguing capabilities instead of the value/outcome they create.
- **No alternative.** Positioning against nothing — no reference point, so no perceived value.
- **Our words, not theirs.** Value framed in internal language the customer wouldn't use.
- **One UVP for everyone.** A generic proposition that fits no segment sharply.
- **CVP above the situations.** A value proposition written for the segment in the abstract — the
  same buyer in a different trigger perceives a different value; write the situations out first.
- **Composing bundles here.** Adding offer/channel/signal, gating, or staging — that is
  `segment-cvp` at Step 5; this skill articulates the value the bundle is built around.

## Worklog & projection
The working is done in the step's **worklog** `<step-folder>/uvp-cpv.md` (`node_type: worklog`,
e.g. `3-strategy/uvp-cpv.md`): the best-fit customer, the named alternative, the lead segment's
situations each with its pain (cost of inaction) and situational CVP, the value stated against
their top jobs/pains via the Value Proposition Canvas, the customer-perceived value in the customer's
own words with the signal behind it (money beats words), and the positioning one-liner. That worklog is
the **source of truth**; the artifact section `{#uvp-cpv}` is its **projection** into the fixed shape of
[`template-fragment.md`](template-fragment.md) — it holds nothing the worklog does not, and the step's
change-log history lives in the worklog, not the section
(`process/CONVENTIONS.md` → *Step folders & worklogs*). External figures arrive here dispatched from
`sources/` by `source-intake`, cited in the worklog, never linked from the artifact.

## Output
Projects `{#uvp-cpv}` via [`template-fragment.md`](template-fragment.md) from the worklog; inputs via
[`questions.yaml`](questions.yaml).
