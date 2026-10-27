#!/usr/bin/env python3
"""Report LaTeX vbox page-break warnings with nearby page numbers.

Usage:
    latex_vbox_report.py /path/to/thesis.log --min-badness 1000
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path


VBOX_RE = re.compile(
    r"(?P<kind>Underfull|Overfull) \\vbox "
    r"(?:\(badness (?P<badness>\d+)\)|\((?P<amount>[0-9.]+)pt too high\))"
)
PAGE_RE = re.compile(r"\[(?P<page>\d+)\]")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("log", type=Path)
    parser.add_argument("--min-badness", type=int, default=1000)
    parser.add_argument("--limit", type=int, default=30)
    parser.add_argument("--lookahead", type=int, default=80)
    return parser.parse_args()


def page_tokens(lines: list[str], start: int, stop: int) -> list[int]:
    pages: list[int] = []
    for line in lines[start:stop]:
        pages.extend(int(match.group("page")) for match in PAGE_RE.finditer(line))
    return pages


def main() -> int:
    args = parse_args()
    lines = args.log.read_text(errors="replace").splitlines()

    entries = []
    previous_pages: list[int] = []
    for index, line in enumerate(lines):
        previous_pages.extend(int(match.group("page")) for match in PAGE_RE.finditer(line))
        match = VBOX_RE.search(line)
        if not match:
            continue
        kind = match.group("kind")
        if match.group("badness") is not None:
            score = int(match.group("badness"))
            if score < args.min_badness:
                continue
            score_label = f"badness {score}"
        else:
            score = int(float(match.group("amount")) * 1000)
            score_label = f"{match.group('amount')}pt too high"
        next_pages = page_tokens(lines, index + 1, min(len(lines), index + 1 + args.lookahead))
        prev_page = previous_pages[-1] if previous_pages else None
        next_page = next_pages[0] if next_pages else None
        entries.append((score, index + 1, kind, score_label, prev_page, next_page))

    entries.sort(reverse=True, key=lambda item: item[0])
    if args.limit:
        entries = entries[: args.limit]

    for score, log_no, kind, score_label, prev_page, next_page in entries:
        page_hint = []
        if prev_page is not None:
            page_hint.append(f"prev page {prev_page}")
        if next_page is not None:
            page_hint.append(f"next page {next_page}")
        hint = ", ".join(page_hint) if page_hint else "page unknown"
        print(f"{kind} vbox | {score_label} | log {log_no} | {hint}")

    print(f"{len(entries)} vbox warning(s) reported")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
