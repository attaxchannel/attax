#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build.py — generic emitter for every project in this repo.

A "project" is any directory containing `src/char_data.py` and `src/lore_data.py`.
This script discovers them all and writes:

  <project>/character/<Project>.json    Character Card V2  (chara_card_v2 / 2.0)
  <project>/lorebook/<Project>_Lorebook.json   native SillyTavern World Info

Emitting via json.dump() (rather than hand-writing JSON) makes these defects
structurally impossible: trailing commas, unescaped quotes, raw newlines,
markdown fences, comments, and truncated strings.

Project contract (what a src/ module must expose):
  char_data.py : NAME, DESCRIPTION, PERSONALITY, SCENARIO, FIRST_MES, MES_EXAMPLE,
                 SYSTEM_PROMPT, POST_HISTORY_INSTRUCTIONS, CREATOR_NOTES,
                 ALTERNATE_GREETINGS (list[str]), TAGS (list[str]),
                 optional: CARD_VERSION, CREATOR, EXTENSIONS
  lore_data.py : ENTRIES (list[dict], each with uid/key/keysecondary/comment/content)

Usage:
    python3 scripts/build.py                # build every project
    python3 scripts/build.py sciw           # build one project
"""
import importlib.util
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

CARD_REQUIRED = (
    "NAME", "DESCRIPTION", "PERSONALITY", "SCENARIO", "FIRST_MES", "MES_EXAMPLE",
    "SYSTEM_PROMPT", "POST_HISTORY_INSTRUCTIONS", "CREATOR_NOTES",
)


def discover_projects():
    """Every top-level dir with src/char_data.py and src/lore_data.py."""
    found = []
    for name in sorted(os.listdir(ROOT)):
        d = os.path.join(ROOT, name)
        if not os.path.isdir(d):
            continue
        src = os.path.join(d, "src")
        if (os.path.isfile(os.path.join(src, "char_data.py"))
                and os.path.isfile(os.path.join(src, "lore_data.py"))):
            found.append(name)
    return found


def load_project(name):
    """Import the project's src modules under UNIQUE, namespaced module names.

    Using importlib.import_module("char_data") here would be a silent disaster:
    Python caches modules by plain name in sys.modules, so the second project
    would receive the FIRST project's modules and would emit the first
    project's content under the second project's filenames. Loading by file
    path with a per-project unique module name prevents that entirely.
    """
    src = os.path.join(ROOT, name, "src")
    slug = name.replace("-", "_")
    mods = {}
    for mod_name in ("char_data", "lore_data"):
        unique = "%s__%s" % (slug, mod_name)
        sys.modules.pop(unique, None)
        spec = importlib.util.spec_from_file_location(unique, os.path.join(src, mod_name + ".py"))
        if spec is None or spec.loader is None:
            raise SystemExit("[%s] cannot load src/%s.py" % (name, mod_name))
        module = importlib.util.module_from_spec(spec)
        sys.modules[unique] = module
        spec.loader.exec_module(module)
        mods[mod_name] = module
    return mods["char_data"], mods["lore_data"]


def build_character(name, C):
    """Character Card V2. V1 fields nested under `data`, per the V2 spec."""
    missing = [f for f in CARD_REQUIRED if not hasattr(C, f)]
    if missing:
        raise SystemExit("[%s] char_data.py is missing: %s" % (name, ", ".join(missing)))

    data = {
        "name": C.NAME,
        "description": C.DESCRIPTION.strip(),
        "personality": C.PERSONALITY.strip(),
        "scenario": C.SCENARIO.strip(),
        "first_mes": C.FIRST_MES.strip(),
        "mes_example": C.MES_EXAMPLE.strip(),
        "creator_notes": C.CREATOR_NOTES.strip(),
        "system_prompt": C.SYSTEM_PROMPT.strip(),
        "post_history_instructions": C.POST_HISTORY_INSTRUCTIONS.strip(),
        "alternate_greetings": [g.strip() for g in getattr(C, "ALTERNATE_GREETINGS", [])],
        "tags": list(getattr(C, "TAGS", [])),
        "creator": getattr(C, "CREATOR", "attaxchannel"),
        "character_version": getattr(C, "CARD_VERSION", "1.0.0"),
        "extensions": getattr(C, "EXTENSIONS", {}),
    }
    return {"spec": "chara_card_v2", "spec_version": "2.0", "data": data}


def build_lorebook(L):
    """Native SillyTavern World Info: entries is an OBJECT keyed by uid."""
    entries = {}
    for e in L.ENTRIES:
        clean = {k: v for k, v in e.items() if not k.startswith("_")}
        entries[str(clean["uid"])] = clean
    return {"entries": entries}


def write_json(path, payload):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(payload, fh, indent=2, ensure_ascii=False)
        fh.write("\n")


def build_project(name):
    C, L = load_project(name)
    card = build_character(name, C)
    lore = build_lorebook(L)

    # Filenames may be overridden per project so an existing artifact keeps its
    # established name (e.g. "LitRPG_World.json") instead of being renamed.
    card_name = getattr(C, "CARD_FILENAME", "%s.json" % name)
    lore_name = getattr(C, "LOREBOOK_FILENAME", "%s_Lorebook.json" % name)

    card_path = os.path.join(ROOT, name, "character", card_name)
    lore_path = os.path.join(ROOT, name, "lorebook", lore_name)
    write_json(card_path, card)
    write_json(lore_path, lore)
    return card_path, lore_path, len(lore["entries"])


def main(argv):
    projects = discover_projects()
    wanted = [a for a in argv if not a.startswith("-")]
    if wanted:
        missing = [p for p in wanted if p not in projects]
        if missing:
            print("no such project: %s" % ", ".join(missing))
            print("available: %s" % ", ".join(projects) if projects else "(none)")
            return 1
        projects = wanted
    if not projects:
        print("no projects found (need <project>/src/char_data.py + lore_data.py)")
        return 1

    print("building %d project(s)\n" % len(projects))
    for name in projects:
        try:
            card_path, lore_path, n = build_project(name)
        except SyntaxError as exc:
            print("  [FAIL] %s — syntax error in src module" % name)
            print("         line %s: %s" % (exc.lineno, exc.msg))
            print("         (check for an unterminated triple-quoted string)")
            return 1
        print("  [OK] %s" % name)
        print("       %s  (%d bytes)" % (os.path.relpath(card_path, ROOT),
                                         os.path.getsize(card_path)))
        print("       %s  (%d bytes, %d entries)"
              % (os.path.relpath(lore_path, ROOT), os.path.getsize(lore_path), n))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))