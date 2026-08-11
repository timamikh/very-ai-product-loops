#!/usr/bin/env python3
"""very-ai-product-loops — the local console for one product instance.

Run it in a product folder; it opens a browser view of the instance: where the cycle stands, what each
gate still has open, a canvas of every step's sections, the three registers, the metric series, every
`— to clarify —`, the change-log timeline, the skills the agent can reach, and the linter's verdict.
Dependency-free (Python 3 stdlib) — the framework's promise is "clone it and it runs on plain python3",
and a product manager should not need npm to see their own product.

    python3 tools/ui/serve.py                 # discovers the instance from the current folder
    python3 tools/ui/serve.py path/to/product  # or point at one directly
    python3 tools/ui/serve.py --port 7788 --no-open

**Read-only by design.** There is no write path at all: no POST route, no file is ever created or
modified. The human works with an agent, the agent writes the files, and this console shows what the
files now say. That is what keeps a UI from becoming a form that bypasses the method — see
tools/ui/README.md, and EXTENDING.md for how the framework itself is changed.

Binds to 127.0.0.1 only, and reads nothing outside the instance folders and the framework root.
"""
import argparse
import json
import mimetypes
import os
import re
import subprocess
import sys
import threading
import time
import webbrowser
from html import escape
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, quote, urlparse

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # tools/ui -> root
sys.path.insert(0, os.path.join(ROOT, "tools"))

from loops import framework as F  # noqa: E402
from loops import instance as I  # noqa: E402
from loops import text as T  # noqa: E402

APP_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "app")
WATCH_EXT = (".md", ".yaml", ".yml", ".csv")
WATCH_INTERVAL = 1.5


# ---------------------------------------------------------------- watching


def signature(path):
    """A cheap fingerprint of an instance folder: which files exist and when they changed."""
    parts = []
    for base, dirs, files in os.walk(path):
        dirs[:] = [d for d in dirs if not d.startswith(".")]
        for f in sorted(files):
            if f.endswith(WATCH_EXT):
                p = os.path.join(base, f)
                try:
                    st = os.stat(p)
                except OSError:
                    continue
                parts.append("%s:%d:%d" % (os.path.relpath(p, path), st.st_mtime_ns, st.st_size))
    return "|".join(parts)


class Watcher:
    """Polls the instance folder and bumps a revision counter — SSE clients follow the counter.

    Polling (not fsevents/inotify) keeps this stdlib-only and behaves the same on every platform;
    at a 1.5s tick the cost is unmeasurable for a folder of markdown.
    """

    def __init__(self, path):
        self.path = path
        self.rev = 0
        self._sig = signature(path)
        self._stop = threading.Event()
        self._t = threading.Thread(target=self._run, daemon=True)
        self._t.start()

    def _run(self):
        while not self._stop.wait(WATCH_INTERVAL):
            try:
                sig = signature(self.path)
            except OSError:
                continue
            if sig != self._sig:
                self._sig = sig
                self.rev += 1

    def stop(self):
        self._stop.set()


# ---------------------------------------------------------------- linter


# The check letter is open-ended on purpose: a new check must never be invisible here (A-G was
# already dropping the H and I findings on the floor).
LINT_LINE_RE = re.compile(r"^\s*(WARN|ERROR)\s+([A-Z]\d?)\s+(?:\[([^\]]+)\]\s*)?(.*)$")


def run_lint(inst_path=None):
    """Run the canon linter on the served instance and structure its output.

    Named explicitly rather than left to discovery: with no argument the linter checks every instance
    it can find, so a product manager looking at one product would be shown findings about another —
    and would reasonably read them as their own.
    """
    argv = [sys.executable, os.path.join(ROOT, "tools", "lint.py")]
    if inst_path:
        argv.append(inst_path)
    try:
        p = subprocess.run(argv, capture_output=True, text=True, timeout=60)
        out = p.stdout
        code = p.returncode
    except Exception as e:  # linter absent or unrunnable — report instead of hiding
        return {"ok": False, "error": str(e), "findings": [], "exit": None}
    findings = []
    for line in out.splitlines():
        m = LINT_LINE_RE.match(line)
        if m:
            findings.append({"level": m.group(1).lower(), "check": m.group(2),
                             "scope": m.group(3) or "", "message": m.group(4).strip()})
    return {"ok": True, "exit": code, "findings": findings, "raw": out}


# ---------------------------------------------------------------- payload


