---
node_type: conventions
title: Conventions — markers, IDs, links, change logs
status: draft
version: 0.10.0
updated: 2026-08-09
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

## Links & register item IDs

Register items have stable IDs:

- Hypotheses: `H-001`, `H-002`, … — each carries **exactly one `type`**: `desirability` (do they
  want it) · `feasibility` (can we build it) · `viability` (does it work for the business) ·
  `usability` (can they use it). (The classic product-risk taxonomy.) A cross-cutting theme
  (e.g. *moat*, *pricing*) is **not** a fifth type — it goes in a separate, free **`tags`** column,
  declared non-load-bearing for aggregators; never compound it into `type`. (`viability/moat` is
  wrong — write `type: viability`, `tags: moat`.) A hypothesis needing **two verdicts** is split in
  two **at the first attempt to test it** (Step 4, when a metric is attached): the halves name the
  original, the original closes as `superseded` — not `refuted`, it was divided, not disproved. Half
  a refuted bet is the half worth keeping: it takes a named bet off the table for good.
- Risks: `R-001`, … — likewise **exactly one `category`**; extra themes go in `tags`.
- Metric nodes: `M-northstar`, `M-activation`, …

Reference an item inline in brackets, e.g. "drives `M-activation`" or "tests `H-003`".

**Cross-artifact links use a relative file path + the target's stable `{#anchor}`** — e.g.
`2-analysis.md#opportunity`, `3-strategy.md#bets` (from a register or other subdirectory, prefix the
path: `../2-analysis.md#opportunity`). This is the one canon: standard markdown, clickable without a
custom resolver, parseable by any tool. **Never** a wiki-style double-bracket link (the removed
GitMark-lite form). Two rules carry over: point at the stable `{#anchor}`, never a heading's changeable text; and keep anchors
stable across revisions (rename the heading freely, keep the id). A gate checklist may use the
shorthand `artifact#section` (e.g. `passport#concept`) to name the section it validates.

## Artifact filenames

A step's output artifact is named **`<step-number>-<slug>.md`** — `1-passport.md`, `2-analysis.md`,
`3-strategy.md`, `4-strategic-plan.md`, `5-tactical-plan.md`, `6-sprint-plan.md`. The numeric prefix
exists for **one reason: a directory listing sorts in step order** (a plain `ls`/Finder view walks
the pipeline top to bottom instead of scrambling it alphabetically). It is good UX and nothing more.

Because cross-artifact links are **real relative paths** (see "Links" above), the prefix is simply
part of the path you link to: `3-strategy.md#bets`, `../1-passport.md#concept`. There is no separate
"logical id" to resolve and no prefix to strip — you link the actual file, and a section is
identified by its bare `{#anchor}` within it. (Registers and deliverables are not step outputs and
take no numeric prefix.)

## Instance config (`config.yaml`) — the pinned schema

`config.yaml` is the **human's decisions** about the instance (the cycle's position lives in
`state.yaml` — see OPERATING-LOOP). Its keys are canon, spelled exactly one way. A second spelling is
a place two readers diverge, so the linter enforces this table.

| Key | Required | Shape | What it is |
|-----|----------|-------|------------|
| `product` | **yes** | text | the product's name as a human says it (never inferred from the folder) |
| `language` | **yes** | `ru` · `en` · … | the documentation language; tools also read it for their own UI |
| `active_status` | **yes** | a status name from `statuses/` | the stage the loops are parameterized by |
| `directions` | **yes** | list | execution streams for Steps 5–6 (default: `development` · `go-to-market` · `back-office`) |
| `scope_note` | no | text (block scalar) | what is in and out of this instance's scope, in prose |
| `metric_source_slots` | no | map | where metric data comes from — *where* it lives and how to reach it, **never a secret value** |
| `sources` | no | list of paths | the origin documents this instance was built from |
| `products` | no | map | **multi-product instance only**: `<name>: { path, title, goal, users, active_status }`, one sub-folder per product, each with its own artifacts, `state.yaml` and `registers/`; the sub-products inherit everything above from this file |

Rules:

