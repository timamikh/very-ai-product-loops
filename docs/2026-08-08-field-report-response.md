# Response to the 2026-08 field report

**What this is.** A dated reply to a field report written by an agent that ran a real product on this
framework (a SaaS instance, Steps 1–6 done, second pass at Step 6, with live database access). The
report listed eleven defects, each one a failure it actually hit. This file records what we decided
about each, **including what we rejected and why** — a rejection with no written reason comes back in
six months as the same proposal.

It is **not a canon file**: no agent reads it before work, it carries no `node_type`, and it is not
counted against the always-loaded budget. Shipped decisions appear in [`CHANGELOG.md`](../CHANGELOG.md);
this file is where the reasoning lives. The report itself is not in this repo — it contains the
product's real numbers, and instance data stays out of the framework.

**How each verdict was reached.** Not by taste: by the rule in
[`process/CONVENTIONS.md`](../process/CONVENTIONS.md) → *Where a new rule goes*. Try the classes in
order — a **check** in the linter costs nothing at read time, a **method** in a skill is read only when
used, and only a **contract** two readers must agree on may grow `process/`. Nine of the eleven
proposals were phrased as canon additions; four of them turned out to be code.

| # | The defect | Verdict | Class | State |
|---|------------|---------|-------|-------|
| 3 | the linter never finds the instance, and reports success | accepted | check | **done** |
| 4 | the table parser reads one table and stops at a blank line | accepted | check | **done** |
| 11 | the canon says a check is manual when the tool already does it | accepted | contract (rewrite) | **done** |
| 1 | no notion of outcome observability (censoring) | accepted, reshaped | contract + method | **done** |
| 2 | `basis` carries three different roles | diagnosis accepted, form rejected | contract | **done** |
| 5 | enum columns have no neighbour for the qualifier | accepted | contract | **done** |
| 6 | no rule "one id, one row" | accepted | contract + check | **done** |
| 7 | a composite hypothesis cannot be half-refuted | accepted, with an addition | contract + check | **done** |
| 9 | `sources/` lacks a third file role: the living method | accepted as written | contract | **done** |
| 10 | "nothing raw outside the instance" breaks under vendoring | accepted, raised in priority | contract (rewrite) | **done** |
| 8 | a negative result has nowhere to live | **fourth register rejected**, need accepted | template + rule | **done** |

All eleven are shipped. What each cost, measured after the fact: the always-loaded set went from 863 to
**876 lines** — +13 against the 15 estimated, and the ceiling of 900 still holds, because the additions
were paid for by deleting the copies they made stale (`OVERVIEW.md` §2 and §8 restated rules that the
change to *Raw data & access* and *Change logs* would otherwise have left contradicting the canon).

---

## Done — the tooling now tells the truth

### 3 · The linter never finds the instance

**Accepted.** `main()` globbed `examples/*` and `instances/*`, so the canonical vendored layout — the
instance in `product/` of the host repo — was never checked, and the run still printed `0 error(s)`.
The report's instance went unvalidated for two weeks while being told it was clean.

**Edit.** `tools/lint.py` takes instance paths as arguments; with none, it discovers them by **marker**
(`config.yaml` / `state.yaml` / `registers/` / artifacts) through `loops.instance.discover` — the same
finder the console uses, so the two can never disagree about what an instance is. Every run now prints
`instances checked: N — <paths>`, so **zero reads as a problem instead of as success**.

**Why here.** A machine can verify this; nothing about it belongs in prose an agent has to remember.

### 4 · The table parser reads one table and stops at a blank line

**Accepted, and it was still true after the read layer was rewritten.** `table_column` returned on the
first matching table, so a register that grew a second table (inherited nodes above, newly instrumented
below) was validated in its top half and reported as undefined in its bottom half. A blank line inside a
table truncated it silently.

**Edit.** `loops/text.py`: `table_column` and `table_rows` now span **every** table carrying the column;
`tables()` resumes across a blank line unless what follows is a real new table (header + divider), and
records `broken` when it happened. New linter check **J** reports the split as a WARN — the reader
stitches the halves, but the file is a trap for the next hand that edits it. Covered by four new
assertions in the smoke test.

**Sequencing note.** 3 and 4 shipped together on purpose. Fixing discovery alone would have produced a
screen of false errors on the first honest run (of the report's 67 findings, 60+ were the parser's
fault) — and a linter nobody believes is worse than one nobody ran.

**Also fixed in passing.** The console's parser of the linter's output matched check letters `A-G`, so
the findings of checks H and I — added a week earlier — were dropped on the floor. The pattern is now
open-ended: a new check can never be invisible there.

### 11 · The canon describes an automated check as manual

**Accepted.** `REGISTERS.md` told the reader to verify csv ids by hand "no lint tool yet" while check E
had been doing exactly that. It cost the report's author two weeks of a hand-rolled procedure.

