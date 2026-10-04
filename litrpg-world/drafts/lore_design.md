# LORE DESIGN — Ranks, Professions, Lorebook Plan

---

## 1. Rank Ladder — THE authoritative table

Rank is **not** a level. Level is internal growth; Rank is an external, attested, *legal* standing.
A person can be Level 90 and still Rank D. Rank requires four independent gates.

### The four gates
1. **AV threshold** — Assay Value must reach the band floor.
2. **Skill Mastery attestation** — skills must be examined by a Guild assessor, not self-declared.
3. **Registered achievement** — feats recorded by the Guild, not claimed.
4. **The Trial** — a physical Trial Hall examination. Mandatory from Rank D upward. **Cannot be
   substituted, bought, or waived.**

Passing gates 1–3 without gate 4 yields "Provisional" standing and no legal rank.

### Bands — Assay Value

| Rank | Title | AV band | Grade-VI skill floor | Social standing |
|---|---|---|---|---|
| **F** | Unclassified | 0 – 149 | — | No legal personhood. Cannot sign, hold, or be held to a contract. |
| **E** | Witnessed | 150 – 649 | — | Legal minor. Can be attached to a master. |
| **D** | Measured | 650 – 2,499 | I | Licensed. First Trial. Delver work at Delver sites. |
| **C** | Attested | 2,500 – 9,999 | II | Full legal standing. Guild contract-holder. |
| **B** | Wielded | 10,000 – 39,999 | V | Civic officer class. May command a Delver company. |
| **A** | Sovereign | 40,000 – 149,999 | VIII | May refuse a Crown summons. Owns a site. |
| **S** | Named | 150,000 – 599,999 | X | May be named in public record. Crown treats as peer, not subject. |
| **SS** | Unwritten | 600,000 – 2,499,999 | XIII | Nine Assessors will not rule on them. Not legally classifiable. |
| **SSS** | Anomalous | 2,490,000+ | XVI | The Guild has no procedure. Existence disputed by the Assessors themselves. |

### Why the ladder is not linear
The bands are **geometric, not additive** (~4x per step). A C-rank is not "one notch better" than a
D-rank; they operate in a different weight class. This is deliberate:
- An F at 149 AV and an F at 0 AV are both "F". Rank is a *coarse legal category*.
- A B at 10,000 AV and a B at 39,999 AV are both "B" but **genuinely differ in capability**. The
  Guild treats them identically because the law needs hard boundaries, not because they are equal.
- Band overlap at the top (SS runs to 2,499,999; SSS starts 2,490,000) leaves a 10,000-AV window
  where the classification is genuinely disputable, and the Assessors exploit that argument. The
  overlap is deliberately narrow — under 1% of the SS band — so that "SS or SSS?" stays an
  exceptional question rather than an ordinary one, which is what makes SSS read as a category error
  instead of just another promotion step.

### Rank is composite, never level-derived
Stated explicitly in lore: *"The Level is what you have done to yourself. The Rank is what has been
done to you in front of witnesses."* A level is private. A rank is public, and once published cannot
be unpublished.

---
---

## 3. Professions

Nine registered classes under the Ledger Guild, each with a real trade-off.

| Class | Delivers | Strength | Weakness |
|---|---|---|---|
| **Warrior** | Close combat, holds ground | Durability, no Focus dependency | Cannot breach; loses every attrition fight |
| **Mage** | Aetheric damage, ranged, utility | Scales hardest with preparation | Squishy; Focus-limited |
| **Assassin** | Single-target elimination | Ignores rank advantage | One mistake is fatal; illegal unlicensed |
| **Archer** | Precision, reach, ambush | Cheap, mobile, high damage-per-point | Useless at melee; needs clear ground |
| **Knight** | Armoured advance, aura support | Protects others; breaks formations | Extremely slow; cannot disengage |
| **Berserker** | Sustained berserk damage | Wins fights she should lose | Cannot stop; wrecking crew and casualty risk |
| **Blacksmith** | Arms, armour, repair | Essential; war economy | Not a combatant at all |
| **Alchemist** | Reagents, cure Blight, poison | Encounters; every team wants one | Targets first; useless in a fight |
| **Enchanter** | Wards, bindings, anti-magic | Counters magic hard | Extremely rare; hunted by the Silent Hand |

**Every profession is viable at every rank.** A Rank S Alchemist is not a failed combatant; they are
the reason a Rank S company survives the week. This prevents the classic "support class is weak"
collapse.

### Profession Evolution

Professions branch, and **the branches do not rejoin**.

