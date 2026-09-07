#!/usr/bin/env python3
"""very-ai-product-loops — wiring & instance linter.

Dependency-free (Python 3 stdlib only) so it runs anywhere the framework is cloned. It checks the
framework's *mechanics* (where drift silently breaks two agents or an aggregator) and every
instance's registers against the canon. This is the "one script" that turns the wiring class of
bugs from a manual audit into a CI gate.

Parsing lives in `tools/loops/` — the one shared read layer, used by this linter and the local UI
alike. A second parser would drift from the canon and reintroduce exactly the bugs checked here.

Checks (ERROR fails CI · WARN never does):
  A  a card's `writes: section:<id>` has a matching `{#id}` in its template-fragment
  A2 tool `questions.yaml` `writes` (atoms, same grammar as the card) matches the card's sections;
     the old `produces:` spelling is an ERROR
  B  every written section is homed in some step's artifact (a step template `{#id}`)
  B2 a card that writes `section:X` is named on X's template marker — the marker is how a reader
     and check P find its worklog (first = primary, later = contributing / revisit)
  C  library index rows <-> tool folders, and index "Steps" <-> the card's `steps`
  C1 an anchor a method's SKILL.md names (`N#x` · `{#x}` · `section:x`, in the body or its
     prerequisites) is inside its perimeter — a matching `section:` atom in `reads:` or `writes:`.
     Exempt: the cumulative/inbox sections (hypotheses, to-clarify, …); a mention inside an
     `## Output` / `## Downstream` / `## Worklog & projection` section; a block that hands OFF rather
     than reads (`→`, feeds, downstream, anchors, owns, contributes, into `{#x}`, "filled later",
     "after `{#x}`", a `<!--w:adds-->` recorded door)  (WARN)
  C2 a section whose method's template-fragment declares a card slot (a live `<!-- card -->` in the
     fragment) carries a card mark of its own — the missing-mark half of the slot contract; and where
     the fragment's face opens with a bold label (`**Moat read:**`) and the instance is written in
     English, the section's mark sits on a block opening with that same label — a mark drifted off its
     slot (decksmith F-16b); a translated instance is matched by step-close, not here  (WARN)
  C3 a method with `evidence_standard: decision` ships the decision line in its fragment (a keyed
     `**Decided:**` — CONVENTIONS → The decision line)  (WARN)
  C4 a fragment of a step ≥ 4 method that projects a SECTION (a `## … {#anchor}` heading) declares a
     card slot (`<!-- card -->`) — without one the console shows title + status for most of the
     plan; an item-block or worklog-shaped fragment has no section to face and is exempt  (WARN)
  C4b two fragments that project the same section anchor declare the same card face label (the
     `**Label:**` opening the `<!-- card -->` block) — one section, one face, whichever method
     re-projected last  (WARN)
  C6 a method whose `volume_rule` states a NUMERIC floor (`≥ N`, `N–M`, `at least N`) puts it in
     questions.yaml as `min:` on the gathering question (library README → The quality declaration);
     a structural rule ("every element of X …", "one row per …") has no list to floor  (WARN)
  C9 template ↔ fragment column parity for the sections a fragment projects: every fragment column
     has a counterpart in the step template's keyed form (matched by header prose — a fragment
     carries no keys, check O), and the section's PRIMARY tool's fragment carries every template
     column  (WARN)
  D  register enums per instance, read through the read layer (instance.load health): hypothesis
     type/status/confidence · post-test signal/decision · risk category/status · metric kind/
     instrumentation · feature state/confidence/priority · surface state; a value outside its enum is
     an ERROR; a missing required key column WARNs on a product instance and ERRORs on `examples/`
     (the same product-vs-reference split as O2)
  E  metrics.csv through the ONE reader (instance.metric_rows): every id has a definition row in
     metric-tree.md; a data row's field count equals the header's (an unquoted comma); every `id` is
     an `M-…` (no comment lines) — ERROR: a series nobody can interpret is a broken register, not a
     prose slip (E2 stays WARN because a prose citation is heuristic)
  E2 a cited `F-…`/`S-…` id in an instance artifact or register has a definition row in
     features.md/surfaces.md — the feature-register mirror of check E  (WARN)
  E3 a worked `6#must` item carries its full pre-registration: a `- **Feature:**` line naming an
     `F-…` row (or a declared `— to clarify —` gap), an `**Expected impact:**` with a check-by,
     and an `**Estimate:**` — everything the next impact-readout reads; the backlog table's
     Feature column likewise; every status (setup births the registers)  (WARN)
  E4 a features.md/surfaces.md row has a non-empty `source` — a row without evidence is an
     inventory from memory  (WARN)
  E5 an id a features.md `serves` cell cites resolves to a row in its own register
     (H-/R-/M-/F-/S-) — the cut rule and the impact-readout both read this link  (WARN)
  E6 a decision id (`D-…`) cited in an artifact, worklog or HANDOFF resolves to a row of the instance's
     `decisions.md` — the home of the dated human decision a `[sourced: decision D-…]` tag names; an
     instance that cites decisions and has no `decisions.md` gets one WARN (decksmith F-11)  (WARN)
  F  link canon: no GitMark-lite `[[...]]` links remain (canon = relative path + stable {#anchor})
  G  step gate-checklist items reference a real section id  (WARN)
  G2 a gate item whose sections are written but whose tick reads `unrecorded` (framework.GATE_READINGS):
     tick `open` and no move-5 trace — the pass wrote the section and stopped before Record  (WARN).
     "Written" is worked content beyond the shell in any language (framework.worked); a section
     reopened for re-sign (its change log records it on/after `last_pass`) reads `re-sign` and is silent
  G3 every state.yaml tick value is one of framework.TICK_VALUES (done · open · n/a · deferred)
  G4 every state.yaml tick id names a real gate item of its step (a stale or misspelled id ticks
     nothing)  (WARN)
  G5 the instance's content is written in `config.language`: a file whose letters are dominantly in
     the other script (Cyrillic vs Latin) contradicts the owner's decision (hub F-08)  (WARN)
  G6 an explicit `n/a` tick carries its reason as a comment beside it (state-schema) — a skip is a
     statement about the concept, never about a source the instance lacks (decksmith D-43 / F-17); a
     bare `n/a` WARNs
  G7 a `deferred` tick names what retires it — `until: <decision | pass | date>` in the tick's comment —
     so step-close can ask whether it has arrived; a `deferred` with no `until:` WARNs (decksmith F-16d)
  D2 confidence/source tags in instance artifacts and worklogs come from the closed CONVENTIONS
     vocabulary, verbatim and never localized: `[assumption]` bare · `[sourced: <where>]` ·
     `[validated: <evidence>]` · `[refuted: <why>]` — a compounded, translated or near-synonym
     (`[inference]`, `[estimate]`, …) tag is an ERROR; a tag whose argument carries a second bare tag
     (`[sourced: the brief — [assumption] on the count]`) is two verdicts in one bracket  (WARN)
  L2 a worked section of an `evidence_standard: external-sources` method that carries neither a
     `[sourced: …]` citation nor a single `— to clarify —` — settled-looking external analysis
     with no evidence shown and no gap declared  (WARN)
  H  instance config.yaml follows the pinned schema (required keys, one spelling, no aliases) and
     value shapes: `language` is a code, `directions` a list, `active_status` a real status file
  H2 an instance artifact's frontmatter carries the template's keys and invents none — an invented
     key (a worklog list, an active_status) is a second home for something the canon stores elsewhere
  H3 a HANDOFF.md names the registers it was verified against (N3: a handoff restores state, not
     truth — its Registers block cites at least one register file)  (WARN)
  I  a product's own skills (product-loops/tool-skills/…) obey the same wiring rules as vendored ones
  I2 a vendored framework is pinned and pointed at: FRAMEWORK-VERSION (tag + SHA) at the vendor root,
     a pointer to `start-work` in the product repo's root AGENTS.md (install/README → point 1; the
     delegation switch is config.yaml `delegation`, check H); detected by layout — the framework at the product repo's root with the instance
     beside it (canon), or in a sub-folder (legacy) — and silent in the framework's own dev repo
  J  a register table is not split by a blank line  (WARN)
  K  a register `id` cell names exactly one item (one row = one id)
  L  every library tool carries the quality declaration (evidence_standard · volume_rule ·
     selection_rule · rejects_shown), with legal values and internally consistent
  M  a vendored operations card has the template-fragment its written sections imply, and the
     operations index matches its folders row for row (the card core is check X's)
  N  a shipped subagent definition (.claude/agents/loops-*.md) carries only its kind's allowed write tool (loops-draft: Write; others: none)
  O  column keys live only on the step template (form of record) and are well-formed there
     (all-keyed-or-none, unique); a key in a method template is an error — the draft is matched by meaning
  O2 an instance artifact section carries its template's column keys (the projection contract;
     enforced — a template-keyed section left un-keyed in the instance is an error)
  O3 a column with a template-declared vocabulary (`<!-- enum:c:key: a | b -->` under the table)
     holds only its tokens — the template is the schema, for artifacts as for registers (check D)
  O4 a decision line's three fields are keyed (`<!--d:date-->` · `<!--d:by-->` · `<!--d:alts-->`,
     all or none) and its alternatives field is neither empty, a bare *none*, nor an unfilled
     placeholder; an English `**Decided:**` label with no keys WARNs (best-effort by construction)
  P  step worklogs: a step folder holds only `node_type: worklog` files named for the tools its
     sections use; required — every artifact section that names a method (or synthesis) has its worklog.
     A revisit (a later step's method on an earlier step's marker) lives in its OWN step's folder; a
     worklog in the wrong step's folder, and one no artifact names at all, get distinct messages  (WARN)
  P2 the worklog inputs BLOCK (`<!--w:reads-->` · `<!--w:adds-->` — a line names a block, so a wrapped
     paragraph reads whole): both keys or none, legal reads atoms, and the primary working's citations
     (section anchors, register ids incl. `M-7d`-style) stay inside the declared perimeter. Exempt:
     the change log, the orchestrator's-conclusions block, inline code and fences, an id quoted from a
     declared section's own text or from a table row sourced to a declared atom (daisy F-03, hub F-09);
     worklogs predating the line get one aggregate WARN per instance  (all WARN)
  P3 a step README's skeleton row and the template marker name the same tools for a section; with a
     single marker the first tool agrees too (it owns the worklog)
  Q  section confirmation: no schema (template/fragment) ships a `confirmed:`/`contested:` marker, and
     an artifact's `confirmed:` marker parses as a YYYY-MM-DD date (ERROR) else it silently means pending
  R  confirmation consistency: an `<!-- open -->` section (inbox) carries no `confirmed:`, and no
     section is both `confirmed:` and `contested:` (a verdict is one or the other)
  S  rests-on provenance: a `rests-on: <step>#<id>` target resolves to a real section, and a confirmed
     section resting on an unconfirmed foundation is surfaced  (WARN)
  T2 raw captures stay out of git: the instance (or a host repo up to the git root) carries a
     `.gitignore` rule for `sources/snapshots/` (or all of `sources/`) — N8, boundary-layout  (WARN)
  T3 no secret in instance text: an API key / token shape (`sk-…`, `AKIA…`, `ghp_…`, `xox…`, a long
     opaque value after `key:`/`token:`/`secret:`/`password:`, a private-key header) is an ERROR (N8)
  T  the boundary layer: sources/ holds only originals/ · snapshots/ · access/ (+INDEX.md; a flat
     legacy file WARNs); a passport (sources/access/*) is not an all-`— to clarify —` invented stub
     (WARN); an instance exchange skill (<instance>/skills/<slug>/) has a SKILL.md, and a `cadence:`
     needs a `last_run` in state.yaml (WARN); a worklog links another STEP's worklog only when the
     reading method's card declares it (`worklog:<step>/<method>` in reads) — undeclared is an ERROR
  S2 sources/INDEX.md rows carry a typed slot (`Type <!--c:type-->`) from the closed list
     `cards.SOURCE_SLOTS` (kb · interview · research · metrics · git): unknown word ERRORs, an
     untyped row or a keyless index header WARNs
  U  a library method serves exactly one step (`steps` has one entry)
  U2 every library method is named by at least one step-template `<!-- tool: … -->` marker — the
     law of ranks makes the marker the only reach, so an unnamed method is unreachable
  V  a status's per-step tools list holds library methods only, each with a `<!-- tool: … -->` home
     in that step's template (how data is gathered belongs in the goals prose)
  W  the always-loaded canon (AGENTS.md + OVERVIEW + OPERATING-LOOP + goal-map + CONVENTIONS) stays
     visible in size — a guideline that WARNs, never a gate (EXTENDING -> subtraction rule)
  W2 a method's `## Worklog & projection` section stays under 120 words — the mechanics live in
     worklog-resolution; the card lists only what is method-specific (audit C5)  (WARN)
  Y  questions.yaml is machine-readable: every question `type` is from the shared vocabulary
     (no `type: x_from: y` double-colon scalars)
  Y2 every YAML the framework reads — a card's frontmatter, an artifact's or worklog's frontmatter,
     config.yaml, state.yaml — stays inside the reader's subset: a flow map `{a: b}` or a list of maps
     `- k: v` parses to a bare string in silence (yamlite.unsupported names the line)
  X  every card fills the one questionnaire (process/reference/card-schema.md): the core is present,
     `kind` and the atoms of reads/writes/surfaces come from the controlled vocabularies, the
     per-kind fields hold (a method has `steps` and no `surfaces` — the law of ranks), and a card the
     goal map routes to owes a non-empty `surfaces`; an off-schema key WARNs
  X2 every instance file that carries a `node_type` names one the matrix knows
     (process/reference/node-type-matrix.md) — an unknown value drops the file out of every
     convention silently (hub F-03); the vocabulary is read from the matrix, never listed here
  Z  a card's home follows its author: `kind: exchange` only inside an instance's `skills/`, and a
     framework kind never there

Run:  python3 tools/lint.py                 # every instance discoverable from here
      python3 tools/lint.py product-loops   # or name the instance(s) to check
      python3 tools/lint.py --ci            # skip gitignored instances (what CI's checkout sees)
"""
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # tools/ -> repo root
sys.path.insert(0, os.path.join(ROOT, "tools"))

from loops import cards as C  # noqa: E402
from loops import framework as F  # noqa: E402
from loops import instance as I  # noqa: E402
from loops import text as T  # noqa: E402
from loops import yamlite  # noqa: E402

ERRORS, WARNS = [], []
SKIPPED = []          # instances `--ci` left out (gitignored), reported so a local run explains itself
# the framework's reference instances — held to ERROR on template shape (they ARE the form); a test
# points this at a fixture to exercise the `examples/` semantics without touching the real examples
EXAMPLE_ROOTS = [os.path.join(ROOT, "examples")]


def err(msg):
    ERRORS.append(msg)


def warn(msg):
    WARNS.append(msg)


def reset():
    """Forget one run's findings and caches — the test runner lints several fixtures in one process."""
    del ERRORS[:]
    del WARNS[:]
    del SKIPPED[:]
    _SNAPSHOTS.clear()
    _READ.clear()
    _MEMO.clear()


_READ = {}


def read(path):
    """One read per file per run — the linter never writes, so a file cannot change underneath it
    (a test that rewrites a fixture between runs calls `reset()`)."""
    if path not in _READ:
        _READ[path] = T.read(path)
    return _READ[path]


_MEMO = {}


def _memo(key, make):
    """Per-run memo for the framework-side tables several checks rebuild (templates, steps)."""
    if key not in _MEMO:
        _MEMO[key] = make()
    return _MEMO[key]


def rel(path):
    return T.rel(path, ROOT)


# ---------------------------------------------------------------- checks

def check_tools(tools, homed):
    for name, t in tools.items():
        fm = t["fm"]
        secs = C.sections_written(T.as_list(fm.get("writes")))
        # A — a written section is present in the template-fragment
        frag = os.path.join(t["dir"], "template-fragment.md")
        frag_ids = T.section_ids(read(frag)) if os.path.exists(frag) else set()
        for sid in secs:
            if sid not in frag_ids:
                err("A [%s] writes `section:%s` but its template-fragment.md has no {#%s}"
                    % (name, sid, sid))
        # A2 — questions.yaml carries no write perimeter of its own: the card header is the one
        # home of `writes` (a second copy drifted in 38 of 47 files and nothing read it)
        q = os.path.join(t["dir"], "questions.yaml")
        if os.path.exists(q):
            qtext = read(q)
            if re.search(r"^(writes|produces):", qtext, re.M):
                err("A2 [%s] questions.yaml declares `writes:`/`produces:` — the write perimeter lives "
                    "in SKILL.md frontmatter only; the interview script asks, it does not write" % name)
        # B — every written section is homed in a step artifact
        writers = _template_writers()                 # memoized — one read of the templates per run
        for sid in secs:
            if sid not in homed:
                err("B [%s] writes `section:%s` with no home — not in any step template {#%s} "
                    "(homeless output)" % (name, sid, sid))
            # B2 — and the section's marker names this method: the marker is how a reader (and
            # check P) finds the method's worklog; a writer the marker omits has a file nobody can
            # resolve (worklog-resolution -> A revisit from a later step)
            elif sid in writers and name not in writers[sid]:
                err("B2 [%s] writes `section:%s` but the template marker on {#%s} names only %s — "
                    "add it to the marker (first = primary, later = contributing / revisit)"
                    % (name, sid, sid, ", ".join(writers[sid])))


def check_readme_markers(tools):
    """P3 — a step README's *Artifact skeleton* rows and the step template's `<!-- tool: -->` markers name
    the same tools, section by section.

    Two homes for "which method fills this section": the README row is what a human (and the console)
    reads, the template marker is what the linter and check P resolve the worklog from. When they
    drift, the console links one worklog and the linter demands another — live finding on `6#must`.
    Only library tool names are compared (a row's prose aside is not a claim); with a single marker the
    first tool must agree too, since the first tool owns the section's worklog.
    """
    writers = _template_writers()
    for st in _steps():                            # the skeleton rows as the read layer parses them
        step = os.path.basename(st["dir"])
        for sk in st["skeleton"]:
            sid = sk["id"]
            row = [t for t in sk["tools"] if t in tools]
            mark = writers.get(sid)
            if mark is None:
                continue                                  # no marker (synthesis) — nothing to compare
            if set(row) != set(mark):
                err("P3 %s/README.md `%s`: the skeleton row names %s, the template marker names %s — one "
                    "section, one set of writers (the console reads the row, check P the marker)"
                    % (step, sid, row or "no tool", mark))
            elif row and mark and row[0] != mark[0] and len(set(mark)) == len(mark):
                # a section with several markers (per-direction blocks) has no single first tool
                tpl = read(os.path.join(ROOT, "steps", step, "template.md"))
                sec = next((s for s in T.sections(tpl) if s["id"] == sid), None)
                if sec and len(TOOL_MARK_RE.findall(sec["body"])) == 1:
                    err("P3 %s/README.md `%s`: the row lists `%s` first, the marker `%s` — the first tool "
                        "owns the section's worklog, so the order is a claim" % (step, sid, row[0], mark[0]))


