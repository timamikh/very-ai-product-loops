"""The product side of the read model: one instance folder, read into a single structure.

Reads only. Everything the local UI shows comes from here, so there is exactly one interpretation of
an instance on disk. Tolerant by design: real instances drift from the canon (an older one has no
`state.yaml`, or artifacts without the number prefix), and the reader must *show* the drift rather
than crash on it — every deviation lands in `health` instead of an exception.
"""
import csv
import glob
import io
import os
import re

from . import framework as F
from . import text as T
from . import yamlite

ARTIFACT_TYPES = ("artifact",)


# ---------------------------------------------------------------- discovery


def has_artifacts(path):
    """True when this folder itself carries step artifacts (files with `node_type: artifact`)."""
    for f in glob.glob(os.path.join(path, "*.md")):
        try:
            fm, _ = T.frontmatter(f)
        except OSError:
            continue
        if fm.get("node_type") in ARTIFACT_TYPES:
            return True
    return False


def sub_instances(path):
    """Sub-product folders of a multi-product instance (`products:` in the parent config.yaml).

    A real layout in the wild: `product/config.yaml` declares three products, each with its own
    numbered artifacts, `state.yaml` and `registers/` in a subfolder, and one shared `sources/`.
    """
    out = []
    for d in sorted(glob.glob(os.path.join(path, "*"))):
        if os.path.isdir(d) and os.path.basename(d) not in ("registers", "sources", "deliverables",
                                                            "briefs", "variants") \
                and not os.path.basename(d).startswith("."):
            if has_artifacts(d) or os.path.exists(os.path.join(d, "state.yaml")):
                out.append(d)
    return out


def looks_like_instance(path):
    if not os.path.isdir(path):
        return False
    if os.path.exists(os.path.join(path, "config.yaml")):
        return True
    if os.path.exists(os.path.join(path, "state.yaml")) or has_artifacts(path):
        return True
    return os.path.isdir(os.path.join(path, "registers")) and bool(
        glob.glob(os.path.join(path, "*.md"))
    )


def describe(path):
    """One candidate: its kind of layout and, for an umbrella, its sub-products."""
    p = os.path.abspath(path)
    subs = sub_instances(p)
    umbrella = bool(subs) and not has_artifacts(p)
    return {
        "path": p,
        "name": os.path.basename(p),
        "umbrella": umbrella,
        "children": [{"path": s, "name": os.path.basename(s)} for s in subs] if umbrella else [],
    }


def discover(start, framework_root=F.ROOT):
    """Candidate instances, most canonical first.

    Canon: the instance lives in `product/` of the host repo the framework was installed into.
    A framework dev-repo also carries `instances/<name>/` (private live data) and `examples/<name>/`.
    Each candidate is reported with the rule that matched; a multi-product instance also contributes
    its sub-products, since those are where the artifacts actually live.
    """
    found, seen = [], set()

    def add(path, kind):
        p = os.path.abspath(path)
        if p in seen or not looks_like_instance(p):
            return
        seen.add(p)
        d = describe(p)
        found.append(dict(d, kind="umbrella" if d["umbrella"] else kind))
        for child in d["children"]:
            if child["path"] not in seen:
                seen.add(child["path"])
                found.append(dict(describe(child["path"]), kind="sub-product"))

    start = os.path.abspath(start)
    add(start, "explicit")
    add(os.path.join(start, "product"), "product")
    for p in sorted(glob.glob(os.path.join(start, "instances", "*"))):
        add(p, "instance")
    for p in sorted(glob.glob(os.path.join(framework_root, "instances", "*"))):
        add(p, "instance")
    add(os.path.join(framework_root, "product"), "product")
    for p in sorted(glob.glob(os.path.join(framework_root, "examples", "*"))):
        add(p, "example")
    return found


# ---------------------------------------------------------------- pieces


