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
  The И5 demonstration (a conclusion drawn → projected → caught by verify) is the first item of the
  next traced run on a re-vendored instance.
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
