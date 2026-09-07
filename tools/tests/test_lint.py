#!/usr/bin/env python3
"""Regression tests for the linter — stdlib `unittest`, no dependencies.

The fixture instance under `tools/tests/fixture/` carries one known defect per check (its files say
which); each test asserts the check ids that fire on the fixture and that nothing else instance-scoped
does. Library-scoped findings (C1, C9, L, X on framework cards …) are the moving library's and are
filtered out — the fixture tests the INSTANCE checks. Every hub/daisy F-finding with a code fix has a
case here, named after it.

Run:  python3 tools/tests/test_lint.py
"""
import io
import os
import re
import shutil
import sys
import tempfile
import unittest
from contextlib import redirect_stdout

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, "tools"))

import lint  # noqa: E402
from loops import framework as F  # noqa: E402
from loops import instance as I  # noqa: E402
from loops import text as T  # noqa: E402
from loops import yamlite  # noqa: E402

FIXTURE = os.path.join(HERE, "fixture")


def run_lint(path, tag=None, example_roots=None):
    """Lint one instance; return (errors, warnings) as [(check_id, message)] scoped to that instance."""
    lint.reset()
    saved = list(lint.EXAMPLE_ROOTS)
    if example_roots is not None:
        lint.EXAMPLE_ROOTS[:] = example_roots
    try:
        with redirect_stdout(io.StringIO()):
            lint.main([path])
    finally:
        lint.EXAMPLE_ROOTS[:] = saved
    tag = tag or lint.rel(path)

    def scoped(msgs):
        out = []
        for m in msgs:
            if tag in m:
                out.append((m.split(" ", 1)[0], m))
        return out
    return scoped(lint.ERRORS), scoped(lint.WARNS)


def ids(found):
    return sorted({cid for cid, _ in found})


def grep(found, cid, needle):
    return [m for c, m in found if c == cid and needle in m]


