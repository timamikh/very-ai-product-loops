---
node_type: reference
title: The boundary layer — sources, snapshots, access, and instance exchange skills
status: draft
version: 0.3.0
updated: 2026-09-02
---

# The boundary layer

Everything that crosses between the instance and the outside world. Read this when adding a source
subfolder, writing an instance's own exchange skill (a scraper, a scheduled pull, a report push), or
resolving where a piece of external data belongs. The one-line contract stays in
[`CONVENTIONS.md`](../CONVENTIONS.md) → *Raw data & access*; the full layout is here.

## The invariant

`sources/` is the boundary with the outside world: **what it gave us**. Not one line in it is born of
reasoning about the product — reasoning is a **worklog**, values are the **registers**, projections
are the **artifact**, files leaving the framework are **`export-files/`** (the mirror of `sources/`).
An agent that would write its own thinking into `sources/` has picked the wrong home.

## `sources/` — three subfolders, one index

```
<instance>/sources/
  INDEX.md      — every file across the subfolders: role, typed slot (`type`: kb · interview ·
                  research · metrics · git — the `reads:` slot it serves; lint S2), routing (orchestrator writes)
  originals/    — files the human brought, byte-for-byte as delivered
  snapshots/    — dated, immutable captures of the outside world
  access/       — one passport per external point: how to reach it
```

**Writer matrix — the discriminator is the delivery channel, and it is objective:**

| Subfolder | Who writes it | Trust | Lifecycle |
|-----------|---------------|-------|-----------|
| `originals/` | the human (`product-setup` *files* what the human brought — a format conversion for diffability is allowed, never a reinterpretation) | the human's content, not agent-derived | kept forever |
| `snapshots/` | the **couriers**: `source-intake` (a URL → a dated extract) and a **pull** exchange skill (an export) | checkable against origin by its date | datable evidence; may be deleted once its values are in the registers |
| `access/` | an agent as **scribe** of the human's answers (via the card's `questions.yaml`) | co-authored (human decides, agent records) | living; updated with a change log |
| `INDEX.md` | the orchestrator | navigation only | living |

A GA4 export the human downloaded by hand → `originals/`; the same export pulled by a script →
`snapshots/`. The test is *who performed the delivery*, never a judgement call.

**The INDEX header is typed, and copied verbatim** — every column carries its `<!--c:key-->` (the
console and check S2 read the keys, never the header words; `type` is the closed slot list):

```markdown
| File <!--c:file--> | Role <!--c:role--> | Type <!--c:type--> | What it contains <!--c:what--> | In scope <!--c:in-scope--> | Out of scope <!--c:out-of-scope--> | Feeds steps <!--c:feeds--> | Dispatched into <!--c:dispatched--> | Confidence / freshness <!--c:conf--> |
```

`Role` is `access` · `evidence`; `Type` is the `reads:` slot the source serves (`kb` · `interview` ·
`research` · `metrics` · `git`); `Dispatched into` is filled by `source-intake` as it routes the
source into step worklogs; `Out of scope` records boundary decisions so a later agent never
re-imports what was excluded.

## The passport (`access/<slug>.md`)

One file per external **point** — a source to read from **or** a destination to push to (a push
endpoint is not a source, which is why access lives here, not folded into a source file). It carries
only what the human supplies: what the point is, its URL/location, its owner, how to verify reach,
how to recover access. **A passport is written only as the human's recorded answers.** No access file,
no answers → the pass asks (`questions.yaml`) and, if unanswered, stops with an open item. A passport
of bare `— to clarify —` is the defect this whole split exists to make impossible — an agent
inventing a source. A source that *is* a human (a manual recount, a founder's figure) needs no
passport: the value arrives as a recorded answer.

## Instance exchange skills (`<instance>/skills/<slug>/`)

A product's repeatable exchange with the outside world — pull this metric from that GA4, push that
weekly report — is an **instance skill**: the same `SKILL.md` form as a vendored one, plus its
scripts alongside. It is a *card* (the goal map routes to it); the skeleton runs it like any pass.

```
<instance>/skills/pull-ga4-weekly/
  SKILL.md      — frontmatter: cadence, direction; body: preconditions, run, verify, on-failure, landing
  <scripts>     — a runnable script, or prose steps for the agent — the two are equal
```

- **Slug:** `<pull|push>-<endpoint>-<what>` — the verb makes the direction visible in the folder name.
- **`cadence:`** in frontmatter (prose, e.g. `"weekly, Mon"`); `last_run` lives in the instance's
  `state.yaml`. The framework is **not a daemon** — an overdue cadence is discovered at session start
  (`start-work`), never by scanning.
- A script and a prose instruction to the agent ("walk the pages, copy the prices, embed them") are
  **equal kinds** of run recipe; `SKILL.md` is read before either runs (N4).

## The rules of exchange (inherited, not new)

1. **A pull writes only to `sources/snapshots/`.** It never lands values in a register itself —
   landing is a cycle pass (`metrics-capture` / `source-intake`), with the verification of move 4 and
   the record of move 5. A cron that runs the script out of session leaves an un-landed snapshot; the
   next session's move 0 sees it as an open item.
2. **A push sends only the contents of `export-files/`** — projections and authored deliverables,
   never a worklog or a draft — and **always with the human's confirmation** (a push is publishing;
   `cadence` on a push is a *reminder*, not an auto-send). The N8 secrets/PII filter runs before send.
3. **Exchange skills are run by the orchestrator** — like every operations pass, they are not
   delegated.
4. **Idempotence.** Snapshots are dated; landing reconciles against existing rows by `id + period`, so
   a re-run makes no duplicate. A changed derivation still mints a new `M-` id — the recipe obeys that
   rule, it does not bypass it.

## Secrets and PII at the boundary

N8 holds throughout. **Raw source captures are never committed**: a raw export, a transcript, a
scraped page under `sources/` is evidence for the pass that lands its values — once they are in the
registers (or dispatched into a worklog), the capture is deleted; what must stay for provenance is
the dated, aggregated snapshot, never the raw rows. `sources/snapshots/` is gitignored by default (the framework ships the rule; check T2 holds it in a vendored repo); an aggregate that must travel with the repo is un-ignored deliberately (`!sources/snapshots/<file>`), never by removing the rule. The linter's secret scan is the check behind the
rule. Per subfolder:

- **`originals/`** — the human's responsibility (they brought it); if it carries product-user PII and
  the `origin` may be public, it lives outside the repo like any raw capture.
- **`snapshots/`** — aggregates and working metadata (a board snapshot, git stats) are fine; an export
  carrying **product users' personal data** is a raw capture: outside the repo, deleted once landed.
- **`access/`** — a point owner's working contact is fine (owners already appear in register `owner`
  fields); a **secret is never written** — only where it lives and how to rotate.

## Sub-products

A sub-product shares its parent's `sources/` (as it does today) and, the same way, its parent's
`skills/`: one product's exchange skills and boundary data serve its sub-products unless a sub-product
overrides with its own. The console and linter resolve both by the same parent-inheritance path.