# config.yaml key aliases. The canon fixes *which decisions* live in config.yaml (product, language,
# active status, directions, metric source slots) but never pinned the exact key spelling, so real
# instances drift: `metric_sources` vs `metric_source_slots`, `product_scope` vs `scope_note`. The
# reader accepts the observed spellings and reports the drift, so the console never shows an empty
# field for data that is right there under another name.
CONFIG_ALIASES = {
    "product": ("product", "title", "name"),
    "language": ("language", "lang"),
    "active_status": ("active_status", "status"),
    "directions": ("directions",),
    "scope_note": ("scope_note", "scope", "product_scope"),
    "metric_source_slots": ("metric_source_slots", "metric_sources", "metric_slots"),
    "sources": ("sources", "sources_dir"),
}
CANON_KEYS = {"product": "product", "language": "language", "active_status": "active_status",
              "directions": "directions", "scope_note": "scope_note",
              "metric_source_slots": "metric_source_slots", "sources": "sources"}


def _flatten(v):
    """A config value that came in as a nested map (e.g. `product_scope: {in:…, out:…}`) as text."""
    if isinstance(v, dict):
        return " · ".join("%s: %s" % (k, _flatten(x)) for k, x in v.items() if x)
    if isinstance(v, list):
        return ", ".join(str(x) for x in v)
    return "" if v is None else str(v)


def _read_yaml(path, label, health):
    data, skipped = yamlite.load(path)
    for ln, raw in skipped:
        health.append({"level": "warn", "code": "yaml-unsupported",
                       "message": "%s line %d not understood by the reader: %s" % (label, ln, raw.strip())})
    return data


def _read_config(path, health):
    """Normalized config for this folder, inheriting a parent instance's config where absent.

    A sub-product of a multi-product instance has no `config.yaml` of its own — the shared decisions
    (language, status, directions) live in the parent, and the parent's `products:` map names it. That
    is a real layout, so the reader resolves it instead of showing a nameless, language-less instance.
    """
    own_file = os.path.join(path, "config.yaml")
    own = _read_yaml(own_file, "config.yaml", health) if os.path.exists(own_file) else {}

    parent_dir = os.path.dirname(path)
    parent_file = os.path.join(parent_dir, "config.yaml")
    parent = {}
    entry = {}
    if not own and os.path.exists(parent_file):
        parent = _read_yaml(parent_file, "../config.yaml", health)
        products = parent.get("products") or {}
        if isinstance(products, dict):
            entry = products.get(os.path.basename(path)) or {}

    if not own and not parent:
        health.append({"level": "warn", "code": "no-config",
                       "message": "config.yaml is missing — the human's decisions (product, status, "
                                  "language, directions, metric source slots) have no home"})

    def pick(canon):
        for src in (own, entry, parent):
            for alias in CONFIG_ALIASES[canon]:
                if src.get(alias) not in (None, "", [], {}):
                    return src[alias], alias
        return None, None

    out, used = {}, {}
    for canon in CONFIG_ALIASES:
        val, alias = pick(canon)
        out[canon] = val
        if alias:
            used[canon] = alias
    out["scope_note"] = _flatten(out.get("scope_note"))
    for canon, alias in used.items():
        if alias != CANON_KEYS[canon]:
            health.append({"level": "warn", "code": "config-key",
                           "message": "config.yaml spells `%s` as `%s` — read it anyway, but the canon "
                                      "key is `%s` (one mechanism, one way: a second spelling is a "
                                      "place two readers diverge)" % (canon, alias, CANON_KEYS[canon])})
    out["_inherited_from"] = parent_dir if (not own and parent) else None
    out["_entry"] = entry
    out["_present"] = bool(own or parent)
    return out


def _read_state(path, health):
    f = os.path.join(path, "state.yaml")
    if not os.path.exists(f):
        health.append({"level": "warn", "code": "no-state",
                       "message": "state.yaml is missing — the cycle's position and gate ticks are not "
                                  "recorded, so a fresh session cannot resume without asking "
                                  "(process/OPERATING-LOOP.md step 0)"})
        return {}, False
    data, skipped = yamlite.load(f)
    for ln, raw in skipped:
        health.append({"level": "warn", "code": "yaml-unsupported",
                       "message": "state.yaml line %d not understood by the reader: %s" % (ln, raw.strip())})
    return data, True


