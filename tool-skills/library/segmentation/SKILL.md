---
name: segmentation
kind: method
produces: segments
reads_registers: []
writes_registers: [hypotheses]
inputs: [interview, kb, metrics]
prerequisites: [concept, audience-knowledge-or-analytics]
used_by_steps: [1]
opinionated: false
method_basis: "JTBD / needs-based segmentation, priority-tiered (segment by the job/context, not demographics)"
evidence_standard: primary-research
volume_rule: "≥3 candidate cuts on different bases (situation · job · behaviour · buying trigger) before one is chosen"
selection_rule: "priority tiers 1–3 on need-difference × reachability × fit with the moat; ⚙️ proposed, human decides; lower tiers kept, never deleted"
rejects_shown: required
status: draft
version: 0.2.3
updated: 2026-08-09
---

# Segmentation

Define **who the product is for** and how the audience is cut into segments. Fills the
`segments` section of the concept (Step 1). Good segments are the foundation for problems
(`segment-pains`), positioning, and channels — get them wrong and everything downstream drifts.

## When to apply

- Step 1: to name the initial segments as the product's audience hypothesis.
- Whenever the audience is fuzzy, or metrics reveal a segment that behaves differently.

## Principles of a good cut

- **Actionable, not demographic-by-default.** Cut by something that changes what the product
  must do or how you reach them (job, context, behavior, willingness to pay) — not by age/geo
  unless that actually drives behavior.
- **Distinct.** Segments should differ in problem, value, or reachability. If two segments
  want the same thing the same way, they're one segment.
- **Reachable.** You must be able to name *where* to find each segment. A segment you can't
  reach is a daydream.
- **Few.** Start with 1–3. More segments early is usually false precision.

## Prerequisites

Checked before the tool runs. If missing, the agent asks or offers to help obtain it.

- **Concept** — what the product is (from `{#idea}`). *Missing → run `concept-formation` first.*
- **Audience knowledge or analytics** — any existing sense of who uses/buys it: interviews,
  usage data, market notes. *Missing → offer `interview` (prep the guide) or a scoped
  desk-research pass (`loops-research` brief per `references/evidence-standards.md`); at
  `concept-viability` this is expected to be thin, so cuts stay `[assumption]`.*

## How to do it

1. **List at least 3 candidate cuts on different bases** — job-to-be-done, use context, behaviour,
   buyer vs user, buying trigger, willingness to pay. Then pick the cut that best predicts *different
   needs*, and **record the bases you rejected and why**. One cut, arrived at directly, is not a
   choice: the first cut anyone proposes is almost always the one the org is already structured
   around (industry, company size), which is the cut least likely to predict need.
2. **Name 1–3 segments** on that cut. For each: a one-line description and *why it matters*
   (size, urgency, fit with the moat).
3. **State reachability** — where each segment is found (a channel, a place, a community).
4. **Rank into priority tiers** — assign each segment a priority (1 = lead, 2 = next, …) on three
   stated grounds: **how sharply its needs differ** from the others (a tier that needs the same thing
   as tier 1 is not a separate segment), **reachability** (can we get in front of it at all), and
   **fit with the moat** from `value-definition`. Say which ground decided each placement; a tier
   order with no stated ground is a preference. ⚙️ the agent proposes the lead; the human decides.
   Everything downstream (problems, solution, value) leads with the priority-1 segment; lower tiers
   are kept, not dropped.
5. **Tag confidence & seed hypotheses — and name which evidence the cut rests on.** Say plainly
   whether this segmentation comes from customer conversations, from usage data, or from desk
   research, because the three fail differently and a reader cannot tell them apart from the table.
   Each segment is `[assumption]` until evidenced; turn "segment X exists and is reachable at Y" into
   an `H-…` for the register.

## Anti-patterns

- **Demographic reflex.** Cutting by age/geo when behavior/job is what actually differs.
- **Everyone is a user.** No cut at all, or a segment so broad it's meaningless.
- **Unreachable segment.** Named but with no idea where to find them.
- **Too many too early.** Five segments before there's a single validated one.

## Worklog & projection

The working is done in the step's **worklog** `<step-folder>/segmentation.md` (`node_type: worklog`,
e.g. `1-concept/segmentation.md`): the ≥3 candidate cuts on different bases with the ones **rejected
and why**, the 1–3 named segments with their reachability, and the priority-tier ranking with the
ground (need-difference · reachability · fit with the moat) that decided each placement. That worklog
is the **source of truth**; the artifact section `{#segments}` is its **projection** into the fixed
shape of [`template-fragment.md`](template-fragment.md) — it holds nothing the worklog does not, and
the step's change-log history lives in the worklog, not the section
(`process/CONVENTIONS.md` → *Step folders & worklogs*). External inputs arrive here dispatched from
`sources/` by `source-intake`, cited in the worklog, never linked from the artifact.

## Output

Projects `{#segments}` via [`template-fragment.md`](template-fragment.md) from the worklog; inputs
gathered via [`questions.yaml`](questions.yaml).
