#!/usr/bin/env python3
"""very-ai-product-loops — wiring & instance linter.

Dependency-free (Python 3 stdlib only) so it runs anywhere the framework is cloned. It checks the
framework's *mechanics* (where drift silently breaks two agents or an aggregator) and every
instance's registers against the canon. This is the "one script" that turns the wiring class of
bugs from a manual audit into a CI gate.

Parsing lives in `tools/loops/` — the one shared read layer, used by this linter and the local UI
alike. A second parser would drift from the canon and reintroduce exactly the bugs checked here.

Checks (ERROR fails CI · WARN never does):
  A  tool `produces` (section form) has a matching `{#id}` in its template-fragment
  A2 tool `questions.yaml` `produces` matches its SKILL `produces`
  B  every section-form `produces` is homed in some step's artifact (a step template `{#id}`)
  C  library index rows <-> tool folders, and index "Steps" <-> SKILL `used_by_steps`
  D  register enums per instance (hypothesis type/status/confidence · post-test signal/decision ·
     risk category/status · metric kind/instrumentation; signal/decision enforced-if-present)
  E  metrics.csv ids are a subset of metric-tree.md ids
  F  link canon: no GitMark-lite `[[...]]` links remain (canon = relative path + stable {#anchor})
  G  step gate-checklist items reference a real section id  (WARN)
  H  instance config.yaml follows the pinned schema (required keys, one spelling, no aliases)
  I  a product's own skills (product-loops/tool-skills/…) obey the same wiring rules as vendored ones
  J  a register table is not split by a blank line  (WARN)
  K  a register `id` cell names exactly one item (one row = one id)
  L  every library tool carries the quality declaration (evidence_standard · volume_rule ·
     selection_rule · rejects_shown), with legal values and internally consistent
  M  every vendored operations skill declares its wiring (name · kind · produces · used_by_steps ·
     status · version), has the template-fragment its `produces` implies, and matches the
     operations index row for row
  N  a shipped subagent definition (.claude/agents/loops-*.md) carries only its kind's allowed write tool (loops-draft: Write; others: none)
  O  column keys live only on the step template (form of record) and are well-formed there
     (all-keyed-or-none, unique); a key in a method template is an error — the draft is matched by meaning
  O2 an instance artifact section carries its template's column keys (the projection contract;
     enforced — a template-keyed section left un-keyed in the instance is an error)
  P  step worklogs: a step folder holds only `node_type: worklog` files named for the tools its
     sections use; required — every artifact section that names a method (or synthesis) has its worklog
  Q  section confirmation: no schema (template/fragment) ships a `confirmed:`/`contested:` marker, and
     an artifact's `confirmed:` marker parses as a YYYY-MM-DD date (ERROR) else it silently means pending
  R  confirmation consistency: an `<!-- open -->` section (inbox) carries no `confirmed:`, and no
     section is both `confirmed:` and `contested:` (a verdict is one or the other)
  S  rests-on provenance: a `rests-on: <step>#<id>` target resolves to a real section, and a confirmed
     section resting on an unconfirmed foundation is surfaced  (WARN)
  U  a library method serves exactly one step (used_by_steps has one entry)
  V  a status's per-step tools list holds library methods only, each with a `<!-- tool: … -->` home
     in that step's template (how data is gathered belongs in the goals prose)
  W  the always-loaded canon (AGENTS.md + OVERVIEW + OPERATING-LOOP + CONVENTIONS) stays within its
     word budget — WARN past the soft ceiling, ERROR past the hard one (EXTENDING -> subtraction rule)
  Y  questions.yaml is machine-readable: every question `type` is from the shared vocabulary
     (no `type: x_from: y` double-colon scalars)

Run:  python3 tools/lint.py            # every instance discoverable from here
      python3 tools/lint.py product    # or name the instance(s) to check
"""
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # tools/ -> repo root
sys.path.insert(0, os.path.join(ROOT, "tools"))

from loops import framework as F  # noqa: E402
from loops import instance as I  # noqa: E402
from loops import text as T  # noqa: E402
from loops import yamlite  # noqa: E402

ERRORS, WARNS = [], []


def err(msg):
    ERRORS.append(msg)


def warn(msg):
    WARNS.append(msg)


def read(path):
    return T.read(path)


def rel(path):
    return T.rel(path, ROOT)


