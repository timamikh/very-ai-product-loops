---
node_type: extending
title: Add an output — a card that puts a file in a human's hands
status: draft
version: 0.1.0
updated: 2026-08-20
---

# Add an output

*Read this when the framework must hand a human a file it cannot produce today — a format, a
deliverable, a house style. The dial table is in* [`../EXTENDING.md`](../EXTENDING.md); *the anatomy is
in* [`../tool-skills/outputs/README.md`](../tool-skills/outputs/README.md) → *Anatomy*.

An **output** is the one plane that points **out**. It fills no artifact section and writes no register:
everything it produces lands in `product-loops/export-files/`.

## Is this the right dial

| What you actually want | The dial |
|---|---|
| a file for use outside the framework | **this file** |
| content the framework does not hold yet — the file would have nothing to render | [`method.md`](method.md) or [`section.md`](section.md) **first**. An output never authors what an artifact should hold |
| your company's branding on an existing deliverable | **this file**, but the card belongs in your private or plugin repo — see *The boundary* below |
| a document that leaves and comes **back** as evidence | **this file**, `output_kind: authored`, and the return trip is [`../tool-skills/operations/source-intake/SKILL.md`](../tool-skills/operations/source-intake/SKILL.md) — `interview` is the worked example |

## First decide which kind it is

Both kinds are `kind: output` cards in one `SKILL.md`; the `output_kind:` field is what tells them
apart. The choice is not cosmetic — it decides where the truth lives.

| `output_kind` | Mechanic | Source of truth | Consequence |
|---|---|---|---|
| **`rendered`** | reads the structured instance and renders a view; authors nothing | the instance | the file is regeneratable — change the artifact and re-run. Never edited in place |
| **`authored`** | authors a document from the instance's state | the document itself (`node_type: deliverable`) | it is signed and carries a dated change log; a renderer may re-format it without becoming its home |

**Ask: if someone edits the file, is that an edit or a mistake?** An edit means `authored`. A mistake
means `rendered`.

## Procedure

1. **Pick the `output_kind`** by the question above.
2. **Create the folder** — `tool-skills/outputs/<name>/` for a neutral base output; your own repo for a
   company format.
3. **Write `SKILL.md`** — what it renders or authors · what it reads · how · the output shape ·
   anti-patterns — plus the card header
   ([`../process/reference/card-schema.md`](../process/reference/card-schema.md)). `writes` and
   `surfaces` are `file:export-files/*`; `formats` lists what it can emit.
4. **Name exactly which instance ids it consumes** and the shape it emits. An output that reads
   "whatever it finds" is the one that quietly invents.
5. **Ship a `render.py` only if the format needs a library or an engine** (`.xlsx` → openpyxl, `.docx`
   → python-docx, PDF → a browser engine). It must read *any* instance and hold **no product data**.
   A format the agent can emit directly — CSV, markdown, the deck's HTML — needs no code.
6. **Add the router reach and the index rows** — the goal map already carries one row for the whole
   plane (*a document must leave the framework* → `tool-skills/outputs/`), so a new output needs **no
   new row**; add it to [`../tool-skills/outputs/README.md`](../tool-skills/outputs/README.md) and the
   at-a-glance table in [`../tool-skills/README.md`](../tool-skills/README.md).
7. **Run the linter to zero**, bump the versions, record it in [`../CHANGELOG.md`](../CHANGELOG.md).

## The last hop, and the boundary

**A renderer's output is the finished deliverable, not another intermediate form.** A deck is a file you
can open and present; a markdown outline of a deck is the failure this rule exists to name. The whole
job is the last hop: from what is structured for an *agent* to read — stable ids, typed links, register
codes — into what a *human* consumes.

**The boundary.** Base outputs are neutral: they assume nothing about a company's house style, templates
or internal forms. A company format — a branded deck, a steering-committee card, a hand-in to a
downstream dev framework — **specializes** a base one and lives outside this folder, in a private or
plugin repo. It may import a base renderer's structure and re-skin it. Keeping the base neutral is what
lets each company layer its own formats without forking.

## Checklist

- [ ] `output_kind` chosen by the edit-or-mistake question, not by which word sounded better.
- [ ] It authors no artifact content and writes no register.
- [ ] The instance ids it consumes are named; nothing is read "as found".
- [ ] Its result is a file a human can open and use, with no further step.
- [ ] Any `render.py` reads any instance and holds no product data.
- [ ] Nothing company-specific landed in the base folder.
- [ ] `python3 tools/lint.py <instance>` — 0 errors, and the `instances checked:` line names your
      instance.
- [ ] Framework files version-bumped, `CHANGELOG.md` entry written.