class FixtureVerdict(unittest.TestCase):
    """The whole fixture: exactly these check ids fire, on a product (non-example) instance."""

    @classmethod
    def setUpClass(cls):
        cls.errors, cls.warns = run_lint(FIXTURE)

    def test_error_ids(self):
        self.assertEqual(ids(self.errors), ["D", "E", "G3", "P", "T3", "X", "X2", "Y2"])

    def test_warn_ids(self):
        self.assertEqual(ids(self.warns),
                         ["C2", "D", "D2", "E2", "E6", "G2", "G4", "G5", "G6", "G7", "H3", "J", "O2",
                          "P", "P2", "T"])

    # -- G6 / G7 · the comment beside a tick is the data (decksmith D-43, F-16d)
    def test_na_without_comment_warns(self):
        self.assertTrue(grep(self.warns, "G6", "`concept#cjm` = `n/a` with no comment"))

    def test_na_with_a_reason_beside_it_is_silent(self):
        self.assertFalse(grep(self.warns, "G6", "concept#value-defensibility"))

    def test_deferred_without_until_warns(self):
        self.assertTrue(grep(self.warns, "G7", "`concept#hypotheses` = `deferred` with no `until:`"))

    def test_deferred_naming_what_retires_it_is_silent(self):
        self.assertFalse(grep(self.warns, "G7", "concept#to-clarify"))

    def test_tick_comments_join_the_block_above_and_the_trailing_note(self):
        notes = lint._tick_comments(os.path.join(FIXTURE, "state.yaml"))
        self.assertIn("test runner", notes["concept#value-defensibility"])
        self.assertTrue(notes["concept#to-clarify"].startswith("until: D-001"))
        self.assertEqual(notes["concept#cjm"], "")

    # -- D2 · a tag nested in a tag's argument (decksmith F-15)
    def test_nested_tag_warns_not_errors(self):
        self.assertTrue(grep(self.warns, "D2", "`[sourced: the brief — [assumption] on the count]` nests"))
        self.assertFalse(grep(self.errors, "D2", "nests"))

    # -- C2 · the mark sits on the slot the fragment declares (decksmith F-16b)
    def test_card_mark_off_its_slot_warns(self):
        self.assertTrue(grep(self.warns, "C2", "1-concept.md#jtbd: the `<!-- card -->` mark sits on an unlabelled block"))
        self.assertTrue(grep(self.warns, "C2", "declares the slot on `**Job statement:**`"))

    def test_card_mark_on_its_slot_is_silent(self):
        self.assertFalse(grep(self.warns, "C2", "#segments"))

    def test_unlabelled_fragment_face_imposes_no_label(self):
        # concept-formation's face is `_<Product> is a …_` — a slot, but no label to hold the mark to
        self.assertFalse(grep(self.warns, "C2", "#idea"))

    # -- E6 · a cited decision id has a row in decisions.md (decksmith F-11)
    def test_decision_without_a_row_warns(self):
        self.assertTrue(grep(self.warns, "E6", "cites `D-002`, which has no row in decisions.md"))

    def test_decision_with_a_row_is_silent(self):
        self.assertFalse(grep(self.warns, "E6", "`D-001`"))

    # -- E · metrics.csv through the one reader (hub F-01, F-05)
    def test_csv_undefined_id_is_error(self):
        self.assertTrue(grep(self.errors, "E", "`M-zzz` has no definition row"))

    def test_csv_quoted_comma_is_not_a_defect(self):
        self.assertFalse([m for m in grep(self.errors, "E", "metrics.csv:2")])

    def test_csv_field_count_mismatch_is_error(self):
        self.assertTrue(grep(self.errors, "E", "metrics.csv:6 has 11 field(s)"))

    def test_csv_comment_line_is_error(self):
        self.assertTrue(grep(self.errors, "E", "metrics.csv:5 `id` is `# a ten-field comment`"))
        self.assertTrue(grep(self.errors, "E", "metrics.csv:4 has 1 field(s)"))

    def test_csv_verdict_matches_the_console(self):
        """The linter reports exactly the defects the read layer's health carries — one parser."""
        health = I.load(FIXTURE, ROOT)["health"]
        codes = sorted(h["code"] for h in health if h["code"].startswith("metric"))
        self.assertEqual(codes, ["metric-undefined", "metrics-fields", "metrics-fields", "metrics-id"])

    # -- D · register enums through the read layer; missing key = WARN on a product instance
    def test_enum_value_error(self):
        self.assertTrue(grep(self.errors, "D", "H-002: status = `maybe`"))

    def test_missing_key_column_warns_on_product_instance(self):
        self.assertTrue(grep(self.warns, "D", "risks.md has no column keyed `<!--c:category-->`"))
        self.assertFalse(grep(self.errors, "D", "no column keyed"))

    # -- P · worklogs (daisy F-05)
    def test_missing_worklog_for_a_worked_section(self):
        self.assertTrue(grep(self.errors, "P", "uses tool `concept-expansion` but 1-concept/concept-expansion.md is missing"))

    def test_unworked_shell_owes_no_worklog(self):
        self.assertFalse(grep(self.errors, "P", "segment-pains"))
        self.assertFalse(grep(self.errors, "P", "cjm-concept"))

    def test_non_worklog_file_in_step_folder(self):
        self.assertTrue(grep(self.errors, "P", "notes.md is not `node_type: worklog`"))
        self.assertFalse(grep(self.warns, "P", "notes.md"))          # not doubled as an orphan

    def test_revisit_in_wrong_folder_gets_its_own_message(self):
        self.assertTrue(grep(self.warns, "P", "cjm-strategy.md sits in the wrong step's folder"))

    def test_true_orphan_message(self):
        self.assertTrue(grep(self.warns, "P", "orphan.md is an orphan — no section of any artifact"))

    # -- P2 · the inputs BLOCK and the perimeter (daisy F-02, F-03; hub F-09)
    def test_wrapped_inputs_line_reads_as_one_block(self):
        self.assertFalse(grep(self.warns, "P2", "half-keyed"))
        self.assertFalse(grep(self.warns, "P2", "not a legal atom"))

    def test_anchor_outside_perimeter_warns(self):
        self.assertTrue(grep(self.warns, "P2", "cites `#jtbd` outside the inputs line"))

    def test_metric_id_short_form_is_read(self):
        self.assertTrue(grep(self.warns, "P2", "cites `M-7d`"))

    def test_id_quoted_from_declared_register_row_is_not_a_leak(self):
        self.assertFalse(grep(self.warns, "P2", "M-quoted-in-register"))

    def test_declared_register_ids_are_covered(self):
        self.assertFalse(grep(self.warns, "P2", "`R-001`"))
        self.assertFalse(grep(self.warns, "P2", "`H-001`"))

    def test_change_log_and_inline_code_are_exempt(self):
        self.assertFalse(grep(self.warns, "P2", "#zzz"))
        self.assertFalse(grep(self.warns, "P2", "S-404"))
        self.assertFalse(grep(self.warns, "P2", "`M-a`"))

    def test_legacy_aggregate(self):
        self.assertTrue(grep(self.warns, "P2", "4 worklog(s) predate"))

    # -- G2/G3/G4 · tick states (hub F-10)
    def test_unrecorded_open_tick_warns(self):
        self.assertTrue(grep(self.warns, "G2", "gate `concept#jtbd`"))

    def test_recorded_reopen_is_silent(self):
        self.assertFalse(grep(self.warns, "G2", "concept#segments"))

    def test_placeholder_only_section_is_not_written(self):
        """A translated caption over the template table is still a shell (tolmach false positives)."""
        self.assertFalse(grep(self.warns, "G2", "concept#problems"))

    def test_tick_vocabulary(self):
        self.assertTrue(grep(self.errors, "G3", "`concept#solution` = `skipped`"))

    def test_tick_id_must_be_a_gate_item(self):
        self.assertTrue(grep(self.warns, "G4", "`concept#nope`"))

    def test_gate_readings_in_model(self):
        m = I.load(FIXTURE, ROOT)
        readings = {g["tick_id"]: g["reading"] for s in m["steps"] for g in s["gate"] if s["step"] == 1}
        self.assertEqual(readings["concept#idea"], "recorded")
        self.assertEqual(readings["concept#jtbd"], "unrecorded")
        self.assertEqual(readings["concept#segments"], "re-sign")
        self.assertEqual(readings["concept#problems"], "blank")
        self.assertEqual(readings["concept#solution"], "invalid")

    # -- localized change-log heading (E1)
    def test_localized_change_log_heading_is_cut(self):
        self.assertFalse(grep(self.warns, "E2", "H-999"))
        self.assertFalse(grep(self.warns, "O4", "Decided"))
        self.assertFalse(grep(self.errors, "O4", ""))

    # -- O2 · drift on a product instance is WARN
    def test_o2_drift_is_warn_on_product_instance(self):
        self.assertTrue(grep(self.warns, "O2", "1-concept.md#jtbd"))
        self.assertFalse(grep(self.errors, "O2", ""))

    def test_unworked_shell_owes_no_keys(self):
        self.assertFalse(grep(self.warns, "O2", "#value-defensibility"))
        self.assertFalse(grep(self.warns, "O2", "#hypotheses"))

    # -- the rest, one each
    def test_j_split_table(self):
        self.assertTrue(grep(self.warns, "J", "hypotheses.md: table at line 9"))

    def test_e2_feature_without_register(self):
        self.assertTrue(grep(self.warns, "E2", "`F-001`"))

    def test_x_bad_file_atom(self):
        self.assertTrue(grep(self.errors, "X", "`file:product-loops/export.md`"))

    def test_y2_flow_map_in_frontmatter(self):
        self.assertTrue(grep(self.errors, "Y2", "orphan.md:8"))

    def test_t3_secret(self):
        self.assertTrue(grep(self.errors, "T3", "orphan.md:14"))

    def test_h3_handoff_names_no_register(self):
        self.assertTrue(grep(self.warns, "H3", "HANDOFF.md names no register"))

    def test_g5_language(self):
        self.assertTrue(grep(self.warns, "G5", "segmentation.md is 9"))

    def test_t2_satisfied_by_repo_gitignore(self):
        self.assertFalse(grep(self.warns, "T2", ""))


