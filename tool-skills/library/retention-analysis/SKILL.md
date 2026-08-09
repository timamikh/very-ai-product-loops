---
name: retention-analysis
kind: method
produces: retention
prerequisites: [usage metrics with a per-user/per-account timestamp, the activation/active definition]
reads_registers: [metrics, hypotheses]
writes_registers: [hypotheses, metrics]
inputs: [metrics, kb]
used_by_steps: [4]
opinionated: true
method_basis: "Cohort retention curve (does it flatten?) + usage-frequency / engagement-loop analysis + resurrection; the flattening retention curve is the PMF signal and the real input to LTV/churn — not an assumed churn %"
status: draft
version: 0.2.1
updated: 2026-08-09
---

# Retention Analysis

Read whether **value repeats**: build the **cohort retention curve** (does it flatten at a
non-zero floor?), characterize **usage frequency / the engagement loop**, and find where users
**drop off** and where they **resurrect**. Fills `{#retention}` and supplies the real churn/retention
input that `unit-economics` (LTV) and `financial-model` (churn scenarios) otherwise only assume.

**Method basis.** A cohort retention curve that **flattens above zero** is the classic
product-market-fit signal — a segment for whom value recurs. A curve that decays to zero has no
retained value no matter how good acquisition looks. Retention is read *by cohort* (not a single
blended churn %), against the product's **natural usage frequency** (daily/weekly/monthly — a
metric that judges a monthly product on daily use lies), and paired with the **engagement loop**
(trigger → action → reward → investment) that would bend the curve up.

> **Relation to neighbours (one mechanism, one way).**
> - `metric-tree` **defines and measures** the retention/engagement nodes (`M-…`) — that's where
>   the number lives. `retention-analysis` is the **method that reads the curve and its drivers**
>   and decides what to do about it; it writes readings to `metrics.csv` and node needs to
>   `metric-tree`, it does not redefine the register.
> - `unit-economics` turns retention into **LTV** and `financial-model` turns it into **churn
>   scenarios** — both *consume* a retention/churn input. Without this tool that input is an
>   assumption; with it, it's a measured curve. Supply the curve here; don't compute LTV here.
> - `segment-pains`/`jtbd` explain *why* value does or doesn't recur; this tool measures *whether*
>   it does.

## When to apply
- **Step 4**, once there is enough usage history to form cohorts (typically `pmf`/`growth`). Build
  the curve, name the flattening floor (or its absence), and feed churn/retention into the
  economics and model.
- When LTV or the financial model rest on an *assumed* churn number — replace the assumption with
  the measured curve.
- When acquisition is up but revenue isn't compounding — the curve usually explains it.

> At `concept-viability` there is rarely enough data for cohorts; use `interview`/`segment-pains`
> for the *why-they'd-return* signal and revisit this tool once usage history exists.

## Prerequisites
- **Usage metrics with a per-user / per-account timestamp** — needed to form cohorts and a curve.
  *Missing → run [`metrics-capture`](../../operations/metrics-capture/SKILL.md) (operations) to pull and
  land them, or instrument the event first (`product-surface`).*
- **The activation / "active" definition** — what counts as a retained active use (the curve is
  meaningless without a crisp "active"). *Missing → define it (a `metric-tree` node) before reading.*

## How to do it
1. **Define "active" and the natural frequency.** State what a retained active action is and the
   product's natural cadence (daily/weekly/monthly). Read retention on that cadence.
2. **Build the cohort curve.** Group users by join period; plot % still active at N periods.
   Read the **shape**: does it flatten at a non-zero floor (value recurs), or decay to zero (no
   retained value)? The floor height and where it flattens are the headline.
3. **Divide by the observed, never by the cohort.** At period N the denominator is only the members
   who joined at least N periods ago — the rest are **censored**: their window has not elapsed, so
   they cannot yet have shown the outcome. Count them and the newest cohorts look worst for a reason
   that is purely arithmetic. Write that count into the reading's `observed_n`; where nothing is
   observable yet, leave `value` empty rather than publishing a zero (REGISTERS → `metrics.csv`).
   State the observation window in the node's definition, so the next reader inherits it.
4. **Segment the curve.** Split by segment / plan / acquisition channel — a blended curve hides a
   retained core inside a churning average. Name the cohort that retains best (often the real
   target segment).
5. **Characterize the engagement loop.** Map trigger → action → reward → investment for the
   retained core: what brings them back, and what the drop-off cohorts never reached. Locate the
   **drop-off point** (where the curve bends down) and any **resurrection** path.
6. **Write readings back and feed the economics.** Append the retention/churn readings to
   `metrics.csv` (dated rows) against their `M-…` nodes; hand the curve to `unit-economics` (LTV)
   and `financial-model` (churn scenario). If a node is missing, flag it for `metric-tree`.
7. **Seed hypotheses.** Each driver you'd act on → `H-…` (`type: desirability`/`usability` — will
   *this change* bend the curve). Retention bets are tested via `hypothesis-test-design`.

## Anti-patterns
- **Dividing by the un-observed.** A period-N rate computed over everyone who ever joined, including
  members who *cannot yet* have reached period N. The result is plausible and simply wrong, and the
  error survives into every comparison: two groups then differ by their age, not their behaviour.
  Report `observed_n` beside the value; an unobservable outcome is an empty `value`, not a zero.
- **Blended churn %.** A single company-wide number hides a retained core inside a churning
  average — always read by cohort and segment.
- **Wrong frequency.** Judging a monthly-value product on daily retention (or vice-versa) — the
  curve lies.
- **Vanity "active".** Counting logins/opens as retention when they don't reflect the value action.
- **Assuming the curve.** Feeding `unit-economics`/`financial-model` a guessed churn when the data
  to measure it exists.
- **Recomputing LTV here.** LTV/contribution live in `unit-economics`; this tool supplies the
  retention input, it doesn't own the economics.

## Output
Fills `{#retention}` via [`template-fragment.md`](template-fragment.md); inputs via
[`questions.yaml`](questions.yaml). Writes retention/churn readings to `metrics.csv` and hands the
curve to `unit-economics` + `financial-model`; unproven drivers seed `H-…`.