# ---------------------------------------------------------------- checks

def check_tools(tools, homed):
    for name, t in tools.items():
        fm = t["fm"]
        produces = T.as_list(fm.get("produces"))
        secs = [p for p in produces if not T.is_file_produces(p)]
        # A — produces section present in template-fragment
        frag = os.path.join(t["dir"], "template-fragment.md")
        frag_ids = T.section_ids(read(frag)) if os.path.exists(frag) else set()
        for sid in secs:
            if sid not in frag_ids:
                err("A [%s] produces `%s` but its template-fragment.md has no {#%s}"
                    % (name, sid, sid))
        # A2 — questions.yaml produces matches SKILL produces
        q = os.path.join(t["dir"], "questions.yaml")
        if os.path.exists(q):
            mm = re.search(r"^produces:\s*(.+)$", read(q), re.M)
            if mm:
                qp = set(T.as_list(T.parse_scalar(mm.group(1))))
                sp = set(produces)
                if qp != sp:
                    err("A2 [%s] questions.yaml produces %s != SKILL produces %s"
                        % (name, sorted(qp), sorted(sp)))
        # B — every section-form produces is homed in a step artifact
        for sid in secs:
            if sid not in homed:
                err("B [%s] produces section `%s` with no home — not in any step template {#%s} "
                    "(homeless output)" % (name, sid, sid))


EVIDENCE_STANDARDS = {"external-sources", "primary-research", "internal-data", "derived", "decision"}
REJECTS_SHOWN = {"required", "n/a"}
QUALITY_KEYS = ("evidence_standard", "volume_rule", "selection_rule", "rejects_shown")

# Register enum columns filled only after a test readout — validated when present, never
# flagged as missing (check D). The gradation lives in the row; not every row has been read yet.
OPTIONAL_ENUM_LABELS = {"hypothesis signal", "hypothesis decision"}


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
    sentence, so a list there is a mistake, while `used_by_steps: [any]` is the canon spelling.
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


OPS_REQUIRED = ("name", "kind", "produces", "used_by_steps", "status", "version")
SECTION_ID_RE = re.compile(r"^[a-z0-9][a-z0-9-]*$")


def check_operations():
    """M — vendored operations skills obey the wiring rules too.

    They were the one plane nothing checked: `library/` had checks A-C and a product's own skills had
    check I, while an operations skill could declare anything at all. Its `produces` is a file or a
    prose note far more often than a section id, so only a real section-form value is held to the
    template-fragment/homing rule.
    """
    homed = F.homed_sections(ROOT)
    names = set()
    for skill in sorted(glob.glob(os.path.join(ROOT, "tool-skills", "operations", "*", "SKILL.md"))):
        d = os.path.dirname(skill)
        name = os.path.basename(d)
        fm, _ = T.frontmatter(skill)
        for key in OPS_REQUIRED:
            if key not in fm or _missing(fm.get(key)):
                err("M [%s] operations skill declares no `%s`" % (name, key))
        if fm.get("name") and fm["name"] != name:
            err("M [%s] frontmatter name is `%s` — it must match the folder" % (name, fm["name"]))
        for p in T.as_list(fm.get("produces")):
            if T.is_file_produces(p) or not SECTION_ID_RE.match(str(p)):
                continue  # a file, or prose about what it produces — not a section id
            frag = os.path.join(d, "template-fragment.md")
            frag_ids = T.section_ids(read(frag)) if os.path.exists(frag) else set()
            if p not in frag_ids:
                err("M [%s] produces `%s` but its template-fragment.md has no {#%s}" % (name, p, p))
            if p not in homed:
                err("M [%s] produces section `%s` with no home in any step template" % (name, p))
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
    # Steps column vs used_by_steps
    for line in idx.splitlines():
        m = re.match(r"^\|\s*`([a-z0-9-]+)`\s*\|[^|]*\|[^|]*\|\s*([0-9, ]+)\|", line)
        if not m:
            continue
        name, steps_col = m.group(1), m.group(2)
        idx_steps = sorted(s.strip() for s in steps_col.split(",") if s.strip())
        if name in tools:
            ubs = sorted(str(x) for x in T.as_list(tools[name]["fm"].get("used_by_steps")))
            if idx_steps and ubs and idx_steps != ubs:
                err("C [%s] index Steps %s != SKILL used_by_steps %s" % (name, idx_steps, ubs))