**Edit.** The paragraph now names the command. The habit it implies: **when a manual check becomes a
machine check, the canon says the command in the same change** — otherwise the canon teaches the slow
path forever.

---

## Shipped — the decision, then what landed

### 1 · Outcome observability (censoring) — accepted, mechanism reshaped

The one place where following the framework faithfully produces a **wrong answer**, quietly. A cohort
metric divided by the whole cohort instead of by the members whose outcome window has elapsed yields a
plausible percentage that is simply false, and the error survives into group comparisons — two groups
"differing" by their age rather than their behaviour.

**Contract** (`REGISTERS.md`, ~4 lines): an `observed_n` column beside `value`; the rule that a cohort
metric's denominator is the observed, not the whole cohort; the observation window declared in the
node's definition. **An empty `value` means the outcome was not observable** — no prose sentinel inside a
numeric column, because the readers (charts, deltas) parse it. Adding a column is safe: the reader is
header-driven (`csv.DictReader`), so old rows simply have an empty cell.

**Method** (`tool-skills/library/retention-analysis/`, anti-patterns): the procedure — filter to the
observed, report `observed_n`, never divide by the cohort. The method already insists on reading *by
cohort* and says nothing about observability, so this is a genuine gap in both layers, not a missed read.

**Not in the canon:** any explanation of cohort analysis itself. The canon carries the contract; the
skill carries the technique. That boundary is what keeps the always-loaded set from becoming a textbook.

**Landed** as decided, plus what the contract implied downstream: the console shows `observed_n` in the
readings table and prints an empty `value` as `—` rather than as a missing number, and the Step 4 template
and the method's fragment both read their cohort cells as `…% (n=…)` with `—` for a period not yet
observable. The smoke test asserts that a csv written before the column existed still reads, with the new
fields empty instead of a shifted row.

### 2 · `basis` carries three roles — diagnosis accepted, the proposed form rejected

The column legitimately holds *how it was calculated*; in practice it also absorbed *who was counted*
(all accounts vs clients only) and *which slice* (a cohort). Rows can be read across the third and never
across the first, so one column cannot mean all three.

**Rejected: a compound value with a role prefix** (`pop:clients_only`). It revives exactly the compound
values the canon bans for a hypothesis `type` and a risk `category` — and which the linter now checks.
A framework cannot forbid compounding on one side and introduce it on the other.

**Accepted instead:** `basis` narrows to the calculation variant; a **`population` column** joins it,
with the node's default population declared as a **field in `metric-tree.md`, not as a paragraph of
prose** (the report's own workaround made an empty cell in the csv mean whatever a neighbouring markdown
sentence said — the exact implicitness the canon otherwise kills). A cohort or segment is **not** a
basis: it is a distinct node, or later a column of its own if it proves it needs one.

**Landed**, and the console was made to obey it: a metric's series is grouped by `basis` **and**
`population`, and a KPI tile's delta is computed only inside one variant. A chart that drew two
populations as one line would have taught the eye exactly the comparison the contract forbids.

**Stated weakness.** This is the only one of the eleven with no cheap machine check — a linter cannot
tell that a `basis` value is really a population. It rests on discipline, and that is recorded here
rather than hidden.

### 5 · Enum columns have no neighbour for the qualifier — accepted

Eight cells in the report's metric register carried a legal value plus a needed qualifier
(`proxy (manual pass)`, `instrumented (since <date>)`). Every one is sensible and every one breaks the
enum. That is content pressing on a form with no valve.

**Edit:** a `note` column in `metric-tree.md`, plus one line: an enum cell holds the value only,
everything else goes in the neighbouring column. And **`tags` gets written into `REGISTERS.md`** — the
valve the report credits to risks is currently documented only in `CONVENTIONS.md`, so the schema file
does not know about its own escape hatch.

### 6 · One id, one row — accepted

Three metric ids in one cell (`M-dau / M-wau / M-mau`, sharing a definition) broke the link to the csv:
three series pointing at nothing. Same disease as a compound enum, one column over.

**Edit:** one contract line (an `id` cell holds exactly one canonical id) plus a check — and the message
must name the likely cause. The existing message was formally correct and read as a linter bug, which
means it failed.

**Landed** as check **K**, which fired on its first run against the report's own instance and named the
cell (`M-dau / M-wau / M-mau`), which id is reachable, and how many rows it should become. Check **E**'s
message now offers the three causes in order of likelihood instead of stating the fact alone.

### 7 · A composite hypothesis cannot be half-refuted — accepted, with an addition

Half of a refuted hypothesis is the most valuable kind of result: it takes a named strategic bet off the
table. There is nowhere to write it, so the next session re-opens it.

**Rule** (`CONVENTIONS.md`): a composite hypothesis is split into two at the first attempt to test it
(Step 4, when a metric is attached), the halves reference the original, the original is closed.

**The addition the report missed:** `superseded` is not in the status enum (`open · testing · validated ·
refuted`), so today the original would be closed as `refuted` — which is a lie, it was not disproved, it
was divided. The enum gains `superseded`.