class ExampleSemantics(unittest.TestCase):
    """The same fixture under `examples/` semantics: shape drift and a missing key column are ERRORS."""

    def setUp(self):
        self.tmp = tempfile.mkdtemp(prefix="lint-example-")
        self.inst = os.path.join(self.tmp, "examples", "fixture-example")
        shutil.copytree(FIXTURE, self.inst)

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_o2_and_d_promote_to_error(self):
        errors, warns = run_lint(self.inst, tag="fixture-example",
                                 example_roots=[os.path.join(self.tmp, "examples")])
        self.assertTrue(grep(errors, "O2", "1-concept.md#jtbd"))
        self.assertTrue(grep(errors, "D", "risks.md has no column keyed `<!--c:category-->`"))
        self.assertFalse(grep(warns, "O2", ""))


class DecisionsHome(unittest.TestCase):
    """E6 when the instance has no decisions.md at all: one aggregate WARN naming the cited ids."""

    def setUp(self):
        self.tmp = tempfile.mkdtemp(prefix="lint-e6-")
        self.inst = os.path.join(self.tmp, "fixture")
        shutil.copytree(FIXTURE, self.inst)
        os.remove(os.path.join(self.inst, "decisions.md"))

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_cited_decisions_with_no_home_warn_once(self):
        _, warns = run_lint(self.inst, tag="fixture")
        hits = grep(warns, "E6", "has no decisions.md")
        self.assertEqual(len(hits), 1)
        self.assertIn("`D-001`, `D-002`", hits[0])

    def test_translated_instance_is_not_held_to_english_labels(self):
        cfg = os.path.join(self.inst, "config.yaml")
        text = open(cfg, encoding="utf-8").read()
        open(cfg, "w", encoding="utf-8").write(re.sub(r"(?m)^language:.*$", "language: ru", text))
        _, warns = run_lint(self.inst, tag="fixture")
        self.assertFalse(grep(warns, "C2", "drifted off its slot"))