def check_instance(inst):
    name = rel(inst)
    reg = os.path.join(inst, "registers")
    files = {
        "hypothesis type": os.path.join(reg, "hypotheses.md"),
        "hypothesis status": os.path.join(reg, "hypotheses.md"),
        "hypothesis confidence": os.path.join(reg, "hypotheses.md"),
        "hypothesis signal": os.path.join(reg, "hypotheses.md"),
        "hypothesis decision": os.path.join(reg, "hypotheses.md"),
        "risk category": os.path.join(reg, "risks.md"),
        "risk status": os.path.join(reg, "risks.md"),
        "metric kind": os.path.join(reg, "metric-tree.md"),
        "metric instrumentation": os.path.join(reg, "metric-tree.md"),
    }
    for label, (allowed, key) in F.ENUMS.items():
        path = files[label]
        if not os.path.exists(path):
            continue
        text = read(path)
        # a register column is found by its language-independent `<!--c:key-->`, never by header prose
        vals = T.column_key_values(text, key)
        if vals is None:
            # A post-test grade (signal/decision) is filled only once a readout exists, so its
            # absence is normal, not a gap to flag. Required columns still warn when missing.
            if label not in OPTIONAL_ENUM_LABELS:
                warn("D [%s] %s: no column keyed `<!--c:%s-->` to check %s (a register the console reads "
                     "must key its columns)" % (name, os.path.basename(path), key, label))
            continue
        for v in vals:
            cv = T.enum_value(v)
            if not cv:
                continue
            if cv not in allowed:
                err("D [%s] %s: `%s` = %r not in enum %s (a qualifier belongs in `note`, a "
                    "cross-cutting theme in `tags` — never compounded into the value)"
                    % (name, os.path.basename(path), key, cv, sorted(allowed)))
    # E — metrics.csv ids subset of metric-tree.md ids
    csv = os.path.join(reg, "metrics.csv")
    mt = os.path.join(reg, "metric-tree.md")
    if os.path.exists(csv) and os.path.exists(mt):
        md_ids = set()
        for v in (T.table_column(read(mt), "id") or []):
            t = T.clean_cell(v)
            if t.startswith("M-"):
                md_ids.add(t)
        for ln in read(csv).splitlines()[1:]:
            cid = ln.split(",")[0].strip()
            if cid and cid.startswith("M-") and cid not in md_ids:
                # Name the cause: the message used to be formally correct and read as a linter bug,
                # which is the same as not reporting it (field report, point 6).
                err("E [%s] metrics.csv id `%s` has no definition row in metric-tree.md — a typo, a "
                    "node renamed without minting a new id, or several ids written into one "
                    "definition cell (a row defines exactly one id)" % (name, cid))


# a section may name several methods (`<!-- tool: A, B -->`); the first is the primary that owns
# the worklog (CONVENTIONS -> primary-tool). Capture the whole list; the caller takes the first.
TOOL_MARK_RE = re.compile(r"<!--\s*tool:\s*([a-z0-9-]+(?:\s*,\s*[a-z0-9-]+)*)\s*-->")
SYNTH_MARK_RE = re.compile(r"<!--\s*synthesis")
SOURCES_LINK_RE = re.compile(r"sources/[A-Za-z0-9._/-]+\.md")


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
    for art in sorted(glob.glob(os.path.join(inst, "[1-6]-*.md"))):
        stem = os.path.basename(art)[:-3]                 # "2-analysis"
        folder = os.path.join(inst, stem)
        text = read(art)
        expected = {m.split(",")[0].strip() for m in TOOL_MARK_RE.findall(text)}
        if SYNTH_MARK_RE.search(text):
            expected.add("synthesis")
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
            if base[:-3] not in expected and base[:-3] != "metrics-capture":
                # `metrics-capture` is event-driven (an operations skill): its derivation worklog may
                # appear in any step folder without a section marker — the csv row cites it.
                warn("P [%s] %s/%s is an orphan — no section uses tool `%s`"
                     % (name, stem, base, base[:-3]))
        for miss in sorted(expected - present):
            err("P [%s] %s uses tool `%s` but %s/%s.md is missing — the section has no source of truth "
                "to project from (CONVENTIONS -> Step folders & worklogs)" % (name, stem, miss, stem, miss))
        if SOURCES_LINK_RE.search(text):
            warn("P [%s] %s links sources/ directly — a source citation routes through the worklog, "
                 "never the artifact (see source-intake)" % (name, stem))


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
        steps = T.as_list(t["fm"].get("used_by_steps"))
        if len(steps) != 1:
            err("U [%s] used_by_steps %s — a library method serves exactly one step; a second step "
                "is a second skill (see EXTENDING.md)" % (name, steps))


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
    for plane, fname in (("operations", "SKILL.md"), ("outputs", "SKILL.md"), ("outputs", "ADAPTER.md")):
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


