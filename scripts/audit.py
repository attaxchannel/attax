#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
audit.py — generic structural + consistency audit for every project in this repo.

Runs only after validate_json.py passes. This checks that artifacts are not just
syntactically valid but actually contain what they claim.

Per-project rules come from `<project>/audit_config.json`, so adding a project
needs no code change here. Shared checks run for every project.

Sections (per project):
  A. Files exist, non-empty, parse.
  B. Character Card V2 envelope + required fields.
  C. Lorebook shape (native World Info, min entries, contiguous uids, schema).
  D. Coverage terms from config.
  E. Hygiene: no fences, no placeholders, no comments.
  F. Rank band ordering from config.
  G. Character-fact consistency regexes from config.

Writes a combined report to validation/audit_report.txt. Exit 0 if all pass.
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

V2_REQUIRED = ("name", "description", "personality", "scenario", "first_mes",
               "mes_example", "creator_notes", "system_prompt",
               "post_history_instructions")

results = []


def audit(section, label, ok, detail=""):
    results.append((section, label, bool(ok), detail))


def discover_projects():
    found = []
    for name in sorted(os.listdir(ROOT)):
        d = os.path.join(ROOT, name)
        if not os.path.isdir(d):
            continue
        if (os.path.isdir(os.path.join(d, "character"))
                and os.path.isdir(os.path.join(d, "lorebook"))):
            found.append(name)
    return found


def find_artifact(proj, kind):
    d = os.path.join(ROOT, proj, kind)
    for name in sorted(os.listdir(d)):
        if name.endswith(".json"):
            return os.path.join(d, name)
    return None
