---
name: metrics-capture
kind: research
produces: product-loops/<step-folder>/metrics-capture.md
reads_registers: [metrics, hypotheses]
writes_registers: [metrics]
inputs: [metrics, kb]
prerequisites:
  - the question the number must answer (a metric node, a hypothesis, or a gate item that is blocked without it)
  - a reachable source — its access file in `sources/`, or the access needed to write one
  - a decision on who counts (population + exclusions) — proposed by the agent, confirmed by the human
used_by_steps: [any]
opinionated: true
method_basis: "Reproducible measurement: a declared population, a declared observation window, a written derivation, and an independent recount before the value is trusted"
status: draft
version: 0.2.1
updated: 2026-08-17
---

# Metrics capture — from a source to a register row

**What it is.** The pass that turns a **source** (a database, an analytics tool, an admin panel, a
billing export, a hand count) into **dated rows in `registers/metrics.csv`** and a **derivation
worklog** — `<step-folder>/metrics-capture.md` in the folder of the step whose need triggered the
capture (`node_type: worklog`) — that says how those rows were derived. The worklog is agent
reasoning, so it lives with the worklogs; `sources/` holds only what comes from outside — the
source's **access file** stays there, and the worklog cites it. Every other tool in the framework starts
after this one: the metric tree wants "the register seeded with captured readings", retention wants
"usage data with a per-user timestamp", unit economics wants a real churn rate rather than an assumed
one. This is the skill that produces what they consume.

**Why it is an operations skill, not a library method.** It fills no section of any step artifact and
belongs to no step. It is triggered by an event — a number is missing, or has gone stale — and it acts
on the instance's registers and sources. Its product content is entirely determined by the metric node
it serves; what it contributes is *how the pass is run*.

**The one thing it exists to prevent.** A number that nobody can reproduce. A reading whose population
and window live only in the head of whoever wrote the query is not evidence — it is an assumption
wearing a decimal point, and it will be compared next quarter against a differently-derived number by
someone who has no way to know.

## When to apply

Triggered by events, not by a step:

1. **A step or gate item needs a value the register does not hold** — the honest move is to capture it,
   not to write `— to clarify —` when the source is one query away.
2. **A hypothesis moves to `testing`** and its metric has no readings, or none inside the window the
   test needs.
