---
node_type: tool-skills-index
title: Tool-skills — the pluggable skills the agent runs
status: draft
version: 0.7.0
updated: 2026-08-21
---

# Tool-skills

The framework splits into two halves:

- **The fixed core** — `process/` (rules), `steps/` (skeleton), `statuses/` (stage config),
  `registers/` (living state). This is the board and the rules of the game; it changes rarely.
- **The pluggable skills** — everything under `tool-skills/`. These are instruction skills the
  agent *picks up and runs*: markdown that says how to do a thing, no build step. Companies swap
  or extend them without forking the core.

`tool-skills/` holds three categories, distinguished by **when in the process they run**:

| Category | What it does | When it runs | Index |
|----------|--------------|--------------|-------|
| [`library/`](library/README.md) | product methods that fill an artifact **section** (segmentation, pricing-strategy, jtbd-concept, …) | *during* a step pass — recommended by the step & status | [`library/README.md`](library/README.md) |
| [`operations/`](operations/README.md) | runtime skills about how the agent **works** (handoff, metrics capture, delegation to subagents; future: scheduling, automation) | at session/process boundaries — triggered by events, not by a step | [`operations/README.md`](operations/README.md) |
| [`outputs/`](outputs/README.md) | produce the **files that leave the framework** — renderers (table · document · deck) and authored deliverables (`brief`, `interview`, `feature-to-spec`); they land in the instance's `export-files/` | *after* the content exists — on a delivery request | [`outputs/README.md`](outputs/README.md) |

## How the agent finds the right skill (discovery rule)

One rule covers all three: **pick the category by the phase of the task, then read that
category's index.**

- The task is *"produce / update a section of an artifact"* → **`library/`**. The active step
  README and status `per_step` already name the recommended tool; the library index is the full
  catalog and fallback.
- The task is *"produce a file for use outside the framework"* (a deck, a one-pager, a table for a
  stakeholder, a brief, an interview guide) → **`outputs/`**. Match it in the outputs index
  (`to-deck` for a presentation, `to-document` for a doc, `to-table` for a register/backlog;
  `brief` / `interview` for an authored document).
- The task is *"carry state across a restart / go get a number the register doesn't have / split this
  pass across several agents / record what the framework got wrong"* → **`operations/`**. See also
  the OPERATING-LOOP sections "Session handoff" (the authority for the handoff mechanism and for the
  rule that a data-gathering errand is a full pass of the loop) and "Delegation" (the authority for
  who may write, and for what is never delegated).

The human may always call any skill directly or override the recommendation — discovery is a
default, not a gate.

## Reference — every skill at a glance

A hand-maintained **projection** of each skill's `SKILL.md` frontmatter and the statuses'
`per_step` lists — those stay the owners; if a row disagrees with a frontmatter, the frontmatter
is right and the row is a bug. Deeper columns (method basis, quality declaration) live in
[`library/README.md`](library/README.md)'s index.

Legend — **Input** (the `inputs:` slots the agent draws on): `interview` = answers to the skill's
`questions.yaml`, `kb` = existing artifacts & dispatched sources, `research` = its own scoped
desk-research pass, `metrics` = register readings, `git` = repo access. **Registers**: H =
hypotheses · R = risks · M = metrics/metric-tree, written `reads → writes`. **Statuses** that
recommend the skill at its step: CV = concept-viability · PMF = pmf · G = growth; `—` = deliberately
recommended by none (reason in the row).

### `library/` — methods, by step