def _artifacts(path, health):
    out = []
    for f in sorted(glob.glob(os.path.join(path, "*.md"))):
        base = os.path.basename(f)
        fm, raw = T.frontmatter(f)
        if fm.get("node_type") not in ARTIFACT_TYPES:
            continue
        secs = []
        for s in T.sections(raw):
            if not s["id"]:
                continue
            body = s["body"]
            secs.append(dict({
                "id": s["id"],
                "title": s["title"],
                "words": len(body.split()),
                "markers": T.markers(body),
                "gaps": T.to_clarify_lines(body),
                "card": T.card_line(body),
                "confirmed": T.confirmed(body),
                "open": T.is_open(body),
                "body": body,
            }, **T.digest(body)))
        if not re.match(r"^\d+-", base):
            health.append({"level": "warn", "code": "artifact-unnumbered",
                           "message": "%s has no step-number prefix — canon is `<step>-<slug>.md` so a "
                                      "folder listing walks the pipeline in order (CONVENTIONS → "
                                      "Artifact filenames)" % base})
        if not T.change_log(raw):
            health.append({"level": "warn", "code": "no-change-log",
                           "message": "%s has no change log — the `artifact` row of the CONVENTIONS "
                                      "matrix requires one (date · from→to · why · trigger), and "
                                      "without it the motivation behind the current state is lost" % base})
        out.append({
            "file": base,
            "artifact": fm.get("artifact", re.sub(r"^\d+-", "", base).replace(".md", "")),
            "step": int(fm.get("step", 0) or 0),
            "title": fm.get("title", ""),
            "updated": fm.get("updated", ""),
            "version": fm.get("version", ""),
            "status_stage": fm.get("status_stage", ""),
            "owner": fm.get("owner", ""),
            "sections": secs,
            "change_log": T.change_log(raw),
        })
    out.sort(key=lambda a: (a["step"], a["file"]))
    return out


def _register(path, filename, id_prefix, health, enum_checks=()):
    """One register file → rows + enum validation.

    `enum_checks` items are (column-aliases, allowed values, label). Aliases exist because an
    instance's registers are written in the product's own language (`config.yaml` → language), so the
    same canonical column is `Type` in one instance and `Тип` in another — the *values* stay canon.
    """
    f = os.path.join(path, "registers", filename)
    if not os.path.exists(f):
        return {"present": False, "file": filename, "columns": [], "rows": []}
    raw = T.read(f)
    headers, rows = None, []
    for t in T.tables(raw):
        hs = [h.lower() for h in t["headers"]]
        if "id" in hs:
            headers = hs
            for r in t["rows"]:
                row = {hs[i]: (r[i] if i < len(r) else "") for i in range(len(hs))}
                if T.clean_cell(row.get("id", "")).startswith(id_prefix):
                    rows.append(row)
            break
    for aliases, allowed, label in enum_checks:
        col = next((a for a in aliases if headers and a in headers), None)
        if col is None:
            health.append({"level": "warn", "code": "register-column",
                           "message": "%s has no `%s` column — %s cannot be validated"
                                      % (filename, aliases[0], label)})
            continue
        for r in rows:
            v = T.enum_value(r.get(col, ""))
            if not v:
                continue
            if v not in allowed:
                health.append({"level": "error", "code": "enum",
                               "message": "%s · %s: %s = `%s` is not one of %s (a qualifier belongs "
                                          "in `note`, a cross-cutting theme in `tags` — never "
                                          "compounded into the value)"
                                          % (filename, T.clean_cell(r.get("id", "?")), col, v,
                                             ", ".join(sorted(allowed)))})
    return {"present": True, "file": filename, "columns": headers or [], "rows": rows}


