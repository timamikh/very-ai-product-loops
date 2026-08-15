<!--
  template-fragment: source-intake → seeds/updates the INTAKE BLOCK of a step worklog,
  product-loops/<step-folder>/<tool>.md (node_type: worklog). It does NOT write a whole artifact section.
  Follow process/CONVENTIONS.md → Step folders & worklogs. ⚙️ = agent proposal awaiting approval.
  One intake block per worklog; each row is a single dispatched fact, dated and cited to its source.
  The reasoning below the block is the method's Act pass, not source-intake's.
-->

# Intake block (inside `product-loops/<step-folder>/<tool>.md`)

A worklog created by this skill carries the standard worklog frontmatter, then the intake block near
the top — the evidence the method works from, before any reasoning:

```markdown
---
node_type: worklog
tool: <tool>            # matches the artifact's <!-- tool: <tool> --> marker
step: <n>
title: "<tool> — the working"
updated: <YYYY-MM-DD>
version: 0.1.0
---

# <tool> — the working

_Source of truth for `<n>-<slug>.md#<section>`; that section is the projection of this file._

## Inputs dispatched from sources {#intake}

_Routed here by `source-intake` from `../sources/`. Each row is a fact the method works from; the
analysis and conclusions are worked below and projected into the artifact section — never here._

| From source | What it gives this method | Value / claim | Captured | Confidence |
|-----------------------------|------------------------------------------|------------------------------|---------------------------|--------------------------|
| `../sources/<file>.md` | <why this method needs it> | <the fact, as the source states it> | <YYYY-MM-DD> | [sourced: <slug>] |
| `../sources/<file>.md` | <…> | <…> | <YYYY-MM-DD> | [sourced: <slug>] |

<A metric value is NOT an intake row — it is captured to registers/metrics.csv by `metrics-capture`,
and the worklog cites the `M-…` id. A superseded fact is struck through and re-dated, never
overwritten in place.>

## <the method's working starts here — filled by the Act pass, not by source-intake>
```

## The index row it updates

In `sources/INDEX.md`, the source's row records which worklog(s) absorbed it — so unrouted evidence is
visible at a glance:

```markdown
| `market-research.md` | market/competitor evidence (dated, public) | → `2-analysis/market-sizing.md`, `2-analysis/competitor-analysis.md`, `2-analysis/synthesis.md` |
```

**Then:** write the change-log entry in each worklog touched (from → to · why · trigger), update
`sources/INDEX.md`, and run `python3 tools/lint.py <instance>` to 0 errors — `check P` holds the
worklog well-formed and confirms no artifact links the source directly.
