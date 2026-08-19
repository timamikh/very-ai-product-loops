"""The card schema, as code — the one place the vocabulary of `process/reference/card-schema.md` lives.

A card is every instruction an agent acts on: a step README, a library method, an operations skill,
an outputs skill, an instance's exchange skill. One frontmatter schema, five kinds. Its three
perimeter fields (`reads` · `writes` · `surfaces`) share one **atom grammar**, so a reader parses
them with one function instead of three heuristics.

This module is data plus two small parsers. It is imported by the linter (checks X and Z) and by the
read layer the console uses; a second copy of these tuples would drift and reintroduce exactly the
class of bug the schema exists to remove.
"""
import re

KINDS = ("step", "method", "operation", "output", "exchange")

# every card, every kind — check X errors when one is missing
CORE = ("node_type", "kind", "name", "prerequisites", "reads", "writes", "surfaces",
        "status", "version", "updated")

# fields a kind adds; anything outside CORE + BY_KIND[kind] + ALWAYS_OK warns as an unknown field,
# so a private key cannot quietly become de-facto schema
BY_KIND = {
    "step":      ("step", "output", "cadence", "method_basis", "title"),
    "method":    ("steps", "opinionated", "method_basis",
                  "evidence_standard", "volume_rule", "selection_rule", "rejects_shown"),
    "operation": ("opinionated", "method_basis"),
    "output":    ("output_kind", "opinionated", "method_basis", "formats",
                  "evidence_standard", "volume_rule", "selection_rule", "rejects_shown"),
    "exchange":  ("direction", "cadence", "reaches", "lands_via"),
}

# the law of ranks, as fields: a method is bound to a step and is never a routing target, so it
# carries `steps` and must not carry `surfaces`; a routed kind is the reverse
REQUIRED_BY_KIND = {
    "step":      ("step", "output"),
    "method":    ("steps",),
    "operation": (),
    "output":    ("output_kind",),
    "exchange":  ("direction", "reaches"),
}
FORBIDDEN_BY_KIND = {
    "step":      ("steps",),
    "method":    ("surfaces",),
    "operation": ("steps",),
    "output":    ("steps",),
    "exchange":  ("steps",),
}

# `surfaces` is what move 5 owes, so it is required of exactly the cards a pass can start at: every
# step card, plus whatever the goal map actually routes to (resolved from goal-map.md, not listed
# here — a second list would be the drift this schema exists to prevent). An operations card that is
# a *move* rather than a pass — `projection`, `orchestration`, invoked from inside moves 2-5 and
# never routed to — honestly declares `surfaces: []`.
NEEDS_SURFACES = ("step",)

REGISTERS = ("hypotheses", "risks", "metrics", "metric-tree")
SOURCE_SLOTS = ("kb", "interview", "research", "metrics", "git")
OUTPUT_KINDS = ("rendered", "authored")
DIRECTIONS = ("pull", "push")

# atom prefix -> the controlled vocabulary its argument must come from (None = free path/slug)
PREFIXED = {
    "register": REGISTERS,
    "source": SOURCE_SLOTS,
    "section": None,     # an artifact `{#anchor}` — checked against real templates by checks B/X
    "worklog": None,     # `worklog` bare = its own; `worklog:*` = one the pass resolves
    "file": None,
    "state": None,
}
BARE = ("worklog", "ticks", "sign-off", "change-log")

# which atoms each perimeter field admits
ALLOWED = {
    "reads":    ("register", "source", "section", "worklog", "file"),
    "writes":   ("register", "section", "worklog", "file", "state", "sign-off"),
    "surfaces": ("register", "section", "worklog", "file", "state",
                 "ticks", "sign-off", "change-log"),
}

ANCHOR_RE = re.compile(r"^[a-z0-9][a-z0-9-]*$")


def split_atom(atom):
    """`register:metrics` -> ("register", "metrics"); a bare atom -> (atom, "")."""
    atom = str(atom).strip()
    if ":" in atom:
        head, _, arg = atom.partition(":")
        return head.strip(), arg.strip()
    return atom, ""


def atom_errors(field, values):
    """Validate one perimeter field's atoms. Returns a list of human-readable defects.

    The whole point of the wave: a check that only asks "is the field present?" leaves 62 cards free
    to describe their inputs 62 ways, and the single structure is nominal.
    """
    out = []
    allowed = ALLOWED.get(field, ())
    for atom in values:
        head, arg = split_atom(atom)
        if head not in allowed:
            out.append("`%s` is not a legal atom for `%s` (allowed: %s)"
                       % (atom, field, " · ".join(allowed)))
            continue
        if head in BARE and not arg:
            continue
        if head not in PREFIXED:
            out.append("`%s` takes no argument" % atom)
            continue
        if not arg:
            out.append("`%s` needs an argument (`%s:<value>`)" % (atom, head))
            continue
        vocab = PREFIXED[head]
        if vocab is not None and arg not in vocab and arg != "*":
            out.append("`%s` is not in the %s vocabulary (%s)" % (atom, head, " · ".join(vocab)))
        if head == "section" and arg != "*" and not ANCHOR_RE.match(arg):
            out.append("`%s` is not a kebab-case section anchor" % atom)
    return out


def sections_written(writes):
    """The artifact anchors a card commits to — `*` excluded, it is a slot, not a commitment."""
    return [arg for head, arg in (split_atom(a) for a in writes)
            if head == "section" and arg and arg != "*"]


def known_fields(kind):
    return set(CORE) | set(BY_KIND.get(kind, ()))