class SourcesIgnored(unittest.TestCase):
    """T2: an instance outside any .gitignore with a sources/ rule WARNs; one with the rule does not."""

    def setUp(self):
        self.tmp = tempfile.mkdtemp(prefix="lint-t2-")
        self.inst = os.path.join(self.tmp, "fixture-t2")
        shutil.copytree(FIXTURE, self.inst)
        os.makedirs(os.path.join(self.tmp, ".git"))          # a git root with no .gitignore

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_missing_rule_warns(self):
        _, warns = run_lint(self.inst, tag="fixture-t2")
        self.assertTrue(grep(warns, "T2", "no `.gitignore` rule"))

    def test_instance_rule_satisfies(self):
        with open(os.path.join(self.inst, ".gitignore"), "w") as f:
            f.write("sources/snapshots/\n")
        _, warns = run_lint(self.inst, tag="fixture-t2")
        self.assertFalse(grep(warns, "T2", ""))


class NodeTypeVocabulary(unittest.TestCase):
    """X2 (hub F-03): a source passport with an off-matrix node_type ERRORs with the nearest legal
    value; the fixture itself, all in vocabulary, is silent."""

    def setUp(self):
        self.tmp = tempfile.mkdtemp(prefix="lint-x2-")
        self.inst = os.path.join(self.tmp, "fixture-x2")
        shutil.copytree(FIXTURE, self.inst)

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_fixture_fires_only_on_the_step_folder_note(self):
        # the fixture's one off-vocabulary file is the `node_type: note` P plants in 1-concept/
        errs, _ = run_lint(self.inst, tag="fixture-x2")
        hits = grep(errs, "X2", "")
        self.assertEqual(len(hits), 1)
        self.assertIn("1-concept/notes.md", hits[0])

    def test_unknown_type_errors_with_hint(self):
        with open(os.path.join(self.inst, "sources", "db-prod-readonly.md"), "w") as f:
            f.write("---\nnode_type: source-access\ntitle: prod db passport\n---\n# passport\n")
        errs, _ = run_lint(self.inst, tag="fixture-x2")
        hits = grep(errs, "X2", "source-access")
        self.assertTrue(hits)
        self.assertIn("did you mean `source`", hits[0])

    def test_vocabulary_comes_from_the_matrix(self):
        vocab = lint._node_type_vocabulary()
        for v in ("artifact", "worklog", "register", "source", "sources-index", "handoff", "card"):
            self.assertIn(v, vocab)
        self.assertNotIn("node_type", vocab)


