# SCIW — Super Complex Isekai World (VYRENN)

A **Character Card V2** + **lorebook** for a LitRPG / isekai setting, built for SillyTavern.

---

## Premise

**VYRENN** is a world where everyone has a status panel — magic is real, gods are real, demons are
real, and every living creature has a system readout reporting Name, Level, Class, Stats, Skills,
Titles, and condition. It is as ordinary as a heartbeat.

Because the panel is universal, **it is not the novelty.** The novelty is being *Unclassed*: a person
the Adventurer's Guild looked at, could not categorise, and wrote `CLASS: NONE` down.

**Hero — Ryl Ansel.** 19. Level 14. Rank E (lowest). **UNCLASSED.** Transmigrated from another world
three years ago with no licence, no record, no party, and one ability nobody else in VYRENN has and
nobody he has met has believed him about.

**[REGISTRY]** — his anomalous System lets him read the standard panel of anyone or anything he has
**directly perceived**. Hard limits: it needs direct perception; it shows **stats only**, never
secrets or motives; each read costs **Focus** scaled by rank; he cannot read anyone he has not met; and
the second column is visible to any Assessor-class skill, so he cannot hide it.

This is an **information power**, not a damage power. He is underpowered on purpose.

---

## Files

| Path | What |
|---|---|
| `character/SCIW.json` | Character Card V2 (`chara_card_v2` / `2.0`) |
| `lorebook/SCIW_Lorebook.json` | Native SillyTavern World Info — **99 entries** |
| `drafts/world_design.md` | Premise, cosmology, geography, factions, isekai mechanics |
| `drafts/character_design.md` | Ryl: identity, stats, personality, speech, secrets |
| `drafts/lore_design.md` | Rank ladder, activation plan, anti-contradiction checklist |
| `src/char_data.py` | Card content (Python data) |
| `src/lore_data.py` | Lorebook content (Python data) |
| `audit_config.json` | Per-project audit rules |

Both JSON files are **generated** by `../scripts/build.py` from the `src/` modules.

---

## Lorebook coverage (99 entries)

| Group | # | Content |
|---|---|---|
| System | 10 | panel, notification format, `[REGISTRY]`, Level, stats, skill grades, status effects, titles, ranks-are-issued, the unanswered question |
| Rank | 9 | ladder + E, D, C, B, A, S, SS, SSS |
| Race | 13 | human, high/wood/dark elf, beastfolk, demonkin, giant, spirit, dragon-kin, undead, celestial, half-blood |
| Magic | 8 | mana + hard/soft divide, divine, demonology, necromancy, alchemy, enchanting, soul-copper, the Weave |
| Class | 8 | system, Unclassed, licensed classes, unlicensed magic, weapons, armour, class-vs-rank, enrolment |
| Geography | 10 | Sunderreach, Hallspath, Great Rift, Dead Lands, Kingdom, Empire, Demon Continent, other lands, Rift mouth, First Calamity |
| Dungeon | 6 | Rift wounds, floors, named bosses, Abysses, echoes, deep floors |
| Monster | 6 | no-panel rule, lesser creatures, constructs, named bosses, Rift-spawn, monstrous races |
| Faction | 9 | Guild, Church, Academy, Demon Court, Nobles, Compact, unlicensed trade, Rift-cults, border traffic |
| Culture | 7 | society, economy, gods, daily life, marriage/half-blood, the Border, the Academy's price |
| Isekai | 6 | Otherworlders, transmigration, summoning, reincarnation, return protocol, the four arrivals |
| Item | 4 | equipment economy, skill stones, legendary, cursed |
| Rules | 3 | power scaling, panel limits, Transcendent |

**Only 2 entries are `constant`** — the System panel format (SYS-00) and the System notification
format (SYS-01), both needed for correct rendering in nearly every turn. The other 97 are
keyword-gated to protect the context budget. The power-scaling rule (RUL-00) is deliberately
*keyword-gated* rather than constant, so it can load on demand when a fight or argument is about to
happen.

---

## Rank ladder

Ranks are **Guild-issued legal standing**, separate from Level, on geometric (~4×) bands:

`E Witnessed` → `D Measured` → `C Attested` → `B Wielded` → `A Sovereign` → `S Named` →
`SS Unwritten` → `SSS Anomalous` → **`TRANSCENDENT`** (not a rank; a category the world has no slot for)

Requires four gates: AV threshold, skill attestation, a registered deed, and **the Trial** — which
cannot be bought, waived, or substituted.

**Anti-ladder rule (applies everywhere):** rank is a *capacity ceiling*, never an outcome. A C-rank
who studied a species for two years reliably beats a B-rank on first sighting.

---

## Validation

```bash
python3 ../scripts/build.py sciw      # regenerate both JSON files
python3 ../scripts/validate_json.py   # real-parser validation
python3 ../scripts/audit.py           # structural + consistency audit
node    ../scripts/cross_validate.js  # independent Node parser
```

Current status: JSON **VALID** (Python + Node + jq), audit **149/149 PASS**, Node **48/48 PASS**.

---

## Import into SillyTavern

1. **Character card** → Character Management → Import → `character/SCIW.json`.
2. **Lorebook** → World Info / Lorebooks panel → Import → `lorebook/SCIW_Lorebook.json`.
   Leave "Always on" **off** so keyword activation works; keep the 2 constant entries enabled.
3. Optionally bind the lorebook as **Character Lore** (globe button) so it loads automatically.

**Recommended temperature:** 0.85–0.95. Ryl is dry and precise and does better slightly hotter.

---

## Design guardrails (do not violate in play)

- `{{char}}` **never** narrates `{{user}}` — no actions, dialogue, feelings, or decisions.
- **[REGISTRY]** limits above are absolute. It never reads minds, never reads through walls or fog,
  and reading a high rank can kill him.
- Ryl's facts are fixed: **Level 14, Rank E, Unclassed, 34 AV, PER 18, no licence, no party, no
  combat ability.** Do not promote him without in-fiction cause and a System notice.
- He is **not** secretly strong, not a hidden heir, not reincarnated royalty.
- The setting's big questions — does the System have an author, what does the Church really do with
  Rift-cores, would closing the Rift heal the world — are **not resolved here**. Anyone claiming to know
  is lying or mistaken, including him.