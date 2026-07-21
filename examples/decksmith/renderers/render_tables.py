#!/usr/bin/env python3
"""to-table · registers + plan sections -> ONE .xlsx workbook (a tab per dataset) for decksmith.

Per the to-table one-table rule: several heterogeneous datasets asked for together become a single
workbook with tabs, not scattered CSVs. Columns are planned per sheet (schema below), IDs first,
confidence kept. Output is a projection of the instance; the artifacts/registers stay the source of
truth. Re-run:  python3 render_tables.py   (requires openpyxl)
"""
import os
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

BASE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.normpath(os.path.join(BASE, "..", "deliverables"))
STAMP = "2026-07-21"

ACCENT = "1D46D6"; ZEBRA = "F3F5F9"; INK = "14171D"; MUTED = "5B6470"
HEAD_FONT = Font(name="Calibri", bold=True, color="FFFFFF", size=10)
CAP_FONT  = Font(name="Calibri", italic=True, color=MUTED, size=8.5)
CELL_FONT = Font(name="Calibri", color=INK, size=10)
ID_FONT   = Font(name="Calibri", bold=True, color=ACCENT, size=10)
HEAD_FILL = PatternFill("solid", fgColor=ACCENT)
ZEBRA_FILL= PatternFill("solid", fgColor=ZEBRA)
TOP = Alignment(vertical="top", wrap_text=True)
THIN = Side(style="thin", color="E4E1DA")
BORDER = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)

def add_sheet(wb, title, caption, header, rows, widths):
    ws = wb.create_sheet(title[:31])
    ncol = len(header)
    # row 1: provenance caption (merged, does not affect column parsing in xlsx)
    ws.merge_cells(start_row=1, start_column=1, end_row=1, end_column=ncol)
    c = ws.cell(row=1, column=1, value=caption); c.font = CAP_FONT
    c.alignment = Alignment(vertical="center")
    ws.row_dimensions[1].height = 16
    # row 2: header
    for j, h in enumerate(header, start=1):
        cell = ws.cell(row=2, column=j, value=h)
        cell.font = HEAD_FONT; cell.fill = HEAD_FILL
        cell.alignment = Alignment(vertical="center", wrap_text=True)
        cell.border = BORDER
    ws.row_dimensions[2].height = 20
    # data
    for i, row in enumerate(rows):
        r = i + 3
        for j, val in enumerate(row, start=1):
            cell = ws.cell(row=r, column=j, value=val)
            cell.font = ID_FONT if j == 1 else CELL_FONT
            cell.alignment = TOP; cell.border = BORDER
            if i % 2 == 1:
                cell.fill = ZEBRA_FILL
    for j, w in enumerate(widths, start=1):
        ws.column_dimensions[get_column_letter(j)].width = w
    ws.freeze_panes = "A3"
    return ws

wb = Workbook(); wb.remove(wb.active)

# ---- Hypotheses (schema: id | hypothesis | type | status | born | test | confidence) ----
add_sheet(wb, "Hypotheses",
    "Hypotheses — source: registers/hypotheses.md · rendered %s (to-table)" % STAMP,
    ["ID", "Hypothesis", "Type", "Status", "Born", "Test", "Confidence"],
    [
        ["H-001", "Engine reliably produces native files both genuinely editable AND well-designed, at scale", "feasibility", "testing", "Step 1", "Step4 M-edit-fidelity >=90% (fail <70%); Step5 20 test decks + rule; Step6 F-1+T-1 first read", "assumption"],
        ["H-002", "Salespeople & marketers are a reachable segment who feel 'AI decks look templated' (P1) enough to switch", "desirability", "open", "Step 1", "discovery interviews + demand test (Step 5)", "assumption"],
        ["H-003", "'Wrong structure/framing' (P2) is a top pain worth solving, not just styling slides", "desirability", "open", "Step 1", "discovery interviews (Step 5)", "assumption"],
        ["H-004", "The editable-and-beautiful quality is defensible (survives an LLM rebuild); pressured at Step 2 by Copilot/Canva", "viability/moat", "open", "Step 1", "observe replication attempts / sustained quality gap (Step 3+)", "assumption"],
        ["H-005", "A native high-fidelity editable+designed deck is a real unmet need valued over web-format generation", "desirability/viability", "testing", "Step 2", "Step4 M-activation >=30% (fail <10%); Step5 demand probe B-01/B-03 >=10 trials; Step6 A-1 seeds B-01", "assumption"],
        ["H-006", "The obtainable market is large enough to build a business on (bottom-up SAM ~$750M)", "viability", "open", "Step 2", "validate reachable-count + price + adoption (Step 4)", "assumption"],
        ["H-007", "For the beachhead job, actually-editable + designed native decks is a strong enough wedge to switch", "desirability", "open", "Step 3", "Step4 M-wk-retention flattens >0; demand test (Step 5)", "assumption"],
        ["H-008", "A standalone native-fidelity+design engine can stay ahead of incumbents long enough to build lock-in", "viability/moat", "open", "Step 3", "sustained quality gap + retention once customers exist (pmf)", "assumption"],
        ["H-009", "The beachhead will pay a standalone subscription (~$15-25) despite incumbents bundling", "viability", "open", "Step 3", "Step4 WTP >=$15/mo (fail <$10); price-talk pilot (Step 5)", "assumption"],
        ["H-010", "Sales/marketing communities + product-led virality acquire the beachhead at viable CAC", "viability", "open", "Step 3", "channel tests with pre-set CAC threshold (Step 5)", "assumption"],
    ],
    [8, 52, 15, 10, 8, 46, 12])