def _metrics(path, tree_rows, health):
    f = os.path.join(path, "registers", "metrics.csv")
    defined = {T.clean_cell(r.get("id", "")) for r in tree_rows}
    series, rows_n, undefined = {}, 0, set()
    if not os.path.exists(f):
        return {"present": False, "series": {}, "rows": 0, "undefined": []}
    with io.open(f, encoding="utf-8", newline="") as fh:
        for row in csv.DictReader(fh):
            mid = (row.get("id") or "").strip()
            if not mid:
                continue
            rows_n += 1
            if defined and mid not in defined:
                undefined.add(mid)
            try:
                value = float((row.get("value") or "").strip())
            except ValueError:
                value = None
            series.setdefault(mid, []).append({
                "period_start": (row.get("period_start") or "").strip(),
                "period_end": (row.get("period_end") or "").strip(),
                "measured_at": (row.get("measured_at") or "").strip(),
                "value": value,
                "raw_value": (row.get("value") or "").strip(),
                # observed_n / population arrived after the first instances were written, and
                # csv.DictReader is header-driven, so an older file simply reports them empty.
                "observed_n": (row.get("observed_n") or "").strip(),
                "population": (row.get("population") or "").strip(),
                "basis": (row.get("basis") or "").strip(),
                "source": (row.get("source") or "").strip(),
                "note": (row.get("note") or "").strip(),
            })
    for mid in series:
        series[mid].sort(key=lambda r: (r["period_end"] or r["measured_at"], r["measured_at"]))
    for mid in sorted(undefined):
        health.append({"level": "error", "code": "metric-undefined",
                       "message": "metrics.csv carries readings for `%s`, which has no definition in "
                                  "metric-tree.md — an orphan series nobody can interpret "
                                  "(REGISTERS → the md file is the authority on which ids exist)" % mid})
    return {"present": True, "series": series, "rows": rows_n, "undefined": sorted(undefined)}


def _sources(path):
    idx = os.path.join(path, "sources", "INDEX.md")
    rows, indexed = [], set()
    if os.path.exists(idx):
        raw = T.read(idx)
        for t in T.tables(raw):
            hs = [h.lower() for h in t["headers"]]
            if not hs or "|".join(hs).count("|") < 2:
                continue
            first = hs[0]
            for r in t["rows"]:
                row = {hs[i]: (r[i] if i < len(r) else "") for i in range(len(hs))}
                name = T.clean_cell(row.get(first, ""))
                if name.endswith(".md"):
                    indexed.add(name)
                    rows.append({"file": name, "cells": row})
            break
    files = []
    for f in sorted(glob.glob(os.path.join(path, "sources", "*.md"))):
        base = os.path.basename(f)
        if base == "INDEX.md":
            continue
        fm, _ = T.frontmatter(f)
        files.append({
            "file": base,
            "node_type": fm.get("node_type", ""),
            "updated": fm.get("updated", ""),
            "indexed": base in indexed,
        })
    return {
        "index_present": os.path.exists(idx),
        "index_columns": list(rows[0]["cells"].keys()) if rows else [],
        "index": rows,
        "files": files,
    }


def _history(timeline):
    """The trail of one register item: every change-log entry that names its id, keyed by id.

    Assembled, never stored a second time. The entries already exist in the artifacts' and registers'
    change logs, and the requirement that a register entry names the ids it moved (CONVENTIONS →
    Change logs) is what makes the assembly reliable rather than lucky. This is why a per-item
    journal column is not needed: the mechanism that carries the reasoning already carries the id.
    """
    out = {}
    for e in timeline:                                   # already newest-first
        mk = T.markers("%s\n%s" % (e["summary"], e["body"]))
        for iid in mk["hypotheses"] + mk["risks"] + mk["metrics"]:
            out.setdefault(iid, []).append({"date": e["date"], "summary": e["summary"],
                                            "file": e["file"], "kind": e["kind"]})
    return out


def _handoff(path):
    f = os.path.join(path, "HANDOFF.md")
    if not os.path.exists(f):
        return {"present": False}
    fm, raw = T.frontmatter(f)
    return {
        "present": True,
        "updated": fm.get("updated", ""),
        "sections": [{"id": s["id"], "title": s["title"], "body": s["body"]}
                     for s in T.sections(raw) if s["id"] or s["title"]],
        "change_log": T.change_log(raw),
    }


# ---------------------------------------------------------------- gates & steps


def _tick_map(state):
    """Flatten `state.yaml` gates into {tick_id: value}, accepting `1-idea` or `1` as the step key."""
    gates = (state or {}).get("gates") or {}
    flat = {}
    per_step = {}
    if isinstance(gates, dict):
        for step_key, items in gates.items():
            if not isinstance(items, dict):
                continue
            m = re.match(r"^(\d+)", str(step_key))
            n = int(m.group(1)) if m else None
            for tick, val in items.items():
                flat[str(tick)] = str(val).strip() if val is not None else "open"
                if n:
                    per_step.setdefault(n, {})[str(tick)] = flat[str(tick)]
    return flat, per_step


