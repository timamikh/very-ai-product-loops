# Changelog

All notable changes to very-ai-product-loops are recorded here. The format follows
[Keep a Changelog](https://keepachangelog.com/), and the project uses
[Semantic Versioning](https://semver.org/): `MAJOR.MINOR.PATCH`.

- **PATCH** — fixes and wording; nothing breaks for existing users.
- **MINOR** — new capability, backward compatible.
- **MAJOR** — a breaking change; adopters must adjust their instance.

The version you pin to is the **git tag**; this file is its human-readable story.

## [Unreleased] — The console gets the house standard, and a page you can send

The console read the instance correctly and looked like rubble: a wall of cards, each carrying the
first two lines of something, most of them cut mid-sentence. The owner's verdict was that a reader
loses the thread on first glance — there are no accents and no theses, only text. And the reading
could not leave the machine it ran on.

- **Repainted to the house standard** — a bespoke set: white
  paper, black ink, one **pure red**, a grey scale, and the deep navy as the single second hue. The
  red is the only colour with energy; it marks what is active and what is next and appears nowhere
  decorative. `#FF0000` gives 4.0:1 on white, so one token paints and a darker one writes. Three
  exceptions keep their hue because they carry meaning: status (open amber · error red), the three
  registers (an id keeps one colour everywhere), and chart series — one red and a grey scale cannot
  separate three lines for a colourblind reader, so the plot keeps its validated categorical palette.
- **Three layout rules, written into the file that implements them.** *Never a cut sentence* — prose
  is shown whole, inside something that opens and closes, or not at all. *One job per element* — the
  overview answers "where are we" in figures and rules, and the detail lives one click away. *No glyph
  we cannot guarantee* — no web fonts, no emoji, no box drawing. The canon's ⚙️ marker is now drawn as
  a word in a badge, which also ends the tofu-box risk in a shared file.
- **The step rail replaces the step tab.** The six steps sit under the header on every tab, each
  showing how far its gate has actually closed. It is the one place with visual energy, and its
  numbering is not decoration: the steps are a real sequence.
- **Sections, tables and accordions instead of cards.** A step's sections are accordions that open to
  the section's **whole** text; the six steps, the gate, the open questions, the readings and the
  source index are tables. Everything that names a section now offers a link into it, and a register
  row links to every artifact section that mentions its id.
- **A new *Sources* tab** — the source index, every file in `sources/` with its role and whether the
  index knows about it, the metric source slots, and the session handoff.
- **Save as HTML** writes one self-contained file for the product currently open: the same renderer
  and stylesheet with the model baked in, plus the linter's verdict. It loads nothing from the
  network, opens offline on a machine that never heard of the framework, and says across the top that
  it is a frozen copy. It is the console handed to someone without the folder — **not** a deliverable;
  a deck or a document is still an adapter's job. Same read layer, same renderer: a snapshot cannot
  say something the console does not. The server still writes no file — one `GET`, and the browser
  saves it.
- **The reading gets the whole width.** On a step, the gate and what the status asks stood in a
  column beside the text: they are short and identical for every section, and they were taking half
  the page, leaving the artifact — sentences, tables, evidence — in a gutter where a six-column table
  came out one word per line and clipped. They now sit across the top, where a frame belongs, and the
  sections run the full width of the window. A paragraph still stops at ~92 characters, because past
  that the eye loses the start of the next line; tables and evidence take everything.
- **A confidence tag wraps.** `[sourced: …]` carries its rationale, and a rationale is a sentence;
  held on one line it ran off the page and was cut. It now wraps, and every line of it keeps the
  chip's padding and corners, so a wrapped tag still reads as one mark. Long paths and ids in a body
  break instead of pushing the line out of the panel.
- **A second pass on the reading experience**, five smaller fixes:
  - *Checks* no longer prints the same warning once per file. Findings that differ only by which file
    they name — six artifacts with no change log — collapse into one line that lists the files. The
    error/warn counts still count every finding.
  - *Skills* was the last wall of cards: ~30 near-identical tiles per plane. It is a searchable table
    now, one line each (kind · steps · origin); a row opens its full wiring below.
  - The rail and tabs **stay pinned to the top** on scroll, so step and tab are reachable however far
    down a long artifact you are — the title bar still scrolls away.
  - An empty section in *Open questions* — nothing to clarify, no gate open — is one quiet line, not
    a full table dressed up as content.
  - A section link (`1#concept`) carries a **tooltip with the human section name**, for a reader who
    does not decode the step-number shorthand.
- **The console opens by double-click** — `tools/ui/console.command` (macOS, Linux) and
  `console.bat` (Windows). The audience is the product manager, and for that reader a terminal is a
  wall: the console is worth nothing to them if reaching it costs a command they have to be taught.
  The launcher finds python, says so plainly if it is missing, and prints ASCII only — a box instead
  of a dash in a console window is the same failure this project refuses in the UI.
- **A dot on every reading.** The chart drew a line and hid the measurements inside it, so the reader
  had to hunt along the line for a tooltip to find out where a real number sat. Each reading is now a
  marked point, ringed in the panel's own colour so two series crossing stay two dots; the point
  under the cursor grows. Two more chart fixes came with it: the fill under the line is drawn only
  for a single series (two translucent fills make a third colour that belongs to neither), and the
  end-of-line label carries the value alone — with the basis appended it ran off the panel and was
  cut, which is the one thing the layout forbids. The basis is named once, in the legend.
- **The snapshot without a server**: `python3 tools/ui/serve.py path/to/product --export` writes the
  file and exits — no port, no browser, nothing left running; give it a folder or a filename, or let
  it name itself `<product>-<date>.html`. Both routes call the same builder, so the two files are
  identical apart from the timestamp. There is no route with no Python at all: the page is built from
  the model, the model is built by the read layer, and a browser cannot read the instance folder on
  its own — teaching it to would mean a second parser that could disagree with the linter.

Not a change to the canon: the console remains a read-only lens with no write path, and the export is
not an exception to that — `--export` writes where the human named it, never into the instance.

**Column keys — a table column carries a stable id, like a section does.** A reader used to find a
table column by matching its header text against an English word, so a Russian or Spanish instance —
header reading `Цена`, not `Price` — collapsed the whole column to a dash while the data sat right
there. Columns now carry a hidden `<!--c:price-->` key in the header cell, the column-level twin of a
section `{#anchor}`: the same "mark, don't guess" rule one level down, invisible in every reader, so
the header prose stays in the instance's own language while a tool still finds the column. Documented
in `process/CONVENTIONS.md` → *Column keys*; the step-2 template and the `competitor-analysis`
fragment carry the keys. New linter **check O** holds the schema honest: a keyed table is all-keyed
with unique keys, and a template and the fragment that fills a section declare the same keys for it —
one section, one schema. (First slice of the artifact-structure-as-contract rework; see
`DESIGN-console-rework.md`.)

**Worklogs — a section says where it was worked out, and the console drills into it.** An artifact
section is a projection: it shows the conclusion in a fixed shape, not the working that reached it.
That working now has a home. Each step artifact gets a sibling folder — `2-analysis/` beside
`2-analysis.md` — holding one worklog per method, named for the tool that produced it
(`2-analysis/market-sizing.md`), with `<!-- synthesis -->` sections sharing `synthesis.md`. One id
threads the chain: the section's `<!-- tool: X -->` marker **is** the skill folder **is** the worklog
filename, so the console derives the drill link from the marker already in the artifact — nothing is
authored per instance. The worklog is the **source of truth**; the artifact section is its projection.
Raw `sources/` files are dispatched **into** the step's worklogs and cited there, never linked from an
artifact directly — the artifact points at the worklog, the worklog points at the source (reachable in
the console only under *Sources*). A new skill `source-intake` (named here, landing next) does that
dispatch at setup and on new files. New linter **check P** holds it: presence-gated per step folder so
a not-yet-migrated step stays silent, then once the folder exists it enforces `node_type: worklog`,
flags an orphan or a missing worklog, and warns when an artifact still links `sources/` directly. In
the console, a board zone or a card footer now carries a *workings* link into the worklog it was worked
out in, with a back link to the artifact it projects into. The `decksmith` sample's Step 2 is fully
migrated as the first proof: four worklogs (`market-sizing`, `competitor-analysis`, `substitutes`,
`synthesis`), every `sources/` citation moved off the artifact and onto them. (Transition A of the
artifact-structure-as-contract rework; see `DESIGN-console-rework.md`.)

## [Unreleased] — Delegation, and a quality declaration on every method

### The first field test moved delegation into the loop itself

One live product ran a full pass on the delegation release, and its owner's review found the same
root under every complaint: **the mechanics were written next to the loop, not into it** — so a
faithful agent ran the eight steps solo and treated the *Delegation* section as reference reading.
Changes, all from that one review:

- **The split decision is step 3** ("size the pass, aloud"), where the volume first becomes
  observable — "wider than one context" was dropped as a trigger because it can only be checked
  after the context is spent. **The split work is step 6**: briefs, spawning, and scoring every
  return against its passport. **Step 7 writes only after returns are accepted.** The *Delegation*
  section remains as the contract the steps reference.
- **Two new obligations before anything lands on disk** (the test's sharpest lesson — one spoken
  answer became writes to nine files with no preview): a section resting mainly on the agent's own
  reasoning or the human's spoken answer is **shown in chat before it is written**, and the pass
  **declares its write perimeter** — the files it will touch — in the same message.
- **A gate tick on a reasoning-based section waits for a `verify` subagent** that did not write it
  (the human may waive). The author ticking their own gate was legal until now.
- **The subagent contract slimmed to the brief.** Subagents no longer read `AGENTS.md`: the brief's
  role block is their complete contract (the canon already said a read-only subagent does not need
  the whole canon — the brief template contradicted it). `AGENTS.md` now defines *orchestrator* and
  *subagent* at first use.
- **The runtime is checked, not assumed.** `start-work` verifies at step 0 that the `loops-*` agent
  types are visible and spawning is permitted, and says so if not; `product-setup` tells the human
  to restart once after install (definitions are read at session start); install writes the owner's
  **standing approval of delegation** into the host repo's root `AGENTS.md` — the field test ran
  solo partly because a session-level restriction forbade spawning and nothing surfaced that.
- Paid for by subtraction: `OVERVIEW.md` stopped restating the six steps' goals and tools (canonical
  in `steps/*/README.md`) and gained the sixth philosophy rule — *one writer, many readers*;
  `CONVENTIONS.md` rationale passages cut to one phrase each. The always-loaded set holds at
  **935 lines** against the 1000 ceiling despite ~30 new lines in the loop.
- `docs/2026-08-08-field-report-response.md` folded into this changelog and deleted — one home for
  the framework's history, and the reference repo stays lean.

### One pass, more than one agent

The framework filled the lead agent's context faster than it filled the artifacts, and a full context
is where an agent starts skipping loop steps — registers not updated, a gate ticked without being
read, a claim shipped without its tag. `process/OPERATING-LOOP.md` → **Delegation** (~45 lines of
canon) now lets one pass run across several agents, on terms that keep the golden rule intact.

- **Only the orchestrator writes.** Subagents read, search, fetch, reason — and **return text**. The
  rule is transitive: a subagent may spawn its own subagents, and none of them writes either. This is
  what removes the two failure modes delegation would otherwise add — two agents allocating `H-0xx`
  at the same time, and a gate ticked by an agent that never read the gate.
- **Never delegated**: a fork with the human (the agent prepares, the human decides — a subagent has
  neither the human nor the context to decide in their place), register ids and writes, gate ticks,
  and the **Step 1–4 reasoning chain**, which is one argument and loses the coherence it exists for
  when cut into parallel pieces.
- **Four task kinds, a closed list:** `gather` · `research` · `draft` · `verify`.
- **A brief is a scoped handoff** — the same mechanism as a session handoff, narrowed, because it is
  the same problem: give a fresh agent enough state without giving it your context.
- **The return gate is hard.** Unlike this framework's step gates, which are soft ticks for a human,
  a return that fails its **passport** is *not integrated*. One remediation with the defects named,
  then stop: the gap becomes `— to clarify —` for the human, because a third attempt is nearly always
  the brief's fault rather than the subagent's.
- **It costs more tokens, not fewer** — every subagent re-reads what it needs. What it buys is a
  context that stays clear enough to think in. The skill says so in a callout, so nobody adopts it
  expecting a saving.

One new operations skill: **`orchestration`** — how to cut the work, brief it, score the nine-line
passport, and integrate a return without laundering its confidence tags.

`.claude/agents/loops-{gather,research,draft,verify}.md` enforce the write rule **mechanically** on
Claude Code: no write tools at all, checked by the linter. The remaining hole — those definitions keep
the ability to spawn further agents, which is guarded by instruction only — is stated in the skill
rather than hidden.

**The ceiling on the always-loaded rule set moves 900 → 1000 lines**, recorded with its reason: the
orchestrator↔subagent protocol is the definition of a contract, and a fresh subagent must know it
*before* it reads anything else. The rest of delegation went to a skill, which is why the raise was
~50 lines and not ~200. Canon is now 934.

### Every method states what would make it wrong

A method that never says what would make its output wrong produces plausible output forever. All 31
library methods now carry a **quality declaration** — `evidence_standard` · `volume_rule` ·
`selection_rule` · `rejects_shown` — enforced by check **L**, and about twenty method bodies were
rewritten so the declarations describe the method instead of decorating it.

- **Volume floors, stated as numbers a reader can fail.** The characteristic failure of a generative
  method is not a bad candidate — it is four polite candidates, all survivors, with no selection
  having happened. `segment-cvp`: ≥3 distinct situations per priority segment and ≥8 bundles (the
  unit of generation is the *situation*, not the segment). `competitor-analysis`: ≥5 named players,
  at least one the team did not name first — which is how the entrant that actually takes the segment
  gets onto the page. `risk-mitigation`: ≥8 failure modes before triage, because the first three are
  always the ones already being discussed. Also `channels-expansion`, `segment-pains`, `segmentation`,
  `where-to-play-how-to-win`.
- **`segment-cvp` gets the scoring rubric it lacked** — 5 criteria × 1/3/5 = 5–25, top 3–5 staged.
  It lives there and not in `prioritization` because of one criterion RICE has no axis for: **speed
  to a signal**. RICE's Effort is build cost, near-constant across bundles that need a landing page
  and ad copy, so it discriminates nothing. The boundary is now written in **both** files —
  `segment-cvp` picks which bet is worth learning about first, `prioritization` decides whether it
  fits the period's capacity, and a staged bundle is never re-scored.
- **Reject tables** wherever `rejects_shown: required` — sources rejected, players excluded, risk
  dispositions, North Star candidates and the filter each failed, cutting bases rejected, values that
  failed the post-AI rebuild test. Rejects are the cheapest artifact here and the most re-derived.

New shared reference **`tool-skills/library/references/evidence-standards.md`** — the part of a
serious research process we did not have at all. A source is judged **per fact type** (a filing is
authoritative for its own revenue and worthless for a rival's share); a credibility pyramid with an
explicit **forbidden zone** (anything whose original cannot be reached is not a weak source, it is not
a source); five statement labels — *fact · estimate · forecast · statement · pledge* — orthogonal to
our confidence tags, because a vendor's shipping promise is honestly `[sourced: …]` and still a
pledge; provenance with `as_of` and **fail loud**; and the **headline check**: any number that will
reach a conclusion gets a second independent source *before* the synthesis, with >20% divergence
reported as `[CONFLICT]` and never quietly resolved.

Three new linter checks: **L** (the quality declaration), **M** (vendored operations skills — the one
plane nothing checked, now including index-vs-folder), **N** (a shipped subagent definition carries no
write-capable tool). Check **C** no longer mistakes the README's schema tables for index rows.

The declarations were drafted by three read-only subagents running the orchestration brief, and the
result was verified by two more against different lenses — the first live use of the mechanism on
itself. Their findings are in this release: an `evidence_standard` value that could be present and
still check nothing, a passport whose two copies had already drifted in its first version, two agent
definitions that dropped a section the other two required, and a `selection_rule` that had been
copied from a neighbouring method rather than derived from its own.

## [Unreleased] — The local console + one shared read layer

**Wave 1 of the field-report fixes — the tooling now tells the truth.** Three defects that made every
other check meaningless, shipped together. (The report raised eleven points; every verdict —
including the rejections and their reasons — is recorded across this section and the next, so a
rejected proposal does not come back in six months as a new one.)

- **The linter finds the instance.** It globbed `examples/*` and `instances/*`, so the canonical vendored
  layout — the instance in `product/` of the host repo — was never checked, and the run still printed
  `0 error(s)`. It now takes instance paths as arguments and, with none, discovers them **by marker**
  through the same finder the console uses, so the two can never disagree about what an instance is. Every
  run prints `instances checked: N — <paths>`: **zero now reads as a problem instead of as success.**
- **A register split across two tables is one register.** `table_column`/`table_rows` returned on the first
  matching table, so a register that grew a second table was validated in its top half and reported as
  undefined in its bottom half. They now span every table carrying the column, and a table split by a stray
  blank line is stitched back rather than truncated — with new check **J** reporting the split, since the
  file is a trap for the next hand that edits it. (Shipped with the discovery fix on purpose: alone, that
  fix would have produced a screen of false errors on its first honest run.)
- **The console stopped losing findings.** Its parser of the linter's output matched check letters `A-G`,
  so checks H and I — added a week earlier — were dropped on the floor. The pattern is open-ended now.
- The smoke test grew an instance created **outside** the repo, plus the multi-table and split-table cases:
  "works in the monorepo" now fails in CI instead of in someone's product. `REGISTERS.md` no longer calls
  check E a manual procedure — it names the command.

**Waves 2–4 — the eight remaining points of the field report, decided and shipped.** The whole set cost
**+13 lines** of always-loaded canon, paid for by deleting the copies it made stale (876 lines against a
900-line ceiling). Four of the eight turned out to be code or a method, exactly as the classification rule
predicted.

- **Outcome observability (censoring)** — the one place where following the framework faithfully produced
  a *wrong* answer. `metrics.csv` gains **`observed_n`**: how many of the population could already have
  shown the outcome. A cohort metric divides by the observed, never by the whole cohort — the un-observed
  yield a plausible false number that survives into every comparison, where two groups then differ by
  their age rather than their behaviour. **An empty `value` means the outcome was not observable yet**, not
  a zero. The observation window is declared in the node's own definition; the procedure (and the
  anti-pattern) went into [`retention-analysis`](tool-skills/library/retention-analysis/SKILL.md) 0.2.0,
  which insisted on reading *by cohort* and said nothing about who could be read at all.
- **`basis` stopped meaning three things.** It now says only **how** a value was computed; **who** was
  counted is a new `population` column, whose per-node default is a *field* in `metric-tree.md` rather
  than a sentence standing nearby; a slice is a node of its own. Rows compare across `basis` and do not
  compare across `population` — the console enforces exactly that, splitting a series by both and
  computing a delta only inside one variant. (A compound `pop:` prefix was rejected: the canon cannot ban
  compound values on one side and mint them on the other.) **Stated weakness, on record:** this is the one
  field-report point with no cheap machine check — a linter cannot tell that a `basis` value is really a
  population; the split rests on discipline.
- **A valve for enum cells.** `metric-tree.md` gains a `note` column, and `tags` is finally written into
  `REGISTERS.md` for hypotheses and risks — the escape hatch existed only in `CONVENTIONS.md`, so the
  schema file did not know about it. An enum cell holds the bare value; the qualifier goes in `note`, the
  theme in `tags`. Check **D** now covers `status` and `confidence` too (only `type` and `category` were
  checked), reading `[sourced: metrics W24]` for the value it carries.
- **One id, one row** — new check **K**. Three ids in one definition cell (`M-dau / M-wau / M-mau`) left
  three csv series pointing at nothing while the register looked complete. Check **E**'s message now names
  its likely cause instead of being formally correct and reading as a linter bug.
- **A hypothesis can be half-refuted.** A bet needing two verdicts is split at the first attempt to test
  it; the halves name the original and the original closes as **`superseded`** — a new status value,
  because closing it as `refuted` would record a falsehood: it was divided, not disproved.
- **`sources/` has three roles, not two**: access · **method** (`node_type: source-method`) · evidence.
  The rules that turn raw rows into register values — who is excluded, how keys fold to one person, which
  window — are living, and putting them inside dated evidence forks them into two authoritative versions
  at the next capture. This is what makes a reading *reproducible*.
- **The raw-data rule restated from its intent.** It assumed the instance folder is a safe place; under
  vendoring it is the opposite — the framework sits in a repo whose `origin` may be public. Raw captures
  are **never committed** and are deleted once their values land; where the origin is external, the
  working folder and the analysis code live *outside* the repository with only a reference inside.
- **Side-effect worth naming:** the console used to run the linter with no argument, so a product
  manager looking at one product was shown findings about every other instance on the machine — and
  would reasonably read them as their own. It now lints the instance it is showing. (Only possible
  because wave 1 gave the linter an argument to take.)
- **A negative result has a home** — without a fourth register (`registers/tests.md` fails the four-sign
  test; a null result about a metric definition is a refuted hypothesis in all but name). Instead: a
  *Checked, not confirmed* table in the Step 4 template, the rule that **a register change-log entry names
  the ids it moved**, and a console lens that assembles the trail of one item from those entries — a `⟲ n`
  control on every register row. Nothing stores a per-item journal; `⟲ 0` means that item moved without
  anyone writing why. The committed example gained the change logs it never had, written that way.

**The missing method the field report was really about** — [`metrics-capture`](tool-skills/operations/metrics-capture/SKILL.md),
a new **operations** skill. Every method in the library begins where the numbers already exist: the metric
tree wants "the register seeded with captured readings", retention wants "usage data with a per-user
timestamp", unit economics wants a measured churn rate. Nothing said how to *get* there. The rule existed —
`OPERATING-LOOP.md` has always said a data-gathering errand is a full pass of the loop — with no procedure
behind it, so each pass was improvised, and points 1, 2 and 9 above were all born in one such improvisation.

The pass it prescribes, in the order that matters: name the question before the source (or you measure what
is easy to query); read the node's existing definition and rows first — **a changed derivation mints a new
id**, because a silently redefined metric keeps a continuous chart over a discontinuous meaning; declare the
population and the identity rule in writing, as judgement calls the human confirms; decide what is
observable and compute `observed_n`; compute with the script living outside the repository where the origin
is external; **verify against something independent** before believing the number; then land it — rows in
`metrics.csv`, a living `source-method` file, a change-log entry naming the ids, and the raw capture
deleted. Operations rather than library because it fills no artifact section and belongs to no step: it is
triggered by an event (a value is missing, or has gone stale) and acts on the registers.

**Zero canon growth beyond one pointer.** The skill produces a file rather than a section, so it needs no
new contract; the always-loaded set moved 876 → 877 lines. What it needed instead was wiring, so it is not
the thirty-second file nobody opens: the three methods whose prerequisites demand readings
(`metric-tree`, `retention-analysis`, `unit-economics`) now name the skill that produces them, and
`OPERATING-LOOP.md` points at it from the errand rule itself.

**Two rules about the framework's own growth.** A field report from a live instance (a SaaS product,
six steps done, real database access) produced eleven proposals — and nine of them would
have added a field, a file or a paragraph to the files an agent reads on *every* pass. Each was justified;
together they would have thickened exactly the expensive layer. So the growth question is now answered
before the individual proposals are:

