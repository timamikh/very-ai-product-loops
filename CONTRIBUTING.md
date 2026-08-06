# Contributing

Thanks for looking at very-ai-product-loops. This is a young project and contributions —
new methods, fixes, sharper wording — are welcome.

## How the repo is organized

- **Fixed core** — `process/` · `steps/` · `statuses/` · the registers schema. This is
  jurisdiction-neutral and changes rarely. Region- or company-specific concretes belong in
  adapters, not here.
- **Pluggable `tool-skills/`** — `library/` (product methods, one per folder),
  `operations/` (runtime capabilities like handoff), `adapters/` (render the working area
  into deliverables). Most contributions land here.

Read `process/OVERVIEW.md` and `process/CONVENTIONS.md` first — they define the wiring rules
the linter enforces. If you are adapting the framework for **your own company** rather than
contributing upstream, most of it needs no fork at all: `EXTENDING.md` maps each dial to its
procedure, and a company's own methods live in its `product/tool-skills/`.

## Proposing a change

1. Branch off `main`.
2. Make your change. If you add or edit a tool, keep its `SKILL.md` frontmatter, its
   `template-fragment.md`, and `questions.yaml` in sync — the linter checks this.
3. Run the linter locally: `python3 tools/lint.py` — it must report **0 errors**.
4. Open a pull request (or, for small fixes, commit to `main`). CI runs the linter on every
   push and PR; a red check blocks the merge.

## What the linter checks

Wiring and enums only — not prose quality or whether your register *values* are correct.
`produces` must match a real template fragment or a file path; library index rows must match
folders; register enums (hypothesis type, risk category, metric kind/instrumentation) must be
single-valued; cross-artifact links must be relative paths, not `[[…]]`. See `tools/lint.py`
for the full list.

## A note on private data

Real product instances live under `instances/`, which is git-ignored and never published.
Keep company data out of the framework and the `examples/`.