| Skill | Step | Statuses | Goal | Input | Output | Registers |
|-------|------|----------|------|-------|--------|-----------|
| `concept-formation` | 1 | CV | Shape a raw idea into a concept | interview · kb | `1#idea` | → H |
| `jtbd-concept` | 1 | CV | Frame the job: statement, forces, desired outcomes | interview · kb | `1#jtbd` | H → H |
| `segmentation` | 1 | CV·PMF·G | Cut the market on candidate bases, pick priority segments | interview · kb · metrics | `1#segments` | → H |
| `segment-pains` | 1 | CV·PMF·G | Surface ≥5 pains in the job, rank by severity × frequency | interview · metrics · kb | `1#problems` | → H |
| `cjm-concept` | 1 | — (optional lens) | Journey map through the concept lens | interview · research | `1#cjm` | H → H |
| `concept-expansion` | 1 | CV | Map every ranked problem to a solution mechanism, cut orphan features | interview · kb | `1#solution` | → H |
| `value-definition-concept` | 1 | CV·PMF·G | Base moats & the defensibility bet | interview · kb | `1#value-defensibility` | → H |
| `market-sizing` | 2 | CV·PMF·G | TAM/SAM/SOM bottom-up with named assumptions | research · kb | `2#market-sizing` | → H |
| `competitor-analysis` | 2 | CV·PMF·G | ≥5 named players & the game each plays | research · kb · interview | `2#competitors` · `2#competitor-strategy` | → R, H |
| `competitor-pricing` | 2 | CV·PMF·G | Dated per-player pricing scan | research · kb | `2#competitor-pricing` | — |
| `competitor-dynamics` | 2 | CV·PMF·G | Trend per player over time (filings, registries) | research · kb | `2#competitor-dynamics` | → R |
| `substitutes` | 2 | CV·PMF·G | Non-obvious competition incl. do-nothing / manual / self-build | interview · kb · research | `2#substitutes` | → R |
| `where-to-play-how-to-win` | 3 | CV·PMF·G | The strategy cascade: aspiration · arena · winning logic | kb · interview | `3#winning-aspiration` · `3#where-to-play` · `3#how-to-win` | H → H |
| `uvp-cpv` | 3 | CV·PMF·G | Value proposition & perceived value per situation | interview · kb | `3#uvp-cpv` | → H |
| `pricing-strategy` | 3 | PMF·G | Value-based pricing model & packaging — the one place price is decided | interview · kb · research | `3#pricing` | H → H |
| `channels-expansion` | 3 | PMF·G | Bullseye channels, GTM motion, expansion path | interview · kb · research | `3#channels-expansion` | → H, R |
| `product-surface` | 3 | CV·PMF·G | Interaction surfaces + instrumentation sketch | interview · kb · git | `3#product-surface` | — |
| `architecture-c4` | 3 | CV·PMF·G | System architecture (C4 Context) | interview · kb · git | `3#architecture` | → R |
| `bets` | 3 | CV·PMF | 3–7 strategy bets seeded as typed hypotheses | interview · kb | `3#bets` | H → H |
| `value-definition-strategy` | 3 | CV·PMF·G | Moat revisit: derivative moats & trajectory | interview · kb | `3#value-defensibility` | H → H |
| `cjm-strategy` | 3 | — (optional lens) | Journey re-walk against the chosen strategy | interview · research | `3#cjm` | H, R → H, R |
| `pre-mortem` | 3 | CV·PMF·G | ≥8 named failure modes, triaged into risks | interview · kb | `3#product-risks` | R → R |
| `metric-tree` | 4 | CV·PMF·G | North Star → drivers → inputs; defines the nodes | metrics · kb | `4#metric-tree` | M, H → M |
| `financial-model` | 4 | PMF·G | Named-scenario projection computed off the tree | metrics | `4#financial-model` | M, H, R → M |
| `strategic-targets` | 4 | PMF·G | Commit horizon values on 3–5 nodes (read off a scenario) | interview · kb | `4#strategic-targets` | M → |
| `unit-economics` | 4 | CV·PMF·G | Does one customer pay for themselves | metrics | `4#unit-economics` | M, H → M |
| `retention-analysis` | 4 | PMF·G | Cohort retention read | metrics · kb | `4#retention` | M, H → H, M |
| `capabilities-systems` | 4 | PMF·G | PTW choices 4–5: capabilities behind how-to-win + their management systems | interview · kb | `4#capabilities` | R → R |
| `risk-mitigation` | 4 | CV·PMF·G | Mitigation, owner and trigger per carried risk | interview · kb | `4#risk-mitigation` | R → R |
| `hypothesis-thresholds` | 4 | CV·PMF·G | Kill/scale thresholds on the global hypotheses | metrics | `4#global-hypotheses` | H, M → H |
| `instrumentation-plan` | 4 | CV·PMF·G | What to measure and how, before building | interview · kb · git | `4#architecture-instrumentation` | M → |
| `pricing-strategic-plan` | 4 | — (revisit, no own section) | Margin-check the Step-3 price; outcome: holds, or ⚙️ change proposed on `3#pricing` | metrics · kb | worklog verdict → `3#pricing` re-confirmation | H, M → H |
| `prioritization-tactical-plan` | 5 | CV·PMF·G | Rank every current candidate goal against the period gate | — | `5#period-goals` | M, H → |
| `goal-targets` | 5 | CV·PMF·G | Period targets as a step toward the horizon commitment | metrics | `5#goal-targets` | M → |
| `segment-cvp` | 5 | CV·PMF·G | Compose ≥8 segment×situation bundles, gate by the 6 filters | interview · kb · research | `5#market-bundles` | H → H |
| `hypothesis-test-design` | 5 | CV·PMF·G | Smallest test per hypothesis with a pre-set decision rule | metrics | `5#hypotheses-to-test` | H, M → H |
| `ab-test` | 5 | PMF·G | Controlled split test: design, power, read | metrics | `5#hypotheses-to-test` | H, M → H, M |
| `experiment-readout` | 5 | CV·PMF·G | Verdict per finished test → signal + decision | metrics | `5#readouts` | H, M → H |
| `resource-check` | 5 | CV·PMF·G | Honest capacity check that bounds the period | interview | `5#resources` | — |
| `guardrails` | 5 | CV·PMF·G | Floors/ceilings so the goals don't break the base | interview · metrics | `5#guardrails` | M, R → R |
| `prioritization-sprint-plan` | 6 | CV·PMF·G | Rank every current sprint item; must/backlog line by capacity | — | `6#must` · `6#backlog` · `6#excluded` | M, H → |
| `feature-spec` | 6 | CV·PMF·G | Spec per development item | interview · kb | `6#must` · `6#backlog` | H, M → |
| `activity-spec` | 6 | CV·PMF·G | Spec per go-to-market activity | interview · kb | `6#must` · `6#backlog` | H, M → |
| `task-spec` | 6 | CV·PMF·G | Spec per back-office task | interview · kb | `6#must` · `6#backlog` | H, M, R → |
| `feature-grooming` | 6 | CV·PMF·G | Close product forks with the owner before the spec; record technical forks | interview | `6#must` · `6#backlog` | H, M → |