- **Nothing else is load-bearing.** Extra keys are allowed but no tool may depend on them (the linter
  reports them so they don't quietly become de-facto schema).
- **No alias spellings.** `metric_sources`, `product_scope`, `lang`, `title` are *not* accepted forms —
  fix the key, don't add a reader.
- **Readers stay tolerant, the linter stays strict.** A reader that meets an off-canon key should still
  show the data (a product manager must not see an empty screen because of a key name) *and* surface
  the drift. Tolerance is for the human's benefit; it is never permission.

## One mechanism, one way

Product decisions fork; **framework mechanics must not**. For anything the framework itself does —
where values live, file formats, ID schemes, section anchors — there is exactly **one canonical
way**. No dual formats, no "start in X then migrate to Y" thresholds, no documented alternatives:
every mechanical variation point is a place where two agents (or an agent and an aggregator)
diverge and break. If two ways exist, pick one and eliminate the other in the same change.

## Where a new rule goes — contract · method · check

The framework accretes: every real failure tempts a paragraph that would have prevented it, and
paragraphs land in the files an agent reads on **every** pass. So a proposed rule is first *classified*,
and only one of the three classes is allowed to grow the canon.

| Class | Home | What it costs | Use it for |
|-------|------|---------------|------------|
| **Check** | [`tools/lint.py`](../tools/lint.py) | **nothing at read time**; catches the case every run | anything a machine can verify: shapes, ids, enum membership, cross-file agreement |
| **Method** | a skill under `tool-skills/` | read only when that skill is used | procedure, technique, judgement — *how* to do the thing well |
| **Contract** | `process/` (this canon) | paid on every pass, by every agent | only what two independent readers must agree on: field names, enum values, id shapes, file roles (`node_type`), path/link form |

**Try the classes in that order.** A check costs no context and does not depend on the agent
remembering; a sentence in the canon costs context forever and does. "The linter is the gate" is not
just enforcement — it is where a rule belongs when it *can* live there.

Two consequences worth stating:

- **A budget on the always-loaded set.** The rule files an agent must read before any work
  (`AGENTS.md` + the four in `process/`) are about **930 lines**; the method library is over twice that
  and costs nothing until used. Keep the first number near **1000**: an addition to `process/` names
  what it displaces, or why it is neither a check nor a method. *(The ceiling was 900 through v0.8.2.
  Delegation raised it: the orchestrator↔subagent protocol is the definition of a contract — two
  independent agent roles must agree on it, and neither a linter check nor a skill file can carry a
  rule that a fresh subagent has to know **before** it reads anything else. The rest of delegation —
  decomposition, templates, the passport — went to a skill, which is why the raise was ~50 lines and
  not ~200.)*
- **Subtraction is part of the job.** A rule stated in two of these files is two places to drift — and
  drift is what happened: the overview described a link mechanism for a release and a half after the
  canon had replaced it. When a change touches a duplicated rule, delete the copy in the same change and
  leave a pointer.

This section governs changes to the framework itself; [`EXTENDING.md`](../EXTENDING.md) says which dial
to turn for what.

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

- **`sources/` holds three roles**, kept apart because they age differently — all indexed in
  `sources/INDEX.md`, pointed at by artifacts and handoffs, never duplicated by them:
  **access** (`node_type: source`, living — what the source is, how to connect, verify, recover),
  **method** (`node_type: source-method`, living — how its raw rows become register values: who is
  excluded, how keys fold to one person, which window; this is what makes a reading *reproducible*),
  and **evidence** (`node_type: source`, dated and immutable — a capture). Put the method inside
  dated evidence and the next capture forks it into two authoritative versions.
- **Captured values** go straight to the registers (dated rows); the source file records the
  capture context.
- **Raw captures** (page snapshots, exports) are **never committed** and are **deleted once their
  values land** in the registers/sources. The instance folder is not automatically a safe place:
  vendored, it sits in a repo whose `origin` may be public — where that is so, the working folder for
  raw data and the analysis code that reads it live **outside** the repository, and only a reference
  goes inside (a change-log entry names the script that produced a reading).
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
| `source-method` (raw source → register values) | **yes** — on every judgement call (a cut-off, an exclusion) | optional | reference by ID | **yes** | living, never dated evidence: rewritten in place, so a reading stays reproducible |
| `sources-index` | n/a | n/a | reference by ID | **yes** | navigation only; no captured values |
| `handoff` | tag any state that is an assumption | n/a | reference by ID | **yes** | never the home of rules or truth |
| `friction` (`FRICTION.md`) | n/a | n/a | reference by ID | **is itself a log** | dated entries, newest first, appended at step 7 of every pass. Records where the *framework* got in the way — never product values, never a substitute for a register |
| framework files (`step`, `status`, `conventions`, `operating-loop`, `library-*`, `template-fragment`, …) | n/a | **yes** where sectioned | n/a | **no** — see root `CHANGELOG.md` | authored by maintainers; `version`-bumped, history in the central changelog |

If a convention is marked n/a / no for a node_type, **omitting it is correct** — not a lapse.
A convention not listed here (e.g. "Talking to the human") is behavioral and applies always.

## Change logs

Every **instance artifact** ends with a change log — the `artifact`, `register`, `source`,
`sources-index`, and `handoff` rows in the matrix above. Narrative artifacts included: the log
carries the *motivation*, not just the diff. Newest entry first.

```markdown
## Change log

### 2026-07-16 — <one-line summary>
- **From → To:** <what the state was> → <what it is now>
- **Why:** <reasoning>
- **Trigger:** <what prompted it — a metric shift, a refuted hypothesis, a decision, …>
```

A **register** entry names the ids it moved (`H-004`, `M-activation`) inside its From → To. That one
habit is what makes a single item's history retrievable — the console assembles the trail of one
hypothesis from these entries instead of anyone storing it a second time.

Framework files (this one included) do **not** carry an inline change log — their history lives in
the repository's root [`CHANGELOG.md`](../CHANGELOG.md), keyed to git version tags.
