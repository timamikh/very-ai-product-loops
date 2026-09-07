---
node_type: tooling
title: The local console — a UI for a very-ai-product-loops instance
status: draft
version: 0.7.0
updated: 2026-08-21
---

# The local console

A local web view of one instance. Run it in the product folder; it reads the files and shows where the
cycle stands, what is still open, and what the numbers do — the same canon the agent works from, laid
out for a human instead of a text editor.

**It is a viewer, not an interface to the process.** The work happens where it always happened: the
human talks to an agent, the agent runs the operating loop and writes the files. The console renders
what the files now say. It has **no write path** — not a deferred one, an absent one.

**Double-click [`console.command`](console.command) (macOS, Linux) or [`console.bat`](console.bat)
(Windows).** It opens the browser and stops when the window closes. That is the whole instruction for
the reader this is built for: a product manager owes nobody a terminal, and the console is worth
nothing to them if reaching it costs a command they have to be taught.

The same thing, typed, when a terminal is where you already are:

```bash
python3 tools/ui/serve.py                    # discover the instance from the current folder
python3 tools/ui/serve.py path/to/product    # or point at one
python3 tools/ui/serve.py --port 7788 --no-open
python3 tools/ui/serve.py path/to/product --export    # write the shareable file and exit
```

Any folder can be added at runtime from the header field — type a path, and the console reads it. That
is the contract to hold onto: **an instance written to the canon renders with no configuration.**

**Save as HTML** in the header — or `--export` with no server at all — writes one self-contained file
for the product currently open. See *Sharing a snapshot* below.

Python 3 standard library only, no build step, no npm. The framework's promise is *clone it and it runs
on plain python3*; a product manager must not need a toolchain to see their own product.

## Why this exists

The framework is deliberately plain markdown, and that is the right home for the *content*. But a
folder of markdown answers "what does section X say" far better than it answers "where are we, what is
still open, and what moved since last week" — the questions a product manager actually asks. Those
answers already exist in the files (gate ticks, confidence tags, `— to clarify —`, dated change logs,
metric readings); the console renders them.

**It does not make the framework a tool.** The console is a lens over the instance and a way to hand a
well-formed task to an agent — never a replacement for the operating loop.

## What the console must never become

Two failure modes are worth naming, because both would quietly destroy the framework's value:

1. **A form that bypasses the method.** The framework's worst failure is filling an artifact section
   straight from the template shell instead of through its library method (see [`AGENTS.md`](../../AGENTS.md)
   → *Read the tool before filling*). A UI full of text areas is an invitation to exactly that. The
   defence is structural, not procedural: there is no write path to misuse.
2. **A second parser.** If the UI read markdown its own way, it would drift from
   [`tools/lint.py`](../lint.py) and reintroduce the wiring bugs the linter exists to catch. So both
   read through one shared layer, [`tools/loops/`](../loops/): the linter and the console cannot
   disagree about what the canon says.

## Architecture

```
   the human ──────────► any agent / any LLM ──── writes ────┐
      │  asks for work    Claude Code · Codex · Cursor ·     │
      │                   a local model · a chat window      ▼
      │                                    the instance folder (the single source of truth)
      │                                                      │  read only
      │                                                      ▼
      │                              tools/loops/    ── one read layer ──
      │                               text · yamlite · framework · instance
      │                                                      │
      │                              tools/ui/serve.py  ── JSON + SSE, 127.0.0.1 only
      │                                                      │
      └──────────── looks at ────────────────────────  tools/ui/app/  (one HTML page, no build)
```

The bus between the agent and the console is **the filesystem**, in one direction. That is what keeps
the framework tool-agnostic: no vendor API, no editor plugin, no agent memory, and nothing for the
console to be wrong about — anything that can read a folder and write markdown can be the agent.

### Adding a folder — what "reads by canon" actually requires

The console needs only what the canon already fixes: `config.yaml` for the human's decisions,
`state.yaml` for the cycle's position, files whose frontmatter says `node_type: artifact`, and
`registers/`. Three real deviations were found in live instances and are handled explicitly rather than
silently:

| Deviation seen in the wild | What the console does |
|---|---|
| `config.yaml` never names the product | falls back to the folder name and says so in *Checks* |
| non-canon key spellings (`metric_sources`, `product_scope`) | reads them via aliases, flags the drift |
| a **multi-product** instance: `product-loops/config.yaml` with `products:` + one folder per product | treats the parent as an umbrella, lists the sub-products, and lets each inherit language / status / directions / title from the parent |

