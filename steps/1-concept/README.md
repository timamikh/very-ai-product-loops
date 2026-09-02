---
node_type: card
kind: step
name: concept
step: 1
title: "Step 1 — Concept"
output: 1-concept.md
prerequisites: []
reads: [source:interview, source:kb, source:git, source:metrics]
writes: [section:*]
surfaces: [ticks, register:hypotheses, sign-off, change-log]
cadence: "~ product lifetime; revisit on pivot or major learning"
method_basis: "Concept as a positioning shift (Dunford) · JTBD/needs-based segmentation · severity×frequency pains · base/derivative moats (7 Powers, post-AI lens)"
status: draft
version: 0.6.0
updated: 2026-08-16
---
# Step 1 — Concept

**Goal.** Capture the product concept: who it's for, the problems they have, how the product
solves them, and its value/defensibility hypothesis. This is the long-lived source of truth
the rest of the loops build on.

This step is **thin by design** — it owns the *skeleton* of the artifact and the rules of the
game. The *how* of each section lives in [library](../../tool-skills/library/README.md) tools; the goal
emphasis is set by the active [status](../../statuses/README.md).

## Inputs (source slots)

`interview` (primary at this stage) · `kb` (existing product notes, if any) ·
`git`/`metrics` (usually empty this early — leave `— to clarify —`).

## Output

`1-concept.md` — assembled from the section skeleton below. Template: [`template.md`](template.md).

## Artifact skeleton

Each section has a stable ID and is filled by a recommended tool. Recommendations are soft —
swap or add tools per product (see [library](../../tool-skills/library/README.md)).

| Section (ID) | What | Recommended tool |
|--------------|------|------------------|
| `idea` | The idea in a few lines: what it is, the shift it makes | `concept-formation` |
| `jtbd` | The job + the four forces that gate switching (anchors segments/pains; feeds Step 2 substitutes) | `jtbd-concept` |
| `segments` | Who it's for — segments and how they're cut | `segmentation` |
| `problems` | Each segment's problems (severity × frequency) | `segment-pains` |
| `cjm` (optional) | The segment's journey over time — where it breaks (the temporal view behind `problems`) | `cjm-concept`, `cjm-strategy` (Step-3 revisit) |
| `solution` | How the product solves each problem | `concept-expansion` |
| `value-defensibility` | Value and moats (base; derivatives deferred to Step 3) | `value-definition-concept`, `value-definition-strategy` (Step-3 revisit) |

## Register touchpoints

- **Hypotheses** — seeds the register. Every segment, problem, and value claim starts as
  `[assumption]` and becomes an entry in the hypothesis register with an ID (`H-001`, …).
- **Risks / Metrics** — not born here (risks: Steps 2–4; metrics: Step 4). Do not force them.

## Gate checklist ("step is defended" — soft)

Reports what's open; does not block descent. **Each item validates a specific artifact
section** (the rule for every step: a checklist item always names the section/artifact it
checks, so "done" is verifiable, not vibes).

- [ ] states what the product is and the shift it makes → `concept#idea`
- [ ] the customer's job stated with its four forces (push/pull/anxiety/habit) → `concept#jtbd`
- [ ] at least one segment named, with its cut rationale → `concept#segments`
- [ ] each named segment has ≥1 problem with severity × frequency → `concept#problems`
- [ ] (optional) journey mapped where a drop-off needs explaining → `concept#cjm`
- [ ] solution maps to the stated problems, no orphan features → `concept#solution`
- [ ] intended moat(s) named, each with a confidence tag → `concept#value-defensibility`
- [ ] every claim carries a confidence tag; unknowns are `— to clarify —` → `concept#to-clarify`
- [ ] seeded hypotheses have IDs and are listed → `concept#hypotheses` → hypothesis register

## Cadence & invalidation

- **Cadence:** ~ product lifetime; revisit on a pivot or a major learning.
- **Invalidates downward:** a change to `segments`, `problems`, or `value-defensibility`
  flags Analysis (2) and Strategy (3) for review.
- **Invalidated from below:** a refuted core hypothesis (from any lower loop) triggers a
  revisit here.

## The human's role

Decide at the forks the agent surfaces (which segment to lead with, which moat to bet on).
The agent drafts everything else from sources and marks its proposals with ⚙️.
