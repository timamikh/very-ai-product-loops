---
node_type: tooling
title: The local console — a UI for a very-ai-product-loops instance
status: draft
version: 0.5.0
updated: 2026-08-11
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

Taken from the instance: `config.yaml` → `language` (`ru` / `en`, English fallback). One `STR` object in
`app.js` per locale, and nothing else in the app knows a language exists. **Chrome is translated;
content is not** — a step's goal and a status's per-step goals are the framework's own English text, and
the product's own text appears in whatever language it was written in. There is no language switch in
the UI on purpose: the instance already declares its language, and a second control would be a second
source of truth.

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
python3 tools/ui/serve.py path/to/product --export           # ./<product>-<date>.html
python3 tools/ui/serve.py path/to/product --export ~/Desktop # into a folder, same name
python3 tools/ui/serve.py path/to/product --export share.html
```

Both routes call the same function, so the two files are byte-identical apart from the timestamp. The
export cannot be built without the read layer that builds the model, which is why there is no way to
produce it with no Python at all: a browser on its own cannot read the instance folder, and teaching
it to would mean a second parser that could disagree with the linter.

It is a **copy of the reading, not a deliverable**. A deck or a document for a stakeholder is an
outputs skill's job ([`tool-skills/outputs/`](../../tool-skills/outputs/README.md)); this is the console
itself, handed to someone who does not have the folder. And it is still product material: it carries
whatever the artifacts carry, so it goes to people who may read them.

### Theme and visual language

The house standard is red_mad_robot: white paper, black ink, one pure red, a grey scale, and the deep
navy as the single second hue. The red is the only colour with energy — it marks what is active and
what is next, and appears nowhere decorative. Everything else is carried by type, rule and space.

Three deliberate exceptions, each earning its hue: **status** (open amber, error red — legible without
reading the label), **registers** (hypotheses navy · risks red · metrics green, so an id keeps one
colour everywhere), and **chart series**, which come from a validated categorical palette because one
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
counts, `— to clarify —` lines, ⚙️ proposals, referenced register ids), the three registers, the
metric series from `metrics.csv`, the sources index, the handoff, the change-log timeline, and a
`health` list of every deviation from the canon it noticed.

Two things it **assembles** rather than reads, because storing them twice is how two homes for one
truth appear:

- **The trail of one item.** Every register row carries a `⟲ n` control that opens the change-log
  entries naming that id — across artifacts *and* registers, newest first. Nothing keeps a per-item
  journal; the trail exists because a register entry names the ids it moved (CONVENTIONS →
  *Change logs*). A row with `⟲ 0` is a real signal: that item moved without anyone writing why.
- **A metric's comparable variants.** A series is split by `basis` **and** `population` — how the
  value was computed and who was counted. Two readings that differ in either are two lines, never two
  points of one, and the delta on a KPI tile is computed inside one variant only.

Two rules hold there:

- **Tolerant, never silent.** Real instances drift (an older one has no `state.yaml`; its artifacts
  predate the number prefix; its registers are written in another language). The reader shows the
  drift in `health` instead of crashing or hiding it.
- **Discovery by frontmatter, not filename.** An artifact is a file whose frontmatter says
  `node_type: artifact` — so renaming or re-numbering files never blinds the console.

### Skills

The *Skills* tab shows every skill the agent can reach — the vendored `library` · `operations` ·
`outputs`, plus the product's own local skills — with its wiring (produces · steps · prerequisites ·
registers · inputs), its files, and a `homeless` flag when a declared section has no home in any step
artifact (the linter's check B, surfaced before it fails).

Adding or changing a skill is the **agent's** job, asked for in words ("add a method that does X", "adapt
this one to how we work"): it writes the canon's three-file anatomy into `<instance>/tool-skills/<plane>/<name>/`,
where a product-local skill wins over a vendored one of the same name, and the console shows it on the next
read. The procedure, and the same for every other adaptation dial, is [`EXTENDING.md`](../../EXTENDING.md).

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
| Artifacts | Section by section, with confidence tags, gaps and proposals highlighted |
| Registers | Hypotheses / risks / metric nodes as filterable tables, with non-canon values flagged, a per-item trail, and a link to every artifact section that names the id |
| Metrics | Latest readings as tiles, one chart per node with a dot on every reading, each node's full definition, the raw `metrics.csv` rows, and the nodes defined but never measured |
| Open questions | Every `— to clarify —`, every gate item still open or unrecorded, every hypothesis in flight — each with a link to the section it sits in |
| Sources | The source index, every file in `sources/` with its role and whether the index knows it, the metric source slots, and the session handoff |
| Skills | Every skill the agent can reach as a searchable table (one line each — kind, steps, origin); a row opens its full wiring and quality declaration below |
| Change log | One timeline across all artifacts and registers — what moved and why, filterable by file |
| Checks | The linter's findings plus the reader's `health` list — findings that differ only by which file they name collapse into one line — and an explicit list of what neither checks |

Deltas compare like with like — a reading is only compared to the previous reading on the same `basis`
and `population`.

## Notes & limits

- `--host` defaults to loopback; the console reads nothing outside the instance folder and the
  framework root, and has no write path at all (`POST` answers 405 by design). The HTML export is not
  an exception: the server writes no file, it answers one `GET` with a page, and the browser saves it
  wherever the human's downloads go. `--export` does write a file — where the human named it, never
  into the instance, and the server is not running at all.
- The change stream is a 1.5s poll (stdlib, identical on every platform). `?live=0` disables it —
  useful for headless captures and smoke tests.
- `tools/loops/yamlite.py` reads the small YAML subset the framework uses. Anything richer is out of
  scope on purpose: if the canon ever needs it, that is a change to the canon first.
- All UI strings sit in one `STR` object in `app.js` — a locale is a translation of that object,
  chosen from `config.yaml` → `language`. Instance content is never translated; it appears in the
  language it was written in.
