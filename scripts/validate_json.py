#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
validate_json.py — real-parser validation for this project.

1. Discovers target JSON files (explicit list first, then a *.json sweep).
2. Opens each file as UTF-8 and parses it with json.load().
3. Catches and reports parse errors with file, line and column where available.
4. Prints VALID / INVALID per file.
5. Exits 0 only if every file parsed; non-zero otherwise.

Usage:
    python3 scripts/validate_json.py
    python3 scripts/validate_json.py --quiet
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)


def discover():
    """Every .json in any project directory (has character/ or lorebook/), skipping tooling."""
    found = []
    for base, dirs, files in os.walk(ROOT):
        dirs[:] = [d for d in dirs if d not in {".git", "__pycache__", "validation", "scripts", "drafts"}]
        for name in sorted(files):
            if name.endswith(".json"):
                found.append(os.path.join(base, name))
    return sorted(found)


def validate(path, quiet=False):
    """Return True if the file parses as JSON."""
    rel = os.path.relpath(path, ROOT)
    if not os.path.isfile(path):
        print("[MISSING] %s" % rel)
        return False
    if os.path.getsize(path) == 0:
        print("[EMPTY]   %s" % rel)
        return False
    try:
        with open(path, "r", encoding="utf-8") as fh:
            json.load(fh)
    except json.JSONDecodeError as exc:
        print("[INVALID] %s" % rel)
        print("           line %s, column %s: %s"
              % (exc.lineno, exc.colno, exc.msg))
        if not quiet:
            with open(path, "r", encoding="utf-8", errors="replace") as fh:
                lines = fh.readlines()
            lo = max(0, exc.lineno - 3)
            hi = min(len(lines), exc.lineno + 2)
            for i in range(lo, hi):
                marker = ">>" if i == exc.lineno - 1 else "  "
                print("           %s %5d | %s" % (marker, i + 1, lines[i].rstrip()))
        return False
    except Exception as exc:  # noqa: BLE001 - report anything else verbatim
        print("[INVALID] %s" % rel)
        print("           %s: %s" % (type(exc).__name__, exc))
        return False
    size = os.path.getsize(path)
    print("[VALID]   %s (%d bytes)" % (rel, size))
    return True


def main(argv):
    quiet = "--quiet" in argv
    targets = discover()
    if not targets:
        print("no JSON targets found")
        return 1
    print("validating %d file(s)\n" % len(targets))
    results = [validate(p, quiet) for p in targets]
    ok = sum(1 for r in results if r)
    bad = len(results) - ok
    print("\n%d/%d valid, %d invalid" % (ok, len(results), bad))
    return 0 if bad == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
