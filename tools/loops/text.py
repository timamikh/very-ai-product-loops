"""Markdown & frontmatter primitives — the canon's notation, parsed in one place.

Deliberately minimal (stdlib only, scalar / inline-list / block-list frontmatter values, no markdown AST): the canon is
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
    """Minimal `key: value` frontmatter parse (top-level; scalars, inline and block lists).

    Returns (dict, full_text) — callers usually want both.
    """
    text = read(path)
    return frontmatter_from(text), text


def frontmatter_from(text):
    """Top-level `key: value` pairs; a value is a scalar, an inline `[a, b]` list, or a block list
    (`key:` alone, then `  - item` lines). Every other YAML form is out of the canon's notation."""
    m = re.match(r"^---\n(.*?)\n---", text, re.S)
    fm = {}
    if not m:
        return fm
    key = None
    for line in m.group(1).splitlines():
        mm = re.match(r"^([A-Za-z_][A-Za-z0-9_]*):\s*(.*)$", line)
        if mm:
            key = mm.group(1)
            fm[key] = parse_scalar(mm.group(2))
            continue
        # a block-list item under the last key — the empty-string scalar becomes a list
        mi = re.match(r"^\s+-\s+(.*)$", line)
        if mi and key is not None:
            if fm[key] == "":
                fm[key] = []
            if isinstance(fm[key], list):
                fm[key].append(mi.group(1).strip().strip('"').strip("'"))
    return fm


def frontmatter_issues(text):
    """YAML forms in the frontmatter block that the canon's notation does not admit, as
    [{line, text, reason}] with `line` numbered in the FILE (the `---` fence is line 1).

    `frontmatter_from` never raises — a card with a flow map (`{a: b}`) or a list of maps
    (`- key: v`) parses to a string where a list or map was meant, and nothing downstream notices.
    The linter surfaces these (check Y2) so a mis-parse is a reported defect, not silent data loss.
    """
    from . import yamlite
    m = re.match(r"^---\n(.*?)\n---", text, re.S)
    if not m:
        return []
    return [dict(i, line=i["line"] + 1) for i in yamlite.unsupported(m.group(1))]


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
    # `…` is the template's slot marker — an unfilled cell, not a value (every reader agrees)
    return "" if s in ("—", "-", "…", "...", "– to clarify –", "— to clarify —", "- to clarify -") else s


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


COL_KEY_RE = re.compile(r"<!--\s*c(?:ol)?:\s*([\w-]+)\s*-->", re.I)


def column_key(cell):
    """The stable column key a header cell carries (`<!--c:key-->`), or None (CONVENTIONS → Column keys).

    The column-level twin of a section `{#anchor}`: a reader addresses the column by this key, never
    by the (translatable, reorderable) header prose. Lives in one place so the linter and the console
    can never disagree about what a header declares.
    """
    m = COL_KEY_RE.search(cell)
    return m.group(1) if m else None


def column_keys(headers):
    """Per-header column keys, aligned to `headers` — None where a header carries no key."""
    return [column_key(h) for h in headers]


def header_name(cell):
    """A header cell's display prose, with any `<!--c:key-->` mark removed.

    The header's identity for a human (and for a by-name match) is its text; the key is metadata that
    rides alongside it. Reading the two apart lets a by-name reader keep matching a keyed header, and
    the console show the header without the comment leaking into the page.
    """
    return COL_KEY_RE.sub("", cell).strip()


def column_key_values(text, key):
    """Values under the column keyed `<!--c:key-->`, across EVERY table that carries it, or None.

    The column-key twin of `table_column`: a reader addresses the column by its stable key instead of
    its (translatable, reorderable) header prose — the same "mark, don't guess" the section `{#anchor}`
    already gives a heading. None when no table carries that key, so the caller can fall back to a
    by-name match for a not-yet-keyed instance.
    """
    found, vals = False, []
    for t in tables(text):
        keys = column_keys(t["headers"])
        if key in keys:
            found = True
            idx = keys.index(key)
            vals.extend(r[idx] for r in t["rows"] if len(r) > idx)
    return vals if found else None


CONFIRMED_RE = re.compile(r"<!--\s*confirmed:\s*(\d{4}-\d{2}-\d{2})(?:\s+by:\s*([\w.@-]+))?\s*-->")


def confirmed(body):
    """The date a human confirmed this section's result (`<!-- confirmed: YYYY-MM-DD -->`), or None.

    The semantic-layer twin of the linter's structural checks (CONVENTIONS → Section confirmation): a
    section is a *thesis* the human signs off, and this marker records that they signed off THIS
    version. A re-projection that changes the section drops the marker, so a stale sign-off can never
    survive the conclusion it approved. Absence = pending (⚙️).
    """
    m = CONFIRMED_RE.search(body)
    return m.group(1) if m else None