- **Where a new rule goes — contract · method · check** (`process/CONVENTIONS.md` 0.7.0 → 0.8.0). Three
  classes, tried in that order: a **check** in the linter costs nothing at read time and does not rely on
  the agent remembering; a **method** in a skill is read only when used; only a **contract** — field names,
  enum values, id shapes, `node_type` roles, link form — earns a place in `process/`. With it: a stated
  budget on the always-loaded set (about 850 lines today; an addition names what it displaces or why it is
  neither a check nor a method) and the duty to *subtract* — a rule stated in two canon files is two places
  to drift, which is how a removed link mechanism survived in the overview for a release and a half.
- **What earns a register — the four-sign test** (`process/REGISTERS.md` 0.4.1 → 0.5.0). A fourth register
  is a core change, so a candidate is tested: a stable id other artifacts cite · an enumerable lifecycle ·
  a life outlasting the step that bore it · state that flows both ways. All four, not three. Fail one and
  the home is a step artifact section, whose change log already carries the reasoning. Two guards: a
  register of *workings* fails by construction (registers hold state, artifacts hold reasoning), and there
  are no halves — an id plus a status inside an artifact *is* a register, hidden where nobody looks.
  **Segments** are recorded as the one open candidate that passes all four, deliberately not adopted, with
  the two triggers that would decide it.
- Paid for in the same change: `process/OVERVIEW.md` (0.5.2 → 0.5.3) stops restating the metric register's
  columns and rules — they live once in `REGISTERS.md`, so the schema change the field report asks for has
  one place to land instead of two. `EXTENDING.md` (0.1.0 → 0.2.0) routes both rules from the doorway where
  changes are actually made.

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