**Check:** `confidence` and `status` join the linted enums. Only `type` is checked today, so the
report's own out-of-enum value would have passed even on an instance the linter could see. The
language-alias machinery already exists; this is a table row.

**Landed**, and it immediately caught drift in the framework's *own* committed example: four risks read
`accepted (monitored)` — a legal value with a qualifier welded on, the exact disease of point 5, sitting
in the file new users copy from. Fixed there (`status: accepted`, `tags: monitored`). Reading the value
out of `[sourced: metrics W24]` is one shared primitive, so the linter and the console agree on it.

### 9 · A third file role in `sources/`: the living method — accepted as written

`sources/` distinguishes a **living** access file from **dated** evidence. The rules for turning a raw
source into register values — who is excluded, how keys fold to a person, which window — fit neither: put
them in dated evidence and the next capture forks them into two authoritative versions.

**Edit:** name the three roles (access · method · evidence, the first two living, the third immutable)
and add `source-method` to the `node_type` matrix. What makes this worth a canon line rather than a
habit: the method file is what makes a reading **reproducible**, which is the question a stakeholder
actually asks.

### 10 · "Nothing raw outside the instance" breaks under vendoring — accepted, raised in priority

The rule assumes the instance folder is a private safe place. Under vendoring it is the opposite: the
framework sits in a repo whose `origin` may be public, so "keep raw captures inside the instance" pushes
personal data **towards** the dangerous location. The report's owner did the right thing and formally
violated the canon.

**Edit:** restate the rule from intent — raw captures never go under version control and are deleted once
their values land; where the instance lives in a repo with an external origin, the working folder goes
outside it. Legitimise the shape the instance already found: **analysis code outside, a reference to it
inside** (their change-log entries cite the script that produced each reading). Named as vendoring,
because the canon still quietly assumes a monorepo while `FRAMEWORK-VERSION` proves vendoring was the
plan. No net growth — the paragraph is rewritten, not extended.

### 8 · A negative result has nowhere to live — the fourth register is rejected

**Rejected: `registers/tests.md`.** It fails the four-sign test now written into
[`process/REGISTERS.md`](../process/REGISTERS.md) — and a fourth register is a core change touching the
overview, the README, the diagram and every tool. The report's own example ("no threshold separates the
groups") is a **refuted hypothesis about a metric definition** in everything but name: the content
already has a home.

**Accepted need, three cheap pieces:**

- a *what we checked and did not confirm* field in the Step 4 artifact template (their option B);
- one rule: **a register change-log entry names the ids it moved.** The mechanism already exists — dated
  entries with From → To / Why / Trigger — and a live instance already writes them this way; what is
  missing is the requirement, so retrieval by id is reliable;
- the per-item history is then **assembled by the console** from the change logs, not stored a second
  time. About twenty lines on the existing read layer, and zero canon.

**Landed** at that size: a `⟲ n` control on every register row opens the trail of that id, gathered from
artifact *and* register change logs, newest first. `⟲ 0` is itself a finding — the item moved and nobody
wrote why. Writing it exposed that the committed example had **no change logs at all**, in any artifact or
register; the three registers now carry them, written the new way, so the example demonstrates the rule
instead of quietly breaking it.

That third piece also answers a separate question we had been circling — how to see the trail of one
hypothesis without reading a whole file. One mechanism, two needs.

---

## What the report changed beyond its eleven points

**A rule about the framework's own growth.** Nine of eleven proposals were phrased as additions to files
an agent reads on every pass. Each was justified; together they would have thickened precisely the
expensive layer. That is how a framework accretes: every scar becomes a paragraph. The classification
rule and the budget in `CONVENTIONS.md` came out of reading this report, and the eleven points were then
re-decided against it — four turned out to be code, two are rewrites with no net growth, and the whole
list came to **+13 lines** of canon, paid for by deleting three restatements it had just made stale.

**A test for a fourth register**, so the next "we need a register for X" is decided on evidence. Its
first two uses are in this file: the workings register is rejected, and *segments* — which pass all four
signs — are recorded in `REGISTERS.md` as an open candidate with the triggers that would decide them.

**A confirmation that the report's own class of bug was structural.** Points 3, 4 and 10 share one root:
the tooling and the canon were written against this repository's layout, while vendoring is how the
framework is actually deployed. The smoke test now carries an instance created **outside** the repo, so
"works in the monorepo" fails in CI instead of in someone's product.

**One thing the framework is still missing, larger than any single point.** There is no method for the
data-gathering pass itself — how to reach a source, decide the population, compute, and land the values
in the registers. The library has 31 methods, including cohort retention, and none of them covers this.
The report's author had to invent it, and points 1, 2 and 9 were all born there. That is a skill to
write, tracked separately from this list — and it stays open after all eleven points are closed, which is
the useful thing to notice: the report's individual complaints were symptoms of one missing method.
