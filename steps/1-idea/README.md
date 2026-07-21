---
node_type: step
step: 1
name: idea
title: "Step 1 — Idea / Concept"
output: 1-passport.md
cadence: "~ product lifetime; revisit on pivot or major learning"
method_basis: "Concept as a positioning shift (Dunford) · JTBD/needs-based segmentation · severity×frequency pains · base/derivative moats (7 Powers, post-AI lens)"
status: draft
version: 0.4.0
updated: 2026-07-21
---

# Step 1 — Idea / Concept

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

`1-passport.md` — assembled from the section skeleton below. Template: [`template.md`](template.md).

## Artifact skeleton

Each section has a stable ID and is filled by a recommended tool. Recommendations are soft —
swap or add tools per product (see [library](../../tool-skills/library/README.md)).

| Section (ID) | What | Recommended tool |
|--------------|------|------------------|
| `concept` | The idea in a few lines: what it is, the shift it makes | `concept-formation` |
| `jtbd` | The job + the four forces that gate switching (anchors segments/pains; feeds Step 2 substitutes) | `jtbd` |
| `segments` | Who it's for — segments and how they're cut | `segmentation` |
| `problems` | Each segment's problems (severity × frequency) | `segment-pains` |
| `cjm` (optional) | The segment's journey over time — where it breaks (the temporal view behind `problems`) | `cjm` |
| `solution` | How the product solves each problem | `concept-formation` |
| `value-defensibility` | Value and moats (base + derivative) | `value-definition` |

## Register touchpoints

- **Hypotheses** — seeds the register. Every segment, problem, and value claim starts as
  `[assumption]` and becomes an entry in the hypothesis register with an ID (`H-001`, …).
- **Risks / Metrics** — not born here (Steps 2 and 4). Do not force them.

## Gate checklist ("step is defended" — soft)

Reports what's open; does not block descent. **Each item validates a specific artifact
section** (the rule for every step: a checklist item always names the section/artifact it
checks, so "done" is verifiable, not vibes).

- [ ] states what the product is and the shift it makes → `passport#concept`
- [ ] the customer's job stated with its four forces (push/pull/anxiety/habit) → `passport#jtbd`
- [ ] at least one segment named, with its cut rationale → `passport#segments`
- [ ] each named segment has ≥1 problem with severity × frequency → `passport#problems`
- [ ] (optional) journey mapped where a drop-off needs explaining → `passport#cjm`
- [ ] solution maps to the stated problems, no orphan features → `passport#solution`
- [ ] intended moat(s) named, each with a confidence tag → `passport#value-defensibility`
- [ ] every claim carries a confidence tag; unknowns are `— to clarify —` → `passport#to-clarify`
- [ ] seeded hypotheses have IDs and are listed → `passport#hypotheses` → hypothesis register

## Cadence & invalidation

- **Cadence:** ~ product lifetime; revisit on a pivot or a major learning.
- **Invalidates downward:** a change to `segments`, `problems`, or `value-defensibility`
  flags Analysis (2) and Strategy (3) for review.
- **Invalidated from below:** a refuted core hypothesis (from any lower loop) triggers a
  revisit here.

## The human's role

Decide at the forks the agent surfaces (which segment to lead with, which moat to bet on).
The agent drafts everything else from sources and marks its proposals with ⚙️.

## Change log

### 2026-07-21 — cjm gets a home section `{#cjm}` (optional)
- **From → To:** cjm was a section-less lens whose output (`produces: cjm`) had nowhere to live → it
  now owns an **optional** `passport#cjm` (journey stages · touchpoints · emotion curve · pains),
  added to the artifact skeleton and a soft (optional) gate item. Mirrors the jtbd fix.
- **Why:** a tool that `produces:` a section with no home is the same homeless-output bug fixed for
  jtbd — the linter now catches it. cjm is optional (used when a drop-off needs explaining), so its
  section and gate item are marked optional, not required.
- **Trigger:** independent audit + wiring linter, 2026-07-21.

### 2026-07-21 — jtbd owns its own section `{#jtbd}`
- **From → To:** jtbd was a section-less Step-1 lens (seeded hypotheses only) → it now owns
  `passport#jtbd` (job statement + four forces + desired outcomes), added to the artifact skeleton
  and the gate checklist. `segment-cvp` remains a section-less lens at Step 1.
- **Why:** the lens produced durable, decision-shaping content (the forces — the anxiety that gates
  adoption; the job that frames indirect competition) with nowhere canonical to live, so it was lost
  and easy to skip. The job statement is also the required input to `substitutes` (Step 2), so a
  homeless jtbd broke indirect-competitor discovery downstream.
- **Trigger:** example run review — jtbd dropped from the Step-1 pass, 2026-07-21.

### 2026-07-16 — created (golden exemplar)
- **From → To:** — → Step 1 skeleton + `template.md` (passport), the anatomy the other steps mirror.
- **Note:** at `concept-viability`, `segment-cvp` acts here as a **lens** (surfaced via the status'
  per_step tools), seeding the hypothesis register without owning a passport section. (`jtbd` also
  did until 2026-07-21, when it was given `#jtbd` — see the entry above.)
- **Trigger:** Phase 1 / PR #2.
