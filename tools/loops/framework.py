"""The framework side of the read model: steps, statuses, library tools.

Everything here is read from the canon itself — never duplicated in code. If a step adds a gate item
or a tool changes what it produces, the tooling picks it up on the next read; there is no second list
to update.
"""
import glob
import os
import re

from . import text as T
from . import yamlite

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # tools/loops -> root


# ---------------------------------------------------------------- steps

GATE_ITEM_RE = re.compile(r"^-\s*\[[ xX]\]\s*(.+)$", re.M)
TICK_ID_RE = re.compile(r"tick-id\s*`([a-z0-9][a-z0-9-]*)`")
TARGET_RE = re.compile(r"`([a-z0-9-]+)#([a-z0-9-]+)`|`#([a-z0-9-]+)`")
REGISTER_HINT_RE = re.compile(r"→\s*(hypothesis|risk|metric)\s+register", re.I)


def _gate_items(body, artifact_slug):
    """Gate checklist items of a step, keyed the way `state.yaml` keys them.

    Per OPERATING-LOOP: a gate item's stable id is its `artifact#section` target, unless the item
    spans/repeats sections and carries an explicit `tick-id`.
    """
    items = []
    for m in GATE_ITEM_RE.finditer(body):
        line = m.group(1).strip()
        targets = []
        for tm in TARGET_RE.finditer(line):
            if tm.group(1):
                targets.append("%s#%s" % (tm.group(1), tm.group(2)))
            elif tm.group(3):
                targets.append("%s#%s" % (artifact_slug, tm.group(3)))
        tick = TICK_ID_RE.search(line)
        label = re.split(r"\s*→\s*`", line)[0].strip()
        label = re.sub(r"\s*·\s*tick-id.*$", "", label).strip()
        reg = REGISTER_HINT_RE.search(line)
        items.append({
            "tick_id": tick.group(1) if tick else (targets[0] if targets else None),
            "label": label,
            "targets": targets,
            "sections": [t.split("#", 1)[1] for t in targets],
            "register": (reg.group(1).lower() if reg else None),
            "optional": label.lower().startswith("(optional)"),
        })
    return items


def _skeleton(body):
    """The artifact skeleton table: which sections exist and which tool is recommended for each."""
    headers, rows = T.table_rows(body, "Section (ID)", "What", "Recommended tool")
    out = []
    for r in rows:
        sid = T.clean_cell(r.get("section (id)", ""))
        sid = re.sub(r"\s*\(optional\)\s*", "", sid).strip()
        if not sid:
            continue
        tools = re.findall(r"`([a-z0-9-]+)`", r.get("recommended tool", ""))
        out.append({
            "id": sid,
            "what": r.get("what", "").strip(),
            "tools": tools,
            "optional": "optional" in r.get("section (id)", "").lower(),
        })
    return out


GOAL_RE = re.compile(r"\*\*Goal\b[^*]*\*\*[:.]?\s*(.+?)(?:\n\n|\Z)", re.S)


def _goal(body):
    """The step's goal sentence, as the step README states it (never restated in code)."""
    m = GOAL_RE.search(body)
    if not m:
        return ""
    return T.plain(re.sub(r"\s+", " ", m.group(1)).strip())


def steps(root=ROOT):
    """Every step of the process core, in order."""
    out = []
    for readme in sorted(glob.glob(os.path.join(root, "steps", "*", "README.md"))):
        fm, body = T.frontmatter(readme)
        output = fm.get("output", "")
        # `1-passport.md` -> artifact slug `passport` (the gate shorthand drops the number prefix)
        slug = re.sub(r"^\d+-", "", output).replace(".md", "")
        out.append({
            "goal": _goal(body),
            "step": int(fm.get("step", 0) or 0),
            "name": fm.get("name", os.path.basename(os.path.dirname(readme))),
            "title": fm.get("title", ""),
            "output": output,
            "artifact": slug,
            "cadence": fm.get("cadence", ""),
            "method_basis": fm.get("method_basis", ""),
            "version": fm.get("version", ""),
            "dir": T.rel(os.path.dirname(readme), root),
            "gate": _gate_items(body, slug),
            "skeleton": _skeleton(body),
        })
    out.sort(key=lambda s: s["step"])
    return out


# ---------------------------------------------------------------- statuses