def _template_writers():
    """{section id: [tools its `<!-- tool: -->` marker names]} across the step templates."""
    return _memo("writers", _template_writers_now)


def _template_writers_now():
    out = {}
    for tpl in glob.glob(os.path.join(ROOT, "steps", "*", "template.md")):
        for sec in T.sections(read(tpl)):
            if not sec["id"]:
                continue
            for m in TOOL_MARK_RE.findall(sec["body"]):
                out.setdefault(sec["id"], []).extend(t.strip() for t in m.split(","))
    return out


EVIDENCE_STANDARDS = {"external-sources", "primary-research", "internal-data", "derived", "decision"}
REJECTS_SHOWN = {"required", "n/a"}
QUALITY_KEYS = ("evidence_standard", "volume_rule", "selection_rule", "rejects_shown")

# Register enum columns filled only after a test readout — validated when present, never
# flagged as missing (check D). The gradation lives in the row; not every row has been read yet.
# `feature priority` joins them: it is written by the Step-4/5 passes, so a register that
# pre-dates the cascade (or a product that has not run those passes) legally lacks the column.
OPTIONAL_ENUM_LABELS = {"hypothesis signal", "hypothesis decision", "feature priority"}


def _blank(v):
    """A frontmatter value that is present but says nothing.

    Anything that is not a non-empty string counts: `key:` with nothing after it parses to None, and
    `key: []` parses to an empty list. Both used to pass the "is it declared" test *and* slip past the
    enum test below (which is guarded on `isinstance(str)`), so a required key could be present and
    check nothing — the exact failure this check exists to prevent, one level up.
    """
    return not (isinstance(v, str) and v.strip())


def _missing(v):
    """A required frontmatter key that is absent or empty — for keys whose legal value may be a list.

    Distinct from `_blank`, which is stricter on purpose: the quality keys are single words or one
    sentence, so a list there is a mistake.
    """
    return v is None or v == "" or v == [] or v == {}


def check_quality(tools):
    """L — the quality declaration every library method owes.

    A method that never states what would make its output wrong produces plausible output forever.
    These four keys are the cheapest place to make it state it: checked once per run, costing nothing
    at read time (CONVENTIONS -> "Where a new rule goes": a check before a paragraph).
    """
    for name, t in sorted(tools.items()):
        fm = t["fm"]
        for key in QUALITY_KEYS:
            if key not in fm or _blank(fm.get(key)):
                err("L [%s] no `%s` in SKILL.md frontmatter — the quality declaration is required for "
                    "every library method (see tool-skills/library/README.md -> The quality declaration)"
                    % (name, key))
        ev = fm.get("evidence_standard")
        if not _blank(ev) and ev.strip() not in EVIDENCE_STANDARDS:
            err("L [%s] evidence_standard = %r is not one of %s — exactly one value; a secondary "
                "class belongs in the body, never compounded into the key"
                % (name, ev, sorted(EVIDENCE_STANDARDS)))
        rs = fm.get("rejects_shown")
        if not _blank(rs) and rs.strip() not in REJECTS_SHOWN:
            err("L [%s] rejects_shown = %r is not one of %s" % (name, rs, sorted(REJECTS_SHOWN)))
        # a method that generates or selects must show what it cut: otherwise the next pass
        # re-proposes the same discarded option, and a filter never reached is indistinguishable
        # from one that was applied and passed
        cuts = [k for k in ("volume_rule", "selection_rule")
                if isinstance(fm.get(k), str) and fm[k].strip() and fm[k].strip() != "n/a"]
        if cuts and isinstance(rs, str) and rs.strip() == "n/a":
            err("L [%s] declares %s but rejects_shown = n/a — a method that generates or selects "
                "shows what it cut and why" % (name, " and ".join("`%s`" % c for c in cuts)))




# sections every method may name without declaring them: cumulative register projections and the
# agent→human inboxes (CONVENTIONS → Section confirmation: `<!-- open -->` sections), plus the
# worklog's own intake anchor
AMBIENT_SECTIONS = {"hypotheses", "global-hypotheses", "to-clarify", "open-questions", "blockers",
                    "intake", "change-log"}
BODY_ANCHOR_RE = re.compile(r"\b[1-6]#([a-z][a-z0-9-]*)|\{#([a-z][a-z0-9-]*)\}|\bsection:([a-z][a-z0-9-]*)")
# a SKILL.md section whose mentions are hand-OFFS, not reads: what the method produces and where it goes
HANDOFF_SECTION_RE = re.compile(r"output|downstream|feeds|worklog\s*&\s*projection", re.I)
# a block that hands a section off, defers it, or names another owner — the anchor in it is not read
HANDOFF_BLOCK_RE = re.compile(
    r"→|\bfeeds?\b|\bdownstream\b|\banchors\b|\bowns\b|\bcontribut|recorded door|w:adds"
    r"|\binto\s+`?\{#|\bfilled later\b|\blater in\b|\bafter\s+`?\{#"
    # a relation or comparison, not a read: "the temporal view behind {#x}", "a flat {#x} list would …"
    r"|\bbehind\s+`?\{#|\bwould\b|\brather than\b|\binstead of\b", re.I)
CARD_LABEL_RE = re.compile(r"^\*\*([^*]+?):?\*\*")
WORKLOG_SECTION_RE = re.compile(r"worklog", re.I)
WORKLOG_SECTION_WORDS = 120


def _read_anchors(body):
    """Anchors a SKILL.md body READS: every `N#x` / `{#x}` / `section:x` mention that is not a hand-off —
    not inside an Output/Downstream/Worklog section, and not in a block that passes the section on
    (`→`, feeds, into `{#x}`, "filled later", …). Mentions in prerequisites count as reads."""
    out = set()
    body = re.sub(r"```.*?```", "", body, flags=re.S)
    for sec in T.sections(body):
        if HANDOFF_SECTION_RE.search(sec["title"] or ""):
            continue
        lines = sec["body"].split("\n")
        seen_blocks = set()
        for n, line in enumerate(lines, 1):
            if not BODY_ANCHOR_RE.search(line):
                continue
            first, _, blk = T.block_at(sec["body"], n)
            if first in seen_blocks:
                continue
            seen_blocks.add(first)
            text = " ".join(x.strip() for x in blk)
            if HANDOFF_BLOCK_RE.search(text):
                continue
            out.update(a or b or c for a, b, c in BODY_ANCHOR_RE.findall(text))
    return out


def _card_labels(fragment_text):
    """{anchor: label} — the bold label opening the `<!-- card -->` block of each SECTION a fragment
    projects (a `## … {#anchor}` heading; `**Journey read:**` → `journey read`). A `{#x}` mentioned in
    the fragment's prose is not a projected section. The face two methods projecting one section
    must agree on."""
    out = {}
    for sec in T.sections(fragment_text):
        if not sec["id"]:
            continue
        lead = T.card_line(sec["body"])
        if lead:
            m = CARD_LABEL_RE.match(lead.strip())
            out[sec["id"]] = m.group(1).strip().lower() if m else lead.strip()[:40].lower()
    return out


def _header_names(headers):
    """Header cells reduced to comparable names: prose only (no key, no emphasis), lower-cased, cut
    before a parenthesised aside — `Links (H-…/M-…) <!--c:links-->` and `Links` are one column."""
    out = []
    for h in headers:
        n = T.plain(T.header_name(h)).lower()
        n = re.sub(r"\s*\(.*$", "", n).strip(" .:")
        if n:
            out.append(n)
    return out


_HEADER_STOP = {"the", "a", "an", "of", "to", "in", "on", "it", "is", "this", "that", "at", "for",
                "by", "with", "and", "or", "our", "us", "we", "be", "its", "per", "vs", "how", "what"}


def _header_words(name):
    return {w for w in re.findall(r"[a-z0-9]{2,}", name) if w not in _HEADER_STOP}


def _header_match(a, b):
    """Two header names mean one column when one contains the other or they share a content word —
    prose is matched by meaning at projection, so the test is lenient on purpose (`Why now` ~ `Why`,
    `Success threshold` ~ `Success`); a column with no word in common is the drift worth a WARN."""
    return a in b or b in a or bool(_header_words(a) & _header_words(b))


def check_library_bodies(tools, homed):
    """C1 · C3 · C4 · C6 · C9 — what a method's card, fragment and questions promise each other.

    C1: an anchor the SKILL.md names in its body or prerequisites (`3#pricing`, `{#segments}`,
    `section:jtbd`) is a read or a write — a method that reasons from a section it never declared has
    a nominal perimeter (14 cards on steps 4–6 did, audit C1). C3: a `decision` method ships the
    decision line in its fragment, or O4 has nothing to hold on the instance. C4: a step ≥ 4 fragment
    declares its card slot, or the console shows title + status for most of the plan. C6: a
    `volume_rule` states its floor as `min:` on the gathering question — the rule the library README
    already makes. C9: template ↔ fragment column parity for the sections a fragment projects — a
    fragment column with no counterpart in the template's keyed form is adapted away at projection
    (the thread breaks: F-… between spec and ranking, audit C9), and the primary tool's fragment
    carries every template column. Fragments carry no keys (check O), so columns match by header
    prose. All WARN — the library is a moving target while its cards are rewritten.
    """
    writers = _template_writers()
    tkeys = _template_section_keys()
    faces = {}                                   # {anchor: {tool: card label}} for C4b
    theaders = {}
    for path in sorted(glob.glob(os.path.join(ROOT, "steps", "*", "template.md"))):
        for sec in T.sections(read(path)):
            if not sec["id"]:
                continue
            for t in T.tables(sec["body"]):
                if any(T.column_keys(t["headers"])):
                    theaders[sec["id"]] = _header_names(t["headers"])
                    break
    for name, t in sorted(tools.items()):
        fm = t["fm"]
        skill_text = read(t["skill"])
        perimeter = set()
        for field in ("reads", "writes"):
            for atom in T.as_list(fm.get(field)):
                head, arg = C.split_atom(atom)
                if head == "section":
                    perimeter.add(arg)
        named = _read_anchors(T.body_after_frontmatter(skill_text))
        prereq = " ".join(str(x) for x in T.as_list(fm.get("prerequisites")))
        named |= {a or b or c for a, b, c in BODY_ANCHOR_RE.findall(prereq)}
        stray = sorted(a for a in named if a in homed and a not in AMBIENT_SECTIONS
                       and a not in perimeter and "*" not in perimeter)
        if stray:
            warn("C1 [%s] SKILL.md names section(s) %s but neither `reads` nor `writes` carries the "
                 "`section:` atom — a section the method works from is a declared input, or the "
                 "perimeter is nominal (card-schema → reads is a perimeter)"
                 % (name, ", ".join("`#%s`" % a for a in stray)))
        frag = os.path.join(t["dir"], "template-fragment.md")
        frag_text = read(frag) if os.path.exists(frag) else ""
        live_frag = re.sub(r"```.*?```", "", frag_text, flags=re.S)
        if str(fm.get("evidence_standard", "")).strip() == "decision" and frag_text \
                and not (D_KEY_RE.search(live_frag) or D_LABEL_RE.search(live_frag)):
            warn("C3 [%s] evidence_standard is `decision` but template-fragment.md carries no decision "
                 "line (`**Decided:** <!--d:date--> … <!--d:by--> … <!--d:alts--> …`) — the choice the "
                 "method rests on has no keyed home (CONVENTIONS → The decision line)" % name)
        steps = [str(x) for x in T.as_list(fm.get("steps"))]
        # only a fragment that projects a SECTION (`## … {#anchor}`) has a face to declare; an
        # item-block fragment (feature-/activity-/task-spec) or a worklog-shaped one has none
        projects_section = bool(re.search(r"^#{2,3}\s.*\{#[a-z0-9-]+\}\s*$", live_frag, re.M))
        if frag_text and projects_section and steps and steps[0].isdigit() and int(steps[0]) >= 4 \
                and not T.CARD_RE.search(live_frag):
            warn("C4 [%s] a step-%s method whose template-fragment.md declares no `<!-- card -->` slot "
                 "— the console shows title + status for its section (CONVENTIONS → Card line; the "
                 "mark's canonical home is the fragment)" % (name, steps[0]))
        q = os.path.join(t["dir"], "questions.yaml")
        vr = fm.get("volume_rule")
        # a rule that states a numeric floor ("10–15 …", "≥ 5", "at least 3") owes a `min:`; a
        # structural rule ("one row per player", "every moat") has no number to state
        numeric = (isinstance(vr, str)
                   and bool(re.search(r"\d+\s*[–-]\s*\d+|≥\s*\d|>=\s*\d|at least \d|min(?:imum)?\s*\d", vr))
                   and not re.match(r"\s*(every|each|all|one\b)", vr, re.I))   # "every X maps to ≥1 Y": per element
        if os.path.exists(q) and numeric and not re.search(r"^\s+min:\s*\d", read(q), re.M):
            warn("C6 [%s] declares a volume_rule (%r) but questions.yaml states no `min:` on the "
                 "gathering question — the floor lives on the `list` question so it runs before any "
                 "cut (library README → The quality declaration)" % (name, vr[:50]))
        # W2 — the boilerplate budget of the "Worklog & projection" section (audit C5)
        for sec in T.sections(skill_text):
            if WORKLOG_SECTION_RE.search(sec["title"] or ""):
                n = len(sec["body"].split())
                if n > WORKLOG_SECTION_WORDS:
                    warn("W2 [%s] `## %s` is %d words (guideline %d) — the mechanics live in "
                         "worklog-resolution; keep only what is method-specific here"
                         % (name, sec["title"], n, WORKLOG_SECTION_WORDS))
        if not frag_text:
            continue
        # C4b — one section, one face: collect the card label per projected anchor
        for sid, label in _card_labels(live_frag).items():
            faces.setdefault(sid, {})[name] = label
        for sec in T.sections(frag_text):
            sid = sec["id"]
            if not sid or sid not in tkeys or sid not in theaders:
                continue
            ftables = T.tables(sec["body"])
            if not ftables:
                continue
            fh = _header_names(ftables[0]["headers"])
            th = theaders[sid]
            extra = [h for h in fh if not any(_header_match(h, x) for x in th)]
            # the draft MAY be wider than the form (column-keys.md: adapted by meaning), so a spare
            # column is not drift — a table whose columns MOSTLY miss the form is another table
            if extra and len(extra) * 2 > len(fh):
                warn("C9 [%s] template-fragment.md#%s: %d of %d column(s) have no counterpart in the "
                     "step template's form — %s vs keys %s — the fragment projects a different table "
                     "than the section holds (CONVENTIONS → Column keys)"
                     % (name, sid, len(extra), len(fh), ", ".join("`%s`" % h for h in extra),
                        ", ".join(tkeys[sid])))
            primary = (writers.get(sid) or [None])[0]
            missing = [h for h in th if not any(_header_match(h, x) for x in fh)]
            if primary == name and missing:
                warn("C9 [%s] template-fragment.md#%s (the section's primary tool) lacks template "
                     "column(s) %s — the form's keys %s have no source in the draft, so the projected "
                     "row is born empty" % (name, sid, ", ".join("`%s`" % h for h in missing),
                                            ", ".join(tkeys[sid])))
    for sid, by_tool in sorted(faces.items()):
        if len(set(by_tool.values())) > 1:
            warn("C4b {#%s}: %s declare different card faces — %s — one section shows one face, "
                 "whichever method re-projected last (CONVENTIONS → Card line)"
                 % (sid, " and ".join("`%s`" % t for t in sorted(by_tool)),
                    " vs ".join("`**%s:**` (%s)" % (lbl, t) for t, lbl in sorted(by_tool.items()))))


def check_operations():
    """M — a vendored operations card's sections are homed, and the plane's index matches its folders.

    The card core (name · kind · the three perimeter fields) is check X's, for every plane at once —
    a second presence test here would be two mechanisms for one rule, and it read an empty list as a
    missing field when an empty list is a *declaration* that the card touches nothing there.
    """
    homed = F.homed_sections(ROOT)
    names = set()
    for skill in sorted(glob.glob(os.path.join(ROOT, "tool-skills", "operations", "*", "SKILL.md"))):
        d = os.path.dirname(skill)
        name = os.path.basename(d)
        fm, _ = T.frontmatter(skill)
        for p in C.sections_written(T.as_list(fm.get("writes"))):
            frag = os.path.join(d, "template-fragment.md")
            frag_ids = T.section_ids(read(frag)) if os.path.exists(frag) else set()
            if p not in frag_ids:
                err("M [%s] writes `section:%s` but its template-fragment.md has no {#%s}"
                    % (name, p, p))
            if p not in homed:
                err("M [%s] writes `section:%s` with no home in any step template" % (name, p))
        if not os.path.exists(os.path.join(d, "template-fragment.md")):
            warn("M [%s] has no template-fragment.md — the shape it produces is described in prose "
                 "only, so two runs can produce two shapes" % name)
        names.add(name)
    # the operations index is the discovery mechanism for this plane (tool-skills/README.md), so an
    # index that has drifted from the folders misdirects silently — the same gap check C closes for
    # the library
    idx = read(os.path.join(ROOT, "tool-skills", "operations", "README.md"))
    listed = set(re.findall(r"^\|\s*\[`([a-z0-9-]+)`\]", idx, re.M))
    for missing in sorted(names - listed):
        err("M operations skill `%s` has a folder but no row in operations/README.md" % missing)
    for extra in sorted(listed - names):
        err("M operations/README.md lists `%s` with no skill folder" % extra)


def _cards(inst=None):
    """Every card in the tree: the framework's five planes, plus a product's own."""
    out = []
    for f in sorted(glob.glob(os.path.join(ROOT, "steps", "*", "README.md"))):
        out.append((f, "steps"))
    for plane in ("library", "operations", "outputs"):
        for f in sorted(glob.glob(os.path.join(ROOT, "tool-skills", plane, "*", "SKILL.md"))):
            out.append((f, plane))
    if inst:
        for f in sorted(glob.glob(os.path.join(inst, "skills", "*", "SKILL.md"))):
            out.append((f, "instance-skills"))
        for plane in ("library", "operations", "outputs"):
            for f in sorted(glob.glob(os.path.join(inst, "tool-skills", plane, "*", "SKILL.md"))):
                out.append((f, plane))
    return out


def routed_cards():
    """The cards the goal map actually routes to — read from goal-map.md, never a second list.

    `surfaces` is what move 5 owes, so it is required of exactly the cards a pass can start at. A
    hand-kept list here would drift from the router within a wave; reading the router keeps the two
    honest by construction.
    """
    text = read(os.path.join(ROOT, "process", "goal-map.md"))
    cut = re.search(r"^##\s+Passes", text, re.M)
    table = text[cut.start():] if cut else text
    table = table[:table.find("\n## ", 10)] if "\n## " in table[10:] else table
    named = set(re.findall(r"tool-skills/(?:operations|outputs)/([a-z0-9-]+)/SKILL\.md", table))
    planes = set()
    if "tool-skills/outputs/" in table:
        planes.add("outputs")
    if "<instance>/skills/" in table:
        planes.add("exchange")
    return named, planes


