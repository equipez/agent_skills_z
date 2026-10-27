#!/usr/bin/env python3
"""Report LaTeX overfull hbox warnings with source snippets.

Usage:
    latex_overfull_report.py /path/to/thesis.log --root /path/to/project --min-pt 5
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path


OVERFULL_RE = re.compile(
    r"Overfull \\hbox \((?P<width>[0-9.]+)pt too wide\) "
    r"(?:in paragraph at lines (?P<start>\d+)--(?P<end>\d+)|detected at line (?P<line>\d+))"
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("log", type=Path)
    parser.add_argument("--root", type=Path, default=None)
    parser.add_argument("--min-pt", type=float, default=5.0)
    parser.add_argument("--context", type=int, default=2)
    parser.add_argument("--limit", type=int, default=0)
    return parser.parse_args()


def build_line_map(log_text: str, root: Path | None) -> dict[int, Path]:
    """Best-effort map from log line number to current included TeX file."""
    current: Path | None = None
    mapping: dict[int, Path] = {}
    tex_path_re = re.compile(r"(?P<path>[A-Za-z0-9_./-]+\.tex)\b")
    for i, line in enumerate(log_text.splitlines(), start=1):
        for match in tex_path_re.finditer(line):
            candidate = Path(match.group("path"))
            if root is not None and not candidate.is_absolute():
                candidate = root / candidate
            if candidate.exists():
                current = candidate
        if current is not None:
            mapping[i] = current
    return mapping


def snippet(path: Path | None, start: int, end: int, context: int) -> str:
    if path is None or not path.exists():
        return ""
    lines = path.read_text(errors="replace").splitlines()
    lo = max(1, start - context)
    hi = min(len(lines), end + context)
    return "\n".join(f"{n}: {lines[n - 1]}" for n in range(lo, hi + 1))


def main() -> int:
    args = parse_args()
    log_text = args.log.read_text(errors="replace")
    root = args.root.resolve() if args.root else args.log.parent.resolve()
    line_map = build_line_map(log_text, root)

    entries = []
    for log_no, line in enumerate(log_text.splitlines(), start=1):
        match = OVERFULL_RE.search(line)
        if not match:
            continue
        width = float(match.group("width"))
        if width < args.min_pt:
            continue
        if match.group("line"):
            start = end = int(match.group("line"))
        else:
            start = int(match.group("start"))
            end = int(match.group("end"))
        source = line_map.get(log_no)
        entries.append((width, log_no, source, start, end))

    entries.sort(reverse=True, key=lambda item: item[0])
    if args.limit:
        entries = entries[: args.limit]

    for width, log_no, source, start, end in entries:
        source_text = str(source.relative_to(root)) if source and source.is_relative_to(root) else str(source or "unknown")
        print(f"WIDTH {width:.5g}pt | log {log_no} | {source_text}:{start}-{end}")
        text = snippet(source, start, end, args.context)
        if text:
            print(text)
        print("---")

    print(f"{len(entries)} overfull hbox warning(s) >= {args.min_pt:g}pt")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
