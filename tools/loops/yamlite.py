"""The YAML subset the framework actually uses — parsed with the stdlib only.

`config.yaml` (human-authored decisions) and `state.yaml` (agent-written cycle position) are the two
instance YAML files. Both stay deliberately simple, so a ~120-line reader beats adding PyYAML as a
dependency: the framework's promise is "clone it and it runs on plain python3".

Supported: nested mappings by indentation · `- item` sequences · inline `[a, b]` lists · `{}` empty
map · block scalars (`>` and `|`) · quoted strings · `#` comments. Anything richer (anchors, multi-doc,
flow maps with pairs, tags) is out of scope by design — if the canon ever needs it, that is a change
to the canon first. `unsupported()` reports lines this reader had to skip — with the reason — so a
caller can surface them instead of silently losing data (the linter's check Y2 does).
"""
import re

TRUE = {"true", "yes", "on"}
FALSE = {"false", "no", "off"}


def _strip_comment(line):
    """Drop a trailing `# comment`, respecting quotes."""
    out, quote = [], None
    i = 0
    while i < len(line):
        ch = line[i]
        if quote:
            out.append(ch)
            if ch == quote:
                quote = None
        elif ch in "\"'":
            quote = ch
            out.append(ch)
        elif ch == "#" and (i == 0 or line[i - 1] in " \t"):
            break
        else:
            out.append(ch)
        i += 1
    return "".join(out).rstrip()


def _scalar(v):
    v = v.strip()
    if not v:
        return None
    if v == "{}":
        return {}
    if v == "[]":
        return []
    if v.startswith("[") and v.endswith("]"):
        inner = v[1:-1].strip()
        if not inner:
            return []
        return [_scalar(x) for x in inner.split(",")]
    if len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
        return v[1:-1]
    low = v.lower()
    if low in TRUE:
        return True
    if low in FALSE:
        return False
    if low in ("null", "~", "-"):
        return None
    if re.match(r"^-?\d+$", v):
        return int(v)
    if re.match(r"^-?\d*\.\d+$", v):
        return float(v)
    return v


# the two YAML forms real files reach for that this reader does NOT model — each parses to a plain
# string where a map or a list of maps was meant, so a caller that only looked at the data would
# never know. `unsupported()` names them; the linter (check Y2) turns them into a reported defect.
_FLOW_MAP_RE = re.compile(r"^\{.*:.*\}$")
_MAP_ITEM_RE = re.compile(r"^[A-Za-z_][\w.-]*:(\s|$)")

REASON_FLOW_MAP = "a flow map `{k: v}` — write it as indented `key: value` lines"
REASON_LIST_OF_MAPS = "a list of maps `- key: value` — write one `key:` block per item, or a plain list"
REASON_STRAY_ITEM = "a `- item` under a key that already holds a scalar or a map"
REASON_NOT_A_PAIR = "not a `key: value` pair"


def _unsupported_reason(s):
    """Why a content line is outside the subset, or None when it is fine."""
    if s.startswith("- "):
        v = s[2:].strip()
        if _FLOW_MAP_RE.match(v):
            return REASON_FLOW_MAP
        if _MAP_ITEM_RE.match(v) and not (len(v) >= 2 and v[0] in "\"'" and v[-1] == v[0]):
            return REASON_LIST_OF_MAPS
        return None
    m = re.match(r"^([^:]+):\s*(.*)$", s)
    if m and _FLOW_MAP_RE.match(m.group(2).strip()):
        return REASON_FLOW_MAP
    return None


def unsupported(text):
    """Lines this reader cannot model, as [{line, text, reason}] (1-based lines).

    Never raises: the reader stays tolerant (an instance must render with its drift showing), but a
    caller that wants a verdict — the linter — gets every offending line with the reason, instead of
    a string where a map was meant. Flow maps `{a: b}` (config-schema once asked for one under
    `products:`) and lists of maps `- key: v` are the two forms seen in the wild; stray items and
    non-pair lines round it out.
    """
    out = []
    _, skipped = parse(text)
    for ln, raw in skipped:
        s = _strip_comment(raw).strip()
        out.append({"line": ln, "text": raw.strip(), "reason": _unsupported_reason(s) or
                    (REASON_STRAY_ITEM if s.startswith("- ") else REASON_NOT_A_PAIR)})
    return out


def parse(text):
    """Parse the supported subset. Returns (data, skipped_lines).

    `skipped_lines` is [(lineno, raw)] for every line the reader could not model — including the two
    forms it deliberately does not (flow maps, lists of maps), which used to parse to a bare string
    in silence. `unsupported()` gives the same lines with a reason each.
    """
    lines = text.splitlines()
    root = {}
    # stack of (indent, container); a container is a dict or a list
    stack = [(-1, root)]
    skipped = []
    i = 0
    while i < len(lines):
        raw = lines[i]
        line = _strip_comment(raw)
        if not line.strip():
            i += 1
            continue
        indent = len(line) - len(line.lstrip(" "))
        s = line.strip()

        while len(stack) > 1 and indent <= stack[-1][0]:
            stack.pop()
        container = stack[-1][1]

        # sequence item
        if s.startswith("- "):
            if _unsupported_reason(s):
                skipped.append((i + 1, raw))
                if isinstance(container, list):
                    container.append(_scalar(s[2:]))   # keep the string so nothing downstream indexes past it
                i += 1
                continue
            item = _scalar(s[2:])
            if isinstance(container, list):
                container.append(item)
            else:
                skipped.append((i + 1, raw))
            i += 1
            continue

        m = re.match(r"^([^:]+):\s*(.*)$", s)
        if not m:
            skipped.append((i + 1, raw))
            i += 1
            continue
        key, rest = m.group(1).strip().strip("\"'"), m.group(2).strip()

        if not isinstance(container, dict):
            skipped.append((i + 1, raw))
            i += 1
            continue

        # block scalar
        if rest in (">", "|", ">-", "|-", ">+", "|+"):
            fold = rest[0] == ">"
            block, j = [], i + 1
            while j < len(lines):
                nxt = lines[j]
                if not nxt.strip():
                    block.append("")
                    j += 1
                    continue
                nind = len(nxt) - len(nxt.lstrip(" "))
                if nind <= indent:
                    break
                block.append(nxt.strip())
                j += 1
            joined = " ".join(x for x in block if x) if fold else "\n".join(block)
            container[key] = joined.strip()
            i = j
            continue

        if rest == "":
            # a nested mapping or sequence follows — decide by the next content line
            nxt_indent, nxt_s = None, None
            j = i + 1
            while j < len(lines):
                cand = _strip_comment(lines[j])
                if cand.strip():
                    nxt_indent = len(cand) - len(cand.lstrip(" "))
                    nxt_s = cand.strip()
                    break
                j += 1
            if nxt_s is not None and nxt_indent > indent and nxt_s.startswith("- "):
                child = []
            elif nxt_s is not None and nxt_indent > indent:
                child = {}
            else:
                container[key] = None
                i += 1
                continue
            container[key] = child
            stack.append((indent, child))
            i += 1
            continue

        if _FLOW_MAP_RE.match(rest):
            skipped.append((i + 1, raw))               # a flow map: kept as its string, reported
        container[key] = _scalar(rest)
        i += 1
    return root, skipped


def load(path):
    """Parse a YAML file. Returns (data, skipped_lines) — never raises on unsupported syntax."""
    with open(path, encoding="utf-8") as f:
        return parse(f.read())