# ---- Risks (schema: id | risk | category | likelihood | impact | mitigation | owner/due | status | source) ----
add_sheet(wb, "Risks",
    "Risks — source: registers/risks.md · rendered %s (to-table)" % STAMP,
    ["ID", "Risk", "Category", "Likelihood", "Impact", "Mitigation", "Owner / Due", "Status", "Source"],
    [
        ["R-001", "Gamma is a dominant, profitable leader ($100M ARR, 70M users) — head-on displacement is hard", "market", "H", "H", "Don't fight head-on — compete on the native-fidelity gap; monitor", "founder", "accepted (monitored)", "Step 2"],
        ["R-002", "Incumbents (Copilot in PPT, Canva AI) bundle native-editable AI generation with distribution", "market", "H", "H", "Move fast on the fidelity gap; position sharply on 'actually editable'; track releases", "founder / ongoing", "mitigating", "Step 2"],
        ["R-003", "Capable buyers self-build with general LLMs (ChatGPT/Claude) — caps willingness to pay", "market", "M", "M", "— (monitored)", "founder", "accepted (monitored)", "Step 2"],
        ["R-004", "Engine quality and COGS depend on third-party LLM providers (cost/availability outside our control)", "dependency", "M", "H", "Abstract the provider (multi-model); cap M-cogs-per-deck; keep the engine in-house", "eng / ongoing", "mitigating", "Step 2"],
        ["R-005", "Low entry barrier for 'AI slide wrappers' — crowded, fast-moving rivalry", "market", "H", "M", "— (monitored; the moat is the fidelity engine, not the app)", "founder", "accepted (monitored)", "Step 2"],
        ["R-006", "Manual build / hiring a designer keeps the high-stakes, brand-critical flagship decks", "market", "M", "M", "— (monitored)", "founder", "accepted (monitored)", "Step 2"],
        ["R-007", "The engine never reliably hits native-fidelity + design at scale — whole strategy rests on H-001", "product/execution", "M", "H", "Build a thin vertical slice first; gate on M-edit-fidelity >=90% before investing further", "founder/eng / next sprint", "mitigating", "Step 3"],
        ["R-008", "The beachhead won't pay standalone vs bundled incumbents ($15-30 bundled) — no viable revenue", "financial", "M", "H", "Test WTP early (Step 5 pilot) before building billing; don't scale spend until validated", "founder / Step 5", "open", "Step 3"],
        ["R-009", "Community + product-led virality doesn't materialize — CAC too high to grow", "market/execution", "M", "M", "Test inner-ring channels cheaply with a pre-set CAC threshold (H-010)", "founder / Step 5", "open", "Step 3"],
    ],
    [8, 50, 15, 11, 8, 46, 18, 20, 8])

