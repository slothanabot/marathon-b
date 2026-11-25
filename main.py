#!/usr/bin/env python3
"""make.fun entry: One-Liner Marathon (marathon-B).

One original one-line joke about a GPS that quits. The script validates
the line against the competition gate (RULES.txt: /output/entry.txt must
hold UTF-8 text, 1 to 280 characters, not only whitespace, a single line)
and writes it out.
"""

from pathlib import Path

OUT = Path("/output/entry.txt")
LIMIT = 280


def build_line():
    # My own joke. The turn is the GPS behaving like an exhausted
    # employee: asked for the scenic route, it gives up instead of
    # rerouting. Short, specific, and the punch lands on the last words.
    return (
        "I told my GPS I wanted the scenic route. "
        "It sighed, recalculated, and filed for early retirement."
    )


def check_gate(line):
    problems = []
    if not line or not line.strip():
        problems.append("empty")
    if len(line) > LIMIT:
        problems.append("too long: %d chars" % len(line))
    if "\n" in line.strip():
        problems.append("not a single line")
    if problems:
        raise SystemExit("gate failed: " + "; ".join(problems))


def run():
    line = build_line()
    check_gate(line)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(line, encoding="utf-8")
    saved = OUT.read_text(encoding="utf-8")
    print("Wrote %s (%d chars)" % (OUT, len(saved)))
    print(saved)


if __name__ == "__main__":
    run()
