---
node_type: install
title: Install — add very-ai-product-loops to your product repo
status: draft
version: 0.1.0
updated: 2026-07-16
---

# Install

Add the framework to a product's repository via an LLM (Claude Code / Claude Desktop), the same
way you'd add any agent framework — point the agent at this repo and ask.

## One-line ask

> "Add the very-ai-product-loops framework from https://github.com/timamikh/very-ai-product-loops
> to this repository and run product setup."

The agent will:
1. **Vendor** the framework (read-only) into the repo, pinned to a version tag:
   `steps/` · `library/` · `statuses/` · `process/` · `adapters/` · the `product-setup` skill.
2. **Run [`product-setup`](../.claude/skills/product-setup/SKILL.md)** — ask your documentation
   language, ask for all existing product materials, convert and file them under
   `product/sources/`, and distribute their content across the step artifacts (as ⚙️ drafts with
   sources; gaps marked `— to clarify —`).
3. Scaffold the `product/` working area and hand back a placement report + the first step to work on.

## What lands in your repo

- **Framework (vendored, read-only, versioned):** `steps/`, `library/`, `statuses/`, `process/`,
  `adapters/`, `.claude/skills/`. Update by bumping the tag.
- **Your product (yours, edited over time):** `product/` — kept **separate from your code** so it
  never interferes with development.

## Requirements

- A git repository (your product's repo).
- An agent with file access (Claude Code, or Claude Desktop with the repo mounted).
- Optionally: connectors to your metrics/KB, so later steps can pull data automatically.