def _tool_card_exists(tool):
    """A card by tool id, on any framework plane — the resolver checks X and T share."""
    return any(os.path.isfile(os.path.join(ROOT, "tool-skills", plane, tool, "SKILL.md"))
               for plane in ("library", "operations", "outputs"))


def check_card_schema(inst=None):
    """X — every card fills the one questionnaire (process/reference/card-schema.md).

    This is the machine half of the wave's two load-bearing invariants: one entity with one schema
    (so a role cannot grow a second header shape), and ranks that do not mix (a method is never a
    routing target). It validates field **values** against the controlled vocabularies, not merely
    that the fields exist — a check that only asks "is `reads` present?" leaves every card free to
    describe its inputs its own way, and the single structure is nominal.
    """
    named, planes = routed_cards()
    for path, plane in _cards(inst):
        fm, _ = T.frontmatter(path)
        d = os.path.dirname(path)
        folder = os.path.basename(d)
        label = rel(path)
        kind = str(fm.get("kind", "")).strip()
        if fm.get("node_type") != "card":
            err("X [%s] node_type is `%s` — every instruction an agent acts on is `card`"
                % (label, fm.get("node_type", "(absent)")))
        if kind not in C.KINDS:
            err("X [%s] kind `%s` is not one of %s" % (label, kind or "(absent)", " · ".join(C.KINDS)))
            continue
        for key in C.CORE:
            if key in C.FORBIDDEN_BY_KIND.get(kind, ()):
                continue          # the law of ranks removes it for this kind — see below
            if key not in fm:
                err("X [%s] declares no `%s` — the core every card carries" % (label, key))
        # name threads the id: folder, frontmatter, worklog. A step folder carries its number.
        expected = re.sub(r"^[0-9]+-", "", folder)
        if str(fm.get("name", "")).strip().strip('"') not in ("", expected):
            err("X [%s] frontmatter name is `%s` — it must match the folder (`%s`)"
                % (label, fm.get("name"), expected))
        for field in ("reads", "writes", "surfaces"):
            if field not in fm:
                continue
            for defect in C.atom_errors(field, T.as_list(fm.get(field))):
                err("X [%s] %s" % (label, defect))
        # a declared foreign worklog input names a real method — a typo here silently widens
        # nothing, it just never resolves; catch it at the card
        for atom in T.as_list(fm.get("reads")):
            head, arg = C.split_atom(atom)
            if head == "worklog" and arg and arg != "*" and C.WORKLOG_ADDR_RE.match(arg):
                tool = arg.split("/", 1)[1]
                if not _tool_card_exists(tool):
                    err("X [%s] reads `%s` but no card `%s/SKILL.md` exists under tool-skills/ — "
                        "a declared worklog input names a real method" % (label, atom, tool))
        for key in C.REQUIRED_BY_KIND.get(kind, ()):
            if key not in fm:
                err("X [%s] a `%s` card declares no `%s`" % (label, kind, key))
        for key in C.FORBIDDEN_BY_KIND.get(kind, ()):
            if key in fm:
                err("X [%s] a `%s` card may not carry `%s` — the law of ranks (card-schema.md)"
                    % (label, kind, key))
        must_surface = (kind in C.NEEDS_SURFACES or folder in named
                        or (kind == "output" and "outputs" in planes)
                        or (kind == "exchange" and "exchange" in planes))
        if must_surface and not T.as_list(fm.get("surfaces")):
            err("X [%s] the goal map routes to this card, so move 5 owes something — `surfaces` "
                "is empty" % label)
        if kind == "output" and str(fm.get("output_kind", "")) not in C.OUTPUT_KINDS:
            err("X [%s] output_kind `%s` is not %s"
                % (label, fm.get("output_kind"), " | ".join(C.OUTPUT_KINDS)))
        if kind == "exchange" and str(fm.get("direction", "")) not in C.DIRECTIONS:
            err("X [%s] direction `%s` is not %s"
                % (label, fm.get("direction"), " | ".join(C.DIRECTIONS)))
        for key in fm:
            if key not in C.known_fields(kind):
                warn("X [%s] unknown card field `%s` — a key outside card-schema.md cannot quietly "
                     "become de-facto schema" % (label, key))


def check_card_home(inst=None):
    """Z — a card's home is decided by who authored it, not by what it is about.

    The discriminator is as objective as the delivery channel in `sources/`: shipped with the
    framework -> `tool-skills/`; written for one product -> `<instance>/skills/`. Without this, a
    product's own procedure lands on the framework shelf and the next re-vendoring erases it.
    """
    for path, plane in _cards(inst):
        fm, _ = T.frontmatter(path)
        kind = str(fm.get("kind", "")).strip()
        label = rel(path)
        if plane == "instance-skills" and kind != "exchange":
            err("Z [%s] a card in a product's `skills/` is `kind: %s` — that home holds the "
                "product's own exchange cards; a framework kind belongs in tool-skills/"
                % (label, kind or "(absent)"))
        if kind == "exchange" and plane != "instance-skills":
            err("Z [%s] `kind: exchange` outside an instance's `skills/` — an exchange card is "
                "written for one product and must not ship with the framework" % label)


WRITE_TOOLS = {"Write", "Edit", "MultiEdit", "NotebookEdit", "Bash"}
# Deliberately NOT flagged: the spawn tools (`Agent` / `Task`). An agent that can spawn any type can
# reach one that writes, which is the hole `orchestration/SKILL.md` states out loud — but every
# shipped definition keeps that tool on purpose, so a check here would warn on every run forever and
# teach the reader to ignore warnings. A standing "this is intended" warning is worse than the prose.


def check_subagent_defs():
    """N — a shipped subagent definition may carry only the write tool its kind is entitled to.

    The write rule (OPERATING-LOOP -> Delegation) is a split, not a blanket ban: a `draft` subagent
    writes exactly one thing — its method's worklog — so `loops-draft` ships with `Write` and only
    `Write`. The other three kinds (`gather`, `research`, `verify`) write nothing, and the framework
    enforces that *mechanically* by shipping their definitions with no write tools. Both halves of the
    split are only true while they stay true: a `Write` slipping into `loops-verify`, or an `Edit`/
    `Bash` into `loops-draft`, silently converts a machine-enforced rule back into a hope. Which tools
    a definition lists is a shape, and a shape belongs in the linter (CONVENTIONS -> "Where a new rule
    goes").
    """
    # loops-draft writes its worklog and nothing else: `Write` is permitted, but no path-unrestricted
    # editor/shell (Edit/MultiEdit/NotebookEdit/Bash) that could reach a register or the artifact.
    ALLOWED = {"loops-draft.md": {"Write"}}
    for path in sorted(glob.glob(os.path.join(ROOT, ".claude", "agents", "loops-*.md"))):
        name = os.path.basename(path)
        fm, _ = T.frontmatter(path)
        raw = fm.get("tools")
        if _missing(raw):
            err("N [%s] declares no `tools` — a subagent definition with no tool list inherits "
                "everything, including the ability to write" % name)
            continue
        items = raw if isinstance(raw, list) else str(raw).split(",")
        listed = {str(t).strip() for t in items if str(t).strip()}
        bad = sorted((listed & WRITE_TOOLS) - ALLOWED.get(name, set()))
        if bad:
            err("N [%s] lists write-capable tool(s) %s — this kind may not write them (a `draft` may "
                "carry only `Write`, for its own worklog; the others write nothing)" % (name, ", ".join(bad)))


def check_index(tools):
    idx = read(ROOT + "/tool-skills/library/README.md")
    # Only the "## Index" section is the index. The file also documents schemas in tables whose first
    # column is a backticked value (`external-sources`, …), and reading the whole file made every enum
    # value look like a tool with a missing folder.
    cut = re.search(r"^##\s+Index\s*$", idx, re.M)
    idx = idx[cut.start():] if cut else idx
    # tool names appear as `name` in the first column of the index table
    listed = set(re.findall(r"^\|\s*`([a-z0-9-]+)`\s*\|", idx, re.M))
    folders = set(tools)
    for missing in sorted(folders - listed):
        err("C tool `%s` has a folder but no row in library/README.md index" % missing)
    for extra in sorted(listed - folders):
        # index may list planned tools; flag only if it claims a folder path
        warn("C index lists `%s` with no tool folder" % extra)
    # Steps column vs the card's `steps`
    for line in idx.splitlines():
        m = re.match(r"^\|\s*`([a-z0-9-]+)`\s*\|[^|]*\|[^|]*\|\s*([0-9, ]+)\|", line)
        if not m:
            continue
        name, steps_col = m.group(1), m.group(2)
        idx_steps = sorted(s.strip() for s in steps_col.split(",") if s.strip())
        if name in tools:
            ubs = sorted(str(x) for x in T.as_list(tools[name]["fm"].get("steps")))
            if idx_steps and ubs and idx_steps != ubs:
                err("C [%s] index Steps %s != card `steps` %s" % (name, idx_steps, ubs))


def check_instance(inst):
    """D + E — register enums and the metrics csv, read through `instance.load` and nothing else.

    The linter and the console used to read the registers with two parsers (the linter every table,
    the console the first; the linter the csv by hand, the console with `csv`) and disagreed on the
    same file — CI green, console red (hub F-01/F-05). Now both read one model; this check only
    *reports* what the read layer found, so the two verdicts cannot drift.
    """
    name = rel(inst)
    snap = _snapshot(inst)
    shape = err if _is_framework_example(inst) else warn
    for h in snap["health"]:
        code, msg = h["code"], h["message"]
        if code == "register-column":
            # a required key column missing: visible debt on a product instance (the register still
            # works by header prose), an ERROR on the reference examples — they ARE the form (as O2)
            shape("D [%s] %s" % (name, msg))
        elif code == "enum":
            err("D [%s] %s" % (name, msg))
        elif code == "metric-undefined":
            # Name the cause: the message used to be formally correct and read as a linter bug,
            # which is the same as not reporting it (field report, point 6).
            mid = re.search(r"`(M-[^`]+)`", msg)
            err("E [%s] metrics.csv id `%s` has no definition row in metric-tree.md — a typo, a "
                "node renamed without minting a new id, or several ids written into one "
                "definition cell (a row defines exactly one id)" % (name, mid.group(1) if mid else "?"))
        elif code in ("metrics-fields", "metrics-id", "metrics-header"):
            err("E [%s] %s" % (name, msg))


# a section may name several methods (`<!-- tool: A, B -->`); the first is the primary that owns
# the worklog (CONVENTIONS -> primary-tool). Capture the whole list; the caller takes the first.
TOOL_MARK_RE = re.compile(r"<!--\s*tool:\s*([a-z0-9-]+(?:\s*,\s*[a-z0-9-]+)*)\s*-->")
SYNTH_MARK_RE = re.compile(r"<!--\s*synthesis")
SOURCES_LINK_RE = re.compile(r"sources/[A-Za-z0-9._/-]+\.md")
# a markdown link whose target names a step folder's worklog (`<n>-<slug>/<tool>.md`)
WORKLOG_XLINK_RE = re.compile(r"\]\(([^)]*?([1-6]-[a-z][a-z0-9-]*)/[a-z0-9-]+\.md)[^)]*\)")
CLARIFY_RE = re.compile(r"to clarify")
SOURCES_SUBFOLDERS = {"originals", "snapshots", "access"}


_SNAPSHOTS = {}


def _snapshot(inst):
    """One `instance.load` per instance per run — the linter never writes, so the model cannot go stale
    underneath it, and the reader is the slowest thing here (it was read 13 times per run)."""
    if inst not in _SNAPSHOTS:
        _SNAPSHOTS[inst] = I.load(inst, ROOT)
    return _SNAPSHOTS[inst]


def _na_sections(inst):
    """{(step, section_id)} whose gate tick is `n/a` — a consciously skipped section.

    An explicit `n/a` (or the defaulted one on an unwritten optional item) says the instance chose
    not to work this section this cycle. A skipped section owes neither a worklog (check P) nor its
    template keys (check O2): both checks guard *filled* projections, and demanding the paperwork of
    a pass that never ran turns an honest skip into two permanent errors (live-run finding, daisy)."""
    if not os.path.exists(os.path.join(inst, "state.yaml")):
        return set()
    try:
        snap = _snapshot(inst)
    except Exception:
        return set()
    out = set()
    for st in snap["steps"]:
        for g in st["gate"]:
            if g.get("tick") == "n/a":
                for sid in (g.get("sections") or []):
                    out.add((st["step"], sid))
    return out


def check_worklogs(inst):
    """P — a step's worklogs live in a folder named for the step and named for the tools it uses.

    A worklog `<step-folder>/<tool>.md` is the source of truth a section projects from (CONVENTIONS ->
    Step folders & worklogs). One id `<tool>` threads the section's `<!-- tool: X -->` marker, the
    skill folder, and this file — so a reader resolves a section's worklog with no guess. **Required**:
    every artifact section that names a method (or `<!-- synthesis -->`) must have its worklog — a
    projection with no source of truth is the drift this layer exists to stop. A step the instance has
    not reached (no artifact file) is simply not iterated; a step whose artifact names no method needs
    no folder. An artifact still citing `sources/` directly (a source belongs in a worklog, cited
    there) is a WARN.
    """
    name = rel(inst)
    worked = _worked_sections(inst)
    for art in sorted(glob.glob(os.path.join(inst, "[1-6]-*.md"))):
        stem = os.path.basename(art)[:-3]                 # "2-analysis"
        folder = os.path.join(inst, stem)
        text = read(art)
        # only the FIRST tool of a marker owes a worklog up front; any named tool may own one
        # (a second tool's pass creates its worklog when that pass actually runs)
        named = {t.strip() for m in TOOL_MARK_RE.findall(text) for t in m.split(",")}
        # a section consciously skipped (`n/a` tick) or not yet worked (an untouched shell — steps
        # 2–6 instantiate whole) owes no worklog — only a FILLED section projects from one
        na = {sid for (st, sid) in _na_sections(inst) if str(st) == stem[0]}
        expected = set()
        for sec in T.sections(text):
            if sec["id"] in na or (int(stem[0]), sec["id"]) not in worked:
                continue
            expected.update(m.split(",")[0].strip() for m in TOOL_MARK_RE.findall(sec["body"]))
        if SYNTH_MARK_RE.search(text):
            expected.add("synthesis")
            named.add("synthesis")
        if not expected:
            continue                                      # no method sections → no worklogs owed
        if not os.path.isdir(folder):
            err("P [%s] %s has method sections but no `%s/` worklog folder — every filled section "
                "projects from a worklog (CONVENTIONS -> Step folders & worklogs)"
                % (name, os.path.basename(art), stem))
            continue
        present = set()
        for wl in sorted(glob.glob(os.path.join(folder, "*.md"))):
            base = os.path.basename(wl)
            present.add(base[:-3])
            fm, _ = T.frontmatter(wl)
            if fm.get("node_type") != "worklog":
                err("P [%s] %s/%s is not `node_type: worklog` — a step folder holds only worklogs"
                    % (name, stem, base))
                continue
            # a revisit (a later step's method named on an EARLIER step's marker) keeps its worklog
            # in its OWN step's folder (worklog-resolution -> A revisit from a later step): a tool
            # named by any artifact whose card runs at this step belongs here; one whose card runs
            # elsewhere sits in the wrong folder — even when this artifact's marker names it second.
            # `metrics-capture` is event-driven (an operations skill): its derivation worklog may
            # appear in any step folder without a section marker — the csv row cites it.
            tool = base[:-3]
            if tool in ("metrics-capture", "synthesis"):
                continue
            card_steps = _card_atoms(tool, inst, "steps")
            if tool in named or tool in _named_anywhere(inst):
                if not card_steps or stem[0] in card_steps:
                    continue                          # its own step's folder (or a card with no steps)
                where = ", ".join(sorted("%s-…/" % st for st in card_steps)) or "its method's step folder"
                warn("P [%s] %s/%s sits in the wrong step's folder — the tool is named by another "
                     "step's marker, and a revisit's worklog lives in its OWN step's folder (%s), "
                     "never the folder of the section it revisits (worklog-resolution → A revisit "
                     "from a later step)" % (name, stem, base, where))
            else:
                warn("P [%s] %s/%s is an orphan — no section of any artifact names tool `%s` in a "
                     "`<!-- tool: … -->` marker (daisy F-05: a marker on another step's section "
                     "would make it a revisit, not an orphan)" % (name, stem, base, tool))
        for miss in sorted(expected - present):
            err("P [%s] %s uses tool `%s` but %s/%s.md is missing — the section has no source of truth "
                "to project from (CONVENTIONS -> Step folders & worklogs)" % (name, stem, miss, stem, miss))
        if SOURCES_LINK_RE.search(text):
            warn("P [%s] %s links sources/ directly — a source citation routes through the worklog, "
                 "never the artifact (see source-intake)" % (name, stem))


def _named_anywhere(inst):
    """Every tool any artifact of the instance names in a `<!-- tool: -->` marker."""
    def make():
        out = set()
        for art in glob.glob(os.path.join(inst, "[1-6]-*.md")):
            out.update(t.strip() for m in TOOL_MARK_RE.findall(read(art)) for t in m.split(","))
        return out
    return _memo(("named", inst), make)


def _worked_sections(inst):
    """{(step, section_id)} the read layer counts as worked (framework.worked) — the one definition
    checks P, O2/O3 and C2 gate on: an untouched shell owes neither worklog, nor keys, nor a face."""
    snap = _snapshot(inst)
    return {(st["step"], sec["id"]) for st in snap["steps"] for sec in st["sections"] if sec.get("worked")}


def _card_atoms(tool, inst, field):
    """One perimeter field's atoms of the card behind a worklog stem — framework planes, then
    instance skills."""
    paths = [os.path.join(ROOT, "tool-skills", plane, tool, "SKILL.md")
             for plane in ("library", "operations", "outputs")]
    paths.append(os.path.join(inst, "skills", tool, "SKILL.md"))
    for path in paths:
        if os.path.isfile(path):
            fm, _ = T.frontmatter(path)
            return {str(a).strip() for a in T.as_list(fm.get(field))}
    return set()


def _declared_worklog_reads(tool, inst):
    """The `reads` atoms of the card behind a worklog stem — framework planes, then instance skills."""
    return _card_atoms(tool, inst, "reads")