The first two are the canon's own gap — `config.yaml`'s schema was never pinned the way the registers'
was. Pinning it (and linting it) is the proposal that follows from this work.

### Interface language

**The chrome is English, always** — the framework is an international, English-language project, and
the console speaks the framework's language like every other framework file. The *content* is never
translated: an instance written in another language appears exactly as written. There is no locale
machinery and no language switch on purpose — a translated chrome would be a second copy of the
framework's vocabulary to keep in step, and `config.yaml → language` describes the instance's
documents, not the console.

### Sharing a snapshot

**Save as HTML** produces one file for **the product currently open** — no other instance on the
machine appears in it. The file carries the same stylesheet, the same renderer and the model as it
was read at that moment, plus the linter's verdict. Opened by anyone, on any machine, offline, it
looks the same as the console did.

Three properties are the point, and each is a constraint on how it is built:

- **One renderer, not a second one.** The export is the app with its data baked in, not a report
  generator. There is no second layout to keep in step, so a snapshot cannot say something the
  console does not.
- **Nothing is loaded from the network.** No web font, no script, no image, no stylesheet — the type
  is the system grotesque, which renders everywhere and never arrives as a row of tofu boxes. That
  rule is why the canon's ⚙️ marker is drawn as a word in a badge rather than as an emoji.
- **It is frozen, and says so.** A black bar across the top names the product and the moment it was
  taken. The live reload, the folder picker and the file viewer are switched off, because a snapshot
  has no folder to follow.

**Two ways to ask for it, one builder.** In the console, the button in the header — that is the one
the product manager uses, and it needs no terminal. Otherwise one command that writes the file and
exits, with no port, no browser and nothing left running:

```bash
python3 tools/ui/serve.py path/to/product --export           # <instance>/export-files/<product>-<date>.html
python3 tools/ui/serve.py path/to/product --export ~/Desktop # into a folder, same name
python3 tools/ui/serve.py path/to/product --export share.html
```

With no target, `--export` writes into the instance's own `export-files/` — the canon home for what
leaves the framework (the mirror of `sources/`), the same folder the outputs skills write their
deliverables to. It creates the folder if needed and never touches any other file of the instance.

Both routes call the same function, so the two files are byte-identical apart from the timestamp. The
export cannot be built without the read layer that builds the model, which is why there is no way to
produce it with no Python at all: a browser on its own cannot read the instance folder, and teaching
it to would mean a second parser that could disagree with the linter.

It is a **copy of the reading, not a deliverable**. A deck or a document for a stakeholder is an
outputs skill's job ([`tool-skills/outputs/`](../../tool-skills/outputs/README.md)); this is the console
itself, handed to someone who does not have the folder. And it is still product material: it carries
whatever the artifacts carry, so it goes to people who may read them.

**What the file carries — and what it does not.** The embedded model is the snapshot shape, not the
live one: the instance is named by its folder name, never by its absolute path (which would name the
user's home directory); the **worklog bodies are left out** — a worklog is private to its method
(CONVENTIONS → *Step folders & worklogs*), and the artifact sections are the projections a reader is
meant to see, so the snapshot keeps each worklog's title and date (the *workings newer* flag still
reads) and the worklog view says the body is not carried; the linter's verdict ships as its structured
findings and their counts, not its raw output.

### Theme and visual language

The house standard is red_mad_robot: white paper, black ink, one pure red, a grey scale, and the deep
navy as the single second hue. The red is the only colour with energy — it marks what is active and
what is next, and appears nowhere decorative. Everything else is carried by type, rule and space.

Three deliberate exceptions, each earning its hue: **status** (open amber, error red — legible without
reading the label), **registers** (hypotheses navy · risks red · metrics green · features purple ·
surfaces ochre — `--feat` / `--surf` in `app.css` — so an id keeps one colour everywhere), and
**chart series**, which come from a validated categorical palette because one
red and a grey scale cannot separate three lines for a colourblind reader.

Pure `#FF0000` gives 4.0:1 on white — enough for marks, rules and large type, not for body text. So
one token paints and a darker one writes.

Light / dark / auto, toggled in the header and remembered per browser. `auto` follows the OS; the
explicit choices win in both directions (`data-theme` on the root element). Chart series colors are
validated separately for each mode.

### Three rules the layout holds to

The first version of this console was a wall of cards, each showing the first two lines of something.
The rules that replaced it:

1. **Never a cut sentence.** Prose is shown whole, inside something that opens and closes, or it is
   not shown at all. The first 84 characters of a definition tell the reader nothing and cost them a
   line of attention.