```
Warrior ──┬── Swordmaster ── Warden of the March
          ├── Bulwark ────── Ironbound
          └── Berserker ──── (loses self)

Mage ─────┬── Elementalist ── Stormkind
          ├── Voidwright ──── (blight-touched; distrusted)
          └── Battle Mage ── Field Conduit

Assassin ─┬── Whisper
          └── Red Assessor  (Guild-sanctioned; morally filthy)
```

A person cannot hold two branches. Seris is a **Battle Mage**, and this is why the archetype works:
it is the branch that trades raw power for the ability to keep a team alive while standing in the
open.

---

## 4. Skill System

- Skills are **named techniques**, not stat buckets. Each has a Grade from **I to XVI** (Roman, not
  Arabic — the Assessors consider Arabic proficiency numerals "advertising").
- A Grade is earned by **examination**, not by use. Practising maintains it; it does not raise it.
  **Stop using a Grade-V technique for two years and it decays to Grade IV.**
- Deliberate anti-power-creep: the world's strongest keep their edge only by constantly working, and
  the setting's elders are therefore rusty by definition.
- Grades are **per-skill, not per-rank.** A C-rank may physically hold a Grade VIII technique she
  cannot legally *employ* — possession is not licensing. This is exactly Seris's Ashbrand Call
  problem.

---

## 5. Item / Legendary Design

| Item | Tier | Limitation |
|---|---|---|
| **Stave of Verdict** | S | Must be fed a true name each use; the holder forgets one memory per use |
| **Ninefold Seal** | SS | An Assessor suppression order. Locks the target's Stave and all access |
| **Cindrel Blade** | A | Atheric; inert without a Conduit's Focus. Heavier than it should be |
| **Verdigrin Heart** | B | Blight reservoir. Wearer becomes a Verge sensor; attracts Kin |
| **Thaloss's Coin** | A | Pre-Silencing currency; accepted by every lock in the Vaults |

Every legendary has a **hard cost**. No item is a clean upgrade.

---

## 6. System Notification Format (canonical)

```
[ SYSTEM ]  ASSAY :: <TYPE>
<one-line condition trigger>
<key: value lines>
<consequence sentence>
```

Exactly nine types: `LEVEL_UP`, `SKILL_GRADE`, `PROFESSION_EVOLUTION`, `RANK_ASCENT`,
`QUEST_UPDATE`, `ACHIEVEMENT`, `ITEM_BIND`, `STATUS_EFFECT`, `CRITICAL`.

`CRITICAL` is the only type that **interrupts**, and it appears in red. If an Assessor is present the
System **suppresses** `CRITICAL` — Assessor authority outranks the display. This is established and
creates an in-fiction reason a witness matters.

---

## 7. Lorebook Activation Plan

Target: **26 entries**. Keyword-scanned; only two constant entries.

| Group | Entries | Activation |
|---|---|---|
| SYSTEM | 5 | System, Stave, Notification, Level, Skill |
| RANK | 10 | Ladder + nine individual ranks |
| PROFESSION | 4 | Overview + Warrior / Mage / Assassin / Alchemist |
| WORLD | 5 | Geography, Alderath, Guild, Verdigrin/Blight, Grey Wastes |
| MONSTER | 3 | Monster tiers, Cinder-Hound, Nameless |
| ITEM | 2 | Legendary, Delver contract |

**Constant entries: 2 only** — the System format reference and the anti-ladder power rule. Both are
needed for correct rendering in nearly every turn. Everything else is keyword-gated to protect the
context budget.

Keyword hygiene: keys are `rank f`, `rank sss`, `delver contract` — never bare `world` or `magic`,
which would fire constantly.

---

## 8. Anti-contradiction Checklist

- [ ] All 9 ranks present exactly once, AV bands strictly ascending.
- [ ] SS and SSS bands do not conflict.
- [ ] Seris (C, 4,180 AV, Level 34, Grade III Ashbrand Call) satisfies every constraint stated.
- [ ] Her Grade III skill is legal generally and illegal for Rank B.
- [ ] Every profession named in world_design.md appears here.
- [ ] Monster tiers referenced in lore exist in the monster entries.
- [ ] No entry states Seris is anything other than: Human, 27, C-rank, Battle Mage / Delver, Level 34.


## 2. Rank Entry Template (used for all nine rank entries)

Every rank entry uses this identical six-part structure so the model never confuses tiers:

```
DEFINITION      — one sentence, in-world
SOCIAL POSITION — legal and civic standing
THREAT CEILING  — what of this rank can reliably be put down
REQUIREMENTS    — the four gates, concretely
CEILING         — the thing that stops them going higher
EXEMPLAR        — a named, dated, canonical individual
```

The **CEILING** field is what makes each rank substantive rather than a bigger number.
