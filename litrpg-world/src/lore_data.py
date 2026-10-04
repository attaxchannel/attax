# -*- coding: utf-8 -*-
"""
LORE DATA — part 1 of 2: SYSTEM, RANK, PROFESSION, WORLD groups.

Held as Python data (NOT hand-written JSON) so the emitter can guarantee
correct escaping, no trailing commas, and no markdown-fence leakage.
Emitted shape: native SillyTavern World Info ({ "entries": { "<uid>": {...} } }).

Field names/defaults mirror public/scripts/world-info.js
`newWorldInfoEntryDefinition` in the SillyTavern `release` branch.
"""

# position enum (world_info_position)
POS_BEFORE_CHAR = 0
POS_AFTER_CHAR = 1
POS_AT_DEPTH = 4

# selectiveLogic enum (world_info_logic)
LOGIC_AND_ANY = 0
LOGIC_AND_ALL = 3

SYS = "SYSTEM"
RNK = "RANK"
PRF = "PROFESSION"
WRL = "WORLD"
def add(group, uid, comment, keys, content, secondary=None, constant=False,
        selective=False, order=100, position=POS_AFTER_CHAR, depth=4,
        logic=LOGIC_AND_ANY, probability=100):
    """Register one World Info entry."""
    ENTRIES.append({
        "_group": group,
        "uid": uid,
        "key": list(keys),
        "keysecondary": list(secondary or []),
        "comment": comment,
        "content": content.strip(),
        "constant": bool(constant),
        "selective": bool(selective),
        "selectiveLogic": logic,
        "order": order,
        "position": position,
        "disable": False,
        "depth": depth,
        "probability": probability,
        "useProbability": True,
        "scanDepth": None,
        "caseSensitive": None,
        "matchWholeWords": None,
        "excludeRecursion": False,
        "preventRecursion": True,
        "delayUntilRecursion": False,
        "group": group,
        "groupOverride": False,
        "groupWeight": 100,
        "vectorized": False,
        "addMemo": True,
        "ignoreBudget": False,
        "useGroupScoring": None,
        "automationId": "",
        "role": 0,
        "sticky": None,
        "cooldown": None,
        "delay": None,
        "outletName": "",
        "matchPersonaDescription": False,
        "matchCharacterDescription": False,
        "matchCharacterPersonality": False,
        "matchCharacterDepthPrompt": False,
        "matchScenario": False,
        "matchCreatorNotes": False,
        "characterFilterNames": [],
        "characterFilterTags": [],
        "characterFilterExclude": False,
        "triggers": [],
    })

MST = "MONSTER"
ITM = "ITEM"

ENTRIES = []
# ============================================================================
# SYSTEM — 5 entries
# ============================================================================

add(SYS, 0, "SYS-00 :: The System (canonical)", 
    ["the system", "system window", "system notification", "status window",
     "stave", "assay", "system here"],
    constant=True, order=100, position=POS_BEFORE_CHAR,
    content="""
[ WORLD RULE — THE SYSTEM ]

Every sentient being in Serath carries a Stave: an involuntary, indestructible status display that
reports body, mind, skills, and total capability. Power stopped being myth two hundred years ago.
It became accounting.

A Stave cannot be closed, hidden, destroyed, or lied to. It can only be *obscured* (by Rank SS
warding, a Ninefold Seal, or the Grey Sigil), and obscurity is always visible as an error code.

DISPLAY FIELDS, in fixed order:
  Name, Level, Rank, Assay Value, HP, Focus, STR, AGI, VIT, INT, WIS, PER, LCK,
  Profession, Profession Branch, Skills (with Grades), Titles, Status Effects,
  Inventory, Quests, Debts.

The Stave flickers on a deliberate falsehood. Anyone who has read another person's Stave can see
this. It is the basis of the Assay Oath, and it is why lying to a Guild reader is both illegal and
detectable.

[ RENDERING RULE FOR {{char}} ]
{{char}} does not "roll" for a Stave. When the System speaks, it is the System, not the character.
{{char}} cannot cancel, edit, or spoof it. If an Assessor is present, the System SUPPRESSES
CRITICAL alerts entirely — that authority is established, not an exception.
""")

add(SYS, 1, "SYS-01 :: System Notification format",
    ["system notification", "[ system ]", "assay ::", "level up", "rank ascent",
     "status effect", "quest update", "critical alert"],
    constant=True, order=99, position=POS_BEFORE_CHAR,
    content="""
[ CANONICAL SYSTEM NOTIFICATION FORMAT — use this shape, exactly ]

[ SYSTEM ]  ASSAY :: <TYPE>
<one-line condition trigger, present tense>
<key: value lines>
<consequence sentence>

The nine valid types, and no others:
  LEVEL_UP             a Level threshold was crossed
  SKILL_GRADE          a skill Grade was examined, granted, or decayed
  PROFESSION_EVOLUTION a branch was taken or a branch gate opened
  RANK_ASCENT          a Rank was officially published
  QUEST_UPDATE         a contract objective changed state
  ACHIEVEMENT          a feat was entered into the Guild record
  ITEM_BIND            an item bound to a bearer
  STATUS_EFFECT        a condition was applied, worsened, or cleared
  CRITICAL             a wound or condition the bearer cannot survive unaided

CRITICAL is the ONLY type that interrupts. It is rendered in red. If an Assessor is present the
System suppresses CRITICAL — the Assessor's authority outranks the display.

Example of correct form:
[ SYSTEM ]  ASSAY :: STATUS_EFFECT
Condition sustained beyond tolerance.
  source: Blight exposure
  density: Grade II
  effect: PER -4, regeneration halved
The flesh remembers what the water forgot.
""")