2. **A number, a label, or a link — one job per element.** The overview answers *where are we* in
   figures and rules; the detail lives one click away, in a table or an accordion.
3. **No glyph we cannot guarantee.** No web fonts, no emoji, no box-drawing — a snapshot is opened on
   machines we know nothing about.
4. **The text gets the width; the frame goes above it.** What is short and the same for every section
   — the gate, what the status asks — sits across the top, not in a column beside the reading. Half a
   page of prose next to half a page of checkboxes turns a six-column table into one word per line. A
   paragraph still stops at about ninety characters, because past that the eye loses the next line;
   tables, evidence and code take the whole window.

The one place with visual energy is the **step rail** under the header: the six steps, always visible,
each with how far its gate has actually closed. The numbering is not decoration — the steps are a real
sequence, and the rail is how you move between them (there is no separate "step" tab).

### The read model

[`tools/loops/instance.py`](../loops/instance.py) reads one instance into a single JSON structure:
config decisions, cycle state and gate ticks, artifacts split into sections (with confidence-tag
counts, `— to clarify —` lines, ⚙️ proposals, referenced register ids), the five registers, the
metric series from `metrics.csv`, the sources index, the handoff, the change-log timeline, and a
`health` list of every deviation from the canon it noticed.

Three things it **assembles** rather than reads, because storing them twice is how two homes for one
truth appear:

- **The trail of one item.** Every register row carries a `⟲ n` control that opens the change-log
  entries naming that id — across artifacts *and* registers, newest first. Nothing keeps a per-item
  journal; the trail exists because a register entry names the ids it moved (CONVENTIONS →
  *Change logs*). A row with `⟲ 0` is a real signal: that item moved without anyone writing why.
- **A metric's comparable variants.** A series is split by `basis` **and** `population` — how the
  value was computed and who was counted. Two readings that differ in either are two lines, never two
  points of one, and the delta on a KPI tile is computed inside one variant only.
- **The dependency graph.** [`tools/loops/graph.py`](../loops/graph.py) joins what the reader already
  holds — sections with their `rests-on` targets and the register ids they name, register rows with
  their `serves` / `surface` / `parent` cells, cards with their `reads` / `writes` atoms — into nodes and
  edges. Nothing is stored: the graph is a view, so the console cannot draw an edge the files do not
  carry, and a row nothing links to shows as exactly that. One edge kind is derived, and drawn dashed
  to say so: *implied* — the card the step README names for a section reads a sibling section
  (`segment-pains` reads `segments` and `jtbd`, so `segments → problems`). The templates carry almost
  no `rests-on` marker inside a step, so without it a step's internal dependencies — which the cards
  do declare — would not show; a pair a `rests-on` marker already states is drawn once, as stated. The
  drawing is inline SVG through the same helper as the charts (no library, nothing from the network),
  so the snapshot carries it.
- **The product, by surface.** The *Surfaces* tab draws the two product registers as a board: one
  column per `S-…` row in file order, carrying the feature cards whose `surface` cell names that
  `S-id` (a substring match, so `S-04 · S-05` lands on both). A card is coloured by the feature's
  `state`, and a feature a current `6#must` item advances wears an *in this sprint's must* tag —
  read off the sprint items, kept nowhere else. A feature naming no known surface lands in a dashed
  *no surface named* column, which is a real signal, not an error. Clicking a card opens that
  feature's row in the register table below — its trail and serves-links live there, so there is no
  second detail view to keep in step.

Two rules hold there:

- **Tolerant, never silent.** Real instances drift (an older one has no `state.yaml`; its artifacts
  predate the number prefix; its registers are written in another language). The reader shows the
  drift in `health` instead of crashing or hiding it.
- **Discovery by frontmatter, not filename.** An artifact is a file whose frontmatter says
  `node_type: artifact` — so renaming or re-numbering files never blinds the console.

### Skills