def model_payload(inst_path):
    m = I.load(inst_path, ROOT)
    m["framework"] = {
        "root": ROOT,
        "library": F.tool_cards(ROOT),
        "skills": F.skills(ROOT, inst_path),
        "statuses": F.statuses(ROOT),
        "enums": {label: sorted(vals) for label, (vals, _) in F.ENUMS.items()},
        "tick_values": F.TICK_VALUES,
        "confidence": F.CONFIDENCE,
        "homed_sections": sorted(F.homed_sections(ROOT)),
    }
    return m


# ---------------------------------------------------------------- export


def _js_string_safe(payload):
    """Make a JSON blob safe to sit inside a <script> element.

    Two sequences would end the script early or open a comment: `</` and `<!--`. Escaping the slash
    is invisible to JSON.parse and to the JS parser, so the embedded model survives verbatim. The two
    line separators are legal in JSON strings but not in JS source before ES2019 — escape them too.
    """
    return (payload.replace("</", "<\\/").replace("<!--", "<\\!--")
            .replace("\u2028", "\\u2028").replace("\u2029", "\\u2029"))


def export_html(inst_path):
    """One self-contained page for one product: the app, its stylesheet, and a frozen model.

    Same renderer, same stylesheet, same read layer — the only difference is that the data is baked
    in instead of fetched, so a shared file cannot drift from what the console shows. Nothing is
    loaded from the network: no web font, no script, no image. It opens on a machine that has never
    heard of this framework, offline, and looks identical.
    """
    model = model_payload(inst_path)
    lint = run_lint(inst_path)
    with open(os.path.join(APP_DIR, "app.css"), encoding="utf-8") as f:
        css = f.read()
    with open(os.path.join(APP_DIR, "app.js"), encoding="utf-8") as f:
        js = f.read()
    snap = {"model": model, "lint": lint, "generated": time.strftime("%Y-%m-%d %H:%M")}
    blob = _js_string_safe(json.dumps(snap, ensure_ascii=False))
    title = "%s — very-ai-product-loops" % (model.get("product") or model.get("name") or "product")
    page = (
        "<!doctype html>\n<html lang=\"%s\">\n<head>\n<meta charset=\"utf-8\">\n"
        "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n"
        "<title>%s</title>\n<style>\n%s\n</style>\n</head>\n<body>\n"
        "<div id=\"snap\"></div>\n"
        "<header class=\"top\">\n  <div class=\"brand\">\n    <div class=\"mark\">loops</div>\n"
        "    <div class=\"who\">\n      <h1 id=\"product\"></h1>\n"
        "      <div class=\"sub\" id=\"subline\"></div>\n    </div>\n  </div>\n"
        "  <div class=\"acts\" id=\"acts\"></div>\n</header>\n"
        "<div class=\"navwrap\">\n"
        "  <nav class=\"rail\" id=\"rail\" aria-label=\"steps\"></nav>\n"
        "  <nav class=\"tabs\" id=\"tabs\"></nav>\n</div>\n"
        "<main id=\"view\"></main>\n"
        "<footer class=\"foot\"><span id=\"footpath\"></span><span class=\"dot\">\u00b7</span>"
        "<span id=\"footrev\"></span></footer>\n"
        "<script>window.__SNAPSHOT__ = %s;</script>\n<script>\n%s\n</script>\n</body>\n</html>\n"
        % (model.get("language") or "en", escape(title), css, blob, js))
    return page, model


def export_filename(model):
    """`<product>-<date>.html` — the name a human recognises, for a file on disk."""
    raw = (model.get("product") or model.get("name") or "product").strip().replace("/", "-")
    return "%s-%s.html" % (raw or "product", time.strftime("%Y-%m-%d"))


def export_disposition(model):
    """The same name twice: an ascii fallback, and the real one for browsers that read RFC 5987.

    A product named in Cyrillic folds to an empty ascii slug, so the fallback falls back again to the
    folder name and finally to `product`. `filename*` carries the name the human recognises.
    """
    date = time.strftime("%Y-%m-%d")
    raw = (model.get("product") or model.get("name") or "product").strip()
    slug = re.sub(r"[^a-z0-9]+", "-", raw.lower()).strip("-")
    if not slug:
        slug = re.sub(r"[^a-z0-9]+", "-", (model.get("name") or "").lower()).strip("-")
    ascii_name = "%s-%s.html" % (slug or "product", date)
    return "attachment; filename=\"%s\"; filename*=UTF-8''%s" % (
        ascii_name, quote(export_filename(model), safe=""))