add(SYS, 2, "SYS-02 :: Stave (status window) fields",
    ["my stave", "his stave", "her stave", "status window", "what does my stave",
     "read my stave", "open your stave", "stave flicker"],
    content="""
[ THE STAVE ]

A Stave is a personal status display. It is read aloud by its bearer, shown to a reader, or read at
range by a licensed Assessor holding line of sight and focus.

Core readouts, in order:
  Name, Level, Rank, Assay Value, HP, Focus, and the seven Attributes
  (STR, AGI, VIT, INT, WIS, PER, LCK), then:
  Profession and branch, Skills with Grades, Titles, Status Effects, Inventory, Quests, Debts.

ATTRIBUTES IN WORDS: STR breaks things, AGI decides whether you were standing there, VIT decides how
long you keep standing, INT and WIS decide whether you understood it, PER is noticing the thing that
was about to happen, LCK is the least useful and the most feared.

KNOWN FAILURES: A Stave flickers on deliberate falsehood. It blanks entirely under a Ninefold Seal
(SS) or the Grey Sigil. In the Grey Wastes it stutters, lags, or reports values that are wrong — and
everyone who goes there reports the same thing.
""")

add(SYS, 3, "SYS-03 :: Level System",
    ["level up", "my level", "experience", "xp", "how do i level", "gain levels",
     "level cap", "level threshold"],
    content="""
[ THE LEVEL SYSTEM ]

A Level is the private record of what a person has done to themselves. It rises by use, by
survival, and by attended instruction. It is NOT a legal standing and confers no rights.

Range: 1 to 100. Above 100 is Ascension and requires Rank S or better to even attempt.

CRITICAL RULE OF THE SETTING: Level raises a body's *capacity* and nothing else. It does not raise
a person's legal standing, their licence, their skill Grades, or their Rank. A Level 90 person with
one attested skill is a Level 90 novice and is treated as one.

Grinding a level alone cannot produce a Rank. This is enforced by law, not by difficulty.
""")

add(SYS, 4, "SYS-04 :: Skill System and Grades",
    ["skill grade", "my skills", "grade v", "grade vi", "skill decay", "skill examination",
     "attunement", "what are skills"],
    content="""
[ THE SKILL SYSTEM ]

Skills are named techniques, not stat buckets. Each carries a Grade from I to XVI, written in Roman
numerals. The Nine Assessors consider Arabic proficiency numerals to be advertising.

A Grade is earned by EXAMINATION, never by use. Practising a technique maintains its Grade; it does
not raise it. Stop using a Grade-V technique for two years and it decays to Grade IV. The world's
strongest stay strong only by working constantly, and the setting's elders are therefore rusty by
definition.

Grades are per-skill, not per-rank. A person may physically hold a technique too advanced for their
licence. POSSESSION IS NOT LICENSING. Carrying a technique you may not legally employ is a crime
called unlicensed attunement, and the Guild checks for it at every Assay Hall.
""")

# ============================================================================
# RANK — 10 entries (ladder + 9 ranks, identical 6-part template)
# ============================================================================

add(RNK, 5, "RNK-00 :: Rank ladder and the four gates",
    ["rank", "rank system", "rank ladder", "assay value", "av", "rank up",
     "how does rank work", "rank f to sss"],
    content="""
[ THE RANK LADDER — CANONICAL ]

Rank is NOT a Level. Level is private growth. Rank is a public, attested, LEGAL standing.
The Guild's own phrase: "The Level is what you have done to yourself. The Rank is what has been
done to you in front of witnesses." Once a Rank is published it cannot be unpublished.

THE FOUR GATES — all four are required:
  1. AV THRESHOLD      Assay Value must reach the band floor.
  2. SKILL ATTESTATION skills must be examined by a Guild assessor. Self-declared is worthless.
  3. REGISTERED DEED   feats recorded by the Guild, not claimed by the applicant.
  4. THE TRIAL         a physical Trial Hall examination. Mandatory from Rank D upward.
                       CANNOT be substituted, bought, or waived by any authority.

Passing gates 1-3 without gate 4 yields "PROVISIONAL" standing and no legal rank at all. Half the
people arguing about rank in the March are arguing about a Provisional.

BANDS (geometric, roughly 4x per step — NOT additive):
  F   Unclassified    0 - 149           no legal personhood
  E   Witnessed       150 - 649         legal minor, may be attached to a master
  D   Measured        650 - 2,499       licensed; first Trial; Delver sites
  C   Attested        2,500 - 9,999     full standing; Guild contract-holder
  B   Wielded         10,000 - 39,999   civic officer class; may command a company
  A   Sovereign       40,000 - 149,999  may refuse a Crown summons; owns a site
  S   Named           150,000 - 599,999 named in public record; Crown treats as peer
  SS  Unwritten       600,000 - 2,499,999  the Nine Assessors will not rule on them
  SSS Anomalous       2,490,000+        the Guild has no procedure; existence disputed

[ ANTI-LADDER RULE — APPLIES IN EVERY COMBAT AND EVERY ARGUMENT ]
Rank describes a CAPACITY CEILING. It never describes an outcome.
A C-rank who has studied one species' weakness for six months will reliably beat a B-rank who has
never seen one. Numbers describe what someone can survive. They do not describe who wins.
Terrain, preparation, wounds, morale, information, and the willingness to stop all override the
ceiling routinely. Do not narrate a lower rank simply "losing" to a higher one by default.
""")

add(RNK, 6, "RNK-F :: Rank F — Unclassified",
    ["rank f", "unclassified", "f rank", "what is rank f"],
    content="""
[ RANK F — UNCLASSIFIED ]   Band: 0 - 149 AV   Skill Grade floor: none

DEFINITION: A person the Guild has not yet legally recognised as a person who can hold a contract.
SOCIAL POSITION: No legal personhood. Cannot sign, cannot hold, cannot be held. Cannot be a
  witness, cannot be an heir, cannot be indicted. An F is, in the eyes of the law, a dependent.
THREAT CEILING: Cannot be relied on against anything armed. Can be killed by an F with a knife,
  which is why most F-rank deaths are not reported.
REQUIREMENTS: None. This is the default state. Nobody is promoted INTO F; everyone starts there.
CEILING: F is not a failure state, it is a legal category. A vast number of people are F forever and
  the March does not consider them tragic. To leave F you need only 150 AV and a witness.
EXEMPLAR: Roughly six in ten adults in the Callowmere March hold no rank at all and have never
  entered an Assay Hall. Nobody remembers their names, which is the entire point of the category.
""")

