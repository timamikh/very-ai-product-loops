---
node_type: conventions
title: Conventions — markers, IDs, links, change logs
status: draft
version: 0.5.0
updated: 2026-07-21
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

- Hypotheses: `H-001`, `H-002`, … — each carries a **type**: `desirability` (do they want it) ·
  `feasibility` (can we build it) · `viability` (does it work for the business) · `usability`
  (can they use it). (The classic product-risk taxonomy.)
- Risks: `R-001`, …
- Metric nodes: `M-northstar`, `M-activation`, …

Reference them inline in brackets, e.g. "drives `M-activation`" or "tests `H-003`".
Cross-artifact links use GitMark-lite: `[[analysis#opportunity]]`, `[[strategy#bets]]`.

## Artifact filenames

A step's output artifact is named **`<step-number>-<slug>.md`** — `1-passport.md`, `2-analysis.md`,
`3-strategy.md`, `4-strategic-plan.md`, `5-tactical-plan.md`, `6-sprint-plan.md`. The numeric prefix
exists for **one reason: a directory listing sorts in step order** (a plain `ls`/Finder view walks
the pipeline top to bottom instead of scrambling it alphabetically). It is good UX and nothing more.

The prefix is a **filesystem ordering key, not part of the artifact's identity.** The **logical id**
of an artifact is its bare slug (`strategy`, `strategic-plan`), and cross-artifact links use that:
`[[strategy#bets]]`, `passport#concept` — **never** `[[3-strategy#bets]]`. When a link (or a tool)
resolves a logical id to a file, it drops any leading `<digits>-` prefix. So there is still exactly
one identity per artifact (the slug); the number is only how the file sorts on disk. A **literal file
path** — e.g. a path passed to an adapter renderer — does carry the prefix (`4-strategic-plan.md`),
because that's the real filename. (Registers and deliverables are not step outputs and take no prefix.)

## One mechanism, one way

Product decisions fork; **framework mechanics must not**. For anything the framework itself does —
where values live, file formats, ID schemes, section anchors — there is exactly **one canonical
way**. No dual formats, no "start in X then migrate to Y" thresholds, no documented alternatives:
every mechanical variation point is a place where two agents (or an agent and an aggregator)
diverge and break. If two ways exist, pick one and eliminate the other in the same change.

## Forks & options

**Triage first — fewer forks, higher quality each.** Escalate a decision to the human only if it
is (a) consequential — changes strategy, is irreversible or expensive — AND (b) not closable from
evidence with a confident default. Everything reversible and cheap the agent decides itself,
marks **⚙️**, and logs with its rationale — it does not ask. An open fork is an unresolved risk:
close it, or escalate it with an owner — never let `— to clarify —` become standing debt.
(This raises the bar on agent judgment: confidence tags and logged defaults become mandatory,
not optional.)

For the forks that survive triage, present **2–4 concrete options with their trade-offs**, then
a recommendation — never a single option with the alternatives hidden. A lone recommendation
removes the human's choice and buries the risk in the paths not shown.

- Each option gets a one-line pro/con; the recommended one is marked **⚙️** and stated as the lead.
- This applies in prose forks and in the operating loop's *Clarify* step alike.
- Technical/implementation gaps are still noted as forks in the artifact, not asked — this rule is
  about the *product decisions* the human owns.

## Talking to the human

In chat, never send a bare register ID, section anchor, or link: decode what stands behind it in
the same sentence ("`H-009` — the bet that tech leads stay for the frontier stream"), so the human
never has to open the repo just to follow the conversation. IDs stay bare only inside artifacts,
where the register is one click away.

## Raw data & access

- **Access to an external data source** (an admin panel, an analytics account) is described in a
  dedicated source file under `sources/` — what it is, how to connect, how to verify, how to
  recover — and indexed in `sources/INDEX.md`. Handoffs and artifacts point to it, never duplicate it.
- **Captured values** go straight to the registers (dated rows); the source file records the
  capture context.
- **Raw captures** (page snapshots, exports) containing real data live only inside the instance
  while being processed and are **deleted once their values land** in the registers/sources.
  Nothing raw ever sits outside the instance directory.
- **Secret values** (tokens, passwords) are never written into artifacts, handoffs, or chat —
  only *where* they live and how to rotate them.

## Which conventions apply where

Conventions are **not** uniform across file types — applying all of them everywhere creates the
same on-the-fly ambiguity "one mechanism, one way" is meant to kill (does a source file need a
change log? does a register need inline confidence tags when confidence is already a column?).
The matrix below is authoritative; a file's `node_type` (frontmatter) selects its row.

| `node_type` | Confidence tags | Section IDs | Register/item IDs | Change log | Notes |
|-------------|-----------------|-------------|-------------------|------------|-------|
| `artifact` (step outputs) | **yes** — on every non-trivial claim | **yes** | reference by ID | **yes** | the full convention set |
| `register` (hypotheses/risks/metric-tree) | **no** in prose — `confidence` is a table column instead | n/a | **defines** the IDs | **yes** | values obey the metric-register split (see REGISTERS.md) |
| `source` (external-data notes) | **yes** — tag each captured fact | optional | reference by ID | **yes** | secrets/raw-data rules apply (see "Raw data & access") |
| `sources-index` | n/a | n/a | reference by ID | **yes** | navigation only; no captured values |
| `handoff` | tag any state that is an assumption | n/a | reference by ID | **yes** | never the home of rules or truth |
| framework files (`step`, `status`, `conventions`, `operating-loop`, `library-*`, `template-fragment`, …) | n/a | **yes** where sectioned | n/a | **yes** + `version` | authored by maintainers; version-bumped |

If a convention is marked n/a / no for a node_type, **omitting it is correct** — not a lapse.
A convention not listed here (e.g. "Talking to the human") is behavioral and applies always.

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