def _merge_steps(steps, artifacts, state, health):
    ticks, _ = _tick_map(state)
    by_step = {a["step"]: a for a in artifacts}
    out = []
    for s in steps:
        art = by_step.get(s["step"])
        present_sections = {sec["id"] for sec in (art or {}).get("sections", [])}
        gate = []
        for item in s["gate"]:
            tick = ticks.get(item["tick_id"]) if item["tick_id"] else None
            written = bool(item["sections"]) and all(sid in present_sections for sid in item["sections"])
            gate.append(dict(item, tick=tick or ("unknown" if not state else "open"), written=written))
        counts = {}
        for g in gate:
            counts[g["tick"]] = counts.get(g["tick"], 0) + 1
        sections = []
        for sk in s["skeleton"]:
            sec = next((x for x in (art or {}).get("sections", []) if x["id"] == sk["id"]), None)
            sections.append({
                "id": sk["id"],
                "what": sk["what"],
                "tools": sk["tools"],
                "optional": sk["optional"],
                "present": sec is not None,
                "words": sec["words"] if sec else 0,
                "gaps": len(sec["gaps"]) if sec else 0,
                "gap_lines": (sec["gaps"] if sec else []),
                "confidence": sec["markers"]["confidence"] if sec else {},
                "proposals": sec["markers"]["proposals"] if sec else 0,
                "ids": ((sec["markers"]["hypotheses"] + sec["markers"]["risks"]
                         + sec["markers"]["metrics"]) if sec else []),
                "lead": sec["lead"] if sec else "",
                "bullets": sec["bullets"] if sec else [],
                "table_rows": sec["table_rows"] if sec else 0,
                "title": sec["title"] if sec else "",
                "confirmed": sec["confirmed"] if sec else None,
                "open": bool(sec["open"]) if sec else False,
            })
        for sec in (art or {}).get("sections", []):
            if sec["id"] not in {x["id"] for x in sections} and sec["id"] != "change-log":
                sections.append({"id": sec["id"], "what": "", "tools": [], "optional": False,
                                 "present": True, "words": sec["words"], "gaps": len(sec["gaps"]),
                                 "gap_lines": sec["gaps"],
                                 "confidence": sec["markers"]["confidence"],
                                 "proposals": sec["markers"]["proposals"],
                                 "ids": (sec["markers"]["hypotheses"] + sec["markers"]["risks"]
                                         + sec["markers"]["metrics"]),
                                 "lead": sec["lead"], "bullets": sec["bullets"],
                                 "table_rows": sec["table_rows"], "title": sec["title"],
                                 "confirmed": sec["confirmed"],
                                 "open": bool(sec["open"]),
                                 "off_skeleton": True})
        out.append(dict(s, artifact_file=(art or {}).get("file"), artifact_updated=(art or {}).get("updated", ""),
                        gate=gate, gate_counts=counts, sections=sections))
    return out


# ---------------------------------------------------------------- the model


def _worklogs(path):
    """Step-folder worklogs, keyed by step-stem then tool id (CONVENTIONS → Step folders & worklogs).

    A worklog `<step-folder>/<tool>.md` is the source of truth a section projects from; the console
    lets a board block drill into it. Only `node_type: worklog` files are taken — a stray file in the
    folder is not silently shown as one (the linter's check P flags it instead).
    """
    out = {}
    for art in sorted(glob.glob(os.path.join(path, "[1-6]-*.md"))):
        stem = os.path.basename(art)[:-3]
        folder = os.path.join(path, stem)
        if not os.path.isdir(folder):
            continue
        logs = {}
        for wl in sorted(glob.glob(os.path.join(folder, "*.md"))):
            fm, raw = T.frontmatter(wl)
            if fm.get("node_type") != "worklog":
                continue
            tool = os.path.basename(wl)[:-3]
            body = T.body_after_frontmatter(raw)
            logs[tool] = {
                "tool": tool,
                "file": "%s/%s" % (stem, os.path.basename(wl)),
                "title": fm.get("title", "") or tool,
                "updated": fm.get("updated", ""),
                "words": len(body.split()),
                "markers": T.markers(body),
                "body": body,
            }
        if logs:
            out[stem] = logs
    return out


