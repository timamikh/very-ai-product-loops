"""Markdown & frontmatter primitives — the canon's notation, parsed in one place.

Deliberately minimal (stdlib only, single-line frontmatter values, no markdown AST): the canon is
written to be greppable, and every consumer must see the *same* interpretation of it.
"""
import os
import re

# ---------------------------------------------------------------- files


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def rel(path, root):
    return os.path.relpath(path, root)


# ---------------------------------------------------------------- frontmatter


def parse_scalar(v):
    v = v.strip()
    if v.startswith("[") and v.endswith("]"):
        inner = v[1:-1].strip()
        return [] if not inner else [x.strip().strip('"').strip("'") for x in inner.split(",")]
    return v.strip('"').strip("'")


def frontmatter(path):
    """Minimal `key: value` frontmatter parse (top-level, single-line values only).

    Returns (dict, full_text) — callers usually want both.
    """
    text = read(path)
    return frontmatter_from(text), text


def frontmatter_from(text):
    m = re.match(r"^---\n(.*?)\n---", text, re.S)
    fm = {}
    if m:
        for line in m.group(1).splitlines():
            mm = re.match(r"^([A-Za-z_][A-Za-z0-9_]*):\s*(.*)$", line)
            if mm:
                fm[mm.group(1)] = parse_scalar(mm.group(2))
    return fm


def body_after_frontmatter(text):
    m = re.match(r"^---\n.*?\n---\n?", text, re.S)
    return text[m.end():] if m else text


def as_list(v):
    if v is None or v == "":
        return []
    return v if isinstance(v, list) else [v]


# ---------------------------------------------------------------- sections


def section_ids(text):
    """Every stable `{#anchor}` in the text (CONVENTIONS → Section IDs)."""
    return set(re.findall(r"\{#([a-z0-9][a-z0-9-]*)\}", text))


HEADING_RE = re.compile(r"^(#{2,3})\s+(.*?)\s*(?:\{#([a-z0-9][a-z0-9-]*)\})?\s*$", re.M)


def sections(text, level=2):
    """Split a document into its `##` sections, keeping heading text, anchor id and body.

    Returns a list of dicts: {id, title, level, body}. Sections before the first heading are
    returned with id None and title "" (the artifact's preamble).
    """
    body = body_after_frontmatter(text)
    out = []
    marks = [m for m in HEADING_RE.finditer(body) if len(m.group(1)) == level]
    if not marks:
        return [{"id": None, "title": "", "level": level, "body": body.strip()}]
    pre = body[: marks[0].start()].strip()
    if pre:
        out.append({"id": None, "title": "", "level": level, "body": pre})
    for i, m in enumerate(marks):
        end = marks[i + 1].start() if i + 1 < len(marks) else len(body)
        out.append({
            "id": m.group(3),
            "title": m.group(2).strip(),
            "level": level,
            "body": body[m.end():end].strip(),
        })
    return out


# ---------------------------------------------------------------- markdown tables


def clean_cell(v):
    return re.sub(r"[*`]", "", v).strip()


def enum_value(v):
    """A table cell reduced to the canonical enum value it carries, or "" for a gap.

    Confidence is written the same way in a register cell as in prose — `[sourced: metrics W24]` —
    so a checker that compared the raw cell to the enum would reject every correctly written one.
    The bracket is notation and everything after the colon is the *evidence*, not the value.
    """
    s = clean_cell(v)
    m = re.match(r"^\[(.*)\]$", s)
    if m:
        s = m.group(1).strip()
    s = s.split(":", 1)[0].strip()
    return "" if s in ("—", "-", "– to clarify –", "— to clarify —", "- to clarify -") else s


def _is_divider(line):
    return bool(re.match(r"^\s*\|?[\s:|-]+\|?\s*$", line))


