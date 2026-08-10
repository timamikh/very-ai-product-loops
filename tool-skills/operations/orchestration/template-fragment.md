---
node_type: template-fragment
title: Task brief & return — the two halves of one contract
status: draft
version: 0.2.0
updated: 2026-08-10
---

# Task brief & return

Two skeletons, one contract: what the orchestrator hands down, and what must come back. Fill them in
the **instance's documentation language** (`config.yaml` → `language`) — the subagent writes what the
human will read. Everything in `<angle brackets>` is replaced; nothing is deleted.

A brief is normally passed as the subagent's prompt. If it is long enough to be worth a file, the file
goes **outside the repository** — a brief carries product material and is never committed, same rule
as a raw capture ([`process/CONVENTIONS.md`](../../../process/CONVENTIONS.md) → *Raw data & access*).

---

## The brief

```markdown
# Task brief — <gather | research | draft | verify>: <the task in one line>

## 1 · Read first, in this order
1. <the method you must apply — e.g. `tool-skills/library/competitor-analysis/SKILL.md`>
2. <the instance context you need — e.g. `product/1-passport.md#segments`, `product/sources/INDEX.md`>
Read nothing else from the instance unless this brief names it: what is not here is not your scope.
You do **not** read the framework canon — §2 below is your complete contract, not a digest of one.

## 2 · Your role and its limits  ← copy this block verbatim into every brief
You are a **subagent**. You read, search, fetch and reason. You **return text**.
- **You never write, edit or create a file.** Not an artifact, not a register row, not a note.
  If you spawn subagents of your own, the rule holds for them too.
- **You never close a fork.** A decision the human owns comes back as 2–4 options with trade-offs
  and a ⚙️ recommendation — never as a choice already made.
- **You never invent.** A value you could not find is written `— to clarify —`. A plausible number
  in place of a missing one is the single worst thing you can return.
- **Every claim carries a confidence tag** — `[sourced: <where>]` · `[assumption]` ·
  `[validated: <evidence>]` · `[refuted: <why>]` — and your own proposals are marked ⚙️.
- **Fail loudly.** A source you could not open, a page behind a paywall, an export that was empty:
  say so by name in §"Could not do". Silence there reads as "done", and that is how a gap becomes
  a fabricated fact one hand later.
- **No secrets, no PII, no raw captures** in what you return — values and their origin, never
  credentials, customer identities, or a pasted export.

## 3 · The task
<one paragraph: what must be true when you are done. Name the question the work must answer, not
the activity to perform.>

## 4 · Scope and stop condition
- **In scope:** <…>
- **Out of scope:** <…>
- **Stop when:** <the concrete condition — "the five named competitors are covered", "each of the
  three claims has two independent sources", "the section is drafted for one direction only">
- **Budget:** <how much reading/searching is proportionate — so "not found" arrives before exhaustion>

## 5 · What you are given
- **Inputs:** <files, source access, the exact export, prior artifacts>
- **Known context:** <the two or three facts without which the task is ambiguous — not your context
  dump; if it takes more than a short list, the task is not separable>
- **Already known / do not re-derive:** <what exists, so the return does not repeat it>

## 6 · What to return
The **return** skeleton below, in that order, in <language>. No preamble, no summary of the brief.
<Plus any task-specific shape: a table with these columns · one row per competitor · the section
draft as it would appear in the artifact.>

## 7 · The return passport — your work is rejected if any line is No
1. Every claim carries a confidence tag and names its origin.
2. Every source listed was actually opened, with the date you read it.
3. Sources you could not reach are declared, not dropped.
4. Any number that will end up in a conclusion is cross-checked against a second independent
   source; a divergence over 20% is reported as a conflict, not silently resolved.
5. Nothing invented — every gap is `— to clarify —`.
6. No fork closed; decisions come back as options.
7. No secrets, no PII, no raw capture.
8. The scope above is covered, or the uncovered part is named.
9. The "Could not do" block is present and specific.
```

---

## The return

```markdown
# Return — <kind>: <the task in one line>

## Result
<the deliverable, in the shape §6 asked for. Every claim tagged. Your own proposals ⚙️.>

## Sources actually opened
| Source | What it gave | Read on | Class |
|--------|--------------|---------|-------|
| <url / file / export> | <the specific fact or number> | <YYYY-MM-DD> | <primary · database · expert · press · vendor> |

## Cross-checks
| Number | First source | Second, independent source | Divergence | Verdict |
|--------|--------------|----------------------------|-----------|---------|
| <the headline figure> | <…> | <…> | <%> | agrees · **CONFLICT — both reported, not resolved** |

*A return with no numeric claims — most `draft` and `verify` work — writes* `n/a — this return
carries no numbers` *here and scores passport line 4 `n/a`. The section is never omitted: every
return has the same six sections, because the orchestrator reads several of them side by side.*

## Open forks — NOT decided
| The decision | Option A | Option B | Option C | ⚙️ Recommended, and why |
|--------------|----------|----------|----------|--------------------------|

## Could not do
- <the source, and why it was unreachable — 404 · paywall · needs credentials · empty export>
- <the part of the scope not covered, and what would unblock it>
- <anything in the brief that could not be followed as written — this is the orchestrator's signal
  that the brief, not the work, is what failed>
- *Nothing to report* is an acceptable entry — write it explicitly, never leave the block empty.

## Passport self-check
1 ✓/✗ · 2 ✓/✗ · 3 ✓/✗ · 4 ✓/✗ · 5 ✓/✗ · 6 ✓/✗ · 7 ✓/✗ · 8 ✓/✗ · 9 ✓/✗
<one line per ✗: which line, and what is missing. A self-check is a claim; the orchestrator scores
the passport itself.>
```

---

## Worked example — a `gather` brief, cut to its bones

```markdown
# Task brief — gather: weekly active accounts for the last 8 weeks

## 1 · Read first, in this order
1. `tool-skills/operations/metrics-capture/SKILL.md` — the procedure for turning a source into rows
2. `product/sources/analytics-access.md` — how to reach the source
3. `product/registers/metric-tree.md` — the node this feeds, and how it is defined today

## 2 · Your role and its limits
<the block, verbatim>

## 3 · The task
Return the weekly count of active accounts for the last 8 complete weeks, on the population and the
window the existing method file defines — so that the reading is reproducible by someone who was not
there. If the method file's definition and the source disagree, report the disagreement; do not
choose.

## 4 · Scope and stop condition
- **In scope:** the eight complete weeks before <date>; the counting rule as written in the method file.
- **Out of scope:** interpreting the trend, updating any file, proposing a new definition.
- **Stop when:** eight rows exist, or the source has been shown not to support one of them.
- **Budget:** one pass over the source; if access fails twice, stop and report.

## 5 · What you are given
- **Inputs:** the analytics access file above; the metric node `M-wau` and its current derivation.
- **Known context:** internal accounts are excluded by the rule already written in the method file.
- **Already known:** rows before <date> are already in the register — do not re-report them.

## 6 · What to return
The return skeleton, with **Result** as a table: `date, metric_id, value, observed_n, note`. A week
that is not yet complete gets an empty `value` and `note: window not elapsed` — never a partial count
presented as a weekly one.

## 7 · The return passport
<the nine lines, verbatim>
```
