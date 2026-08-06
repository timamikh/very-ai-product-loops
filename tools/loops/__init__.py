"""very-ai-product-loops — the shared read layer.

One parser for the canon, used by every piece of tooling (the linter `tools/lint.py`, the local UI
`tools/ui/`, and anything added later). A second parser would drift from the canon and reintroduce
exactly the class of bug the linter exists to kill — so *nothing* re-implements frontmatter, section
anchors, register tables, or the two instance YAML files. It reads; it never writes.

Modules:
  text       — markdown/frontmatter primitives (frontmatter, section ids, tables)
  yamlite    — the small YAML subset used by config.yaml / state.yaml (stdlib only, no PyYAML)
  framework  — the framework side: steps, statuses, library tools
  instance   — the product side: config, state, artifacts, registers, metrics, sources
"""
from . import text, yamlite, framework, instance  # noqa: F401

__all__ = ["text", "yamlite", "framework", "instance"]