def tables(text):
    """Every pipe table in the text as {headers, rows, broken, line}.

    A blank line inside a table is an editing accident, not a second table: markdown renders the
    halves as two tables and a reader barely notices, while a parser that stopped at the blank line
    would silently lose the rest of a register. So the rows resume across blanks — unless what
    follows is a real new table (a header row with its own divider underneath). `broken` records
    that it happened, so the linter can report it instead of the reader guessing.
    """
    lines = text.splitlines()
    out = []
    i = 0
    while i < len(lines):
        s = lines[i].strip()
        if s.startswith("|") and i + 1 < len(lines) and _is_divider(lines[i + 1]):
            headers = [c.strip() for c in s.strip("|").split("|")]
            rows, broken = [], False
            j = i + 2
            while j < len(lines):
                cur = lines[j].strip()
                if cur.startswith("|"):
                    if _is_divider(lines[j]):       # a divider mid-table: a new table's, not ours
                        break
                    rows.append([c.strip() for c in cur.strip("|").split("|")])
                    j += 1
                    continue
                if cur:                             # any other prose ends the table
                    break
                k = j                               # blank line(s): look past them
                while k < len(lines) and not lines[k].strip():
                    k += 1
                if (k < len(lines) and lines[k].strip().startswith("|")
                        and not (k + 1 < len(lines) and _is_divider(lines[k + 1]))):
                    broken = True                   # same table, accidentally split
                    j = k
                    continue
                break
            out.append({"headers": headers, "rows": rows, "broken": broken, "line": i + 1})
            i = j
        else:
            i += 1
    return out


def table_column(text, colname):
    """Values under `colname` across EVERY table in the file that carries it (case-insensitive).

    Reading only the first table is how half a register becomes invisible: a register naturally grows
    a second table (inherited nodes above, newly instrumented ones below, a paragraph between), and a
    first-table-only reader validates the top half while reporting the bottom half's ids as undefined.

    Returns None when no table carries that column — the caller distinguishes "no such column"
    (a schema problem) from "column present but empty".
    """
    target = colname.lower()
    found, vals = False, []
    for t in tables(text):
        headers = [h.lower() for h in t["headers"]]
        if target not in headers:
            continue
        found = True
        idx = headers.index(target)
        vals.extend(r[idx] for r in t["rows"] if len(r) > idx)
    return vals if found else None


def table_rows(text, *required_headers):
    """Rows of EVERY table containing all `required_headers`, as dicts keyed by header.

    Same reason as `table_column`: a register split across two tables is one register. Headers come
    from the first matching table; a later table's own column order is honoured per row.
    """
    want = [h.lower() for h in required_headers]
    first, rows = None, []
    for t in tables(text):
        headers = [h.lower() for h in t["headers"]]
        if not all(w in headers for w in want):
            continue
        if first is None:
            first = headers
        for r in t["rows"]:
            row = {}
            for k, h in enumerate(headers):
                row[h] = r[k] if k < len(r) else ""
            rows.append(row)
    return first, rows


# ---------------------------------------------------------------- canon markers

CONFIDENCE_RE = re.compile(r"\[(assumption|sourced|validated|refuted)(?::[^\]]*)?\]")
TO_CLARIFY_RE = re.compile(r"—\s*to clarify\s*—|—\s*уточнить\s*—")
PROPOSAL_RE = re.compile(r"⚙️")
HYP_RE = re.compile(r"\bH-\d{3}\b")
RISK_RE = re.compile(r"\bR-\d{3}\b")
METRIC_RE = re.compile(r"\bM-[a-z0-9][a-z0-9-]*\b")
LINK_RE = re.compile(r"\[\[[^\]]+\]\]")


def markers(text):
    """Count the canon's inline markers in a chunk of text (CONVENTIONS → tags, gaps, proposals)."""
    conf = {}
    for m in CONFIDENCE_RE.finditer(text):
        conf[m.group(1)] = conf.get(m.group(1), 0) + 1
    return {
        "confidence": conf,
        "to_clarify": len(TO_CLARIFY_RE.findall(text)),
        "proposals": len(PROPOSAL_RE.findall(text)),
        "hypotheses": sorted(set(HYP_RE.findall(text))),
        "risks": sorted(set(RISK_RE.findall(text))),
        "metrics": sorted(set(METRIC_RE.findall(text))),
    }


