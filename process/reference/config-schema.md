---
node_type: reference
title: Instance config (config.yaml) — the pinned schema
status: draft
version: 0.1.0
updated: 2026-08-15
---

# Instance config (`config.yaml`) — the pinned schema

*Read this when writing or validating an instance's **`config.yaml`** (setup, or adding a key). The
one-line pointer stays in* [`CONVENTIONS.md`](../CONVENTIONS.md) → *Instance config*; *the linter
enforces this table as check **H**.*

`config.yaml` is the **human's decisions** about the instance (the cycle's position lives in
`state.yaml` — see [`OPERATING-LOOP.md`](../OPERATING-LOOP.md)). Its keys are canon, spelled exactly
one way. A second spelling is a place two readers diverge, so the linter enforces this table.

| Key | Required | Shape | What it is |
|-----|----------|-------|------------|
| `product` | **yes** | text | the product's name as a human says it (never inferred from the folder) |
| `language` | **yes** | `ru` · `en` · … | the documentation language; tools also read it for their own UI |
| `active_status` | **yes** | a status name from `statuses/` | the stage the loops are parameterized by |
| `directions` | **yes** | list | execution streams for Steps 5–6 (default: `development` · `go-to-market` · `back-office`) |
| `delegation` | no | `allowed` · `off` | may the orchestrator spawn subagents this instance? Absent = `allowed` (the framework's normal mode). `off` = the orchestrator runs every pass itself and writes every worklog directly — for restricted environments, or when the human wants no fan-out. Set at setup (`product-setup`), changeable any time |
| `scope_note` | no | text (block scalar) | what is in and out of this instance's scope, in prose |
| `metric_source_slots` | no | map | names each metric source; the *how to reach it* (URL, owner, recovery) lives in its passport `sources/access/<slug>.md`, **never a secret value** |
| `sources` | no | list of paths | the origin documents this instance was built from |
| `products` | no | map of maps | **multi-product instance only**: one nested block per product (`<name>:` then indented `path` · `title` · `goal` · `users` · `active_status` lines — block form, never a `{ … }` flow map: the framework's YAML reader does not accept one), one sub-folder per product, each with its own artifacts, `state.yaml` and `registers/`; the sub-products inherit everything above from this file |

Rules:

- **Nothing else is load-bearing.** Extra keys are allowed but no tool may depend on them (the linter
  reports them so they don't quietly become de-facto schema).
- **No alias spellings.** `metric_sources`, `product_scope`, `lang`, `title` are *not* accepted forms —
  fix the key, don't add a reader.
- **Readers stay tolerant, the linter stays strict.** A reader that meets an off-canon key still
  shows the data *and* surfaces the drift. Tolerance is for the human's benefit, never permission.
