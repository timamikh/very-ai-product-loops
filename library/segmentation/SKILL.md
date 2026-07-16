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
status: draft
version: 0.1.0
updated: 2026-07-16
---

# Segmentation

Define **who the product is for** and how the audience is cut into segments. Fills the
`segments` section of the passport (Step 1). Good segments are the foundation for problems
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

- **Concept** — what the product is (from `{#concept}`). *Missing → run `concept-formation` first.*
- **Audience knowledge or analytics** — any existing sense of who uses/buys it: interviews,
  usage data, market notes. *Missing → offer `interview` or `analytics-search`; at
  `concept-viability` this is expected to be thin, so cuts stay `[assumption]`.*

## How to do it

1. **List candidate cuts** — by job-to-be-done, use context, behavior, buyer vs user, or
   willingness to pay. Pick the cut that best predicts different needs.
2. **Name 1–3 segments** on that cut. For each: a one-line description and *why it matters*
   (size, urgency, fit with the moat).
3. **State reachability** — where each segment is found (a channel, a place, a community).
4. **Rank into priority tiers** — assign each segment a priority (1 = lead, 2 = next, …). ⚙️ the
   agent proposes the lead; the human decides. Everything downstream (problems, solution, value)
   leads with the priority-1 segment; lower tiers are kept, not dropped.
5. **Tag confidence & seed hypotheses.** Each segment is `[assumption]` until evidenced;
   turn "segment X exists and is reachable at Y" into an `H-…` for the register.

## Anti-patterns

- **Demographic reflex.** Cutting by age/geo when behavior/job is what actually differs.
- **Everyone is a user.** No cut at all, or a segment so broad it's meaningless.
- **Unreachable segment.** Named but with no idea where to find them.
- **Too many too early.** Five segments before there's a single validated one.

## Output

Fills `segments` using [`template-fragment.md`](template-fragment.md). Inputs gathered via
[`questions.yaml`](questions.yaml).
