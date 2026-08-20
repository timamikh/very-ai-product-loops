---
node_type: reference
title: Worklog skeleton — the copyable shape of a working document
status: draft
version: 0.1.0
updated: 2026-08-20
---

# Worklog skeleton

*Copy the fenced block below **verbatim** when creating a worklog, then substitute the four
placeholders: `<tool>` (the method id from the section's `<!-- tool: -->` marker — it names this
file too: `<step-folder>/<tool>.md`), `<step-number>`, `<step-slug>#<section>`, `<date>`. How a
section finds its worklog — the folder, the stem, the first-tool-owns rule — is
[`worklog-resolution.md`](worklog-resolution.md); this file only makes the shape copyable
(the test-run lesson: what is in a copyable template gets reproduced, what is only described
does not).*

```markdown
---
node_type: worklog
tool: <tool>
step: <step-number>
title: "<tool> — the working"
updated: <date>
version: 0.1.0
---

# <tool> — the working

_Source of truth for `<step-slug>.md#<section>`; that section is the projection of this file._

## Inputs dispatched from sources {#intake}

_Each row is a fact the method works from; the analysis and conclusions are worked below and
projected into the artifact section — never here._

| From source | What it gives this method | Value / claim | Captured | Confidence |
|-------------|---------------------------|---------------|----------|------------|

## The working

```

Rules the skeleton encodes, so they survive the copy:

- **The frontmatter is check P's contract** — `node_type: worklog` and a `tool` that matches the
  file name; a worklog with another `node_type`, or named for something no section marker names,
  is an orphan.
- **The intake table holds facts, never conclusions.** Conclusions are worked under *The working*
  and projected into the artifact section by the method (`projection`); the worklog keeps the
  reasoning, the section keeps the result.
- **A `<!-- synthesis -->` section** uses the same skeleton with `tool: synthesis` in the shared
  `<step-folder>/synthesis.md`.
- The worklog is a **draft surface**: its tables carry no column keys — keys belong to the step
  template, the instance section and the registers (CONVENTIONS → Column keys), never here.
