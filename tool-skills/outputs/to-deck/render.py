#!/usr/bin/env python3
"""to-deck — GENERIC renderer: an approved HTML deck -> a PDF beside it, for sending by email.
Instance-agnostic: no product data lives here, only the HTML->PDF conversion — so it travels with
the framework. Rendering a PDF needs a browser engine (that's why this is code, not instructions);
this uses whatever Chromium-family browser is already installed (Chrome / Edge / Brave / Chromium)
via `--headless --print-to-pdf`. No pip install, no bundled browser.

The DECK must carry the standard `@media print` block (see to-deck/SKILL.md) so each slide prints
as one landscape page. This tool only drives the browser; the pagination lives in the HTML's CSS.

Usage:  render.py DECK.html [--out FILE]   # default out = DECK.pdf beside the html
"""
import argparse, os, shutil, subprocess, sys

# Chromium-family browsers, by platform, in preference order. First one found wins.
CANDIDATES = {
    "darwin": [
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
        "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser",
        "/Applications/Chromium.app/Contents/MacOS/Chromium",
    ],
    "linux": [
        "google-chrome", "google-chrome-stable", "chromium", "chromium-browser",
        "microsoft-edge", "brave-browser",
    ],
    "win32": [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    ],
}

def find_browser():
    for cand in CANDIDATES.get(sys.platform, CANDIDATES["linux"]):
        if os.path.sep in cand or (sys.platform == "win32" and ":" in cand):
            if os.path.exists(cand):
                return cand
        else:
            hit = shutil.which(cand)
            if hit:
                return hit
    return None

def render(html, out, browser=None):
    browser = browser or find_browser()
    if not browser:
        sys.exit("No Chromium-family browser found (Chrome/Edge/Brave/Chromium). Install one, or "
                 "pass --browser PATH. This adapter uses the system browser to print HTML -> PDF.")
    html_url = "file://" + os.path.abspath(html)
    os.makedirs(os.path.dirname(os.path.abspath(out)) or ".", exist_ok=True)   # fresh instance: no deliverables/ yet
    cmd = [browser, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
           "--print-to-pdf=" + os.path.abspath(out), html_url]
    r = subprocess.run(cmd, capture_output=True, text=True)
    # Some builds only accept the legacy --headless; retry once.
    if r.returncode != 0 or not os.path.exists(out):
        cmd[1] = "--headless"
        r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0 or not os.path.exists(out):
        sys.exit("PDF render failed (%s):\n%s" % (browser, (r.stderr or r.stdout).strip()))
    print("saved", out, "· via", os.path.basename(browser))

def main(argv=None):
    ap = argparse.ArgumentParser(description="to-deck generic renderer (HTML deck -> PDF)")
    ap.add_argument("deck", help="the approved HTML deck")
    ap.add_argument("--out", help="PDF output path (default: DECK.pdf beside the html)")
    ap.add_argument("--browser", help="path to a Chromium-family browser (else auto-detected)")
    a = ap.parse_args(argv)
    out = a.out or os.path.splitext(a.deck)[0] + ".pdf"
    render(a.deck, out, a.browser)

if __name__ == "__main__":
    sys.exit(main())
