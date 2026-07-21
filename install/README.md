---
node_type: install
title: Install — add very-ai-product-loops to your product repo
status: draft
version: 0.3.0
updated: 2026-07-21
---

# Install

Add the framework to a product's repository via an LLM (Claude Code / Claude Desktop), the same
way you'd add any agent framework — point the agent at this repo and ask.

Install and product setup are **two separate phases**: first the framework is installed, then —
when you're ready — the product is set up. Keeping them apart means you can add the framework now
and onboard the product later.

## 1. Install (one request)

> "Install the very-ai-product-loops framework from
> https://github.com/timamikh/very-ai-product-loops for this project."

The agent **vendors** the framework (read-only) into the repo, pinned to a version tag:
`steps/` · `statuses/` · `process/` · `tool-skills/` (library · operations · adapters) · the
`product-setup` and `start-work` skills. That's it — the framework is present and configured; **no
product is set up yet.**

As part of vendoring, the agent also:
- writes a **`FRAMEWORK-VERSION`** file at the vendor root recording the exact **tag _and_ commit
  SHA** it pinned — the tag is the human-readable version, the SHA the immutable anchor (tags can
  move or be deleted; a SHA can't). Updating the framework = re-vendor at a newer tag and rewrite
  this file. (The tag in git is the source of truth; `FRAMEWORK-VERSION` is its echo inside the
  vendored copy, written at install time — not a second number anyone hand-bumps.)
- adds a short **pointer to your repo's root `CLAUDE.md`** (creating it if absent): *"Product-strategy
  work in this repo runs through very-ai-product-loops — begin with the `start-work` skill; the rules
  live in the vendored `process/`."* This is what makes a plain "continue the strategy" land in the
  disciplined loop instead of an ad-hoc bulk-fill.

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
  `tool-skills/` (library · operations · adapters), `.claude/skills/`, and a `FRAMEWORK-VERSION`
  file (pinned tag + SHA). Update by bumping the tag and re-vendoring.
- **Your product (yours, edited over time):** `product/` — kept **separate from your code** so it
  never interferes with development.

## Requirements

- A git repository (your product's repo).
- An agent with file access. The skill entry-points (`product-setup`, `start-work`) are a **Claude
  Code** mechanism; on **Claude Desktop** (repo mounted) they don't auto-surface — ask the agent to
  read `process/` in order (`OVERVIEW → OPERATING-LOOP → CONVENTIONS → REGISTERS`) and then run the
  same loop manually.
- Optionally: connectors to your metrics/KB, so later steps can pull data automatically.

## Change log

### 2026-07-21 — versioning contract + host-repo CLAUDE.md pointer + Desktop caveat
- **From → To:** install now (1) writes a **`FRAMEWORK-VERSION`** file recording the pinned **tag +
  SHA** (legalizing what the first real install improvised); (2) adds a **pointer to the host repo's
  root `CLAUDE.md`** so a plain request enters the `start-work` loop instead of an ad-hoc bulk-fill;
  (3) states the **Claude Desktop** limitation (skills don't auto-surface — read `process/` in order
  manually). The tag-pin promise is now real: the framework carries git tags.
- **Why:** the docs promised tag-pinning with no tags in git, the entry-skills only fire when
  invoked, and Desktop had no working entry path — all three surfaced by the independent audit.
- **Trigger:** independent audit, 2026-07-21.

### 2026-07-20 — vendor the `start-work` skill
- **From → To:** added `start-work` to the vendored skills and to the "set up the product" section —
  the entry point for every working session after onboarding (self-bootstraps the rules + runs the loop).
- **Trigger:** post-first-run hardening, 2026-07-20.

### 2026-07-19 — split install from product setup
- **From → To:** the one-line ask "add framework **and run product setup**" → two separate phases:
  (1) install (vendor the framework only), (2) product setup as a later, separate ask.
- **Why:** installing the framework and onboarding a product are distinct; bundling them forced setup
  to run immediately. Matches the corrected `product-setup` flow.
- **Trigger:** onboarding-flow fix, 2026-07-19.
