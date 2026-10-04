# attax — SillyTavern worldbuilding

A repo of **character cards + lorebooks** for SillyTavern. Each project is self-contained: its own
character JSON, lorebook JSON, design drafts, and Python source-of-truth modules.

## Projects

| Project | Card | Lorebook entries | Theme |
|---|---|---|---|
| **[`litrpg-world/`](litrpg-world/)** | Seris Valdor (CCv2) | 30 | System-based fantasy. A world that was *measured*; magic is audited. Rank F→SSS. |
| **[`sciw/`](sciw/)** | Ryl Ansel (CCv2) | 99 | **Super Complex Isekai World (VYRENN)** — everyone has a status panel, so being *Unclassed* is the twist. Rank E→SSS + Transcendent. |

## Repo layout

```
attax/
├── README.md                    ← this file
├── litrpg-world/                ← project 1
│   ├── README.md
│   ├── character/LitRPG_World.json
│   ├── lorebook/LitRPG_World_Lorebook.json
│   ├── drafts/                  ← design docs
│   ├── src/                     ← char_data.py + lore_data.py (source of truth)
│   └── audit_config.json
├── sciw/                        ← project 2
│   ├── README.md
│   ├── character/SCIW.json
│   ├── lorebook/SCIW_Lorebook.json   ← 99 entries
│   ├── drafts/
│   ├── src/
│   └── audit_config.json
├── scripts/                     ← generic tooling for ALL projects
│   ├── build.py                 ← regenerate every JSON from src/
│   ├── validate_json.py         ← real-parser validation
│   ├── audit.py                 ← structural + consistency audit
│   └── cross_validate.js        ← independent Node validation
└── validation/                  ← generated reports
```

## Toolchain (one generic set for every project)

All JSON is **generated** by `build.py` from the per-project `src/` modules via `json.dump()`. This
makes trailing commas, unescaped quotes, raw newlines, markdown fences, and truncation *structurally
impossible* rather than merely unlikely. To change content, edit `src/` and rebuild — do not
hand-edit the JSON.

```bash
python3 scripts/build.py                # rebuild every project
python3 scripts/build.py sciw           # rebuild one project
python3 scripts/validate_json.py        # real-parser JSON validation
python3 scripts/audit.py                # structural + consistency audit
node    scripts/cross_validate.js       # independent Node parser cross-check
```

Adding a new project needs **no new tooling** — drop in `<project>/{character,lorebook}/`, a `src/`
with `char_data.py` + `lore_data.py`, and an optional `audit_config.json`.

## Current validation status

- JSON syntax: **VALID** — Python `json`, Node `JSON.parse`, and `jq` all parse every artifact.
- `scripts/audit.py`: **149/149 PASS**.
- `scripts/cross_validate.js`: **48/48 PASS**.
- Lorebook entries: `litrpg-world` **30**, `sciw` **99**.

## Schema choice (per project, deliberately not mixed)

- **Character cards → Character Card V2** (`chara_card_v2` / `2.0`), the most widely supported format.
- **Lorebooks → native SillyTavern World Info** (`{ "entries": { "<uid>": {...} } }`), using ST's own
  entry field names so it imports and round-trips without conversion.

Field names were verified against the SillyTavern `release` branch source
(`public/scripts/world-info.js`).

---

## Status

- JSON syntax: **VALID** (Python, Node, and jq all parse both files).
- Structural audit: **76/76 PASS**.
- Node cross-validation: **46/46 PASS**.
- Lorebook entries: **30**.
---

# attax — SillyTavern worldbuilding

A repo of **character cards + lorebooks** for SillyTavern. Each project is self-contained: its own
character JSON, lorebook JSON, design drafts, and Python source-of-truth modules.

## Projects

| Project | Card | Lorebook entries | Theme |
|---|---|---|---|
| **[`litrpg-world/`](litrpg-world/)** | Seris Valdor (CCv2) | 30 | System-based fantasy. A world that was *measured*; magic is audited. Rank F→SSS. |
| **[`sciw/`](sciw/)** | Ryl Ansel (CCv2) | 99 | **Super Complex Isekai World (VYRENN)** — everyone has a status panel, so being *Unclassed* is the twist. Rank E→SSS + Transcendent. |

## Repo layout

```
attax/
├── README.md                    ← this file
├── litrpg-world/                ← project 1 (existing)
│   ├── README.md
│   ├── character/LitRPG_World.json
│   ├── lorebook/LitRPG_World_Lorebook.json
│   ├── drafts/                  ← design docs
│   ├── src/                     ← char_data.py + lore_data.py (source of truth)
│   └── audit_config.json
├── sciw/                        ← project 2 (new)
│   ├── README.md
│   ├── character/SCIW.json
│   ├── lorebook/SCIW_Lorebook.json   ← 99 entries
│   ├── drafts/
│   ├── src/
│   └── audit_config.json
├── scripts/                     ← generic tooling for ALL projects
│   ├── build.py                 ← regenerate every JSON from src/
│   ├── validate_json.py         ← real-parser validation
│   ├── audit.py                 ← structural + consistency audit
│   └── cross_validate.js        ← independent Node validation
└── validation/                  ← generated reports
```

## Toolchain (one generic set for every project)

All JSON is **generated** by `build.py` from the per-project `src/` modules via `json.dump()`. This
makes trailing commas, unescaped quotes, raw newlines, markdown fences, and truncation *structurally
impossible* rather than merely unlikely. To change content, edit `src/` and rebuild — do not
hand-edit the JSON.

```bash
# Rebuild every project
python3 scripts/build.py

# Rebuild one project
python3 scripts/build.py sciw

# Real-parser JSON validation (Python)
python3 scripts/validate_json.py

# Structural + consistency audit (config-driven per project)
python3 scripts/audit.py

# Independent Node parser cross-check
node scripts/cross_validate.js
```

Adding a new project needs **no new tooling** — drop in `<project>/{character,lorebook}/`, a `src/`
with `char_data.py` + `lore_data.py`, and an optional `audit_config.json`.

## Current validation status

- JSON syntax: **VALID** — Python `json`, Node `JSON.parse`, and `jq` all parse every artifact.
- `scripts/audit.py`: **149/149 PASS**.
- `scripts/cross_validate.js`: **48/48 PASS**.
- `litrpg-world` lorebook: 30 entries. `sciw` lorebook: 99 entries.

## Schema choice (per project, deliberately not mixed)

- **Character cards → Character Card V2** (`chara_card_v2` / `2.0`), the most widely supported format.
- **Lorebooks → native SillyTavern World Info** (`{ "entries": { "<uid>": {...} } }`), using ST's own
  entry field names so it imports and round-trips without conversion.

Field names were verified against the SillyTavern `release` branch source (`public/scripts/world-info.js`).