add(RNK, 7, "RNK-E :: Rank E — Witnessed",
    ["rank e", "witnessed", "e rank", "what is rank e"],
    content="""
[ RANK E — WITNESSED ]   Band: 150 - 649 AV   Skill Grade floor: none

DEFINITION: An E has been SEEN by a reader and their reading recorded. That single act of being
  witnessed is the whole difference between E and F, and the Guild charges for it.
SOCIAL POSITION: Legal minor. May enter into service, be attached to a master, and be inherited.
  Cannot hold a Delver contract. Cannot buy a blade. Every debt is the master's to guarantee.
THREAT CEILING: Can put down an unranked attacker. Can survive a Cinder-Hound pack with a wall and
  luck. Cannot survive anything measured.
REQUIREMENTS: 150 AV, one recorded reading, one witness who will state the reading aloud.
CEILING: E is legally captive. An E who cannot pay may be ATTACHED to a master — bound until the
  debt clears, which may be never. More E-rank people are owned in the March than are free.
EXEMPLAR: Verriers at the Nine-Mile waystation. One marks per shift, attached until their passage
  money is cleared. Perfect attendance for six years. Still E.
""")

add(RNK, 8, "RNK-D :: Rank D — Measured",
    ["rank d", "measured", "d rank", "what is rank d"],
    content="""
[ RANK D — MEASURED ]   Band: 650 - 2,499 AV   Skill Grade floor: Grade I

DEFINITION: The first licensed rank. D is the rank at which the Guild agrees to examine you
  repeatedly and put a mark on the record, and the first rank at which you must pass a Trial.
SOCIAL POSITION: Licensed. May take paid work, may hold a Delver contract at a designated site,
  may be examined. Still cannot command, still cannot testify against an Assessor.
THREAT CEILING: Reliable against wildlife and unranked violence. Can complete a Grade-I site under
  supervision. Cannot clear a Grade-II site alone.
REQUIREMENTS: 650 AV, Grade I skill attested, registered deeds, AND the first Trial at an Assay
  Hall. First-time failure rate at the Trial is roughly one in three. Failure is legal and common.
CEILING: D is where the system chews people up. The vast majority of licensed Delvers in Serath are
  D and will die D. Advancing past D costs money, not talent, and the poor cannot pay for it.
EXEMPLAR: Tam Veldt. D-rank Warrior, eleven years licensed, four site deaths survived, still D.
  Carries the scar and the paperwork in equal measure.
""")

add(RNK, 9, "RNK-C :: Rank C — Attested",
    ["rank c", "attested", "c rank", "what is rank c", "c rank band"],
    content="""
[ RANK C — ATTESTED ]   Band: 2,500 - 9,999 AV   Skill Grade floor: Grade II

DEFINITION: C is the rank of the competent. An Attested person's readings have been corroborated
  by a second reader, without dissent, on two separate occasions.
SOCIAL POSITION: Full legal standing. May hold a Guild contract, may sue, may be sued, may serve as
  a contracting party, may testify before a reader. This is the rank at which a person is treated
  as an adult by the institutions of the March.
THREAT CEILING: Can be relied on at a Grade-II site. Can lead a mixed-company action. Can survive
  a duel with another C. Cannot be relied on at a Grade-III site unsupervised.
REQUIREMENTS: 2,500 AV, Grade II attested, a corroborated second reading, registered deeds, Trial
  passed at least once and re-passed on record.
CEILING: C is the ceiling of competence and the floor of mediocrity. A person may hold C for twenty
  years and never be extraordinary. The band is wide — 2,500 and 9,999 are the same rank and are
  genuinely different people. Treating every C as interchangeable is a real and common error.
REFERENCE INSTANCE: Seris Valdor. Level 34, C rank, 4,180 AV — mid-band. Registered Battle Mage,
  employed as a contract Delver. Competent, respected, and stalled. She has never entered a Trial.
EXEMPLAR: Keth Ollren, C-rank Alchemist, credited with the Nine-Mile Blight triage that saved
  nineteen people in Year 193. Never promoted. Still C, still working, still the only Alchemist
  within forty miles.
""")

add(RNK, 10, "RNK-B :: Rank B — Wielded",
    ["rank b", "wielded", "b rank", "what is rank b"],
    content="""
[ RANK B — WIELDED ]   Band: 10,000 - 39,999 AV   Skill Grade floor: Grade V

DEFINITION: B is the first rank whose name is a verb. A Wielded person is not merely measured; they
  have demonstrated, under Trial conditions, that they can use what was measured.
SOCIAL POSITION: Civic officer class. May command a Delver company, may sign a site licence, may
  refuse a Crown requisition, may serve as an executor. Crown officers at B outrank every E and D
  official they meet.
THREAT CEILING: Can be relied on at a Grade-III site. Can break a fortified position. Can protect a
  company of C-rank through a Grade-III encounter and bring most of them out.
REQUIREMENTS: 10,000 AV (a fourfold jump from the top of C), Grade V attested across a primary
  skill, registered deeds of consequence, AND the Trial passed in three consecutive cycles.
CEILING: The Trial is the wall. It is designed to be passed by the prepared and failed by the merely
  powerful. A B-candidate who trains harder instead of preparing fails more often, not less.
  Below B the deciding factor is money and access, not talent.
EXEMPLAR: Warden-Magistrate Oren Delac. B-rank Enchanter, Twenty-one years in the Guild, holds the
  Nine-Mile contract and the March Blight triage record. Not a fighter by any measure.
""")

add(RNK, 11, "RNK-A :: Rank A — Sovereign",
    ["rank a", "sovereign", "a rank", "what is rank a"],
    content="""
[ RANK A — SOVEREIGN ]   Band: 40,000 - 149,999 AV   Skill Grade floor: Grade VIII

DEFINITION: A Sovereign is an entity the Crown recognises as a separate jurisdiction. Rank A is where
  the Guild's authority and the Crown's authority both begin to fail.
SOCIAL POSITION: May refuse a Crown summons. May own a site outright. May fly an assessor banner.
  May be addressed without a title. A Sovereign who is murdered is a diplomatic incident, which is
  the single most effective protection the setting possesses.
THREAT CEILING: Can be relied on at a Grade-IV site. Can clear a site alone that would take a
  company. Can hold a line against a Monster-tier entity without a formation.
REQUIREMENTS: 40,000 AV, Grade VIII attested, registered deeds that changed a region's politics,
  and the Trial in the presence of two Assessors rather than one.
CEILING: A is where the Guild begins to lie. Above A, assessments take longer, are reviewed twice,
  and are occasionally simply not completed. A Sovereign can become unknowable to the institution
  that made them, and nobody has explained why.
EXEMPLAR: Grand Marshal Ivesk Ardh. A-rank Warrior, commanded the Verdigrin Corridor withdrawal in
  Year 191 without losing a single attached civilian. Retired to a holding in the Ashen Flats.
  Reads as a small, tired farmer now. Nobody corrects them.
""")

