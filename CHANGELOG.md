# Changelog

All notable changes to very-ai-product-loops are recorded here. The format follows
[Keep a Changelog](https://keepachangelog.com/), and the project uses
[Semantic Versioning](https://semver.org/): `MAJOR.MINOR.PATCH`.

- **PATCH** — fixes and wording; nothing breaks for existing users.
- **MINOR** — new capability, backward compatible.
- **MAJOR** — a breaking change; adopters must adjust their instance.

The version you pin to is the **git tag**; this file is its human-readable story.

## [Unreleased] — The local console + one shared read layer

**Vendor-neutral by name, not just by claim.** The framework never needed a vendor API, but its entry
points were spelled for one tool. Now:

- **`AGENTS.md` is the one home of the agent rules** (the cross-vendor name Codex, Cursor and others
  auto-load). The root `CLAUDE.md` remains as a **pointer only**, because Claude Code auto-loads that
  name — one home, two names for the door, nothing normative in the pointer. The six step templates,
  both skills and the README now cite `AGENTS.md`.
- **`install/README.md` gained *Running on an agent other than Claude Code***: what Claude Code does for
  you (auto-loads the rules, exposes `product-setup` / `start-work` as slash-skills, runs the linter on
  request) and the one-line workaround for each elsewhere — the skills are plain markdown a human can
  point any agent at.
- **The real constraint is stated where it belongs** (install requirements): a frontier-class model with
  a long context. The framework depends on the agent working *one section per pass*, opening a method
  before filling its section, and writing `— to clarify —` instead of a plausible guess. A weaker model
  bulk-fills the template and it *looks* finished — and the linter cannot catch that, because it checks
  wiring and enums, never whether a claim is true.

**[`EXTENDING.md`](EXTENDING.md) — a new file: the map of the adaptation dials.** Four of them already
had procedures, each inside its own index (add a method · add an adapter · add or change a status ·
where a product's own skills live), findable only if you already knew which plane you wanted. Two had
none at all:

- **changing the work directions** — what depends on them (Steps 5–6 grouping, a status's per-step goals
  when split by direction, the required `config.yaml` key) and the pass that changes them safely;
- **adding, removing or reordering a step** — first the five cheaper dials that nearly always turn out to
  be what was actually wanted, then, if none fit, the honest cost list (gate items keyed to
  `artifact#section`, relative links, homeless methods, every status needing a new `per_step` block,
  renumbering as a rename) and the fact that it is a fork or an upstream change, never an instance edit.

The file routes rather than restates: one procedure per dial, in one place.

**Canon** — two decisions the console forced into the open, now pinned and enforced:

- **`config.yaml` has a schema** (`process/CONVENTIONS.md` 0.6.0 → 0.7.0): `product` · `language` ·
  `active_status` · `directions` required; `scope_note` · `metric_source_slots` · `sources` ·
  `products` optional; one spelling each, no aliases. New linter **check H** enforces it (a
  sub-product that inherits its parent's config passes by design). Readers stay tolerant and report
  the drift; the linter is where strictness lives.
- **A product's own skills have a home** (`tool-skills/README.md` 0.1.0 → 0.2.0):
  `product/tool-skills/<plane>/<name>/` — same anatomy as a vendored skill, local wins on a name
  collision, survives re-vendoring. New linter **check I** holds local skills to the same wiring
  rules (produces homed, fragment anchor present, steps declared).

**The console is read-only — by construction, not by phase.** It is a viewer, not an interface to the
process: the human asks an agent, the agent runs the loop and writes the files, the console renders what
they now say. So the one write path that existed (a scaffold for a new skill) was **removed**, together
with the designed-but-unbuilt phases (a validating writer for the human's own decisions, an agent
bridge). `POST` answers 405 and `tools/loops/` is a read layer with no writer in it.

The reasoning, now in [`tools/ui/README.md`](tools/ui/README.md): everything a UI here could offer either
**carries a method** (a section, a register item, a new skill's body — needs the method, a prerequisite
check and a confidence judgement, which a text area cannot do) or **carries a decision** (status,
directions, a gate tick, a metric reading — needs a dated reason, which is a sentence you say to the agent
anyway). Both go through the same door, so the defence cannot be eroded by a later feature and the
framework keeps one mechanism per change. The *Skills* tab still shows every skill the agent can reach and
now points at `EXTENDING.md` for adding one.

**Console, second pass** — tested against three live instances (not the framework's own example):

- **Any canon folder renders.** A path typed into the header is read on the spot. Three real
  deviations are now handled and reported instead of silently mis-rendering: a `config.yaml` that
  never names the product, non-canon key spellings (`metric_sources`, `product_scope`), and a
  **multi-product** instance (`products:` in the parent config, one folder per product) — the parent
  is an umbrella, each sub-product inherits language / status / directions / title and the shared
  `sources/`.
- **Interface language from `config.yaml` → `language`** (ru / en, English fallback). Chrome is
  translated; content stays in the language it was written in.
- **Light / dark / auto theme toggle**, remembered per browser, explicit choice winning over the OS.
- **Step canvas** replaces the old list view: one card per section with its real lead line, first
  bullets, tick, confidence mix, gaps, ⚙️ count and linked register ids; the status's asks and the
  full gate beside it.
- **Skills tab**: every skill the agent can reach (vendored library / operations / adapters + the
  product's own local skills), its wiring, its files, and a `homeless` flag — the linter's check that a
  declared section has a home, surfaced before it fails.
- Step goals are now read from each step README's own `**Goal.**` line, so nothing is restated in code.

## [Unreleased · first pass] — The local console (read-only) + one shared read layer

- **Local console** (`tools/ui/`): `python3 tools/ui/serve.py` serves a browser view of one instance —
  the cycle's position and gate ticks, each step's artifact skeleton with how filled its sections are,
  the three registers as filterable tables, metric series charted straight from `metrics.csv`, every
  `— to clarify —`, the change-log timeline, and the linter's findings. Python 3 stdlib only, loopback
  only, **no write path in this phase**. The write policy and the vendor-neutral agent bridge (a prompt
  handed to *any* agent, the filesystem as the bus) are specified in `tools/ui/README.md`.
- **One shared read layer** (`tools/loops/`): frontmatter, section anchors, register tables, the
  `config.yaml`/`state.yaml` YAML subset, steps, statuses and library wiring are now parsed in exactly
  one place. `tools/lint.py` was refactored onto it — same checks, byte-identical output.
- **Linter fix — enum checks were language-blind.** Check D looked for an English `type`/`category`
  column, so a register written in the product's own language silently escaped validation (it reported
  "no column found" as a warning). Enum *values* are canon; column headers now accept the instance's
  language. On a real Russian-language instance this turned 2 warnings into 8 genuine errors.
- **`process/OVERVIEW.md`** (0.5.0 → 0.5.1): says where the console sits (a lens over the structure,
  not an aggregator and not a home for values); the stale "Typed links (GitMark-lite)" bullet now
  states the actual link canon (relative path + `{#anchor}`).

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