def statuses(root=ROOT):
    """The product-stage plane: each status with its per-step goals and tool emphasis."""
    out = []
    for path in sorted(glob.glob(os.path.join(root, "statuses", "[0-9]*.md"))):
        raw = T.read(path)
        m = re.match(r"^---\n(.*?)\n---", raw, re.S)
        data, _ = yamlite.parse(m.group(1)) if m else ({}, [])
        per_step = data.get("per_step") or {}
        out.append({
            "name": data.get("name", os.path.basename(path)),
            "order": data.get("order", 0),
            "gate_emphasis": data.get("gate_emphasis", ""),
            "per_step": {str(k): v for k, v in per_step.items()} if isinstance(per_step, dict) else {},
            "file": T.rel(path, root),
        })
    out.sort(key=lambda s: s["order"] or 0)
    return out


# ---------------------------------------------------------------- library tools


def load_tools(root=ROOT):
    """Every library tool-skill, keyed by name, with its wiring frontmatter."""
    tools = {}
    for skill in sorted(glob.glob(os.path.join(root, "tool-skills", "library", "*", "SKILL.md"))):
        d = os.path.dirname(skill)
        fm, _ = T.frontmatter(skill)
        tools[os.path.basename(d)] = {"dir": d, "fm": fm, "skill": skill}
    return tools


def tool_cards(root=ROOT):
    """The library as UI-ready cards (no file paths to resolve in the browser)."""
    cards = []
    for name, t in sorted(load_tools(root).items()):
        fm = t["fm"]
        cards.append({
            "name": name,
            "kind": fm.get("kind", ""),
            "produces": T.as_list(fm.get("produces")),
            "prerequisites": T.as_list(fm.get("prerequisites")),
            "reads_registers": T.as_list(fm.get("reads_registers")),
            "writes_registers": T.as_list(fm.get("writes_registers")),
            "inputs": T.as_list(fm.get("inputs")),
            "used_by_steps": [str(x) for x in T.as_list(fm.get("used_by_steps"))],
            "method_basis": fm.get("method_basis", ""),
            "skill": T.rel(t["skill"], root),
            "has_questions": os.path.exists(os.path.join(t["dir"], "questions.yaml")),
        })
    return cards


def skill_card(path, plane, origin, root=ROOT):
    """One skill (library method · operations · adapter) as a UI-ready card."""
    fm, body = T.frontmatter(path)
    d = os.path.dirname(path)
    # the intro paragraph, without the document's own H1 (a card that starts by repeating its title
    # wastes the only line a human reads)
    intro = ""
    for sec in T.sections(body):
        if sec["id"] is None and sec["body"]:
            intro = sec["body"]
            break
    if not intro:
        after = T.body_after_frontmatter(body)
        intro = after.split("\n\n")[1] if "\n\n" in after else after
    intro = re.sub(r"^\s*#[^\n]*\n+", "", intro)
    # skip the meta lines some skills open with ("Method basis: …") — a card should lead with what the
    # method IS, not with its provenance
    for para in re.split(r"\n\s*\n", intro):
        clean = T.plain(para.replace("\n", " ")).strip()
        if len(clean) > 40 and not re.match(r"^(method basis|status|version|updated)\b", clean, re.I):
            intro = clean
            break
    else:
        # every paragraph opens with provenance — drop that first sentence and keep the rest
        intro = re.sub(r"^\s*(method basis|status|version|updated)\b[^.]*\.\s*", "",
                       T.plain(intro.replace("\n", " ")), flags=re.I)
    return {
        "name": fm.get("name", os.path.basename(d)),
        "plane": plane,                                  # library · operations · adapters
        "origin": origin,                                # vendored (framework) · local (product)
        "kind": fm.get("kind", ""),
        "produces": T.as_list(fm.get("produces")),
        "prerequisites": T.as_list(fm.get("prerequisites")),
        "reads_registers": T.as_list(fm.get("reads_registers")),
        "writes_registers": T.as_list(fm.get("writes_registers")),
        "inputs": T.as_list(fm.get("inputs")),
        "used_by_steps": [str(x) for x in T.as_list(fm.get("used_by_steps"))],
        "method_basis": fm.get("method_basis", ""),
        # the quality declaration (library README -> "The quality declaration"); shown so a reader can
        # see what the method claims about its own evidence before running it
        "evidence_standard": fm.get("evidence_standard", ""),
        "volume_rule": fm.get("volume_rule", ""),
        "selection_rule": fm.get("selection_rule", ""),
        "rejects_shown": fm.get("rejects_shown", ""),
        "version": fm.get("version", ""),
        "opinionated": fm.get("opinionated", ""),
        "summary": re.sub(r"\s+", " ", T.plain(intro))[:260] if intro else "",
        "file": path,
        "dir": d,
        "has_questions": os.path.exists(os.path.join(d, "questions.yaml")),
        "has_fragment": os.path.exists(os.path.join(d, "template-fragment.md")),
    }