def check_boundary(inst):
    """T — the boundary layer: sources/ subfolders, passports, exchange skills, worklog privacy.

    `sources/` holds only what comes from outside, in `originals/` · `snapshots/` · `access/` (+INDEX)
    — CONVENTIONS -> Raw data & access, reference/boundary-layout. A passport (`sources/access/*`) is
    the human's recorded answers, never an invented all-`— to clarify —` stub. An instance exchange
    skill lives at `<instance>/skills/<slug>/` with a `SKILL.md`; a `cadence:` needs a `last_run` in
    `state.yaml` or an overdue run can't be caught at session start. And a worklog is **private by
    default**: it links another STEP's worklog only when the reading method's card declares it
    (`worklog:<step>/<method>` in reads); undeclared cross-step exchange runs through the registers
    and the signed artifact sections (CONVENTIONS -> Step folders & worklogs).
    """
    name = rel(inst)
    srcdir = os.path.join(inst, "sources")
    if os.path.isdir(srcdir):
        stray = []
        for entry in sorted(os.listdir(srcdir)):
            p = os.path.join(srcdir, entry)
            if os.path.isdir(p):
                if entry not in SOURCES_SUBFOLDERS:
                    err("T [%s] sources/%s/ is not a known subfolder — sources/ holds only "
                        "originals/ · snapshots/ · access/ (reference/boundary-layout)" % (name, entry))
            elif entry != "INDEX.md":
                stray.append(entry)
        if stray:
            # Grandfather a flat legacy layout to WARN so pre-migration instances don't hard-fail.
            warn("T [%s] sources/ has flat file(s) %s — the layout is originals/ · snapshots/ · "
                 "access/ + INDEX.md; move them into a subfolder (reference/boundary-layout)"
                 % (name, ", ".join(stray)))
        for pf in sorted(glob.glob(os.path.join(srcdir, "access", "*.md"))):
            _, body = T.frontmatter(pf)
            content = [ln.strip() for ln in body.splitlines()
                       if ln.strip() and not ln.strip().startswith("#")]
            if content and all(CLARIFY_RE.search(ln) or set(ln) <= set("-—|: *_") for ln in content):
                warn("T [%s] sources/access/%s is all `— to clarify —` — a passport is the human's "
                     "recorded answers, not an invented stub (reference/boundary-layout)"
                     % (name, os.path.basename(pf)))
    # instance exchange skills
    last_runs = _snapshot(inst).get("last_run") or {}
    for sk in sorted(glob.glob(os.path.join(inst, "skills", "*"))):
        if not os.path.isdir(sk):
            continue
        slug = os.path.basename(sk)
        skill_md = os.path.join(sk, "SKILL.md")
        if not os.path.exists(skill_md):
            err("T [%s] skills/%s/ has no SKILL.md — an exchange skill is a normal skill "
                "(reference/boundary-layout)" % (name, slug))
            continue
        fm, _ = T.frontmatter(skill_md)
        if fm.get("cadence") and slug not in last_runs:
            warn("T [%s] skills/%s declares a `cadence` but state.yaml has no `last_run` for it — an "
                 "overdue run can't be detected at session start (boundary-layout)" % (name, slug))
    # a worklog links another STEP's worklog only when the reading method's card DECLARES it
    # (`worklog:<step>/<method>` in reads) — undeclared cross-step exchange still goes through
    # the registers and the signed sections
    for folder in sorted(glob.glob(os.path.join(inst, "[1-6]-*"))):
        if not os.path.isdir(folder):
            continue
        step_a = os.path.basename(folder)
        for wl in sorted(glob.glob(os.path.join(folder, "*.md"))):
            reader = os.path.splitext(os.path.basename(wl))[0]
            for m in WORKLOG_XLINK_RE.finditer(read(wl)):
                if m.group(2) == step_a:
                    continue
                linked = os.path.splitext(os.path.basename(m.group(1)))[0]
                atom = "worklog:%s/%s" % (m.group(2), linked)
                if atom in _declared_worklog_reads(reader, inst):
                    continue
                err("T [%s] %s/%s links another step's worklog `%s` without declaring it — a "
                    "worklog is an input only when the reading card's `reads` carries `%s`; "
                    "undeclared cross-step exchange goes through the registers and the signed "
                    "sections (CONVENTIONS -> Step folders & worklogs)"
                    % (name, step_a, os.path.basename(wl), m.group(1), atom))


def _gitignore_rules(start):
    """Every `.gitignore` rule from `start` up to the git root (or the filesystem root), as one list."""
    rules, d = [], os.path.abspath(start)
    while True:
        gi = os.path.join(d, ".gitignore")
        if os.path.exists(gi):
            rules.extend(ln.strip() for ln in read(gi).splitlines()
                         if ln.strip() and not ln.strip().startswith("#"))
        if os.path.isdir(os.path.join(d, ".git")) or os.path.dirname(d) == d:
            return rules
        d = os.path.dirname(d)


def check_sources_ignored(inst):
    """T2 — raw captures never reach git (N8; boundary-layout → snapshots/).

    The rule lived in prose only: the linter checked the subfolder *names* and nothing checked that
    `sources/snapshots/` is actually ignored. An instance with a `sources/` folder needs a rule for
    `sources/snapshots/` (or all of `sources/`) in its own `.gitignore` or any host `.gitignore` up to
    the git root; the framework repo ships one for its private instances.
    """
    if not os.path.isdir(os.path.join(inst, "sources")):
        return
    rules = _gitignore_rules(inst)
    if not any(re.search(r"(^|/)sources/(snapshots/?)?$|(^|/)sources/snapshots", r.rstrip("/") + "/")
               for r in rules):
        warn("T2 [%s] no `.gitignore` rule keeps `sources/snapshots/` out of git — raw captures are "
             "never committed (N8); add `sources/snapshots/` (or `sources/`) to the instance's or "
             "the host repo's .gitignore (reference/boundary-layout)" % rel(inst))


