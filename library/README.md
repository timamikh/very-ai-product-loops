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

| Tool | Purpose | Recommended for | Status |
|------|---------|-----------------|--------|
| `interview` | Gather qualitative signal from users/customers (guide + synthesis) | Steps 1–2 | planned |
| `analytics-search` | Find and pull relevant analytical/market data | Steps 1–2, 4 | planned |
| `concept-formation` | Shape the product concept from a raw idea | Step 1 | planned |
| `segmentation` | Define and cut user/customer segments | Step 1 | draft |
| `segment-pains` | Surface each segment's problems (severity × frequency) | Step 1 | planned |
| `value-definition` | Define value & defensibility (base + derivative moats; post-AI lens) | Step 1, 3 | draft |
| `market-sizing` | TAM / SAM / SOM with method + source | Step 2 | planned |
| `competitor-analysis` | Direct / indirect competitors and the game they play | Step 2 | planned |
| `substitutes` | Non-obvious competition incl. "do nothing / do it manually" | Step 2 | planned |
| `where-to-play-how-to-win` | Strategic choice of arena and winning logic | Step 3 | planned |
| `uvp-cpv` | Unique value proposition / customer-perceived value | Step 3 | planned |
| `channels-expansion` | Acquisition/comms channels and expansion paths | Step 3 | planned |
| `metric-tree` | North Star → drivers → input metrics | Step 4 | planned |
| `unit-economics` | CAC/LTV/payback/contribution (incl. LLM inference COGS) | Step 4 | planned |
| `financial-model` | Simple projection tied to the metric tree | Step 4 | planned |
| `risk-mitigation` | Turn risks into owned mitigations | Step 4 | planned |
| `hypothesis-test-design` | Design a test for a hypothesis | Step 5 | planned |
| `ab-test` | Run an A/B test — what/when/how + template | as needed | planned |
| `cjm` | Customer journey map | as needed | planned |
| `jtbd` | Jobs-to-be-done framing | Step 1, 3 | planned |
| `brief` | Product/feature brief | as needed | planned |
| `prioritization` | Rank items (must vs backlog) by contribution to the gate | Step 5, 6 | planned |

The list is a starting set, not a closed spec — grow it as the community adds methods.
