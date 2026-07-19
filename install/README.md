---
node_type: install
title: Install — add very-ai-product-loops to your product repo
status: draft
version: 0.2.0
updated: 2026-07-19
---

# Install

Add the framework to a product's repository via an AI agent (Claude Code / Claude Desktop), the
same way you'd add any agent framework — point the agent at this repo and ask.

## One-line ask

> "Add the very-ai-product-loops framework from https://github.com/timamikh/very-ai-product-loops
> to this repository and run product setup."

The agent will:
1. **Vendor** the framework (read-only) into the repo, pinned to a version tag:
   `steps/` · `statuses/` · `process/` · `tool-skills/` (library · operations · adapters) · the `product-setup` skill.
2. **Run [`product-setup`](../.claude/skills/product-setup/SKILL.md)** — ask your documentation
   language, ask for all existing product materials, convert and file them under
   `product/sources/`, and distribute their content across the step artifacts (as ⚙️ drafts with
   sources; gaps marked `— to clarify —`).
3. Scaffold the `product/` working area and hand back a placement report + the first step to work on.

## What lands in your repo

- **Framework (vendored, read-only, versioned):** `steps/`, `statuses/`, `process/`,
  `tool-skills/` (library · operations · adapters), `.claude/skills/`. Update by bumping the tag.
- **Your product (yours, edited over time):** `product/` — kept **separate from your code** so it
  never interferes with development.

## Requirements

- A git repository (your product's repo). If you're starting from scratch, `git init` first.
- An agent with file access (Claude Code, or Claude Desktop with the repo mounted).
- Optionally: connectors to your metrics/KB, so later steps can pull data automatically.

---

## The user story, step by step

Actors (lifelines):

```
HUMAN │ AGENT │ GIT │ FRAMEWORK (vendored, read-only) │ product/ (your instance)
```

### The canonical install (all cases share this)

```
━━ 0 · Prepare the repo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
HUMAN → GIT       : make sure a git repo exists (git init if starting fresh)

━━ 1 · Ask ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
HUMAN → AGENT     : "Add the framework from <url> and run product setup."

━━ 2 · Vendor the framework ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
AGENT → FRAMEWORK : copy in `process/ steps/ statuses/ tool-skills/ .claude/skills/`,
                    pinned to a version tag, READ-ONLY (you update by bumping the tag)

━━ 3 · Product setup (the onboarding skill) ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
AGENT → HUMAN     : "Which language for the product docs?"  → product/config.yaml (language)
AGENT → HUMAN     : "Give me everything you already have — docs, decks, sheets, metrics,
                     PRDs, links. However messy. Nothing? That's fine too."
  loop [per material provided]:
     AGENT → product/ : convert to markdown/csv → product/sources/<name>.md
                        (one file per original, header w/ orig name+date; originals untouched)
  AGENT → product/  : write sources/INDEX.md — per source: what it is · in-scope · OUT-of-scope
                      · which steps it feeds · confidence/freshness
  AGENT → HUMAN     : present the proposed INDEX → HUMAN corrects scope boundaries → save
  AGENT → product/  : distribute source content across the 6 step artifacts as ⚙️ drafts,
                      every claim [sourced: …]; conflicts → [assumption] + surfaced;
                      no support → `— to clarify —`; seed registers (H-/R-/M-)
AGENT → HUMAN     : "Current status? (concept-viability / pmf / growth) Directions?"
                    → product/config.yaml (active_status, directions)

━━ 4 · Scaffold + hand back ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
AGENT → product/  : create the product/ working area from templates, pre-filled per step 3
AGENT → HUMAN     : placement report (what went where · conflicts · what's still open)
                    + the first step to work on

━━ 5 · Start working ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
HUMAN + AGENT     : begin the operating loop at the suggested step
```

The result is always the same shape:

```
your-repo/
  <your code, if any — untouched>
  process/  steps/  statuses/  tool-skills/  .claude/   ← framework (read-only, versioned)
  product/                                              ← your instance (yours to edit)
    config.yaml · sources/ (INDEX.md + converted copies) · the 6 artifacts · registers/
```

### The three starting points — what differs

Only step 0 and how much of step 3 runs change. The rest is identical.

**A · From scratch (greenfield — no repo, no materials yet).**
```
0  HUMAN → GIT   : git init in an empty folder
3  materials     : "nothing yet" → skip convert/INDEX/distribute
4  scaffold      : product/ created with EMPTY templates (every section `— to clarify —`)
5  start         : begin at Step 1 (Idea/Concept); the agent interviews you to fill it
```
You start with clean templates and build up through conversation. The registers are born empty and
fill as you descend.

**B · History outside git (a pile of docs/decks/sheets that were never versioned).**
```
0  HUMAN → GIT   : git init (the docs themselves stay wherever they are — you hand them over)
3  materials     : the HEAVY path — every doc gets converted → product/sources/,
                   INDEX.md records what applies and what does NOT (e.g. "only the SaaS
                   part of this deck; the infra section is a different product"),
                   content distributed → artifacts pre-filled as ⚙️ [sourced] drafts
4  scaffold      : product/ arrives PARTIALLY FILLED — much of Steps 1–2 already drafted
5  start         : the agent points you at the biggest gaps / conflicts first
```
This is the "make the pile useful" path: unstructured history becomes a versioned, scoped,
source-tagged working area. The out-of-scope column in INDEX.md is what stops a later agent from
silently re-importing the parts that don't apply.

**C · Into an existing code repo (a real product with a codebase).**
```
0  GIT           : the repo already exists — no init
2  vendor        : framework copied in at top level, ALONGSIDE src/ (read-only, pinned tag)
3  materials     : as in A or B, depending on what product docs exist
4  scaffold      : product/ created at top level, SEPARATE from src/ — never touches code
5  start         : optionally wire metrics/KB connectors so later steps pull data automatically
```
The rule that keeps this safe: **product docs live in `product/`, away from `src/`.** The framework
is read-only and versioned; your product area is the only thing you edit. Updating the framework is
a tag bump, not a merge into your code.

## Anti-patterns (install-time)

- **Framework in the code tree.** Product docs must sit in `product/`, not scattered into `src/`.
- **Editing the vendored framework.** It's read-only; to change a method, extend it per your
  company (see [`tool-skills/README.md`](../tool-skills/README.md)) or contribute upstream — don't
  fork it in place, or you can't take updates.
- **Skipping the sources INDEX.** Without `sources/INDEX.md`, later agents re-read everything every
  time and lose the scope boundaries you decided at setup.
- **Inventing to fill.** Empty is honest; `— to clarify —` beats a plausible guess.

## Change log

### 2026-07-19 — added the step-by-step user story
- **From → To:** added "The user story, step by step" — a canonical install sequence (actors +
  BOOT→VENDOR→SETUP→SCAFFOLD→START) plus the three starting points (from scratch · docs outside git ·
  existing code repo) and install-time anti-patterns.
- **Why:** a person evaluating the framework needs to see the install as concrete actions, not just
  a one-line ask. Linked from the root README quickstart.
- **Trigger:** user request, 2026-07-19.
