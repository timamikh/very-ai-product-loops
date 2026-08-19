---
node_type: reference
title: Column keys — the authoring rule
status: draft
version: 0.2.0
updated: 2026-08-19
---

# Column keys

*Read this when authoring or editing a **step template** or a **register** — deciding whether a
table column carries a `<!--c:key-->` and where its key lives. The one-line contract stays in*
[`CONVENTIONS.md`](../CONVENTIONS.md) → *Column keys*; *the authoring detail is here.*

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
