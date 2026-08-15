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
