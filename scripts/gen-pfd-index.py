#!/usr/bin/env python3
"""Regenerate PFD learnings index files from atom frontmatter.

Scans `skills/pfd/references/learnings/**/*.md` (relative to this script's
parent), extracts YAML frontmatter from each atom, emits:
  - `_index.md`     (human-readable, grouped by layer, sorted by date desc)
  - `_search.json`  (machine-readable, flat JSON array)

Both land in `references/learnings/` and are fully derived — never hand-edit.

Usage:
    python3 scripts/gen-pfd-index.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML not installed. Run: pip install pyyaml", file=sys.stderr)
    sys.exit(1)


SCRIPT_DIR = Path(__file__).resolve().parent
LEARNINGS_ROOT = SCRIPT_DIR.parent / "skills" / "pfd" / "references" / "learnings"

LAYER_NAMES = {
    "L0": "Cognitive Load",
    "L1": "First-Impression Architecture",
    "L2": "Processing Fluency",
    "L3": "Perception Bias Optimization",
    "L4": "Decision Architecture",
    "meta": "Methodology",
    "cross": "Cross-Layer",
}
LAYER_ORDER = ["L0", "L1", "L2", "L3", "L4", "meta", "cross"]


def parse_atom(path: Path) -> dict:
    """Extract YAML frontmatter from an atom file."""
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError(f"{path}: missing frontmatter delimiter '---\\n' at file start")
    end = text.find("\n---\n", 4)
    if end == -1:
        raise ValueError(f"{path}: unterminated frontmatter (no closing '---')")
    fm = yaml.safe_load(text[4:end])
    if not isinstance(fm, dict):
        raise ValueError(f"{path}: frontmatter is not a YAML mapping")
    for required in ("id", "title", "layer", "date"):
        if required not in fm:
            raise ValueError(f"{path}: missing required frontmatter field '{required}'")
    if fm["layer"] not in LAYER_NAMES:
        raise ValueError(
            f"{path}: layer '{fm['layer']}' is not a recognized shard key "
            f"(expected one of {list(LAYER_NAMES.keys())})"
        )
    rel_path = path.relative_to(LEARNINGS_ROOT).as_posix()
    return {
        "id": fm["id"],
        "title": fm["title"],
        "layer": fm["layer"],
        "secondary_layers": fm.get("secondary_layers", []) or [],
        "date": str(fm["date"]),
        "updated": str(fm["updated"]) if fm.get("updated") else None,
        "contributor": fm.get("contributor", ""),
        "related": fm.get("related", []) or [],
        "tags": fm.get("tags", []) or [],
        "path": rel_path,
    }


def collect_atoms() -> list[dict]:
    atoms = []
    for path in sorted(LEARNINGS_ROOT.glob("**/*.md")):
        if path.name.startswith("_") or path.name == ".gitkeep":
            continue
        atoms.append(parse_atom(path))
    return atoms


def render_index_md(atoms: list[dict]) -> str:
    lines = [
        "# PFD Learnings Index",
        "",
        "> Generated from atom frontmatter by `scripts/gen-pfd-index.py`. DO NOT HAND-EDIT.",
        "",
        f"**Total:** {len(atoms)} learning{'s' if len(atoms) != 1 else ''}",
        "",
    ]
    for layer in LAYER_ORDER:
        layer_atoms = sorted(
            [a for a in atoms if a["layer"] == layer],
            key=lambda a: a["date"],
            reverse=True,
        )
        if not layer_atoms:
            continue
        lines.append(f"## {layer} — {LAYER_NAMES[layer]}")
        lines.append("")
        for a in layer_atoms:
            date_str = f"{a['date']}"
            if a["updated"]:
                date_str += f" (updated {a['updated']})"
            lines.append(f"- **{a['id']}** · [{a['title']}]({a['path']}) — {date_str}")
        lines.append("")
    return "\n".join(lines)


def render_search_json(atoms: list[dict]) -> str:
    return json.dumps(atoms, indent=2, ensure_ascii=False) + "\n"


def main() -> int:
    if not LEARNINGS_ROOT.exists():
        print(f"ERROR: learnings root does not exist: {LEARNINGS_ROOT}", file=sys.stderr)
        return 1
    try:
        atoms = collect_atoms()
    except ValueError as exc:
        print(f"ERROR parsing atom frontmatter: {exc}", file=sys.stderr)
        return 2
    (LEARNINGS_ROOT / "_index.md").write_text(render_index_md(atoms), encoding="utf-8")
    (LEARNINGS_ROOT / "_search.json").write_text(render_search_json(atoms), encoding="utf-8")
    print(f"Generated _index.md and _search.json from {len(atoms)} atom{'s' if len(atoms) != 1 else ''}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
