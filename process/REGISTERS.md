---
node_type: registers
title: Registers — metrics, hypotheses, risks
status: draft
version: 0.9.1
updated: 2026-08-18
---

# Registers

Three living, vertical objects, shared across all steps — born once, refined downward, results
flowing back up, **not re-authored per step**. In an instance: `registers/` at the instance root
(the working area — `product-loops/` in a live product). IDs, confidence and change logs follow
[`CONVENTIONS.md`](CONVENTIONS.md).

*Read this file at its named moments* (OPERATING-LOOP): **move 2** — pulling register rows as
inputs, when field semantics or gradations are in doubt — and **move 5** — before writing rows.
The register *values* live in the instance files, read on every pass that needs them.

| Register | Born at | Refined at |
|----------|---------|------------|
| Hypotheses | Steps 1 (concept) · 2 (sizing) · 3 (bets) | 4 (quantify) → 5 (test design) → 6 (experiment tasks) |
| Risks | Steps 2 (niche) · 3 (product) · 4 (capability gaps) | 4 (mitigation) → 5 (period blockers) |
| Metric tree | Step 4 | 5 (select nodes) → 6 (task ↔ metric) |

## What earns a register — the four-sign test

A candidate is **tested, not argued**, on all four signs: a stable cross-step id · an enumerable
lifecycle (`status`) · a life outlasting the step that bore it · state that flows both ways. Fail
one and the home is a step artifact section. The full test —
[`EXTENDING.md`](../EXTENDING.md) → *What earns a register*.

## Hypothesis register (`hypotheses.md`)

| Field | Values / notes |
|-------|----------------|
| `id` | `H-001`, … (stable) |
| `statement` | the hypothesis, falsifiable |
| `type` | `desirability` · `feasibility` · `viability` · `usability` — **exactly one** |
| `tags` | free cross-cutting themes (*moat*, *pricing*) — never compounded into `type`, never load-bearing |
| `status` | `open` · `testing` · `validated` · `refuted` · `superseded` — never delete; `superseded` = split in two, not disproved |
| `born` | step it originated in |
| `source` | where it came from |
| `test` | link to the test design (Step 5) / experiment (Step 6) |
| `confidence` | `assumption` · `sourced` · `validated` · `refuted` |
| `signal` | *post-test*, the observed market response: `weak` (click · like · page-view) · `medium` (lead · sign-up · reply · details request) · `strong` (meeting with a real DM · trial access · price talk · pilot · pre-pay · sale). Empty until read |
| `decision` | *post-test*, the call the readout drives: `scale` · `iterate` · `reject` · `research`. Distinct from `status` — a bet can be `validated`/`scale` or partially-true/`iterate`. Empty until read |

A cross-cutting theme is **not** a fifth type (`viability/moat` is wrong — `type: viability`,
`tags: moat`). A hypothesis needing **two verdicts is split in two** at the first attempt to test it
(Step 4): the halves name the original, the original closes as `superseded`. This id/type taxonomy
is defined **here**; CONVENTIONS carries only the link form.

`signal` and `decision` are **gradations** (in the row), orthogonal to the human's confirmation
marker (CONVENTIONS → *Gradation vs confirmation*). A refuted bet or a `reject`/`research` decision
can trigger an upward revisit (step cadence/invalidation). The test-selection **priority score**
(1/3/5 tiers) is not a register column — it is defined by
[`hypothesis-test-design`](../tool-skills/library/hypothesis-test-design/SKILL.md) §Scales and
operated at Step 5 by [`segment-cvp`](../tool-skills/library/segment-cvp/SKILL.md).

## Risk register (`risks.md`)

| Field | Values / notes |
|-------|----------------|
| `id` | `R-001`, … |
| `description` | the risk |
| `category` | market · product · execution · legal · financial · dependency — **exactly one**; extra themes in `tags` |
| `tags` | free cross-cutting themes |
| `likelihood` | H/M/L, backed by 5/3/1 for ranking |
| `impact` | H/M/L, same 5/3/1 backing |
| `mitigation` | the plan (added Step 4) |
| `owner` / `due` | who, by when (added Step 4/5) |
| `status` | `open` · `mitigating` · `contained` · `realized` · `closed` · `accepted` (carried un-mitigated on purpose) |
| `source` | where it surfaced |

Carried risks are **ranked by likelihood × impact** on the 5/3/1 tiers — the numeric backing makes a
real ordering out of a pile of "high"s. The scale and its pre-mortem —
[`pre-mortem`](../tool-skills/library/pre-mortem/SKILL.md) (Step 3); the mitigation lifecycle —
[`risk-mitigation`](../tool-skills/library/risk-mitigation/SKILL.md) (Step 4).

## Metric register (`metric-tree.md` + `metrics.csv`)

A decomposition — **North Star → drivers → input metrics**. One canonical split (CONVENTIONS →
*One mechanism, one way*): **definitions in markdown, values in CSV** — always, from the first
capture; no md-cell time series.

**`metric-tree.md` — node definitions only:**

| Field | Values / notes |
|-------|----------------|
| `id` | `M-northstar`, … — **one id per row**, and **a changed definition mints a NEW id**, never reuses the old (else the series compares incomparables) |
| `name` / `definition` | what it is, precisely — incl. exclusions and, for an outcome/cohort node, **the observation window** |
| `unit` | $ · € · % · count · … (a property of the node, not of a reading) |
| `kind` | `measured` · `derived` (state the formula) |
| `parent` | the node it feeds; `— to clarify —` before Step 4 |
| `population` | who is counted **by default**; an empty `population` in the csv means *this* value |
| `instrumentation` | `instrumented` · `proxy` · `not-instrumented` |
| `target` | the goal + horizon |
| `owner` | who owns it |
| `source` | metric source slot |
| `note` | qualifiers an enum cell may not carry (`since 2026-05`, a caveat) — **an enum cell holds the bare value** |

**`metrics.csv` — append-only dated readings**, one row per reading:

```csv
id,period_start,period_end,measured_at,value,observed_n,population,basis,source,note
```

- `measured_at` = when the reading was taken; `period_start/period_end` = the interval the value
  describes (empty for point-in-time). Collapsing them makes every trailing-window metric lie.
- `observed_n` = how many of the population **could already have shown the outcome** — the rate's
  denominator. A cohort metric divides by the observed, never the whole cohort; a plain count that
  is no rate's numerator leaves `observed_n` empty. **An empty `value` means the outcome was not
  observable yet** — never a word inside a numeric column.
- `basis` = **how the value was computed**, nothing else (`operational` · `with_depreciation` ·
  `metered` · `fact` …). *Who* was counted is `population`; *which slice* is a node of its own.
  Rows are comparable across `basis`, not across `population`.
- Rows are appended, never edited or deleted. Every csv `id` must be defined in `metric-tree.md`
  (check E) — lint after every csv write.

**Where metric readings live (hard rule).** Any captured metric value goes into **`metrics.csv` as a
dated row at capture time**, even before Step 4 builds the tree. A raw capture in `sources/` is
*evidence of the reading*, not its home: the csv holds the series, the source holds the context. The
capture procedure — [`metrics-capture`](../tool-skills/operations/metrics-capture/SKILL.md).