def audit_project(proj):
    card_path = find_artifact(proj, "character")
    lore_path = find_artifact(proj, "lorebook")
    cfg_path = os.path.join(ROOT, proj, "audit_config.json")
    cfg = {}
    if os.path.isfile(cfg_path):
        cfg = json.load(open(cfg_path, "r", encoding="utf-8"))

    sec = proj
    audit(sec + " A. Files", "character json present", bool(card_path),
          os.path.basename(card_path) if card_path else "missing")
    audit(sec + " A. Files", "lorebook json present", bool(lore_path),
          os.path.basename(lore_path) if lore_path else "missing")
    if not (card_path and lore_path):
        return
    audit(sec + " A. Files", "character non-empty", os.path.getsize(card_path) > 0,
          "%d bytes" % os.path.getsize(card_path))
    audit(sec + " A. Files", "lorebook non-empty", os.path.getsize(lore_path) > 0,
          "%d bytes" % os.path.getsize(lore_path))

    try:
        card = json.load(open(card_path, "r", encoding="utf-8"))
        lore = json.load(open(lore_path, "r", encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        audit(sec + " A. Files", "both parse", False, str(exc))
        return

    # ---- B. V2 envelope ----
    audit(sec + " B. Card", "spec == chara_card_v2", card.get("spec") == "chara_card_v2",
          str(card.get("spec")))
    audit(sec + " B. Card", "spec_version == 2.0", card.get("spec_version") == "2.0",
          str(card.get("spec_version")))
    data = card.get("data", {})
    audit(sec + " B. Card", "data object present", isinstance(data, dict))
    for field in V2_REQUIRED:
        v = data.get(field)
        audit(sec + " B. Card", "data.%s non-empty string" % field,
              isinstance(v, str) and v.strip() != "",
              "%d chars" % len(v) if isinstance(v, str) else "missing")
    audit(sec + " B. Card", "alternate_greetings is list[str]",
          isinstance(data.get("alternate_greetings"), list) and
          all(isinstance(x, str) for x in data.get("alternate_greetings", [])),
          "%d entries" % len(data.get("alternate_greetings", [])))
    audit(sec + " B. Card", "tags is list[str]",
          isinstance(data.get("tags"), list) and
          all(isinstance(x, str) for x in data.get("tags", [])),
          "%d tags" % len(data.get("tags", [])))
    audit(sec + " B. Card", "extensions is dict", isinstance(data.get("extensions"), dict))
    if cfg.get("expect_name"):
        audit(sec + " B. Card", "name matches config",
              data.get("name") == cfg["expect_name"], str(data.get("name")))
# ---- C. lorebook shape ----
    entries = lore.get("entries")
    audit(sec + " C. Lorebook", "entries is dict keyed by uid",
          isinstance(entries, dict) and not isinstance(entries, list))
    if not isinstance(entries, dict):
        return
    min_entries = cfg.get("min_entries", 15)
    audit(sec + " C. Lorebook", "at least %d entries" % min_entries, len(entries) >= min_entries,
          "%d entries" % len(entries))
    uids = sorted(int(u) for u in entries)
    audit(sec + " C. Lorebook", "uids contiguous from 0", uids == list(range(len(uids))),
          "%d..%d" % (uids[0], uids[-1]))
    schema_bad = 0
    for uid, e in entries.items():
        for f in ("uid", "key", "keysecondary", "content", "comment", "constant",
                  "selective", "selectiveLogic", "order", "position", "disable",
                  "depth", "probability", "useProbability", "group", "role"):
            if f not in e:
                schema_bad += 1
        if not isinstance(e.get("key"), list):
            schema_bad += 1
        if not isinstance(e.get("content"), str) or not e["content"].strip():
            schema_bad += 1
        if e.get("uid") != int(uid):
            schema_bad += 1
    audit(sec + " C. Lorebook", "every entry matches ST entry schema", schema_bad == 0,
          "all %d entries" % len(entries) if schema_bad == 0 else "%d defects" % schema_bad)

    alltext = " ".join((e.get("content", "") + " " + e.get("comment", ""))
                       for e in entries.values())

    # ---- D. coverage from config ----
    for term in cfg.get("must_contain", []):
        audit(sec + " D. Coverage", "lore mentions %r" % term, term in alltext)

    # ---- E. hygiene ----
    for kind, path in (("card", card_path), ("lorebook", lore_path)):
        raw = open(path, encoding="utf-8").read()
        audit(sec + " E. Hygiene", "%s has no markdown fence" % kind, "```" not in raw)
        audit(sec + " E. Hygiene", "%s has no TODO/FIXME/PLACEHOLDER" % kind,
              not re.search(r"\bTODO\b|\bFIXME\b|\bPLACEHOLDER\b", raw))
        audit(sec + " E. Hygiene", "%s has no line comments" % kind,
              not re.search(r"^\s*//", raw, re.M))
        audit(sec + " E. Hygiene", "%s has no block comments" % kind, "/*" not in raw)

    # ---- F. band ordering from config ----
    bands = cfg.get("bands")
    if bands:
        floors = [b[1] for b in bands]
        ascending = all(floors[i] <= floors[i + 1] for i in range(len(floors) - 1))
        audit(sec + " F. Bands", "band floors ascending", ascending,
              "%d bands" % len(bands))

    # ---- G. character consistency from config ----
    blob = " ".join([str(data.get(k, "")) for k in
                     ("description", "personality", "creator_notes")])

    # ---- I. cross-project contamination guard ----
    # A build bug (e.g. sys.modules caching) can cause one project's content to be
    # emitted under another project's filename. Catch it by requiring that each
    # project's character name is distinctive across the repo.
    names = {}
    for other in discover_projects():
        op = find_artifact(other, "character")
        if not op:
            continue
        try:
            names[other] = json.load(open(op, "r", encoding="utf-8")).get("data", {}).get("name")
        except Exception:  # noqa: BLE001
            continue
    expected = cfg.get("expect_name")
    if expected and names.get(proj):
        audit(sec + " I. Isolation",
              "this project's card contains ITS OWN character, not another project's",
              names[proj] == expected,
              "found %r (expected %r)" % (names[proj], expected))
    dupes = [p for p, n in names.items() if n and list(names.values()).count(n) > 1]
    audit(sec + " I. Isolation", "no two projects emit the same character name",
          not dupes, "duplicated: %s" % ", ".join(sorted(set(dupes))) if dupes else "none")
    for label, pattern in cfg.get("char_must_match", {}).items():
        audit(sec + " G. Character", label, re.search(pattern, blob) is not None)

    # char_must_not_match is negation-aware: a phrase preceded by a negator
    # ("not secretly strong", "no hidden heir") is a DISCLAIMER, not a claim.
    # The world design frequently states negative constraints in prose, and a
    # naive regex would flag the disclaimer as the violation it forbids.
    NEGATORS = (r"not", r"no", r"never", r"cannot", r"isn't", r"is not",
                r"never once", r"nothing")
    for label, pattern in cfg.get("char_must_not_match", {}).items():
        ok = True
        for m in re.finditer(pattern, blob, re.I):
            window = blob[max(0, m.start() - 40):m.start()].lower()
            if not any(re.search(r"\b%s\b" % n, window) for n in NEGATORS):
                ok = False
                break
        audit(sec + " G. Character", label, ok)


def main():
    projects = discover_projects()
    if not projects:
        print("no projects found")
        return 1
    for p in projects:
        audit_project(p)

    current = None
    passed = failed = 0
    lines = []
    for section, label, ok, detail in results:
        if section != current:
            lines.append("")
            lines.append(section)
            current = section
        mark = "PASS" if ok else "FAIL"
        lines.append("  [%s] %s%s" % (mark, label, ("  (" + detail + ")") if detail else ""))
        if ok:
            passed += 1
        else:
            failed += 1

    header = "=" * 72
    out = [header, "STRUCTURAL AUDIT — attax (all projects)", header, ""]
    out += lines
    out += ["", header, "TOTAL: %d passed, %d failed" % (passed, failed), header]
    report = "\n".join(out)
    print(report)

    os.makedirs(os.path.join(ROOT, "validation"), exist_ok=True)
    with open(os.path.join(ROOT, "validation", "audit_report.txt"), "w", encoding="utf-8") as fh:
        fh.write(report + "\n")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())