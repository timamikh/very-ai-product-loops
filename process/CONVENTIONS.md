---
node_type: conventions
title: Conventions — markers, IDs, links, change logs
status: draft
version: 0.1.0
updated: 2026-07-16
---

# Conventions

Shared notation used by every step template and library tool. Keeps artifacts machine-readable
(for aggregators, adapters, and the GitMark graph) while staying human-readable.

## Confidence tags

Every non-trivial claim ends with a confidence tag. A claim with no tag is treated as
`assumption`.

- `[assumption]` — stated, not yet backed by a source.
- `[sourced: <where>]` — backed by a document/metric/decision. Name it, e.g. `[sourced: metrics W24]`.
- `[validated: <evidence>]` — confirmed by evidence (an experiment, data, customer signal).
- `[refuted: <why>]` — tested and found false. Kept, not deleted (see change log).

Agent-proposed defaults awaiting human approval are prefixed with **⚙️**.

## Sources

`[sourced: ...]` names the origin. Source slots a tool/step may draw from:
`interview` · `metrics` · `git` · `kb` · `human-decision (dated)`.
Missing data is written literally as `— to clarify —`, never guessed.

## Section IDs

Every artifact section carries a stable ID so tools can fill it and links can target it:

```markdown
## Value & Defensibility {#value-defensibility}
```

IDs are kebab-case and stable across revisions — rename the heading text freely, keep the ID.

## Typed links & register item IDs

Register items have stable IDs:

- Hypotheses: `H-001`, `H-002`, …
- Risks: `R-001`, …
- Metric nodes: `M-northstar`, `M-activation`, …

Reference them inline in brackets, e.g. "drives `M-activation`" or "tests `H-003`".
Cross-artifact links use GitMark-lite: `[[analysis#opportunity]]`, `[[strategy#bets]]`.

## Change log

Every artifact ends with a change log. Narrative artifacts included — the log carries the
*motivation*, not just the diff. Newest entry first.

```markdown
## Change log

### 2026-07-16 — <one-line summary>
- **From → To:** <what the state was> → <what it is now>
- **Why:** <reasoning>
- **Trigger:** <what prompted it — a metric shift, a refuted hypothesis, a decision, …>
```