class ReadLayerPrimitives(unittest.TestCase):
    """The primitives the checks lean on, in isolation."""

    def test_block_after_reads_a_wrapped_label_block(self):
        body = "# t\n\n**Inputs:** <!--w:reads--> a ·\nb · **Supplements:** <!--w:adds--> none\n\n## next"
        self.assertEqual(T.block_after("Inputs", body),
                         "**Inputs:** <!--w:reads--> a · b · **Supplements:** <!--w:adds--> none")

    def test_block_at_stops_at_list_items(self):
        self.assertEqual(T.block_at("- one\n  two\n- three\n", 2), (1, 2, ["- one", "  two"]))

    def test_without_change_log_any_language(self):
        for heading in ("## Change log", "## Журнал изменений", "## History {#change-log}"):
            text = "## A {#a}\nbody\n\n%s\n### 2026-01-01 — x\nH-2\n" % heading
            self.assertNotIn("H-2", T.without_change_log(text))
            self.assertIn("body", T.without_change_log(text))

    def test_yamlite_unsupported_names_the_forms(self):
        issues = yamlite.unsupported("a: 1\np:\n  x: {path: p}\nl:\n  - k: v\n  - plain\n")
        self.assertEqual([i["line"] for i in issues], [3, 5])
        self.assertIn("flow map", issues[0]["reason"])
        self.assertIn("list of maps", issues[1]["reason"])

    def test_worked_ignores_translated_placeholder(self):
        tpl = frozenset(["_Who it's for._", "| A | B |", "|---|---|", "| … | … |"])
        self.assertFalse(F.worked("_Для кого продукт._\n| A | B |\n|---|---|\n| … | … |\n", tpl))
        self.assertTrue(F.worked("_Для кого продукт._\n| A | B |\n|---|---|\n| real | row |\n", tpl))
        self.assertFalse(F.worked("<!-- tool: x -->\n", None))
        self.assertTrue(F.worked("One real sentence.", None))

    def test_register_reads_every_id_table(self):
        tmp = tempfile.mkdtemp(prefix="lint-reg-")
        try:
            os.makedirs(os.path.join(tmp, "registers"))
            with open(os.path.join(tmp, "config.yaml"), "w") as f:
                f.write('product: "x"\nlanguage: en\nactive_status: pmf\ndirections: [development]\n')
            with open(os.path.join(tmp, "registers", "metric-tree.md"), "w") as f:
                f.write("| id | kind |\n|----|------|\n| M-a | measured |\n\nprose\n\n"
                        "| id | kind |\n|----|------|\n| M-b | derived |\n")
            rows = I.load(tmp, ROOT)["registers"]["metric_tree"]["rows"]
            self.assertEqual([r["id"] for r in rows], ["M-a", "M-b"])
        finally:
            shutil.rmtree(tmp, ignore_errors=True)

    def test_gitignored_helper(self):
        got = I.gitignored([os.path.join(ROOT, "examples", "tolmach"),
                            os.path.join(ROOT, "examples", "decksmith")], ROOT)
        self.assertEqual({os.path.basename(p) for p in got}, {"tolmach"})


