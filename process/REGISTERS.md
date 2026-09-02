---
node_type: registers
title: Registers — metrics, hypotheses, risks, features
status: draft
version: 0.14.0
updated: 2026-09-02
---

# Registers

**Four registers, six files, five id prefixes** — this table is the one enumeration; every other
file points here. Living, vertical objects shared across all steps — born once, refined downward,
results flowing back up, **not re-authored per step**. In an instance: `registers/` at the instance
root (`product-loops/` in a live product). Confidence tags and change logs follow
[`CONVENTIONS.md`](CONVENTIONS.md).

| Register | File(s) in `registers/` | Id prefix | Atom (`register:<name>`) |
|----------|-------------------------|-----------|--------------------------|
| Hypotheses | `hypotheses.md` | `H-` | `hypotheses` |
| Risks | `risks.md` | `R-` | `risks` |
| Metrics | `metric-tree.md` (node definitions) + `metrics.csv` (dated readings) | `M-` | `metric-tree` · `metrics` |
| Features & surfaces | `features.md` + `surfaces.md` | `F-` · `S-` | `features` · `surfaces` |

Numbered ids count sequentially and are never reused; a changed metric definition mints a new `M-`
id (below).

*Read this file at its named moments* (OPERATING-LOOP): **move 2** — pulling register rows as
inputs, when field semantics or gradations are in doubt — and **move 5** — before writing rows.
The register *values* live in the instance files, read on every pass that needs them.

**Creating the register files** (setup, or a lost file): copy the skeletons from
[`reference/register-skeletons/`](reference/register-skeletons/) **verbatim** — one file per
register, frontmatter plus the keyed table header (`<!--c:key-->`, what check D and the console
read), zero rows. Never retype a header from the field tables below: prose is not a carrier.

| Register | Born at | Refined at |
|----------|---------|------------|
| Hypotheses | Steps 1 (concept) · 2 (sizing) · 3 (bets) | 4 (quantify) → 5 (test design) → 6 (experiment tasks) |
| Risks | Steps 2 (niche) · 3 (product) · 4 (capability gaps) | 4 (mitigation) → 5 (period blockers) |
| Metric tree | Step 4 | 5 (select nodes) → 6 (task ↔ metric) |
| Features & surfaces | Steps 3 (surfaces: `product-surface` ledgers the designed ones `planned` pre-build, `product-baseline` inventories the live ones; live features via `product-baseline`) · 6 (planned feature candidates via the item specs; a new g2m surface via `activity-spec`) | 4 (strategic targets seed `priority`) → 5 (period goals finalize `priority`; item readouts flip `planned → live`) → 6 (sprint items advance their `F-…`) |

## Gradation vs confirmation — two orthogonal axes

**Confirmation** answers *has a human signed this?* — the binary section marker (CONVENTIONS →
*Section confirmation*). **Gradation** answers *how good is it?* — the ordinal scales carried inside
a register row (the enums below). The axes are independent: a reader renders **two chips**, never
folding one into the other.

## What earns a register — the four-sign test

A candidate is **tested, not argued**, on all four signs: a stable cross-step id · an enumerable
lifecycle (`status`) · a life outlasting the step that bore it · state that flows both ways. Fail
one and the home is a step artifact section. The full test —
[`extending/register.md`](../extending/register.md).

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
marker (*Gradation vs confirmation*, above). A refuted bet or a `reject`/`research` decision
can trigger an upward revisit (step cadence/invalidation). The test-selection **priority score**
(1/3/5 tiers) is not a register column — it is defined by
[`process/reference/scales.md`](reference/scales.md) and
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
| `trigger` | the observable act-now signal — fires the mitigation before the review date (added Step 4) |
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
- Rows are appended, never edited or deleted. The file holds data rows only — no comment or
  separator lines; a reading's context goes in its `note` column, a group's context in
  `metric-tree.md` prose. Every csv `id` must be defined in `metric-tree.md` (check E) — lint after
  every csv write.