def confirmed_by(body):
    """Who signed the confirmation (`<!-- confirmed: <date> by:<who> -->`), or None.

    Optional attribution: on a team "a human signed off" is meaningless without a name; single-operator
    products simply omit it. Read, never guessed — the `theses` skill fills it from the recorded
    operator identity (CONVENTIONS → Section confirmation).
    """
    m = CONFIRMED_RE.search(body)
    return m.group(2) if m else None


CONTESTED_RE = re.compile(r"<!--\s*contested:\s*(\d{4}-\d{2}-\d{2})\s*-->")


def contested(body):
    """The date a human sent this section's result BACK for rework (`<!-- contested: YYYY-MM-DD -->`).

    Distinct from pending (never reviewed): here the human *looked* and pushed back, so the board can
    show contested work apart from work nobody has signed yet. The reason lives in the change log.
    Mutually exclusive with `confirmed` — the linter's check R holds that (CONVENTIONS → Section
    confirmation).
    """
    m = CONTESTED_RE.search(body)
    return m.group(1) if m else None


RESTS_ON_RE = re.compile(r"<!--\s*rests-on:\s*(.*?)\s*-->")
_REST_TARGET_RE = re.compile(r"(\d+)#([a-z0-9][a-z0-9-]*)")


def rests_on(body):
    """Upstream sections this section's thesis rests on (`<!-- rests-on: 1#segments, 2#opportunity -->`).

    Returns normalized `"<step>#<section-id>"` refs (empty if no marker). A confirmed thesis whose
    foundation is not itself confirmed is a silent staleness the console surfaces (CONVENTIONS → Section
    confirmation); the linter checks each ref resolves to a real section.
    """
    m = RESTS_ON_RE.search(body)
    if not m:
        return []
    return ["%s#%s" % (s, sid) for s, sid in _REST_TARGET_RE.findall(m.group(1))]


OPEN_RE = re.compile(r"<!--\s*open\s*-->")


def is_open(body):
    """True when a section is declared structurally OPEN (`<!-- open -->`) — an agent→human inbox
    (to-clarify, open-questions, blockers), never a signed result (CONVENTIONS → Section confirmation).

    Kept out of a step's "N of M confirmed" count: an open section has no result to sign, so counting
    it would peg the figure below full forever. Such a section must never carry a `confirmed:` marker.
    """
    return bool(OPEN_RE.search(body))


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
        headers = [header_name(h).lower() for h in t["headers"]]
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
        headers = [header_name(h).lower() for h in t["headers"]]
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
HYP_RE = re.compile(r"\bH-\d+\b")
RISK_RE = re.compile(r"\bR-\d+\b")
METRIC_RE = re.compile(r"\bM-[a-z0-9][a-z0-9-]*\b")
# free width (CONVENTIONS → ids count sequentially, padding is style): a v0.12 instance has no
# positional `F-<n>` item ids left to collide with — pre-v0.12 instances rename items on migration
FEATURE_RE = re.compile(r"\bF-\d+\b")
SURFACE_RE = re.compile(r"\bS-\d+\b")
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
        "features": sorted(set(FEATURE_RE.findall(text))),
        "surfaces": sorted(set(SURFACE_RE.findall(text))),
    }


def to_clarify_lines(text):
    """The BLOCKS carrying a `— to clarify —` gap, for the open-questions view — each a wrapped bullet or
    paragraph joined into one line, never the physical line the marker happens to sit on (a file
    hard-wraps prose, so the marker's line is a soft-wrap accident; `block_at` is the one primitive)."""
    out, seen = [], set()
    for n, ln in enumerate(text.split("\n"), 1):
        if TO_CLARIFY_RE.search(ln):
            first, _, lines = block_at(text, n)
            if first in seen:
                continue
            seen.add(first)
            out.append(re.sub(r"\s+", " ", " ".join(x.strip() for x in lines)).strip())
    return out


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


CARD_RE = re.compile(r"<!--\s*card\s*-->")
_BULLET_RE = re.compile(r"^([-*+]|\d+\.)\s")
_HARD_BREAK_RE = re.compile(r"(?:\\|\s{2,})$")


