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
method_basis: "Dunford positioning + Value Proposition Canvas + customer-perceived value"
evidence_standard: primary-research
volume_rule: n/a
selection_rule: n/a
rejects_shown: n/a
status: draft
version: 0.1.2
updated: 2026-08-09
---

# UVP & Customer-Perceived Value

Articulate the **unique value proposition** — for whom, what job, versus which alternative, and
why us — and the **customer-perceived value** behind it. Fills `{#uvp-cpv}`.

**Method basis.** Dunford's positioning (value is relative to a chosen *alternative*, for a *best-fit*
customer), the Value Proposition Canvas (fit between our offer and the customer's jobs / pains /
gains), and customer-perceived value (what the customer believes they get, not what we shipped).

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
3. **State the value, not the features.** For the top jobs/pains, say what outcome the customer
   gets and why it beats the alternative. Map to the Value Proposition Canvas: our pain-relievers
   and gain-creators against their pains and gains.
4. **Capture customer-perceived value.** Phrase it as the customer would — the benefit they
   believe they receive. Back it with a signal and say what the signal was: a quote is evidence of one
   person (name the sample), and **money beats words** — what they pay for today, or agreed to pay,
   outranks what they said they would value. Absent a signal, tag `[assumption]`; "customers tell us
   they love it" with no behaviour behind it is one.
5. **Write the one-liner.** "For [best-fit customer] who [job/pain], we [value] — unlike
   [alternative], because [why us / moat]."
6. **Seed hypotheses.** Each unproven value claim → `H-…` for the register.

## Anti-patterns
- **Feature-listing.** Cataloguing capabilities instead of the value/outcome they create.
- **No alternative.** Positioning against nothing — no reference point, so no perceived value.
- **Our words, not theirs.** Value framed in internal language the customer wouldn't use.
- **One UVP for everyone.** A generic proposition that fits no segment sharply.

## Output
Fills `{#uvp-cpv}` via [`template-fragment.md`](template-fragment.md); inputs via
[`questions.yaml`](questions.yaml).
