"""The dependency graph — assembled from what the read layer already reads, stored nowhere.

Two graphs, one shape (`{"nodes": [...], "edges": [...]}`), both built here so the console and any
later check read the same edges:

- **the product graph** (`instance_graph`) — one instance: its artifact sections and its register
  rows as nodes; `rests-on` markers, register ids named in a section, a feature's `serves` /
  `surface` cells and a metric node's `parent` as edges. Every one of those is a fact a file already
  states (CONVENTIONS → Section confirmation · REGISTERS); nothing is inferred from prose. One edge
  kind is derived rather than stated and is marked as such: `implied` — the section's own card reads
  a neighbouring section (the step README's skeleton names the card, the card's `reads` atoms name
  the sections). Inside a step the templates carry almost no `rests-on` marker (step 1 carries none),
  so without it the step's internal dependencies — which the cards do declare — would be invisible.
- **the method graph** (`framework_graph`) — the framework itself: the step sections of the
  templates, every card the agent can reach, and the six registers; edges are the cards' `reads` /
  `writes` atoms (reference/card-schema.md → one atom grammar). It is the same for every instance.

Node ids are prefixed so the two graphs can never collide in a reader: `s:<step>#<anchor>` a
section · `r:<ID>` a register row · `c:<name>` a card · `g:<register>` a register file.
"""
from . import cards
from . import text as T

# the cell a row is titled by, per register (REGISTERS.md → the schemas)
TITLE_COL = {"hypotheses": "statement", "risks": "description", "metrics": "name",
             "features": "name", "surfaces": "name"}
STATE_COL = {"hypotheses": "status", "risks": "status", "metrics": "instrumentation",
             "features": "state", "surfaces": "state"}
# ids are matched through the read layer's one table of grammars (text.ID_RES), so a cell that
# counts as a reference for the linter counts as an edge here — and nowhere else is a second grammar
_ids = T.register_ids


def _section_status(sec):
    if sec.get("contested"):
        return "contested"
    if sec.get("confirmed"):
        return "confirmed"
    if sec.get("open"):
        return "open"
    if (sec.get("words") or 0) > 0:
        return "written"
    return "empty"


# ---------------------------------------------------------------- the product graph


def instance_graph(artifacts, registers, steps=None, skills=None):
    """Sections and register rows of one instance, with the edges their files state.

    `artifacts` and `registers` are the structures `instance.load` already built — the graph is a
    view over them, so the console cannot show an edge the files do not carry. `steps` (with their
    skeletons) and `skills` (the cards) add the one derived kind, `implied`; without them the graph
    holds stated edges only.
    """
    nodes, edges, seen = [], [], set()

    def node(nid, **kw):
        if nid in seen:
            return
        seen.add(nid)
        nodes.append(dict(id=nid, **kw))

    def edge(src, dst, kind):
        edges.append({"from": src, "to": dst, "kind": kind})

    # register rows first, so a section's reference can be checked against a real row
    rows_by_id = {}
    for reg_key, reg in (registers or {}).items():
        kind = "metrics" if reg_key == "metric_tree" else reg_key
        for row in reg.get("rows") or []:
            rid = str(row.get("id") or "").strip()
            if not rid:
                continue
            rows_by_id[rid] = (kind, row)
            node("r:" + rid, kind=kind, label=rid,
                 title=str(row.get(TITLE_COL[kind]) or "").strip(),
                 state=str(row.get(STATE_COL[kind]) or "").strip(),
                 reg=reg.get("file", ""))

    # sections, in artifact order — the file order is the pipeline order
    sec_ids = set()
    for art in artifacts or []:
        for sec in art.get("sections") or []:
            if not sec.get("id"):
                continue
            sid = "%d#%s" % (art.get("step", 0), sec["id"])
            sec_ids.add(sid)
            node("s:" + sid, kind="section", label=sec["id"], title=sec.get("title") or sec["id"],
                 step=art.get("step", 0), file=art.get("file", ""), anchor=sec["id"],
                 status=_section_status(sec), gaps=len(sec.get("gaps") or []),
                 words=sec.get("words") or 0, card=sec.get("card") or "")

    # edges: rests-on (upstream → this section), and register ids a section names
    for art in artifacts or []:
        for sec in art.get("sections") or []:
            if not sec.get("id"):
                continue
            me = "s:%d#%s" % (art.get("step", 0), sec["id"])
            for tgt in sec.get("rests_on") or []:
                if tgt in sec_ids:
                    edge("s:" + tgt, me, "rests")
                else:
                    # a marker naming a section the instance has not written yet — still a fact
                    node("s:" + tgt, kind="section", label=tgt.split("#", 1)[1], title=tgt,
                         step=int(tgt.split("#", 1)[0] or 0), file="", anchor=tgt.split("#", 1)[1],
                         status="missing", gaps=0, words=0, card="")
                    edge("s:" + tgt, me, "rests")
            m = sec.get("markers") or {}
            for k in ("hypotheses", "risks", "metrics", "features", "surfaces"):
                for rid in m.get(k) or []:
                    if rid in rows_by_id:
                        edge(me, "r:" + rid, "ref")

    # edges inside the registers: serves, surface, parent
    for rid, (kind, row) in rows_by_id.items():
        if kind == "features":
            for tgt in _ids(row.get("serves")):
                if tgt in rows_by_id:
                    edge("r:" + rid, "r:" + tgt, "serves")
            for tgt in _ids(row.get("surface")):
                if tgt in rows_by_id:
                    edge("r:" + rid, "r:" + tgt, "on")
        if kind == "metrics":
            for tgt in _ids(row.get("parent")):
                if tgt in rows_by_id and tgt != rid:
                    edge("r:" + rid, "r:" + tgt, "parent")
        if kind == "hypotheses":
            for tgt in _ids(row.get("test")):
                if tgt in rows_by_id and tgt != rid:
                    edge("r:" + rid, "r:" + tgt, "test")

    # implied: the section's card reads a sibling section. The card is the one the step README's
    # skeleton names for the section (not `sec["card"]` — that is the card-face text, not a name),
    # taken only when the card runs at this step (`cjm-strategy` is listed on `1#cjm` as a Step-3
    # revisit and would otherwise pull Step-3 sections into Step 1). Both ends must be sections the
    # instance has written — a prescription is drawn between facts, never made into a `missing` node —
    # and a pair already stated by a `rests-on` marker is not drawn twice.
    stated = {(e["from"], e["to"]) for e in edges if e["kind"] == "rests"}
    for src, dst in _implied_pairs(steps, skills):
        if src in sec_ids and dst in sec_ids and ("s:" + src, "s:" + dst) not in stated:
            stated.add(("s:" + src, "s:" + dst))
            edge("s:" + src, "s:" + dst, "implied")

    return _with_degree(nodes, edges)


