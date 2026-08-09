---
node_type: tooling
title: The local console — a UI for a very-ai-product-loops instance
status: draft
version: 0.4.0
updated: 2026-08-08
---

# The local console

A local web view of one instance. Run it in the product folder; it reads the files and shows where the
cycle stands, what is still open, and what the numbers do — the same canon the agent works from, laid
out for a human instead of a text editor.

**It is a viewer, not an interface to the process.** The work happens where it always happened: the
human talks to an agent, the agent runs the operating loop and writes the files. The console renders
what the files now say. It has **no write path** — not a deferred one, an absent one.

```bash
python3 tools/ui/serve.py                    # discover the instance from the current folder
python3 tools/ui/serve.py path/to/product    # or point at one
python3 tools/ui/serve.py --port 7788 --no-open
```

Any folder can be added at runtime from the header field — type a path, and the console reads it. That
is the contract to hold onto: **an instance written to the canon renders with no configuration.**

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
| a **multi-product** instance: `product/config.yaml` with `products:` + one folder per product | treats the parent as an umbrella, lists the sub-products, and lets each inherit language / status / directions / title from the parent |

The first two are the canon's own gap — `config.yaml`'s schema was never pinned the way the registers'
was. Pinning it (and linting it) is the proposal that follows from this work.

### Interface language

Taken from the instance: `config.yaml` → `language` (`ru` / `en`, English fallback). One `STR` object in
`app.js` per locale, and nothing else in the app knows a language exists. **Chrome is translated;
content is not** — a step's goal and a status's per-step goals are the framework's own English text, and
the product's own text appears in whatever language it was written in. There is no language switch in
the UI on purpose: the instance already declares its language, and a second control would be a second
source of truth.

### Theme

Light / dark / auto, toggled in the header and remembered per browser. `auto` follows the OS; the
explicit choices win in both directions (`data-theme` on the root element). Chart series colors are
validated separately for each mode.

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
`adapters`, plus the product's own local skills — with its wiring (produces · steps · prerequisites ·
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

| Tab | What it answers |
|---|---|
| Overview | What this product is, where the cycle stands, which step the next pass belongs to, and how the instance reads against the canon |
| Step | One step as a **canvas**: a card per section carrying its actual lead line and first bullets, its tick, confidence mix, gaps, ⚙️ proposals and linked register items — plus what the active status asks here and the full gate |
| Artifacts | Section by section, with confidence tags, gaps and ⚙️ proposals highlighted |
| Registers | Hypotheses / risks / metric nodes as filterable tables, with non-canon values flagged |
| Metrics | Latest readings as tiles, one small-multiple chart per node with readings, the raw `metrics.csv` rows, and the nodes defined but never measured |
| Open questions | Every `— to clarify —`, every gate item still open or unrecorded, every hypothesis in flight |
| Change log | One timeline across all artifacts and registers — what moved and why |
| Checks | The linter's findings plus the reader's `health` list, and an explicit list of what neither checks |

Charts follow the house visual language for chrome, but their **series colors come from a validated
categorical palette** (checked for colorblind separation against both surfaces) rather than the house
hues, which fail that check as a set. Deltas compare like with like — a reading is only compared to the
previous reading on the same `basis`.

## Notes & limits

- `--host` defaults to loopback; the console reads nothing outside the instance folder and the
  framework root, and has no write path at all (`POST` answers 405 by design).
- The change stream is a 1.5s poll (stdlib, identical on every platform). `?live=0` disables it —
  useful for headless captures and smoke tests.
- `tools/loops/yamlite.py` reads the small YAML subset the framework uses. Anything richer is out of
  scope on purpose: if the canon ever needs it, that is a change to the canon first.
- All UI strings sit in one `STR` object in `app.js` — a locale is a translation of that object,
  chosen from `config.yaml` → `language`. Instance content is never translated; it appears in the
  language it was written in.