3. **A reading has gone stale** — the period it describes has passed and a decision is about to lean on
   it. (What "stale" means per node is an instance decision; if a cadence is agreed, record it in the
   node's `note`.)
4. **A source changed** — new instrumentation, a migration, a redefined event. Re-capture, and see step
   2 below on when this must mint a new id instead of appending to the old series.
5. **On request** — the human asks for a number.

The pass ends the way any pass of the [operating loop](../../../process/OPERATING-LOOP.md) ends: register
updates and a change-log entry. "I only collected data" does not skip Update state.

## Prerequisites

- **The question, before the source.** Which node (`M-…`), which hypothesis (`H-…`), or which gate item
  is waiting on this number. Without it you will measure what the source makes easy.
- **A reachable source.** If it has no access file in `sources/`, writing one is part of this pass —
  what it is, how to connect, how to verify, how to recover. Never a token value, only where it lives.
- **A decision on who counts.** The agent proposes (⚙️) and the human confirms; a material exclusion is
  a fork, not a detail. Never guess it silently — a guessed population is the defect this skill exists
  to prevent.
- **Somewhere to work that is not the repository**, if the instance is vendored into a repo with an
  external `origin` — see CONVENTIONS → *Raw data & access*.

## How to do it

**1 · Name the question, then find the source.** Write down which node or hypothesis the number serves
and what decision changes depending on the answer. If nothing changes, stop — you have found a metric
worth deleting rather than capturing.

**2 · Read what already exists before computing anything.** Open the node in `metric-tree.md`: its
`definition` (including what it excludes and its observation window), its default `population`, its
`unit`, its `instrumentation`. Then read the existing rows for that id in `metrics.csv`. Two outcomes
matter:

- **Your derivation matches the definition** → you are appending to a series. Good.
- **It does not** → you are not capturing a reading, you are redefining the metric. A changed definition
  **mints a new id**; it never reuses the old one. Silent redefinition is the worst available outcome:
  the chart stays continuous while the meaning underneath it changes.

**3 · Declare the population, in writing.** Who is in, who is out, and why — test accounts, internal
staff, deleted or soft-deleted rows, trials, refunded orders, accounts below a size threshold. Then
**identity**: whether one human can hold several accounts, and how keys fold if so. Every one of these is
a judgement call, so each carries a confidence tag in the method file, and the material ones go to the
human before the number is computed rather than after.

**4 · Decide what is observable.** For any outcome or cohort node: which members have had the full
observation window elapse as of `measured_at`. That count is `observed_n`, and it is the **denominator**
— never the whole cohort. Where the window has not elapsed, the row is written with an **empty `value`**;
that is the framework's way of saying "not observable yet", and it is not the same as zero. This is the
step people skip, and skipping it produces a plausible number that is simply false.

**5 · Compute, with the derivation kept outside the repository.** Where the instance sits in a repo with
an external origin, the query or script and the raw rows it reads live outside it; only a reference goes
inside. Prefer a script you can re-run over a click path you can only describe — reproducibility is the
whole point, and a UI that changes next month takes an unrepeatable procedure with it.

> **Web analytics (GA4, Yandex Metrika and kin).** The counter / property id, the exact report or
> API query, the date range, the segment and the **sampling state** are all part of the derivation:
> `basis` names the tool and the query (`GA4 API runReport · sessions · 2026-07`), never just
> "analytics", and a sampled number is an estimate and says so in `note`. Prefer the API or a saved
> export over reading numbers off the UI — a click path is not reproducible, and the UI resegments
> silently between visits. If the agent has no access, the access file names who does, and the
> export is requested from the human (`questions.yaml`) — that export then lands in `sources/` and
> the worklog cites it.

**6 · Verify before you believe it.** At least one independent check, and say in the method file which one
you ran:

- recompute a different way (a total from a sum of parts, a rate from its two counts);
- reconcile against a number owned elsewhere (billing, an existing dashboard, a known headcount);
- sanity-check the shape — a share above 100%, a count above the entire base, a period-over-period jump
  with no event behind it.

A check that fails is a finding, not an obstacle: it usually means the population or the join is wrong,
and it is far cheaper to learn it now than from a stakeholder.

**7 · Land it, then clean up.** In one pass:

- **Rows** appended to `metrics.csv` — `id`, the period the value describes, `measured_at`, `value`,
  `observed_n`, `population`, `basis` (how it was computed, and nothing else), `source`, `note`. One row
  per population and per basis; two populations are two rows, never one blended number.
- **The derivation worklog** `<step-folder>/metrics-capture.md` (`node_type: worklog`) — one per step
  folder, a dated block per capture pass, naming the ids it feeds and citing the source's access file
  in `sources/`; the csv row's `source` column points at this worklog. This is what makes the reading
  reproducible, which is the first question anyone asks about it. (An event-driven worklog needs no
  section marker — the linter's check P knows the name.)
- **`metric-tree.md` updated** where the pass taught you something about the node: `instrumentation`, the
  default `population`, a `note` for a qualifier the enum cannot hold.
- **A change-log entry naming the ids** it moved, with the *why* — this is what makes the item's history
  retrievable later.
- **Raw captures deleted** once their values have landed; they are never committed.
- **`python3 tools/lint.py <instance>` reports 0 errors** — check E catches a csv id with no definition,
  the commonest result of a hurried capture.

Then tell the human what landed, decoding each id in the same sentence, and name what you had to assume.

## Anti-patterns

- **Dividing by the un-observed.** The whole cohort as the denominator when part of it could not yet have
  shown the outcome. Produces a number that is wrong in a direction that always flatters the young cohort.
- **Measuring what is queryable.** Starting from the source instead of the question, and quietly
  substituting the nearest available event for the one the node defines.
- **Silent redefinition.** Appending to an existing series with a changed derivation. A new definition
  is a new id.
- **The blended number.** One value covering several populations or several bases because a split "looks
  noisy". The split is the finding.
- **Population in someone's head.** Exclusions applied in the query and written down nowhere; the next
  capture makes different ones and the series is incomparable with itself.
- **A number with no `measured_at`**, or one date doing the work of both the reading date and the period
  it describes — every trailing-window metric then lies to trend readers.
- **The raw export that stays "just for now."** It gets committed, and personal data is now in git
  history.
- **`sourced` without a derivation worklog.** A confidence tag claiming evidence for a derivation nobody
  can repeat; until it is written down, the reading is an assumption.
- **A capture that skips Update state.** Values in a file somewhere, registers untouched, no change-log
  entry — the pass did not happen as far as the next agent is concerned.

## Output

- Dated rows in `registers/metrics.csv` (the home of every value).
- A derivation worklog `product-loops/<step-folder>/metrics-capture.md` (`node_type: worklog`) via
  [`template-fragment.md`](template-fragment.md), citing the source's access file in `sources/`.
- No new file in `sources/` — that folder holds what comes from outside (the access file, a raw
  export the user keeps), never the agent's derivation.
- Inputs the agent cannot observe itself via [`questions.yaml`](questions.yaml).