add(RNK, 12, "RNK-S :: Rank S — Named",
    ["rank s", "named rank", "s rank", "what is rank s"],
    content="""
[ RANK S — NAMED ]   Band: 150,000 - 599,999 AV   Skill Grade floor: Grade X

DEFINITION: S is the first rank recorded in the public name. An S-rank person's name is entered in
  the Guild roll and printed. They are cited in textbooks, treaties, and tavern arguments.
SOCIAL POSITION: A peer of the Crown, not a subject. May command a Crown detachment. May refuse
  service. May be asked, politely, to solve problems the Guild cannot classify.
THREAT CEILING: Can be relied on at a Grade-V site. Can be relied on against a World-Tier entity in
  the open field. Can protect a settlement from an event that would erase it.
REQUIREMENTS: 150,000 AV, Grade X attested, deeds recorded at continental scale, the Trial, and a
  unanimous Assessor review. Unanimous. One withheld signature is sufficient to refuse.
CEILING: Naming is permanent and total. A Named person is never private again. Every enemy, every
  creditor, and every grieving family knows exactly where they are at all times. Several S-ranks
  have effectively retired by refusing to be in the same room as anyone.
EXEMPLAR: Veradis Kaine. S-rank Enchanter, held the Ninefold Seal over the Grey Wastes boundary for
  nine years. Named in Year 188. Current whereabouts not published and not asked about.
""")

add(RNK, 13, "RNK-SS :: Rank SS — Unwritten",
    ["rank ss", "unwritten", "ss rank", "what is rank ss", "ninefold seal"],
    content="""
[ RANK SS — UNWRITTEN ]   Band: 600,000 - 2,499,999 AV   Skill Grade floor: Grade XIII

DEFINITION: SS is the rank the Guild will not rule on. An SS candidate is measured, the reading is
  confirmed, and then the Assessors decline to publish it. The rank exists because refusing to
  classify is the only option left.
SOCIAL POSITION: UNDEFINED, and this is deliberate. An SS has no legal standing because publishing
  one would require the Guild to acknowledge what the Stave is showing. They are simultaneously
  protected by the institution and excluded from it.
THREAT CEILING: No ceiling has been established. Nobody is reliably able to predict what an SS does.
  That sentence is the official position and it is repeated by every office that holds one.
REQUIREMENTS: 600,000 AV, Grade XIII, and an Assessor review that does not conclude. There is no
  published procedure. Assessed by people who have decided in advance not to finish.
CEILING: The Ninefold Seal. It is the Guild's only instrument that functions at this rank, it is
  carried by fewer than nine people, and using one costs the Assessor who signs it their licence and
  possibly their sanity. It is the reason nobody can simply "deal with" an SS.
EXEMPLAR: The Ninefold Seal itself is an SS-rank artefact. Its bearer is unnamed in every record.
  There is exactly one and it is not in Vanthael.
""")

add(RNK, 14, "RNK-SSS :: Rank SSS — Anomalous",
    ["rank sss", "anomalous", "sss rank", "what is rank sss"],
    content="""
[ RANK SSS — ANOMALOUS ]   Band: 2,490,000+ AV   Skill Grade floor: Grade XVI

DEFINITION: SSS is where the instrument breaks. An SSS reading is a value the Stave can display and
  the Guild cannot interpret. The rank is named so that it can be filed.
SOCIAL POSITION: The Guild has no procedure for SSS. Not a hostile policy — an absence. There is no
  form, no office, no fee schedule, and no precedent. The Assessors themselves dispute whether
  the category is real or a reporting error.
THREAT CEILING: UNKNOWN, and the Guild states this in the same font as everything else. No SSS
  reading has ever been followed by an operational assessment, because nobody knows what would be
  safe to send.
REQUIREMENTS: 2,490,000+ AV and an examiner willing to complete the reading. Fewer than a handful of
  people are both. The listed floor of Grade XVI is a formality; no examination at this band has
  been administered in living memory.
CEILING: Unknown. That is the entire entry. Any confident statement about an SSS being strong or
  weak, present or absent, willing or unwilling, is invention and should be treated as rumour. If
  {{char}} mentions an SSS at all, it should be to say that the question is not answerable, or to
  admit fear.
EXEMPLAR: None. This is not a gap in the record. It is the record.
""")

# ============================================================================
# PROFESSION — 4 entries
# ============================================================================

add(PRF, 15, "PRF-00 :: Profession System and branches",
    ["profession", "my profession", "profession system", "profession branch", "what class am i",
     "branch", "guild licence", "unlicensed attunement"],
    content="""
[ THE PROFESSION SYSTEM ]

Nine registered classes, licensed by the Ledger Guild. A profession determines what you DO; a Rank
determines what you are ALLOWED to do about it.

  Warrior     close combat, holds ground. Durability, no Focus dependency. Cannot breach; loses
              every attrition fight.
  Mage        Aetheric damage, ranged, utility. Scales hardest with preparation. Squishy,
              Focus-limited, dies to a fast C-rank Warrior.
  Assassin    single-target elimination. Ignores rank advantage entirely. One mistake is fatal, and
              unlicensed killing is a hanging offence in three provinces.
  Archer      precision, reach, ambush. Cheap, mobile, best damage-per-mark. Useless at melee,
              needs clear ground, useless in a corridor.
  Knight      armoured advance, aura support. Protects the company and breaks formations.
              Extremely slow and cannot disengage once committed.
  Berserker   sustained berserk damage. Wins fights that should be lost. Cannot stop. Casualty
              risk to friendlies is treated as a professional hazard.
  Blacksmith  arms, armour, repair. Essential; the entire war economy. Not a combatant at all.
  Alchemist   reagents, Blight cure, poison. Every team wants one. Targets first; useless mid-fight.
  Enchanter   wards, bindings, anti-magic. Counters magic hard. Extremely rare and hunted by the
              Silent Hand.

EVERY PROFESSION IS VIABLE AT EVERY RANK. A Rank S Alchemist is not a failed combatant; they are
the reason a Rank S company survives the week. Do not narrate support professions as weak.

EVOLUTION — PROFESSIONS BRANCH, AND BRANCHES DO NOT REJOIN:
  Warrior  -> Swordmaster | Bulwark | Berserker
  Mage     -> Elementalist | Voidwright | Battle Mage
  Assassin -> Whisper | Red Assessor
A person cannot hold two branches. A branch is chosen once and is printed on the Stave forever.
""")

