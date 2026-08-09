<!--
  template-fragment: metrics-capture → writes a whole file, product/sources/<source>-method.md
  (node_type: source-method), plus the csv rows it justifies.
  Follow process/CONVENTIONS.md. ⚙️ = agent proposal awaiting approval.
  The file is LIVING: rewritten in place when the derivation changes, never dated evidence.
  One method file per (source × derivation), not one per capture.
-->

# Source-method template (`product/sources/<source>-method.md`)

```markdown
---
node_type: source-method
title: "<source> → <what it yields> — derivation"
source: <relative path to the access file, e.g. ./analytics-access.md>
feeds: [M-activation, M-retention-30d]
status: draft
updated: <YYYY-MM-DD>
---

# <source> → register values

**Question it answers.** <which node / hypothesis waits on these numbers, and what decision moves>

**Source & access.** <one line — what the source is>; access, verification and recovery live in
[`<access-file>.md`](./<access-file>.md) and are not repeated here.

## Population

| | Rule | Why | Confidence |
|---|---|---|---|
| **Included** | <who counts> | <reason> | [sourced: <where the rule comes from>] |
| **Excluded** | <test accounts / internal staff / soft-deleted / trials / …> | <reason> | [assumption] ⚙️ |
| **Identity** | <how keys fold to one person or account; or "one row = one account, folding not needed"> | <reason> | [validated: <check>] |

<Every line above is a judgement call. A material exclusion was confirmed by the human — record
which, and when.>

## Window & observability

- **Observation window:** <e.g. 30 days from signup — the outcome is countable only once it elapses>
- **`observed_n`:** <how it is computed — the members whose window has elapsed as of `measured_at`>
- **Not-yet-observable periods** are written as rows with an empty `value`, never as `0`.

## Derivation

- **Where it lives:** <path OUTSIDE the repository if the instance sits in a repo with an external
  origin — only this reference goes inside>
- **How to re-run:** <exact command / steps>
- **What it emits:** <the columns, and how they map to metrics.csv fields>
- **`basis`:** <how the value is computed — and nothing about who was counted>

## Verification

| Check | Method | Result | Date |
|---|---|---|---|
| <e.g. total reconciles with billing> | <how it was checked> | <matched / diverged by X, explained by …> | <YYYY-MM-DD> |

<A reading nobody verified carries [assumption], however precise it looks.>

## Known limits

- <what this derivation cannot see — an event not instrumented before a date, a segment missing
  from the source, a known double-count>

## Change log

### <YYYY-MM-DD> — <one-line summary>
- **From → To:** <the derivation before> → <the derivation now>
- **Why:** <reasoning>
- **Trigger:** <a migration, a redefined event, a failed verification, …>
```

## The rows it justifies

Appended to `registers/metrics.csv` — never edited, never deleted; one row per population and per
basis:

```csv
id,period_start,period_end,measured_at,value,observed_n,population,basis,source,note
M-retention-30d,2026-05-01,2026-05-31,2026-07-02,0.41,318,all_accounts,fact,analytics-method,
M-retention-30d,2026-05-01,2026-05-31,2026-07-02,0.57,96,paying,fact,analytics-method,
M-retention-30d,2026-06-01,2026-06-30,2026-07-02,,0,all_accounts,fact,analytics-method,window not elapsed
```

Read the third row as: the outcome for the June cohort was **not observable** at capture time — an
empty `value`, not a zero. The first two are the same period and the same basis for two populations,
which is why they are two rows.

**Then:** update the node in `metric-tree.md` where the pass taught you something (`instrumentation`,
default `population`, a `note`), add the file to `sources/INDEX.md`, write a change-log entry naming
the ids it moved, delete the raw capture, and run `python3 tools/lint.py <instance>` to 0 errors.