The *Skills* tab shows every skill the agent can reach — the vendored `library` · `operations` ·
`outputs`, plus the product's own local skills — with its card header (reads ·
writes · surfaces · prerequisites · steps), its files, and a `homeless` flag when a written section
has no home in any step
artifact (the linter's check B, surfaced before it fails).

Adding or changing a skill is the **agent's** job, asked for in words ("add a method that does X", "adapt
this one to how we work"): it writes the canon's three-file anatomy into `<instance>/tool-skills/<plane>/<name>/`,
where a product-local skill wins over a vendored one of the same name, and the console shows it on the next
read. The procedure is [`extending/method.md`](../../extending/method.md) and its neighbours; changing the
console itself is [`extending/interface.md`](../../extending/interface.md).

### Why there is no write path

A UI can only offer what it can validate. Everything a product manager would want to change here falls
into one of two classes:

- **carries a method** — an artifact section, a register item, a handoff, a new skill's body. Filling one
  needs its library method, a prerequisite check and a confidence judgement. A text area cannot do that,
  and offering one invites exactly the failure the framework exists to prevent.
- **carries a decision** — the active status, the work directions, a gate tick, a metric reading. These
  need no method, but they *do* need a dated change-log entry and a reason, which is a sentence the human
  says to the agent anyway. Adding a second door for them would mean two ways to change one thing.

So the answer for both is the same door: **say it to the agent.** The console gains a defence that cannot
be eroded by a later feature, and the framework keeps one mechanism per change.

## What it shows

| Where | What it answers |
|---|---|
| The step rail | Where the cycle stands, and how far each of the six gates has closed. Pinned to the top with the tabs, so step and tab stay reachable however far you scroll; click a step to open it |
| Overview | What this product is, in one thesis line and six figures; the six steps as a table; where the next pass goes; how the instance reads against the canon |
| Step | The gate and what the active status asks, across the top; below them, full width, the step's sections as **accordions** — each opens to the section's full text, its confidence mix, gaps, proposals and register ids |
| Artifacts | One artifact whole — every section in order with its confidence tags, gaps and proposals; the TOC lists the files, and under the open one its worklogs (the workings each section projects from) |
| Registers | Hypotheses / risks / metric nodes / features / surfaces as filterable tables, with non-canon values flagged, a per-item trail, and a link to every artifact section that names the id. The Surfaces tab opens with the board — the product by surface, one column per `S-…` row (see *The read model*) |
| Metrics | Latest readings as tiles, one chart per node with a dot on every reading, each node's full definition, the raw `metrics.csv` rows, and the nodes defined but never measured |
| Open questions | Every `— to clarify —`, every gate item still open or unrecorded, every hypothesis in flight — each with a link to the section it sits in |
| Graph | The instance as a dependency graph in a pannable, zoomable stage (drag · pinch or ctrl+wheel · fit) — *the product*: the six steps' sections and the register rows as columns, joined by `rests-on` markers, the dashed *implied* reads of each section's card, the register ids a section names, and the registers' own `serves` / `surface` / `parent` cells; *the method*: the template sections with their methods, the operations and outputs, and the six registers, joined by the cards' `reads` / `writes` atoms. Hover lights up a node's neighbours; a click pins it and opens a side panel with what the node contains — a section's confidence mix, worklog link and full projected text, a register row's cells, a card's header — and its links, each one click to the node or to its home. *Neighbours only* cuts the drawing to one or two hops. Every solid edge is a fact a file states; the one dashed kind is derived from the cards and labelled as such |
| Sources | The source index, every file in `sources/` with its role and whether the index knows it, the metric source slots, and the session handoff |
| Skills | Every skill the agent can reach as a searchable table (one line each — kind, steps, origin); a row opens its full wiring and quality declaration below |
| Change log | One timeline across all artifacts and registers — what moved and why, filterable by file |
| Checks | The linter's findings plus the reader's `health` list — findings that differ only by which file they name collapse into one line — and an explicit list of what neither checks |
| Guide | The framework explained in place: the one-direction write cycle, the seven-move operating loop, the rules the agent lives by, the nested cadences with this instance's six steps live, what lives where (three homes + the folder tab by tab), a legend of every mark the console uses, and how to phrase work for the agent |

Deltas compare like with like — a reading is only compared to the previous reading on the same `basis`
and `population`.

## Notes & limits

- `--host` defaults to loopback; the console reads nothing outside the instance folder and the
  framework root, and has no write path at all (`POST` answers 405 by design). The HTML export is not
  an exception: the server writes no file, it answers one `GET` with a page, and the browser saves it
  wherever the human's downloads go. `--export` does write a file — where the human named it, or by
  default into the instance's `export-files/` (the canon home for outbound files; nothing else in the
  instance is touched) — and the server is not running at all.
- The change stream is a 1.5s poll (stdlib, identical on every platform). `?live=0` disables it —
  useful for headless captures and smoke tests.
- `tools/loops/yamlite.py` reads the small YAML subset the framework uses. Anything richer is out of
  scope on purpose: if the canon ever needs it, that is a change to the canon first.
- All UI strings sit in one `STR` object in `app.js`, in English — the framework's language.
  Instance content is never translated; it appears in the language it was written in.
