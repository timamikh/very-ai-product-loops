# Changelog

All notable changes to very-ai-product-loops are recorded here. The format follows
[Keep a Changelog](https://keepachangelog.com/), and the project uses
[Semantic Versioning](https://semver.org/): `MAJOR.MINOR.PATCH`.

- **PATCH** — fixes and wording; nothing breaks for existing users.
- **MINOR** — new capability, backward compatible.
- **MAJOR** — a breaking change; adopters must adjust their instance.

The version you pin to is the **git tag**; this file is its human-readable story — a record, never a
rule: where a bullet here and the canon in `process/` disagree, the canon wins.

## [Unreleased]

Work accumulated since 0.8.2, grouped by area (collapsed into one release when a tag is cut).
Bullets are theses; the reasoning for any item lives in its commit and in the `process/` canon.

### Audit batch 4 — one read layer, tested

- **The linter reads everything through `tools/loops`.** `metrics.csv` via the new
  `instance.metric_rows` (field-count and comment-line errors — hub F-01/F-05); registers via
  `instance.load` health; one `worked` definition (`framework.worked`, placeholder-shaped lines
  ignored in any language); change logs located by `text.without_change_log` in any language. No
  second parser remains.
- **A line names a block.** `text.block_after` / `block_at` / `marked_block` are the primitive; P2
  reads the Inputs block (daisy F-02), ignores ids in code and fences, covers ids quoted from declared
  sections and declared-atom rows (daisy F-03, hub F-09), reads `M-7d`-style ids.
- **Gate ticks have states** (`framework.GATE_READINGS`): G2 warns only on an unrecorded `open`; a
  recorded reopen for re-sign is silent (hub F-10). G3 validates tick values, G4 that a tick names a
  real gate item. Check P tells a missing worklog, a wrong step folder and a true orphan apart
  (daisy F-05).
- **New checks.** C1 (a section a method works from is a `reads` atom; hand-off mentions exempt),
  C3 (decision-standard method ships a Decided line), C4 (step ≥ 4 section fragment declares its
  card), C4b (one card face per shared section), C6 (numeric `volume_rule` floor carries `min:`),
  C9 (template ↔ fragment column parity by header), W2 ("Worklog & projection" ≤ 120 words), T2
  (`sources/snapshots/` gitignored), T3 (secret scan — ERROR), H3 (handoff names a register), G5
  (content script vs `config.language`), Y2 (`yamlite.unsupported`: flow maps and lists of maps
  reported with file:line). D missing key is WARN on a product instance, ERROR under `examples/`.
- **Tests.** `tools/tests/test_lint.py` (58 cases) runs the linter on a defect fixture and a fake
  library; every hub/daisy finding with a code fix has a regression case. CI runs it next to
  selftest.
- **`lint.py --ci`** skips gitignored instances and names them, so the local verdict matches CI.
  `.gitignore` gains `sources/snapshots/`. Lint on the example runs in 0.3 s.

### Audit batch 5 — one home per rule

- **The always-loaded core is deduplicated.** `AGENTS.md` is a door: reading order plus the
  non-negotiables as one-line pointers to each rule's one home. OVERVIEW is concept only,
  OPERATING-LOOP the procedure, CONVENTIONS the notation, the reference files the detail. Core
  5760 → 4597 words; check W is silent.
- **One section per pass** is canon in OPERATING-LOOP move 1 (with its one widening: a method whose
  single worklog fills several sections); start-work and product-setup point there.
- **The write rule has one text** — OPERATING-LOOP → Delegation: the orchestrator writes registers,
  sections, sign-off and ticks; a `draft` subagent writes exactly the worklog its brief names,
  change-log entry included; gather/research/verify write nothing. The brief template §2 and the four
  `loops-*` agent definitions carry it verbatim; everything else points there.
- **The goal map loses its *Move-5 surfaces* column** — a card's `surfaces:` is the home.
- **REGISTERS.md opens with the one enumeration** — four registers, six files, five id prefixes,
  their atom names; product-setup scaffolds exactly that set.
- **Vocabularies that lived only in code get a canon carrier:** `process/reference/state-schema.md`
  (state.yaml shape, tick values, the recorded reopen for re-sign), the typed `sources/INDEX.md`
  header in boundary-layout, the closed `node_type` set in the matrix, the question types in
  `extending/method.md`, the word budget in `extending/rules.md`, the "worked section" in
  CONVENTIONS, the shared scales in `process/reference/scales.md`.
- **Rules name their checks:** `projection` writes in `config.language` (check G5); N8 names the
  linter's secret scan; `sources/snapshots/` is gitignored by default (check T2); `metrics.csv`
  holds data rows only (check E).
- **install/README** describes delegation on a non-Claude agent (the orchestrator runs each brief
  itself); **UPDATE.md** gains *Adopt an existing instance* for a filled instance from an earlier
  framework version.

### Audit batch 3 — the console reads keys, shows what was written

- **Every board reads by column key only.** A table that lacks a key the board needs shows an
  explicit "board not drawn — lacks `c:key`" note beside the section's card instead of a guessed
  column. One table parser (`tablesOf`), blank-line continuation identical to the linter's.
- **Prose heuristics are gone.** Driver family, instrumentation, channel state, moat state, risk and
  hypothesis status are read as exact enum tokens from the model. The few reads the templates do not
  key yet sit in one TEMPLATE-KEY-DEBT table at the top of `app.js`, to be deleted with the key
  migration.
- **No composed text.** No truncated tiles or labels, no invented bullets, currency taken from the
  author's cell; the four competitor sections are four cards, not a merged table; North Star and
  Horizon shown whole.
- **Step 5 gets its canvas:** goal lanes by direction, target tiles, guardrail plates, resources,
  bundle cards, threshold gauges, readout tables. **Step 6** items group by whatever direction token
  they carry; F-ties resolve by id pattern.
- **Accessibility:** expand is a real button (no nested interactives), skill rows are
  keyboard-operable, tooltips reachable by focus, tag meanings in visible text.
- **Export** carries instance-relative paths, no worklog bodies (private to the method), lint
  findings and counts only; the console README describes `--export` writing into `export-files/`.

### Audit batch 2 — the library declares what it reads and shows

- **The reads perimeter is closed for steps 4–6.** Every section a method reasons from is a
  `section:` atom on its card; declared-but-unused register and source atoms are removed (a register
  atom is used when the card cites its id family); `impact-readout` names its one forward edge to
  `6#must`.
- **Every step 4–6 fragment declares its `<!-- card -->` face**; the three double-faced sections
  (`{#cjm}`, `{#value-defensibility}`, `{#pricing}`) project one slot each; every
  `evidence_standard: decision` method ships a Decided line (`where-to-play-how-to-win` one per
  section).
- **`process/reference/scales.md`** is the one home of the hypothesis, priority, signal, decision and
  risk gradations; six methods point there instead of `hypothesis-test-design` §Scales.
- **"Worklog & projection" is method-specific** in all 47 cards (5336 → 2458 words) plus a pointer
  to `worklog-resolution`; the gap-report paragraph (check L2) and the long Decided placeholder are
  gone.
- **Step-6 product axis:** item fragments mirror the template field for field (Owner, Groom); the
  backlog carries Feature and Est.; one notion of estimate (class S/M/L plus range, set by the spec,
  summed by the ranking); `pricing-strategic-plan` re-projects the full `{#pricing}` form; each
  fragment's first table carries its template's column names. `volume_rule` floors carry `min:`.

### Audit batch 1 — the canon decisions

- **A revisit owns its worklog.** A later step's method named on an earlier step's marker
  (`cjm-strategy` on `1#cjm`, `value-definition-strategy` on `1#value-defensibility`,
  `pricing-strategic-plan` on `3#pricing`) works in its own worklog in its own step's folder, reads
  the earlier worklog as a declared input, and re-projects the section. A contributing method of the
  same step likewise keeps its own file; the first tool in the marker owns the section's thread.
  `worklog-resolution` carries the rule, the two revisit cards follow it, check P accepts the
  revisit's folder, and two new checks hold the wiring: **B2** (a card that writes a section is named
  on its marker) and **P3** (a step README's skeleton row and the template marker name the same
  tools). Any other return to an earlier section comes through a register revision.
- **No tag = `assumption`**, once: N7 now says it the way CONVENTIONS and check D2 always did.
- **Template drift is debt on a product, an error on the example.** O2/O3 report WARN on a vendored
  instance whose template moved under it (install/UPDATE.md) and ERROR on `examples/`.
- **questions.yaml is the agent's interview script** and nothing more: the fillable-file promise and
  the duplicated `writes:` are gone from all 47 files (check A2 now forbids the field); three
  `single_select` questions got their options.
- **The vendored layout is canon**: the framework's folders at the product repo's root, the product
  beside them in `product-loops/`. Check I2 reads that layout (and still the legacy sub-folder one);
  install/README holds the one list of what is vendored, UPDATE.md and product-setup point at it.
- **CHANGELOG is a record, never a rule**; UPDATE.md reads the diff between pinned SHAs. No tag is cut
  until the rework lands on a green CI; README says so.

### Audit batch 0 — what was broken now, mechanics only

- **Read layer**: frontmatter block lists (`prerequisites:` then `- item` lines) parse as lists — ten
  cards had been reading as empty, and a block-form `reads:` was a silently empty perimeter.
  `products:` in a multi-product `config.yaml` is documented in block form (the reader never accepted a
  `{ … }` flow map); a flow-map entry now surfaces a health warning instead of crashing the load.
- **Cards**: a `file:` atom's argument is validated — a path without spaces, instance-relative (never
  `product-loops/…` or absolute); `theses` writes the bare `sign-off` atom; six cards drop the
  host-relative prefix. `where-to-play-how-to-win` names the two real value-definition methods.
