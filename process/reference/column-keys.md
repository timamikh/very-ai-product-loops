---
node_type: reference
title: Keys — columns, and the decision line's fields
status: draft
version: 0.3.0
updated: 2026-08-20
---

# Column keys

*Read this when authoring or editing a **step template**, a **register**, or a method fragment that
ends in a **decision line** — deciding whether something carries a key and where that key lives. The
one-line contracts stay in* [`CONVENTIONS.md`](../CONVENTIONS.md) → *Column keys* *and* → *The decision
line*; *the authoring detail is here.*

A table column is addressed by a **stable key**, never by its header text — the column-level twin of
a section `{#anchor}`, the same "mark, don't guess" rule one level down. The key rides in a hidden
comment in the header cell:

```markdown
| Layer <!--c:layer--> | Value <!--c:value--> | Confidence <!--c:conf--> |
```

The comment is invisible in every reader (rendered markdown, the console, `plain()`), so the header
prose stays whatever the instance's language makes it (`Уровень`, `Nivel`) while a tool still finds
the column. Keys are kebab-case, unique within their table, and stable across revisions **and
translations** — translate or reorder the header freely, keep the key. A table is **all-keyed or
none**: a half-keyed header is the very ambiguity the key removes, so the linter rejects it (check O).

**The three homes of a key — and the one place it must never be.** The **clean copy** (an instance's
artifact section) and the **interface** that renders it are the *same form*, one to one, and that form
is defined by the **step template**. So a column key has exactly three homes:

1. the **step template** (`steps/*/template.md`) — the form of record, where a section's keys are declared;
2. the **instance** section that carries that form — so the console can read it in any language;
3. the instance **registers** — on every column a tool reads: the `id`, the statement (`hypothesis`),
   the enum columns (`type` / `status` / `category` / `kind` / `instrumentation` / `confidence`) the
   console and the linter (check D) validate, and the metric descriptors the metrics view shows
   (`definition` / `unit`). There is **no header-name fallback** — a register the console reads must key
   these columns, and a language-alias list is exactly the maintenance trap the key removes. A purely
   descriptive column nothing reads by key (tags, source, notes) carries none — the same "no consumer,
   no key" rule that keeps a key out of a method template.

A key is **never** put in a method's template (`template-fragment.md`). That file is the *draft's*
shape — by default it matches the section's theses, but a method may work a wider table, more tables,
or more detail than the clean copy shows, and data may arrive from `sources/` or a method the product
altered. When it does, the **orchestrator adapts the draft's data into the clean copy's fixed form**,
matching columns **by meaning**, not by any machine key — so a key in a method template is consumed by
nothing and only creates a sync burden every new skill would have to carry. The linter therefore treats
a key in a method template as an **error** (check O), and enforces on the step templates the shape a key
needs to be trustworthy: a table is **all-keyed or none** (a half-keyed header is the very ambiguity the
key removes), keys are kebab-case and unique within their table. The projection contract — an instance
section carrying its template's keys — is check O2 (instance-conformance).

This exists because matching a column by header prose breaks the moment the instance is written in
another language or its columns are reordered — the failure the section `{#anchor}` already prevents
for whole sections.

## Decision-line field keys

The same "mark, don't guess" rule on a **line** instead of a table row. A `decision` method's canonical
line (CONVENTIONS → *The decision line*) carries `<!--d:date-->`, `<!--d:by-->` and `<!--d:alts-->`,
each **after its label and before its value** — exactly where a column key sits relative to its column.
The parse rule the linter uses, and the one an author must not break:

- the **block** is the decision line and its wrapped continuation, ending at the first blank line;
- `·` is the field separator, so `d:date` and `d:by` end at the next one and may not contain it;
  `d:alts`, being last, may list several alternatives separated by `·` — the block's end is its end;
- `d:alts` is **last** and runs to the end of the block, which is why the canonical line is the last
  thing in its section: a paragraph after it with no blank line between would be read as alternatives.

Three keys or none: a half-keyed line is the same ambiguity a half-keyed table is. Check **O4** holds
the shape and rejects an empty or bare-*none* alternatives field.

**Why this key lives where a column key may not.** A column key is banned from a method's
`template-fragment.md` because the draft's table is adapted into the clean copy **by meaning** — a key
there would sync with nothing. The decision line is the opposite case: the framework fixes its shape,
and the method copies it **verbatim** into the section. So the fragment is one of its homes, alongside
the step template that carries the line and the instance section that ends in it.

**The one thing the key cannot fix.** An instance that never carried the keys is invisible to check O4 —
a Russian artifact writing *Решено / кем / рассмотренные альтернативы* with no markers reads as "no
decision line here". The linter warns where it can (an English `**Decided:**` label with no keys), and
that warning is best-effort by construction: the keys are the contract, the prose is not.

## Column vocabularies (enums)

A keyed column whose values come from a **closed vocabulary** declares it in the step template,
right under the table — one comment per column:

```markdown
<!-- enum:c:inaction: nice-to-have | recurring irritation | already paying or improvising -->
```

The template is the schema: the same contract check D holds for register enums, check **O3** holds
for artifact columns — an instance cell under that key must be one of the tokens (a `— to clarify —`
gap is fine; a qualifier belongs in a note or the worklog, never compounded into the value). The
declaration binds to a key the section's table actually carries, and an empty vocabulary is an error
(check O). Declare a vocabulary only where the method genuinely fixes it — a free-text column takes
none, the same "no consumer, no key" restraint.

## Fixed machine-read literals (not keys, still contracts)

A few machine reads anchor to a **fixed English literal** instead of a key. These labels are part of
the form, like a key: **they carry verbatim in any documentation language** — the value after them is
written in the instance's language, the label itself is never translated (translating it silently
detaches the linter and the console from the data):

- the **`## Change log`** heading — the history cut every reader makes (check E2 excludes it, the
  console builds trails from it);
- the step-6 item field labels **`**Feature:**`**, **`**Expected impact:**`** (with its `check-by`
  keyword) and **`**Estimate:**`** — the item's pre-registration, read by check E3, the console's
  sprint-item view and `impact-readout`.