# ---- Metric tree (schema: id | definition | unit | kind | parent | instrumentation | target | source) ----
add_sheet(wb, "Metric tree",
    "Metric tree (definitions) — source: registers/metric-tree.md · rendered %s (to-table) · concept stage: all not-instrumented, no readings" % STAMP,
    ["ID", "Definition", "Unit", "Kind", "Parent", "Instrumentation", "Target", "Source"],
    [
        ["M-ns-kept-decks-wk", "North Star (candidate). Decks generated -> exported -> kept and edited per active deck-maker per week. A redo = value failed, so it encodes 'editable AND designed'.", "count", "measured", "— (top)", "not-instrumented", "grow", "product events (future)"],
        ["M-edit-fidelity", "THE concept-proving metric. Share of exported slide objects that are natively editable (real shapes/text, not flattened images) — the anti-Gamma metric.", "%", "measured", "M-ns-kept-decks-wk", "not-instrumented", ">= 90%", "export pipeline (future)"],
        ["M-activation", "Share of new signups who generate AND export a first editable deck <= 7d.", "%", "measured", "M-ns-kept-decks-wk", "not-instrumented", "to clarify", "product events (future)"],
        ["M-wk-retention", "Share of activated users who return and export another deck the next week.", "%", "measured", "M-ns-kept-decks-wk", "not-instrumented", "to clarify (no cohorts)", "product events (future)"],
        ["M-free-paid-conv", "Free -> paid conversion <= 30d (full funnel).", "%", "measured", "M-ns-kept-decks-wk", "not-instrumented", "to clarify", "billing (future)"],
        ["M-cogs-per-deck", "LLM inference + render cost per generated deck (COGS).", "$", "measured", "— (guardrail)", "not-instrumented", "down", "LLM/API billing (future)"],
        ["M-gross-margin", "(Revenue - COGS) / Revenue.", "%", "derived", "— (guardrail)", "not-instrumented", ">= 70%", "derived (future)"],
    ],
    [20, 54, 7, 10, 20, 16, 12, 22])

# ---- Strategic plan: global hypotheses (schema: id | bet | metric_node | success | failure | confidence) ----
add_sheet(wb, "Strategic plan",
    "Strategic plan — global hypotheses (quantified bets) — source: strategic-plan.md#global-hypotheses · rendered %s (to-table)" % STAMP,
    ["ID", "Bet", "Metric node", "Success threshold", "Failure threshold", "Confidence"],
    [
        ["H-001", "The engine reliably produces editable+designed native files", "M-edit-fidelity", ">= 90% objects natively editable", "< 70%", "assumption"],
        ["H-005", "The editable+designed wedge is valued (users keep/edit, don't redo)", "M-activation / M-ns-kept-decks-wk", ">= 30% activate (generate+export+keep)", "< 10%", "assumption"],
        ["H-007", "The beachhead switches for the wedge", "M-wk-retention", "retention curve flattens > 0", "decays to 0", "assumption"],
        ["H-009", "Beachhead pays a standalone subscription", "WTP -> M-free-paid-conv", "WTP >= $15/mo in pilot", "< $10/mo", "assumption"],
    ],
    [8, 48, 26, 30, 20, 12])

# ---- Sprint plan: must + backlog (schema: tier | rank | direction | item | format | links | est | confidence) ----
add_sheet(wb, "Sprint plan",
    "Sprint 1 plan (must + backlog) — source: sprint-plan.md#must / #backlog · rendered %s (to-table)" % STAMP,
    ["Tier", "Rank", "Direction", "Item", "Format", "Links", "Est.", "Confidence"],
    [
        ["must", "", "development", "F-1 Native .pptx export slice (generate -> export one deck)", "Feature", "H-001 / M-edit-fidelity", "", "assumption"],
        ["must", "", "go-to-market", "A-1 Seed the demand probe in one sales-enablement community (B-01)", "Activity", "H-005 / M-activation", "", "assumption"],
        ["must", "", "back-office", "T-1 Edit-fidelity measurement harness + export event capture", "Task+DoD", "M-edit-fidelity / M-activation / R-007", "", "assumption"],
        ["backlog", "1", "back-office", "T-2 Assemble the 20 representative test decks", "Task+DoD", "M-edit-fidelity / R-007", "S", "assumption"],
        ["backlog", "2", "back-office", "T-3 Abstract the LLM provider behind one interface", "Task+DoD", "M-cogs-per-deck / R-004", "M", "assumption"],
        ["backlog", "3", "go-to-market", "A-2 Intent SEO page 'fix Gamma PPT export' (B-03)", "Activity", "H-005 / M-activation", "M", "assumption"],
        ["backlog", "4", "development", "F-2 Brand-kit intake (B-02)", "Feature", "H-007 / M-activation", "M", "assumption"],
        ["backlog", "5", "development", "F-3 Chart-fidelity hardening", "Feature", "H-001 / M-edit-fidelity", "M", "assumption"],
    ],
    [9, 6, 14, 46, 11, 30, 6, 12])

out = os.path.join(OUT_DIR, "decksmith-registers-and-plan.xlsx")
wb.save(out)
print("saved", out, "· sheets:", wb.sheetnames)
