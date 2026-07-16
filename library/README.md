---
node_type: library-index
title: Library — product methods as skills
status: draft
version: 0.1.0
updated: 2026-07-16
---

# Library

The library is the framework's **method plane**: a catalog of product instruments, each
authored as a **skill**. A step's job is to say *which section must exist*; a tool's job is to
say *how to produce it*. Keeping methods here (not inside steps) is what makes the process
core neutral and the workflow adaptable — companies swap or extend tools without forking the
framework.

## When the agent reaches for a tool

- A **step** recommends tools for the sections of its artifact.
- A **status** re-prioritizes and highlights the tools relevant to the current product stage.
- A **hypothesis** that needs testing pulls a testing tool (e.g. `ab-test`, `interview`).
- The **human** can call any tool directly, or override the recommendation.

All of this is soft: recommendations, not requirements.

## Anatomy of a tool

Each tool is a folder `library/<tool>/`:

```
library/<tool>/
  SKILL.md             # what it is · when to apply it · PREREQUISITES · how to do it · anti-patterns
  template-fragment.md # the artifact section it produces, with source + confidence markers
  questions.yaml       # the interview to gather inputs (also renders to a fillable file)
  references/          # deeper method notes, worked examples
```

**Prerequisites checklist (required).** Every `SKILL.md` lists the info / artifacts / access the
tool needs before it can run. In the [operating loop](../process/OPERATING-LOOP.md) the agent
checks this list first; for anything missing it **asks the human to provide it, or offers to
help develop or obtain it** (draft the analysis, prepare an interview guide, write the access
request). A tool never runs on a guessed input.

`SKILL.md` frontmatter declares the tool's wiring so steps, statuses, and future aggregators
can find and compose it:

```yaml
---
name: <tool>
kind: method | check | template | research   # research = gathers inputs (interviews, data search)
produces: <artifact-section-id>        # which section it fills
prerequisites: [<info/artifact/access it needs>]  # checked first; asked for or helped-with if missing
reads_registers: [metrics, hypotheses] # registers it consumes
writes_registers: [hypotheses]         # registers it updates
inputs: [interview, metrics, git, kb]  # source slots it needs
used_by_steps: [1, 3]                  # soft, informational
---
```

## How to add a tool

1. Create `library/<tool>/` with the anatomy above.
2. Fill `SKILL.md` (what / when / how / anti-patterns) and its frontmatter wiring.
3. Add `template-fragment.md` and `questions.yaml`.
4. Register it in the index below.
5. Link it from the relevant step(s) and status(es) as a *recommendation*.

Keep tools **single-purpose** and **opinion-explicit**: if a method reflects a particular
school of thought (e.g. a post-AI view of defensibility), say so in `SKILL.md` — that is
exactly why it lives here and not in the neutral core, so another company can supply its own.

## Index

Status: `planned` = named, not yet authored · `draft` = authored, in review · `stable` = merged to main.

Every authored tool cites a **method basis** — a recognized, current methodology it applies —
so the library stays sharp without reinventing theory. Keep it to the method(s) that matter;
don't turn a tool into a literature review.

| Tool | Purpose | Method basis | Steps | Status |
|------|---------|--------------|-------|--------|
| `interview` | Gather qualitative signal from users/customers | Continuous discovery · *The Mom Test* | 1–2 | planned |
| `analytics-search` | Find & pull relevant analytical/market data | Triangulated desk research | 1–2, 4 | planned |
| `concept-formation` | Shape the concept from a raw idea | Dunford positioning ('the shift') | 1 | draft |
| `segmentation` | Define & cut segments | JTBD / needs-based, priority-tiered | 1 | draft |
| `segment-pains` | Surface problems in the job | JTBD + Value Proposition Canvas; severity × frequency; differentiator vs table-stakes | 1 | draft |
| `value-definition` | Value & defensibility | 7 Powers (Helmer) → base/derivative; post-AI lens | 1, 3 | draft |
| `market-sizing` | TAM / SAM / SOM | Bottom-up sizing with named assumptions | 2 | planned |
| `competitor-analysis` | Competitors, their game, pricing & dynamics | 'What game are they playing' + moat comparison + pricing scan + registry dynamics (datanewton for RU) | 2 | draft |
| `substitutes` | Non-obvious competition | JTBD competition incl. do-nothing | 2 | planned |
| `where-to-play-how-to-win` | Arena + winning logic | Playing to Win (Lafley/Martin) — winning-aspiration / where-to-play / how-to-win cascade | 3 | draft |
| `uvp-cpv` | Value proposition / CPV | Dunford positioning + Value Proposition Canvas + customer-perceived value | 3 | draft |
| `channels-expansion` | Channels & expansion | Bullseye framework (*Traction*, Weinberg/Mares) + expansion-path thinking | 3 | draft |
| `risk-mitigation` | Risks → owned mitigations | Pre-mortem (Klein) + risk-register triage (prob × impact) + mitigation/owner | 3, 4 | draft |
| `product-surface` | User-interaction surfaces + instrumentation | Touchpoint mapping + instrumentation planning | 3, 4 | draft |
| `architecture-c4` | System architecture (Context level) | C4 model — Context (Simon Brown) | 3, 4 | draft |
| `metric-tree` | North Star → drivers → inputs | North Star Framework (Amplitude) | 4 | planned |
| `unit-economics` | CAC/LTV/payback/contribution | Unit economics incl. LLM inference COGS | 4 | planned |
| `financial-model` | Projection off the metric tree | Driver-based modeling | 4 | planned |
| `guardrails` | What must not drop while hitting goals | Guardrail metrics + red lines (steering-committee reconciliation) | 5 | draft |
| `resource-check` | Assess available resources this period | Lightweight capacity survey | 5 | draft |
| `hypothesis-test-design` | Design a test for a hypothesis | Assumption mapping + smallest viable test | 5 | planned |
| `ab-test` | Run a controlled experiment | A/B testing with guardrail metrics | as needed | planned |
| `cjm` | Customer journey map | Journey mapping | as needed | planned |
| `jtbd` | Jobs-to-be-Done framing | JTBD (Christensen / Ulwick) | 1, 3 | planned |
| `brief` | Product/feature brief | Structured brief | as needed | planned |
| `prioritization` | Rank must vs backlog | RICE / ICE, ranked by gate contribution | 5, 6 | planned |
| `feature-spec` | Development item as a Feature | Description/Scope/Business value/User value/User stories | 6 | draft |
| `growth-activity` | Growth item as an Activity | Feature-altitude activity tied to a metric/hypothesis | 6 | draft |

The list is a starting set, not a closed spec — grow it as the community adds methods.
