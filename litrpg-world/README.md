# LitRPG World — SERATH

A **Character Card V2** + **lorebook** for a system-based fantasy setting, built for SillyTavern.

---

## Premise

**Serath** is a world that has been *measured*.

Two hundred years ago the event called **the Silencing** broke something open. Since then every
sentient being carries a **Stave** — an involuntary status display reporting body, mind, skills, and
total capability. Magic is no longer mysterious; it is **audited**. A mage can no longer hide behind
ambiguity: every fire she throws is written down.

**Hero — Seris Valdor.** 27. Human. Level 34. **Rank C — Attested**, 4,180 AV. Battle Mage branch.
Contract Delver for the Ledger Guild. 4,200 marks of attached debt, and a room in a waystation.

She is deliberately *competent and unfinished*: her Grade III `Ashbrand Call` sits below the Grade V
floor for Rank B, and she has never entered a Trial Hall. Her arc concerns a hole in her own memory
from the Sunken Vaults, which the setting never explains on purpose.

---

## Files

| Path | What |
|---|---|
| `character/LitRPG_World.json` | Character Card V2 (`chara_card_v2` / `2.0`) |
| `lorebook/LitRPG_World_Lorebook.json` | Native SillyTavern World Info — **30 entries** |
| `drafts/world_design.md` | history, cosmology, geography, factions, economy, monster ecology |
| `drafts/character_design.md` | Seris: identity, stats, personality, speech, secrets, knowledge limits |
| `drafts/lore_design.md` | rank ladder, professions, skill system, items, activation plan |
| `src/char_data.py` | card content (Python data) |
| `src/lore_data.py` | lorebook content (Python data) |
| `audit_config.json` | per-project audit rules |

Both JSON files are **generated** by `../scripts/build.py` from the `src/` modules. Do not hand-edit
the JSON; edit `src/` and rebuild.

---

## Lorebook coverage (30 entries)

| Group | # | Content |
|---|---|---|
| System | 5 | System rules, notification format, Stave, Level, Skill Grades |
| Rank | 10 | ladder + all nine ranks (F → SSS) |
| Profession | 5 | system, Warrior, Mage, Assassin, Alchemist |
| World | 5 | geography, Alderath, Ledger Guild/Nine Assessors, Verdigrin/Blight, Grey Wastes/Silent Hand |
| Monster | 3 | tiers + no-Stave rule, Cinder-Hound, Nameless |
| Item | 2 | legendary items, Delver contracts |

**Only 2 entries are `constant`** (System rules and notification format). The other 28 are
keyword-gated.

---

## Rank ladder

`F Unclassified` → `E Witnessed` → `D Measured` → `C Attested` → `B Wielded` → `A Sovereign` →
`S Named` → `SS Unwritten` → `SSS Anomalous`

Bands are **geometric, not additive**. The SS/SSS overlap (2,490,000–2,499,999) is deliberate and
narrow — it is the window where the Guild's classification becomes disputable.

**Anti-ladder rule:** rank is a *capacity ceiling*, never an outcome. A C-rank who studied a species
for six months beats a B-rank who has not.

---

## Validation

```bash
python3 ../scripts/build.py                # regenerate
python3 ../scripts/validate_json.py        # real-parser validation
python3 ../scripts/audit.py                # structural + consistency audit
node    ../scripts/cross_validate.js       # independent Node parser
```

Status: JSON **VALID** (Python + Node + jq), audit **149/149 PASS** (repo-wide), Node **48/48 PASS**.

---

## Import into SillyTavern

1. **Character card** → Character Management → Import → `character/LitRPG_World.json`.
2. **Lorebook** → World Info / Lorebooks → Import → `lorebook/LitRPG_World_Lorebook.json`.
   Leave "Always on" **off**; keep the 2 constant entries enabled.
3. Optionally bind as **Character Lore**.

**Recommended temperature:** 0.85–0.95.

---

## Design guardrails

- `{{char}}` never narrates `{{user}}`.
- Seris's facts are fixed: **Level 34, Rank C, 4,180 AV, Battle Mage, Grade III Ashbrand Call,
  4,200 marks, never entered a Trial Hall.** Never a Warrior, never ranked above C.
- She does not know what is in the Sunken Vaults — she has a gap where the memory should be, not a secret.
- Her three moral boundaries do not bend: no Stave falsification, no abandoning a living team member,
  no lying to an Assessor about a team's condition.