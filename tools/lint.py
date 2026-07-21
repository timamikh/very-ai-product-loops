#!/usr/bin/env python3
"""very-ai-product-loops — wiring & instance linter.

Dependency-free (Python 3 stdlib only) so it runs anywhere the framework is cloned. It checks the
framework's *mechanics* (where drift silently breaks two agents or an aggregator) and every
instance's registers against the canon. This is the "one script" that turns the wiring class of
bugs from a manual audit into a CI gate.

Checks (ERROR fails CI · WARN never does):
  A  tool `produces` (section form) has a matching `{#id}` in its template-fragment
  A2 tool `questions.yaml` `produces` matches its SKILL `produces`
  B  every section-form `produces` is homed in some step's artifact (a step template `{#id}`)
  C  library index rows <-> tool folders, and index "Steps" <-> SKILL `used_by_steps`
  D  register enums per instance (hypothesis type · risk category · metric kind/instrumentation)
  E  metrics.csv ids are a subset of metric-tree.md ids
  F  link canon: no GitMark-lite `[[...]]` links remain (canon = relative path + stable {#anchor})
  G  step gate-checklist items reference a real section id  (WARN)

Run:  python3 tools/lint.py            # from anywhere; resolves the repo root itself
"""
import os, re, sys, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # tools/ -> repo root

ERRORS, WARNS = [], []
def err(msg):  ERRORS.append(msg)
def warn(msg): WARNS.append(msg)

def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()

def rel(path):
    return os.path.relpath(path, ROOT)

# ---------------------------------------------------------------- frontmatter

def parse_scalar(v):
    v = v.strip()
    if v.startswith("[") and v.endswith("]"):
        inner = v[1:-1].strip()
        return [] if not inner else [x.strip().strip('"').strip("'") for x in inner.split(",")]
    return v.strip('"').strip("'")

def frontmatter(path):
    """Minimal `key: value` frontmatter parse (top-level, single-line values only)."""
    text = read(path)
    m = re.match(r"^---\n(.*?)\n---", text, re.S)
    fm = {}
    if m:
        for line in m.group(1).splitlines():
            mm = re.match(r"^([A-Za-z_][A-Za-z0-9_]*):\s*(.*)$", line)
            if mm:
                fm[mm.group(1)] = parse_scalar(mm.group(2))
    return fm, text

def as_list(v):
    if v is None or v == "":
        return []
    return v if isinstance(v, list) else [v]

def section_ids(text):
    return set(re.findall(r"\{#([a-z0-9][a-z0-9-]*)\}", text))

def is_file_produces(p):
    # a `produces` that names a file (brief -> product/briefs/<slug>.md, handoff -> HANDOFF.md),
    # not an artifact section id.
    return "/" in p or p.endswith(".md") or p.isupper() or p in ("HANDOFF.md",)

# ---------------------------------------------------------------- markdown tables

def table_column(text, colname):
    """Values under the first table column whose header equals `colname` (case-insensitive)."""
    lines = text.splitlines()
    target = colname.lower()
    for i, line in enumerate(lines):
        s = line.strip()
        if not s.startswith("|"):
            continue
        headers = [c.strip().lower() for c in s.strip("|").split("|")]
        if target not in headers:
            continue
        if i + 1 >= len(lines) or not re.match(r"^\s*\|?[\s:|-]+\|?\s*$", lines[i + 1]):
            continue
        idx = headers.index(target)
        vals = []
        for row in lines[i + 2:]:
            if not row.strip().startswith("|"):
                break
            cells = [c.strip() for c in row.strip().strip("|").split("|")]
            if len(cells) > idx:
                vals.append(cells[idx])
        return vals
    return None

def clean_cell(v):
    return re.sub(r"[*`]", "", v).strip()

# ---------------------------------------------------------------- load tools

def load_tools():
    tools = {}
    for skill in sorted(glob.glob(ROOT + "/tool-skills/library/*/SKILL.md")):
        d = os.path.dirname(skill)
        name = os.path.basename(d)
        fm, _ = frontmatter(skill)
        tools[name] = {"dir": d, "fm": fm, "skill": skill}
    return tools

def homed_sections():
    """Every section id that has a real home in a step artifact (a step template {#id})."""
    homed = set()
    for tpl in glob.glob(ROOT + "/steps/*/template.md"):
        homed |= section_ids(read(tpl))
    return homed

# ---------------------------------------------------------------- checks

