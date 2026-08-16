# Changelog

All notable changes to very-ai-product-loops are recorded here. The format follows
[Keep a Changelog](https://keepachangelog.com/), and the project uses
[Semantic Versioning](https://semver.org/): `MAJOR.MINOR.PATCH`.

- **PATCH** — fixes and wording; nothing breaks for existing users.
- **MINOR** — new capability, backward compatible.
- **MAJOR** — a breaking change; adopters must adjust their instance.

The version you pin to is the **git tag**; this file is its human-readable story.

## [Unreleased]

Work accumulated since 0.8.2, grouped by area (collapsed into one release when a tag is cut).
Bullets are theses; the reasoning for any item lives in its commit and in the `process/` canon.

### Statuses audited against the post-release skeleton

- **growth catches up with the competitor recut**: its step-2 list gains `competitor-pricing` +
  `competitor-dynamics` — the goal already said "track competitor dynamics from live data", the
  tools didn't (the P1 sweep bumped the version and missed the list).
- **`product-surface` + `architecture-c4` enter step 3 of all three statuses**: every status
  recommended `instrumentation-plan` (step 4), which rests on `3#product-surface` and
  `3#architecture` — the foundation was never staged. The methods scale with the stage themselves.
- **concept-viability owns its risk chain**: `pre-mortem` added to step 3; the step-4 goal now
  reads "own mitigations for the 2–3 concept-killing risks" (the pre-mortem itself runs at Step 3
  — before, `risk-mitigation` was recommended with nothing upstream to mitigate).
- **`ab-test` enters step 5 of pmf and growth** (not concept-viability — no traffic to split);
  `segment-pains` enters growth step 1 (its goal watches for a segment/pain shift).
- **Wording**: growth's "at the passport level" → the concept level; pmf/growth bodies name their
  center of gravity (retention cohorts / guardrails) the way concept-viability already named the
  hypothesis register; statuses README states the check-V rules for `tools:` lists (library
  methods only, template home required, contributing methods never listed).

### Wide and quality — the P2 pass (content gaps, the PTW tail, orphan links)

- **Question-type vocabulary unified**: `text` is gone — `free_text` everywhere
  (`market-sizing`, `substitutes` renamed; check Y now enforces a single name).
- **Buyer vs user lands in `1#segments`** (`segmentation` 0.4.0): a column naming who pays vs who
  uses — when they differ, pains are scored for the user but the CVP and channel must convince the
  buyer.
- **Cost of inaction lands in `1#problems`** (`segment-pains` 0.2.0): per-pain
  `nice-to-have / recurring irritation / already paying or improvising` — the same gradation as
  pain acuteness in `hypothesis-test-design` §Scales, so Step 1 feeds the Step-3 CVP and the
  Step-5 priority score without translation.
- **GTM motion lands in `3#channels-expansion`** (`channels-expansion` 0.2.0): product-led /
  sales-led / partner-led / community-led, decided by price-per-account vs cost of the motion's
  touch; inner-ring channels are coherence-checked against it.
- **The PTW cascade completes — `capabilities-systems`** (new, Step 4, library 42 → 43): choices
  4–5 of Playing to Win get a home. `{#capabilities}` walks the winning logic element by element:
  capability (an ability, not an asset) · have/partial/missing · gap & close · management system;
  gaps seed execution `R-…` consumed by `risk-mitigation` in the same step. The
  `where-to-play-how-to-win` "land in later steps" promise now names its heir. In `pmf`/`growth`
  step-4 tool lists; kept out of `concept-viability` (that status defers step-4 depth by design).
- **The target ladder gets its top — `strategic-targets`** (new, Step 4, library 43 → 44): three
  target objects, three owners — `metric-tree` defines a node, `{#strategic-targets}` commits its
  horizon value (3–5 nodes, values read off a named `financial-model` scenario, horizon date from
  `3#winning-aspiration`, decision-attributed, untargeted nodes kept with why), Step-5
  `goal-targets` sets the period value as a step toward it (`4#strategic-targets` rests-on; a
  period in which no horizon target moves is drift). No double-write: a projection is a
  computation, a target is a commitment.
- **Orphan links closed**: `2#competitor-dynamics` gains its consumer (`where-to-play-how-to-win`
  prerequisites + `3#how-to-win` rests-on); Step-6 activities link the `B-…` bundle they launch
  (`activity-spec`, `#must`/`#backlog`); the REGISTERS born-at table now matches reality
  (hypotheses born 1·2·3; risks born 2·3·4).

### One operation even within a step — P1 pass after the recut

- **The rule extends** (EXTENDING, library gates): a second pass inside a step is a second skill,
  and a skill filling several sections must be one operation across them. Library 39 → 42.
- **`concept-formation` → + `concept-expansion`** (1): the concept one-liner is first thing; the
  problem→solution mapping runs after `{#problems}`, with an orphan-feature reject table and
  `type: feasibility` seeds. `{#solution}` re-homed.
- **`competitor-analysis` recut along the original/imported seam**: keeps players + their game
  (`{#competitors}`, `{#competitor-strategy}`); the dated pricing scan is **`competitor-pricing`**
  (feeds `market-sizing`'s price anchor, Step-3 `pricing-strategy`, the Step-4 financial model);
  the registry trend read is **`competitor-dynamics`**. The RU-specific interview question
  (ОГРН/datanewton) is gone — the registry question is jurisdiction-neutral, regional pulls go
  through adapters.
- **Iteration notes for the honest cycles**: `1#jtbd` first pass runs on the `#idea` customer and
  re-reads after `#segments`; `segmentation`'s moat ground is skipped ⚙️ until
  `{#value-defensibility}` exists; `market-sizing`'s first-pass price is a named `[assumption]`
  revisited after `{#competitor-pricing}`.
- **`rests-on` rolled out**: 15 markers across steps 2–6 (was 2) — derived from skill
  prerequisites, validated by check S; the console's foundation-unconfirmed signal and derivation
  map now have a schema to read.
- **One owner for the priority score**: defined in `hypothesis-test-design` §Scales (criteria
  wording adopted from `segment-cvp`: pain acuteness · reachability · deliverability · evidence of
  WTP · speed to a signal), operated at Step 5 by `segment-cvp`; REGISTERS points at both roles.
- **Gate holes closed**: items for `2#hypotheses`, `2#to-clarify`, `3#to-clarify`.
- **Status tools = library methods only**: `interview` left the `concept-viability` step-1 list
  (its role stays in the goals prose); the rule is one phrase in OPERATING-LOOP step 2, and linter
  check V now errors on an operations/outputs skill in a status list. The questions-vocabulary
  check is re-lettered **Y** (its old letter collided with the confirmation-schema check Q).

### One skill, one step — the multi-step methods recut

- **The rule** (EXTENDING → *Rules that hold for any change*, linter check U): a library method
  declares exactly one step. A different operation per step is a second skill with its own name;
  the same operation revisited at another step is a per-step variant. The library grows 28 → 39.
- **Operation cuts** (a skill was doing two different things): `metric-tree` [4,5] → `metric-tree`
  (4) + `goal-targets` (5, ex-ghost section); `hypothesis-test-design` [4,5] →
  `hypothesis-thresholds` (4, single source of truth for thresholds) + `hypothesis-test-design` (5);
  `risk-mitigation` [3,4] → `pre-mortem` (3, surface & triage) + `risk-mitigation` (4,
  mitigation·owner·trigger; `produces` desync fixed); `jtbd` [1,3] → `jtbd-concept` (1) + `bets`
  (3); `{#architecture-instrumentation}` co-ownership → one owner, `instrumentation-plan` (4).
- **Per-step variants** (same operation, another step): `cjm` → `cjm-concept`/`cjm-strategy`
  (concept variant no longer births risks at Step 1); `value-definition` →
  `value-definition-concept`/`value-definition-strategy`; `pricing` → `pricing-strategy` (3) +
  `pricing-strategic-plan` (4, margin revisit); `prioritization` →
  `prioritization-tactical-plan`/`prioritization-sprint-plan` (the "no file of its own"
  contradiction removed — a primary always owns its worklog).
- **segment-cvp homed**: Step 5 only; its value half (segment · situation · pain · CVP) absorbed
  into `uvp-cpv` at Step 3; statuses no longer recommend it where it had no section.
- **Steps 5–6 widened**: `{#readouts}` (experiment-readout — verdicts against pre-registered
  rules, write-back to the register), `{#sprint-goal}`, `{#to-clarify}` at Step 6; `{#handoff}` →
  `{#delivery}` (the name collided with the operations `handoff`); Feature format gains acceptance
  criteria, items gain owner/estimate; back-office Tasks get `task-spec`.
- **Three new linter checks**: Q (questions.yaml types are machine-readable — the
  `single_select_from:` invalid-YAML class), U (one skill, one step), V (a status may only
  recommend a tool with a `<!-- tool: … -->` home at that step — the segment-cvp failure class).
- **Library gates for donated methods** (library README → *How to add a tool*): one step · a home
  for every recommendation · jurisdiction/vendor-neutral · one owner per scale or definition.
- **Two-form design written down** (library README → *Anatomy*): `template-fragment.md` is the
  draft form the worklog works in — richer than the step template by design; the orchestrator
  projects only the theses into the artifact.

### The entity law — a source only comes from outside

- **The law** (CONVENTIONS → *Raw data & access*): `sources/` = what the user (or the world) brings
  **in**; **no skill produces a source from inside**. Agent reasoning is a **worklog**; a file made
  for use outside is an **export file**. A skill that fits no entity is **recut along the seams** —
  a new entity or hybrid home is never minted.
- **`tool-skills/adapters/` → `tool-skills/outputs/`** — the plane now holds two kinds: renderers
  (`ADAPTER.md`, read → regeneratable view) and authored deliverables (`SKILL.md`, author → signed
  document). `brief` and `interview` moved in from `library/` — neither fills a section.
- **`product-loops/export-files/`** — one instance home for everything that leaves the framework
  (the mirror of `sources/`); replaces `briefs/` and the double-named `deliverables/`/`outputs/`.
- **`interview` recut**: produces the guide (a deliverable); the conducted interviews' notes come
  **back** as a *source* the user adds → `source-intake` → consumers' worklogs; `writes_registers`
  emptied (the orchestrator writes registers during the methods' passes).
- **`analytics-search` dismantled** — it authored a "digest" into `sources/` (an agent file posing
  as a source). Desk research is now each consumer's own gathering: the `research` input slot,
  `loops-research` briefs, discipline per `references/evidence-standards.md`, findings in the
  consumer's worklog. Removed from statuses' tool lists and step inputs.
- **`metrics-capture` recut**: the derivation moves from `sources/<source>-method.md`
  (`node_type: source-method`, now gone) to the triggering step's worklog
  `<step-folder>/metrics-capture.md`; the csv `source` column cites the worklog, the worklog cites
  the access file. Check **P** knows the reserved name (event-driven worklog needs no marker).
- **Skill-audit fixes (pre-law)**: shared-enum drift killed (`back-to-research`→`research`,
  `not`→`not-instrumented`), stale `passport` refs, `hypothesis-test-design` declares both sections
  it fills, and Step 6 gains the `{#excluded}` slot so `prioritization`'s cut candidates have a home
  (gate tick `rejects-shown`).

### Delegation — one pass across many agents

- **Only the orchestrator writes.** Subagents `gather` · `research` · `draft` · `verify` return text
  (rule is transitive). Never delegated: a human fork, register ids/writes, gate ticks, the Step 1–4
  reasoning chain. New ops skill **`orchestration`**; `.claude/agents/loops-*` carry no write tools
  (checks **M**, **N**).
- **The return gate is hard.** A return that fails its **passport** is not integrated — one
  remediation, then `— to clarify —`. It costs more tokens, buys a clear context (stated, not hidden).
- **Mechanics moved into the loop**, not beside it: split decided at step 3 (by observable volume, not
  "wider than one context"), run at step 6, writes at step 7 only after returns are accepted. Two
  obligations before disk — a reasoning-based section is shown in chat first, and a pass declares its
  write perimeter; a reasoning-based gate tick waits for a `verify` subagent. `start-work` checks spawn
  permission at step 0; install writes the owner's delegation approval into the host `AGENTS.md`.
- `OPERATING-LOOP.md` → *Delegation*; always-loaded ceiling 900 → 1000 lines.

### Method quality — every method states what would make it wrong

- All 31 library methods carry a **quality declaration** (`evidence_standard` · `volume_rule` ·
  `selection_rule` · `rejects_shown`), enforced by check **L**; ~20 bodies rewritten to match.
- **Volume floors** as failable numbers (`segment-cvp` ≥3 situations / ≥8 bundles; `competitor-analysis`
  ≥5 players; `risk-mitigation` ≥8 failure modes; also channels-expansion, segment-pains, segmentation,
  where-to-play). `segment-cvp` gains a 5×(1/3/5) scoring rubric (its axis RICE lacks: speed-to-signal).
  **Reject tables** wherever `rejects_shown: required`.
- New reference `tool-skills/library/references/evidence-standards.md` — source judged per fact-type,
  a forbidden zone, fact/estimate/forecast/statement/pledge labels, and a headline cross-check
  (`[CONFLICT]` on >20% divergence). Check **C** no longer reads README schema tables as index rows.

### Confirmation & gradation — the semantic half of the check

- A section is a **thesis the human signs**: `<!-- confirmed: YYYY-MM-DD -->` (absence = pending;
  re-projection drops it), stamped by new ops skill **`theses`** at step 7. Check **Q** (no marker in a
  schema; an instance marker must parse as a date).
- **Open sections** (`<!-- open -->` on to-clarify / open-questions / blockers) leave the confirmed
  count; check **R**. **`contested`** marker (returned ≠ unseen) + optional `by:<who>`; check **R**
  (confirmed ⊕ contested).
- **`rests-on`** provenance (`<!-- rests-on: 1#segments, 2#opportunity -->`): a signed section on an
  unsigned foundation flags *foundation unconfirmed*; check **S**. `theses` gains `scope: step |
  instance` — instance scope clears cross-step rests-on debt a per-step pass can't.
- **Gradations = a second axis** (not a sign-off): hypothesis `signal`/`decision`, risk
  likelihood×impact + lifecycle; enforced-if-present via check **D**. Defined once in `REGISTERS.md`,
  `hypothesis-test-design`, `risk-mitigation`; `CONVENTIONS.md` holds the two axes apart.
- `CONVENTIONS.md` 0.13.0 → 0.18.0 across these.

### Worklogs & keys — a section says where it was worked out

- Each step artifact gets a sibling worklog folder (`2-analysis/…`), one worklog per method
  (`node_type: worklog`, the **source of truth**); the artifact section is a **projection**. One id
  threads section marker = skill folder = worklog file, so the console drills in with nothing authored
  per instance. Check **P**.
- **Column keys** `<!--c:key-->` — a table column carries a stable id like a section `{#anchor}`, read
  instead of header prose (language-safe). Check **O** (all-keyed or none; template ↔ fragment agree).
- Contract enforced: the console reads columns by key only (positional `COL_SCHEMA` gone); check **O2**
  (an instance must carry its template's keys) and check **P** (a worklog is required for every method
  section) — reddens un-migrated instances by design. New ops skill **`source-intake`** routes a raw
  `sources/` file into the worklogs that absorb it (cited there, never from an artifact).
  `OPERATING-LOOP.md` step 6 names the working. **`EXTENDING.md`** gains the section/column dial.

### The local console (read-only) + one shared read layer

- **`tools/loops/`** — one parser for frontmatter, anchors, register tables, config/state, steps,
  statuses and wiring; `tools/lint.py` refactored onto it.
- **`tools/ui/`** console: cycle position, gate ticks, registers, metric series, open `— to clarify —`,
  change-log timeline, linter findings. Python stdlib, loopback, **no write path** (`POST` → 405).
  House-standard repaint (one red, navy, grey); step rail; accordions/tables instead of cards; *Sources*
  tab; per-browser language + light/dark theme; multi-product / umbrella instances; a dot per chart
  reading. Double-click launchers `console.command` / `console.bat`.
- **Save as HTML** / `serve.py --export`: one self-contained offline snapshot from the same renderer +
  linter verdict — a copy to hand over, not a deliverable.
- The linter now **finds the instance by marker** (takes paths; prints `instances checked: N`; zero now
  reads as a problem). A multi-table register spans every table (check **J**); the console's linter
  parser is open-ended (was `A-G`, dropped checks H–I).

### Metrics capture & the field-report wave

- New ops skill **`metrics-capture`**: name the question before the source; a changed derivation mints a
  new id; declare population + identity rule; compute `observed_n`; verify independently; land rows + a
  `source-method` file + a change-log entry, raw capture deleted.
- `metrics.csv` gains **`observed_n`** (a cohort divides by the observed, not the whole cohort; empty
  value = not yet observable). **`basis`** = how a value was computed only; new **`population`** column
  (rows don't compare across it). `note` column + `tags` written into `REGISTERS.md`; check **D**
  extended to `status`/`confidence`.
- One-id-one-row (check **K**); `superseded` status for a split hypothesis; `sources/` has three roles
  (access · **method** `node_type: source-method` · evidence); raw captures never committed; negative
  results get a *Checked, not confirmed* table + the register-change-log-names-ids rule + a console
  trail (`⟲ n` per row).

### Framework hygiene & vendor-neutrality

- **`config.yaml` has a schema** (check **H**); **a product's own skills** live in
  `product-loops/tool-skills/…` (check **I**). New **`EXTENDING.md`** — the map of adaptation dials.
- **`AGENTS.md`** is the one home of the agent rules (cross-vendor); `CLAUDE.md` is a pointer only.
  `install/README.md` gains *Running on an agent other than Claude Code*; requirements name the real
  constraint (a frontier-class, long-context model).
- **Where a new rule goes — contract · method · check** (`CONVENTIONS.md`); **the four-sign test for a
  new register** (`REGISTERS.md`); `OVERVIEW.md` stops restating what lives once elsewhere.
- Linter false-positives fixed: check **F** ignores `[[…]]` inside a fenced block (Mermaid nodes); the
  tool marker parses `<!-- tool: A, B -->`; a malformed `confirmed:` date is an ERROR, not a WARN.

### Naming brought into line

- **Step 1 is `concept` end to end** — `steps/1-concept/`, `1-concept.md`, worklog `1-concept/` share
  one stem (kills the `1-passport/`-vs-`1-idea/` folder trap); first section `{#concept}` → `{#idea}`;
  gate ids are `concept#…`; "passport" now means only the delegation acceptance passport.
  `CONVENTIONS.md` 0.19.0 → 0.20.0 drops the obsolete step-folder special case.
- **Instance folder `product/` → `product-loops/`** (collides with product repos' own `product/`);
  legacy `product/` still recognised, discovery is by marker.
- New **`GLOSSARY`** (now `process/reference/GLOSSARY.md`) — the entity vocabulary + a renames table.
  Only framework files are renamed; `examples/` are left to the from-scratch rebuild, so the linter stays
  red on them by design.

### Always-loaded canon slimmed — contract stays, procedure moves out

- The four `process/` files an agent reads **every pass** are down from ~1150 to ~920 lines (`CONVENTIONS`
  385→253, `OVERVIEW` 293→238, `OPERATING-LOOP` 258→235, `REGISTERS` +id-taxonomy / −four-sign). Only a
  contract two readers must agree on stays in the core; procedure and extension-time rules move to their
  owner.
- New **`process/reference/`** — canon read **on demand**, not in the reading order: `column-keys`,
  `config-schema`, `node-type-matrix`, `worked-example`, `late-hypothesis`, and the **`GLOSSARY`** (moved
  from `docs/`, reframed as a *map* of names, not a second definition home). Each is reached from a
  one-line stub in the core file that needs it.
- *Where a new rule goes* and the *four-sign test* moved to **`EXTENDING.md`** (they govern changing the
  framework, not a pass); the confirmation procedure and raw-data routing point to the `theses` /
  `source-intake` skills that already own them; the `H-`/`R-`/`M-` id taxonomy is now owned solely by
  `REGISTERS.md`, with `CONVENTIONS` keeping only the link form.
- **OVERVIEW** rewritten: adds the **three-homes document model** (worklog = source of truth · registers =
  shared ids · artifact = projection of the worklog, *not* grown from the registers), names the worklog /
  column-key / confirmation-gradation machinery, drops stale "Phase 1" vocabulary, and points at the
  console and linter as consumers of the one structure.

## [0.8.2] — 2026-07-22 — One-page overview in the README

- **One-pager diagram** (`docs/onepager.html` + rendered `docs/onepager.png`): the whole
  framework on a single page — the six steps, the three living registers running through them as
  vertical rails, the working loop, the fixed-core/pluggable split, and the deliverables. Embedded
  near the top of the README.
- Docs only — no change to framework mechanics.

## [0.8.1] — 2026-07-21 — Single changelog

- **Single changelog:** framework files no longer carry inline `## Change log` sections —
  their history is consolidated into this file, keyed to git tags. Instance artifacts (a
  product's own step outputs, registers, sources, handoff) still keep their change logs; that
  reasoning trail is a product feature, not maintainer bookkeeping.
- `process/CONVENTIONS.md` updated accordingly: the node_type matrix now routes framework-file
  history to this changelog, while instance artifacts keep the dated-change-log convention.
- Docs only — no change to framework mechanics.

## [0.8.0] — 2026-07-21 — First public release

- **License:** the project is now released under the MIT license.
- **Contributing guide** and this changelog added; the README is marked released.
- No changes to the framework mechanics beyond 0.7.0 — this release opens the project
  for others to use and vendor.

## [0.7.0] — 2026-07-21 — Wiring hardening

- **Linter + CI:** `tools/lint.py` (dependency-free) checks wiring and enums; runs in
  GitHub Actions on every push and pull request. First run surfaced ~15 desyncs the eye
  had missed.
- **One link canon:** cross-artifact links are relative paths + `{#anchor}`; the
  `[[…]]` wiki-link machinery was removed.
- **`state.yaml`:** the cycle's position (current step, gate ticks) now lives in a
  separate `state.yaml`, apart from the human-facing `config.yaml`.
- **Enum discipline:** register `type`/`category` are single-valued, with an optional
  non-load-bearing `tags` column for cross-cutting themes.
- **Versioning contract:** real git tags, plus a `FRAMEWORK-VERSION` file written at
  install time echoing the pinned tag + commit SHA.

[0.8.2]: https://github.com/timamikh/very-ai-product-loops/releases/tag/v0.8.2
[0.8.1]: https://github.com/timamikh/very-ai-product-loops/releases/tag/v0.8.1
[0.8.0]: https://github.com/timamikh/very-ai-product-loops/releases/tag/v0.8.0
[0.7.0]: https://github.com/timamikh/very-ai-product-loops/releases/tag/v0.7.0