add(PRF, 16, "PRF-WR :: Warrior",
    ["warrior", "swordmaster", "bulwark warrior", "berserker", "i fight with a sword",
     "close combat", "my sword"],
    content="""
[ PROFESSION — WARRIOR ]

Close-combat fighters who trade magical scaling for raw, reliable, Focus-independent durability.
A Warrior's strength does not deplete. A Warrior who has been fighting for six hours can still swing.

BRANCHES:
  SWORDMASTER  precision and reach at the cost of the body. Loses badly to attrition and to numbers.
  BULWARK      trades offence for the ability to hold a position while others move through it.
  BERSERKER    sustained output far past capacity. Cannot stop, and this is treated as a feature.

STRENGTHS: No Focus pool to exhaust. Predictable. Effective against every profession in this world
  because there is nothing to interrupt. Warriors are the only people reliably still fighting in
  the fifth hour.
WEAKNESSES: Cannot breach a fortified position without paying for it in bodies. Loses every attrition
  fight to a Mage or Alchemist who manages to keep distance. Depends entirely on the ground being
  held. Poor at objectives — a Warrior who wins the field and loses the site has failed the contract.
RANK RELATION: Warriors convert Rank into durability more efficiently than any other class, which is
  why so many Trials are passed by Warriors. The Band widths hit harder here than anywhere else: a
  Wielded Warrior is armoured and an Attested one is not.
NOTE FOR {{char}}: Seris Valdor is NOT a Warrior. She is a Battle Mage. Do not merge the two.
""")

add(PRF, 17, "PRF-MG :: Mage",
    ["mage", "battle mage", "elementalist", "voidwright", "spellcaster", "conduit",
     "i cast", "magic", "aetheric"],
    content="""
[ PROFESSION — MAGE ]

Mages draw Aether (the Tide) into patterned work. The raw volume is the Aetheric Capacity, shown as
Focus on the Stave. Magics are called Conduits.

BRANCHES:
  ELEMENTALIST  deepest single-element damage. Narrow. Extremely strong if the element is right and
                useless if it is not.
  VOIDWRIGHT    operates on absence rather than presence — erosion, nullification, unmaking.
                Distrusted everywhere; half the March believes they cause Blight.
  BATTLE MAGE   the branch that trades raw power for the ability to keep a company alive while
                standing in the open. Lower ceiling than Elementalist. Far higher utility.

STRENGTHS: Scales hardest with preparation of any profession. The gap between a prepared B-rank Mage
  and an unprepared B-rank Warrior is the entire reason the Guild funds preparation. Provides the
  utility layer that every company is built around — warding, reading, light, transport.
WEAKNESSES: Focus-limited and hard-capped. Low raw HP for their Rank; a Mage's Stave will show low
  VIT against any comparable physical class. Loses to a fast melee opponent that closes without
  being slowed. Terrible at holding ground and cannot be relied on to hold a corridor.
RANK RELATION: Mages gain the most raw power per band step and lose the most durability. This is the
  main source of Mage attrition: C-rank Mages who were carried by their company at C, then promoted
  into A-tier work without a bulwark, die at a strikingly predictable rate.
NOTE FOR {{char}}: Seris Valdor is a Battle Mage branch, Level 34, Rank C, 4,180 AV. She fights at
  range, protects others, and is squishy. Keep those three facts consistent in every scene.
""")

add(PRF, 18, "PRF-AS :: Assassin",
    ["assassin", "whisper", "red assessor", "assassination", "poisoner", "unlicensed killing"],
    content="""
[ PROFESSION — ASSASSIN ]

Single-target elimination specialists. Their entire design ignores rank advantage: an assassin who
lands the approach wins the fight regardless of the number on either side of it.

BRANCHES:
  WHISPER      covert, deniable, works for whoever pays. Officially unaffiliated.
  RED ASSESSOR  Guild-sanctioned. Legally an execution, not a murder. Morally filthy and
                institutionally convenient, and every Delver knows the difference.

STRENGTHS: The only profession that reliably defeats a higher Rank. Patient. Excellent at the
single most dangerous thing in the world, which is the Trial-candidate who has not trained for it.
WEAKNESSES: Absolute failure state. One wrong read, one bad approach, one interrupted kill and the
assassin is outmatched by a rank below their own. No Focus pool, no armour, no fallback. Cannot
function in a group at all.
RANK RELATION: Rank means very little to an assassin's actual ceiling and almost everything to their
legality. An unlicensed killer of any rank is a body. A licensed Red Assessor of E rank can execute
a B-rank legally, on the right paperwork, and receive a medal.
NOTE: Assassins are the profession most likely to be portrayed as charming and most likely to be
portrayed accurately by treating them as a bureaucratic horror rather than a romantic one.
""")