def check_tools(tools, homed):
    for name, t in tools.items():
        fm = t["fm"]
        produces = as_list(fm.get("produces"))
        secs = [p for p in produces if not is_file_produces(p)]
        # A — produces section present in template-fragment
        frag = os.path.join(t["dir"], "template-fragment.md")
        frag_ids = section_ids(read(frag)) if os.path.exists(frag) else set()
        for sid in secs:
            if sid not in frag_ids:
                err("A [%s] produces `%s` but its template-fragment.md has no {#%s}"
                    % (name, sid, sid))
        # A2 — questions.yaml produces matches SKILL produces
        q = os.path.join(t["dir"], "questions.yaml")
        if os.path.exists(q):
            mm = re.search(r"^produces:\s*(.+)$", read(q), re.M)
            if mm:
                qp = set(as_list(parse_scalar(mm.group(1))))
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
            ubs = sorted(str(x) for x in as_list(tools[name]["fm"].get("used_by_steps")))
            if idx_steps and ubs and idx_steps != ubs:
                err("C [%s] index Steps %s != SKILL used_by_steps %s" % (name, idx_steps, ubs))

ENUMS = {
    "hypothesis type":       ({"desirability", "feasibility", "viability", "usability"}, "type"),
    "risk category":         ({"market", "product", "execution", "legal", "financial", "dependency"}, "category"),
    "metric kind":           ({"measured", "derived"}, "kind"),
    "metric instrumentation":({"instrumented", "proxy", "not-instrumented"}, "instrumentation"),
}

def check_instance(inst):
    name = rel(inst)
    reg = os.path.join(inst, "registers")
    files = {
        "hypothesis type":        os.path.join(reg, "hypotheses.md"),
        "risk category":          os.path.join(reg, "risks.md"),
        "metric kind":            os.path.join(reg, "metric-tree.md"),
        "metric instrumentation": os.path.join(reg, "metric-tree.md"),
    }
    for label, (allowed, col) in ENUMS.items():
        path = files[label]
        if not os.path.exists(path):
            continue
        vals = table_column(read(path), col)
        if vals is None:
            warn("D [%s] %s: no `%s` column found to check" % (name, os.path.basename(path), col))
            continue
        for v in vals:
            cv = clean_cell(v)
            if not cv or cv in ("—", "- to clarify -", "— to clarify —"):
                continue
            if cv not in allowed:
                err("D [%s] %s: `%s` = %r not in enum %s (compound values -> use a `tags` column)"
                    % (name, os.path.basename(path), col, cv, sorted(allowed)))
    # E — metrics.csv ids subset of metric-tree.md ids
    csv = os.path.join(reg, "metrics.csv")
    mt = os.path.join(reg, "metric-tree.md")
    if os.path.exists(csv) and os.path.exists(mt):
        md_ids = set()
        for v in (table_column(read(mt), "id") or []):
            t = clean_cell(v)
            if t.startswith("M-"):
                md_ids.add(t)
        for ln in read(csv).splitlines()[1:]:
            cid = ln.split(",")[0].strip()
            if cid and cid.startswith("M-") and cid not in md_ids:
                err("E [%s] metrics.csv id `%s` not defined in metric-tree.md" % (name, cid))

def check_links():
    roots = ["process", "steps", "statuses", "tool-skills", "examples", "README.md"]
    for r in roots:
        base = os.path.join(ROOT, r)
        paths = [base] if os.path.isfile(base) else glob.glob(base + "/**/*.md", recursive=True)
        for p in paths:
            if "/.git/" in p:
                continue
            hits = re.findall(r"\[\[[^\]]+\]\]", read(p))
            if hits:
                err("F %s: %d GitMark-lite [[...]] link(s) — canon is relative path + {#anchor}: %s"
                    % (rel(p), len(hits), ", ".join(sorted(set(hits))[:5])))

def check_gates(homed):
    for readme in glob.glob(ROOT + "/steps/*/README.md"):
        for m in re.finditer(r"->|→", read(readme)):
            pass
        for mm in re.finditer(r"[→>]\s*`?[a-z0-9-]+#([a-z0-9-]+)`?", read(readme)):
            sid = mm.group(1)
            if sid not in homed:
                warn("G %s: gate item references section `%s` not found in any step template"
                     % (rel(readme), sid))

# ---------------------------------------------------------------- main

def main():
    tools = load_tools()
    homed = homed_sections()

    check_tools(tools, homed)
    check_index(tools)
    for inst in sorted(glob.glob(ROOT + "/examples/*") + glob.glob(ROOT + "/instances/*")):
        if os.path.isdir(inst):
            check_instance(inst)
    check_links()
    check_gates(homed)

    print("very-ai-product-loops linter — %d tool(s), canon: relative links + strict enums\n"
          % len(tools))
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
    sys.exit(main())
