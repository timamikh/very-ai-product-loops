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
  D  register enums per instance (hypothesis type/status/confidence · risk category/status ·
     metric kind/instrumentation)
  E  metrics.csv ids are a subset of metric-tree.md ids
  F  link canon: no GitMark-lite `[[...]]` links remain (canon = relative path + stable {#anchor})
  G  step gate-checklist items reference a real section id  (WARN)
  H  instance config.yaml follows the pinned schema (required keys, one spelling, no aliases)
  I  a product's own skills (product/tool-skills/…) obey the same wiring rules as vendored ones
  J  a register table is not split by a blank line  (WARN)
  K  a register `id` cell names exactly one item (one row = one id)

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


def check_index(tools):
    idx = read(ROOT + "/tool-skills/library/README.md")
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
        "risk category": os.path.join(reg, "risks.md"),
        "risk status": os.path.join(reg, "risks.md"),
        "metric kind": os.path.join(reg, "metric-tree.md"),
        "metric instrumentation": os.path.join(reg, "metric-tree.md"),
    }
    for label, (allowed, aliases) in F.ENUMS.items():
        path = files[label]
        if not os.path.exists(path):
            continue
        text = read(path)
        vals, col = None, None
        for alias in aliases:  # the column header follows the instance's language; values never do
            vals = T.table_column(text, alias)
            if vals is not None:
                col = alias
                break
        if vals is None:
            warn("D [%s] %s: no `%s` column found to check" % (name, os.path.basename(path), aliases[0]))
            continue
        for v in vals:
            cv = T.enum_value(v)
            if not cv:
                continue
            if cv not in allowed:
                err("D [%s] %s: `%s` = %r not in enum %s (a qualifier belongs in `note`, a "
                    "cross-cutting theme in `tags` — never compounded into the value)"
                    % (name, os.path.basename(path), col, cv, sorted(allowed)))
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
CONFIG_OPTIONAL = ("scope_note", "metric_source_slots", "sources", "products")
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
    """I — a product's own skills (product/tool-skills/…) obey the same wiring rules as vendored ones."""
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
            hits = T.LINK_RE.findall(read(p))
            if hits:
                err("F %s: %d GitMark-lite [[...]] link(s) — canon is relative path + {#anchor}: %s"
                    % (rel(p), len(hits), ", ".join(sorted(set(hits))[:5])))


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
    parent folder's name — the canon puts a vendored framework's instance in `product/`, so a linter
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


def main(argv=()):
    tools = F.load_tools(ROOT)
    homed = F.homed_sections(ROOT)

    check_tools(tools, homed)
    check_index(tools)
    checked = instances(list(argv))
    for inst in checked:
        check_instance(inst)
        check_config(inst)
        check_local_skills(inst)
        check_register_tables(inst)
        check_register_ids(inst)
    check_links()
    check_gates(homed)

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