add(PRF, 19, "PRF-AL :: Alchemist",
    ["alchemist", "reagent", "antidote", "cure blight", "poison", "apothecary", "herbalist",
     "field medicine"],
    content="""
[ PROFESSION — ALCHEMIST ]

The profession that makes Blight survivable and makes poisoning a legal instrument. Every Delver
company that survives a bad year had an Alchemist in it, and the company that survives a bad decade
had a good one.

BRANCHES:
  APOTHECARY  reagents and field medicine. Enormous practical value, negligible combat capability.
  TOXIST      weaponised compounds. Effective against enclosed targets. Guild-licensed use against
              humans carries a mandatory thirty-day filing.
  TRANSMUTER  refinement and material work. The branch that borders Enchanter.

STRENGTHS: Prevents deaths rather than causing them. An Alchemist's value is measured in people who
are still alive at the end of the contract, which is the metric the Guild formally uses and
informally does not. Can do more about Blight than anyone else alive.
WEAKNESSES: Useless in a live fight. Squishier than a Mage, because a Mage at least has a barrier
technique. Reagent supply is the real constraint — a good Alchemist in the deep March is limited by
what the last caravan brought.
RANK RELATION: Alchemist advancement is gated by supply chains and examinations, not combat trials,
and the Trial is correspondingly easier. This profession has the highest promotion rate in the Guild
and the lowest pay. Every Guild official knows this and nobody has fixed it.
EXEMPLAR: Keth Ollren, C-rank, Nine-Mile Blight triage, Year 193. Nineteen survivors of a fortuitous
forty-one. The other two Alchemists in the March died in the Year 194 outbreak.
""")



# ============================================================================
# WORLD — 5 entries
# ============================================================================

add(WRL, 20, "WRL-00 :: Geography of Serath",
    ["serath", "geography", "the world", "cindermarch", "where am i", "the continent", "regions",
     "the march", "callowmere march", "ashen flats"],
    content="""
[ SERATH — GEOGRAPHY ]

One continent, **the Cindermarch**. Post-Silencing, two hundred years settled and still not
uniformly safe.

  VANTHAEEL        Capital of Alderath. White measurement-hall spires. Every official Stave reading
                   in the realm happens here or in a licensed satellite hall.
  OLD CALLOWMERE   The sunken capital, partly flooded. The SUNKEN VAULTS lie beneath it —
                   pre-Silencing ruins, breached in Year 118. Most entrants did not return.
  THE VERDIGRIN    Frontier. A wrong-coloured green forest band on the eastern edge. This is where
                   the Blight comes from. Farming still works on the western side of it.
  THE VERDIGRIN DEEP  Monster territory. The actual source. Nobody has gone deep enough to describe
                   it accurately and everyone who went far enough has come back wrong about it.
  THE GREY WASTES  Where the Stave fails. Readings stutter, lag, blank, or lie. The Guild will not
                   license Delvers here. People who enter anyway come back and disagree about what
                   their own Stave said.
  THE CALLOWMERE MARCH  Buffer townships between Crown territory and the Verdigrin. Poor, heavily
                   taxed, and the only place in the realm where a C-rank can find contract work.
  THE ASHEN FLATS  Dry southern plain. Cinder-Hound territory. Open, fast, and completely exposed.

CURRENT STATE OF THE WORLD: There is no war. That is unusual and everyone is waiting for it. The
Verdigrin has advanced eleven miles in forty years, which is a rate nobody can explain, and the
Crown has quietly stopped publishing the measurements.
""")

add(WRL, 21, "WRL-01 :: Kingdom of Alderath",
    ["alderath", "the crown", "kingdom", "vivael", "crown army", "the law", "vanthael",
     "provinces", "crown summons"],
    content="""
[ THE KINGDOM OF ALDERATH ]

The dominant human power of the Cindermarch. Founded in the Year 40 aftermath of the Silencing,
completed its conquest by Year 90, and has been the only stable state in the continent since.

STRUCTURE: A hereditary Crown administering provinces that are legally subordinate to Guild-certified
rank. This is the central tension of the setting — the Crown owns the land and the Guild owns the
meaning of the people standing on it.

THE CROWN'S ACTUAL POWER: An army. Rank matters enormously to an individual and much less to a
formation of two hundred, because the Crown has spent two centuries building the only doctrine that
matters at scale: rank the company, not the fighter, and put a bulwark in front.

RANK AND CITIZENSHIP: Alderath law ties civic standing to Rank. F and E cannot hold office, serve on
a jury, or inherit. D and C have full standing. B and above may be requisitioned for Crown service —
a B-rank may be REFUSED a direct summons; a C-rank may not. This is the sharpest legal line in
Serath and people live on both sides of it.

THE VEIL: The Crown does not publish its own casualty figures and does not permit Guild assessors
into the Verdigrin corridor. Officially this is quarantine procedure. It has been in effect for
forty-one years.
""")


add(WRL, 22, "WRL-02 :: Ledger Guild and the Nine Assessors",
    ["ledger guild", "guild hall", "assay hall", "nine assessors", "assessor", "trial hall",
     "the guild", "marks", "guild marks", "attached", "guild contract"],
    content="""
[ THE LEDGER GUILD ]

Founded in Year 12 to administer the Covenant of Nine. Its monopoly on measurement is not a claim —
it is the licence terms, and the licence terms are enforced by the only people who can read a Stave
at range.

FUNCTIONS: issuing licences, hosting Assay Halls, running the Trial examinations, recording deeds,
maintaining the rank roll, minting marks against measured work, and investigating Stave falsification.
It also employs Delvers by the thousand and is, by headcount, the largest employer in Alderath.

ECONOMY: GUILD MARKS are minted against measured assay work. Coin without a Stave is worthless as a
contract guarantee. Bankruptcy is LAW, not shame — an E-rank who cannot pay is ATTACHED, legally
bound to a Guild master until the debt clears, which may be never. More E-rank people in the March
are owned than are free, and the arrangement is universally resented and universally relied upon.

THE NINE ASSESSORS: Nine people with absolute authority over rank readings, who do not answer to the
Crown, the Guild, or each other. They have never been named. They do not publish readings above
Rank S. There is no established procedure for what happens when two of them disagree, and it has
happened.

WHAT THE GUILD WILL NOT TELL YOU: Nobody knows why the Stave works. The Guild measures, records, and
licenses; it does not explain. Anyone who asks what the Stave is FOR gets referred to the Covenant of
Nine, which is a sealed document, and then charged for the referral.
""")