def _join_card(raws):
    """Join the lines a `<!-- card -->` mark collected into one card lead. A line that ends in a
    markdown hard break — a trailing backslash `\\` or two-plus spaces — starts a NEW line in the card
    (returned as a `\\n`); an ordinary soft wrap joins with a space, so a sentence wrapped for file
    width is never shown broken. The break marker itself is dropped, and a leading blockquote `>` is
    stripped per line. This is how an enumeration laid one-item-per-line in the artifact reaches the
    card as separate lines instead of one run."""
    parts, seps = [], []
    for raw in raws:
        hard = bool(_HARD_BREAK_RE.search(raw))
        t = re.sub(r"^>\s?", "", raw.strip())
        t = re.sub(r"\s*\\$", "", t).rstrip()  # drop a trailing backslash break marker
        parts.append(t)
        seps.append("\n" if hard else " ")
    out = ""
    for k, t in enumerate(parts):
        out += t + (seps[k] if k < len(parts) - 1 else "")
    return out


def _card_clean(s):
    """Drop a leading block marker (blockquote `>`, bullet, number) from a card lead, keeping the
    inline markdown (`**bold**`, `code`, links) the interface renders."""
    return re.sub(r"^\s*(?:[>\-*+]\s+|\d+\.\s+)+", "", s).strip()


def card_line(body):
    """The paragraph a `<!-- card -->` mark designates as a section's showcase lead — returned
    verbatim, its markdown kept, so the interface shows the artifact's own words exactly.

    Two forms are read, and both name a **block**, never a physical line: the mark alone on a line
    points at the paragraph below it; the mark at the end of a line points at the whole paragraph or
    bullet that line sits in. Files hard-wrap prose at file width, so a physical line is a soft-wrap
    accident — a mark trailing the last line of a wrapped paragraph used to surface just that tail
    (mid-sentence) as the card face, which is the one thing this function must not do. Within the
    collected lead, a
    markdown hard break (a line ending in `\\` or two spaces) is kept as a `\\n`, so an enumeration the
    author laid one-item-per-line reaches the card as separate lines; ordinary soft wraps still join
    with a space. The agent places the mark at projection time (choosing the headline is projection
    judgement — CONVENTIONS → *Card line*); nothing is generated or summarised here, so a card can
    neither drift from the text nor invent past it. No mark → None, and the interface shows the
    section's title and status only — it never composes a gist of its own.
    """
    lines = body.splitlines()
    for i, raw in enumerate(lines):
        if not CARD_RE.search(raw):
            continue
        before = CARD_RE.sub("", raw).strip()
        if before:
            # Trailing form. Walk back over any continuation lines to the block's start, then collect
            # the whole block — paragraph and bullet alike, so a lead wrapped across physical lines is
            # never returned cut at a soft wrap.
            top = i
            while top > 0 and lines[top].strip() and not _BULLET_RE.match(lines[top].strip()):
                t = lines[top - 1].strip()
                if not t or t[:1] in ("|", "#") or _BULLET_RE.match(t):
                    break
                top -= 1
            if top > 0 and _BULLET_RE.match(lines[top - 1].strip()):
                top -= 1  # the bullet's own line sits one above the first continuation
            raws = []
            for nxt in lines[top:]:
                clean = CARD_RE.sub("", nxt)
                t = clean.strip()
                if raws and (not t or t[:1] in ("|", "#") or _BULLET_RE.match(t)):
                    break  # one block only — stop at the next blank/list/table/heading
                if t:
                    raws.append(clean)
            return _card_clean(_join_card(raws)) or None
        raws = []
        for nxt in lines[i + 1:]:
            t = nxt.strip()
            if not t:
                if raws:
                    break
                continue
            if t[:1] in ("|", "#") or _BULLET_RE.match(t):
                break  # a table/list/heading is not a card lead — leave the section to its fallback
            raws.append(nxt)
        return _card_clean(_join_card(raws)) or None
    return None


def digest(body, max_bullets=3, width=190):
    """The gist of a section, for a card in the step canvas.

    A canvas is only useful if its cards say something. The lead line and first bullets are what a
    human would read first anyway; a table's row count stands in for "how much is in here".
    """
    lead, caption, bullets, table_rows, table_head = "", "", [], 0, []
    in_table = False
    raw_lines = body.split("\n")
    n = 0
    while n < len(raw_lines):
        n += 1
        line = raw_lines[n - 1].strip()
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
        if line.startswith("#"):
            continue
        # prose is read by BLOCK, never by physical line (CONVENTIONS -> Card line; `block_at` is the
        # one primitive): a hard-wrapped bullet's continuation is part of the bullet, not a new lead
        _, last, blines = block_at(body, n)
        n = last
        p = re.sub(r"\s+", " ", " ".join(_plain(x.strip()) for x in blines)).strip()
        if not p or len(p) < 2:
            continue
        if re.match(r"^[-*+]\s", line) or re.match(r"^\d+\.\s", line):
            if len(bullets) < max_bullets:
                bullets.append(p[:width])
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