def write_export(inst, out):
    """`--export`: the same page the console hands over, written straight to disk.

    The server is one way to reach the snapshot, not the only one — the page is built by a function,
    so a terminal can ask for it as easily as a browser. Nothing else changes: same builder, same
    file, and the instance is still only read.
    """
    page, model = export_html(inst["path"])
    name = export_filename(model)
    out = os.path.join(out, name) if (not out or os.path.isdir(out)) else out
    with open(out, "w", encoding="utf-8") as f:
        f.write(page)
    print("very-ai-product-loops · snapshot")
    print("  instance: %s  (%s)" % (inst["path"], inst["kind"]))
    print("  wrote:    %s  (%d KB, one file, opens offline)"
          % (os.path.abspath(out), round(len(page.encode("utf-8")) / 1024)))
    print("  it carries everything the artifacts say — send it only where they may be read")
    return 0


def safe_path(candidate, roots):
    """Resolve a requested file, refusing anything outside the instance or the framework."""
    p = os.path.abspath(candidate)
    for r in roots:
        if p == r or p.startswith(os.path.abspath(r) + os.sep):
            return p
    return None


# ---------------------------------------------------------------- server


class Handler(BaseHTTPRequestHandler):
    server_version = "loops-console"

    # -- plumbing
    def log_message(self, fmt, *args):  # quiet by default; the console is the product, not the log
        if self.server.verbose:
            sys.stderr.write("  %s\n" % (fmt % args))

    def _send(self, code, body, ctype="application/json; charset=utf-8", extra=None):
        if isinstance(body, str):
            body = body.encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        for k, v in (extra or {}).items():
            self.send_header(k, v)
        self.end_headers()
        self.wfile.write(body)

    def _json(self, obj, code=200):
        self._send(code, json.dumps(obj, ensure_ascii=False), "application/json; charset=utf-8")

    # -- routes
    def do_GET(self):
        u = urlparse(self.path)
        q = parse_qs(u.query)
        route = u.path
        try:
            if route == "/":
                return self._static("index.html")
            if route.startswith("/app/"):
                return self._static(route[len("/app/"):])
            if route == "/api/instances":
                return self._json({"instances": self.server.candidates,
                                   "current": self.server.instance_path,
                                   "framework": ROOT})
            if route == "/api/add":
                # a folder the human points at now — this is a local tool, and reading a folder the
                # human named is the whole feature ("add a folder, see the product")
                raw = (q.get("path", [""])[0] or "").strip()
                cand = os.path.abspath(os.path.expanduser(raw))
                if not os.path.isdir(cand):
                    return self._json({"error": "no such folder: %s" % cand}, 400)
                found = I.discover(cand, ROOT)
                own = [c for c in found if c["path"] == cand or c["path"].startswith(cand + os.sep)]
                if not own:
                    return self._json({"error": "no instance found in %s — an instance is a folder with "
                                                "config.yaml, or with step artifacts and state.yaml" % cand,
                                       "instances": self.server.candidates}, 404)
                known = {c["path"] for c in self.server.candidates}
                for c in own:
                    if c["path"] not in known:
                        self.server.candidates.append(c)
                first = next((c for c in own if not c["umbrella"]), own[0])
                self.server.switch(first["path"])
                return self._json({"instances": self.server.candidates, "current": first["path"]})
            if route == "/api/skills":
                path = q.get("instance", [self.server.instance_path])[0]
                p = self._resolve_instance(path)
                if not p:
                    return self._json({"error": "instance outside the served roots"}, 403)
                return self._json({"skills": F.skills(ROOT, p)})
            if route == "/api/model":
                path = q.get("instance", [self.server.instance_path])[0]
                p = self._resolve_instance(path)
                if not p:
                    return self._json({"error": "instance outside the served roots"}, 403)
                if p != self.server.instance_path:
                    self.server.switch(p)
                return self._json({"rev": self.server.watcher.rev, "model": model_payload(p)})
            if route == "/api/export":
                # one product, one file — the instance the human is looking at, and nothing else
                path = q.get("instance", [self.server.instance_path])[0]
                p = self._resolve_instance(path)
                if not p:
                    return self._json({"error": "instance outside the served roots"}, 403)
                page, model = export_html(p)
                return self._send(200, page, "text/html; charset=utf-8",
                                  {"Content-Disposition": export_disposition(model)})
            if route == "/api/lint":
                path = q.get("instance", [self.server.instance_path])[0]
                p = self._resolve_instance(path)
                if not p:
                    return self._json({"error": "instance outside the served roots"}, 403)
                return self._json(run_lint(p))
            if route == "/api/file":
                rel = q.get("path", [""])[0]
                p = safe_path(os.path.join(self.server.instance_path, rel),
                              [self.server.instance_path, ROOT])
                if not p or not os.path.isfile(p):
                    return self._json({"error": "not found"}, 404)
                return self._send(200, T.read(p), "text/plain; charset=utf-8")
            if route == "/api/events":
                return self._sse()
            return self._json({"error": "no such route"}, 404)
        except BrokenPipeError:
            pass
        except Exception as e:  # never take the console down on one bad read
            return self._json({"error": "%s: %s" % (type(e).__name__, e)}, 500)

    def _resolve_instance(self, path):
        roots = [c["path"] for c in self.server.candidates] + [self.server.instance_path]
        return safe_path(path, roots)

    def do_POST(self):
        # The console has no write path: every change to the instance goes through the agent and the
        # operating loop. Answering here (instead of leaving the verb unhandled) makes that explicit.
        return self._json({"error": "the console is read-only — the agent writes the files"}, 405)

    def _static(self, name):
        p = safe_path(os.path.join(APP_DIR, name), [APP_DIR])
        if not p or not os.path.isfile(p):
            return self._json({"error": "not found"}, 404)
        ctype = mimetypes.guess_type(p)[0] or "application/octet-stream"
        if ctype.startswith("text/") or ctype in ("application/javascript",):
            ctype += "; charset=utf-8"
        with open(p, "rb") as f:
            return self._send(200, f.read(), ctype)

    def _sse(self):
        """Server-sent events: one line per change. Simpler than websockets and stdlib-only."""
        self.send_response(200)
        self.send_header("Content-Type", "text/event-stream; charset=utf-8")
        self.send_header("Cache-Control", "no-cache")
        self.send_header("Connection", "keep-alive")
        self.end_headers()
        last = -1
        try:
            while True:
                rev = self.server.watcher.rev
                if rev != last:
                    last = rev
                    self.wfile.write(("data: %d\n\n" % rev).encode("utf-8"))
                    self.wfile.flush()
                else:
                    self.wfile.write(b": ping\n\n")  # keeps proxies and idle sockets awake
                    self.wfile.flush()
                time.sleep(1.0)
        except (BrokenPipeError, ConnectionResetError):
            return