def skills(root=ROOT, instance=None):
    """Every skill the agent can reach: the vendored planes, plus a product's own local skills.

    The vendored framework is read-only (re-vendoring overwrites it), so a product's own methods live
    under `<instance>/tool-skills/…` and win on a name collision. Reported here so the console can show
    one library with the origin of each entry marked.
    """
    out = []
    planes = (("library", os.path.join(root, "tool-skills", "library", "*", "SKILL.md")),
              ("operations", os.path.join(root, "tool-skills", "operations", "*", "SKILL.md")),
              ("adapters", os.path.join(root, "tool-skills", "adapters", "*", "ADAPTER.md")))
    for plane, pattern in planes:
        for f in sorted(glob.glob(pattern)):
            out.append(skill_card(f, plane, "vendored", root))
    if instance:
        for plane in ("library", "operations", "adapters"):
            for name in ("SKILL.md", "ADAPTER.md"):
                for f in sorted(glob.glob(os.path.join(instance, "tool-skills", plane, "*", name))):
                    out.append(skill_card(f, plane, "local", root))
    homed = homed_sections(root)
    for c in out:
        # only library methods declare a section id; an adapter's `produces` is prose about a
        # deliverable, so "is it homed in a step artifact" does not apply to it
        secs = ([p for p in c["produces"] if not T.is_file_produces(p)]
                if c["plane"] == "library" else [])
        c["homeless"] = [p for p in secs if p not in homed]
        if c["plane"] == "adapters":
            c["produces"] = [T.plain(p)[:200] for p in c["produces"]]
    return out


def homed_sections(root=ROOT):
    """Every section id that has a real home in a step artifact (a step template {#id})."""
    homed = set()
    for tpl in glob.glob(os.path.join(root, "steps", "*", "template.md")):
        homed |= T.section_ids(T.read(tpl))
    return homed


# ---------------------------------------------------------------- canon enums

# label -> (allowed values, canonical column key)
#
# The *values* are canon and never translated. A register's *column header* is written in the
# instance's own language (`config.yaml` → language), so it is found by its language-independent
# **column key** (`<!--c:key-->` on the header) — the register twin of a section `{#anchor}`. There is
# no by-name fallback: a register the console reads must carry its keys (CONVENTIONS → Column keys). The
# old EN/RU header-alias lists are gone — a per-language list is exactly the maintenance trap a key
# removes, and a language it never listed escaped validation silently.
CONFIDENCE = ["assumption", "sourced", "validated", "refuted"]   # ordered for display

ENUMS = {
    "hypothesis type": ({"desirability", "feasibility", "viability", "usability"}, "type"),
    # `superseded`: the hypothesis was split in two, not disproved — closing it as `refuted` would
    # record a falsehood (CONVENTIONS → Links & register item IDs).
    "hypothesis status": ({"open", "testing", "validated", "refuted", "superseded"}, "status"),
    "hypothesis confidence": (set(CONFIDENCE), "confidence"),
    # Post-test grades (filled only after a readout, so enforced-if-present, not required —
    # see OPTIONAL_ENUM_LABELS in tools/lint.py). `signal` grades the observed market response;
    # `decision` is the call it drives — a `reject`/`research` triggers an upward revisit like a
    # refuted bet. Both are gradations, orthogonal to the confirmation marker (CONVENTIONS).
    "hypothesis signal": ({"weak", "medium", "strong"}, "signal"),
    "hypothesis decision": ({"scale", "iterate", "reject", "research"}, "decision"),
    "risk category": ({"market", "product", "execution", "legal", "financial", "dependency"}, "category"),
    # Lifecycle superset: `contained` (mitigated but still live) and `realized` (the risk fired)
    # extend the old open/mitigating/closed; `accepted` stays the off-cycle disposition (carried
    # un-mitigated on purpose).
    "risk status": ({"open", "mitigating", "contained", "realized", "closed", "accepted"}, "status"),
    "metric kind": ({"measured", "derived"}, "kind"),
    "metric instrumentation": ({"instrumented", "proxy", "not-instrumented"}, "instrumentation"),
}

TICK_VALUES = ["done", "open", "n/a", "deferred"]