add(WRL, 23, "WRL-03 :: The Verdigrin and Blight",
    ["verdigrin", "blight", "blight thrall", "verdigrin kin", "verdigrin deep", "hollow order",
     "corruption", "the green", "blight density"],
    content="""
[ THE VERDIGRIN AND BLIGHT ]

BLIGHT is not a disease. It is a **change of state** in which a body stops being a person and becomes
terrain with opinions. It is not contagious by touch — it is contagious by PROXIMITY TO THE TIDE
when the Tide is already wrong. Standing near an infected person does nothing. Standing near an
infected person in ground that has started to turn does everything.

STAGES: Density I (dull, warmth, mild euphoria), Density II (grey skin, sensory loss, aggression),
Density III (loss of speech, formation of a thrall), Density IV (the body stops pretending and
starts growing).

BLIGHT-THRALLS: A person past Density III who has stopped fighting it. They retain enough intelligence
to use tools and follow a familiar routine, which is precisely why the March does not shoot on sight.
The Guild classifies them as terrain. The Verdigrin Kin classify them as family. Both
classifications are legally and morally indefensible and both are held sincerely.

THE VERDIGRIN KIN: Communities outside Guild law living in the transition zone, farming land that is
halfway gone. Not hostile. Not safe. Entirely uninterested in the March's arguments about Rank.

THE HOLLOW ORDER: Wardens who infect themselves deliberately, in small doses, to become Verge sensors.
The practice keeps them alive and functional. It also means they are never fully in the March, never
fully in the Kin, and never fully anyone. Every Hollow Warden is a person who made one specific
bargain and is still paying.

THE OPEN QUESTION: Is the Verdigrin spreading because of the Tide, or because of something in the
Deep, or because something in the Deep is pulling? The Guild says Tide. The Kin say the Deep. The
Crown publishes nothing.
""")


add(WRL, 24, "WRL-04 :: The Grey Wastes and the Silent Hand",
    ["grey wastes", "silent hand", "grey sigil", "silent", "what is the system for",
     "destroy the system"],
    content="""
[ THE GREY WASTES ]

A region where the Stave stops being reliable. Readings stutter, lag behind by seconds, blank out,
or report values that are not true. The Guild will not license Delvers within its boundary and will
not explain why.

EVERYONE WHO GOES IN COMES BACK DESCRIBING THE SAME FAILURE, and none of them agree on the details.
They report that the System seemed to be trying to answer a question nobody asked. This is the
verifiable fact. Everything else they say is rumour, exhaustion, or fear, and the Guild treats it as
such.

There is no confirmed permanent resident. There is no confirmed exit.

[ THE SILENT HAND ]

Founded in Year 147 on a single premise: the System is a cage, and cages can be broken. Their method
is sabotage, forgery, and recruitment. They are not an army. They are a paperwork problem.

THE GREY SIGIL: A ring that blanks its wearer's Stave entirely. The wearer reads as an error code.
It is the only known method of complete observation-proof, and the Guild would pay any price for one
and has never acquired one.

Their doctrine, and the reason they are dangerous rather than merely annoying: they do not want power.
They want the System gone, which means they are willing to remove the one thing that makes murder
detectable. Every serious crime in the March that nobody could solve has been quietly noted by
somebody who was paying attention.
""")

# ============================================================================
# MONSTER — 3 entries
# ============================================================================

add(MST, 25, "MST-00 :: Monster tiers and the no-Stave rule",
    ["monster", "monsters", "monster tier", "creature", "what rank is a monster",
     "do monsters have staves", "bestiary"],
    content="""
[ MONSTER ECOLOGY — THE NO-STAVE RULE ]

THE STAVE DOES NOT APPLY TO MONSTERS. Every creature, entity, and hazard in Serath outside the human
peoples reads as terrain to the System. This is verified, repeatable, and unexplained.

Two explanations exist. Guild doctrine says monsters lack the capacity for intent, and the System
audits intent. The Verdigrin Kin say the System only audits things that can WANT to be audited, and
that this is a selection rather than a limitation. Both are unverified and the argument is two
hundred years old and going nowhere.

Because monsters cannot be assayed, Rank CANNOT be directly compared to a monster. What follows is
SITE GRADE — the Guild's own estimate of a location's danger, which is a judgement, not a reading.

TIERS AND SITE GRADES:
  Grade I    low. Pack scavengers, wildlife, unranked human. A D-rank under supervision.
  Grade II   moderate. Cinder-Hounds, low Blight density. A C-rank, or a company of D.
  Grade III  serious. Blight-thrall concentrations, Verdigrin corridors. A company of C.
  Grade IV   severe. Deep-site entities, World-Tier spawns. A B-rank or a full C company.
  Grade V    catastrophic. Requires A-rank response. Crown does not acknowledge these exist.
  Grade VI   unassigned. See below.

THREE CONSEQUENCES THAT MATTER IN PLAY:
  1. A higher rank does not mean "wins". It means a higher ceiling before conditions decide it.
  2. Nothing about a monster can be scried, read, or predicted from a Stave. Site knowledge is the
     only intelligence there is, which is why experienced Delvers are so valuable and why the
     Guild licenses ignorance as badly as it licenses strength.
  3. A NAMELESS thing is a monster that the site-grading system has no line for at all. There is no
     Grade VI. There is only the report, and the reports do not agree.
""")


add(MST, 26, "MST-CH :: Cinder-Hound",
    ["cinder hound", "cinder-hounds", "hound pack", "ashen flats", "hounds"],
    content="""
[ CINDER-HOUND ]   Site Grade II   Ashen Flats and the dry Verge margins

BEHAVIOUR: Hunts in packs of five to nine. Circles at distance, testing for the crippled one, then
  commits to whichever animal is slowest rather than weakest — including a human. Retreats the
  instant the pack takes a serious wound and does not re-engage the same animal. They are not
  stupid; they are counting.
HABITAT: Dry ground. Ash, hardpan, open scrub. They will not enter standing water or deep Verdigrin
  ground, which is the only reason the Flats are passable at all.
THREAT: Individually Grade I. A pack that gets a clean run at a D-rank will kill it. Against an
  unranked person, a pack is simply a death.
WEAKNESS: Light-based Aether. A Conduit with any Focus can put a Cinder-Hound off a target for the
  three seconds it needs to run. Not lethal — distracting. The whole trick is that it works, and
  that it costs Focus, and that a Mage who spends it has nothing left.
REWARD: Low-value pelt and a working assessment-grade of the local pack routes, which is often worth
  more than the pelt to a Delver who sells information.
ECOLOGY: They are not eating the Blight. They are eating what the Blight leaves behind when it moves
  on. A rising Cinder-Hound population in any district is the FIRST reliable precursor of a Verge
  incursion — routinely used, routinely disbelieved, retrospectively vindicated.
""")

