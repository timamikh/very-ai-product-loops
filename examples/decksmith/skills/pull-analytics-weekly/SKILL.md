---
node_type: instance-exchange-skill
name: pull-analytics-weekly
direction: pull
cadence: "weekly, Mon"
reaches: sources/access/product-analytics.md
lands_via: metrics-capture
status: draft
version: 0.1.0
updated: 2026-08-18
---

# Pull — weekly product analytics (fictional)

**What it is.** Decksmith's own exchange skill: a repeatable **pull** that captures last week's
activation / generation / export counts from the product analytics panel into a dated snapshot, so
`metrics-capture` can land them into the metric register. It is a *card* — the goal map routes to it
by trigger; the skeleton runs it like any pass. The panel goes live with the prototype; until then
this is a registered, un-run recipe (see `state.yaml → last_run`).

**Direction:** pull (reads the outside world; writes only to `sources/snapshots/`). It never touches
a register itself — landing is a separate cycle pass.

## Preconditions

1. The passport [`../../sources/access/product-analytics.md`](../../sources/access/product-analytics.md)
   resolves (point reachable, reach verified per its *How to verify reach*). If it does not, stop and
   raise it as an open item — do **not** invent a source.
2. The analytics token is in the operator's own secret store (never in the repo). If absent, stop and
   recover access per the passport, then rerun.

## Run

A script and a prose recipe are equal kinds of run recipe (N4 — read this file before either runs):

1. Sign in to project `decksmith-proto` per the passport.
2. Export last completed ISO week (Mon–Sun) for events: `activation`, `generation`, `export`.
3. Write the export verbatim to `../../sources/snapshots/analytics-<YYYY-Www>.csv` (dated, immutable).
   Aggregate counts only — **no product-user personal data** in the snapshot (N8; if the export
   carries any, it is a raw capture: keep it outside the repo and land the aggregate).

## Verify

- The snapshot's week matches the ISO week requested and its row count is non-zero.
- The event names match the three above; an unexpected column stops the run for review.

## On failure

- Reach fails → recover access per the passport; if it still fails, raise an open item at move 0.
- The panel is empty (pre-launch) → expected until the prototype ships; skip and leave `last_run` as is.

## Landing

The snapshot is **not** a register value. Hand it to `metrics-capture`, which lands each count into
the metric register (population + window + derivation + recount, then move 5 records it). Idempotent:
landing reconciles by `id + period`, so a re-pulled week makes no duplicate row.

## Cadence

`cadence: "weekly, Mon"` — a **reminder**, not a daemon. An overdue pull is discovered at session
start (`start-work` compares this cadence against `state.yaml → last_run.pull-analytics-weekly`),
never by a background scan. This skill is run by the orchestrator, never delegated.

## Change log

### 2026-08-18 — created
- **From → To:** — → weekly analytics pull registered (recipe + cadence), awaiting the live prototype
- **Why:** demonstrate an instance exchange skill end-to-end (passport → snapshot → landing) and give
  `check T` a live skill to validate
- **Trigger:** framework 0.10 boundary layer