**Where metric readings live (hard rule).** Any captured metric value goes into **`metrics.csv` as a
dated row at capture time**, even before Step 4 builds the tree. A raw capture in `sources/` is
*evidence of the reading*, not its home: the csv holds the series, the source holds the context. The
capture procedure — [`metrics-capture`](../tool-skills/operations/metrics-capture/SKILL.md).

## Feature register (`features.md` + `surfaces.md`)

What the product is made of — **as-is and to-be in one register, never two documents**: `state: live`
rows are the current product, `state: planned` rows are the accumulating candidates (a backlog that
survives between sprints because its items have ids). One register, two files, the metric register's
own split: **features in `features.md`, the surfaces they live on in `surfaces.md`** — surfaces are
few, long-lived, and referenced by id from features, sprint items and `3#product-surface`.

**`features.md`:**

| Field | Values / notes |
|-------|----------------|
| `id` | `F-001`, … (stable across sprints — a sprint item advances a feature, never replaces it) |
| `name` | the feature at feature altitude — "autopay", "the AI content line" — never a sprint task ("post id 123" is an item, not a row) |
| `direction` | which work direction owns it (instance config; default development · go-to-market · back-office) — **not** a linted enum, directions are config |
| `surface` | the `S-…` it lives on |
| `state` | `planned` · `live` · `retired` — as-is = `live`, to-be = `planned`; flipped by an item readout, never by hand mid-sprint |
| `priority` | `now` · `next` · `later` — the cascade's carrier: Step 4 seeds the structural weight (a feature whose `serves` target is a committed strategic target or a top risk outranks one moving a peripheral node), Step 5 finalizes by period fit (`now` = serves this period's goals), Step 6 reads it as a ranking input and adds only cost/confidence; **optional until those passes run** — a register that pre-dates the cascade legally lacks the column |
| `serves` | the `M-…` it moves / `R-…` it closes / `H-…` it tests — a feature serving nothing is a candidate to cut (the Step-6 rule, now with a home) |
| `owner` | who is accountable |
| `confidence` | `assumption` · `sourced` · `validated` · `refuted` — a `live` row needs a source; a `planned` row's expected impact is `[assumption]` until its readout |
| `source` | where the row came from (baseline inventory, a spec's pass) |
| `note` | qualifiers an enum cell may not carry |

**`surfaces.md`:**

| Field | Values / notes |
|-------|----------------|
| `id` | `S-01`, … |
| `name` / `purpose` | the surface and why it exists |
| `type` | free descriptor (landing · in-product · admin · mailing · content · channel · internal — or the product's own word); deliberately not an enum |
| `state` | `planned` · `live` · `retired` (same lifecycle as features) |
| `source` / `note` | provenance; qualifiers |

Rows are **born from sources, not from the head**: `live` rows by
[`product-baseline`](../tool-skills/library/product-baseline/SKILL.md) (Step 3 — product walkthrough,
analytics, interview), `planned` rows by the Step-6 item specs
([`feature-spec`](../tool-skills/library/feature-spec/SKILL.md) /
[`activity-spec`](../tool-skills/library/activity-spec/SKILL.md) /
[`task-spec`](../tool-skills/library/task-spec/SKILL.md)) when an item advances a feature the
register does not yet hold. Surfaces have the same doors, one per stage of existence: pre-build,
[`product-surface`](../tool-skills/library/product-surface/SKILL.md) (Step 3) ledgers the designed
surfaces as `planned` rows; once something ships, `product-baseline` inventories the live ones; and
a Step-6 `activity-spec` may mint a new go-to-market surface the strategy pass did not carry (a
community, a channel). The readout that flips state —
[`impact-readout`](../tool-skills/library/impact-readout/SKILL.md) (Step 5) — reads the item's
pre-registered expected impact against the fact and writes the verdict onto the row's `serves`
confidence. A cut candidate **stays** a `planned` row (with the cut noted), so prioritization never
silently loses it.