SECRET_RES = (
    ("an OpenAI-style key", re.compile(r"\bsk-(?:proj-|ant-)?[A-Za-z0-9_-]{20,}\b")),
    ("an AWS access key id", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
    ("a GitHub token", re.compile(r"\b(?:ghp|gho|ghu|ghs|ghr)_[A-Za-z0-9]{36,}\b|\bgithub_pat_[A-Za-z0-9_]{40,}\b")),
    ("a Slack token", re.compile(r"\bxox[abprs]-[A-Za-z0-9-]{10,}\b")),
    ("a private key block", re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |DSA |PGP )?PRIVATE KEY")),
    ("a long opaque value after a key/token/secret/password label",
     re.compile(r"(?i)\b(?:api[_-]?key|access[_-]?key|secret(?:[_-]?key)?|token|password|passwd)\b"
                r"\s*[:=]\s*[\"'`]?([A-Za-z0-9+/_=-]{32,})")),
)


def check_secrets(inst):
    """T3 — no secret in instance text (N8): a cheap regex sweep over every text file of the instance.

    A key pasted into a passport or a worklog "for now" is committed with the next `git add .`; the
    rule had no carrier. Shapes only — the sweep never decodes or validates a credential.
    """
    name = rel(inst)
    for path in sorted(glob.glob(os.path.join(inst, "**", "*"), recursive=True)):
        if not os.path.isfile(path) or not path.endswith((".md", ".yaml", ".yml", ".csv", ".txt", ".json")):
            continue
        try:
            text = read(path)
        except (OSError, UnicodeDecodeError):
            continue
        for what, rx in SECRET_RES:
            for m in rx.finditer(text):
                token = m.group(m.lastindex or 0)
                if re.fullmatch(r"[0-9a-f]{32,}", token or ""):
                    continue                                   # a git SHA, not a credential
                lineno = text[:m.start()].count("\n") + 1
                err("T3 [%s] %s:%d carries what reads as %s (`%s…`) — no secrets or PII in artifacts, "
                    "handoffs or worklogs (N8); move it to an access passport's *where it lives*, "
                    "never its value" % (name, os.path.relpath(path, inst), lineno, what, (token or "")[:6]))
                break


def check_handoff_registers(inst):
    """H3 — a handoff names the registers it was verified against (N3).

    A handoff restores state, not truth: its claims are checked against the registers before anyone
    relies on them. The `Registers (by reference only)` block is where that check leaves its trace —
    a handoff whose registers block (or whole body) never names a register file was written blind.
    """
    snap = _snapshot(inst)
    ho = snap.get("handoff") or {}
    if not ho.get("present"):
        return
    regs = ("hypotheses.md", "risks.md", "metric-tree.md", "metrics.csv", "features.md", "surfaces.md",
            "registers/")
    body = "\n".join(sec["body"] for sec in ho.get("sections", []))
    if not any(r in body for r in regs):
        warn("H3 [%s] HANDOFF.md names no register (registers/…, hypotheses.md, metrics.csv …) — a "
             "handoff restores state, not truth (N3): say which registers its claims were verified "
             "against, by reference" % rel(inst))


CYRILLIC_LANGS = {"ru", "uk", "be", "bg", "sr", "mk", "kk", "ky", "mn", "tg"}
NON_LATIN_LANGS = CYRILLIC_LANGS | {"el", "he", "ar", "fa", "zh", "ja", "ko", "hi", "th", "ka", "hy"}
_CYR_RE = re.compile(r"[\u0400-\u04FF]")
_LAT_RE = re.compile(r"[A-Za-z]")


def _node_type_vocabulary():
    """The `node_type` values the matrix names — its first column, backticked, plus the framework
    row's closed set. Read from the file so the matrix stays the one home of the enumeration."""
    vocab = set()
    for line in read(os.path.join(ROOT, "process", "reference", "node-type-matrix.md")).split("\n"):
        if not line.startswith("|") or line.startswith("|-"):
            continue
        first = line.strip("|").split("|")[0]
        vocab.update(re.findall(r"`([a-z][a-z0-9-]*)`", first))
    vocab.discard("node_type")
    return vocab


def check_node_types(inst):
    """X2 — every instance file with a `node_type` names one the matrix knows (hub F-03).

    `node_type` selects which conventions apply to a file (CONVENTIONS → Which conventions apply
    where). Cards, worklogs and artifacts were already checked by kind; sources, passports, registers
    and the handoff were not, so a typo (`source-access`) dropped the file out of every check without
    a word. The vocabulary comes from the matrix itself — a second list in code would drift.
    """
    import difflib
    vocab = _node_type_vocabulary()
    if not vocab:
        return
    name = rel(inst)
    for dirpath, dirnames, files in os.walk(inst):
        dirnames[:] = [d for d in dirnames if d not in (".git", "snapshots", "node_modules")]
        for fn in files:
            if not fn.endswith(".md"):
                continue
            path = os.path.join(dirpath, fn)
            fm = T.frontmatter_from(read(path))
            nt = fm.get("node_type")
            if nt is None or str(nt).strip() in vocab:
                continue
            near = difflib.get_close_matches(str(nt).strip(), sorted(vocab), n=1, cutoff=0.5)
            hint = " — did you mean `%s`?" % near[0] if near else ""
            err("X2 [%s] %s: node_type `%s` is not in the matrix (process/reference/node-type-matrix.md)"
                "%s — an unknown type drops the file out of every convention silently"
                % (name, os.path.relpath(path, inst), nt, hint))


def check_language(inst):
    """G5 — the instance's content is written in `config.language` (hub F-08).

    The canon and every card are English; in a long session an agent continues the instance in the
    language it has been reading, not the owner's. The decision is recorded in config.yaml and nothing
    guarded it. Cheap by design: count Cyrillic vs Latin letters per artifact/worklog (code, comments,
    tags and links stripped); a file whose letters are ≥ 60% in the contradicting script WARNs. Only
    the Cyrillic/Latin pair is judged — other scripts are not mapped, so they never fire.
    """
    snap = _snapshot(inst)
    lang = (snap.get("language") or "en").split("-")[0].lower()
    if lang in NON_LATIN_LANGS and lang not in CYRILLIC_LANGS:
        return
    expect_cyr = lang in CYRILLIC_LANGS
    files = sorted(glob.glob(os.path.join(inst, "[1-6]-*.md")))
    for folder in sorted(glob.glob(os.path.join(inst, "[1-6]-*"))):
        if os.path.isdir(folder):
            files.extend(sorted(glob.glob(os.path.join(folder, "*.md"))))
    for path in files:
        text = _live(T.body_after_frontmatter(read(path)))
        text = re.sub(r"<!--.*?-->|\[(?:assumption|sourced|validated|refuted)[^\]]*\]|https?://\S+", "", text, flags=re.S)
        cyr, lat = len(_CYR_RE.findall(text)), len(_LAT_RE.findall(text))
        if cyr + lat < 200:
            continue
        other = lat if expect_cyr else cyr
        if other / float(cyr + lat) >= 0.6:
            warn("G5 [%s] %s is %d%% %s letters but config.yaml says `language: %s` — the content "
                 "language is the owner's decision, not the canon's (hub F-08); write the instance in "
                 "its declared language" % (rel(inst), os.path.relpath(path, inst),
                                            round(100.0 * other / (cyr + lat)),
                                            "Latin" if expect_cyr else "Cyrillic", lang))


def check_yaml_forms(inst=None):
    """Y2 — every YAML the framework reads stays inside the reader's subset (yamlite.unsupported).

    A flow map (`products: {path: …}`) or a list of maps (`- key: value`) parses to a bare string with
    no error, and the consumer fails later or — worse — reads an empty perimeter. The reader stays
    tolerant (the console must render drift); the linter turns each such line into an ERROR with file
    and line. Framework cards are checked once (no `inst`), an instance's files per instance.
    """
    def report(label, issues):
        for i in issues:
            err("Y2 [%s:%d] %s — %s" % (label, i["line"], i["text"], i["reason"]))
    if inst is None:
        for path, _plane in _cards():
            report(rel(path), T.frontmatter_issues(read(path)))
        return
    name = rel(inst)
    for path, _plane in _cards(inst):
        if path.startswith(os.path.abspath(inst)):
            report(os.path.join(name, os.path.relpath(path, inst)), T.frontmatter_issues(read(path)))
    files = sorted(glob.glob(os.path.join(inst, "[1-6]-*.md"))) + \
        sorted(glob.glob(os.path.join(inst, "[1-6]-*", "*.md"))) + \
        sorted(glob.glob(os.path.join(inst, "registers", "*.md"))) + \
        [p for p in (os.path.join(inst, "HANDOFF.md"),) if os.path.exists(p)]
    for path in files:
        report(os.path.join(name, os.path.relpath(path, inst)), T.frontmatter_issues(read(path)))
    for fname in ("config.yaml", "state.yaml"):
        path = os.path.join(inst, fname)
        if os.path.exists(path):
            report(os.path.join(name, fname), yamlite.unsupported(read(path)))


W_KEY_RE = re.compile(r"<!--\s*w:([a-z-]+)\s*-->")
W_FIELDS = ("reads", "adds")
# a citation of an artifact section: a link/mention `<n>-<slug>.md#anchor` or an inline `` `#anchor` ``
ANCHOR_CITE_RE = re.compile(r"(?:[1-6]-[a-z][a-z0-9-]*\.md|`)#([a-z][a-z0-9-]*)")
REG_ID_CITE_RE = re.compile(r"\b([HRFS]-\d+)\b")
ID_FAMILY = {"H": "hypotheses", "R": "risks", "F": "features", "S": "surfaces"}
ORCH_HEAD_RE = re.compile(r"<!--\s*orchestrator\s*-->|orchestrator|оркестратор", re.I)


def _w_value(line, key):
    """The text of one `w:` field on the inputs line — the next field's label cut off."""
    parts = W_KEY_RE.split(line)
    for i in range(1, len(parts), 2):
        if parts[i] == key:
            return re.sub(r"·\s*\*\*[^*]*:?\*\*\s*$", "", parts[i + 1]).strip(" ·")
    return None


def _primary_region(text):
    """The worklog minus its two unrestricted zones — the change log and every orchestrator's-
    conclusions block (projection step 0). Only what remains is held to the perimeter."""
    body = T.without_change_log(text)
    out, skip_level = [], None
    for line in body.split("\n"):
        m = re.match(r"^(#{2,6})\s", line)
        if m:
            if skip_level is not None and len(m.group(1)) <= skip_level:
                skip_level = None
            if skip_level is None and ORCH_HEAD_RE.search(line):
                skip_level = len(m.group(1))
                continue
        if skip_level is None:
            out.append(line)
    return "\n".join(out)


def check_perimeter(inst):
    """P2 — the worklog's inputs line: keyed, legal atoms, citations inside the perimeter.

    A method's primary working draws on its card's `reads` and nothing else (card-schema → *reads is
    a perimeter*); the worklog records that perimeter on one keyed line — `w:reads` as the pass ran
    under it, `w:adds` for what the orchestrator supplemented on a rework — so an audit can tell a
    sanctioned widening from a leak. What the machine can see: the keys, the atoms' grammar, and the
    two mechanical citation classes (section anchors, register ids) landing outside the declared
    doors. What it cannot: whether an untagged claim came from outside — that stays with a `verify`
    lens. All WARN: prose citation is heuristic, and a hard gate here would teach agents to cite
    less, which is the opposite of the point. Worklogs predating the line get one aggregate WARN
    per instance (the S2 introduction pattern).
    """
    name = rel(inst)
    snap = _snapshot(inst)
    section_text = {}                          # {anchor: every artifact section body with that id}
    for a in snap["artifacts"]:
        for sec in a["sections"]:
            section_text[sec["id"]] = section_text.get(sec["id"], "") + "\n" + sec["body"]
    legacy = 0
    for step, logs in sorted(snap["worklogs"].items()):
        folder = os.path.join(inst, step)
        for tool, log in sorted(logs.items()):
            base = os.path.basename(log["file"])
            wl = os.path.join(folder, base)
            text = read(wl)
            # the inputs LINE names a block (B14): a paragraph wrapped for file width — `w:reads` on
            # line 1, the atoms and `w:adds` on lines 2–3 — is one declaration (daisy F-02)
            lineno, line = T.marked_block(text, W_KEY_RE)
            if line is None:
                legacy += 1
                continue
            keys = W_KEY_RE.findall(line)
            for k in sorted(set(keys) - set(W_FIELDS)):
                warn("P2 [%s] %s/%s:%d: unknown inputs-line key `w:%s` — the two are `w:reads` and "
                     "`w:adds` (worklog-skeleton)" % (name, step, base, lineno, k))
            for k in (set(W_FIELDS) - set(keys)):
                warn("P2 [%s] %s/%s:%d: inputs line is half-keyed — missing `w:%s`; both keys or "
                     "none (worklog-skeleton)" % (name, step, base, lineno, k))
            reads_val = _w_value(line, "reads") or ""
            adds_val = _w_value(line, "adds") or ""
            if "<" in reads_val + adds_val:
                warn("P2 [%s] %s/%s:%d: the inputs line still holds a template placeholder — copy "
                     "the card's `reads:` at pass time (worklog-skeleton)" % (name, step, base, lineno))
                continue
            atoms = [a.strip() for a in re.split(r"[·,]", reads_val) if a.strip()]
            defects = C.atom_errors("reads", atoms)
            for d in defects:
                warn("P2 [%s] %s/%s:%d: %s (card-schema → One atom grammar)"
                     % (name, step, base, lineno, d))
            if defects:
                continue
            adds = [a.strip() for a in re.split(r"[·,]", adds_val) if a.strip()
                    and ":" in a and not a.startswith("<")]
            perimeter = [C.split_atom(a) for a in atoms + adds]
            declared = {"%s:%s" % (h, a) for h, a in perimeter}
            allowed_anchors = {arg for head, arg in perimeter if head == "section"}
            allowed_anchors |= set(C.sections_written(_card_atoms(tool, inst, "writes")))
            allowed_anchors.add("intake")
            any_section = "*" in allowed_anchors
            allowed_regs = {arg for head, arg in perimeter if head == "register"}
            # the text of every declared door: an id that travels inside a quoted line of a declared
            # section (daisy F-03) or a declared foreign worklog is that door's, not a leak
            door_text = "".join(section_text.get(a, "") for a in allowed_anchors)
            for head, arg in perimeter:
                if head == "worklog" and "/" in arg:
                    fstep, ftool = arg.split("/", 1)
                    door_text += (snap["worklogs"].get(fstep, {}).get(ftool) or {}).get("body", "")
            region = _primary_region(text)
            # a table row whose source cell names a declared atom quotes that door (hub F-09): the
            # ids inside it are provenance, not readings — drop the row before reading citations
            kept = []
            for ln in region.split("\n"):
                if ln.strip().startswith("|"):
                    first = T.clean_cell(ln.strip().strip("|").split("|")[0])
                    if first in declared or (first.startswith("section:") and any_section):
                        continue
                kept.append(ln)
            region = _live("\n".join(kept))     # ids inside inline code / fences are not citations
            if not any_section:
                for a in sorted(set(ANCHOR_CITE_RE.findall(region)) - allowed_anchors):
                    warn("P2 [%s] %s/%s: cites `#%s` outside the inputs line — a citation names its "
                         "door: the card's `reads` (`section:%s`) or a recorded supplement (`w:adds`)"
                         % (name, step, base, a, a))
            cited = set(REG_ID_CITE_RE.findall(region)) | set(T.METRIC_RE.findall(region))
            leaks = {}
            for cid in sorted(cited):
                fam = cid[0]
                covered = ({"metrics", "metric-tree"} & allowed_regs if fam == "M"
                           else ID_FAMILY[fam] in allowed_regs)
                if covered or "*" in allowed_regs or cid in door_text:
                    continue
                leaks.setdefault(fam, []).append(cid)
            for fam, ids in sorted(leaks.items()):
                reg = "metrics" if fam == "M" else ID_FAMILY[fam]
                warn("P2 [%s] %s/%s: cites %s but `register:%s` is not on the inputs line and none "
                     "of them is quoted from a declared section — declare the register in the "
                     "card's `reads`, or record the supplement (`w:adds`)"
                     % (name, step, base, ", ".join("`%s`" % i for i in ids[:5]), reg))
    if legacy:
        warn("P2 [%s] %d worklog(s) predate the `**Inputs:**` line — a new worklog copies it from "
             "the skeleton; a rework pass adds it (worklog-skeleton)" % (name, legacy))


QUESTION_TYPES = {"free_text", "list", "per_item", "single_select", "multi_select"}


def check_questions(tools):
    """Y — questions.yaml is machine-readable: every question `type` is from the shared vocabulary.

    Donated skills arrived with `type: single_select_from: x` — a second `:` inside a plain scalar,
    which is invalid YAML — and the interview silently died at run time. A check costs nothing;
    unifying the vocabulary itself stays a method decision (this only holds the fence).
    """
    for name, t in sorted(tools.items()):
        q = os.path.join(t["dir"], "questions.yaml")
        if not os.path.exists(q):
            continue
        for i, line in enumerate(read(q).splitlines(), 1):
            m = re.match(r"\s*type:\s*([^#]+?)\s*(#.*)?$", line)
            if not m:
                continue
            val = m.group(1).strip()
            if ":" in val:
                err("Y [%s] questions.yaml:%d `type: %s` — a second `:` in a plain scalar is invalid "
                    "YAML; spell it `type: single_select` + `from: <question-id>` (or `options: [...]`)"
                    % (name, i, val))
            elif val not in QUESTION_TYPES:
                err("Y [%s] questions.yaml:%d unknown question type `%s` (allowed: %s)"
                    % (name, i, val, ", ".join(sorted(QUESTION_TYPES))))


def check_single_step(tools):
    """U — a library method serves exactly one step.

    A skill that did different operations on different steps (build the tree at 4, pick the period
    targets at 5) was two methods wearing one name; the 2026-08 rework cut every such skill apart.
    This keeps the seam from growing back: the same operation revisited at another step is a
    separate `<name>-<step>` skill, a different operation is a differently named one (EXTENDING.md).
    """
    for name, t in sorted(tools.items()):
        steps = T.as_list(t["fm"].get("steps"))
        if len(steps) != 1:
            err("U [%s] steps %s — a library method serves exactly one step; a second step "
                "is a second skill (see EXTENDING.md)" % (name, steps))


def check_reachable(tools):
    """U2 — every library method is named by at least one step-template marker.

    The law of ranks makes the marker the ONLY way a method is ever reached — a method is never a
    routing target (goal-map). So a method no `<!-- tool: … -->` names is dead code with a card:
    no pass can legally arrive at it, and the gap is invisible until someone wonders why a skill is
    never used. A contributing method (no section of its own) is named SECOND in its receiving
    section's marker — reach and rank both hold.
    """
    named = set()
    for path in sorted(glob.glob(os.path.join(ROOT, "steps", "*", "template.md"))):
        for m in TOOL_MARK_RE.findall(read(path)):
            named.update(t.strip() for t in m.split(","))
    for name in sorted(tools):
        if name not in named:
            err("U2 [%s] no step template's `<!-- tool: … -->` marker names this method — by the "
                "law of ranks it is unreachable; name it (second, if contributing) in its receiving "
                "section's marker" % name)


def check_status_tools(tools):
    """V — a status may only recommend a tool that has a home at that step.

    For a library method that means a `<!-- tool: ... -->` marker in that step's template. A
    recommendation with no section to land in forces the agent to invent one or stall (the
    segment-cvp failure: three statuses recommended it at steps 1 and 3, its section lived at 5).
    """
    step_tools = {}
    for tpl in glob.glob(os.path.join(ROOT, "steps", "[1-6]-*", "template.md")):
        n = os.path.basename(os.path.dirname(tpl))[0]
        names = set()
        for m in TOOL_MARK_RE.findall(read(tpl)):
            names.update(x.strip() for x in m.split(","))
        step_tools[n] = names
    other = {}
    for plane, fname in (("operations", "SKILL.md"), ("outputs", "SKILL.md")):
        for p in glob.glob(os.path.join(ROOT, "tool-skills", plane, "*", fname)):
            other[os.path.basename(os.path.dirname(p))] = plane
    for st in F.statuses(ROOT):
        for step, block in sorted(st["per_step"].items()):
            for tool in T.as_list((block or {}).get("tools")):
                if tool in tools:
                    if tool not in step_tools.get(step, set()):
                        err("V [%s] step %s recommends `%s` but steps/%s-*/template.md has no "
                            "`<!-- tool: %s -->` marker — a recommendation with no home section"
                            % (st["name"], step, tool, step, tool))
                elif tool in other:
                    err("V [%s] step %s recommends `%s` — an %s skill in a library tools list; "
                        "status tools are library methods only, how data is gathered belongs in "
                        "the goals prose (OPERATING-LOOP step 2)" % (st["name"], step, tool, other[tool]))
                else:
                    err("V [%s] step %s recommends unknown tool `%s` — no such skill folder"
                        % (st["name"], step, tool))


def check_register_tables(inst):
    """J — a register's table is one table, not one split by a stray blank line.

    The reader stitches the halves back together (see loops.text.tables), so nothing is lost — but a
    split table renders as two in markdown and is a live trap for the next hand that edits it.
    """
    name = rel(inst)
    for path in sorted(glob.glob(os.path.join(inst, "registers", "*.md"))):
        for t in T.tables(read(path)):
            if t["broken"]:
                warn("J [%s] %s: table at line %d is split by a blank line — remove it (the halves "
                     "are read as one table, but markdown renders two)"
                     % (name, os.path.basename(path), t["line"]))


REGISTER_ID_RE = re.compile(r"\b(?:H-\d+|R-\d+|F-\d+|S-\d+|M-[a-z0-9][a-z0-9-]*)\b")


def check_register_ids(inst):
    """K — an `id` cell names exactly one register item.

    Three ids sharing one definition row (`M-dau / M-wau / M-mau`) is the compound-enum disease one
    column over: every reference and every `metrics.csv` series can only reach the first, so the
    other two point at nothing while the register looks complete.
    """
    name = rel(inst)
    for filename in ("hypotheses.md", "risks.md", "metric-tree.md", "features.md", "surfaces.md"):
        path = os.path.join(inst, "registers", filename)
        if not os.path.exists(path):
            continue
        text = read(path)
        cells = T.column_key_values(text, "id")
        if cells is None:  # a not-yet-keyed legacy register — header prose is the fallback
            cells = T.table_column(text, "id")
        for v in (cells or []):
            ids = REGISTER_ID_RE.findall(T.clean_cell(v))
            if len(ids) > 1:
                err("K [%s] %s: id cell `%s` names %d ids — one row is one item, so only `%s` is "
                    "reachable and the rest have no definition; split it into %d rows (they may "
                    "repeat the definition text)"
                    % (name, filename, T.clean_cell(v), len(ids), ids[0], len(ids)))


FS_ID_RE = re.compile(r"\b([FS]-\d+)\b")


def _fs_defined(inst):
    """The F-/S- ids the feature register defines, or None if neither file exists yet."""
    reg = os.path.join(inst, "registers")
    found_any, ids = False, set()
    for filename in ("features.md", "surfaces.md"):
        path = os.path.join(reg, filename)
        if not os.path.exists(path):
            continue
        found_any = True
        text = read(path)
        cells = T.column_key_values(text, "id")
        if cells is None:  # a not-yet-keyed legacy register — header prose is the fallback
            cells = T.table_column(text, "id")
        for v in (cells or []):
            ids.update(FS_ID_RE.findall(T.clean_cell(v)))
    return ids if found_any else None


def check_feature_refs(inst):
    """E2 — cited F-…/S-… ids resolve to a register row (the feature mirror of check E).

    A citation with no definition row is a typo, a row deleted without retiring its references, or
    an id minted in prose instead of the register (only the orchestrator mints ids).
    """
    name = rel(inst)
    defined = _fs_defined(inst)
    files = sorted(glob.glob(os.path.join(inst, "[1-6]-*.md")))
    files += sorted(glob.glob(os.path.join(inst, "registers", "*.md")))
    for path in files:
        base = os.path.basename(path)
        if base in ("features.md", "surfaces.md"):
            continue  # definitions themselves are checked by D/K
        # the change log is history — ids there may legitimately predate a rename or the register
        # (the heading is a fixed machine-read literal, but match it case-insensitively)
        text = T.without_change_log(read(path))
        cited = sorted(set(FS_ID_RE.findall(text)))
        for cid in cited:
            if defined is None:
                warn("E2 [%s] %s cites `%s` but the instance has no features.md/surfaces.md — "
                     "mint the row first (register-skeletons/), then reference it" % (name, base, cid))
                break  # one warn per file is enough when the register is absent
            if cid not in defined:
                warn("E2 [%s] %s cites `%s` with no definition row in %s — a typo, or an id minted "
                     "outside the register" % (name, base, cid,
                                               "features.md" if cid.startswith("F-") else "surfaces.md"))


ITEM_HEAD_RE = re.compile(r"^\*\*(?:\d+|[FAT]-\d+)\s*·\s*(.+?)\*\*", re.M)


def check_item_features(inst):
    """E3 — a worked must-item at pmf/growth carries its full pre-registration.

    The item number is sprint-local; the `Feature:` line is its only cross-sprint identity — an
    item without one ships work the next impact-readout cannot find. The same readout also needs
    the item's `Expected impact` (with a check-by) and `Estimate` pre-registered — the gate line
    (`item-feature`) names all three, so the check does too. The backlog table's Feature column is
    the same identity one section over. Every status: setup births the registers, the specs mint
    `planned` rows at any stage — a concept-viability sprint pre-registers like any other.
    """
    name = rel(inst)
    path = os.path.join(inst, "6-sprint-plan.md")
    if not os.path.exists(path):
        return
    for sec in T.sections(read(path)):
        if sec["id"] != "backlog":
            continue
        feats = T.column_key_values(sec["body"], "feature")
        items = T.column_key_values(sec["body"], "item") or []
        for i, cell in enumerate(feats or []):
            item = T.clean_cell(items[i]) if i < len(items) else ""
            if "<" in item or item in ("", "…"):
                continue  # template sample row, not a worked one
            cell = T.clean_cell(cell)
            if not (FS_ID_RE.search(cell) or T.TO_CLARIFY_RE.search(cell)):
                warn("E3 [%s] 6-sprint-plan.md#backlog row `%s`: Feature cell names neither an "
                     "`F-…` row nor a declared `— to clarify —` gap — a candidate without an id "
                     "cannot re-enter a later ranking" % (name, item))
    # the must-items as the read layer parses them (instance._sprint_items) — one item parser for
    # the console's step-6 board and this check
    for it in _snapshot(inst)["sprint_items"]:
        item_name = it["name"]
        if "<" in item_name:
            continue  # template placeholder, not a worked item
        fields = {k.strip().lower(): v for k, v in it["fields"]}
        if "feature" not in fields:
            warn("E3 [%s] 6-sprint-plan.md#must item `%s` has no `- **Feature:** F-…` line — "
                 "every item names the register row it advances" % (name, item_name))
        elif not (FS_ID_RE.search(fields["feature"]) or T.TO_CLARIFY_RE.search(fields["feature"])):
            warn("E3 [%s] 6-sprint-plan.md#must item `%s`: the `**Feature:**` line names "
                 "neither an `F-…` row nor a declared `— to clarify —` gap — a placeholder "
                 "is not an identity" % (name, item_name))
        if "expected impact" not in fields:
            warn("E3 [%s] 6-sprint-plan.md#must item `%s` pre-registers no `**Expected "
                 "impact:**` — the next impact-readout has nothing to read the shipped work "
                 "against" % (name, item_name))
        elif "check-by" not in fields["expected impact"].lower():
            warn("E3 [%s] 6-sprint-plan.md#must item `%s`: Expected impact carries no "
                 "`check-by` — without a read-date the readout can neither read it nor call it "
                 "`pending`" % (name, item_name))
        if "estimate" not in fields:
            warn("E3 [%s] 6-sprint-plan.md#must item `%s` pre-registers no `**Estimate:**` — "
                 "the readout's calibration read (est → actual) has no baseline"
                 % (name, item_name))


def check_register_sources(inst):
    """E4 — a feature/surface row shows where it came from.

    The register is an inventory read from sources (a walkthrough, analytics, the codebase) — a
    row with an empty `source` is a memory posing as evidence (product-baseline's first rule).
    """
    name = rel(inst)
    for filename in ("features.md", "surfaces.md"):
        path = os.path.join(inst, "registers", filename)
        if not os.path.exists(path):
            continue
        text = read(path)
        ids = T.column_key_values(text, "id") or []
        srcs = T.column_key_values(text, "source") or []
        for rid, src in zip(ids, srcs):
            rid = T.clean_cell(rid)
            if not FS_ID_RE.fullmatch(rid):
                continue  # placeholder row of a fresh skeleton
            if T.clean_cell(src) in ("", "…", "—"):
                warn("E4 [%s] %s row `%s` has an empty source — name where the row was read from "
                     "(a walkthrough, analytics, the codebase passport)" % (name, filename, rid))


SERVES_ID_RE = re.compile(r"\b(H-\d+|R-\d+|F-\d+|S-\d+|M-[a-z0-9][a-z0-9-]*)\b")
_SERVES_HOME = {"H": "hypotheses.md", "R": "risks.md", "M": "metric-tree.md",
                "F": "features.md", "S": "surfaces.md"}


def _register_id_set(inst, filename):
    """All ids a register file defines, or None if the file does not exist."""
    path = os.path.join(inst, "registers", filename)
    if not os.path.exists(path):
        return None
    text = read(path)
    cells = T.column_key_values(text, "id")
    if cells is None:
        cells = T.table_column(text, "id")
    out = set()
    for v in (cells or []):
        out.update(SERVES_ID_RE.findall(T.clean_cell(v)))
    return out


def check_serves_links(inst):
    """E5 — every id a features.md `serves` cell cites resolves to a row in its own register.

    `serves` is the load-bearing link ("a feature serving nothing is a candidate to cut", and the
    readout writes its verdict onto it) — a typo'd id silently detaches the feature from the
    metric/hypothesis/risk it claims to move, and no downstream reader notices.
    """
    name = rel(inst)
    path = os.path.join(inst, "registers", "features.md")
    if not os.path.exists(path):
        return
    defined = {fam: _register_id_set(inst, fn) for fam, fn in _SERVES_HOME.items()}
    text = read(path)
    ids = T.column_key_values(text, "id") or T.table_column(text, "id") or []
    serves = T.column_key_values(text, "serves") or T.table_column(text, "serves") or []
    for rid, cell in zip(ids, serves):
        rid = T.clean_cell(rid)
        if not FS_ID_RE.fullmatch(rid):
            continue  # placeholder row of a fresh skeleton
        for cited in SERVES_ID_RE.findall(T.clean_cell(cell)):
            home = defined.get(cited[0])
            if home is None:
                continue  # that register file is absent — E2/E4 surface that, not this check
            if cited not in home:
                warn("E5 [%s] features.md row `%s` serves `%s` with no such row in %s — a typo, or "
                     "an id minted in prose" % (name, rid, cited, _SERVES_HOME[cited[0]]))


CONFIG_REQUIRED = ("product", "language", "active_status", "directions")
CONFIG_OPTIONAL = ("scope_note", "metric_source_slots", "sources", "products", "delegation")
CONFIG_BANNED = {"metric_sources": "metric_source_slots", "metric_slots": "metric_source_slots",
                 "product_scope": "scope_note", "scope": "scope_note", "lang": "language",
                 "title": "product", "name": "product", "status": "active_status",
                 "sources_dir": "sources"}


def check_decisions(inst):
    """E6 — a cited decision id resolves to a row of the instance's `decisions.md`.

    A dated human decision is a legal `[sourced:]` origin (CONVENTIONS → Sources) and its home is the
    instance's `decisions.md` (node-type-matrix → `decisions`): one dated row per decision, `D-…` ids.
    Before that home existed a run kept its decisions in a journal outside the instance, and the
    `[sourced: acting PO decision D-16]` tags pointed where no verify could read (decksmith F-11) —
    half the load-bearing claims of a step rested on a source inside nobody's perimeter. WARN: the
    id grammar is shared with nothing else, but a prose `D-…` can still be a quoted label.
    """
    name = rel(inst)
    files = sorted(glob.glob(os.path.join(inst, "[1-6]-*.md")))
    for folder in sorted(glob.glob(os.path.join(inst, "[1-6]-*"))):
        if os.path.isdir(folder):
            files.extend(sorted(glob.glob(os.path.join(folder, "*.md"))))
    handoff = os.path.join(inst, "HANDOFF.md")
    if os.path.exists(handoff):
        files.append(handoff)
    cited = {}
    for path in files:
        for did in T.DECISION_RE.findall(_live(read(path))):
            cited.setdefault(did, os.path.relpath(path, inst))
    if not cited:
        return
    home = os.path.join(inst, "decisions.md")
    if not os.path.exists(home):
        warn("E6 [%s] %d decision id(s) cited (%s) but the instance has no decisions.md — the home of a "
             "dated human decision is the instance's decisions.md, one `D-…` row each, so a "
             "`[sourced: decision D-…]` tag points where a verify can read (CONVENTIONS → Sources; "
             "reference/register-skeletons/decisions.md)"
             % (name, len(cited), ", ".join("`%s`" % d for d in sorted(cited)[:5])
                + (", …" if len(cited) > 5 else "")))
        return
    _, rows = T.table_rows(read(home), "ID")
    defined = set()
    for r in rows:
        defined.update(T.DECISION_RE.findall(r.get("id", "")))
    for did in sorted(cited):
        if did not in defined:
            warn("E6 [%s] %s cites `%s`, which has no row in decisions.md — a decision a tag names "
                 "is a row (id · date · by · where · decision · why), or the claim rests on a memory "
                 "(CONVENTIONS → Sources)" % (name, cited[did], did))


def check_config(inst):
    """H — the instance config follows the pinned schema (CONVENTIONS → Instance config)."""
    name = rel(inst)
    path = os.path.join(inst, "config.yaml")
    if not os.path.exists(path):
        # a sub-product of a multi-product instance inherits the parent's config — that is canon
        parent = os.path.join(os.path.dirname(inst), "config.yaml")
        if not os.path.exists(parent):
            err("H [%s] no config.yaml, and no parent instance to inherit one from" % name)
        return
    data, _skipped = yamlite.load(path)      # unsupported lines are check Y2's, with a reason each
    for key in CONFIG_REQUIRED:
        if data.get(key) in (None, "", [], {}):
            err("H [%s] config.yaml is missing required key `%s`" % (name, key))
    for key in data:
        if key in CONFIG_BANNED:
            err("H [%s] config.yaml uses `%s` — the canon key is `%s` (one spelling, no aliases)"
                % (name, key, CONFIG_BANNED[key]))
        elif key not in CONFIG_REQUIRED and key not in CONFIG_OPTIONAL:
            warn("H [%s] config.yaml has non-schema key `%s` — allowed, but no tool may depend on it"
                 % (name, key))
    # Value shapes — each learned from a live local-model run that passed the key-presence check
    # while writing values no tool can read (config-schema.md is the authority for all three).
    lang = data.get("language")
    if isinstance(lang, str) and lang and not re.fullmatch(r"[a-z]{2,3}(-[A-Za-z]{2})?", lang):
        err("H [%s] config.yaml `language: %s` is not a language code — the schema takes codes "
            "(`ru`, `en`), which tools compare; a word written in some language is exactly what "
            "the code exists to avoid" % (name, lang))
    dirs = data.get("directions")
    if dirs not in (None, "", [], {}) and not isinstance(dirs, list):
        err("H [%s] config.yaml `directions` is a single string — the schema takes a list "
            "(one `- <stream>` per line); a comma-joined string reads as ONE direction" % name)
    status = data.get("active_status")
    if isinstance(status, str) and status:
        known = {os.path.basename(p)[:-3].split("-", 1)[1]
                 for p in glob.glob(os.path.join(ROOT, "statuses", "[0-9]*-*.md"))}
        if known and status not in known:
            err("H [%s] config.yaml `active_status: %s` names no status file — statuses/ holds: %s"
                % (name, status, " / ".join(sorted(known))))


# The artifact frontmatter schema is the step template's own frontmatter (`artifact-template` ->
# `artifact`); status/version/updated ride along like on every framework file.
ARTIFACT_FM_KEYS = ("node_type", "artifact", "step", "title", "status", "version", "updated")
ARTIFACT_FM_HOMES = {
    "worklog": "worklogs are named by each section's `<!-- tool: … -->` marker and live in the "
               "step folder (check P) — a frontmatter list is a second home that drifts",
    "active_status": "the active status lives in config.yaml, never in an artifact",
    "confirmed": "confirmation is a per-section `<!-- confirmed: -->` marker, not a frontmatter key",
}


def check_artifact_frontmatter(inst):
    """H2 — an instance artifact's frontmatter carries the template's keys and invents none.

    Gate ids are `<artifact>#<section>`, so a file that drops `artifact`/`step` unhooks its own
    ticks; and an invented key (seen live: a `worklog:` list that immediately went stale against
    the folder) is a second home for something the canon already stores elsewhere. Off-schema keys
    WARN with the canon home where one is known.
    """
    name = rel(inst)
    for art in sorted(glob.glob(os.path.join(inst, "[1-6]-*.md"))):
        fm, _ = T.frontmatter(art)
        if fm.get("node_type") != "artifact":
            # A file wearing an artifact's name with no artifact passport is worse than a wrong
            # one: the loader skips it entirely, so the steps view, the console and check G2 are
            # all blind to it while the content checks (O2, P) still read it — a half-existing
            # artifact (live-run finding: a weak model wrote 1-concept.md with no frontmatter and
            # every structural check went silent).
            err("H2 [%s] %s wears an artifact's name but its frontmatter never says "
                "`node_type: artifact` — the loader skips the file, so the steps view, the console "
                "and the gate checks are blind to it; add the template's frontmatter "
                "(node_type/artifact/step)" % (name, os.path.basename(art)))
            continue
        base = os.path.basename(art)
        for key in ("artifact", "step"):
            if fm.get(key) in (None, ""):
                err("H2 [%s] %s frontmatter is missing `%s` — gate ids are `<artifact>#<section>`, "
                    "so without it no tool can key this file's ticks" % (name, base, key))
        for key in fm:
            if key not in ARTIFACT_FM_KEYS:
                hint = ARTIFACT_FM_HOMES.get(
                    key, "no tool reads it, and an invented key is a second home for something "
                         "the canon stores elsewhere")
                warn("H2 [%s] %s frontmatter has off-schema key `%s` — %s" % (name, base, key, hint))


def check_install(checked):
    """I2 — a vendored framework is pinned and pointed at (install/README -> Acceptance).

    Detected by layout, not by flag. The canon layout is the vendored framework AT the product repo's
    root with the instance beside its folders (`product-loops/`); a framework in a sub-folder of the
    product repo is still read. Either way the install's two machine-checkable debts become errors:
    the FRAMEWORK-VERSION pin at the vendor root (tag AND commit SHA — without it nobody can say what
    version the instance runs on), and the pointer in the product repo's root AGENTS.md (what makes a
    plain "continue the strategy" land in the loop instead of an ad-hoc bulk fill). The framework's
    own dev repo (it ships `examples/`) is not an install and stays silent.
    """
    root_abs = os.path.abspath(ROOT)
    dev_repo = os.path.isdir(os.path.join(root_abs, "examples"))   # the framework's own repo ships examples/
    seen = set()
    for inst in checked:
        ia = os.path.abspath(inst)
        repo = os.path.dirname(ia)
        if repo in seen or repo in ("", os.sep):
            continue
        seen.add(repo)
        # the canon layout (install/README -> What lands in your repo): the vendored framework IS the
        # product repo's root and the instance sits beside its folders (`product-loops/`). The
        # framework's own dev repo (examples/ present) is not an install and stays silent. A legacy
        # layout — framework in a sub-folder of the product repo — is still read.
        if repo == root_abs:
            if dev_repo:
                continue
        elif not root_abs.startswith(repo + os.sep) or ia.startswith(root_abs + os.sep):
            continue
        tag = rel(inst)
        pin = os.path.join(root_abs, "FRAMEWORK-VERSION")
        if not os.path.exists(pin):
            err("I2 [%s] the framework is vendored but has no FRAMEWORK-VERSION at the vendor root "
                "— write the pinned tag AND commit SHA (install/README -> Acceptance); without it "
                "nobody can say what version this instance runs on" % tag)
        elif not re.search(r"\b[0-9a-f]{7,40}\b", read(pin)):
            warn("I2 [%s] FRAMEWORK-VERSION names no commit SHA — tags can move or be deleted; "
                 "the SHA is the immutable anchor" % tag)
        agents = os.path.join(repo, "AGENTS.md")
        if not os.path.exists(agents):
            err("I2 [%s] no AGENTS.md at the product repo root (%s) — the install owes it the "
                "pointer into the framework (install/README -> point 1)" % (tag, rel(repo) or repo))
        else:
            body = read(agents)
            if "start-work" not in body:
                warn("I2 [%s] the root AGENTS.md never names `start-work` — without the pointer, "
                     "\"continue the strategy\" lands outside the loop" % tag)


def check_local_skills(inst):
    """I — a product's own skills (product-loops/tool-skills/…) obey the same wiring rules as vendored ones."""
    name = rel(inst)
    homed = F.homed_sections(ROOT)
    for plane in ("library", "operations"):
        for skill in sorted(glob.glob(os.path.join(inst, "tool-skills", plane, "*", "SKILL.md"))):
            d = os.path.dirname(skill)
            local = os.path.basename(d)
            fm, _ = T.frontmatter(skill)
            if "writes" not in fm:
                err("I [%s] local card `%s` declares no `writes`" % (name, local))
            secs = C.sections_written(T.as_list(fm.get("writes")))
            frag = os.path.join(d, "template-fragment.md")
            frag_ids = T.section_ids(read(frag)) if os.path.exists(frag) else set()
            for sid in secs:
                if sid not in homed:
                    err("I [%s] local card `%s` writes `section:%s` with no home in any step "
                        "template" % (name, local, sid))
                if sid not in frag_ids:
                    err("I [%s] local card `%s` writes `section:%s` but its template-fragment.md "
                        "has no {#%s}" % (name, local, sid, sid))
            if not T.as_list(fm.get("steps")):
                warn("I [%s] local card `%s` names no `steps` — no step reaches it" % (name, local))


def check_links():
    roots = ["process", "steps", "statuses", "tool-skills", "examples", "README.md"]
    for r in roots:
        base = os.path.join(ROOT, r)
        paths = [base] if os.path.isfile(base) else glob.glob(base + "/**/*.md", recursive=True)
        for p in paths:
            if "/.git/" in p:
                continue
            # a `[[...]]` inside a fenced block is not a wiki-link — a Mermaid subroutine node
            # is written `SYS[[label]]`. Strip fences first (cf. check_schema_not_confirmed).
            live = re.sub(r"```.*?```", "", read(p), flags=re.S)
            hits = T.LINK_RE.findall(live)
            if hits:
                err("F %s: %d GitMark-lite [[...]] link(s) — canon is relative path + {#anchor}: %s"
                    % (rel(p), len(hits), ", ".join(sorted(set(hits))[:5])))


def _file_keyed_tables(text):
    """(headers, keys) for every table in `text` that carries at least one column key."""
    out = []
    for t in T.tables(text):
        keys = T.column_keys(t["headers"])
        if any(keys):
            out.append((t["headers"], keys))
    return out


def _section_keys(text):
    """{section_id: [keys]} — keys of the first keyed table found in each identified section."""
    out = {}
    for sec in T.sections(text):
        if not sec["id"]:
            continue
        for t in T.tables(sec["body"]):
            keys = T.column_keys(t["headers"])
            if any(keys):
                out[sec["id"]] = [k for k in keys if k]
                break
    return out


# a template-declared column vocabulary: `<!-- enum:c:inaction: a | b | c -->` under the table
ENUM_DECL_RE = re.compile(r"<!--\s*enum:c:([\w-]+):\s*([^>]*?)\s*-->", re.I)


def _section_enums(text):
    """{section_id: {key: (tokens…)}} — the enum vocabularies a step template declares per section."""
    out = {}
    for sec in T.sections(text):
        if not sec["id"]:
            continue
        for m in ENUM_DECL_RE.finditer(sec["body"]):
            toks = tuple(t.strip() for t in m.group(2).split("|") if t.strip())
            out.setdefault(sec["id"], {})[m.group(1)] = toks
    return out


def _template_section_enums():
    def make():
        out = {}
        for path in sorted(glob.glob(os.path.join(ROOT, "steps", "*", "template.md"))):
            out.update(_section_enums(read(path)))
        return out
    return _memo("enums", make)


SCHEMA_FILES = ("steps/*/template.md",
                "tool-skills/library/*/template-fragment.md",
                "tool-skills/operations/*/template-fragment.md")


def check_column_keys():
    """O — column keys live only on the step template (the form of record), and are well-formed there.

    Column keys (CONVENTIONS → Column keys) are what lets a reader find a table column without
    matching its (translatable, reorderable) header prose — the fix for the "every cell is a dash"
    failure on a non-English instance. They have exactly **three homes**: the **step template** (the
    chistovik's form of record, = the interface 1:1), the **instance** section that carries it (check
    O2), and the instance **registers** (read by the console). A method's template (`template-fragment.md`)
    is the *draft's* shape — it may be wider than the chistovik and is adapted into the fixed form by
    the orchestrator, which matches columns by meaning, not by key. So a key in a method template is
    dead weight and a live break risk (every new skill would have to keep it in sync with nothing
    consuming it) — it is therefore an **error**, not a schema to maintain.

    On the step templates this holds the shape a key needs to be trustworthy: a table is all-keyed or
    none (a half-keyed header is the ambiguity the key removes), and keys are unique within a table.
    """
    # Home 1 — step templates: well-formed keyed tables.
    for path in sorted(glob.glob(os.path.join(ROOT, "steps", "*", "template.md"))):
        text = read(path)
        for headers, keys in _file_keyed_tables(text):
            unkeyed = [h for h, k in zip(headers, keys) if not k]
            if unkeyed:
                err("O %s: a column-keyed table leaves %d header(s) unkeyed (%s) — a table is "
                    "all-keyed or none (CONVENTIONS → Column keys)"
                    % (rel(path), len(unkeyed), ", ".join(T.plain(h) or "∅" for h in unkeyed)))
            present = [k for k in keys if k]
            dupes = sorted({k for k in present if present.count(k) > 1})
            if dupes:
                err("O %s: column key(s) %s repeat in one table — keys are unique within a table"
                    % (rel(path), ", ".join("`%s`" % d for d in dupes)))
        # an enum declaration binds to a key its section's table actually carries (O3 reads these)
        skeys = _section_keys(text)
        for sid, enums in _section_enums(text).items():
            for key, toks in enums.items():
                if not toks:
                    err("O %s#%s: `enum:c:%s` declares no tokens — an empty vocabulary checks "
                        "nothing" % (rel(path), sid, key))
                if key not in skeys.get(sid, []):
                    err("O %s#%s: `enum:c:%s` but the section's table carries no `<!--c:%s-->` "
                        "column — a vocabulary binds to a real key" % (rel(path), sid, key, key))
    # Not a home — method templates: a key here is a maintenance trap with no consumer.
    for pattern in ("tool-skills/library/*/template-fragment.md",
                    "tool-skills/operations/*/template-fragment.md"):
        for path in sorted(glob.glob(os.path.join(ROOT, pattern))):
            if any(_file_keyed_tables(read(path))):
                err("O %s: a method template carries a column key — keys live on the step template "
                    "(the chistovik's form of record), never here; the draft is matched by meaning "
                    "(CONVENTIONS → Column keys)" % rel(path))


def _template_section_keys():
    """{section_id: [keys]} — the column keys each step template declares, the form of record.

    A section id is homed in exactly one step template (CONVENTIONS → section anchors), so a flat map
    across all templates has no collisions.
    """
    def make():
        out = {}
        for path in sorted(glob.glob(os.path.join(ROOT, "steps", "*", "template.md"))):
            out.update(_section_keys(read(path)))
        return out
    return _memo("keys", make)


def _steps():
    """The steps as the read layer parses them, once per run."""
    return _memo("steps", lambda: F.steps(ROOT))


def _is_framework_example(inst):
    """The framework's own reference instances (`examples/` in the dev repo). They are held to ERROR
    on template shape — they ARE the form. A product instance that vendored the framework gets WARN:
    a template that moved under a filled instance is visible debt, not a blocker (install/UPDATE.md)."""
    p = os.path.abspath(inst)
    return any(p.startswith(os.path.abspath(r) + os.sep) for r in EXAMPLE_ROOTS)


def check_instance_conformance(inst):
    """O2 — an instance's artifact section carries its template's column keys (the projection contract).

    The chistovik (an instance artifact section) and the interface that renders it are one form, and
    that form is the **step template's** (CONVENTIONS → Column keys). So a section the template keys
    must, in the instance, be present and carry exactly those keys — no more, no less: the draft may be
    wider, the chistovik may not. **Enforced**: a template-keyed section that the instance leaves
    un-keyed is flagged, because the console reads by key and cannot render an un-keyed table in any
    language. A step the instance has not reached (no artifact file) is simply not iterated.
    """
    tkeys = _template_section_keys()
    tenums = _template_section_enums()
    shape = err if _is_framework_example(inst) else warn
    debt = "" if _is_framework_example(inst) else (
        " — a template that moved under a filled instance is visible debt, not a blocker: re-project "
        "the section as an ordinary pass (install/UPDATE.md)")
    worked = _worked_sections(inst)
    for art in sorted(glob.glob(os.path.join(inst, "[1-6]-*.md"))):
        text = read(art)
        step = int(os.path.basename(art).split("-", 1)[0])
        bodies = {sec["id"]: sec["body"] for sec in T.sections(text) if sec["id"]}
        present = set(bodies)
        inst_keys = _section_keys(text)   # {sid: [keys]} for keyed instance tables only
        na = {sid for (st, sid) in _na_sections(inst)
              if str(st) == os.path.basename(art)[0]}
        for sid, tks in tkeys.items():
            if sid not in present:
                continue                  # section not in this artifact (or step not reached)
            if sid in na or (step, sid) not in worked:
                continue                  # skipped (`n/a` tick) or an untouched shell — no projection owed
            iks = inst_keys.get(sid)
            if iks is None:
                shape("O2 %s#%s: the template keys this section but the instance carries no column keys — "
                      "the chistovik must carry its template's form so the console reads it by key "
                      "(CONVENTIONS → Column keys)%s" % (rel(art), sid, debt))
            elif set(iks) != set(tks):
                shape("O2 %s#%s: instance table keys %s do not match the template's form %s — the "
                      "chistovik must carry its template's keys (CONVENTIONS → Column keys)%s"
                      % (rel(art), sid, sorted(iks), sorted(tks), debt))
        # O3 — a column with a template-declared vocabulary holds only its tokens. The template is
        # the schema (the same contract check D holds for registers): a truncated or improvised
        # token reads plausibly and slips through every human pass — this is the machine's catch.
        for sid, enums in tenums.items():
            body = bodies.get(sid)
            if body is None or (step, sid) not in worked:
                continue
            for key, toks in enums.items():
                for v in (T.column_key_values(body, key) or ()):
                    cv = T.enum_value(v)
                    if cv and cv not in toks:
                        shape("O3 %s#%s: `%s` = %r not in the template's enum %s — the template is "
                              "the schema; a qualifier belongs in a note or the worklog, never "
                              "compounded into the value%s" % (rel(art), sid, key, cv, sorted(toks), debt))


CONFIRM_LOOSE_RE = re.compile(r"<!--\s*confirmed:\s*(.*?)\s*-->")
CONTEST_LOOSE_RE = re.compile(r"<!--\s*contested:\s*(.*?)\s*-->")


def check_card_slots(tools, inst):
    """C2 (instance, WARN) — a fragment-declared card slot is honoured by the projected section.

    CONVENTIONS → Card line: the mark's canonical home is the method's template-fragment — a fragment
    carrying a live `<!-- card -->` has *declared the slot*, and every projection places the section's
    mark on that element. Whether the mark sits on the right element is a semantic judgement
    (step-close audits it); what a linter can see is the mark missing entirely — a face the method
    decided on and the instance does not show. A fragment with no slot imposes nothing: a mark there
    is projection judgement and an honestly faceless section is legal, so only declared-but-absent
    warns.
    """
    slotted, faces = set(), {}
    for name, t in tools.items():
        frag = os.path.join(t["dir"], "template-fragment.md")
        if os.path.exists(frag) and T.CARD_RE.search(_live(read(frag))):
            slotted.add(name)
            # the slot's machine-readable half: the bold label the fragment's face opens with. A
            # face with no label (`_<Product> is a …_`) declares only that a mark exists
            for sid, sec in ((s["id"], s) for s in T.sections(_live(read(frag))) if s["id"]):
                lead = T.card_line(sec["body"])
                lm = CARD_LABEL_RE.match(lead.strip()) if lead else None
                if lm:
                    faces[(name, sid)] = (_face_label(lm.group(1)), lm.group(1).strip(" .:"))
    if not slotted:
        return
    # labels are prose, and the fragment's is English: a translated instance (`language: ru`) is
    # matched by step-close's reading, never by a string compare that would flag every section
    match_labels = (_snapshot(inst).get("language") or "en").lower().startswith("en")
    worked = _worked_sections(inst)
    for art in sorted(glob.glob(os.path.join(inst, "[1-6]-*.md"))):
        step = int(os.path.basename(art).split("-", 1)[0])
        for sec in T.sections(read(art)):
            if not sec["id"] or (step, sec["id"]) not in worked:
                continue                                   # an unwritten shell owes no face yet
            m = TOOL_MARK_RE.search(sec["body"])
            if not m:
                continue
            primary = m.group(1).split(",")[0].strip()
            lead = T.card_line(sec["body"])
            if primary in slotted and lead is None:
                warn("C2 [%s] %s#%s: the %s fragment declares a card slot, but the section carries "
                     "no `<!-- card -->` mark — the face the method decided on once is not shown "
                     "(CONVENTIONS → Card line; projection step 3)"
                     % (rel(inst), os.path.basename(art), sec["id"], primary))
                continue
            declared, declared_text = faces.get((primary, sec["id"]), (None, None))
            if not (declared and lead and match_labels):
                continue
            lm = CARD_LABEL_RE.match(lead.strip())
            shown = _face_label(lm.group(1)) if lm else ""
            if shown != declared and not (shown and (shown in declared or declared in shown)):
                warn("C2 [%s] %s#%s: the `<!-- card -->` mark sits on %s, but the %s fragment declares "
                     "the slot on `**%s:**` — the mark drifted off its slot, so the board shows a "
                     "different face than the method decided on (CONVENTIONS → Card line; step-close "
                     "step 4)" % (rel(inst), os.path.basename(art), sec["id"],
                                  ("`**%s:**`" % lm.group(1).strip()) if lm else "an unlabelled block",
                                  primary, declared_text))


def _face_label(label):
    """A card face label reduced for comparison — case, emphasis, a trailing colon or period, and a
    parenthesised aside (`Moat read (concept)` ~ `Moat read`) do not make two faces."""
    s = re.sub(r"\s*\(.*$", "", T.plain(label)).strip().lower()
    return s.strip(" .:*_")


def check_schema_not_confirmed():
    """Q (schema) — a template or fragment must never ship a `confirmed`/`contested` marker.

    Both record a human's verdict on one instance's result (CONVENTIONS → Section confirmation). Baked
    into the schema every instance copies, they would pre-decide work nobody reviewed — the exact
    inversion of what the markers are for.
    """
    for pattern in SCHEMA_FILES:
        for path in sorted(glob.glob(os.path.join(ROOT, pattern))):
            # A fragment documents the markers inside a ``` example (that is its job); only a LIVE
            # marker in the schema body — outside any fence — would actually pre-decide an instance.
            live = re.sub(r"```.*?```", "", read(path), flags=re.S)
            for rx, word in ((CONFIRM_LOOSE_RE, "confirmed"), (CONTEST_LOOSE_RE, "contested")):
                if rx.search(live):
                    err("Q %s: ships a live `%s:` marker — a schema must not pre-decide an "
                        "instance's result (CONVENTIONS → Section confirmation)" % (rel(path), word))


def _confirm_date(raw):
    """The date token of a `confirmed:` payload, dropping an optional `by:<who>` suffix."""
    return raw.split()[0] if raw.split() else raw


def check_confirm_dates(inst):
    """Q (instance) — an artifact's `confirmed:` marker parses as a date, else it silently means pending.

    A malformed date is not a soft nit: the section reads as *pending* while its author believes it is
    signed, so the mismatch is silent and one-directional. Cheap and unambiguous to catch — an ERROR.
    """
    for art in sorted(glob.glob(os.path.join(inst, "[1-6]-*.md"))):
        text = read(art)
        for raw in CONFIRM_LOOSE_RE.findall(text):
            if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", _confirm_date(raw)):
                err("Q [%s] %s: `confirmed: %s` is not a YYYY-MM-DD date, so it reads as *pending* — "
                    "a typo silently un-confirms the section (CONVENTIONS → Section confirmation)"
                    % (rel(inst), os.path.basename(art), raw))
        # the date alone is not enough: the WHOLE marker must parse the way the read layer parses it,
        # or the section is pending while its author believes it is signed (J-09: a `by:` value the
        # regex refused voided the marker and this check stayed silent)
        for m in re.finditer(r"<!--\s*confirmed:[^>]*-->", _live(text)):
            if not T.CONFIRMED_RE.fullmatch(m.group(0)):
                err("Q [%s] %s: `%s` does not parse as a confirmation marker, so it reads as *pending* "
                    "— write `<!-- confirmed: YYYY-MM-DD by:<who> -->` (CONVENTIONS → Section confirmation)"
                    % (rel(inst), os.path.basename(art), m.group(0)))


D_KEY_RE = re.compile(r"<!--\s*d:([a-z0-9-]+)\s*-->")
D_LABEL_RE = re.compile(r"^\*\*Decided:\*\*", re.M)
D_FIELDS = ("date", "by", "alts")
D_BARE_NONE_RE = re.compile(r"^(none|none recorded|no alternatives|not considered|n/?a|нет|не рассматривались"
                            r"|—|-|\.\.\.|…)[.\s]*$", re.I)


def _live(s):
    """`s` with inline-code spans and fenced blocks removed — a *documented* marker is not a live one.

    The framework documents its own markers in prose (a change-log entry naming the keys it added, a
    reference file showing the shape). Reading those as live fields would make every explanation of
    the mechanism a defect in it — the same reasoning that makes check Q strip fences.
    """
    return re.sub(r"`[^`]*`", "``", re.sub(r"```.*?```", "", s, flags=re.S))


def _decision_blocks(text):
    """(line_no, block) for every paragraph carrying a *live* `d:` field key — the line and its wrap.

    The block ends at the first blank line, which is the parse rule the canon states (reference/
    column-keys.md → Decision-line field keys): `d:alts` is last and runs to the end of the block.
    The artifact's **change log** is cut first: it is the last section by convention (CONVENTIONS →
    Change logs) and it talks *about* sections, so a decision line never lives there.
    """
    text = T.without_change_log(text)
    lines = text.split("\n")
    out, i = [], 0
    while i < len(lines):
        if D_KEY_RE.search(_live(lines[i])):
            start = i
            while start > 0 and lines[start - 1].strip():   # back up to the paragraph's first line
                start -= 1
            end = i
            while end < len(lines) and lines[end].strip():
                end += 1
            out.append((start + 1, "\n".join(lines[start:end])))
            i = end
        else:
            i += 1
    return out


def _d_value(block, key, last=False):
    """The value a `d:` key introduces: to the next `·`, or to the end of the block for the last field."""
    m = re.search(r"<!--\s*d:%s\s*-->" % re.escape(key), block)
    if not m:
        return None
    rest = block[m.end():]
    if last:
        return rest.strip()
    cut = rest.find("·")
    return (rest if cut < 0 else rest[:cut]).strip()


def check_decision_lines(inst):
    """O4 (instance) — the decision line is machine-readable, and it names what the choice beat.

    A `decision` method's section ends in one canonical line (CONVENTIONS → The decision line). Its
    third field is the only one an agent can satisfy by writing nothing — *alternatives considered:
    none* is legal prose and the commonest shape of a bad decision: the first idea, dated. The fields
    carry keys so this check reads them in **any** language, which is the whole reason the keys exist:
    a Russian artifact writes `Решено / кем / рассмотренные альтернативы`, and a check keyed on the
    English label would pass it in silence.

    What the machine can and cannot do: it sees whether something is written in the alternatives
    field, never whether what is written is a real alternative. That half is held by a `verify` return
    and by the human at sign-off (`operations/theses` asks what the choice beat).
    """
    for art in sorted(glob.glob(os.path.join(inst, "[1-6]-*.md"))):
        text = read(art)
        keyed_lines = set()
        for lineno, block in _decision_blocks(text):
            keyed_lines.update(range(lineno, lineno + block.count("\n") + 1))
            keys = D_KEY_RE.findall(_live(block))
            unknown = sorted(set(keys) - set(D_FIELDS))
            if unknown:
                err("O4 [%s] %s:%d: unknown decision field key(s) %s — the three are `d:date`, "
                    "`d:by`, `d:alts` (CONVENTIONS → The decision line)"
                    % (rel(inst), os.path.basename(art), lineno,
                       ", ".join("`d:%s`" % k for k in unknown)))
            dupes = sorted({k for k in keys if keys.count(k) > 1})
            if dupes:
                err("O4 [%s] %s:%d: decision field key(s) %s repeat in one line — one key, one field"
                    % (rel(inst), os.path.basename(art), lineno,
                       ", ".join("`d:%s`" % d for d in dupes)))
            missing = [k for k in D_FIELDS if k not in keys]
            if missing:
                err("O4 [%s] %s:%d: decision line is half-keyed — missing %s. All three keys or none: "
                    "a half-keyed line is the ambiguity the key removes (CONVENTIONS → The decision line)"
                    % (rel(inst), os.path.basename(art), lineno,
                       ", ".join("`d:%s`" % m for m in missing)))
            date = _d_value(block, "date")
            if date is not None and not re.fullmatch(r"\d{4}-\d{2}-\d{2}", date):
                err("O4 [%s] %s:%d: `d:date` = %r is not a YYYY-MM-DD date — an undated decision has "
                    "no version it approved" % (rel(inst), os.path.basename(art), lineno, date))
            alts = _d_value(block, "alts", last=True)
            if alts is None:
                continue
            if alts.startswith("<") and alts.endswith(">"):
                err("O4 [%s] %s:%d: the alternatives field still holds its template placeholder %r — "
                    "the line was copied, not filled" % (rel(inst), os.path.basename(art), lineno, alts))
            elif not alts or D_BARE_NONE_RE.match(alts):
                err("O4 [%s] %s:%d: the alternatives field is %s — name one alternative that was "
                    "weighed and why it lost, or what makes the choice forced (tool-skills/library/"
                    "README.md → The rejected alternative)"
                    % (rel(inst), os.path.basename(art), lineno,
                       "empty" if not alts else "a bare %r" % alts))
        # Best-effort, and only where the prose happens to be English: a decision line with no keys
        # at all is unreadable to this check. The keys are the contract; the label never was.
        for m in D_LABEL_RE.finditer(T.without_change_log(text)):
            lineno = text[:m.start()].count("\n") + 1
            if lineno not in keyed_lines:
                warn("O4 [%s] %s:%d: a `**Decided:**` line carries no `d:` field keys — nothing can "
                     "read its alternatives field in any language (CONVENTIONS → The decision line)"
                     % (rel(inst), os.path.basename(art), lineno))


def check_open_not_confirmed(inst):
    """R (instance) — confirmation markers are used consistently on a section:

    - an `<!-- open -->` section (inbox: to-clarify/open-questions/blockers) carries no `confirmed:` —
      an open inbox is resolved by removing items, not by signing a result;
    - a section is never both `confirmed:` and `contested:` — a verdict is one or the other.
    """
    for art in sorted(glob.glob(os.path.join(inst, "[1-6]-*.md"))):
        for sec in T.sections(read(art)):
            if not sec["id"]:
                continue
            body = sec["body"]
            if T.is_open(body) and T.confirmed(body):
                err("R [%s] %s#%s: an `<!-- open -->` section carries a `confirmed:` marker — an open "
                    "inbox has no result to sign (CONVENTIONS → Section confirmation)"
                    % (rel(inst), os.path.basename(art), sec["id"]))
            if T.confirmed(body) and T.contested(body):
                err("R [%s] %s#%s: a section is both `confirmed:` and `contested:` — a human's verdict "
                    "is one or the other (CONVENTIONS → Section confirmation)"
                    % (rel(inst), os.path.basename(art), sec["id"]))


def check_rests_on(homed):
    """S (schema) — a `rests-on: <step>#<id>` target names a real section (a step template `{#id}`)."""
    for tpl in sorted(glob.glob(os.path.join(ROOT, "steps", "*", "template.md"))):
        for sec in T.sections(read(tpl)):
            for tgt in T.rests_on(sec["body"]):
                sid = tgt.split("#", 1)[1]
                if sid not in homed:
                    err("S %s#%s: rests-on target `%s` names no known section (CONVENTIONS → Section "
                        "confirmation)" % (rel(tpl), sec["id"], tgt))


def check_rests_confirmed(inst):
    """S (instance) — a confirmed section that rests on an unconfirmed foundation (WARN).

    Not an error: the foundation may simply be a step not reached yet. But a signed thesis standing on
    unsigned ground is exactly the silent staleness the marker exists to surface, so it is said out loud.
    """
    parsed, conf = [], {}
    for art in sorted(glob.glob(os.path.join(inst, "[1-6]-*.md"))):
        mm = re.match(r"^(\d+)-", os.path.basename(art))
        step = mm.group(1) if mm else "?"
        secs = T.sections(read(art))
        parsed.append((art, secs))
        for sec in secs:
            if sec["id"]:
                conf["%s#%s" % (step, sec["id"])] = bool(T.confirmed(sec["body"]))
    for art, secs in parsed:
        for sec in secs:
            if sec["id"] and T.confirmed(sec["body"]):
                missing = [tgt for tgt in T.rests_on(sec["body"]) if not conf.get(tgt)]
                if missing:
                    warn("S [%s] %s#%s: confirmed, but rests on unconfirmed %s — re-confirm once the "
                         "foundation is signed (CONVENTIONS → Section confirmation)"
                         % (rel(inst), os.path.basename(art), sec["id"], ", ".join(missing)))


def check_gate_ticks(inst):
    """G2 — sections written, tick still `open`: move 5 (Record) was not finished.

    A pass ends by ticking its gate in `state.yaml` (OPERATING-LOOP move 5). A weaker agent writes
    the section and the worklog and stops there (live-run finding), so the recorded position
    silently falls behind what is on disk — the one drift the section checks (P, O2) cannot see,
    because both look at files, never at the tick. Only written-vs-tick can. A WARN, not an error:
    mid-pass, written-but-unticked is the legal in-between state; left across sessions it is debt,
    and session start (start-work step 1) is where a human sees this report.

    "Written" is worked content, not a present anchor (framework.template_section_lines): steps 2–6
    instantiate their whole shell up front, and v1 of this check fired on every untouched skeleton
    of a first pass — nine false warnings drowning the one real one (live-run finding, run 2).
    """
    if not os.path.exists(os.path.join(inst, "state.yaml")):
        return  # instance health already reports a missing state.yaml on its own
    snap = _snapshot(inst)
    known = set()
    for s in snap["steps"]:
        for g in s["gate"]:
            if g.get("tick_id"):
                known.add(g["tick_id"])
            # the reading, not the raw tick: `re-sign` (a recorded reopen awaiting the owner) is a
            # legitimate waiting state and stays silent — hub F-10 (framework.GATE_READINGS)
            if g.get("reading") == "unrecorded":
                warn("G2 [%s] step %d gate `%s`: its section(s) are written but the tick is `open` with "
                     "no move-5 trace (no change-log entry for the section on/after `last_pass`) — "
                     "Record was not finished; tick it (`done`/`n/a`/`deferred`) in state.yaml "
                     "(gates → %d-…), or record the reopen in the artifact's change log if the "
                     "section awaits re-sign" % (rel(inst), s["step"],
                                                 g.get("tick_id") or ",".join(g.get("sections") or []),
                                                 s["step"]))
    # G3 — the tick vocabulary is closed; G4 — a tick id names a real gate item
    for tick_id, val in sorted(snap.get("ticks", {}).items()):
        if val not in F.TICK_VALUES:
            err("G3 [%s] state.yaml tick `%s` = `%s` — a tick is one of %s (OPERATING-LOOP move 5); "
                "anything else records nothing" % (rel(inst), tick_id, val, " · ".join(F.TICK_VALUES)))
        if tick_id not in known:
            warn("G4 [%s] state.yaml ticks `%s`, which is no gate item of any step (ids are "
                 "`<artifact>#<section>` or the item's `tick-id`) — a stale or misspelled id ticks "
                 "nothing; the real item stays `open`" % (rel(inst), tick_id))
    # G6 / G7 — the comment beside a tick is the ONE home of a skip's reason and a deferral's
    # condition (state-schema → Rules). The reader drops comments, so they are read from the raw file
    # here: a `n/a` with no reason was how a section got skipped for a missing source (decksmith
    # D-43), and a `deferred` with no condition outlived the decision that retired it (F-16d)
    notes = _tick_comments(os.path.join(inst, "state.yaml"))
    for tick_id, val in sorted(snap.get("ticks", {}).items()):
        note = notes.get(tick_id, "")
        if val == "n/a" and not note.strip():
            warn("G6 [%s] state.yaml tick `%s` = `n/a` with no comment — a skip carries its reason "
                 "beside the tick (state-schema), and the reason is a statement about the concept, "
                 "never about a source the instance lacks (Step-1 template → `#cjm`)"
                 % (rel(inst), tick_id))
        if val == "deferred" and not re.search(r"\buntil\s*:", note, re.I):
            warn("G7 [%s] state.yaml tick `%s` = `deferred` with no `until:` in its comment — a "
                 "deferral names what retires it (`until: <decision | pass | date>`, state-schema), "
                 "or nothing ever asks whether that has arrived (step-close step 5)"
                 % (rel(inst), tick_id))


# a tick line of state.yaml: a quoted or bare key, the value, an optional trailing comment
_TICK_LINE_RE = re.compile(r'^\s*(?:"([^"]+)"|\'([^\']+)\'|([^\s"\'#][^:#]*?))\s*:\s*([^#\s][^#]*?)\s*(?:#\s*(.*))?$')


def _tick_comments(path):
    """{tick_id: comment} from the raw state.yaml — the trailing `# …` of a tick line joined with the
    block of comment lines directly above it (no blank line between). The YAML reader strips comments
    by design; here the comment IS the data (G6, G7)."""
    if not os.path.exists(path):
        return {}
    out, pending = {}, []
    for raw in read(path).splitlines():
        s = raw.strip()
        if s.startswith("#"):
            pending.append(s[1:].strip())
            continue
        if not s:
            pending = []
            continue
        m = _TICK_LINE_RE.match(raw)
        if m:
            key = m.group(1) or m.group(2) or (m.group(3) or "").strip()
            out[key] = " ".join(pending + ([m.group(5).strip()] if m.group(5) else []))
        pending = []
    return out


CANON_TAG_WORDS = ("assumption", "sourced", "validated", "refuted")
# near-synonyms a drifting model invents for the canon words — curated, so a deliberate prose
# bracket (`[CONFLICT]`, `[why us]`) is not second-guessed; extend the list when a run teaches a new one
TAG_SYNONYMS = {"inference", "inferred", "estimate", "estimated", "fact", "opinion",
                "guess", "derived", "observed"}
TAG_TOKEN_RE = re.compile(r"(?<!!)\[([^\[\]\n]+)\]")
# a tag whose argument holds a second bare tag — `[sourced: the brief — [assumption] on the count]`.
# TAG_TOKEN_RE cannot see the outer bracket (it never matches across a nested one), so without this
# the compound passes D2 in silence; a backticked mention (`[assumption]`) is already gone from the
# live text the check reads
NESTED_TAG_RE = re.compile(
    r"\[(?:sourced|validated|refuted):[^\[\]\n]*\[(?:assumption|sourced|validated|refuted)\b[^\]\n]*\]"
    r"[^\[\]\n]*\]")
NON_LATIN_RE = re.compile(r"[^\x00-\x7F]")


def check_tag_vocabulary(inst):
    """D2 — confidence/source tags come from the closed vocabulary, verbatim, never localized.

    CONVENTIONS → Confidence tags names exactly four: `[assumption]` (bare) · `[sourced: <where>]` ·
    `[validated: <evidence>]` · `[refuted: <why>]`. The vocabulary is controlled and Latin — a local
    model was observed translating it mid-artifact (`[Премия]`, `[Источники: …]`) and inventing
    near-synonyms (`[inference]`), and every consumer keyed on the canon words (text.CONFIDENCE_RE,
    the console's confidence digest) silently stops counting such a claim. Three tiers:

    - a canon-word tag written off-grammar (compounded qualifier, missing argument) — the
      compound-enum disease, one bracket over (a qualifier belongs in a note);
    - a **trailing** bracket whose head word is non-Latin — a localized tag, unreadable to every
      consumer. Trailing-position only (end of a claim line or table cell — where the canon puts
      tags), because mid-sentence brackets are legitimate prose devices (`для [клиента]…`, a UVP
      slot template) that must not be second-guessed;
    - a trailing single-word bracket from the curated near-synonym list;
    - a tag nested inside another tag's argument (WARN) — one claim carries one verdict, and the
      qualifier that wants to be a second tag goes after the bracket, in words (decksmith F-15: the
      first draft of one pass wrote seventeen compounded tags; the step-close found the nested form).

    A markdown link, a fenced/inline-code example, and mid-sentence prose brackets are all skipped —
    the check reads tags, it does not police prose. Every tier but the last is an ERROR (promoted
    2026-08-23, once the shipped example cleaned its pre-grammar tag debt).
    """
    name = rel(inst)
    files = sorted(glob.glob(os.path.join(inst, "[1-6]-*.md")))
    for folder in sorted(glob.glob(os.path.join(inst, "[1-6]-*"))):
        if os.path.isdir(folder):
            files.extend(sorted(glob.glob(os.path.join(folder, "*.md"))))
    for path in files:
        text = _live(read(path))
        base = os.path.relpath(path, inst)
        for m in TAG_TOKEN_RE.finditer(text):
            if text[m.end():m.end() + 1] == "(":
                continue                                   # a markdown link, not a tag
            inner = m.group(1).strip()
            head = re.match(r"[^\s:,—–]+", inner)
            head = head.group(0).rstrip(".;") if head else ""
            lineno = text[:m.start()].count("\n") + 1
            # trailing = the tag position: to the end of the line/cell, nothing but emphasis
            # closers and further bracket tokens (a claim may end in several tags)
            tail = text[m.end():].split("\n", 1)[0]
            trailing = bool(re.match(r"[\s*_]*(\[[^\]\[]*\][\s*_]*)*(\||$)", tail))
            if head.lower() in CANON_TAG_WORDS:
                word = head.lower()
                ok = (inner == "assumption") if word == "assumption" \
                    else bool(re.fullmatch(r"%s:\s*\S.*" % word, inner, re.S))
                if not ok:
                    err("D2 [%s] %s:%d: tag `[%s]` is off-grammar — the vocabulary is `[assumption]` "
                         "bare · `[sourced: <where>]` · `[validated: <evidence>]` · `[refuted: <why>]`; "
                         "a qualifier belongs in a note, never compounded into the tag "
                         "(CONVENTIONS → Confidence tags)" % (name, base, lineno, inner))
            elif trailing and head and NON_LATIN_RE.search(head) and (":" in inner or " " not in inner):
                err("D2 [%s] %s:%d: `[%s]` reads as a localized tag — the vocabulary is controlled "
                     "and verbatim (`[assumption]` · `[sourced: <where>]` · `[validated: …]` · "
                     "`[refuted: …]`), never translated into the instance language "
                     "(CONVENTIONS → Confidence tags)" % (name, base, lineno, inner))
            elif trailing and " " not in inner and head.lower() in TAG_SYNONYMS:
                err("D2 [%s] %s:%d: `[%s]` looks like an invented confidence tag — the vocabulary "
                     "is closed (no tag = `assumption`; an inferred claim is `[assumption]` too, "
                     "with its reasoning in the worklog)" % (name, base, lineno, inner))
        for m in NESTED_TAG_RE.finditer(text):
            lineno = text[:m.start()].count("\n") + 1
            warn("D2 [%s] %s:%d: `%s` nests one tag inside another — a claim carries ONE verdict; "
                 "the argument of `[sourced:]` names where, and a qualifier goes after the bracket in "
                 "words, never as a second tag (CONVENTIONS → Confidence tags)"
                 % (name, base, lineno, m.group(0)))


def check_source_types(inst):
    """S2 — every sources/INDEX.md row carries a typed slot from the closed list.

    The index is the navigation map an agent reads first; the `type` column is what makes it
    machine-checkable — a method's `reads: [source:research]` can only ever be verified against an
    index that says which slot each source serves. The vocabulary has one machine home
    (`cards.SOURCE_SLOTS`: kb · interview · research · metrics · git); this check holds index rows
    to it. An index whose header carries no `<!--c:type-->` key predates typed slots — one WARN for
    the file, not per-row noise. A word outside the list is an ERROR (the list is closed); an empty
    cell or an explicit `— to clarify —` WARNs (the row is honestly untyped).
    """
    name = rel(inst)
    idx = os.path.join(inst, "sources", "INDEX.md")
    if not os.path.exists(idx):
        return
    # fences stripped (a documented example is not a live table), but inline code kept — the file
    # column is backticked by convention, and _live would blank it out of every message
    raw = re.sub(r"```.*?```", "", read(idx), flags=re.S)
    for tbl in T.tables(raw):
        keys = T.column_keys(tbl["headers"])
        if len(tbl["headers"]) < 3:
            continue                                       # not the index table
        if "type" not in keys:
            warn("S2 [%s] sources/INDEX.md: the index header carries no `Type <!--c:type-->` column "
                 "— rows can't be matched against the source slots methods declare in `reads:` "
                 "(the closed list: %s)" % (name, " · ".join(C.SOURCE_SLOTS)))
            return
        ti = keys.index("type")
        fi = keys.index("file") if "file" in keys else 0
        for i, row in enumerate(tbl["rows"]):
            val = T.clean_cell(row[ti]) if ti < len(row) else ""
            fname = T.clean_cell(row[fi]) if fi < len(row) else "?"
            lineno = tbl["line"] + 2 + i
            if not val or "to clarify" in val:
                warn("S2 [%s] sources/INDEX.md:%d: `%s` has no typed slot — name which slot it "
                     "serves (%s)" % (name, lineno, fname, " · ".join(C.SOURCE_SLOTS)))
            elif val.lower() not in C.SOURCE_SLOTS:
                err("S2 [%s] sources/INDEX.md:%d: `%s` names slot `%s` — not in the closed list "
                    "%s (cards.SOURCE_SLOTS; a new slot is a framework change, not an index edit)"
                    % (name, lineno, fname, val, " · ".join(C.SOURCE_SLOTS)))
        return


def check_evidence_shown(inst):
    """L2 — an external-sources section shows its evidence or declares its gap.

    A method with `evidence_standard: external-sources` (market-sizing, the competitor family,
    substitutes, channels-expansion) rests on data from outside the founder's head. The machine
    cannot know whether real research arrived — but it can see a *worked* section that carries
    neither a single `[sourced: …]` citation nor a single `— to clarify —`: settled-looking
    analysis with no evidence shown and no gap declared, which is the fabrication shape a run-2
    finding predicted. WARN, not error — the judgment call stays with the reviewer.
    """
    name = rel(inst)
    tools = F.load_tools(ROOT)
    external = {t for t, d in tools.items()
                if str(d["fm"].get("evidence_standard", "")).strip() == "external-sources"}
    snap = _snapshot(inst)
    bodies = {(a["step"], s["id"]): s["body"] for a in snap["artifacts"] for s in a["sections"]}
    for st in snap["steps"]:
        for sec in st["sections"]:
            body = bodies.get((st["step"], sec["id"]))
            if body is None or not sec.get("worked"):      # one definition of worked: framework.worked
                continue
            mm = TOOL_MARK_RE.search(body)
            primary = mm.group(1).split(",")[0].strip() if mm else None
            if primary not in external:
                continue
            # the citation is read live (a documented `[sourced:` in code is not evidence); the gap
            # marker is read raw — an agent that writes `— to clarify —` in backticks still declared it
            if "[sourced:" not in _live(body) and not T.TO_CLARIFY_RE.search(body):
                warn("L2 [%s] %s#%s: written by `%s` (evidence_standard: external-sources) with no "
                     "`[sourced: …]` and no `— to clarify —` — settled-looking analysis that shows "
                     "no evidence and declares no gap; cite the source, dispatch research/"
                     "source-intake, or mark the missing input" % (name, st["artifact_file"],
                                                                   sec["id"], primary))


def check_gates(homed):
    """G — every gate item's target section exists (the items as framework.steps reads them)."""
    for st in _steps():
        for item in st["gate"]:
            for sid in item["sections"]:
                if sid not in homed:
                    warn("G %s/README.md: gate item `%s` references section `%s` not found in any step "
                         "template" % (st["dir"], item["label"][:60], sid))


# ---------------------------------------------------------------- main

def instances(argv):
    """The instances to check: the paths given, else every instance discoverable from here.

    Discovery is by **marker** (`config.yaml` / `state.yaml` / `registers/` / artifacts), never by a
    parent folder's name — the canon puts a vendored framework's instance in `product-loops/`, so a linter
    that only globbed `examples/*` and `instances/*` checked nothing at all in the normal install and
    still reported success. `loops.instance.discover` is the same finder the console uses, so the two
    can never disagree about what an instance is.
    """
    if argv:
        out = []
        for raw in argv:
            p = os.path.abspath(os.path.expanduser(raw))
            if not os.path.isdir(p):
                err("path `%s` is not a folder" % raw)
            elif not I.looks_like_instance(p):
                err("path `%s` has no instance marker (config.yaml / state.yaml / registers/)" % raw)
            else:
                out.append(p)
                out.extend(c["path"] for c in I.discover(p, ROOT)
                           if c["path"].startswith(p + os.sep))
        return sorted(set(out))
    return sorted({c["path"] for c in I.discover(ROOT, ROOT)})


def tracked_only(paths):
    """`--ci`: the instances CI's checkout actually contains — gitignored folders dropped and named.

    A local run sees the private instances (`instances/`, the stale example runs) and reports dozens
    of errors CI never will; the noise hides the signal and two runs of the same linter disagree.
    Skipped folders are printed so the local verdict explains itself.
    """
    ignored = I.gitignored(paths, ROOT)
    SKIPPED.extend(sorted(rel(p) for p in ignored))
    return [p for p in paths if p not in ignored]


# The per-pass canon: every agent reads these before every pass, so each word here is paid on every
# read. The guideline number makes growth *visible* — it is a reference point, never a gate (the
# author's call: mechanics and the entity invariant decide acceptance, not a word count). Growth
# past it means the subtraction rule (extending/rules.md) — move something to a
# skill or reference/ before adding.
PER_PASS_CANON = ("AGENTS.md", "process/OVERVIEW.md", "process/OPERATING-LOOP.md",
                  "process/goal-map.md", "process/CONVENTIONS.md")
BUDGET_GUIDELINE_WORDS = 4600


def check_word_budget():
    """W — the always-loaded canon's size stays visible (a guideline, never a gate)."""
    total, missing = 0, []
    for name in PER_PASS_CANON:
        path = os.path.join(ROOT, name)
        if not os.path.exists(path):
            missing.append(name)
            continue
        total += len(read(path).split())
    for name in missing:
        err("W %s: per-pass canon file missing — the reading order in AGENTS.md points at it" % name)
    if total > BUDGET_GUIDELINE_WORDS:
        warn("W per-pass canon is %d words (guideline %d): every agent pays this on every pass — "
             "prefer the subtraction rule (extending/rules.md) over growth"
             % (total, BUDGET_GUIDELINE_WORDS))


def _catalogue():
    """The check catalogue from this module's docstring — `--help` lists every check from one source."""
    doc = __doc__
    start, end = doc.find("Checks ("), doc.find("\nRun:")
    return doc[start:end].rstrip() if start >= 0 and end > start else doc


USAGE = """usage: python3 tools/lint.py [--ci] [instance-folder ...]

Checks the framework's wiring (tools, canon, links) and every instance it can find.
With no arguments, instances are discovered from the framework root by marker
(config.yaml / state.yaml / registers/); in a vendored install pass the instance
folder, e.g. `python3 tools/lint.py product-loops`. Exit code 1 on any ERROR.

  --ci   skip gitignored instance folders (the tree CI's checkout sees) and name them
  -h     this help, with the check catalogue
"""


def main(argv=()):
    argv = list(argv)
    if any(a in ("-h", "--help") for a in argv):
        print(USAGE)
        print(_catalogue())
        return 0
    ci = False
    for flag in ("--ci", "--tracked-only"):
        while flag in argv:
            argv.remove(flag)
            ci = True
    tools = F.load_tools(ROOT)
    homed = F.homed_sections(ROOT)

    check_word_budget()
    check_tools(tools, homed)
    check_quality(tools)
    check_questions(tools)
    check_library_bodies(tools, homed)
    check_single_step(tools)
    check_reachable(tools)
    check_status_tools(tools)
    check_operations()
    check_card_schema()
    check_card_home()
    check_yaml_forms()
    check_subagent_defs()
    check_column_keys()
    check_schema_not_confirmed()
    check_index(tools)
    check_readme_markers(tools)
    checked = instances(argv)
    if ci:
        checked = tracked_only(checked)
    for inst in checked:
        check_instance(inst)
        check_config(inst)
        check_yaml_forms(inst)
        check_artifact_frontmatter(inst)
        check_local_skills(inst)
        check_card_schema(inst)
        check_card_home(inst)
        check_worklogs(inst)
        check_gate_ticks(inst)
        check_language(inst)
        check_node_types(inst)
        check_tag_vocabulary(inst)
        check_evidence_shown(inst)
        check_source_types(inst)
        check_boundary(inst)
        check_sources_ignored(inst)
        check_secrets(inst)
        check_handoff_registers(inst)
        check_perimeter(inst)
        check_card_slots(tools, inst)
        check_instance_conformance(inst)
        check_confirm_dates(inst)
        check_decision_lines(inst)
        check_open_not_confirmed(inst)
        check_rests_confirmed(inst)
        check_register_tables(inst)
        check_register_ids(inst)
        check_feature_refs(inst)
        check_item_features(inst)
        check_register_sources(inst)
        check_serves_links(inst)
        check_decisions(inst)
    check_install(checked)
    check_links()
    check_gates(homed)
    check_rests_on(homed)

    print("very-ai-product-loops linter — %d tool(s), canon: relative links + strict enums" % len(tools))
    # Say what was covered: "0 instances" must read as a problem, not as a clean run.
    print("instances checked: %d%s"
          % (len(checked), (" — " + ", ".join(rel(c) for c in checked)) if checked else
             " (none found — pass a path, e.g. `python3 tools/lint.py product-loops`)"))
    if SKIPPED:
        print("instances skipped (--ci, gitignored): %s" % ", ".join(SKIPPED))
    print()
    for w in WARNS:
        print("  WARN  " + w)
    if WARNS:
        print()
    for e in ERRORS:
        print("  ERROR " + e)
    print("\n%d error(s), %d warning(s)." % (len(ERRORS), len(WARNS)))
    print("NOT checked: prose quality, prerequisite completeness, whether register *values* are "
          "correct (only their enums/ids), or adapter render fidelity.")
    return 1 if ERRORS else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