def _implied_pairs(steps, skills):
    """`(Y, X)` for every card the skeleton names on section X that reads section Y, both as
    `<step>#<anchor>`; a section's step comes from the skeleton that lists it."""
    if not steps or not skills:
        return []
    step_of, cards_on = {}, {}
    for st in steps:
        for sec in st.get("skeleton") or []:
            step_of[sec["id"]] = st["step"]
            cards_on["%d#%s" % (st["step"], sec["id"])] = list(sec.get("tools") or [])
    by_name = {c["name"]: c for c in skills}
    out = []
    for dst, names in cards_on.items():
        step = int(dst.split("#", 1)[0])
        for name in names:
            c = by_name.get(name)
            if not c or str(step) not in [str(s) for s in c.get("steps") or []]:
                continue
            for atom in c.get("reads") or []:
                head, arg = cards.split_atom(atom)
                if head == "section" and arg and arg != "*" and arg in step_of:
                    src = "%d#%s" % (step_of[arg], arg)
                    if src != dst:
                        out.append((src, dst))
    return out


def _with_degree(nodes, edges):
    deg = {}
    for e in edges:
        deg[e["from"]] = deg.get(e["from"], 0) + 1
        deg[e["to"]] = deg.get(e["to"], 0) + 1
    for n in nodes:
        n["degree"] = deg.get(n["id"], 0)
    return {"nodes": nodes, "edges": edges}


# ---------------------------------------------------------------- the method graph


def framework_graph(steps, skills):
    """The template sections, the cards and the registers, joined by the cards' atoms.

    `steps` is `framework.steps()` (each with its skeleton: section id → recommended tools),
    `skills` is `framework.skills()` (each card with `reads` / `writes` as atoms).
    """
    nodes, edges, seen = [], [], set()

    def node(nid, **kw):
        if nid in seen:
            return
        seen.add(nid)
        nodes.append(dict(id=nid, **kw))

    def edge(src, dst, kind):
        edges.append({"from": src, "to": dst, "kind": kind})

    step_of = {}
    for st in steps or []:
        for sec in st.get("skeleton") or []:
            step_of[sec["id"]] = st["step"]
            node("s:%d#%s" % (st["step"], sec["id"]), kind="section", label=sec["id"],
                 title=sec.get("what") or sec["id"], step=st["step"], anchor=sec["id"],
                 optional=bool(sec.get("optional")), tools=list(sec.get("tools") or []))
    for name in ("hypotheses", "risks", "metrics", "metric-tree", "features", "surfaces"):
        node("g:" + name, kind="register", label=name, title="registers/%s" % name)

    by_name = {}
    for c in skills or []:
        by_name[c["name"]] = c
        node("c:" + c["name"], kind="card", label=c["name"], title=c.get("summary") or c["name"],
             plane=c.get("plane", ""), card_kind=c.get("kind", ""), origin=c.get("origin", ""),
             steps=[int(s) for s in c.get("steps") or [] if str(s).isdigit()])

    for c in skills or []:
        me = "c:" + c["name"]
        for atom in c.get("writes") or []:
            head, arg = cards.split_atom(atom)
            if head == "section" and arg and arg != "*" and arg in step_of:
                edge(me, "s:%d#%s" % (step_of[arg], arg), "writes")
            elif head == "register" and arg and arg != "*":
                edge(me, "g:" + arg, "writes")
        for atom in c.get("reads") or []:
            head, arg = cards.split_atom(atom)
            if head == "section" and arg and arg != "*" and arg in step_of:
                edge("s:%d#%s" % (step_of[arg], arg), me, "reads")
            elif head == "register" and arg and arg != "*":
                edge("g:" + arg, me, "reads")
            elif head == "worklog" and arg and arg != "*":
                # `worklog:1-concept/cjm-concept` — the one legal foreign-worklog input
                other = arg.rsplit("/", 1)[-1]
                if other in by_name:
                    edge("c:" + other, me, "worklog")

    return _with_degree(nodes, edges)