### `operations/` — runtime skills, by trigger

| Skill | When it runs | Goal | Output |
|-------|--------------|------|--------|
| `orchestration` | a pass splits across subagents | written briefs + acceptance passport; the orchestrator alone projects and writes state | worklogs via `loops-draft`; returns integrated |
| `projection` | a worklog is ready to become its section (or changed under one) | the conclusion in the fragment's shape — tags verbatim, headline marked, stale sign-offs dropped | artifact section(s) + `<!-- card -->` mark |
| `source-intake` | a raw file lands in `sources/` | dispatch it into the step worklog(s) it feeds, cite it there | routed citations + `sources/INDEX.md` entry |
| `metrics-capture` | a number arrives | source → dated register row with population, window, derivation | `metrics-capture` worklog + M row |
| `theses` | operating-loop move 5 (scope: step) · before a step change (scope: instance) | walk the human through the sections, record the sign-off | `confirmed:` / `contested:` markers |
| `step-close` | every gate section of a step is projected, before the gate is ticked | read the step whole — links, tensions and gaps no single section shows — and land them through the ordinary channels | section / worklog / register edits + change-log entry |
| `handoff` | session boundary | carry state and next-actions to the next session | `HANDOFF.md` |

### `outputs/` — files that leave the framework, on a delivery request

| Skill | What leaves |
|-------|-------------|
| `brief` | an authored brief compiled from the instance (`export-files/<slug>-brief.md`) |
| `feature-to-spec` | a development instruction for one F-item, compiled from its spec and its registers (`export-files/<feature>-spec.md`) |
| `interview` | an interview guide for steps 1–2 primary research; the notes come back as a source |
| `to-deck` | a self-contained HTML slide deck (+ PDF companion once approved) |
| `to-document` | a compiled `.docx` — one-pager · full doc · report · status update |
| `to-table` | CSV (or one multi-tab `.xlsx`) from a register or artifact section |

## Where a product's OWN skills live

The vendored framework is **read-only**: updating it means re-vendoring at a newer tag, which
overwrites `tool-skills/`. So a company's or a product's own methods do **not** go here. Their one
canonical home is inside the product's working area, mirroring this layout:

```
product-loops/tool-skills/library/<name>/      # a product's own method
product-loops/tool-skills/operations/<name>/   # a product's own runtime skill
product-loops/skills/<pull|push>-<endpoint>-<what>/  # a product's own EXCHANGE skill (see reference/boundary-layout)
```

A product's **exchange skills** — repeatable pulls and pushes across the instance boundary — are the
one kind kept apart, at `<instance>/skills/`, because the goal map routes to them by trigger and they
carry a `cadence`; their spec is [`process/reference/boundary-layout.md`](../process/reference/boundary-layout.md).

Three rules, and no other variant:

- **Same anatomy.** A local skill is a normal skill — `SKILL.md` (with the same frontmatter wiring) +
  `template-fragment.md` + `questions.yaml`. The linter checks it exactly like a vendored one, so a
  local method cannot quietly produce a homeless section.
- **Local wins.** If a local skill and a vendored one share a name, the local one is the method the
  agent runs. That is how a company specializes a base method without forking the framework.
- **Survives updates.** Because it sits under `product-loops/`, re-vendoring the framework never touches it.

The **agent** writes it, asked for in words — describe the method, or point at an existing skill to adapt.
The procedure is per kind: a method → [`extending/method.md`](../extending/method.md), a runtime skill →
[`extending/operation.md`](../extending/operation.md), a deliverable →
[`extending/output.md`](../extending/output.md), an exchange card →
[`process/reference/boundary-layout.md`](../process/reference/boundary-layout.md). The local console
([`tools/ui/`](../tools/ui/README.md)) then displays it, and never creates one itself.

## Not to be confused with `.claude/skills/`

`.claude/skills/` holds **Claude Code-native skills** (e.g. `product-setup`), invoked by the
harness as slash-skills. `tool-skills/` holds **framework skills** — markdown methods the agent
*reads and applies* as part of the workflow. Different mechanism, different home.

`.claude/agents/` is the same distinction one step further: the `loops-*` subagent definitions there
are **runtime enforcement** of a rule that is written in markdown. The write rule is a split — a
`draft` subagent writes exactly one file (its method's worklog), and `gather`/`research`/`verify`
write nothing — so three of the four definitions ship with no write tools at all, and `loops-draft`
carries `Write` and only `Write`. The rule lives in
[`process/OPERATING-LOOP.md`](../process/OPERATING-LOOP.md) → *Delegation* and the procedure in
[`operations/orchestration/`](operations/orchestration/SKILL.md); the definitions are how one
particular runtime happens to enforce it, and the framework runs without them.