REGISTER_ID_RE = re.compile(r"\b(?:H-\d+|R-\d+|M-[a-z0-9][a-z0-9-]*)\b")


def check_register_ids(inst):
    """K — an `id` cell names exactly one register item.

    Three ids sharing one definition row (`M-dau / M-wau / M-mau`) is the compound-enum disease one
    column over: every reference and every `metrics.csv` series can only reach the first, so the
    other two point at nothing while the register looks complete.
    """
    name = rel(inst)
    for filename in ("hypotheses.md", "risks.md", "metric-tree.md"):
        path = os.path.join(inst, "registers", filename)
        if not os.path.exists(path):
            continue
        for v in (T.table_column(read(path), "id") or []):
            ids = REGISTER_ID_RE.findall(T.clean_cell(v))
            if len(ids) > 1:
                err("K [%s] %s: id cell `%s` names %d ids — one row is one item, so only `%s` is "
                    "reachable and the rest have no definition; split it into %d rows (they may "
                    "repeat the definition text)"
                    % (name, filename, T.clean_cell(v), len(ids), ids[0], len(ids)))


CONFIG_REQUIRED = ("product", "language", "active_status", "directions")
CONFIG_OPTIONAL = ("scope_note", "metric_source_slots", "sources", "products", "delegation")
CONFIG_BANNED = {"metric_sources": "metric_source_slots", "metric_slots": "metric_source_slots",
                 "product_scope": "scope_note", "scope": "scope_note", "lang": "language",
                 "title": "product", "name": "product", "status": "active_status",
                 "sources_dir": "sources"}


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
    data, skipped = yamlite.load(path)
    for ln, raw in skipped:
        warn("H [%s] config.yaml line %d not parseable by the framework's YAML subset: %s"
             % (name, ln, raw.strip()))
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


def check_local_skills(inst):
    """I — a product's own skills (product-loops/tool-skills/…) obey the same wiring rules as vendored ones."""
    name = rel(inst)
    homed = F.homed_sections(ROOT)
    for plane in ("library", "operations"):
        for skill in sorted(glob.glob(os.path.join(inst, "tool-skills", plane, "*", "SKILL.md"))):
            d = os.path.dirname(skill)
            local = os.path.basename(d)
            fm, _ = T.frontmatter(skill)
            produces = T.as_list(fm.get("produces"))
            if not produces:
                err("I [%s] local skill `%s` declares no `produces`" % (name, local))
            secs = [p for p in produces if not T.is_file_produces(p)]
            frag = os.path.join(d, "template-fragment.md")
            frag_ids = T.section_ids(read(frag)) if os.path.exists(frag) else set()
            for sid in secs:
                if sid not in homed:
                    err("I [%s] local skill `%s` produces section `%s` with no home in any step template"
                        % (name, local, sid))
                if sid not in frag_ids:
                    err("I [%s] local skill `%s` produces `%s` but its template-fragment.md has no {#%s}"
                        % (name, local, sid, sid))
            if not T.as_list(fm.get("used_by_steps")):
                warn("I [%s] local skill `%s` names no `used_by_steps` — no step reaches it" % (name, local))


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
    out = {}
    for path in sorted(glob.glob(os.path.join(ROOT, "steps", "*", "template.md"))):
        out.update(_section_keys(read(path)))
    return out


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
    for art in sorted(glob.glob(os.path.join(inst, "[1-6]-*.md"))):
        text = read(art)
        present = {sec["id"] for sec in T.sections(text) if sec["id"]}
        inst_keys = _section_keys(text)   # {sid: [keys]} for keyed instance tables only
        for sid, tks in tkeys.items():
            if sid not in present:
                continue                  # section not in this artifact (or step not reached)
            iks = inst_keys.get(sid)
            if iks is None:
                err("O2 %s#%s: the template keys this section but the instance carries no column keys — "
                    "the chistovik must carry its template's form so the console reads it by key "
                    "(CONVENTIONS → Column keys)" % (rel(art), sid))
            elif set(iks) != set(tks):
                err("O2 %s#%s: instance table keys %s do not match the template's form %s — the "
                    "chistovik must carry its template's keys (CONVENTIONS → Column keys)"
                    % (rel(art), sid, sorted(iks), sorted(tks)))