def load(path, framework_root=F.ROOT):
    """Read one instance into a single JSON-serialisable structure."""
    path = os.path.abspath(path)
    health = []
    config = _read_config(path, health)
    state, state_present = _read_state(path, health)
    artifacts = _artifacts(path, health)

    def check(label):
        allowed, aliases = F.ENUMS[label]
        return (aliases, allowed, label)

    hypotheses = _register(path, "hypotheses.md", "H-", health,
                           [check("hypothesis type"), check("hypothesis status"),
                            check("hypothesis confidence")])
    risks = _register(path, "risks.md", "R-", health, [check("risk category"), check("risk status")])
    metric_tree = _register(path, "metric-tree.md", "M-", health,
                            [check("metric kind"), check("metric instrumentation")])
    metrics = _metrics(path, metric_tree["rows"], health)

    steps = _merge_steps(F.steps(framework_root), artifacts, state, health)

    gaps = []
    for a in artifacts:
        for sec in a["sections"]:
            for line in sec["gaps"]:
                gaps.append({"file": a["file"], "section": sec["id"], "title": sec["title"], "line": line})

    timeline = []
    for a in artifacts:
        for e in a["change_log"]:
            timeline.append(dict(e, file=a["file"], kind="artifact"))
    for reg, label in ((hypotheses, "hypotheses.md"), (risks, "risks.md"), (metric_tree, "metric-tree.md")):
        if not reg["present"]:
            continue
        entries = T.change_log(T.read(os.path.join(path, "registers", reg["file"])))
        if not entries:
            health.append({"level": "warn", "code": "no-change-log",
                           "message": "registers/%s has no change log — the `register` row of the "
                                      "CONVENTIONS matrix requires one" % label})
        for e in entries:
            timeline.append(dict(e, file="registers/" + label, kind="register"))
    timeline.sort(key=lambda e: e["date"], reverse=True)

    active_status = config.get("active_status") or ""
    statuses = F.statuses(framework_root)
    status = next((s for s in statuses if s["name"] == active_status), None)

    deliverables = [os.path.basename(f) for f in sorted(glob.glob(os.path.join(path, "deliverables", "*")))
                    if not os.path.basename(f).startswith(".")]

    product = config.get("product")
    if not product:
        product = os.path.basename(path)
        if config.get("_present"):
            health.append({"level": "warn", "code": "no-product-name",
                           "message": "config.yaml never names the product, so the console falls back to "
                                      "the folder name (%s) — add `product: \"…\"`" % product})

    shared = _sources(path)
    if not shared["files"] and not shared["index_present"] and config.get("_inherited_from"):
        shared = _sources(config["_inherited_from"])   # a sub-product shares the parent's sources/

    return {
        "path": path,
        "name": os.path.basename(path),
        "product": product,
        "language": config.get("language") or "en",
        "active_status": active_status,
        "directions": T.as_list(config.get("directions")),
        "scope_note": config.get("scope_note") or "",
        "metric_source_slots": config.get("metric_source_slots") or {},
        "config_sources": T.as_list(config.get("sources")),
        "config_present": bool(config.get("_present")),
        "config_inherited_from": config.get("_inherited_from"),
        "children": [c["name"] for c in describe(path)["children"]],
        "umbrella": describe(path)["umbrella"],
        "goal": (config.get("_entry") or {}).get("goal", ""),
        "audience": (config.get("_entry") or {}).get("users", ""),
        "state_present": state_present,
        "current_step": (state or {}).get("current_step"),
        "last_pass": (state or {}).get("last_pass"),
        "status": status,
        "statuses": [{"name": s["name"], "order": s["order"]} for s in statuses],
        "steps": steps,
        "artifacts": artifacts,
        "registers": {"hypotheses": hypotheses, "risks": risks, "metric_tree": metric_tree},
        "metrics": metrics,
        "sources": shared,
        "worklogs": _worklogs(path),
        "handoff": _handoff(path),
        "deliverables": deliverables,
        "gaps": gaps,
        "timeline": timeline,
        "history": _history(timeline),
        "health": health,
    }