# ---------------------------------------------------------------- blocks

_BLOCK_EDGE_RE = re.compile(r"^\s*(?:#{1,6}\s|\||```|~~~)")


def _is_block_edge(line):
    """A line that can never be part of a prose block: blank, heading, table row, fence."""
    return not line.strip() or bool(_BLOCK_EDGE_RE.match(line))


def block_at(text, lineno):
    """(first_lineno, last_lineno, lines) of the prose BLOCK containing 1-based `lineno`.

    The canon's rule for every "line" it names — the card line, the decision line, the inputs line —
    is that a line names a **block**, never a physical line (CONVENTIONS → Card line): files hard-wrap
    prose, so a physical line is a soft-wrap accident. A block is the run of non-blank lines around
    `lineno`, cut at a blank line, a heading, a table row or a fence; a list item starts a new block
    (its wrapped continuation lines belong to it). This is the one primitive every such reader uses.
    """
    lines = text.split("\n")
    i = max(0, min(lineno - 1, len(lines) - 1))
    if _is_block_edge(lines[i]):
        return lineno, lineno, [lines[i]]
    start = i
    while start > 0 and not _is_block_edge(lines[start - 1]) and not _BULLET_RE.match(lines[start].strip()):
        start -= 1
    end = i
    while end + 1 < len(lines) and not _is_block_edge(lines[end + 1]) \
            and not _BULLET_RE.match(lines[end + 1].strip()):
        end += 1
    return start + 1, end + 1, lines[start:end + 1]


def marked_block(text, marker):
    """(first_lineno, block_text) of the first block carrying `marker` (a compiled regex or a string),
    the block's lines joined with single spaces — or (0, None) when nothing carries it."""
    rx = marker if hasattr(marker, "search") else re.compile(re.escape(marker))
    for n, line in enumerate(text.split("\n"), 1):
        if rx.search(line):
            first, _, lines = block_at(text, n)
            return first, re.sub(r"\s+", " ", " ".join(ln.strip() for ln in lines)).strip()
    return 0, None


def block_after(label, text):
    """The block a `**Label:**` line opens (label matched case-insensitively at the block's start),
    joined into one string — or None. `block_after("Inputs", body)` reads the whole inputs paragraph
    of a worklog even when it wraps; `block_after("North Star", body)` the North-Star statement."""
    rx = re.compile(r"^\s*(?:[-*+]\s+|\d+\.\s+|>\s*)?\*\*%s[^*]*\*\*" % re.escape(label), re.I)
    for n, line in enumerate(text.split("\n"), 1):
        if rx.match(line):
            _, _, lines = block_at(text, n)
            return re.sub(r"\s+", " ", " ".join(ln.strip() for ln in lines)).strip()
    return None


# ---------------------------------------------------------------- change logs

CHANGELOG_ENTRY_RE = re.compile(r"^###\s+(\d{4}-\d{2}-\d{2})\s*[—–-]\s*(.*)$", re.M)
_CHANGELOG_TITLE_RE = re.compile(r"change\s*log|журнал\s+изменен|changelog", re.I)


def is_change_log_title(title):
    """True for the change-log heading in any language the framework has met (CONVENTIONS → Change
    logs). One predicate, so a reader that cuts the history off (the linter's regions) and the
    reader that parses it (`change_log`) can never disagree about where the history starts."""
    return bool(_CHANGELOG_TITLE_RE.search(title or ""))


def without_change_log(text):
    """The file with its change-log section removed — what a check that reads *current state* looks at.

    The change log is the last `##` section by convention and talks *about* sections, so ids, anchors
    and decision lines inside it are history, not claims. A localized heading (`## Журнал изменений`)
    is cut the same way; a literal `split("\\n## Change log")` was not, and history leaked into the
    perimeter, decision-line and feature-reference checks on every non-English instance.
    """
    body = body_after_frontmatter(text)
    for m in HEADING_RE.finditer(body):
        if len(m.group(1)) == 2 and (is_change_log_title(m.group(2)) or m.group(3) == "change-log"):
            cut = len(text) - len(body) + m.start()
            return text[:cut]
    return text


def change_log(text):
    """Dated change-log entries of an instance file (newest first, per CONVENTIONS).

    Returns [{date, summary, body}] — body keeps the From→To / Why / Trigger bullets verbatim.
    """
    for sec in sections(text):
        if is_change_log_title(sec["title"]) or sec["id"] == "change-log":
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