def to_clarify_lines(text):
    """The actual lines carrying a `— to clarify —` gap, for the open-questions view."""
    return [ln.strip() for ln in text.splitlines() if TO_CLARIFY_RE.search(ln)]


MARKUP_RE = re.compile(r"\*\*|__|`|\{#[a-z0-9-]+\}|<!--.*?-->", re.S)


def _plain(line):
    """A line reduced to its readable sentence: no emphasis, no markers, no anchors."""
    s = MARKUP_RE.sub("", line)
    s = CONFIDENCE_RE.sub("", s)
    s = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", s)   # links keep their text
    s = re.sub(r"^[\s>*+-]*", "", s)
    s = re.sub(r"^\d+\.\s*", "", s)
    return re.sub(r"\s{2,}", " ", s).strip(" _*")


def plain(line):
    """Public alias of the readable-sentence reducer (used for skill summaries and card leads)."""
    return _plain(line)


def digest(body, max_bullets=3, width=190):
    """The gist of a section, for a card in the step canvas.

    A canvas is only useful if its cards say something. The lead line and first bullets are what a
    human would read first anyway; a table's row count stands in for "how much is in here".
    """
    lead, caption, bullets, table_rows, table_head = "", "", [], 0, []
    in_table = False
    for raw in body.splitlines():
        line = raw.strip()
        if not line:
            continue
        if line.startswith("|"):
            cells = [c.strip() for c in line.strip("|").split("|")]
            if re.match(r"^\s*\|?[\s:|-]+\|?\s*$", line):
                in_table = True
                continue
            if not in_table and not table_head:
                table_head = [_plain(c) for c in cells]
            elif in_table:
                table_rows += 1
            continue
        in_table = False
        if line.startswith("<!--"):
            continue
        p = _plain(line)
        if not p or len(p) < 2:
            continue
        if re.match(r"^[-*+]\s", line) or re.match(r"^\d+\.\s", line):
            if len(bullets) < max_bullets:
                bullets.append(p[:width])
            continue
        if line.startswith("#"):
            continue
        # `_… _` on its own line is the step template's caption for the section — keep it apart so the
        # card's lead line is the product's own text, not the shell's instruction
        if not caption and re.match(r"^_[^_]+_$", line):
            caption = p[:width]
            continue
        if not lead:
            lead = p[:width]
    return {"lead": lead or caption, "caption": caption, "bullets": bullets,
            "table_rows": table_rows, "table_head": table_head}


def is_file_produces(p):
    """A `produces` that names a file (brief -> product/briefs/<slug>.md, handoff -> HANDOFF.md),
    not an artifact section id."""
    return "/" in p or p.endswith(".md") or p.isupper() or p in ("HANDOFF.md",)


# ---------------------------------------------------------------- change logs

CHANGELOG_ENTRY_RE = re.compile(r"^###\s+(\d{4}-\d{2}-\d{2})\s*[—–-]\s*(.*)$", re.M)


def change_log(text):
    """Dated change-log entries of an instance file (newest first, per CONVENTIONS).

    Returns [{date, summary, body}] — body keeps the From→To / Why / Trigger bullets verbatim.
    """
    for sec in sections(text):
        title = (sec["title"] or "").lower()
        if "change log" in title or "журнал изменен" in title:
            entries = []
            marks = list(CHANGELOG_ENTRY_RE.finditer(sec["body"]))
            for i, m in enumerate(marks):
                end = marks[i + 1].start() if i + 1 < len(marks) else len(sec["body"])
                entries.append({
                    "date": m.group(1),
                    "summary": m.group(2).strip(),
                    "body": sec["body"][m.end():end].strip(),
                })
            return entries
    return []