def main(argv=None):
    ap = argparse.ArgumentParser(description="Local console for a very-ai-product-loops instance.")
    ap.add_argument("path", nargs="?", default=os.getcwd(),
                    help="instance folder, or a folder to discover one in (default: current)")
    ap.add_argument("--export", nargs="?", const="", metavar="FILE_OR_DIR",
                    help="write the shareable snapshot and exit — no server, no port, no browser "
                         "(default name: <product>-<date>.html in the current folder)")
    ap.add_argument("--port", type=int, default=7777)
    ap.add_argument("--host", default="127.0.0.1", help="loopback by default — this is a local tool")
    ap.add_argument("--no-open", action="store_true", help="don't open a browser")
    ap.add_argument("--verbose", action="store_true")
    args = ap.parse_args(argv)

    candidates = I.discover(args.path, ROOT)
    if not candidates:
        print("No instance found in %s.\n"
              "An instance is a folder with config.yaml (canon: `product/` of the repo the framework\n"
              "was installed into). Point at one directly: python3 tools/ui/serve.py path/to/product"
              % os.path.abspath(args.path), file=sys.stderr)
        return 2
    current = candidates[0]

    if args.export is not None:
        return write_export(current, args.export)

    httpd = ThreadingHTTPServer((args.host, args.port), Handler)
    httpd.candidates = candidates
    httpd.instance_path = current["path"]
    httpd.watcher = Watcher(current["path"])
    httpd.verbose = args.verbose

    def switch(path):
        """Follow the human to another instance: watch the folder they are actually looking at."""
        if path == httpd.instance_path:
            return
        httpd.instance_path = path
        old, httpd.watcher = httpd.watcher, Watcher(path)
        old.stop()

    httpd.switch = switch

    url = "http://%s:%d/" % (args.host, args.port)
    print("very-ai-product-loops · console")
    print("  instance:  %s  (%s)" % (current["path"], current["kind"]))
    if len(candidates) > 1:
        print("  also found: %s" % ", ".join(c["name"] for c in candidates[1:]))
    print("  framework: %s" % ROOT)
    print("  serving:   %s   (Ctrl+C to stop)" % url)
    print("  read-only: this phase never writes to the instance")
    if not args.no_open:
        threading.Timer(0.4, lambda: webbrowser.open(url)).start()
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nstopped.")
    finally:
        httpd.watcher.stop()
    return 0


if __name__ == "__main__":
    sys.exit(main())
