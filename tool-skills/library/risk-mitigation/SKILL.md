---
node_type: card
kind: method
name: risk-mitigation
steps: [4]
prerequisites: [carried risks in the R- register]
reads: [register:risks]
writes: [worklog, section:risk-mitigation, register:risks]
opinionated: false
method_basis: "Risk-register upkeep: mitigation + owner + observable trigger + review date per carried risk; lifecycle status written back"
evidence_standard: decision
volume_rule: n/a
selection_rule: n/a
rejects_shown: n/a
status: draft
version: 0.4.2
updated: 2026-09-02
---
# Risk Mitigation

Make every carried risk **managed**: each `R-…` gets a **mitigation**, an **owner**, an
**observable trigger**, and a **status** — written back into the R- register, never into a copy of
it. Fills `{#risk-mitigation}` at Step 4.

**Method basis.** Risk-register upkeep. Surfacing and triage happen upstream (see the boundary
below); this method takes the carried set and attaches what makes a risk actionable: what we'll do,
who acts, what signal says "act now", and when the plan is next reviewed.

> **Upstream boundary (one mechanism, one way).** Carried `R-…` arrive from `pre-mortem` at Step 3
> and from `niche-risks` at Step 2. Those methods surface and triage (probability × impact,
> carried · parked · dropped); this one does neither — it never re-runs the pre-mortem or re-scores
> the set. A new risk surfacing at Step 4 goes back through the register with a triage note, not
> around it.

## When to apply
- **Step 4**, once the plan's numbers exist — attach a mitigation, owner, trigger, and review date
  to every carried risk before the plan is signed.
- When a live risk changes (trigger fired, mitigation landed, risk no longer credible): update the
  same register row's status — don't open a new one.

## Prerequisites
- **Carried risks in the R- register** — the triaged set marked `carried`, with their P×I scores.
  *Missing → run `pre-mortem` (Step 3); niche-level risks arrive from `niche-risks` (Step 2).*

## How to do it
1. **Pull the carried set.** Read the R- register for every risk marked carried; don't re-invent or
   re-score them — the P×I score travels with the row from triage.
2. **Assign a mitigation.** What we will actually do about the risk — an action, not a hope
   ("monitor closely" is not a mitigation unless the monitoring has a trigger and a response).
3. **Name the owner.** One person who acts when the trigger fires. A committee is not an owner.
4. **Set the observable trigger and the due date.** Two different columns, two different things:
   the **Trigger** is the observable signal that says "act now" (a metric crossing a line, an event
   occurring); the **Due** is the date the mitigation is *reviewed* — the moment somebody checks
   whether it still holds, even if the trigger never fired. A risk with a trigger but no review date
   rots silently; one with a date but no trigger gets acted on too late.
5. **Set the status and upsert the register.** Write mitigation, owner, trigger, due, and lifecycle
   status into the **same** R- row — one row per risk, upserted, never forked into a step-local
   copy. The register is the single home; this section projects it.

## Scales
The risk **lifecycle** — `open` → `mitigating` → `contained` → `realized` → `closed`, plus the
off-cycle `accepted` — is defined in [`process/reference/scales.md`](../../../process/reference/scales.md) and written back to the
register's `status` from here. The likelihood × impact scale (H/M/L backed 5/3/1) belongs to the
triage upstream in `pre-mortem`; the score arrives on the row and is not re-derived.

## Anti-patterns
- **No owner / no trigger.** A risk logged but unassigned, with nothing that says when to act.
- **Trigger and due conflated.** "Review in Q3" written as the trigger — then nobody acts when the
  signal actually fires in July.
- **Mitigation theatre.** "Monitor" / "be careful" as the mitigation — no action, no owner, nothing
  falsifiable.
- **Register fork.** Copying the carried risks into a step-local table that then drifts from R- —
  upsert the register; the section is a projection.
- **Re-triaging here.** Re-scoring or re-litigating the carried set — that argument belongs in
  `pre-mortem`'s worklog, where the dispositions and reasons live.

## Worklog & projection
Worklog: `4-strategic-plan/risk-mitigation.md` — the carried set pulled from the R- register and, per risk, mitigation · owner · trigger · due · status with the reasoning. Projects `{#risk-mitigation}`; face: the **Exposure read** line, via [`template-fragment.md`](template-fragment.md). The register row is the home; the section projects it. Path form, primary/contributing and revisit rules: [`worklog-resolution.md`](../../../process/reference/worklog-resolution.md).

## Output
Projects `{#risk-mitigation}` via [`template-fragment.md`](template-fragment.md) from the worklog;
inputs via [`questions.yaml`](questions.yaml). Upserts mitigation · owner · trigger · due · status
into the R- register — one row per risk, the same row triage filled upstream.
