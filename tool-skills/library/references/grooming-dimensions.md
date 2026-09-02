---
node_type: library-reference
title: Grooming dimensions — the fork sweep behind feature-grooming
status: draft
version: 0.1.0
updated: 2026-09-02
---

# Grooming dimensions

Walked by `feature-grooming` at step 2, after the text sweep. The failure mode is a dimension nobody
thought to ask — so each is marked *asked* or *n/a* in the groom block; a silent skip is the defect.

| Dimension | The question it forces |
|---|---|
| **surface** | where the user meets it (which UI · API · none); any user-visible behaviour implies one |
| **told or silent** | for every ignored, blocked or overridden user action: notified, or silent |
| **media & content types** | images, files, fonts, embedded data — in or out of scope |
| **cardinality** | one or many, for every entity touched (themes, templates, formats, accounts) |
| **inputs the developer can't produce** | token sets, definitions, test sets, copy — each named, owned, with a due (one already in `sources/` is `source:kb`); unowned blocks readiness |
| **check targets** | what "works in X" means (which product, version/build) — the *target* is the PO's decision, the *verification method* the tech lead's |
| **trigger boundaries** | every behaviour keyed on a classification ("a styling request") needs its line drawn — what falls in, what out; every threshold its counting rule (what counts · measured when · retries in?). An undrawn line is redrawn by each implementer; a ruled number with an unruled count is still a fork |
| **out-of-scope encounters** | input will ask for what scope excludes ("insert our logo" when images are out) — what the user sees then (omitted, told, refused) is a product decision; "out of scope" alone doesn't make it |

**Closing pass**, once per scope item: *could two implementers build this differently in a way that
changes behaviour or cost?* A "yes" is a fork — usually the mechanism everyone assumed (record it,
owner: tech lead).
