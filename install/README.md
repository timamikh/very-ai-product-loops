---
node_type: install
title: Install — add very-ai-product-loops to your product repo
status: draft
version: 0.5.0
updated: 2026-08-10
---

# Install

Add the framework to a product's repository via **any** agent that can read and write files — the
same way you'd add any agent framework: point the agent at this repo and ask. Claude Code is the
smoothest ride (it has the skill entry-points), not a requirement; see *Running on an agent other
than Claude Code* below.

Install and product setup are **two separate phases**: first the framework is installed, then —
when you're ready — the product is set up. Keeping them apart means you can add the framework now
and onboard the product later.

## 1. Install (one request)

> "Install the very-ai-product-loops framework from
> https://github.com/timamikh/very-ai-product-loops for this project."

The agent **vendors** the framework (read-only) into the repo, pinned to a version tag:
`steps/` · `statuses/` · `process/` · `tool-skills/` (library · operations · adapters) · `AGENTS.md`
(the rules) · `EXTENDING.md` · the `product-setup` and `start-work` skills. That's it — the framework is present and configured; **no
product is set up yet.**

As part of vendoring, the agent also:
- writes a **`FRAMEWORK-VERSION`** file at the vendor root recording the exact **tag _and_ commit
  SHA** it pinned — the tag is the human-readable version, the SHA the immutable anchor (tags can
  move or be deleted; a SHA can't). Updating the framework = re-vendor at a newer tag and rewrite
  this file. (The tag in git is the source of truth; `FRAMEWORK-VERSION` is its echo inside the
  vendored copy, written at install time — not a second number anyone hand-bumps.)
- adds a short **pointer to your repo's root `AGENTS.md`** (creating it if absent), and the same
  pointer to `CLAUDE.md` if that file already exists: *"Product-strategy work in this repo runs
  through very-ai-product-loops — begin with the `start-work` skill; the rules live in the vendored
  `AGENTS.md` and `process/`."* This is what makes a plain "continue the strategy" land in the
  disciplined loop instead of an ad-hoc bulk-fill. Two names, one home: the rules are never copied
  into either pointer.
- adds, next to that pointer in the root `AGENTS.md`, the owner's **standing approval of
  delegation**: *"The repo owner pre-approves spawning subagents for framework passes (the
  `loops-*` read-only types) — per the vendored `process/OPERATING-LOOP.md` → Delegation."* The
  operating loop runs on subagents; without this line, a session whose environment restricts agent
  spawning would silently fall back to working solo. (It lives in `AGENTS.md`, not `CLAUDE.md` —
  the pointer files carry nothing normative.)
- reminds the human at the end: **restart the session once** — agent definitions and skills
  vendored mid-session are picked up only at the next session start.

## 2. Set up the product (a separate phase)

When ready, ask the agent to set up the product. It runs the
[`product-setup`](../.claude/skills/product-setup/SKILL.md) skill: asks your documentation language
and for all existing materials / links / accesses, converts and files them under `product/sources/`,
distributes their content across the step artifacts (⚙️ drafts with sources; gaps `— to clarify —`),
then **proposes a status** for you to pick. It finishes by summarizing what's filled vs still open
and proposing where to start — which is the first turn of the working loop. See
[`product-setup`](../.claude/skills/product-setup/SKILL.md) for the full flow.

Every session after that, begin with the [`start-work`](../.claude/skills/start-work/SKILL.md)
skill — it self-bootstraps the rules and runs the operating loop one pass at a time.

## What lands in your repo

- **Framework (vendored, read-only, versioned):** `steps/`, `statuses/`, `process/`,
  `tool-skills/` (library · operations · adapters), `AGENTS.md`, `EXTENDING.md`, `.claude/skills/`,
  `tools/` (the linter and the local console), and a `FRAMEWORK-VERSION` file (pinned tag + SHA).
  Update by bumping the tag and re-vendoring — your own skills under `product/tool-skills/` survive
  it untouched.
- **Your product (yours, edited over time):** `product/` — kept **separate from your code** so it
  never interferes with development.

## Requirements

- A git repository (your product's repo).
- **An agent that can read and write files.** No vendor API, no plugin, no agent memory: the
  framework's whole interface is a folder of markdown. See the section below for what differs per tool.
- **A frontier-class model with a long context** — this is the one real constraint, and it is about
  capability, not vendor. The framework depends on the agent holding four rule files plus an artifact,
  working *one section per pass*, opening a method's `SKILL.md` before filling its section, and writing
  `— to clarify —` instead of a plausible guess. A weaker model bulk-fills the template and it *looks*
  like finished work; the linter will not catch that, because it checks wiring and enums, never whether
  a claim is true.
- `python3` for the tooling (standard library only) — needed for the linter and the local console, not
  for the process itself.
- Optionally: connectors to your metrics/KB, so later steps can pull data automatically.

## Running on an agent other than Claude Code

The method is vendor-neutral; only the *entry points* are Claude Code conveniences. Three differences,
and the workaround for each:

| What Claude Code does for you | Everywhere else |
|---|---|
| auto-loads the rules from `CLAUDE.md` | `AGENTS.md` is the same content under the cross-vendor name — Codex and Cursor auto-load it; elsewhere say *"read `AGENTS.md` first and follow its reading order"* |
| `/product-setup` and `/start-work` as slash-skills | they are plain markdown: *"read `.claude/skills/start-work/SKILL.md` and follow it"* — the file itself assumes nothing auto-loaded |
| runs `python3 tools/lint.py` on request | run it yourself in a terminal; CI runs it too |

Nothing else changes. If your agent can open a file, edit a file, and stay disciplined about the loop,
it can run this framework — and the local console reads the same folder regardless of who wrote it.