- **Linter**: `--help` prints usage instead of "not a folder"; the no-instance hint says
  `product-loops`; one `instance.load` per instance per run (1.56 s → 0.24 s on the example).
- **Console**: the hypotheses-in-flight table reads `c:statement` (the register's key); a step-2 board
  that cannot draw its section falls back to the section's card, and the three competitor readings
  render as cards; the `**North Star:**` and `**Horizon:**` lines are read as blocks, not physical
  lines; metric-family and retention-series hues are theme tokens; `--faint` reaches AA at small
  sizes; the strategy cascade draws its arrows on the cards (no arrow ever wraps alone) and stacks
  when any card is wide; the four NUL bytes are gone from `app.js`.
- **Server**: requests must carry a loopback (or bound) `Host`, and an `Origin` when present must
  match — DNS rebinding sees 403; `/api/file` serves instance files and skill-folder files only,
  paths resolved through `realpath`.
- **Docs**: product-setup's boundary-layout link resolves; README and tool-skills/README list all
  seven operations and `feature-to-spec`; install/README quotes the linter's real `instances checked:
  0` line.

### Step 4 gets its canvas and the metric tree keys its families

- **Console: seven strategic-plan boards** — the metric tree drawn (North Star over its driver nodes,
  each node's border its data source: instrumented / proxy / none; each node's chip its metric
  family), horizon-target cockpit tiles, the unit-economics contribution waterfall + CAC/payback/LTV
  tiles, per-cohort retention curves (a censored cell is a gap, not a zero), capability shields
  (reusing the moat plates with a red missing-band), the risk-mitigation heatmap (the pre-mortem 2×2
  now with answers — dots coloured by lifecycle status, the panel showing mitigation · owner ·
  trigger · due), and hypothesis threshold gauges (fail zone · conscious inconclusive gap · pass
  zone). Each reads its columns by `<!--c:key-->` only and falls back to the section's ordinary card.
- **The metric-tree Driver column is the metric's family**: step-4 template 0.6.0 declares
  `enum:c:driver: acquisition · activation · engagement · retention · referral · revenue · quality ·
  cost` — AARRR plus the behavioural, product-health and COGS families AARRR has no slot for. One
  token per cell, read literally onto the console's family grouping; cohorts and funnels are *views*
  of these families, not families. `metric-tree` 0.4.0 prescribes the one-token cell and gains a
  `<!-- card -->` face on the North Star line. The board still infers a family from prose so a
  pre-enum instance groups too.

### Step 3 joins the perimeter and the strategy canvas gets its boards

- **The ten step-3 cards declare in `reads` what their prerequisites already demanded**:
  `where-to-play-how-to-win` 0.3.0 reads the whole step-2 table (it is the step's synthesis method);
  `value-definition-strategy` 0.2.0, `uvp-cpv` 0.3.0, `pricing-strategy` 0.2.0 (the step-2 price
  anchor — the sizing-revisit door), `channels-expansion` 0.3.0, `product-surface` 0.5.0,
  `architecture-c4` 0.3.0, `bets` 0.2.0, `pre-mortem` 0.2.0 each carry their named sections;
  `cjm-strategy` 0.3.0 adds the cascade and channels it re-walks the map against. Register seeders
  read the registers they seed.
- **All ten step-3 fragments carry `<!-- card -->` slots with a prescribed line form** (aspiration ·
  arena call · winning logic · moat read · one-liner · price stance · channel read · surface read ·
  context read · lead bet · death read · journey read) — the face is authored by the method under a
  stated form, not composed at projection; garbage cannot ride an unspecified slot.
- **Widget-feeding cells become named requirements**: step-3 template 0.6.0 — keyed price-anchor
  table (`altprice`/`ourprice`), channel `segment`+`state` (enum live · building · leaking ·
  untested), bets `moat`+`order`; step-1 template 0.9.0 — keyed moats table (`moat`/`have`/
  `rebuild`); fragments prescribe literal cells (H/M/L one letter; Emotion `▲/▼` plus `(was …)` on
  revisit-changed rows; prices as numbers).
- **Console: six strategy boards** (price ladder against every named anchor, journey emotion curve
  in two layers, pre-mortem heatmap 3×3 with focusable dots, ordered bets board, moat shields,
  channel → segment map) — each reads its columns by `<!--c:key-->` only and falls back to the
  section's ordinary card when an instance lacks the keys.

### The face is a slot: the method decides its card once

- **The card slot lives in the fragment** (CONVENTIONS 0.33.0, projection 0.6.0): a method's
  `template-fragment.md` carrying a live `<!-- card -->` has declared which element is the
  section's face, and every projection places the instance's mark there — judgement remains only
  where no slot is declared. Six step-1 fragments now carry slots (cjm waits for a live example);
  `segment-pains` and `concept-expansion` gained the conclusion line both live instances had
  already written for themselves.
- **A face is text + table, full-width** (console): a card whose section has a `<!-- card -->`
  line shows that line **plus the section's own first table** and takes the full row; an
  `<!-- open -->` inbox section is shown whole — a list of open items has nothing to collapse.
  Wide is the norm on a data-bearing step, not the exception.
- **Duck test at projection** (projection step 2): a section must read without the pass's context —
  fragment labels are translated, never renamed or multiplied; metaphors unfolded; code names
  expanded at first use.
- **Check C2** (lint, WARN): a fragment-declared slot with no `<!-- card -->` mark in the projected
  section; whether the mark sits on the *right* element is semantic — step-close 0.3.0 audits it.

### The input perimeter + the card line names a block

- **Step 2 joins the perimeter**: the five step-2 cards now declare in `reads` everything their
  prerequisites already demanded — `market-sizing` 0.4.0 reads the concept, the segments and the
  step-1 value work (its first-pass price); `competitor-analysis` 0.3.0 reads the concept, the
  segments and the **sized arena** (`section:market-sizing` — the SAM cut names where to sweep);
  `competitor-pricing` 0.2.0 and `competitor-dynamics` 0.2.0 read `section:competitors` (the list
  they scan is made by a neighbour, not conjured); `substitutes` 0.2.0 reads the job, the segments
  and the sized arena (what the segment already spends is where substitutes hide). Register
  seeders now read the registers they seed.
- **Step-2 sections get faces**: all five step-2 fragments (plus `cjm-concept`'s, its live example
  arriving) gained `<!-- card -->` slots — a one-sentence read (sizing read · field read · strategy
  read · price anchor · momentum read · strongest substitute) above/beside the section's first
  table. Column keys stay on the **step template** per canon (check O reverted an attempt to plant
  them in fragments — the draft is matched by meaning). Console: `substitutes` and `opportunity`
  now render as cards with faces (collapse/expand, 5-row table cap) instead of raw markdown dumps.

- **`cjm-concept` 0.4.0 — the map produces the interview plan, it does not wait for one**: the
  apply trigger is the journey's time structure mattering to the concept (a long multi-actor path,
  pains living at different stages); an assumption-tagged map is a legal first pass whose breakage
  points seed `H-…` — the sprint's interviews are planned against those rows. Skip only when the
  journey is trivial for the concept; the call is never about a source the instance lacks ("no
  interviews yet" waits for what this map produces; "no funnel data" imports a running-product
  signal into a step that never had one — both named anti-patterns). `evidence_standard` clarified
  as an honesty bar for `[sourced]` tags, not an entry bar. Step-1 template `{#cjm}` lead recut to
  match; the fragment gained its `<!-- card -->` slot (face = *Moments that matter* + the journey
  table).

- **`source-intake` 0.4.0 — dispatch respects the perimeter**: a fact is routed only into worklogs
  of methods whose `reads` carries the source's typed slot (the INDEX `type` column names it) — a
  `research` snapshot never lands in a step-1 method that reads only `kb`/`interview`, however close
  the topic. Forward-only: rows dispatched before the rule are a record, not an error. New
  anti-pattern *Dispatch past the perimeter*. Found by the daisy step-1 re-run: the old intake had
  routed research snapshots into six step-1 worklogs their methods had to ignore.
- **A skipped section owes no paperwork** (lint P/O2): a gate item ticked `n/a` — the conscious
  skip — no longer demands a worklog (P) or template keys (O2) for its section; both checks guard
  filled projections. Found on daisy: an honestly skipped `#cjm` sat as two permanent errors.
- **The step ring shows written-but-unverified** (console): the outer gate arc gains a faint tail —
  gate items whose sections are worked but not yet ticked/verified. An all-open step full of drafted
  sections no longer shows the same zero as an untouched one; the faint arc never counterfeits a
  closed gate. Tooltip and legend updated.
- **`segmentation` 0.7.0 — the perimeter loses its one forward edge**: `section:value-defensibility`
  is out of `reads` — the moat is stated *later* in the step, so it cannot be an input to the
  primary pass. Tier ranking at concept stage runs on need-difference × reachability; a moat-driven
  re-cut is a later re-run with `<!--w:adds-->` recording the door, or the Step-3 revisit. The
  daisy step-1 orchestrator hit this edge independently on the same day the perimeter rule shipped.

- **`reads` is a perimeter, not a hint** (card-schema): a method's **primary worklog pass** draws
  on the declared atoms and nothing else — a missing input is a declared gap, never a substitute.
  Wider context enters through two **recorded** doors, both the orchestrator's: the conclusions
  block (its heading now carries `<!-- orchestrator -->`, machine-findable in any language) and a
  rework order that supplements the perimeter. Four ambient inputs stay undeclared: the card, its
  own worklog, `config.yaml`/`state.yaml`, the human's answers to the method's own questions.
  `prerequisites` names a prose subset of `reads`, never more. OPERATING-LOOP move 2 gains the
  fourth law; a `draft` brief's inputs are **assembled, not chosen** (orchestration), and the
  first draft never gets a supplement — that is a rework decision.
- **The worklog records the perimeter it ran under**: the skeleton gains
  `**Inputs:** <!--w:reads--> … · **Supplements:** <!--w:adds--> none` — keys canon, labels free
  (the decision-line pattern). New check **P2** (all WARN) holds the keys, the atoms' grammar and
  the two mechanical citation classes (section anchors, register ids) to that line; the change log
  and the orchestrator's block are exempt; pre-perimeter worklogs get one aggregate WARN.
- **Step-1 cards declare what the hub run showed they actually eat**: sections
  (`section:jtbd`, `section:problems`, …) and registers enter `reads` on all seven method cards —
  reverse-engineered from hub-v012's real consumption; the observed cross-step leaks stayed out,
  they are exactly what a recorded supplement is for.
- **One slot vocabulary**: CONVENTIONS aligns to `cards.SOURCE_SLOTS`
  (kb · interview · research · metrics · git); a dated human decision is a legal `[sourced:]`
  origin, not a slot.
- **The card line names a block, never a physical line** (`card_line`): the trailing form collects
  the whole paragraph or bullet across soft wraps — a lead marked on a hard-wrapped paragraph's
  last line no longer returns one truncated line (the hub case, now a selftest).
- **Console**: the step-goal boilerplate moves off the page into an ⓘ dot beside the step title.

### The axis on every status + the priority cascade (v0.13)

Two rulings from the hub-saas test run's owner. First: the axis obeys the general principle —
**a method is gated by its own prerequisites, not by the status**. A concept-viability product
with a landing page already has an as-is to inventory; a shipped prototype slice is already an
impact to read. Second: an item's priority is not born at Step 6 — the knowledge exists earlier,
it just had no carrier.

- **`product-baseline` and `impact-readout` run at `concept-viability`** (statuses/1 names both);
  the skill's "not at concept-viability" clause is gone — with nothing shipped, baseline skips by
  its own first prerequisite. Check E3 expects the item pre-registration on every status.
- **Surfaces' three birth doors are canon** (`REGISTERS.md`): `product-surface` ledgers designed
  surfaces as `planned` (Step 3, pre-build) · `product-baseline` inventories the live ones ·
  `activity-spec` may mint a new g2m surface at Step 6 — the last two now declare the write.
- **The priority cascade**: `features.md` gains an optional `priority` column (`now · next ·
  later`). Step 4 (`strategic-targets`) seeds the structural weight — a feature whose `serves`
  target is committed, or closes a top risk, outranks one moving a peripheral node; Step 5
  (`prioritization-tactical-plan`) finalizes by period fit; Step 6 ranks a **weighted pool**
  instead of a cold list, adding only cost/confidence. `capabilities-systems` grounds its
  capability walk in the live rows. Optional column: a register that pre-dates the cascade is
  legal until the first pass writes it (`OPTIONAL_ENUM_LABELS`, like signal/decision).
- Baseline assembles its sources before walking: read `sources/INDEX.md` for the method's slots,
  show the owner the list, ask what's missing — a gap is declared, never silent.

### The product axis: surfaces → features → items, with an impact loop (v0.12)

Steps 3–6 gain the register that was missing between them: what the product *is made of*. The
framework's target action — issue items that move `R`/`H`/`M`, then check whether they did — now
has both halves. Design: `DESIGN-product-axis.md`; migration: `install/UPDATE.md` → Migrating.

- **Fourth register: features & surfaces** — `registers/features.md` (`F-001…`) +
  `registers/surfaces.md` (`S-01…`), one schema in `process/REGISTERS.md`, skeletons in
  `process/reference/register-skeletons/`. As-is and to-be in one table: `state: planned · live ·
  retired` (new enums, linted like every other); `direction` stays instance vocabulary, not an
  enum. Two files for the same reason the metric register is two: the reader takes one id-table
  per file.
- **Step-6 items lose their positional letters.** `F-1`/`A-1`/`T-1` looked like register ids and
  died with the sprint. Items are now numbered `1, 2, …` inside their direction subsection; the
  cross-sprint identity is the `- **Feature:** F-…` line every item carries (many items may
  advance one row). Each item pre-registers `- **Expected impact:** … · check-by …` and an
  `- **Estimate:**` class (S/M/L); the backlog gains a `feature` column.
- **Two new library methods.** `product-baseline` (step 3, drift-triggered, not at
  concept-viability): inventories live surfaces/features from sources into the register —
  reconcile, never re-author. `impact-readout` (step 5, new `{#item-readouts}` section): reads
  shipped items against their pre-registered expectations — `confirmed / missed / inconclusive /
  pending`, flips `planned → live`, reads estimate-vs-actual for calibration; an `H-…` verdict is
  cited from `experiment-readout`, never re-judged. Both named by the pmf/growth statuses.
- **Linter: E2/E3/E4 (all WARN)** — a cited `F-…`/`S-…` resolves to a register row (mirror of E,
  change logs exempt as history); a worked must item at pmf/growth names its `Feature:`; a
  feature/surface row shows its `source`. Checks D/K/O2 extend to the new files/columns; the
  step-6 gate gains `item-feature`.
- **Console.** Registers view gains Features and Surfaces tabs (state enum-guarded, direction/type
  as facets); the Surfaces tab opens with a board — one column per surface, feature cards coloured
  by state, must-advanced features flagged, click-through to the row and its trail. The step-6
  board parses the new numbered items (direction from the subsection heading; legacy `[FAT]-n`
  still reads), and `F-…`/`S-…` ids get chips/trails everywhere `H-`/`R-`/`M-` had them.
- **Examples.** `decksmith` migrated whole (F-001…F-008 / S-01…S-09 minted from its own specs,
  items renumbered, empty item-readout stated); `tolmach` migrated minimally (skeleton registers,
  renames, `item-feature: deferred`) — the two shapes an adopter can copy.

### Carriers from the second local-model run (Отклик / Qwen 3.8, steps 1–2 end-to-end)

The run closed every finding of run 1 (wave 3.7 held) and surfaced a new class: rules whose carrier
was an anchor, not the content. Everything below is a script or a card — nothing was added to the
per-pass canon (it already runs over the word guideline; the subtraction rule stands).

- **`written` = worked content, not a present anchor** (`tools/loops/framework.py` →
  `template_section_lines`, used by the read model and check G2). Steps 2–6 instantiate their whole
  artifact shell, so "anchor on disk" stopped meaning "section written": the first pass of step 2
  raised nine false move-5 warnings on untouched skeletons, drowning the one real one. A section
  now counts as written only when it carries at least one normalized line beyond its step template's
  placeholder shell (keyed by step *and* id — the cumulative sections repeat their id across steps).
- **A skipped optional section no longer poisons next-pass.** An optional gate item with no explicit
  tick and no worked section defaults to `n/a` in the read model (`tick_defaulted: true`); an
  explicit tick always wins, and writing the section revives the normal `open` flow. Before this, a
  consciously skipped `concept#cjm` sat `open` forever and dragged "where the next pass goes" back
  to a closed step.
- **Check D2 — the confidence-tag vocabulary has a carrier.** CONVENTIONS declares the tags closed
  (`[assumption]` · `[sourced: <where>]` · `[validated: …]` · `[refuted: …]`), but nothing held it:
  a local model localized tags mid-artifact (`[Премия]`, `[Источники: …]`) and invented near-synonyms
  (`[inference]`) that every consumer silently stops counting. D2 warns on off-grammar canon tags,
  on localized tags in the trailing (tag) position, and on a curated near-synonym list — WARN for
  now, promoted to ERROR once the shipped examples clean their pre-grammar tag debt.
  *Follow-up (2026-08-23):* the decksmith example cleaned its 24 pre-grammar tags (compound
  qualifiers moved into notes, bare `[sourced]` given its where) and every D2 tier is an **ERROR**.
- **The risk register carries the `trigger` it was always owed** (run-journal J-004). The
  `risk-mitigation` method writes back mitigation · owner · **trigger** · due · status, but the
  register had no trigger column — the act-now signal had nowhere to land (decksmith's `R-013` had
  it parked inside the mitigation cell). REGISTERS 0.11.0 + skeleton 0.2.0 add `trigger`; the
  decksmith register carries all 13 signals, copied from its step-4 artifact.
- **`--export` lands in the instance, not the launch folder** (run-journal J-002). The default
  destination for the console snapshot is now `<instance>/export-files/` — the convention home for
  files that leave the instance — instead of whatever directory the command happened to run from.
- **Check S2 — `sources/INDEX.md` rows carry a typed slot.** The index header is keyed
  (`<!--c:file-->` … `<!--c:conf-->`) and gains a `Type` column naming which `reads:` slot each
  source serves — `kb` · `interview` · `research` · `metrics` · `git`, the closed list that already
  lived in `cards.SOURCE_SLOTS`. A word outside the list is an ERROR; an untyped row or a keyless
  header WARNs. Carriers: the verbatim keyed header in `product-setup`, the slot line in
  `source-intake` and `reference/boundary-layout.md` — the per-pass canon is untouched (the slot
  vocabulary was already CONVENTIONS' — this wave only gives it a machine-checkable home in the
  index). This is the groundwork for a mechanical evidence gate: an external-sources method can now
  be matched against a typed evidence row instead of a heuristic.
- **Check L2 — an external-sources method shows its evidence or declares its gap.** A worked section
  of a method declaring `evidence_standard: external-sources` that carries neither one
  `[sourced: …]` nor one `— to clarify —` is settled-looking analysis resting on nothing visible.
  The six external-sources cards also state the gap-report rule in prose: **no external source, no
  settled verdict** — load-bearing values degrade to `— to clarify —` naming the source that would
  settle them, never to silent certainty.
- **Market sizing grows a growth layer.** The run delivered TAM/SAM/SOM with no CAGR/trend anywhere —
  silence about growth reads as "flat", a claim nobody made. The step-2 template, the fragment and
  the card now carry Growth as a layer, not an option.
- **Step 2's synthesis sections name their worklog.** The linter (check P) has always required
  `2-analysis/synthesis.md` behind `#niche-risks` / `#opportunity`, but the step README's tool
  column said "—", so both the driver and the agent read "no worklog needed" — documentation
  contradicting a carrier is the same defect class G2/D2 close. The README and the template now
  name `synthesis.md` explicitly.
- **Console.** The STEP figure shows only the *date* of the last pass (the full move-5 narrative
  inflated the card and broke the figs row); every figure is top-aligned (a UA button centers,
  a div tops — one row had two baselines); the Checks tab separates findings about the framework
  itself (the canon word-budget WARN) from findings about the product being read.

### Library & outputs — the dev-handoff chain (feature → groom → written instruction)

- **`feature-grooming` (library, step 6).** The intermediate pass between a featured item and its
  written instruction: enumerates the scope one-to-one, then splits every open fork by kind —
  **product/UX/business forks are closed by the product owner before anything is written for
  developers** (2–4 options each, a recommended default, dated decisions); **technical forks are
  recorded for the tech lead**, never asked of the owner. A feature with an open product fork is
  not spec-ready. Named on `6#must` / `6#backlog` markers after `feature-spec`; recommended by all
  three statuses at step 6.
- **`feature-to-spec` (outputs, authored).** Ported from a field skill (daisy-feature-2-spec) and
  genericized: authors the development instruction a team implements from — BRD/PRD by default,
  tech spec for engine-internal features — one `.md` per groomed feature in `export-files/`.
  Scope-faithful (every requirement traces to the groom), WHAT-not-HOW, no hard names (the
  codebase wins), Given/When/Then acceptance on every requirement, product decisions arrive fixed
  and only technical forks stay open. Meeting an open product fork while writing is a stop, not a
  workaround. `steps/6-sprint-plan/README.md` → *From feature to development instruction* pins the
  chain: `feature-spec` → `feature-grooming` → `outputs/feature-to-spec`.
- **Hardened from the first dry run** (the chain applied end-to-end on the decksmith example, the
  spec then read by a context-free "developer" agent — whose questions were the defect list). The
  goal the chain now enforces: **zero open product questions in the delivered instruction.** The
  groom's fork sweep walks a *dimension list* — surface · told-or-silent · media & content types ·
  cardinality · inputs the developer can't produce (owned, or readiness blocks) · check targets ·
  trigger boundaries (the line under every classification a behaviour keys on) — each marked asked
  or n/a, plus a per-scope-item "could two implementers build this differently?" pass for the
  assumed mechanism. The spec's checklist gains: every criterion has something to check it against
  (inputs owned, check targets concrete — never "current"), every normative clause of an FR is
  exercised by a criterion, no two fixed decisions collide on the same behaviour, no criterion
  presupposes what a requirement only permits, and a **developer pass** (re-read as the
  implementer, nothing but the file) runs clean before delivery.

### Console 0.6.0 — the Guide tab, English-only chrome, honest card heights

- **A Guide tab** explains the framework inside the console, so it can be handed to someone who
  never opened `process/`: the one-direction write cycle (human → agent → files → console), the
  seven-move operating loop, the rules the agent lives by, the nested cadences with this instance's
  six steps live, what lives where (the three homes and the folder tab by tab), a legend built from
  the console's own marks, and how to phrase work for the agent. Pure chrome — nothing new is read
  from the instance, and the tab renders identically inside an exported snapshot (diagrams are plain
  HTML on the house tokens, no assets).
- **The chrome is English, always.** The `ru` locale and the locale machinery are removed: the
  framework is an international, English-language project, and a translated chrome was a second copy
  of its vocabulary to keep in step. Instance *content* still appears exactly as written, in any
  language. (`tools/ui/README.md` → *Interface language*, `extending/interface.md` step 6.)
- **Cards are as tall as what they honestly carry.** The step-board card lost its fixed min-height:
  a section with no authored `<!-- card -->` face folds to its title and tags instead of standing as
  an empty box. The card's head split into two quiet lines — the title with its gate tick, then the
  sign-off state with the evidence strip stretched beside it — so a long title no longer shuffles
  the tags, and the strip has a full line to be legible on.
- **The artifact reader opens the whole file.** Reading a projection in per-section slices hid the
  through-line; now the Artifacts tab renders one artifact top to bottom, each section keeping its
  own tags, and the TOC lists the files with the open one's worklogs nested beneath — the drill goes
  file → workings (worklog = source of truth, artifact = projection), not file → slice. A section id
  in the hash or from a cross-link still lands: the page scrolls to it.
- **The Skills tab reads the current card schema.** It still expected the pre-wave-3 fields
  (`used_by_steps`, `reads_registers`, the `adapters` plane) and crashed on the model the reader now
  returns; it now shows `reads · writes · surfaces · steps` and the `library · operations · outputs`
  planes, matching the card canon.
- **A wide table gets the whole card.** The expanded card body capped everything at prose width, so
  an eight-column table scrolled sideways beside empty space; the cap now applies to prose only
  (the `.md` line-length rules), and a table earns its scrollbar only when it is genuinely wider
  than the card.
- **The sprint board shows items, not slabs.** The shared read layer parses the must-set's
  F-/A-/T- blocks (`sprint_items` — the template's own head-line + bold-label convention, labels
  carried verbatim), and step 6 draws one card per item, grouped by direction: description, scope,
  acceptance, values, stories, owner·estimate, register links as chips, the groom state when
  present. The backlog stays a ranked table; an instance the parser doesn't recognise falls back to
  the old two-section board. `export-files/` is now read alongside the legacy `deliverables/` for
  the overview's deliverables row.

### Canon wave 3 — the card: one entity, one schema, a thin router

- The gap: wave 2 gave the loop a router, but what it routed *to* was still five different things.
  A step README, a library method, an operations skill, an outputs skill and a product's own
  exchange skill each declared themselves their own way — five questionnaires for one role — and the
  router's table carried facts about cards (which surfaces move 5 owes) that belonged in the cards.
  An agent that met an unfamiliar skill had to infer its shape.
- **One entity.** Everything an agent acts on is now a **card**: `node_type: card` with
  `kind: step | method | operation | output | exchange`. The kind is a **field value, never a second
  schema**. The pinned schema is the new `process/reference/card-schema.md`.
- **The header is the pass plan.** Every card declares `prerequisites` · `reads` · `writes` ·
  `surfaces` — move 3's gaps, move 2's read perimeter, move 4's write perimeter, move 5's owed
  surfaces. The header gives **types and slots**; the pass resolves instances from the data
  (`section:*` is a slot, an `H-` id never appears in a header).
- **One atom grammar for all three perimeter fields** — `register:` · `source:` · `section:` ·
  `worklog` · `file:` · `state:` · `ticks` · `sign-off` · `change-log`. Prefixes are mandatory
  because `metrics` is both a register and a source slot. Without controlled *values*, a shared field
  name would have been unification in name only.
- **A thin router.** `goal-map.md` rows are now **(trigger, goal) → card**; the *Move-5 surfaces*
  column moved into the cards it described. The commonest row — *the gate has open items* — is
  spelled out to the end: its goal is one named section, and it resolves to a **pair**, the step card
  (gate, input map, surfaces) plus the section's method (prerequisites, read types, writes), with
  move 2's perimeter their **union**.
- **The law of ranks, as fields.** A `method` carries `steps` and no `surfaces` — it is reached from
  inside a pass, never routed to. Who *does* owe surfaces is resolved against `goal-map.md` itself,
  so the two cannot drift; an operations card that is a **move** rather than a pass (`projection`,
  `orchestration`) declares `surfaces: []`, and that empty list states its rank honestly.
- **The law of two homes.** `tool-skills/` holds cards that ship with the framework;
  `<instance>/skills/` holds cards written for one product, which a framework update never touches.
  The discriminator is **who authored it** — as objective as the delivery channel in `sources/`.
- **New checks X and Z** validate the schema and the home. X checks field *values* against the
  vocabularies, holds the per-kind exclusions, and warns on any key outside the schema so a private
  field cannot quietly become de-facto canon.
- **Breaking — field renames across all 62 cards.** `produces` + `writes_registers` → `writes`;
  `reads_registers` + `inputs` → `reads`; `used_by_steps` → `steps` (methods only). `ADAPTER.md` is
  renamed `SKILL.md`, the renderer/deliverable distinction becoming `output_kind: rendered |
  authored`. Dropped for having no consumer: `title`, `kind: method|template|research`, `mode`,
  `consumes`, `reads_ids`, `used_by_steps: [any]`. An instance with its own skills must migrate its
  headers; `process/reference/card-schema.md` carries the mapping table.
- Canon: 4,447 → 4,945 words. check W warns (guideline 4,600); the wave's acceptance is the entity
  invariant, not the word count.
- **Audit fixes after the wave.** `start-work` (the every-session entry point) no longer carries its
  own eight-step paraphrase of the loop — it had drifted to the pre-wave model ("recommend the tool
  from `per_step`", no card, no header-as-plan); it now defers to the skeleton and holds only the
  shape of a pass, and its bootstrap list starts with `AGENTS.md` itself (the non-negotiables were
  never in the list). `install/README.md` sent a product's own skills to `product-loops/tool-skills/`
  — the one place the law of two homes forbids; now `product-loops/skills/`. GLOSSARY gains the
  wave's three entities: **Card**, **Kind**, **Atom**. `.gitignore`'s unanchored `outputs/` also
  matched `tool-skills/outputs/`, silently keeping new output cards out of every commit — now
  root-anchored.
- **check W demoted from gate to guideline.** The hard 5,000-word ERROR is gone; W now only warns.
  The ceiling was never the author's requirement — it was introduced by an agent in `4334d32` and
  the author's explicit call is the opposite: *the word budget is a reference point, mechanics
  decide acceptance*. The gate also failed every fresh install on its own: vendoring appends the
  host-repo pointers to `AGENTS.md` (~75 words), pushing 4,945 past 5,000 — an install that fails
  its own linter out of the box.

### Canon wave 3.7 — the carriers the full-path test run found missing

Source: the end-to-end run (install → setup → first loop passes) driven on a weak local model
against an invented pmf product; findings F1–F8 in the run journal. One lesson, five carriers:
*what is in a copyable template gets reproduced; what is only described does not.*

- **Register skeletons** (`process/reference/register-skeletons/`): the register schema finally
  has a vendored, copyable carrier — one file per register (hypotheses · risks · metric-tree ·
  metrics.csv) holding the frontmatter and the keyed table header (exactly the keys check D and
  the console read), zero rows. `REGISTERS.md` and `product-setup` step 4 now say *copy, don't
  retype*. The full file layout stays a wave-4 subject; this ships only what tools already read.
- **Worklog skeleton** (`process/reference/worklog-skeleton.md`): the working document's shape —
  frontmatter, the projection line, the intake table, "The working" — as one copyable fenced
  block; `worklog-resolution.md` points to it at creation time.
- **The first-run door**: the install pointer now routes both ways ("first run → `product-setup`;
  every session after → `start-work`"), and `start-work` step 1 stops on `instances checked: none`
  and routes to onboarding instead of improvising one (live finding: the old pointer sent a first
  run into `start-work`).
- **Setup verifies before closing**: `product-setup` step 6 now ends Phase 1 by checking
  `config.yaml` against the pinned schema (all four required keys — a live setup silently dropped
  `product`) and running the linter, fixing errors before hand-over.
- **Check G2** — the drift no file-check could see: a gate item whose sections are all written but
  whose `state.yaml` tick is still `open` means move 5 (Record) was never finished and the cycle's
  recorded position fell behind the disk. WARN, not error (mid-pass this state is legal).
  Proven on the live instance: flags the unticked section and a gates block written in a shape the
  reader can't parse; clears when `state.yaml` is recorded canonically.
- **Check H2 hardened**: a file wearing an artifact's name whose frontmatter never says
  `node_type: artifact` is now an **error**, not a silent skip — the loader ignores such a file,
  so the steps view, the console and G2 were all blind to it while content checks still read it
  (live finding: a weak model wrote `1-concept.md` with no frontmatter and every structural check
  went quiet).
- Install requirements now name an observable capability probe from the run: a model that cannot
  copy a keyed table header out of a step template — even told to — cannot run this framework.

### Hardening from the local-model test run — prose is not a carrier for a weak model

A live install-and-setup run on a small local model (opencode · Qwen3.6-35B) drew the line exactly
where the rule classification predicted: everything that had a linter check was caught; everything
that lived only in prose — the version pin, the root pointers, the install order — failed silently,
and the artifact was bulk-filled with every gate ticked on setup day. Conclusions applied, all as
checks (per `extending/rules.md` — a machine-verifiable rule never becomes prose):

- **Check I2 — install acceptance.** Detected by layout, not by flag: an instance whose repo root
  contains the framework means a vendored copy, and then the install's machine-checkable debts fire —
  no `FRAMEWORK-VERSION` at the vendor root is an ERROR (no SHA in it a WARN), no root `AGENTS.md`
  an ERROR (no `start-work` pointer or no `loops-*` delegation approval a WARN). Silent in the
  framework's own dev repo, whose instances live *inside* it.
- **Check H tightened — value shapes, not just key presence.** All three from the live run:
  `language: русский` (a word, not a code) · `directions` as a comma string (reads as ONE stream) ·
  `active_status` naming no status file. Each is now an ERROR.
- **Check H2 — artifact frontmatter.** Missing `artifact`/`step` is an ERROR (gate ids are
  `<artifact>#<section>` — the file unhooks its own ticks); an invented key WARNs, with the canon
  home named for the two seen live (a `worklog:` list that was stale against its folder on day one;
  `active_status` in an artifact).
- **`start-work` orients with the linter first** (0.4.0). Session start is the one moment a human is
  guaranteed to see the debt a previous session left silently — the report is shown before anything
  else, findings become triggers, nothing is auto-fixed.
- **Proven on the defective run itself**: the same instance re-linted in a mock vendored layout went
  from 2 errors to 7 — five new catches, each a real defect; half-fixed installs produce the WARNs;
  a complete install is silent. The bulk-fill itself gets **no prose rule**: the run confirmed a
  weak model doesn't read prose, and the frontier-model requirement already stands in
  `install/README.md`.

### Canon wave 3.6 — one instruction per change, and a door that only routes

`EXTENDING.md` had grown into five jobs in one file: a router, three procedures written inline, the
rules that hold for any change, and two policy tests. A router is read every time; a procedure is read
once, when you are making that one change. Mixing them meant everyone paid for everything, and the
procedures that lived elsewhere drifted from the ones that did not.

- **A folder of instructions.** New `extending/` — one file per kind of change, each with the same
  five parts: *is this the right dial* · what it touches · the procedure · **a checklist** · what the
  change drags with it. `method` · `operation` · `output` · `status` · `section` · `step` ·
  `interface` · `config` · `rules` · `register`. None of it is in the always-loaded set, so an agent
  pays for it only when changing the framework — which the goal map already classes as *outside the
  loop*.
- **The door only routes.** `EXTENDING.md` keeps the dial table and the rules that hold for **any**
  change, and nothing else. The procedures for directions, sections and steps moved out; the two
  policy tests (*where a new rule goes*, *what earns a register*) moved to `extending/rules.md` and
  `extending/register.md`, with the one-line stubs staying in `CONVENTIONS.md` and `REGISTERS.md`.
- **A checklist never re-implements the linter.** Written into the door as a rule of its own: anything
  a machine can judge is a check in `tools/lint.py`, and a checklist holds only what a machine cannot.
  A hand-held copy of a machine rule is one more thing to drift.
- **Three circular or duplicated pointers cut.** `tool-skills/README.md` sent the reader to
  `EXTENDING.md` for the procedure while `EXTENDING.md` sent them back — same loop in
  `tools/ui/README.md`. And the four gates a method must clear were stated twice, in `EXTENDING.md`
  and in `library/README.md`, with the same two checks (U, V) named in both. One home now:
  `extending/method.md`. Every former home keeps the anatomy and a pointer.
- **One gap named instead of guessed, one decided.** A product's own **operation** has no door — the
  law of ranks says an operation is reached only through the goal map, and the goal map is vendored,
  so a product cannot add a row (`extending/operation.md` → *Open question*); an agent that hits it
  stops and asks. **Migrating a filled instance** through a shape change is decided the other way:
  no mechanism, on purpose — the linter's off-form report is the work list, the human orders the
  migration in chat, and each one is an ordinary re-projection. An off-form section is a visible,
  linted debt, not a blocker (`install/UPDATE.md` → *Migrating a filled instance*).
- **Install grew an acceptance checklist and an update procedure.** Six things that are each a real
  failure if missing — including the one non-obvious case: at install time `instances checked: none`
  is the *correct* answer, and after setup it is a failure wearing a success message. New
  `install/UPDATE.md` gives re-vendoring a carrier at last: what is overwritten, what survives, the
  four CHANGELOG items that can leave an instance off-form, and the local-card shadow that was correct
  at the old tag and may not be at the new one.

### Canon wave 3.5 — the rules that had no carrier

Six debts closed, all of the same shape: a rule stated in one file and worked from another.

- **The open item's kind: two became three.** `step-close` told the pass to label an open item with
  "one of the two kinds" while CONVENTIONS (wave 3.4's own addition) had made them three — and the
  card's own `template-fragment.md` already listed all three. An agent reads the card in the pass, not
  the rule file, so it would have shipped two labels out of three: exactly *a later step owns it*, the
  kind that otherwise reads as decided when it is merely inherited. The card now points at the canon
  instead of restating it.
- **The kind label reaches the form.** All six step templates left their `open` inbox as a bare
  `- …` — the rule lived in CONVENTIONS and nowhere the agent looks while filling the section. The
  placeholder now carries the three kinds, "keep exactly one". And the rule gained the qualifier it
  needed: where the inbox is a **table with an owner column** (`#blockers`), that column *is* the
  kind — a second label beside it would be the same fact spelled twice.
- **The refutation lens is reachable from the pass.** Wave 3.4 made the rejected alternative
  mandatory, but the route to one — the refutation lens — was named only in `library/README.md` (read
  when *authoring* a method) and in `orchestration`. The `Decided:` placeholder in all 15 method
  fragments now carries it: *weighed none? order a refutation*. An obligation with no route gets
  satisfied the cheapest way, which here means "forced" written where nothing forced it.
- **The decision line is keyed** (`<!--d:date-->` · `<!--d:by-->` · `<!--d:alts-->`, all three or
  none) and **check O4** reads it. This is what wave 3.4 said it could not do: the line was prose in
  the instance's language, so an English-keyed check would pass every translated artifact in silence.
  Keys move it into the same contract as a column key — label prose free and translatable, the key
  fixed. The parse rule is canon (CONVENTIONS → *The decision line*; detail in
  `reference/column-keys.md`): `·` separates fields, `d:alts` is last and runs to the end of the
  block, so the line is its section's last. O4 errors on a half-keyed line, a malformed date, an
  unfilled placeholder, and an empty or bare-*none* alternatives field; it warns where an English
  `**Decided:**` label carries no keys, and that warning is best-effort **by construction** — the
  keys are the contract, the label never was. Proven by injection: five defects, five catches, plus a
  Russian-labelled keyed line passing clean and an unkeyed Russian one staying invisible.
  **Unlike a column key, this key does live in a method's `template-fragment.md`** — the line is
  copied verbatim, not adapted by meaning, so its keys travel with it. The reference example's nine
  decision lines are migrated (values unchanged; one `**Ladder rule:**` paragraph moved above its
  line, which must be its section's last), each artifact carrying the change-log entry.
- **The fresh reader looks at it.** `loops-verify`'s checklist gains decision lines as its item 5:
  an empty field, a bare *none*, or the chosen option restated in other words is a finding. Until now
  nothing but the author's attention held the rule.
- **The human is asked what the choice beat.** New step 3 of `theses`: where a section carries a
  `Decided:` line, one plain question before the verdict — *what makes this better than the option it
  beat?* — with the three answers and their moves (sign · send back · do not sign and do not invent
  one on the spot). This is the only place a **bad** decision, as opposed to a badly written one, is
  caught by design: a check can see that the field is filled, never that what fills it is real. New
  anti-pattern: signing a choice without its alternative.
- Canon: 5,167 → 5,372 words. The growth is the decision-line contract, which is a contract two
  independent readers must agree on — the one thing CONVENTIONS is for.

### Canon wave 3.4 — the conclusion nobody argued against

- The gap, measured on the same two artifacts as wave 3.2: the traced run's sections were correct
  line by line, and every choice in them arrived **unopposed**. Two of the v0.9 reference's decision
  lines weigh a real alternative and say why it lost; the run's say *none recorded* with nothing after
  it. Nothing in the canon asked for more, and `verify` — the one fresh reader in the loop — was only
  ever briefed to check whether a section was *written* correctly.
- **The refutation lens of a `verify`** (`operations/orchestration`, new *The two lenses of a
  `verify`*). A `verify` brief names its lens, and there are two: **conformance** (tags, sourcing,
  gaps, consistency, gate coverage — *is this written correctly?*) and **refutation** (one quoted
  claim, and the strongest case that it is **false** — *is this true?*). Three brief fields change and
  nothing else: §3 quotes the claim, §4 stops at the two or three attacks that would change the
  decision, §6 asks for the return table (*claim · the case against it · what must be true for it to
  hold · what evidence would settle it · verdict*). **`holds` is a real answer and the brief says so** —
  an agent that reads its brief as *find something wrong* manufactures an objection, and a
  manufactured one costs more than none. The lens decides nothing and rewrites nothing: passport line
  6 stands, and a landed refutation reaches the artifact through the worklog like any other finding.
  Two new anti-patterns: reviewing where you needed refuting, and ordering a refutation you will not
  act on. `.claude/agents/loops-verify.md` carries the mode; the brief template carries the variant.
- **The rejected alternative is no longer optional** (`library/README.md`, new subsection). The
  `Decided:` line's third field is the only one an agent can satisfy by writing nothing — *alternatives
  considered: none* is legal prose and the commonest shape of a bad decision: the first idea, dated.
  The rule now: **name at least one alternative actually weighed and why it lost, or name what makes
  the choice forced** (a constraint with no second option, an upstream decision already signed). The
  empty field is a defect because a choice with no alternative and an alternative nobody looked for
  are indistinguishable there. Fifteen method fragments, the outputs `brief` fragment and the Step-4
  template carry the new placeholder.
- **The two are one obligation with two routes.** When a pass's own reasoning produced no alternative,
  the refutation lens is how it finds one — the fresh reader argues the other side, and what survives
  is what the line records. A pass that already weighed a real alternative owes no subagent.
- **Why no linter check.** The decision line is prose in the instance's documentation language (the
  shipped Russian example writes *Решено / кем / рассмотренные альтернативы*), so a check keyed on the
  English label would pass every translated artifact in silence — the failure the column-key rule
  exists to prevent. Recorded in `library/README.md` rather than left implicit: until the decision
  line carries a key, the rule is held by `verify` and by the human who signs the section. A keyed
  decision line is a data-unification candidate, not a wording fix.
- Canon: unchanged at 5,167 words — both mechanisms live in the skills that need them, nothing entered
  the always-loaded set.

### Canon wave 3.3 — the contradictions the two traced runs left standing

- **A source can be dispatched at setup again.** `source-intake` named the setup dispatch as its first
  scenario and then required *the target step's artifact* to exist so its `<!-- tool: X -->` markers
  could be read — while `product-setup` forbids creating a step artifact at all. Three rules closed a
  circle and the legal path was unreachable. The markers come from the **step template**, which is the
  schema and exists before any instance does.
- **One side seeds a register.** `product-setup` said "seed the registers from anything the materials
  state" and the step-1 method says "seed it as a hypothesis" — both sides seeding is how one `H-` id
  gets issued twice. Setup now creates the files and seeds only what a source states outright *and*
  no method owns; anything a method owns is that method's to seed, on its pass.
- **`concept-expansion`'s volume rule had two readings** — a row per *ranked* problem or a row per
  problem *carried forward* — and the first collided with its own anti-pattern *one mechanism, every
  pain*. It is the carried-forward set; a lower-ranked pain another mechanism removes as a side effect
  is noted under the table, never given a row.
- **A worklog carries a change log** — the node-type matrix always said so, and `CONVENTIONS` →
  *Change logs* listed every other node type but that one. A section is a projection and holds no
  history, so the method's history has nowhere else to live.
- **A stale handoff is now visible as stale.** Nothing in the loop forces a pass to update
  `HANDOFF.md`: no `surfaces` holds it and its trigger only fires if the previous agent reached it —
  so a note six passes behind is a normal state that reads as current. It now carries `reflects:`, the
  newest change-log entry it was written against, and the reader is told to compare it before trusting
  a word.
- Tooling: `--export <path>` given a target that does not exist and does not name an `.html` file now
  treats it as a folder to create, instead of writing an extensionless HTML file nothing opens.

### Canon wave 3.2 — the whole is a different reader

- The gap, found by comparing a traced run against the v0.9 reference concept: the two artifacts came
  out the same size, and the run's was the more honest of the two (provenance not blurred, rejects
  visible in the artifact, no pain dropped) — but every place the reference was *sharper* was a
  judgement spanning two sections, and the run had produced those judgements and left them in its
  worklogs. The cause was structural, not a matter of agent quality: the reference wrote all six
  sections in **one** pass, so its writer held six worklogs at once; the run wrote one section per
  pass, so `#problems` was closed while the moat was still unwritten and "which segment proves the
  moat" was a question no pass could ask. **Nobody was ever the reader of the whole.**
- **`step-close` — a pass whose perimeter is the step** (`tool-skills/operations/step-close/`, and a
  router row triggered by *the step's own sections are all worked*). It reads every section, every
  worklog and the registers in one sitting and asks the four questions a section pass cannot: what
  one section means next to another, which conclusion never left its worklog, what the whole is
  missing, and which section states no conclusion. *Nothing new* is a legal answer; skipping the
  reading is not.
- **It needed no new write permission.** A finding that belongs to a section reaches it by ordinary
  re-projection, and the *orchestrator's conclusions* block that `projection` step 0 already
  sanctions is the channel into that section's worklog. The only new thing in the canon is the
  moment. `card-schema.md` pins `worklog:*` in `writes` to that block alone — never permission to
  write another method's working.
- **A card headline is about the conclusion, not the prose.** `projection` step 3 said a section with
  no natural headline — "a table of rows" — stays unmarked, and the run read it literally: four
  table-shaped sections went unmarked, so most of the board showed title-and-status. The reference's
  `#problems` is also a table, but it states its judgement in a line beneath it and marks that. The
  criterion is now stated as such, the ban on writing a line *for the mark* stands, and a table whose
  judgement is only implied is a `step-close` finding — returned through the worklog.
- Also: `projection` said it was the writing move at "step 6"; it is move 4 (F-001 of the run's
  friction log, fixed without a rule change).

### Canon wave 3.1 — contradictions surfaced by the traced test run

A traced run on a fresh vendor (decksmith brief; TRACE per pass, FRICTION log, per-pass commits)
walked Step 1 end-to-end and hit three places where one canon rule contradicts another. All three
were resolved by the run's agent the same way the fix now spells out — the canon catches up with
what a disciplined pass already had to do.

- **Onboarding no longer scaffolds step artifacts** (F-002/F-003). `product-setup` used to say
  "pre-fill all six artifacts", while check P reads *every* `<!-- tool -->` marker in an artifact as
  a worklog obligation — so setup's own output failed the linter before the loop had run once. Now:
  setup creates config/state/sources/registers only, routes materials to steps via
  `sources/INDEX.md` (*Feeds steps*), and the step artifact is **born by the step's first pass and
  grows section-by-section** — the rule is written where the writing happens (`projection`,
  prerequisites), not in the loop.
- **`projection` no longer misattributes column keys** (F-006). It said keys are "the fragment's";
  keys live only on step templates (CONVENTIONS, check O) — a literal reading produced an un-keyed
  table and an O2 error. Now: structure and prose from the fragment, `c:` keys from the step template.
- **Gate items without a router row** (F-009). `goal-map.md` now says it: a gate item that is another
  pass's `surfaces` (`#to-clarify`, `#hypotheses`) or an optional section closes at move 5 of the
  passes that feed it or at step finalization — one pass per *section*, not per gate item.
- **A worklog can be a declared input** (F-008; the author's call, 2026-08-19). The absolute "a
  worklog is never an input" was agent-written canon, and the traced run hit its cost:
  `concept-expansion` requires the solution stub that `concept-formation` deliberately keeps in its
  worklog — under the ban a delegated draft could never receive that input at all. The law is now
  **declaration, not prohibition**: a card may read another method's worklog by declaring
  `worklog:<step>/<method>` in `reads` (grammar — card-schema.md; format and method existence —
  check X; an undeclared cross-step link stays a check-T error). Tags carry verbatim, sign-off stays
  on artifact sections, and only its own method ever writes a worklog. `concept-expansion` is the
  first declared reader. Injection proofs: bad format, unknown method, foreign worklog in `writes` —
  each an ERROR; the declared cross-step link — silent, the undeclared one — caught.
- **`questions.yaml` speaks atoms too** (the author's call, 2026-08-19). The file's `produces:` was
  the last pre-wave spelling of the write perimeter — a second word for what card headers call
  `writes`. All 48 files migrated to `writes: [section:…]` / `writes: [file:…]` (same atom grammar
  as the header); check A2 now reads the atoms and errors on the old spelling.
- **Artifact column vocabularies are machine-checked** (F-007; the author's call: template + linter).
  A truncated token (`already improvising`) passed the linter in the traced run and only a `verify`
  subagent caught it. Now a step template declares a closed vocabulary under the table
  (`<!-- enum:c:inaction: … | … -->`) and the new **check O3** holds every instance cell to it — the
  same template-is-the-schema contract check D holds for registers. First declarations: the four
  vocabulary columns of `1-concept#problems`. The check immediately caught **five real defects in
  the published reference example** (`examples/decksmith`): compound `M–H` grades and the very same
  truncated token — fixed there with a change-log entry, ranges rounded down (confidence is never
  upgraded in transit).
- **No more unreachable methods** (framework audit). `cjm-strategy` and `pricing-strategic-plan`
  were named by no step-template marker — by the law of ranks, no pass could legally arrive at
  them; the "contributing method" prose even had `pricing-strategic-plan` working *inside other
  methods' worklogs* (a write-rule violation in canon). Both are now the **second tool** of their
  receiving section's marker (`{#cjm}`, `{#pricing}`), each works in its own worklog, and the
  step-4 economics workings `pricing-strategic-plan` re-reads became declared worklog inputs. New
  **check U2** keeps it true: every library method must be named by at least one template marker.
  Check P's orphan warning now recognizes non-first marker tools as legitimate worklog owners.
- **The orchestrator's conclusions** (the author's idea, 2026-08-19). The traced run matched the
  v0.9 reference on correctness and lost on synthesis — every losing spot was a conclusion *between*
  sections (feasibility↔anxiety, a disqualifier, a repeatability→self-serve link) that only the
  holder of the whole context can draw, and no subagent can by construction. New **step 0 of
  `projection`**: before projecting, the orchestrator appends an *Orchestrator's conclusions* block
  to the worklog — cross-section links, tensions, card-line candidates — every line ⚙️ or
  `[assumption]` (never laundered into sourced fact); *"no conclusions"* is a legal answer, skipping
  the question is not. `orchestration` step 5 adds the cross-return half: what the accepted returns
  mean **together**. Whether a conclusion reaches the section is decided by the ordinary projection
  that follows — and the ⚙️ tag triggers the existing chat-preview + verify-before-tick guards.
  The acceptance demonstration (a conclusion drawn → projected → caught by verify) is the first item
  of the next traced run on a re-vendored instance.
- Canon: 4,945 → 5,013 words (the goal-map phrase + the declared-input law); W warns, mechanics
  decide acceptance.

### Canon wave 2 — the seven-move skeleton and the goal map

- The gap: the loop was an 8-step spine assumed to run in full for every trigger, but most triggers
  (a metric capture, a source landing, a handoff) exercise only part of it — so the canon carried a
  spine heavier than most passes need, and an agent had no cheap way to route a trigger to the right
  card.
- The rework: the loop is now a **seven-move skeleton** (0 Orient · 1 Name the goal · 2 Gather
  inputs & size · 3 Close gaps · 4 Act · 5 Record · 6 Bubble), and a new per-pass file
  `process/goal-map.md` is the **router** — a trigger → card table (passes) over the skeleton, with
  *moves* (ask a human, delegate, project, sign-off, verify) invoked **inside** moves 2–5, never
  routed to. Three ranks — passes · moves · outside-loop — replace the flat step list.
  This **supersedes the "loop 0–8 / step 3 / step 7" numbering** named in the wave-1 bullets below:
  old step 0 → move 0, old steps 1–2 → move 1, old step 3 → move 2, old steps 4–5 → move 3,
  old step 6 → move 4, old step 7 → move 5, old step 8 → move 6.
- **The three laws of interfaces.** A worklog is **private** to its own method — cross-step exchange
  is only through registers and signed artifact sections; no pass reads another step's worklog. Slots
  come from the card, instances from the data. Move 2 declares a **read perimeter** so a pass gathers
  only what its goal needs. New linter **check T** enforces the privacy law (a worklog that links
  another step's worklog is an error).
- **check W** now budgets the per-pass set as AGENTS + OVERVIEW + OPERATING-LOOP + **goal-map** +
  CONVENTIONS (router added; warn ceiling 4,500 → 4,600, error 5,000); the set lands at ~4,450 words
  with the router included.

### The boundary layer — one home for everything that crosses the edge

- `sources/` is now explicitly **only external data**, split into three subfolders by *delivery
  channel* (an objective test, never a judgement call): `originals/` (files the human brought),
  `snapshots/` (dated captures by the couriers — `source-intake` and pull skills), `access/` (one
  **passport** per external point). `INDEX.md` orchestrates. Full spec:
  `process/reference/boundary-layout.md`.
- A **passport** is written *only* as the human's recorded answers; no answers → the pass asks via
  `questions.yaml` and stops with an open item. A passport of bare `— to clarify —` is the exact
  defect this split makes impossible — the v0.9 bug where an agent invented an empty access stub.
- A product's own **exchange skills** (repeatable pulls/pushes) live at `<instance>/skills/<slug>/`
  with `cadence` in frontmatter and `last_run` in `state.yaml`; the framework is not a daemon — an
  overdue run is caught at session start, never by a background scan. Rules of exchange: a pull
  writes only to `snapshots/`, a push sends only `export-files/` with the human's confirmation,
  secrets live nowhere in the repo.
- `metrics-capture` (0.3.0) and `source-intake` (0.2.0) rewired onto the layout; the `decksmith`
  sample migrated (`sources/originals/founder-brief.md`, an analytics passport, a live
  `pull-analytics-weekly` skill). **Revert of d2e21dc**: the `metrics-capture` Output no longer
  authors the access file — the passport is **cited, never minted** by the pass. This is the
  correction that closes the invented-stub bug end to end.

### The per-pass canon halved — pay for contracts, not exposition

- The gap: the always-loaded set (AGENTS + OVERVIEW + OPERATING-LOOP + CONVENTIONS + REGISTERS) cost
  ~9,150 words per pass, much of it exposition duplicated from skills and reference — and a loaded
  context is exactly where an agent starts skipping loop steps.
- The cut, by the contract·method·check test (each deletion lands in the same change as its
  receiving home): **CONVENTIONS** is now a notation card — every marker, id, link and change-log
  form kept verbatim, the worklog-resolution exposition moved to the new
  `process/reference/worklog-resolution.md`; **OPERATING-LOOP** keeps the loop 0–8 and compresses
  *Delegation* to the contract kernel (write rule · never-delegated · closed task-kind list · hard
  return gate · the `delegation: off` / no-subagent-runtime fallback), with the task-kinds table
  moved to the `orchestration` skill that already owns the procedure; **OVERVIEW** stays in the
  per-pass order as the philosophy's one home (§1) plus the four planes, three homes and the loop
  model — the §5/§6/§9 duplicate tables are gone, each replaced by a pointer to its canonical home.
- **REGISTERS.md leaves the per-pass order** — it is canon read at named moments: loop **step 3**
  (pulling register rows as inputs, when field semantics are in doubt) and **step 7** (before
  writing rows). The loop carries explicit pointers at both steps; register *values* are still read
  every pass from the instance files.
- **AGENTS.md non-negotiables now carry ids N1–N10**, each an imperative plus the one-clause reason
  it exists; the reading order routes: per-pass (OVERVIEW → LOOP → CONVENTIONS), named-moment
  (REGISTERS, `reference/`).
- **Step 7 gains an exit self-check** ("do not leave step 7 until: ticks ⊕ registers ⊕ theses
  sign-off ⊕ change log ⊕ open items") — the step most often skipped by a loaded context.
- **New linter check W** holds the per-pass set to a word budget (soft/hard ceiling in
  `tools/lint.py`); EXTENDING's "~1000 lines" prose budget is superseded by the machine-held one.
- Net: per-pass set 9,152 → ~4,300 words (−53%), zero contract removed — every enum, marker, id
  shape, path form and hard rule survives verbatim in exactly one home.
- **Field-tested A/B before merge**: two cold agents, same brief (a real metrics-capture pass on
  `examples/decksmith` + a 7-question contract quiz), one on the old canon, one on this one. Both:
  identical correct file set, lint 0/0, 7/7 quiz; the new canon answered the `delegation: off`
  question *more* completely at 53% less always-loaded reading. Fixes from what the run surfaced:
  - `metrics-capture` 0.3.0: the access-file contradiction resolved (Output now says no *derivation*
    in `sources/` — the access file **is** created by the pass when missing); an unsolicited reading's
    worklog lands in the **current step's** folder (one rule, no judgement call); explicit: a reading
    stays `[assumption]` until one independent check passes — for readings this tightens `[sourced]`.
  - `REGISTERS.md` 0.9.1: registers live at the instance root (`registers/`), the `product-loops/`
    spelling scoped to what it is — the live working area; empty `observed_n` defined for plain counts.
  - `AGENTS.md` 0.8.1: a missing instance `HANDOFF.md` is declared benign (no handoff pending), not
    a defect.

### Questionnaires carry their volume rules

- The gap: a method's `volume_rule` lived in SKILL.md frontmatter while its interview quietly
  allowed less — `segmentation` even *opened* with "pick the cut" (a choice before any candidates
  existed), and `where-to-play-how-to-win` went straight into detailing one cascade. An agent that
  honestly follows the questionnaire would honestly break the method.
- The fix, across all 9 questionnaires whose rule wasn't already forced: the question that gathers
  the set now states the floor in its `ask` and carries `min:`; where the rule demands
  candidates-before-choice, the divergence question + a `single_select from:` choice now precede
  the detailing (`segmentation` candidate cuts → cut; `where-to-play-how-to-win` ≥3 cascade
  sketches → chosen cascade; `segment-cvp` opens with the ≥8-bundle slate). Prioritization pair:
  "every candidate current — none pre-cut; record the count N".
- The convention is written where `volume_rule` itself is defined (library/README): the
  questionnaire carries the rule; an interview that opens with "pick one" has already broken it.
- 7 questionnaires already complied (metric-tree, pre-mortem, capabilities-systems,
  concept-expansion, competitor-dynamics/-pricing, bets) — untouched.

### Console S-signals — the main axes readable at a distance

- **Dual ring per step** (overview cascade, step header, snapshot cover; the rail gets a second
  navy bar): outer ring = gate items closed (green, process), inner = sections a human confirmed
  (navy, semantics). The gap between the rings is the signal — a closed gate nobody signed, or
  signed work whose gate was never ticked.
- **Evidence heat strip** on every canvas card (and step-2 zone headers): the section's confidence
  mix as one thin bar in the colours the `.conf` chips already taught — sourced/validated vs
  assumption at a glance, counts on hover. Untagged section → no strip.
- **Freshness**: a sign-off older than 60 days turns its `confirmed` tag amber with the age; a
  metric KPI whose last reading is older than 90 days carries an age chip; a worklog whose
  `updated` is later than its artifact's gets a "workings newer" chip on the card, the section row
  and the reader — the projection may no longer say what the workings say.
- **Snapshot cover**: the exported file opens on a title screen — product, status, current step,
  the six steps as dual rings — so a stakeholder's first screen answers "where are we" before any
  navigation. Renders only inside a snapshot; the live console keeps its chrome.
- Pure render: no canon, no schema, no read-layer change; `instance.py` already carried every
  value. Selftest green.

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