CONFIRM_LOOSE_RE = re.compile(r"<!--\s*confirmed:\s*(.*?)\s*-->")
CONTEST_LOOSE_RE = re.compile(r"<!--\s*contested:\s*(.*?)\s*-->")


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
        for raw in CONFIRM_LOOSE_RE.findall(read(art)):
            if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", _confirm_date(raw)):
                err("Q [%s] %s: `confirmed: %s` is not a YYYY-MM-DD date, so it reads as *pending* — "
                    "a typo silently un-confirms the section (CONVENTIONS → Section confirmation)"
                    % (rel(inst), os.path.basename(art), raw))


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


def check_gates(homed):
    for readme in glob.glob(ROOT + "/steps/*/README.md"):
        for mm in re.finditer(r"[→>]\s*`?[a-z0-9-]+#([a-z0-9-]+)`?", read(readme)):
            sid = mm.group(1)
            if sid not in homed:
                warn("G %s: gate item references section `%s` not found in any step template"
                     % (rel(readme), sid))


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


# The per-pass canon: every agent reads these before every pass, so each word here is paid on every
# read. The ceilings hold the set at roughly half its pre-0.10 size; growth past WARN means the
# subtraction rule (EXTENDING -> "Where a new rule goes") — move something to a skill or reference/
# before adding, never just raise the numbers.
PER_PASS_CANON = ("AGENTS.md", "process/OVERVIEW.md", "process/OPERATING-LOOP.md",
                  "process/goal-map.md", "process/CONVENTIONS.md")
BUDGET_WARN_WORDS = 4600
BUDGET_ERROR_WORDS = 5000


def check_word_budget():
    """W — the always-loaded canon stays within its word budget."""
    total, missing = 0, []
    for name in PER_PASS_CANON:
        path = os.path.join(ROOT, name)
        if not os.path.exists(path):
            missing.append(name)
            continue
        total += len(read(path).split())
    for name in missing:
        err("W %s: per-pass canon file missing — the reading order in AGENTS.md points at it" % name)
    if total > BUDGET_ERROR_WORDS:
        err("W per-pass canon is %d words (> %d): every agent pays this on every pass — apply the "
            "subtraction rule (EXTENDING -> Where a new rule goes) before adding"
            % (total, BUDGET_ERROR_WORDS))
    elif total > BUDGET_WARN_WORDS:
        warn("W per-pass canon is %d words (> %d soft ceiling of %d hard): move something to a "
             "skill or process/reference/ before it grows further"
             % (total, BUDGET_WARN_WORDS, BUDGET_ERROR_WORDS))


def main(argv=()):
    tools = F.load_tools(ROOT)
    homed = F.homed_sections(ROOT)

    check_word_budget()
    check_tools(tools, homed)
    check_quality(tools)
    check_questions(tools)
    check_single_step(tools)
    check_status_tools(tools)
    check_operations()
    check_subagent_defs()
    check_column_keys()
    check_schema_not_confirmed()
    check_index(tools)
    checked = instances(list(argv))
    for inst in checked:
        check_instance(inst)
        check_config(inst)
        check_local_skills(inst)
        check_worklogs(inst)
        check_instance_conformance(inst)
        check_confirm_dates(inst)
        check_open_not_confirmed(inst)
        check_rests_confirmed(inst)
        check_register_tables(inst)
        check_register_ids(inst)
    check_links()
    check_gates(homed)
    check_rests_on(homed)

    print("very-ai-product-loops linter — %d tool(s), canon: relative links + strict enums" % len(tools))
    # Say what was covered: "0 instances" must read as a problem, not as a clean run.
    print("instances checked: %d%s\n"
          % (len(checked), (" — " + ", ".join(rel(c) for c in checked)) if checked else
             " (none found — pass a path, e.g. `python3 tools/lint.py product`)"))
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