class LibraryChecks(unittest.TestCase):
    """C1/C3/C4/C4b/C6/W2 on a fixture library (tools/tests/fixture-library) — the real library is
    another agent's moving target, so these run on fake cards whose defects are named in their text."""

    @classmethod
    def setUpClass(cls):
        lib = os.path.join(HERE, "fixture-library")
        tools = {}
        for name in sorted(os.listdir(lib)):
            d = os.path.join(lib, name)
            skill = os.path.join(d, "SKILL.md")
            if os.path.isfile(skill):
                tools[name] = {"dir": d, "fm": T.frontmatter(skill)[0], "skill": skill}
        lint.reset()
        lint.check_library_bodies(tools, F.homed_sections(ROOT))
        cls.warns = [(w.split(" ", 1)[0], w) for w in lint.WARNS]
        cls.errors = list(lint.ERRORS)

    def test_only_warns(self):
        self.assertEqual(self.errors, [])
        self.assertEqual(ids(self.warns), ["C1", "C4", "C4b", "C6", "W2"])

    def test_c1_genuine_read_warns_handoffs_do_not(self):
        hits = grep(self.warns, "C1", "[fx-reader]")
        self.assertEqual(len(hits), 1)
        self.assertIn("`#problems`", hits[0])
        for exempt in ("competitor-pricing", "segments", "value-defensibility", "jtbd", "solution", "idea"):
            self.assertNotIn(exempt, hits[0])

    def test_c4_section_fragment_without_slot(self):
        self.assertTrue(grep(self.warns, "C4", "[fx-plan]"))

    def test_c4_item_block_fragment_is_exempt(self):
        self.assertFalse(grep(self.warns, "C4", "[fx-item]"))

    def test_c4b_two_faces_one_anchor(self):
        hits = grep(self.warns, "C4b", "{#cjm}")
        self.assertEqual(len(hits), 1)
        self.assertIn("journey read", hits[0])
        self.assertIn("strategy read", hits[0])

    def test_c6_numeric_floor_needs_min(self):
        self.assertTrue(grep(self.warns, "C6", "[fx-reader]"))

    def test_c6_structural_rule_is_exempt(self):
        self.assertFalse(grep(self.warns, "C6", "[fx-plan]"))

    def test_c3_decision_line_present_is_silent(self):
        self.assertFalse(grep(self.warns, "C3", ""))

    def test_w2_worklog_section_budget(self):
        self.assertTrue(grep(self.warns, "W2", "[fx-other]"))
        self.assertFalse(grep(self.warns, "W2", "[fx-reader]"))


class Help(unittest.TestCase):
    def test_help_lists_every_check(self):
        out = io.StringIO()
        with redirect_stdout(out):
            lint.main(["--help"])
        text = out.getvalue()
        for cid in ("C1", "C3", "C4", "C4b", "C6", "C9", "G3", "G4", "G5", "H3", "T2", "T3", "W2", "X2", "Y2", "--ci"):
            self.assertIn(cid, text)


