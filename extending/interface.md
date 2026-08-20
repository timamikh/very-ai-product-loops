---
node_type: extending
title: Change the interface — the local console
status: draft
version: 0.1.0
updated: 2026-08-20
---

# Change the interface

*Read this when the console does not show something you need. The dial table is in*
[`../EXTENDING.md`](../EXTENDING.md); *the console's architecture and its full read model are in*
[`../tools/ui/README.md`](../tools/ui/README.md).

## First: it is almost never the dial

The console reads the instance **by canon** — an artifact is a file whose frontmatter says
`node_type: artifact`, a section is its `{#anchor}`, a column is its `<!--c:key-->`. So most of what
looks like a console change is not one:

| You changed | What the console does |
|---|---|
| added or reshaped a section | renders it generically on the next read — **no console edit**, no widget to author |
| added a keyed column | reads it by key, in any language |
| added a method, an operation, an output, a local skill | shows it in *Skills* with its card header, and flags it `homeless` if its written section has no home |
| renamed or renumbered a file | still finds it — discovery is by frontmatter, not filename |
| wrote the instance in another language | reads it; the chrome follows `config.yaml` → `language`, the content stays as written |

**If a change to a section made you want to edit the console, the section is missing a key.** Go back to
[`section.md`](section.md); that is the actual fix, and it fixes the linter at the same time.

What genuinely needs a console change is a **new kind of thing to look at**: a file class it does not
read, a view that does not exist, a derived reading it cannot assemble, or a deviation it meets in the
wild and handles badly.

## Two invariants, and they are not negotiable

- **There is no write path, and none is added.** Everything a product person would want to change here
  either **carries a method** (a section, a register item, a skill body — filling it needs the method, a
  prerequisite check and a confidence judgement) or **carries a decision** (the active status, the
  directions, a gate tick, a reading — each needing a dated change-log entry and a reason). Both go
  through the same door: **say it to the agent.** A text area cannot hold either, and offering one invites
  exactly the failure the framework exists to prevent. The defence is structural, not procedural — do not
  make it procedural.
- **One read layer, shared with the linter.** Both the console and [`../tools/lint.py`](../tools/lint.py)
  read through [`../tools/loops/`](../tools/loops/). A second parser in the UI would drift from the
  linter and reintroduce the wiring bugs the linter exists to catch. **New reading goes in the shared
  layer, never in `app.js`.**

## Procedure

1. **Prove it is not a key.** Name the thing you want shown and where it lives in the instance. If a
   `{#anchor}` or a `<!--c:key-->` would carry it, stop and go to [`section.md`](section.md).
2. **Add the reading to the shared layer** — [`../tools/loops/instance.py`](../tools/loops/instance.py).
   Read it once, into the single JSON structure; if the value can be **assembled** from what is already
   read, assemble it — storing it twice is how two homes for one truth appear.
3. **Handle drift tolerantly, never silently.** Real instances deviate: an older one has no `state.yaml`,
   its artifacts predate the number prefix, its registers are in another language. Show the deviation in
   `health` instead of crashing or hiding it — and if the deviation is the canon's own gap, say so and
   propose pinning the canon rather than adding an alias forever.
4. **Expose it in [`../tools/ui/serve.py`](../tools/ui/serve.py)** — JSON, `127.0.0.1` only, read-only.
5. **Render it in `tools/ui/app/`** — one HTML page, no build step.
6. **Add the chrome strings for every locale** — one `STR` object per locale in `app.js`, and nothing
   else in the app knows a language exists. **Chrome is translated; content is not.** No language switch
   in the UI: the instance already declares its language, and a second control would be a second source
   of truth.
7. **Check the snapshot.** *Save as HTML* must still produce one self-contained file for the product
   currently open — and no other instance's data.
8. **Run the linter to zero**, bump the versions, record it in [`../CHANGELOG.md`](../CHANGELOG.md).

## Checklist

- [ ] The thing shown cannot be carried by an anchor or a column key.
- [ ] Every new read lives in `tools/loops/`, and the app parses no markdown of its own.
- [ ] Nothing is stored twice that could be assembled.
- [ ] Every deviation the reader meets lands in `health` — nothing crashes, nothing is swallowed.
- [ ] No write path, no form, no text area, no second door for a decision.
- [ ] Chrome strings exist for every locale; no content was translated.
- [ ] The snapshot still holds exactly one product.
- [ ] `python3 tools/lint.py <instance>` — 0 errors, and the `instances checked:` line names your
      instance.
- [ ] Framework files version-bumped, `CHANGELOG.md` entry written.