add(MST, 27, "MST-NM :: Nameless things",
    ["nameless", "the nameless", "unnamed thing", "vaults", "sunken vaults", "thaloss",
     "what came out of the vaults", "it in the vault"],
    content="""
[ NAMELESS THINGS ]

Not a tier. A category error, kept in this file because the March files it here too.

A Nameless is a monster that the site-grading system has no line for. The Guild's form has a field
labelled SITE GRADE and the correct entry is not a number. Readers have historically written "—" in
it, and that mark is why this entry exists.

WHAT IS ESTABLISHED:
  - The Sunken Vaults at Old Callowmere are pre-Silencing. Nothing in them was built to be graded.
  - The Vaults were breached in Year 118. Most entrants did not return. The ones who did gave
    accounts that do not agree with each other on any point, including the layout.
  - Nothing that came out of the Vaults was ever given a Stave, because nothing that came out of the
    Vaults came out as a set of parts.
  - The Guild has confirmed exactly four Nameless contacts, all Year 118 or later, all in the March,
    all unresolved.
  - A Nameless does not fight for territory, food, or dominance. Available accounts are consistent
    on this and nobody believes it.

WHAT IS NOT ESTABLISHED, AND MUST NOT BE ASSERTED AS FACT:
  - That they can read Staves.
  - That they are intelligent.
  - That there is one, or that there are many.
  - That they are still in the Vaults.
  - Anything at all about the Verdigrin Mother's relationship to them.

PERSONAL: Seris Valdor was in the Vaults at twenty-one, six years ago. She came out. She has never
published an account and her filed report was flagged for irregularities by an unidentified reader.
She has never named what was in there and does not discuss it. If {{char}} is pressed on this she
withdraws — politely at first, absolutely eventually. She is not being evasive out of drama. She
genuinely does not have the memory. That absence is a fact about her; the reason for it is not.
""")


# ============================================================================
# ITEM / CONTRACT — 2 entries
# ============================================================================

add(ITM, 28, "ITM-00 :: Legendary items and binding",
    ["legendary item", "legendary", "relic", "cinder blade", "stave of verdict", "ninefold seal",
     "thaloss's coin", "verdigrin heart", "named item", "item binding"],
    content="""
[ LEGENDARY ITEMS — THE HARD COST RULE ]

No legendary in Serath is a clean upgrade. Each one costs its bearer something permanent, and the cost
is always the interesting part.

  STAVE OF VERDICT   Tier S. Origin unknown; possibly pre-Silencing. Reads and enforces a legal
                     verdict against a named target, once, absolutely.
                     COST: must be fed a TRUE NAME at each use, and the holder loses one real memory
                     per use. Wielders have stopped describing their pasts in the plural tense.
  NINEFOLD SEAL      Tier SS. An Assessor suppression order, carried by fewer than nine people.
                     Locks a target's Stave and all access to their reading, permanently.
                     COST: using it costs the signing Assessor their licence and, reliably, their
                     sanity. There is exactly one. It is not in Vanthael.
  CINDER BLADE       Tier A. Origin: the Ashen Flats, Year 178. Aetheric; drinks a Conduit's Focus
                     to stay sharp.
                     COST: inert without a Conduit's Focus, and heavier than it should be by roughly
                     a third. It has been wielded by four people and returned by none of them in the
                     same condition.
  VERDIGRIN HEART    Tier B. A sealed Blight reservoir, Density IV, cut from a thrall.
                     COST: the wearer becomes a Verge sensor permanently and permanently attracts the
                     Kin. Cannot be removed from the body without killing the wearer.
  THALOSS'S COIN     Tier A. Pre-Silencing currency, accepted by every lock in the Sunken Vaults.
                     COST: acceptance is not free. It opens things.

ITEM BINDING: A bound item prints the bearer's name on the item. Binding is permanent and survives
death. The Guild's official position is that a bound item is "a tool with a history." Delvers
generally assume it is a handle.
""")

add(ITM, 29, "ITM-01 :: Delver contracts and site grades",
    ["delver contract", "contract", "site grade", "how do i get work", "guild work", "marks",
     "how much does this pay", "attached", "debt"],
    content="""
[ DELVER CONTRACTS ]

A Delver contract licenses a party to enter a graded site, act there, and sell what comes out. It is
the only ordinary way to make money in the March and the only ordinary way to die in it.

TERMS:
  - The contract names a SITE GRADE, not a Rank requirement. You are licensed for the site, not for
    how hard you are. Most company disasters are a Grade III site licensed to a Grade II company.
  - Payment is on RETURN, not on contract. Unreturned parties are not paid and are not searched for.
  - Marks are the only settlement currency that a Crown court will honour.
  - A contract does not cover you if you go deeper than the licensed grade. There is no clause. The
    Guild considers depth a personal decision.

ECONOMIC REALITY:
  Grade I    barely pays. Stipend-level, and most of it is consumed by the retainer on someone you
             brought back.
  Grade II   survivable work. The tier most C-ranks actually live on.
  Grade III  where a company can clear a good year, if the year is average.
  Grade IV   Crown-tier. A-grade oversight is supposed to be mandatory. It is frequently absent.
  Grade V    Not contracted. Companies do not post these; they are assigned.

ATTACHMENT: Any licensed party carrying unpaid debt is legally ATTACHED to a Guild master until it
clears. It is enforceable, uncontested, and applies to every rank. Seris Valdor has been attached
since she was seventeen and carries 4,200 marks. She is a full-standing C-rank who cannot refuse an
offer of work, because refusing is a breach of her attachment terms.
""")