class GraphTests(unittest.TestCase):
    """The dependency graph (tools/loops/graph.py) is a view over what the read layer read — every
    edge names two nodes that exist, and every edge kind is one the files can state."""

    def test_instance_graph_is_closed_over_its_nodes(self):
        from loops import graph as G
        m = I.load(FIXTURE, ROOT)
        g = m["graph"]
        ids = {n["id"] for n in g["nodes"]}
        for e in g["edges"]:
            self.assertIn(e["from"], ids, e)
            self.assertIn(e["to"], ids, e)
            self.assertIn(e["kind"], {"rests", "implied", "ref", "serves", "on", "parent", "test"})
        # a section's rests-on marker is an edge from the foundation to the section
        rests = [(e["from"], e["to"]) for e in g["edges"] if e["kind"] == "rests"]
        for art in m["artifacts"]:
            for sec in art["sections"]:
                for tgt in sec["rests_on"]:
                    self.assertIn(("s:" + tgt, "s:%d#%s" % (art["step"], sec["id"])), rests)
        # a register id a section names is an edge to that row — and only to a row that exists
        rows = {n["id"] for n in g["nodes"] if n["kind"] != "section"}
        for e in g["edges"]:
            if e["kind"] == "ref":
                self.assertIn(e["to"], rows)
        self.assertEqual(G.instance_graph([], {}), {"nodes": [], "edges": []})

    def _two_sections(self, rests_on=()):
        """A one-step instance with `segments` and `problems` written; `problems` may carry markers."""
        def sec(sid, rests):
            return {"id": sid, "title": sid, "words": 10, "confirmed": True, "contested": False,
                    "open": False, "gaps": [], "card": "", "markers": {}, "rests_on": list(rests)}
        return [{"step": 1, "file": "1-concept.md",
                 "sections": [sec("segments", []), sec("problems", rests_on)]}]

    def test_implied_edges_come_from_the_skeleton_and_never_double_a_rests_on(self):
        from loops import graph as G
        steps, skills = F.steps(ROOT), F.skills(ROOT)
        # the skeleton names `segment-pains` on `problems`; the card reads `segments` and `jtbd`
        g = G.instance_graph(self._two_sections(), {}, steps, skills)
        kinds = {(e["from"], e["to"]): e["kind"] for e in g["edges"]}
        self.assertEqual(kinds.get(("s:1#segments", "s:1#problems")), "implied")
        # `jtbd` is read too, but not written here — a prescription never makes a node
        self.assertNotIn("s:1#jtbd", {n["id"] for n in g["nodes"]})
        # the same pair stated by a `rests-on` marker is drawn once, as the stated kind
        g2 = G.instance_graph(self._two_sections(["1#segments"]), {}, steps, skills)
        pairs = [(e["from"], e["to"], e["kind"]) for e in g2["edges"]]
        self.assertEqual(pairs.count(("s:1#segments", "s:1#problems", "rests")), 1)
        self.assertNotIn(("s:1#segments", "s:1#problems", "implied"), pairs)
        # without the skeleton or the cards the graph holds stated edges only
        self.assertEqual(G.instance_graph(self._two_sections(), {})["edges"], [])

    def test_a_missing_rests_on_target_is_one_node(self):
        from loops import graph as G
        arts = self._two_sections(["2#market-sizing"])
        arts[0]["sections"][0]["rests_on"] = ["2#market-sizing"]      # two sections rest on the same absent one
        g = G.instance_graph(arts, {})
        missing = [n for n in g["nodes"] if n["status"] == "missing"]
        self.assertEqual([n["id"] for n in missing], ["s:2#market-sizing"])
        self.assertEqual(sum(1 for e in g["edges"] if e["from"] == "s:2#market-sizing"), 2)

    def test_register_ids_is_the_one_grammar(self):
        from loops import graph as G
        self.assertIs(G._ids, T.register_ids)
        self.assertEqual(T.register_ids("M-requests-30d, M-mau · S-03 · S-04 (H-2 twice H-2)"),
                         ["M-requests-30d", "M-mau", "S-03", "S-04", "H-2"])
        self.assertEqual(T.register_ids("H-1 M-x B-01", ("metrics",)), ["M-x"])
        self.assertEqual(T.register_ids(None), [])

    def test_framework_graph_reads_the_atoms(self):
        from loops import graph as G
        g = G.framework_graph(F.steps(ROOT), F.skills(ROOT))
        ids = {n["id"] for n in g["nodes"]}
        for e in g["edges"]:
            self.assertIn(e["from"], ids, e)
            self.assertIn(e["to"], ids, e)
            self.assertIn(e["kind"], {"reads", "writes", "worklog"})
        # every template section is a node, every card is a node, the six registers are nodes
        for st in F.steps(ROOT):
            for sec in st["skeleton"]:
                self.assertIn("s:%d#%s" % (st["step"], sec["id"]), ids)
        for c in F.skills(ROOT):
            self.assertIn("c:" + c["name"], ids)
        self.assertIn("g:hypotheses", ids)
        # a wildcard atom (`section:*`, `register:*`) names no node
        self.assertNotIn("g:*", ids)
        self.assertFalse([i for i in ids if i.endswith("#*")])
        # a declared foreign worklog input is a card-to-card edge
        wl = {(e["from"], e["to"]) for e in g["edges"] if e["kind"] == "worklog"}
        self.assertIn(("c:cjm-concept", "c:cjm-strategy"), wl)


if __name__ == "__main__":
    unittest.main(verbosity=1)
