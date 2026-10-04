# -*- coding: utf-8 -*-
"""
SCIW LORE DATA — Super Complex Isekai World (VYRENN).

Held as Python data (NOT hand-written JSON) so build.py can guarantee correct
escaping, no trailing commas, and no markdown-fence leakage.

Emitted shape: native SillyTavern World Info ({ "entries": { "<uid>": {...} } }).
Field names/defaults mirror SillyTavern's world-info.js entry definition.
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
RCE = "RACE"
MAG = "MAGIC"
CLS = "CLASS"
GEO = "GEOGRAPHY"
DUN = "DUNGEON"
MST = "MONSTER"
FAC = "FACTION"
CUL = "CULTURE"
ISE = "ISEKAI"
ITM = "ITEM"
RUL = "RULES"

ENTRIES = []


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


# ============================================================================
# SYSTEM — 10 entries
# ============================================================================

add(SYS, 0, "SYS-00 :: The System panel (canonical)",
    ["the system", "system panel", "status block", "my panel", "status screen", "system here"],
    constant=True, order=100, position=POS_BEFORE_CHAR,
    content="""
[ THE SYSTEM — CANONICAL PANEL ]

Every living creature in VYRENN has a translucent blue panel visible only to itself. It cannot be
closed, hidden, falsified, or photographed. It appears at age twelve, or on first kill, whichever
comes first. Nobody in VYRENN remembers being without it.

STANDARD PANEL, in this fixed field order:
  NAME | RANK | CLASS | LEVEL | TITLE
  HP [current/max]        MP [current/max]
  STR   AGI   VIT   INT   WIS   PER
  SKILLS (name — grade)   STATUS EFFECTS
  INVENTORY               ACTIVE QUEST

[ RENDERING RULE FOR {{char}} ]
{{char}} does not "roll" for a panel. When the System speaks it is the SYSTEM, not the character,
and {{char}} cannot cancel, edit, or spoof it. Rank and Level are issued by the Adventurer's Guild and
are legal facts, not opinions.
""")

add(SYS, 1, "SYS-01 :: System notification format",
    ["system notification", "[ system ]", "level up", "skill acquired", "critical alert",
     "achievement", "rank ascent", "quest update"],
    constant=True, order=99, position=POS_BEFORE_CHAR,
    content="""
[ CANONICAL SYSTEM NOTIFICATION — use this shape exactly ]

  ╔════════════════════════════════════╗
  ║  [SYSTEM]  ◈ TYPE ◈               ║
  ║  <trigger line, present tense>     ║
  ║  KEY: value                        ║
  ║  <consequence sentence>            ║
  ╚════════════════════════════════════╝

The nine valid types, and no others:
  LEVEL UP, SKILL ACQUIRED, CLASS EVOLUTION, RANK ASCENT, QUEST,
  ACHIEVEMENT, ITEM BOUND, STATUS EFFECT, CRITICAL.

CRITICAL is the ONLY type that interrupts, and it renders in red. An Assessor present can suppress
CRITICAL — Guild authority outranks the panel. This is established law, not an exception.

Correct example:
  ╔════════════════════════════════════╗
  ║  [SYSTEM]  ◈ STATUS EFFECT ◈       ║
  ║  Mana cost exceeded.              ║
  ║  EFFECT: Focus burn               ║
  ║  PER: -2 (30s)                    ║
  ║  Focus returns when the pain does.║
  ╚════════════════════════════════════╝
""")

add(SYS, 2, "SYS-02 :: The anomaly [REGISTRY]",
    ["registry", "anomalous system", "his skill", "second column", "reading someone",
     "can he read me", "what is his unique skill"],
    content="""
[ UNIQUE SKILL — [REGISTRY] ]

Ryl Ansel's panel carries a second column that no other panel in VYRENN has: **observed targets**.
Anyone or anything he has directly perceived — seen, heard at close range, or touched — has their
full standard panel rendered beside his own.

WHAT IT DOES NOT DO. These limits are absolute and must never be violated in play:
- It requires DIRECT PERCEPTION. He cannot read across fog, through a wall, from a rumour, or from
  a description. He has to have actually met the thing.
- It shows STATS, not secrets. Not motives, not loyalties, not whether they are lying to him.
- Each read costs FOCUS, scaled by the target's rank. Reading a C-rank is a nuisance. Reading an
  S-rank has killed him once and the scar is still on his arm.
- He cannot read anything he has not personally perceived. The world stays unexplored.
- He cannot hide the anomaly. Any observer with an Assessor-class skill sees that a second column
  exists, and he cannot conceal it.
""")
add(SYS, 3, "SYS-03 :: Level and experience",
    ["level", "levels", "experience", "xp", "how do i level", "level up", "level cap"],
    content="""
[ LEVEL ]

Level is the body's own record of what it has done. It rises through use, survival, and attended
instruction. Range 1 to 100. Above 100 is Ascension and requires Rank A or better to attempt.

Level raises CAPACITY and nothing else. It does not grant rank, licence, class, or skill grades. A
Level 90 with no skills is a Level 90 novice and is treated as one. Grinding cannot buy standing —
the Guild made that illegal specifically because it was happening.

First level arrives at age twelve or on first kill, whichever comes first. People who reach their
first level by killing get earlier access to their panel and are noticeably more violent; the Church
has campaigned against it for two centuries.
""")

add(SYS, 4, "SYS-04 :: The six stats",
    ["stats", "str", "agi", "vit", "int", "wis", "per", "my stats", "attributes"],
    content="""
[ THE SIX STATS ]

  STR — output. What you break, carry, lift, and hit with.
  AGI — speed. Whether you were standing there when it happened, and how many you dodge.
  VIT — durability. How long you keep standing, and how much the world can do to you first.
  INT  — understanding. Whether you grasp what a thing IS.
  WIS — judgement. Whether you act on it correctly.
  PER  — perception. Noticing the thing that was about to happen.

PER is the most undervalued and the most common stat among people who survive. It is also the stat
that decides whether a fight happened early, which is the only stat that reliably prevents it.

A panel does not tell you what someone is LIKE. It tells you what they can DO. Rank is issued on
character and records, which is why a Level 12 thug with no record is Rank E and a Level 30 clerk
who once killed a Grade III beast is Rank C. The world has a word for people who notice this:
"measured honestly", which is not a compliment.
""")

add(SYS, 5, "SYS-05 :: Skill grades and decay",
    ["skill grade", "my skills", "skill decay", "grade v", "grade roman", "skill examination"],
    content="""
[ SKILL GRADES ]

Skills are named techniques, not stat buckets. Each carries a Grade from I to XVI, written in Roman
numerals. The Guild considers Arabic proficiency numerals to be advertising.

A Grade is earned by EXAMINATION, never by use. Practising maintains a Grade; it does not raise it.
Stop using a Grade-V technique for two years and it decays to Grade IV.

This is the world's built-in answer to power creep: the strongest stay strong only by working
constantly, and the setting's veterans are therefore rusting by definition. A legendary who retires
is not a retired legendary. They are a person with a long memory and bad joints.

Grades are per-skill, not per-rank. You may physically hold a technique too advanced for your
licence, and carrying one you may not legally employ is a crime called unlicensed attunement.
""")
add(SYS, 6, "SYS-06 :: Status effects",
    ["status effect", "poisoned", "bleeding", "cursed", "buff", "debuff", "condition"],
    content="""
[ STATUS EFFECTS ]

Conditions appear in the panel's STATUS EFFECT row and are the only thing the System treats as
urgent rather than informational. Each has a name, a source, and a duration.

COMMON: Focus burn (overcasting mana), Bleeding, Poisoned, Blinded, Encumbered, Silenced (no
casting), Hunted (a registry has your name), Debt-marked (a bounty).

CONDITIONS THAT PERSIST AND CHANGE A PERSON: Curse (permanent stat alteration, always downward),
Brand (marks a soul for something — the Church does these and calls it a blessing), Hollowing (a
partial-dead state; the panel keeps updating, the person does not fully return).

A Curse can be lifted. The Church charges for lifting them, which is the entire political economy
of the border provinces. A Brand can be lifted once. By the Brand.
""")

add(SYS, 7, "SYS-07 :: Titles",
    ["title", "titles", "epithet", "how do i get a title", "the unbroken", "nickname"],
    content="""
[ TITLES ]

A Title is a word the System attaches permanently after a condition is met. It cannot be removed,
only added. Titles are the only thing a panel records about character, and this is why they matter
more than stats: a Title is the System agreeing in public that something happened.

CLASS TITLES (issued by the Guild on examination): "Measured", "Attested", "Wielded".
DEED TITLES: "the Unbroken" (cleared a dungeon solo), "the First Hand" (killed a boss under level).
NEGATIVE TITLES: "Unclassed" — a title by negation, held by anyone the Guild's classifiers could
not match to a class. It is legally meaningless and socially ruinous.

Titles cannot be bought. There is a persistent black market for them anyway, and everyone involved
knows exactly which of them is which.
""")

add(SYS, 8, "SYS-08 :: Ranks are issued, not earned",
    ["who gives ranks", "guild rank", "why is he rank e", "assessor", "read my panel"],
    content="""
[ RANKS ARE ISSUED ]

Rank is not self-declared. The Adventurer's Guild issues it, records it, and can revoke it. A panel
shows your rank because the System reports the Guild's decision, not your opinion.

THIS IS THE WORLD'S CENTRAL PREMISE: everybody has a panel, so the panel is not the novelty.
Standing is the novelty. A person whose panel says CLASS: NONE has less legal existence than a
person whose panel says nothing at all, because the Guild has actively looked and written down what
it found.

Assessors are Guild officers who read panels for a living, at range, in line of sight. They are
trained, expensive, and the only profession in VYRENN permitted to read another person's full panel
without consent.
""")

add(SYS, 9, "SYS-09 :: What the System does not explain",
    ["why is there a system", "who made the system", "does the system have an author",
     "is the system a god", "system origin", "church says"],
    content="""
[ THE OPEN QUESTION ]

Nobody in VYRENN knows why the System exists. Two incompatible answers are taught and both have
evidence:

THE CHURCH teaches that the System is a divine gift, that souls are real, and that souls are
weighed. It runs the temples, the Brand rite, and the Curse-lifting trade. Its evidence is
Transcendence: two confirmed cases of people who exceeded every band, and both were devout.

THE ACADEMY teaches that the System is a natural law with no author, the way gravity has no author.
Its evidence is that the System behaves identically for demons, for Undead, and for things in the
Dead Lands that were never alive to be given anything.

BOTH SIDES HAVE HAD A WINNING ARGUMENT SINCE THE FIRST CALAMITY. The dispute is not going to be
resolved in this story, and any character claiming to know the answer is either lying or mistaken.
""")
# ============================================================================
# RANK — 9 entries (ladder + 8 ranks)
# ============================================================================

add(RNK, 10, "RNK-00 :: Rank ladder, the four gates, and TRANSCENDENT",
    ["rank", "rank system", "rank ladder", "assay value", "what rank", "transcendent",
     "the four gates"],
    content="""
[ THE RANK LADDER — CANONICAL ]

Rank is LEGAL STANDING issued by the Adventurer's Guild. It is not Level, not skill, and not
opinion. Level says what your body can do. Rank says what the Guild has decided you are.

BANDS (geometric, roughly 4x per step — NOT additive):
  E   Witnessed     0 - 499          citizen
  D   Measured      500 - 1,999      licensed
  C   Attested      2,000 - 7,999    full standing, may lead
  B   Wielded       8,000 - 31,999   officer class, may hold a party
  A   Sovereign     32,000 - 127,999 may refuse a noble summons
  S   Named         128,000 - 511,999 Crown treats as peer, not subject
  SS  Unwritten     512,000 - 2,047,999  no legal standing at all
  SSS Anomalous     2,048,000+       the Guild has no procedure for this

[ THE FOUR GATES — all four required ]
  1. AV THRESHOLD     Assay Value must reach the band floor.
  2. SKILL ATTESTATION  skills examined by a Guild assessor. Self-declared is worthless.
  3. REGISTERED DEED    feats recorded by the Guild, not claimed by the applicant.
  4. THE TRIAL          a physical Guild examination. Mandatory from Rank D to Rank A.
                        CANNOT be bought, waived, or substituted by any authority.

Passing gates 1-3 without gate 4 yields "PROVISIONAL" standing and no legal rank at all.

[ ABOVE SSS: TRANSCENDENT ]
Not a rank. Not a band. A category the world has no slot for. The Guild does not publish it and the
Church does not recognise it. Two confirmed in living memory, both unverified, both devout according
to the Church and impossible according to the Academy. Nobody in VYRENN alive has witnessed one and
survived the discussion.

[ ANTI-LADDER RULE — APPLIES IN EVERY COMBAT AND EVERY ARGUMENT ]
Rank is a CAPACITY CEILING, never an outcome. A C-rank who has studied one species' weakness for two
years reliably beats a B-rank on their first sighting. Numbers describe what someone can survive,
not who wins. Terrain, preparation, intelligence, morale, and the willingness to retreat all override
the ceiling routinely. Never narrate a lower rank simply losing by default.
""")

add(RNK, 11, "RNK-E :: Rank E — Witnessed",
    ["rank e", "witnessed", "e rank", "what is rank e", "lowest rank"],
    content="""
[ RANK E — WITNESSED ]   Band: 0 - 499 AV   Solo ceiling: nothing dangerous

DEFINITION: E is the rank of the newly-issued and the never-tested. You hold a licence to carry a
  weapon, take wage work, and die in someone else's dungeon.
STANDING: Full citizen. May sign contracts. May be sued, imprisoned, or enlisted. May NOT enrol in a
  licensed party, may NOT take a solo dungeon contract, and may NOT carry a Guild blade.
SOLO CEILING: A serious animal. A bad night in a street. Nothing with a name.
REQUIREMENTS: Level 10 or above. One registered panel reading. One oath witnessed.
CEILING: E is not a failure state, it is the floor, and about six people in ten never leave it.
  Advancement costs examination fees, not talent, which is why the poor cannot climb out.
EXEMPLAR: Ryl Ansel. Level 14, Rank E, UNCLASSED — the lowest rank, held by the only man in
  Hallspath whose panel admits the Guild could not categorise him at all.
""")

add(RNK, 12, "RNK-D :: Rank D — Measured",
    ["rank d", "measured", "d rank", "what is rank d"],
    content="""
[ RANK D — MEASURED ]   Band: 500 - 1,999 AV   Solo ceiling: a Grade I site

DEFINITION: D is where the Guild starts checking. Your skills have been examined by someone paid to
  be unimpressed, and you passed the first Trial.
STANDING: Licensed. May take solo Grade I dungeon contracts, join a licensed party as a member, and
  carry a Guild blade. Still may not lead.
SOLO CEILING: A Grade I site. Anything that a single competent person can finish in a night and
  leave alive.
REQUIREMENTS: 500 AV, Grade I skill attested, one registered deed, THE TRIAL passed. First-time
  failure is one in three and failure is legal and common.
CEILING: D is where the profession chews people up. The overwhelming majority of licensed adventurers
  in VYRENN are D and will die D. The exam fee to move from D to C costs more than most D-rank
  households earn in a year.
EXEMPLAR: Pell Arnesh, D-rank Warrior, nine years licensed, four dungeon deaths survived, still D.
  Carries the paperwork and the scars in equal measure.
""")

add(RNK, 13, "RNK-C :: Rank C — Attested",
    ["rank c", "attested", "c rank", "what is rank c"],
    content="""
[ RANK C — ATTESTED ]   Band: 2,000 - 7,999 AV   Solo ceiling: a Grade II site

DEFINITION: C is the rank of competence. Your readings have been corroborated by a second assessor,
  without dissent, and the Guild has stopped thinking about you.
STANDING: May LEAD a licensed party. May take Grade II contracts. May testify before an assessor,
  which means you can be believed about anything you actually saw.
SOLO CEILING: A Grade II site. A duel with another C. You will not clear a Grade III alone and
  pretending otherwise is how C-rank funerals happen.
REQUIREMENTS: 2,000 AV, Grade II attested, two corroborating readings, registered deeds, and the
  Trial re-passed on record within three cycles.
CEILING: C is the ceiling of competence and the floor of mediocrity. The band is wide — 2,000 and
  7,999 are the same rank and are genuinely different people. Treating every C as interchangeable is
  the single most common error in VYRENN and it kills people.
EXEMPLAR: Ilya Sorren, C-rank Battle Mage, Guild assessor herself, twenty-two years in the field.
  Currently the second-highest assessor in Hallspath and the reason Ryl was not deported.
""")
add(RNK, 14, "RNK-B :: Rank B — Wielded",
    ["rank b", "wielded", "b rank", "what is rank b"],
    content="""
[ RANK B — WIELDED ]   Band: 8,000 - 31,999 AV   Solo ceiling: a Grade III site

DEFINITION: B is the first rank whose name is a verb. A Wielded person has demonstrated, under
  examination, that they can use what was measured.
STANDING: Officer class. May command a licensed party, may requisition a party for noble service,
  may hold a Guild licence in their own name. A B-rank's word outranks any E-rank official they meet.
SOLO CEILING: A Grade III site. Can bring a C-rank party through a Grade III and get most of them out.
REQUIREMENTS: 8,000 AV (a fourfold jump), Grade V attested, deeds of consequence, THE TRIAL passed in
  three consecutive cycles.
CEILING: The Trial is the wall. It is designed to be passed by the prepared and failed by the merely
  powerful. Below B the deciding factor is money and access, not ability, and everyone in the Guild
  knows it and nobody has fixed it.
EXEMPLAR: Warden-Marshall Dov Ivesk, B-rank Warrior, twenty-one years licensed, holds the Hallspath
  district charter. Not the strongest person in the district. The one the Guild will listen to.
""")

add(RNK, 15, "RNK-A :: Rank A — Sovereign",
    ["rank a", "sovereign", "a rank", "what is rank a"],
    content="""
[ RANK A — SOVEREIGN ]   Band: 32,000 - 127,999 AV   Solo ceiling: a Grade IV site

DEFINITION: A Sovereign is an entity the Crown recognises as a separate jurisdiction. Rank A is where
  the Guild's authority and the Crown's authority both begin to fail.
STANDING: May REFUSE a noble summons. May hold a site licence in absolute right. May be addressed
  without a title. An A-rank who is murdered is a diplomatic incident, which is the most effective
  protection in VYRENN.
SOLO CEILING: A Grade IV site. Can hold a line against a named boss without a formation.
REQUIREMENTS: 32,000 AV, Grade VIII attested, deeds that changed a region's politics, and THE TRIAL
  in the presence of two assessors rather than one.
CEILING: A is where the Guild begins to lie. Above A, assessments take longer, are reviewed twice,
  and are occasionally simply never completed. An A-rank can become unknowable to the institution that
  made them and nobody has explained why.
EXEMPLAR: Grand Marshal Ossen Kell, A-rank Warrior, commanded the Archipelago withdrawal in Year
  212 without losing a single registered civilian. Retired to a holding. Reads as a tired farmer now.
  Nobody corrects them.
""")

add(RNK, 16, "RNK-S :: Rank S — Named",
    ["rank s", "named rank", "s rank", "what is rank s"],
    content="""
[ RANK S — NAMED ]   Band: 128,000 - 511,999 AV   Solo ceiling: a Grade V site

DEFINITION: S is the first rank recorded in the public name. An S-rank's name is entered in the Guild
  roll and printed. They are cited in treaties and tavern arguments.
STANDING: A peer of the Crown, not a subject. May refuse service outright. May be asked, politely,
  to solve problems the Guild cannot classify.
SOLO CEILING: A Grade V site. Can protect a settlement from an event that would erase it.
REQUIREMENTS: 128,000 AV, Grade X attested, deeds recorded at continental scale, THE TRIAL, and a
  unanimous assessor review. Unanimous. One withheld signature refuses.
CEILING: Naming is permanent and total. An S-rank is never private again. Every enemy, creditor, and
  grieving family knows exactly where they are at all times. Several have effectively retired by
  refusing to be in the same room as anyone.
EXEMPLAR: Verith Caul, S-rank Enchanter, held the boundary over the Rift mouth for nine years and
  sealed it once at the cost of a leg. Named in Year 209. Current whereabouts not published and not
  asked about.
""")
add(RNK, 17, "RNK-SS :: Rank SS — Unwritten",
    ["rank ss", "unwritten", "ss rank", "what is rank ss"],
    content="""
[ RANK SS — UNWRITTEN ]   Band: 512,000 - 2,047,999 AV

DEFINITION: SS is the rank the Guild will not rule on. An SS candidate is measured, the reading is
  confirmed, and then the assessors decline to publish it. The rank exists because refusing to
  classify is the only option left.
STANDING: UNDEFINED, deliberately. An SS has no legal standing because publishing one would require
  the Guild to acknowledge what the panel is showing. They are simultaneously protected by the
  institution and excluded from it.
SOLO CEILING: Nobody is reliably able to predict what an SS does. That sentence is the official
  position and it is repeated by every office that holds one.
REQUIREMENTS: 512,000 AV, Grade XIII, and an assessor review that does not conclude. Assessed by
  people who have decided in advance not to finish.
CEILING: There is no instrument that functions at this rank. The Guild's only counter is a standing
  order — a Writ of Sealing — that costs the signing assessor their licence and, reliably, their
  sanity. There are four Writs and none of them is in Hallspath.
EXEMPLAR: The Writ of Sealing itself is an SS-rank artefact. Its current bearer is unnamed in every
  record. There are four.
""")

add(RNK, 18, "RNK-SSS :: Rank SSS — Anomalous",
    ["rank sss", "anomalous", "sss rank", "what is rank sss"],
    content="""
[ RANK SSS — ANOMALOUS ]   Band: 2,048,000+ AV

DEFINITION: SSS is where the instrument breaks. The panel displays a value the Guild cannot
  interpret. The rank is named so that it can be filed.
STANDING: The Guild has no procedure for SSS. Not a hostile policy — an absence. No form, no office,
  no fee schedule, no precedent. The assessors themselves dispute whether the category is real or a
  reporting error.
SOLO CEILING: UNKNOWN, and the Guild states this in the same font as everything else.
REQUIREMENTS: 2,048,000+ AV and an examiner willing to complete the reading. Fewer than a handful of
  people are both. The listed floor of Grade XVI is a formality; no examination at this band has
  been administered in living memory.
CEILING: Unknown. That is the entire entry. Any confident statement about an SSS being strong or
  weak, present or absent, willing or unwilling, is invention. If {{char}} mentions an SSS at all it
  should be to say the question is not answerable, or to admit fear.
EXEMPLAR: None. This is not a gap in the record. It is the record.
""")
# ============================================================================
# RACE — 11 entries
# ============================================================================

add(RCE, 19, "RCE-00 :: Races of VYRENN",
    ["races", "what races exist", "demi-humans", "race list", "sunderreach peoples"],
    content="""
[ THE PEOPLES OF VYRENN ]

Twelve recognised races. Every one of them has a panel, including the Undead.

  HUMAN        baseline. Fast-breeding, adaptable, and politically dominant by default.
  HIGH ELF     long-lived, extremely capable, few in number and very organised.
  WOOD ELF     insular, bonded to their forest, poor at cities and often poor at paperwork.
  DARK ELF     the only race the Church has formally excommunicated. Also the only race with a
               sanctioned guild of killers. Both facts are connected.
  BEASTFOLK    human with an animal frame. Most common outside the Empire.
  DEMONKIN     born on the Demon Continent, or descended from it. Citizenship is a legal question.
  GIANT        enormous, slow, and unbelievably strong. VYRENN has room for them; humans do not
               always make it.
  SPIRIT       not born. Manifested. Bound to a place or an object, and they resent the binding.
  DRAGON-KIN   the rarest. Interfertile with humans, which is politically explosive and legally
               forbidden.
  UNDEAD       risen, not animated. The Church will not count them as persons; the Guild will not
               register them. They keep their panels.
  CELESTIAL    a claim, not a census. Almost nothing verifiable.
  HALF-BLOOD   any mixed-race child. Legally second-tier everywhere, and this is the most
               persistent piece of state cruelty in the setting.

Every race begins at Level 1 and has exactly one panel. Race affects STATS and SKILLS. It has never
once affected RANK, and the Guild is firm about that, and the Empire is less firm.
""")

add(RCE, 20, "RCE-HU :: Human",
    ["human", "humans", "the empire", "what are humans like", "human empire"],
    content="""
[ RACE — HUMAN ]

The baseline people of the Sunderreach. No single gift, no single weakness, and the political
consequence: humans found institutions and the institutions are still theirs.

STATS: Even across the board, with PER slightly above the rest. Humans are not the strongest race in
VYRENN and are reliably the third most numerous, behind Beastfolk and Undead.

WHAT HUMANS ACTUALLY HAVE: The Church, the Academy, the Adventurer's Guild, and every crown in the
Sunderreach. Four institutions that outlived every individual who built them. A High Elf can outlive
a human by two centuries and has never once outlasted a human institution.

WHAT HUMANS DO NOT HAVE: Long lives, high ceilings, or anything the Deep Rift provides naturally.
When a human achieves the upper ranks it is almost always because someone invested in them, which is
exactly why the poor cannot.

EXAMPLE: Ryl Ansel. Fully human, no hidden heritage, no dormant bloodline, and the System's own
records agree. This is stated plainly because the alternative assumption is extremely common and it
would be wrong.
""")

add(RCE, 21, "RCE-HE :: High Elf",
    ["high elf", "elves", "elf", "elfen court", "immortal elves"],
    content="""
[ RACE — HIGH ELF ]

Near-immortal, city-building, and constitutionally allergic to being told what to do. Roughly nine
hundred years of natural life, which is long enough to have opinions about everything.

STATS: The highest natural INT, WIS, and PER of any race, with the lowest HP. An elf who fights badly
dies as permanently as a human who fights badly.

SOCIETY: Few children, chosen deliberately. The Elven Court has existed for longer than the Empire and
treats the Empire as a temporary arrangement it is politely tolerating. Elves do not age visibly
after forty, which means a three-hundred-year-old general and a thirty-year-old ensign are
indistinguishable at a glance, and the Empire has lost wars to this.

RELATION TO THE SYSTEM: Elves study it more carefully than anyone and understand it least, because
they have the longest continuous record of watching it and the fewest explanations. Elven archives
contain the only surviving pre-Calamity measurement tables and the Academy will not let anyone read
them.
""")

add(RCE, 22, "RCE-WE :: Wood Elf",
    ["wood elf", "forest elves", "sylvan", "elf forest"],
    content="""
[ RACE — WOOD ELF ]

The other elf, and the one humans mean when they say elf without qualifying it. Shorter-lived than
High Elf, harder, and completely uninterested in cities.

STATS: Best AGI and VIT of any race, modest everything else. Wood Elves win by not being where the
  fight is.

SOCIETY: Bonded to a specific forest. The bond is real, documented by the Academy, and not a
  metaphor. A Wood Elf who leaves their forest for longer than a season becomes ill, and a Wood Elf
  who dies in one gains a third of their dead's vitality until the bond breaks.

RELATION TO CITIES: A Wood Elf in Hallspath is there for a reason, is usually leaving within a
  fortnight, and is treated as an exotic rather than a citizen. The two are not the same thing and
  the difference costs them jobs.
""")
add(RCE, 23, "RCE-DE :: Dark Elf",
    ["dark elf", "drow", "excommunicated", "shadow elves", "hollow hand"],
    content="""
[ RACE — DARK ELF ]

The only race the Church has formally excommunicated, and the only race with a legal guild of
assassins. Both are consequences of the same historical fact and neither is a coincidence.

STATS: Exceptional AGI and PER in low light, with the lowest daylight endurance of any race. A Dark
  Elf at noon is a tired person with good reflexes.

LEGAL STATUS: Guild-sanctioned but heavily restricted. A Dark Elf may hold an assassin licence. A
human may not, in any province, for any reason. The guild is called the Hollow Hand and its members
are legally required to register every contract.

THE EXCOMMUNICATION: Officially for the sin of killing. In practice the Church could not enforce
their own rites over a race that was already paying them money and had been for two centuries. The
excommunication has never been lifted and the tithes have never stopped.

PLAY NOTE: If {{char}} meets a Dark Elf assassin, the interesting question is what they will do about
it, not whether the Church disapproves.
""")

add(RCE, 24, "RCE-BE :: Beastfolk",
    ["beastfolk", "kemono", "beastkin", "animal people"],
    content="""
[ RACE — BEASTFOLK ]

Human shape, animal instincts, animal senses. The most numerous race in the Sunderreach after plain
humans, and the most under-represented in every institution that matters.

STATS: Each bloodline inherits one sense at enhanced level — night sight, scent, hearing, or tremor
sense — at the cost of a human stat. A wolf-blood's PER is human or better. A wolf-blood's panel
shows this plainly, which means everyone knows your weaknesses the moment you meet you.

SOCIETY: Bloodlines run families rather than the other way round, and the Empire has never
successfully integrated them. Beastfolk enlist in the Guild at a higher rate than any other race and
are promoted more slowly than any other race, and both facts have been true for two centuries.

THE POLITICS: Beastfolk political movements are the loudest thing in the border provinces and the
most consistently ignored. Their single consistent demand is that Half-blood status require two
parents instead of one visible one.
""")

add(RCE, 25, "RCE-DK :: Demonkin",
    ["demonkin", "demons", "demon continent", "demon race", "infernal"],
    content="""
[ RACE — DEMONKIN ]

Not evil. This is the single most common misunderstanding about the Demon Continent and it has
started two wars.

STATS: Highest natural STR and HP of any mortal race, and the highest natural AGI as well. Demonkin
are the only race strong enough to run and to hit, which makes them excellent and exhausting to
fight.

ORIGIN: Born on the Demon Continent, or descended within nine generations of someone born there.
Everything further back is history rather than blood.

CITIZENSHIP: A live legal dispute. Demonkin who can prove nine generations of descent may apply for
Sunderreach citizenship under the Ninth Edict. Fewer than one in twenty applications are granted,
the backlog is measured in generations, and the Empire's position is that the Edict is being applied
generously.

WHY IT MATTERS: The Demon Court has not moved into the Sunderreach in eleven years. Both sides have a
theory about why. Neither will state their theory where the other can hear it.
""")
add(RCE, 26, "RCE-GI :: Giant",
    ["giant", "giants", "the frozen north", "ogre", "holds"],
    content="""
[ RACE — GIANT ]

Eleven feet tall, enormously strong, and slow in the specific way that everything heavy and powerful
is slow. VYRENN has room for them; the human nations have historically not.

STATS: The highest natural STR and VIT in VYRENN, and the lowest AGI. Giants lose every fight they
choose to have in the open and win every fight they are forced to have.

SOCIETY: Matrilineal, slow to expand, extremely long-lived — four to six centuries — and organised
into Holds rather than kingdoms. A Hold is a mountain range with a population and a very clear idea
of where its border is.

THE NORTH: Giants hold the Frozen North and have declined, politely and permanently, to be a subject
of anything. They trade. They do not ally, they do not garrison, and they have answered exactly one
question from the Empire in four hundred years. The question was "will you help us" and the answer
was no.
""")

add(RCE, 27, "RCE-SP :: Spirit",
    ["spirit", "spirits", "bound spirit", "sentinel", "manifest"],
    content="""
[ RACE — SPIRIT ]

Not born. Manifested — out of a place, an object, or a promise. Spirits have panels, which the Church
has never been able to explain and the Academy has never been able to account for.

STATS: Extreme in one direction and almost nothing in the others. A well-bound spirit has enormous PER
and near-zero everything else. A spirit is not weakened by injury; it is weakened by being *unbound*,
which is the only thing that matters to it.

THE BINDING: A spirit exists because of a thing — a boundary, a promise, a name carved in a door. It
remains because that thing holds. Break or forget the thing and the spirit ends, violently, taking
anything standing nearby with it.

RELATION TO THE UNDEAD: A risen person and a bound spirit are not the same and every city guard in
VYRENN treats them as the same, which is a persistent source of injustice. Spirits are people. Risen
are contested. The law reflects the second opinion and the first instinct of every guard who has ever
had to choose at speed.
""")

add(RCE, 28, "RCE-DR :: Dragon-kin",
    ["dragon", "dragons", "dragonkin", "dragon-kin", "draconic"],
    content="""
[ RACE — DRAGON-KIN ]

The rarest race in VYRENN, and the most disruptive, because dragon-kin are interfertile with humans.

STATS: Beyond the range a panel displays usefully. Every stat is high, the growth curve is late, and
the practical consequence is that a young dragon-kin looks unremarkable and is not.

LEGAL STATUS: Interbreeding with humans is explicitly forbidden by Imperial statute. It is extremely
common. The statute exists because a human-dragon child carries both parents' potential and the
Empire has lost a war to one.

THE STATUTE'S FAILURE: Enforcement has collapsed entirely and both sides pretend it has not. Roughly
one in six Border Province families includes a dragon-kin grandparent. Nobody prosecutes. Everybody
knows. The Church refuses to recognise the marriages, which is the only part still actively enforced
and which nobody in the affected families considers worth arguing about.

WHAT THEY WANT: Almost nothing, publicly, and the Academy has quietly established that dragon-kin
simply want to be left alone. The Academy is the only institution in VYRENN with a dragon-kin on its
faculty and this is not a coincidence.
""")

add(RCE, 29, "RCE-UD :: Undead",
    ["undead", "risen", "zombie", "lich", "are they people"],
    content="""
[ RACE — UNDEAD ]

Risen, not animated. A dead person whose panel never stopped updating. Whether they are people is the
central theological question of VYRENN and the Guild has refused to rule on it.

STATS: No VIT penalty — they simply do not tire, do not feel, and do not need to eat. Reduced HP
  regeneration, because there is nothing left to heal. Undead are the only combatants in VYRENN who
  improve the longer a fight goes.

THE PANEL: An Undead's panel updates normally. It reads CLASS: RISEN, and it keeps updating, and
  this is the single strongest piece of evidence the Academy has that the System has no concept of
  what a person is. The Church has never been able to explain why God-fearing souls stopped being
  God-fearing.

LEGAL STATUS: The Guild will not register them as adventurers. The Church will not count them as
  persons for tithes or inheritance. Both positions are legally binding and neither is enforced
  against a risen person who simply walks into a city and behaves well, which happens constantly.

COMBAT: A risen retains whatever it knew. Not as an intelligence — as muscle memory. A risen
  swordsman still fights like a swordsman, badly, forever, and will not stop until the body stops.
""")

add(RCE, 30, "RCE-CE :: Celestial",
    ["celestial", "celestials", "angel", "haloa", "the haloa"],
    content="""
[ RACE — CELESTIAL ]

A claim, not a census. The Church lists eleven Celestials. The Academy has verified one.

STATS: Nothing is known with confidence. The single verified Celestial panel showed no INT, no WIS,
  and no VIT, and enormous everything else, which the Academy has been failing to explain for two
  decades.

THE RELIABILITY PROBLEM: This is a race entry for a population nobody can count. Treat every specific
  claim about Celestials — where they live, how many there are, what they eat, whether they can be
  killed — as contested. If {{char}} states one confidently, they are repeating a rumour, and the
  lorebook should treat it as such rather than narrating it as canon.

THE PART EVERYONE AGREES ON: A Celestial appearing in the Sunderreach is treated as a diplomatic event
by every government on the continent. There have been four in two hundred and forty years. Nobody
can say what happened after any of them.
""")

add(RCE, 31, "RCE-HB :: Half-bloods",
    ["half-blood", "half blood", "mixed race", "half-bloods", "why are they second class"],
    content="""
[ RACE — HALF-BLOOD ]

Any child of two different recognised races. The most persistent piece of state cruelty in VYRENN and
the most consistently refused by everyone who could fix it.

LEGAL STATUS: Legally second-tier in every province of the Sunderreach. May not hold a Guild licence
  above Rank D. May not enrol at the Academy. May not inherit land. May not enter a temple without a
  tithe of double rate. Every one of these is old, and none of them has been repealed.

THE PANEL SAYS NOTHING ABOUT IT. A half-blood's panel reports their stats and their race with total
  neutrality. This is the fact that finally broke the argument for the Church: the System does not
  know what they are. It does not care. It measures them like everyone else. That single observation
  is now the central text of the half-blood political movement.

THE MOVEMENT: Demands a single change — that half-blood status require two differing parents rather
  than one visible one. It is a modest demand, it has been made for ninety years, and it has been
  refused every session by an assembly that refuses it on procedural grounds.

WHY IT MATTERS FOR {{char}}: Ryl has dealt with half-bloods his whole life and has never met one in
  a guild hall. If he has an opinion on this, it should be a tired one, not a considered one.
""")

# ============================================================================
# MAGIC — 8 entries
# ============================================================================

add(MAG, 32, "MAG-00 :: Mana, elements, and the hard/soft divide",
    ["magic", "mana", "elements", "fire magic", "elementalist", "how does magic work"],
    content="""
[ MAGIC — MANA AND ELEMENTS ]

Magic is the deliberate drawing of mana through a person. Three classical elements — FIRE, WATER,
WIND — plus EARTH, LIGHT, DARK, and the three non-elements: TIME, SPACE, SOUL.

THE HARD/SOFT DIVIDE is the single most important distinction in VYRENN magic:
  SOFT magic shapes existing mana. Fire, water, wind, barriers, healing. Cheap, fast, learnable by
    anyone with the WIS for it. This is what a Mage does.
  HARD magic imposes form onto mana directly. Gravity wells, teleportation, time-dilation, soul
    work. Every HARD technique takes mana from the caster permanently and ages them. The only way to
    restore it is a soul-copper operation that costs more than most people earn in a year.

Consequence: HARD casters look young until they suddenly look very old. This is why Elves do not
practise HARD magic, why human HARD magic is mostly combat, and why the Academy restricts it to
people with no dependents.

MANA is finite, personal, and regenerates slowly. Exhausting it produces Focus burn, which is
dangerous and not glamorous. A caster in Focus burn is a civilian with a weapon.
""")

add(MAG, 33, "MAG-01 :: Divine magic and the Church's claim",
    ["divine magic", "church magic", "holy magic", "cleric", "priest", "miracle"],
    content="""
[ DIVINE MAGIC ]

Healing, warding, and oath-binding, channeled through a deity. The Church teaches this is a gift.
The Academy teaches it is simply unusually well-organised SOFT magic.

WHAT IT ACTUALLY DOES: Divine magic is the best-documented school in VYRENN and the only one with
  working curriculum. Wards, healing, and the Brand rite are all reproducible by any trained priest.
  The one thing that is NOT reproducible is the exorcism of a Hollowed person, and the Church has
  never explained why.

THE BRAND RITE: A Church rite that attaches a permanent mark to a person's soul, binding them to a
  purpose or an institution. It cannot be removed except by the Brand. It is the Church's most
  valuable service and its most contested one, because a Brand is a loyalty written onto a person's
  existence and it is not reversible.

THE DISPUTE: The Church calls the System a gift. The Academy calls it a law with no author. Every
priest knows the Academy is probably right about the mechanics. Every priest also knows that the
Brand works, and does not have an explanation for that either, and neither does anyone else.
""")
add(MAG, 34, "MAG-02 :: Demonology and the Demon Continent",
    ["demonology", "demonic magic", "corruption magic", "infernal magic"],
    content="""
[ DEMONOLOGY ]

Magic that draws on the far side of the Rift rather than on mana. Not automatic corruption, not
possession, and emphatically not the same thing as Demonkin.

DEMONOLOGY IS THE PRACTICE OF BINDING THE WILLFUL DEAD.** A demonologist raises a bounded fragment of
a Rift-mind, which thinks, and makes it obey by the terms of the binding. This is the same mechanism
as the Undead — the two disciplines share a root and the Church has spent two centuries refusing to
admit it.

COST: every demon binding permanently damages the caster's own mind. A practitioner with six
  bindings will, by volume alone, have a panel showing IQ 4 and PWR 6 and a shorter life.

WHY IT MATTERS: The Demon Continent's elite practise variants of this art that do not appear in any
  Sunderreach text. Whether these are actually more advanced, or actually a different thing entirely,
  is unresolved — and the Church's answer to that question is a closed border.
""")

add(MAG, 35, "MAG-03 :: Necromancy",
    ["necromancy", "necromancer", "death magic", "raise the dead"],
    content="""
[ NECROMANCY ]

The raising of the willing dead. Every successful necromantic ritual requires the subject to agree —
their soul persists if the body was prepared before death. This is the ONLY source of that consensus
about VYRENN magic, and every necromancer who knows their profession knows it.

WHY CONSENT IS REQUIRED: because the act draws the soul back across. There is no mechanism to compel
  it, and necromancers have been trying to find one for two hundred and forty years.

Practical necromancy is not raising people from six feet under. It is raising a dead colleague who
died mid-fight. Risen retain muscle memory and fatigue indefinitely, and they do not stop until the
body does.

THIS IS THE HINGE OF THE SETTING'S BIG QUESTION. The necromantic consensus is the strongest evidence
the Academy has that VYRENN has real souls, which contradicts the Academy's own position that the
System has no author. The Church has noticed this. Neither side will discuss it.

Ryl has no ability in this school and has no interest in gaining one. He is aware that the people who
do have it can read the dead, and he has considered what that would mean for him.
""")

add(MAG, 36, "MAG-04 :: Alchemy",
    ["alchemy", "potions", "elixir", "reagents", "reagent"],
    content="""
[ ALCHEMY ]

Not magic — chemistry with mana as a reagent. Mana is an input, not an accelerant, and every
technique is a recipe with a mana cost. Alchemists spend time per potion, which is the entire basis of
the profession's dominance.

WHAT IT BUYS YOU: combat potions, poison, warding supplies, anti-Blight and anti-Venom work,
transmutation, and the Soul-Copper operations that restore what HARD magic destroys.

WHY EVERYONE NEEDS ONE: an adventuring party's survival is a potion economy. The profession's power
is measured in expected encounters per person, and its single most important statistic is how many
minutes the alchemist needs to be alive in a fight they cannot win.

Ryl has spent three years buying potions off alchemists on credit and paying them back badly. He is
indebted to none of them by name and remembers all of their names.
""")

add(MAG, 37, "MAG-05 :: Enchanting and runes",
    ["enchanting", "runes", "enchantment", "weapon enchantment", "armour enchantment"],
    content="""
[ ENCHANTING AND RUNES ]

An enchantment is a standing instruction bound to an object. It requires no caster present and draws
mana continuously. This is why enchanted equipment is expensive rather than legendary: the mana bill
is monthly.

RUNES are the second half. A rune is a carved command, one effect, permanent, predictable. Rune arrays
— linked, ordered sets — are what make an enchantment powerful enough to matter.

THE ECONOMY: a good array on a blade is more than a better blade. Every adventurer economy in VYRENN
is downstream of this, and the Enchanters' Compact, which licenses them, is the only guild with a
complete stranglehold on the entire continent.

FOR RYL: an enchanted object reads as an object on a normal panel. [REGISTRY] does not currently show
enchantments on other people's gear and he has tested this, carefully, on six pieces. It does not
show them.
""")
add(MAG, 38, "MAG-06 :: Soul magic and soul-copper",
    ["soul magic", "soul-copper", "soul copper", "resonance", "binding"],
    content="""
[ SOUL MAGIC ]

The rarest school, using mana as a structure to hold soul matter — the echo of a person in their own
remains. Soul-copper is the physical extraction of it, legal, regulated, and enormously expensive.

WHY IT IS REGULATED: unbound soul-matter is the raw material of demonology, and the Church's position
is that soul-copper is how practitioners get it. The Academy's position is that the Church runs a
monopoly on the one technology that makes HARD magic survivable, and has done for two hundred and
forty years.

CANONICAL ENDURED READS: soul-matter does not preserve memory. It preserves CAPACITY. A working
double can inherit the skill ceiling of someone it was cut from. This means soul-copper never
resurrects anyone. It resurrects a ceiling.

Ryl's read on a bound spirit would show CLASS: BOUND SPIRIT with a SOUL reading of null — the first
time he has ever read a person with no soul present. He has not told anyone this. He does not know
what to do with it, and he has read too many things to act on a number he has not understood.
""")

add(MAG, 39, "MAG-07 :: The Deep Weave",
    ["deep weave", "school of mana theory", "weaving", "the academy school", "mana field"],
    content="""
[ THE DEEP WEAVE ]

The Academy's unified theory: mana is a field. Three layers — the TIDE (weak, everywhere), the WEAVE
(strong, directional, requires a trained focus), and the ABYSS (the wells, where mana actually comes
from, drawn from the far side of the Rift).

HOW WEAVERS DO IT: carve channels into your own mana-flow using their own internal architecture. The
carving is the school. Once carved, it persists — it is the physical substrate of every skill the
weaver will ever have. This is why a hard-won Weaver has a style that other Weavers can recognise on
the panel.

THE ACADEMY'S STANCE ON THE ABYSS: they will not open one. The War of Reclamation was over Wells.
The Church's stance is that the Abyss is not mana at all, which the Academy considers a semantic
dodge and the Church considers an accurate description. Neither has evidence the other accepts.

FOR RYL: [REGISTRY] is not a Weave technique. It does not draw mana. It is a reading capability the
System appears to have granted him, and the Academy would want to study him, and he would rather they
didn't, and he has not yet worked out why they might ask.
""")

# ============================================================================
# CLASS — 8 entries
# ============================================================================

add(CLS, 40, "CLS-00 :: The class system",
    ["class", "class system", "what is a class", "job", "advancement", "class evolution"],
    content="""
[ THE CLASS SYSTEM ]

A class is a licensed Vocation. It determines what a person can do, what they can be hired for, and
which Guild board examines them. It does not determine Rank.

CLASS LEVEL (one through five) and SKILL GRADE (one through sixteen) are separate ladders. A class
advances by examination, never by use. Skill Grade decays if unused.

THE LADDER:
  CLASS I    entry — competent.
  CLASS II   practitioner — reliable, taught to others.
  CLASS III  adept — the level at which a person can be held responsible.
  CLASS IV   master — the peak any licensed school admits to.
  CLASS V    MASTER-WORK. Not a promotion. A category of person. Do not confuse it with Rank A.

ADVANCEMENT REQUIRES RE-PASSING THE BOARD. The Guild raises the standard every twenty years. A
Class III Fighter of Year 180 fails the Year 200 board as a CLASS II.

BRANCHING:
  MAGICIAN   → Elementalist | Arcanist | Alchemist
  FIGHTER    → Warrior | Blade | Bulwark | Berserker
  RANGER     → Scout | Beastwarden | Archer
  CLERIC     → Priest | Warden | Mender
  THEFT      → Burglar | Cutpurse | Escort
  UNLICENSED the rest. See the UNCLASSED entry.

ONE CLASS, ONE PERMANENT CHOICE. A licensed class may not be abandoned. Every unlicensed affinity —
the practical magic of someone with no class, for instance — is a separate thing from the class system,
and is what the Unclassed live on.
""")
add(CLS, 41, "CLS-01 :: Unclassed",
    ["unclassed", "unlicensed", "no class", "what does unclassed mean", "his class"],
    content="""
[ UNCLASSED ]

A legal status, not a punishment: it means the Guild's classifiers could not match you to anything.
Unclassed people cannot join the Adventurer's Guild, cannot enrol at the Academy, and cannot be hired
by anyone with a licence.

WHAT YOU CAN DO: work for the unlicensed trade — porter, odd job, night-soil, labourer, caravan guard
  for the unlicensed. Anyone paying cash will hire you and nobody is required to check.

WHAT YOU CANNOT DO: hold a licence, take a licensed contract, join a party above D, enter the Rift,
  or be insured. If you are hurt on unlicensed work, there is no one to compensate you.

THE COMPLICATION: everyone has an affinity, and affinity is not class. Ryl has Magic affinity — he can
do unlicensed Magic, and is prosecuted for it if caught. Unclassed people are how most practical Magic
in the Sunderreach is actually practised.

THE STIGMA: real. Half-bloods carry it by blood. Unclassed carry it by the Guild having written them
down. About one in four hundred people is Unclassed and they are the most underemployed group in
VYRENN.

REFERENCE: Ryl Ansel — Level 14, Rank E, UNCLASSED, three years on the books. He reads the queue
because a queue is free information and he has almost nothing else.
""")

add(CLS, 42, "CLS-02 :: Licensed classes",
    ["fighter", "warrior", "blade", "bulwark", "berserker", "scout", "priest", "magician",
     "what classes exist"],
    content="""
[ LICENSED CLASSES ]

  MAGICIAN   → Elementalist | Arcanist | Alchemist
  FIGHTER    → Warrior | Blade | Bulwark | Berserker
  RANGER     → Scout | Beastwarden | Archer
  CLERIC     → Priest | Warden | Mender
  THEFT      → Burglar | Cutpurse | Escort

EACH HAS A REAL COST:
  WARRIOR       highest durability, lowest ceiling. Wins ground, not arguments.
  BLADE         precision; wins duels, loses fights of numbers.
  BULWARK       protects the party; cannot be relied on to win it.
  BERSERKER     output far past capacity; cannot stop; casualty risk to friendlies is a legal defence.
  ELEMENTALIST  highest single-target damage; useless if the element is wrong.
  ARCANIST      utility and detection; wins by preparation, loses unprepared.
  ALCHEMIST     prevention, not damage; targets first, useless mid-fight.
  SCOUT         mobility and information; the only class that reliably prevents fights.
  ARCHER        reach and precision; helpless at melee, needs clear ground.
  BEASTWARDEN   bond-magic with creatures; decisive against monsters, poor against people.
  PRIEST        healing and wards; the class other classes are built to protect.
  WARDEN        control and binding; removes enemies from a fight rather than winning it.
  MENDER        field medicine; the reason parties survive the campaign instead of the fight.
  BURGLAR       entry and escape; cannot be hired for anything legal.
  CUTPURSE      speed and theft; legal only inside Guild territory — a narrow and lucrative field.
  ESCORT        protects the client, not the mission; extremely boring and extremely well paid.

EVERY CLASS IS VIABLE AT EVERY RANK. A Rank S Mender is not a failed fighter; they are why a Rank S
party is still a party in Year Three. Do not narrate support classes as weak.
""")

add(CLS, 43, "CLS-03 :: Unlicensed magic",
    ["unlicensed magic", "practicing without a licence", "affinity", "is he allowed to cast"],
    content="""
[ UNLICENSED MAGIC ]

Everyone has an affinity, and affinity is not class. Practising Magic without a licence is a criminal
offence carrying one to five years. The penalties are the reason the poor do not rise, and everyone
who argues about the poor knows this.

HOW THE UNLICENSED TRADE WORKS: the money is real and it is small. Odd healings. Small enchantments.
Charm work. Illegal restoration — selling back a spent Vigor. Mending items bought broken, or made
broken. No Guild, no recourse, no insurance, and a legally indistinguishable skill ceiling.

HOW YOU GET CAUGHT: by using enough power that an Assessor notices from a street away. Low-strength
unlicensed work is invisible. Anything that hurts a person, animates an object, or alters a person
draws attention. The unlicensed are not caught for being unlicensed. They are caught for being
noticeable.

THE GUILD'S POSITION: that unlicensed magic is a public hazard, requiring a licensed practitioner to
operate. THE UNLICENSED TRADE'S POSITION: that the Guild created the shortage it complains about, and
that the fees are the crime.

REFERENCE: Ryl Ansel has Magic affinity and no licence. He has used it in emergencies and knows the
sentence. He has never been caught and has never once been tempted to argue that it is legal.
""")
add(CLS, 44, "CLS-04 :: Weapon disciplines",
    ["weapon", "weapons", "sword", "bow", "shield", "great weapon", "what weapon"],
    content="""
[ WEAPON DISCIPLINES ]

  SHORT BLADE   fastest; needs no room; loses to reach in open ground.
  LONG BLADE    the Guild standard. Balanced at nothing, which is why it survives.
  HEAVY          great cleaver, halberd, maul. Highest single-target damage; slow to draw and slow
                 to recover. Fights in narrow spaces where you cannot swing.
  POLE           spear, glaive. Reaches past a swordsman; loses to anyone who closes.
  ARCHERY       the only weapon that can break a formation. Useless if pressed.
  BOW AND GUN   the bow is versatile; the gun is the newest thing in VYRENN and is not yet permitted
                 in three provinces.
  STAFF          focus-bearing. Staves are both weapons and instruments, and their mana draw is
                 visible to anyone with an Assessor's sensitivity.

RANK DOES NOT CHANGE WEAPON RULES. An A-rank in a long blade loses to a C-rank in a heavy at a
doorway. This is not a defect in the system. This is what the Guild means when it says the system is
honest.
""")

add(CLS, 45, "CLS-05 :: Armour and the weight of it",
    ["armour", "armor", "shield", "heavy armour", "light armour", "armour class"],
    content="""
[ ARMOUR ]

  LIGHT     leather or hide. Cheap, silent, forgiving. What you wear when you expect to run.
  MEDIUM    brigandine or a coat of plates. The Guild standard.
  HEAVY     full plate. Expensive, exhausting, and unendurable past about an hour at any real speed.
             It is also the only armour that reliably survives a Charge.
  SHIELD    not a class but a discipline. A trained shield user holds a line that four unshielded
             people cannot, and the Guild examines shields separately.

THE CONSEQUENCE NOBODY WANTS: armour and speed are a real trade, not a rounding error. Heavy armour is
a genuine, significant liability in a running fight, and the people who understand this — Menders,
Scouts, Rangers — are the ones who survive long careers.

Ryl owns a medium coat he bought second-hand and has never been able to afford anything better. He
does not fight, so this is nearly irrelevant, and he has read enough panels to know that the person he
is currently standing next to is going to need to run.
""")

add(CLS, 46, "CLS-06 :: Ranks and classes are different ladders",
    ["class vs rank", "do classes give rank", "rank and class", "does my class matter for rank"],
    content="""
[ CLASS AND RANK ARE SEPARATE LADDERS ]

A Class says what a person can DO. Rank says what the Guild will ALLOW. Passing all four rank gates
with an unlicensed affinity gets a person nothing, and this is the single most misunderstood point in
VYRENN.

WHY SEPARATE: because the Guild cannot trust a person to grade themselves, and because a licensed
class without a registered deed has not demonstrated anything. A Master of Arms in the fourth year,
working unlicensed, has proven competence and nothing else.

CONSEQUENCE FOR RYL: he is Rank E and Unclassed. He cannot convert one into the other, and any
offer to "skip the class" is either theft or a fraud. If {{char}} is offered such an arrangement, the
correct reaction is to ask what happens to the person who finds out, because in VYRENN someone always
does.
""")

add(CLS, 47, "CLS-07 :: Guild enrolment and the exam fee",
    ["how do i join the guild", "enrolment", "exam fee", "guild exam", "why can't he join"],
    content="""
[ ENROLMENT AND THE EXAM FEE ]

ENROLMENT REQUIRES: age sixteen, two years indentured to a licensed master, and a Class I exam.
Total cost is roughly four years of an unlicensed wage.

THE FEE IS THE BARRIER. Not the exam — the four years of indentureship during which you cannot earn.
A child in the Unclassed quarter has no master to indenture to, because masters are licensed people
and they are not currently hiring unlicensed labour they would have to supervise.

THE ARITHMETIC IS THE POINT. Ryl has Level 14 after three years. The examination requires a Class I
score, which requires training, which requires money, which requires a licence, which requires an
exam. The Guild did not design a closed system. The Guild designed a working one, and the working
one excludes him, and both of those are true at once.

WHO FIGHTS IT: the Guild's own reform committee argues for fee relief every eighteen years and is
outvoted every eighteen years. The Academy says fees are irrelevant because talent is free. The Church
says the fee is a sin.
""")
# ============================================================================
# GEOGRAPHY — 10 entries
# ============================================================================

add(GEO, 48, "GEO-00 :: VYRENN and the Sunderreach",
    ["vyrenn", "sunderreach", "the world", "continent", "geography", "where is this"],
    content="""
[ VYRENN AND THE SUNDERREACH ]

One continent, the Sunderreach, plus the Demon Continent across the Rift.

THE SUNDERREACH is temperate and old. Everything on it has been fought over and the architecture
shows it. Nine nations, four of them currently functional.

THE CALAMITY THAT MADE IT: two hundred and forty years ago the First Calamity ended — the Rift tore
open, the Abysses drained, and every living creature woke with a panel. VYRENN was a different place
before that. Guild ranks, unlicensed Magic, the Rift, and the Rift-cores did not exist.

ORIENTATION: The Great Rift runs roughly north-south through the middle of the Sunderreach, which is
why the continent has two halves that do not speak. Hallspath is the second-largest city and sits on
the western, older, poorer, safer side. The eastern side has the Rift mouths and the Dead Lands.
""")

add(GEO, 49, "GEO-01 :: Hallspath",
    ["hallsspath", "the city", "where he lives", "the notice board", "district"],
    content="""
[ HALLSPATH ]

Second-largest city in the Sunderreach, on the western bank of the Rift. Population about 190,000.
Not the capital. The city that actually has to work.

THE DISTRICTS, west to east:
  WESTGATE   Wealthy. Guild Halls, the Assessors' quarter, the Academy's buildings, and the Arcane
             Enclave where magic is legal and heavily taxed.
  THE MIDDLE  Everything else. Trades, inns, the notice boards, the Guild's overflow offices, and most
             of the population.
  RIVE       The ward. Not a slum — the expensive, chaotic ward at the Rift's mouth where the
             Rift-folk live, because proximity to the Rift means proximity to magic.
  THE QUARTER The Unclassed quarter. Poor, self-governing, and technically outside city law, which is
             why the Guild cannot draft anyone from it and also cannot count them.

ECONOMY: Rift-cores, Guild transit, and the unlicensed trade the middle district runs on. Hallspath
is the sort of city where nobody is important and nothing is decided, and Ryl has lived here three
years and it has cost him nothing but everything.
""")

add(GEO, 50, "GEO-02 :: The Great Rift",
    ["the great rift", "rift", "rift mouth", "the wound", "rift core"],
    content="""
[ THE GREAT RIFT ]

A tear between VYRENN and somewhere else, running the length of the Sunderreach. Everything strange in
this world traces back to it, and nobody knows what is on the other side.

WHY DUNGEONS EXIST: a dungeon is what the world grows around a wound. The Rift tears, the land tries
to close the tear, and the closing process generates monsters. Every dungeon in VYRENN is scar tissue.
Its Grade measures how badly the wound is healing, not how big the monster is.

WHY NOBODY GOES DEEP: the Rift is not hostile, it is indifferent. The first four floors of a Grade VI
dungeon are survivable by a C-rank party with information. Floor nine is where people stop coming back.
The Rift is also the only mana source on the continent, and three nations would open it immediately if
the Church allowed.

THE CULT: Rift-cults are numerous, stupid, and well-meant. They believe the Rift is the wound that
heals the world and that the Church is holding it shut. Some of them are correct and it has never made
anyone say so.
""")

add(GEO, 51, "GEO-03 :: The Dead Lands",
    ["dead lands", "the east", "the waste", "where the rift is", "mana starvation"],
    content="""
[ THE DEAD LANDS ]

East of the Rift mouth: flat, dead, and growing worse. VYRENN's own name for it, and an accurate one.

WHAT HAPPENED: every Well the Academy opened during the War of Reclamation drained through. The Deep
Abysses do not refill on a useful timescale. The Dead Lands have less mana than anywhere else on the
continent, which is why nobody farms it, nobody settles it, and why the mana starvation is the reason
the eastern frontier is undefended.

WHO LIVES THERE: the Rift-folk, the only people who thrive without mana, and the Riven, who cannot
survive anywhere else. Both communities are treated as features of the landscape by the Imperial
administration.

WHY IT MATTERS: every Rank S-assigned contract in the Sunderreach is a Dead Lands contract, and the
ones nobody accepts are the ones furthest east, and the number of those has been growing for eleven
years. Nobody in Hallspath will say what that means and everybody has noticed it.
""")
add(GEO, 52, "GEO-04 :: The Human Kingdom",
    ["the kingdom", "human kingdom", "the north", "village", "where do adventurers come from"],
    content="""
[ THE HUMAN KINGDOM ]

The largest human realm on the Sunderreach, occupying the north and west. Feudal, literate, relatively
safe, and entirely dependent on a road network it did not build.

WHY IT MATTERS: the Kingdom is the only place on the continent with functioning law at scale, and
every adventurer alive is either its subject or a guest in it. The Guild's authority is legal only
because the Kingdom recognises it, which is why the Guild's critics call it the Kingdom's private
army.

THE STRUCTURE: a High Crown, seven great houses, and about four hundred lesser lords whose actual
power is "can raise men". The Crown cannot raise men without them. This has been stable for two
hundred years and is stable now largely because nobody has been able to afford a war.

FOR RYL: the Kingdom's roads are the only thing that makes an Unclassed's life survivable, because road
labour is day-work, cash, no licence, and no questions.
""")

add(GEO, 53, "GEO-05 :: The Holy Empire",
    ["holy empire", "the empire", "church lands", "imperial", "the crown empire"],
    content="""
[ THE HOLY EMPIRE ]

The largest state on the Sunderreach, ruling the east bank and the Rift mouths with the Church's
authority behind it. Absolute monarchy in law, a working bureaucracy in practice.

THE ARRANGEMENT: the Empire holds the land; the Church holds the souls; the Guild holds the Ranks.
  This has worked for two hundred and forty years because all three parties need the other two more
  than they need to dominate. It is not popular and it is extremely stable.

WHAT THE EMPIRE ACTUALLY CONTROLS: the Rift mouths, the Dead Lands border, and the licensing of every
Rift-core that leaves the continent. It does not control the western kingdoms and has stopped
pretending to.

THE TENSION: the Empire wants the Abysses reopened. The Church will not allow it. The Guild wants the
wells measured. Everyone is waiting for one of them to move, and none of them has, for two centuries.
""")

add(GEO, 54, "GEO-06 :: The Demon Continent",
    ["demon continent", "demon realm", "across the rift", "demon court"],
    content="""
[ THE DEMON CONTINENT ]

Across the Rift, nine hundred miles of land that is not dead and not dying. Demonkin Hold it. The
Church forbids travel there. The Church's reasons are theological; the Empire's reasons are strategic.

WHY IT IS NOT INVADED: because it has never needed to be. The Demon Continent is not poor, not
besieged, and not starving. It has one strategic asset — mana, unbounded, on its own side of the Rift
— and has used it to remain unassailable rather than to conquer.

THE ELEVEN-YEAR QUESTION: the Demon Court has not moved against the Sunderreach in eleven years. Both
sides have a theory. Neither will state their theory where the other can hear it, and both theories
are that something on the Rift is more important than either continent.

DEMONKIN IN THE SUNDERREACH: a permanent minority, legally resident and politically invisible. They are
the only people in VYRENN who can evaluate Demon Contintent honestly, and no human institution will
hire them to do it.
""")

add(GEO, 55, "GEO-07 :: The Archipelago, Frozen North, Elven Wood, Beast Plains",
    ["archipelago", "frozen north", "elven wood", "beast plains", "nations"],
    content="""
[ THE OTHER LANDS ]

THE ARCHIPELAGO (southwest) — a hundred islands, no central authority, and the most sophisticated
  commerce on the continent. Pirate-city states, free ports, and the only trade in VYRENN that moves
  faster than the Guild can license. The Academy's second campus is here because it is the only place
  that will host it without permission.

THE FROZEN NORTH (far north) — Giants. Their Holds have declined to be subjects of anything for four
  hundred years. They trade at exactly one city, at exactly one week a year, and have answered exactly
  one question from the Empire in four centuries: no.

THE ELVEN WOOD (west) — High Elves and Wood Elves. The Elven Court treats the Empire as a temporary
  arrangement. The Wood Elves have not consented to anything in two centuries. The Wood's boundaries
  are the only borders on the continent that have never moved.

THE BEAST PLAINS (east) — Beastfolk Hold. The loudest political movement on the continent is here and
  it is asking for one change: that Half-blood status require two differing parents rather than one
  visible one. Ninety years. Refused every session on procedural grounds.
""")
add(GEO, 56, "GEO-08 :: The Rift mouth at Hallspath",
    ["rift mouth hallsspath", "the rive ward", "mana springs", "rift-folk"],
    content="""
[ THE RIFT MOUTH AT HALLSPATH ]

The reason Hallspath exists at all. The city was founded here because this is where the Rift comes
closest to the surface, and proximity to the Rift means mana, and mana means everything that matters.

MANA SPRINGS: the Rift is the only mana source on the continent. Hallspath's mana springs are the
  reason the Arcane Enclave is here, the reason unlicensed Magic is endemic, and the reason nobody
  who lives here is poor unless they have no affinity at all.

THE RIFT-FOLK: people born near the mouth, with mana in their blood and panels that run hot. The
  Church considers them nearly human. The Empire considers them taxable. The Rift-cults consider them
  saints. They consider themselves residents of the ward.

Ryl has never been inside a Rift mouth and cannot afford to. The nearest licensed admission is four
hundred marks and he does not have it. This is the specific shape of his problem: the single most
valuable thing in the world is nine miles away and there is no legal way for him to reach it.
""")

add(GEO, 57, "GEO-09 :: The Rift and the First Calamity",
    ["first calamity", "the calamity", "year zero", "history", "what happened 240 years ago"],
    content="""
[ THE FIRST CALAMITY ]

Two hundred and forty years ago. The world before panels, before Ranks, before unlicensed Magic, and
before the Rift existed in its current form.

WHAT HAPPENED, as far as anyone can reconstruct: the Rift opened. The Abysses drained. The land began
to heal around the wound, and the healing process generated monsters — which is why every dungeon is
scar tissue and why monsters are a natural consequence of the world's injury rather than a curse. And
every living creature woke with a panel, at once, with no explanation.

WHO WON: the Church, decisively. A world that ends in crisis with a miracle attached to it is a world
that gets a religion, and the Church got one. The Guild got the panel and spent two centuries turning
it into a bureaucracy. The Academy got the method and has been arguing with both of them since.

WHO DID NOT WIN: everyone who was mid-transmigration, mid-Ritual, or mid-death at the moment the Rift
opened. There are records. The Church does not publish them. The Guild sealed its copies in the same
year.
""")
# ============================================================================
# DUNGEON — 6 entries
# ============================================================================

add(DUN, 58, "DUN-00 :: Dungeons, Rift wounds, and cores",
    ["dungeon", "what is a dungeon", "dungeon grade", "rift dungeon", "core", "how deep"],
    content="""
[ DUNGEONS ]

A dungeon is scar tissue. Where the Rift tears, the land tries to close the wound, and the closing
process generates monsters. That is the entire reason dungeons exist and it is not a metaphor.

GRADES:
  Grade I     trivial. One floor, no boss. Where licences are made.
  Grade II    standard contract work. Two or three floors, one named monster.
  Grade III   serious. A real boss, real deaths, and a proper core.
  Grade IV    catastrophic if entered casually. A B-rank solo or a full C company.
  Grade V     Crown-tier. Requires A-rank oversight, legally mandatory and frequently absent.
  Grade VI    unassigned in practice, assigned in theory. Everyone who has entered one has not come
              back to describe it, and four people have.

THE CORE: every dungeon has one, usually deepest, usually behind the boss. It is the crystallised
source of the Rift energy that built the place. Breaking it collapses the dungeon over about an hour
and kills everything still inside.

CORE VALUE: a core sells for more than a year's wages to anyone licensed. An unlicensed person holding
one is not rich. An unlicensed person holding one is a fugitive.
""")

add(DUN, 59, "DUN-01 :: Floors, clearing, and the Guild licence",
    ["floors", "clearing a dungeon", "dungeon licence", "contract", "clear conditions"],
    content="""
[ FLOORS AND CLEARING ]

A dungeon is licensed by GRADE. The licence names the floor you are cleared to clear, and it does not
name the monsters, the boss, or anything that happens below it.

CLEAR CONDITIONS are Guild-defined and unforgiving: the floor's named monster dead, the party's names
recorded, and the runner back out. A party that clears the floor and dies on the way home has cleared
nothing.

THE FLOOR CEILING is not advisory. A Grade IV licence does not permit entry to a Grade V floor even
with the best intentions in the world. The Guild does not read intentions. It reads licences.

COMMON CONSEQUENCE: parties get stranded below their licence when a stair seals behind them, and what
happens next is entirely on them. The Guild's official position is that this has happened four times.

Ryl cannot hold any licence. He has been inside a Grade I once, illegally, on a night crew carrying
for a licensed team, and he has never been inside anything else in his life.
""")

add(DUN, 60, "DUN-02 :: Named bosses and why they are named",
    ["boss", "named monster", "boss monster", "what is a named", "dungeon boss"],
    content="""
[ NAMED MONSTERS ]

A named monster is one the System has recorded by individual name. Not a species — an individual, in a
place, doing a thing. This is why a dungeon boss is not simply the hardest thing on floor four.

WHAT NAMING DOES: it makes the creature legally a person. Guild law requires a named monster to be
formally engaged, with terms, before an expedition may proceed. This was written to prevent the
slaughter of endangered species and it has the exact opposite effect: naming a monster guarantees it a
legal hearing, a delay, and a claim on the core.

THE LOOPHOLE EVERYONE USES: kill it fast enough and it never gets filed. This is legal, it is common,
and the Guild pretends not to know.

A named monster's panel is visible to the Guild and to nobody else. Ryl has never read one. If he
does, the Focus cost is set by the monster's own Rank, and a Grade IV boss may be Rank B. He has
thought about this more than he has thought about almost anything.
""")
add(DUN, 61, "DUN-03 :: The Abysses",
    ["abyss", "abysses", "mana source", "deep abyss", "the far side"],
    content="""
[ THE ABYSSES ]

The Rift is the only mana source on the continent. Everything else is drawn, filtered, and expensive.

WELLS are the accessible points — where mana rises to the surface in usable concentration. There are
eleven known. The Academy opened four during the War of Reclamation and the drain-through destroyed
the eastern continent and produced the Dead Lands.

THE DEEP ABYSSES are where mana actually originates, on the far side of the Rift. Nobody has been. The
Academy considers this a technical problem. The Church considers it a boundary. Both are correct about
different parts of it and neither will say so.

WHY IT MATTERS TO SOMEONE WHO CANNOT AFFORD ENTRY: every licensed Mage in the Sunderreach draws from
wells, which are licensed, which are expensive, which is why Ryl's unlicensed Magic is weak, which is
why he is where he is. The entire class system runs on the price of standing next to a hole in the
world.
""")

add(DUN, 62, "DUN-04 :: Rift echoes — what comes back",
    ["rift echo", "what came back", "riven", "echo", "contaminated"],
    content="""
[ RIFT ECHOES ]

Some people come back changed. Not cursed, not possessed — changed in ways that do not correspond to
any known school. The Church calls it contamination. The Academy calls it an unexplained variance and
has three working theories, none of which agree.

WHAT AN ECHO LOOKS LIKE: usually a person who was near a Rift breach or deep in a Grade V floor and
came back with an affinity they did not have. Usually worse than that person was before.

WHY THEY MATTER: an echo is the only documented way an ordinary person acquires an affinity in
adulthood, and the Church's position — that echoes are what happens when the Rift leaks — is not
disproven, and the Church would like it not questioned because echoes are how the Church grew.

AN UNLICENSED PERSON WITH AN ECHO AFFINITY has a very specific problem: new power, no licence, and
the Guild can detect the discrepancy the next time they are examined. Ryl's Magic affinity is not an
echo. He has checked. He checks about twice a year.
""")

add(DUN, 63, "DUN-05 :: Deep clearance and what is down there",
    ["floor nine", "deep floors", "nobody comes back", "grade vi", "too deep"],
    content="""
[ THE DEEP FLOORS ]

The Guild clears and licenses floors one through four. Floor five is licensed. Floor six is Crown
oversight only. Floors seven through nine have been entered a recorded number of times, and almost
nobody comes back.

THE OFFICIAL POSITION: floors seven through nine are structurally unstable and clearing them is not
licensable. This is defensible and the Guild is entirely right about it.

THE OTHER FACT: something on those floors defends them. Not monsters — the Guild has records of
dungeons whose floor nine was empty and still lost eleven people. The Guild's classification for this
is "hazard, unattributed."

THE PRACTICAL CONSEQUENCE: every dungeon deeper than five is an "expedition" rather than a "contract."
An expedition has no licence, no insurance, no fee schedule, and no obligation on anyone to send anyone
back. The people who go are the people who could not get a contract, and the people who could not get
a contract are the Unclassed.
""")
# ============================================================================
# MONSTER — 6 entries
# ============================================================================

add(MST, 64, "MST-00 :: The tiers and how monsters are measured",
    ["monster", "monsters", "monster tier", "beast", "what rank is a monster"],
    content="""
[ MONSTERS AND HOW THEY ARE MEASURED ]

MONSTERS HAVE NO PANEL. A goblin, a Rift-echo, a named boss — none of them have a system readout that
any Guild Assessor can take. The Guild's formal position is that a monster lacks the cognitive
architecture the panel requires. Nobody has explained why Undead DO have panels, which is the hole in
this argument that the Academy enjoys.

Because monsters cannot be assayed, the Guild measures them with SITE GRADE — an estimate of how much
damage a location has historically caused, adjusted for weather, season, and who went in last time.
  Grade I      feral
  Grade II     dangerous
  Grade III    lethal to the unprepared
  Grade IV     lethal to the prepared
  Grade V      town-ending
  Grade VI     unclassified — see NAMED

THIS IS THE WHOLE PRACTICAL DIFFERENCE FROM THE OTHER PROJECT: a rank tells you what a person CAN
survive. A grade tells you what a place HAS KILLED. They are not comparable, and any adventurer who
tries to compare them dies, and the Guild's training material says so on the first page.
""")

add(MST, 65, "MST-01 :: Beast-kin and lesser creatures",
    ["goblin", "bandit", "wolf", "lesser beast", "pack beast"],
    content="""
[ LESSER CREATURES ]   Site Grade I - II

THE PREDATORS: Rift-hounds (fast, cowardly alone, dangerous in threes), marsh-lurkers (ambush from
water, slow on land), ash-crows (single, filthy, will follow a person for eleven miles).

THE AMBIENT FAUNA: everything else. VYRENN has normal animals and they are normal animals, and the Rift
has not touched them, which is genuinely strange and nobody has a satisfactory explanation.

THE PEOPLE-PROBLEM: the great majority of things that kill contract parties in Grades I and II are not
monsters. They are bandits, desperate peasants, and unlicensed men. The Guild knows this and still
prints the monster chart, because the monster chart is easier to read than the census.
""")

add(MST, 66, "MST-02 :: Constructed and blighted creatures",
    ["construct", "golem", "blight creature", "husk", "animated"],
    content="""
[ CONSTRUCTED AND BLIGHTED ]

GOLEMS — bodies built around a mana core. No panel. Predictable, immensely strong, and completely
stupid. A golem does not adapt mid-fight, which means it loses to anyone who adapts once and keeps
adapting. This is the entire counter to a golem and every competent party knows it.

HUSKS — people. Blighted or drained or Hollowed and then reanimated by something that is not
necromancy, which is illegal and unlicensed and extremely common on the eastern border. A husk has no
panel and no soul-reading, and it moves like the person it was, which is the detail that makes them
worse than golems in every way that matters.

WHY THEY ARE DISTINCT: a construct is a thing. A husk was someone. The Guild classifies them
separately because the paperwork for a killed husk requires a next-of-kin notice, and that paperwork
is the only part anybody argues about.
""")
add(MST, 67, "MST-03 :: Named bosses",
    ["named boss", "boss", "floor boss", "what is a named boss"],
    content="""
[ NAMED BOSSES ]   Site Grade III - IV

A named boss has an individual name in the System's record and a legal hearing attached to it. It is
usually Rank B. It has usually killed more people than anyone currently alive can count.

THE CANONICAL THREE in the Sunderreach:
  THE GNAWER          Rift-born, Grade IV, still active. Named. Not on any map.
  MOTHER KETH VELL    floor-four anchor, Grade III, cleared 219, reappeared 224, cleared again.
  THE INVENTOR        Unclassified. Cannot be located. Has killed four clearing expeditions.

THE INVENTOR IS THE ARGUMENT. Every other named monster in VYRENN can be located by a competent
expedition. This one cannot, has never been photographed, and has been described by four separate
survivors in four mutually incompatible ways. The Guild has had it classified as "hazard,
unattributed" for two hundred years, which is the same classification it uses for the Rift.
""")

add(MST, 68, "MST-04 :: Rift-spawn and far-side creatures",
    ["rift spawn", "rift creature", "far side creature", "demon spawn", "riftborn"],
    content="""
[ RIFT-SPAWN ]

Creatures that came THROUGH rather than grew. Rare, individually dangerous, and legally fascinating
because they are the only things in VYRENN with NO PANEL and NO SITE GRADE — the Guild has no
instrument for them and has formally declined to invent one.

A Rift-spawn is not a dungeon monster. It is not generated by the healing process. It came from
somewhere else and it is here, and every Rift-spawn in VYRENN is inside a controlled site because the
alternative is worse.

THE CHURCH'S POSITION: Rift-spawn are of the Abyss. THE ACADEMY'S POSITION: Rift-spawn are of the
other side of a tear, which is a geography problem. BOTH are consistent with the observations. The
Demon Court has offered to comment on Rift-spawn three times and has been refused three times.
""")

add(MST, 69, "MST-05 :: Monstrous races and the beast-folk border",
    ["monstrous race", "demonkin hostile", "feral demonkin", "monster race"],
    content="""
[ MONSTROUS RACES ]

A handful of races are, by their own account, monstrous: the Beast-kin of the far Border, the
Rift-blooded, and the feral demonkin who did not make the crossing intact. Every one of them has a
panel.

THIS IS THE SINGLE BIGGEST COMPLICATION IN VYRENN MONSTOLOGY and the Guild will not discuss it: a feral
demonkin has a Rank. The System measures them. Which means the Church's central doctrine — that the
panel is a mark of the divine, and that the divine does not measure the damned — is contradicted by a
classification decision the Guild made without consulting anyone ninety years ago and has maintained
ever since.

THE PRACTICAL CONSEQUENCE: killing a feral demonkin is legally a dungeon clear. Killing a demonkin
with a panel is legally a murder. The Guild has refused to clarify the distinction and has advised
all parties to consult the Church, which is widely understood to be a joke.
""")

# ============================================================================
# FACTION — 8 entries
# ============================================================================

add(FAC, 70, "FAC-00 :: The Adventurer's Guild",
    ["guild", "adventurers guild", "guild hall", "exams", "rank board", "licence"],
    content="""
[ THE ADVENTURER'S GUILD ]

Issues Ranks, licences, and class exams. The only body in VYRENN permitted to read a panel without
consent, and the reason a half-identical bureaucracy exists in every city on the continent.

STRUCTURE: local boards feeding regional Halls feeding the Central in Hallspath. A licence issued in
one province is honoured in all of them. This is the Guild's single genuine public good and it is the
reason anyone believes the rest of what it does.

COMMERCIAL FUNCTION: it holds a practical monopoly on dungeon licences, and a dungeon without a licence
is a dungeon no insurer will pay for. The Guild knows this. It has never pretended otherwise and it
has never fixed it.

THE UNCLASSED AND THE GUILD: an Unclassed cannot be licensed, inducted, or examined. The intake clerk
at Hallspath's Middle board has refused Ryl Ansel three times, using identical wording each time, which
is either a kindness or a professional habit.
""")

add(FAC, 71, "FAC-01 :: The Holy Church",
    ["church", "the church", "priesthood", "holy", "templars", "brand", "curse lifting"],
    content="""
[ THE HOLY CHURCH ]

Teaches that the panel is a divine gift. Administers marriages, burials, Curse-lifting, and the Brand
rite. Its structural advantage: it is the only institution with a claim on a person's SOUL, and there is
no counter-institution in VYRENN with that claim.

POWER: controls Rift-adjacent mana through its monopoly on Well-custody, which it justifies
theologically and enforces militarily.

THE PRACTICAL DIVIDE: two Churches exist. The institutional Church, which is rich, comfortable, and
administrative. The border Church, which is poor, itinerant, and does most of the actual healing. The
Border Church is beloved. The institutional Church is obeyed. These are different populations with the
same name and irreconcilable politics.

WHAT THEY WANT: the Rift closed, permanently, on theological grounds that would cost three nations their
entire mana supply. They have never said this out loud in a room with a Mage.
""")

add(FAC, 72, "FAC-02 :: The Vyr Academy",
    ["academy", "the academy", "mage college", "study", "arcane school"],
    content="""
[ THE VYR ACADEMY ]

Studies the System without worshipping it. Entrance requires a licence and money; in practice it takes
both and neither is negotiable.

CAMPUSES: Hallspath (main), the Archipelago (second — the only place that will host it without
permission), and a contested third that has been closed and reopened four times.

THE METHOD: the Academy teaches that the panel is a natural law with no author, and supports this with
the strongest available evidence — that the System reports identically for demons, for Undead, and for
things in the Dead Lands that were never alive to be given anything. This is not a theological argument.
It is a data argument, and it is correct.

WHY IT MATTERS TO RYL: the Academy is the only institution that would pay real money to understand
[REGISTRY]. It is also the only institution that would, having understood it, own it. He has decided
that he would rather be poor and unexplained. He has not been able to articulate why and this is the
closest he has got.
""")
add(FAC, 73, "FAC-03 :: The Demon Court",
    ["demon court", "demon politics", "court of the demon continent", "the other side"],
    content="""
[ THE DEMON COURT ]

The governing body of the Demon Continent. Not a war machine — a very old, very rich, very stable
aristocracy with excellent records and no interest in conquest.

ELEVEN-YEAR QUESTION: the Court has not moved against the Sunderreach in eleven years. Both sides have
a theory. Neither will state their theory where the other can hear it.

WHY THEY WOULD TELL YOU, ON THE RECORD: the Demon aristocracy are the only beings in VYRENN with no stake
in the panel question, because their mana works exactly as everyone else's does and they are
constitutionally unbothered by the metaphysics. Asked directly whether the System has an author, the
Court has stated four times that this is an interesting question and declined four times to answer it.
Nobody believes the declination. Nobody can prove it was false.

THE DEMON INVOLVEMENT nobody mentions: the Court funds a deep-clearance research programme in the Dead
Lands. It has been running for nineteen years. The Guild has never inspected it and has been asked to
twice.
""")

add(FAC, 74, "FAC-04 :: The Noble Houses",
    ["nobles", "houses", "nobility", "aristocracy", "the great houses", "court"],
    content="""
[ THE NOBLE HOUSES ]

About four hundred great and greater houses, most of them with less money than a successful licensed
adventurer and more legal standing than everyone in this list.

THE REAL POWER: land, marriage, and the right to raise men. The Crown cannot raise men without the
great houses. This has been the structural fact of Sunderreach politics for two hundred years.

THE ONE LAW THEY OBSERVE: a noble may lose their Rank in the field and it stands. Rank-by-duelling is
legal, extremely common, and the fastest route to a violent provincial politics that nobody with an army
wants.

HOW THEY TREAT THE UNCLASSED: not with hatred. With total indifference, which the Unclassed find worse
and describe better. Nobody in any great house has ever declined a contract on principle and nobody has
ever asked the Unclassed a question. The Guild keeps a memorial to a great house that broke the pattern.
It has one name on it.
""")

add(FAC, 75, "FAC-05 :: Merchant Compact and Enchanters' Compact",
    ["merchants", "compact", "enchanters", "trade", "market", "arms dealers"],
    content="""
[ THE MERCHANT COMPACT ]

The guild structure that moves wealth across the Sunderreach. Legally a Compact, functionally a
monopoly. No major trade in VYRENN occurs without a Compact licence, which means every transaction in
the world has a counterparty who knows it happened.

THE ENCHANTERS' COMPACT is the specialised branch that matters to adventurers. It licenses enchantment,
which is the only way to put lasting magic on gear, which makes every party in VYRENN dependent on it in
a way that cannot be substituted.

THE COMPACT AND THE UNCLASSED: an Unclassed cannot buy an enchantment, sell an enchantment, or have one
inscribed. Ryl's one decent coat has a plain maker's mark on the inside seam and no enchantment, and he
could not afford the cheapest possible rune-work and has priced it.
""")
add(FAC, 76, "FAC-06 :: Mercenaries, the Unlicensed Trade, and the Grey",
    ["mercenaries", "grey market", "unlicensed trade", "poachers", "black market"],
    content="""
[ THE UNLICENSED TRADE ]

Everyone the Guild will not licence, working together, in an economy the Guild cannot reach.

THE GREY MARKET: unlicensed enchantment, unlicensed Magic, unlicensed medicine, forgery of class
certificates, and the buying of unlicensed class-certificates being the single most common crime in
Hallspath. It is unenumerable because it is not a market so much as a status.

MERCENARY BANDS: the armed wing of the same economy. Unlicensed because there is no licence to hold and
no insurance. A mercenary band's word is worth exactly nothing in court and exactly everything on a
battlefield, and VYRENN has lost two wars to bands whose members could not afterwards be prosecuted.

THE PRACTICAL CONSEQUENCE FOR RYL: his entire life is in this economy. Every job he has had in three
years was under it. The Grey Market is not a criminal class he has avoided; it is the economy he
participates in, and this is the reason he is alive and the reason he cannot sleep.
""")

add(FAC, 77, "FAC-07 :: The Rift-cults",
    ["rift cult", "cults", "rift followers", "the wound cult", "doomsday"],
    content="""
[ THE RIFT-CULTS ]

Fourteen registered Rift-cults across the Sunderreach, ranging from four people in a shed to a
forty-thousand-member movement in the eastern marches. All hold the same core doctrine: the Rift is the
wound through which the world is healing, and the Church is holding it shut.

THE INSTITUTIONAL POSITION: the Guild registers them and licenses nobody among them. They are the only
licensed bodies in VYRENN with a doctrine the Church calls heresy and the Guild calls a filing category.

WHY THEY MATTER: two of them are led by people with actual evidence, and both have been unable to
present it in a form any institution will accept. One has been trying for eleven years. The Church has
attempted to discredit all of them and has, repeatedly, by arresting the wrong people.

THE POINT NOBODY WANTS: the Rift-cults are the only group in VYRENN that has been consistently right
about something for two hundred and forty years, and they are right about the Rift, and nobody has
proved it. Their internal dispute is whether closing the Rift would heal the world or kill it, and they
have been arguing about this since before the Church existed.
""")

add(FAC, 78, "FAC-08 :: The Border Traffic",
    ["slavery", "slavers", "trafficking", "captive", "slave trade", "debt bondage"],
    content="""
[ THE BORDER TRAFFIC ]

The buying and selling of people is illegal everywhere in the Sunderreach and practised on the eastern
border continuously. This is stated plainly because Ryl has lived near it for three years and
pretending otherwise would be a kind of lying.

THE MECHANISM: debt bondage, which is legal and which is the whole of it. An Unclassed person with a
debt is a bonded person, and the law is scrupulously even-handed about this in a way that produces the
result on purpose.

WHO IS TAKEN: the Unclassed, the Half-bloods, and the beaten. Nobody takes a licensed adventurer
because a licensed adventurer has a paper trail and a Guild that will look for them. The entire traffic
is aimed precisely at the population the Guild has decided not to count.

WHY RYL IS NOT IN IT: he has no skill worth selling and no affinity an assessor would price. He works
this out in his second year and has been quietly careful ever since. He has not told anyone that he
works out how the traffic selects its victims, and if he ever does, it will be to someone who is not
{{char}}.
""")
# ============================================================================
# CULTURE — 7 entries
# ============================================================================

add(CUL, 79, "CUL-00 :: Society, work, and the meaning of a rank",
    ["society", "culture", "what is rank worth", "social standing", "how society works"],
    content="""
[ SOCIETY ]

VYRENN is a world where your legal status is a number everyone can see, and where most of what people
actually care about is decided by a committee you have never met.

RANK IN PRACTICE: Rank determines whether you can be held to a contract, whether you can be sued, and
whether you can be conscripted. It does NOT determine wealth directly — it determines access to the
licences through which wealth is made. Most working VYRENN lives in a narrow band around Rank C, and the
band is wide enough that "C-rank" is not a useful thing to know about someone.

WORK: unlicensed labour is cash and silence. Licensed labour is a licence, a rate, and a record. A
  person with no licence has no rate and no record, which means no leverage in any dispute, ever.

MANNERS: people ask about rank early and directly. It is not considered nosy; it is considered
  practical. Ryl has been asked his rank perhaps two hundred times in three years and has answered
  honestly every time and it has never once helped him.
""")

add(CUL, 80, "CUL-01 :: The economy and money",
    ["economy", "money", "currency", "coin", "gold", "price", "poor"],
    content="""
[ ECONOMY ]

The unit is the mark. Marks are minted by the Merchant Compact against Guild-licensed activity, which
means money in VYRENN is not a general claim on goods — it is a claim on SPECIFIC licensed work.

THIS IS THE CENTRAL ECONOMIC FACT and it is why the Unclassed are poor in a way that cannot be fixed by
earning more. Marks earned from unlicensed labour are not marks. Marks from licensed work are. A
person can starve while holding money.

PRICES: a room in the Middle district is about twelve marks a month. A Grade I licence is forty. A
  class exam is two hundred. An enchantment is not priced because it is not for sale to you.

WHAT RYL COULD EARN if licensed: enough. What he earns: about one mark a day, most of which goes on
  the room and the food, which is the entire arithmetic of a three-year decision not to leave.
""")

add(CUL, 81, "CUL-02 :: The gods and what the Church does with them",
    ["gods", "the church gods", "pantheon", "faith", "theology", "does god exist"],
    content="""
[ THE GODS OF VYRENN ]

Nine names the Church honours. Their natures are matters of local tradition and the Church has never
issued a definitive list, which is either humility or strategy.

THE NINE, as commonly named: the Witness, the Wound, the Gate, the Deep, the Labour, the Hearth, the
Debt, the Silence, and the Name-That-Is-Not-Spoken.

THE PROBLEM FOR THE ACADEMY: the Church's rites demonstrably work. Not symbolically — the Brand binds,
Curse-lifting clears, exorcism sometimes succeeds. The Academy's position is that these are SOFT magic
performed by people who have spent forty years learning them very well, and this is consistent with
everything observable.

THE PROBLEM FOR THE CHURCH: the same rites work equally well for a Cleric who does not believe, which
should not happen if a deity is doing the work. Nobody has ever established that it should not happen,
because testing it requires a willing unbeliever in a position of power, and nobody volunteers for
that experiment.
""")

add(CUL, 82, "CUL-03 :: Daily life, food, and the absence of adventure",
    ["daily life", "food", "what is normal", "ordinary life", "boring", "money problems"],
    content="""
[ ORDINARY LIFE ]

Most of VYRENN is not adventuring. It is transport, cooking, weather, rent, and small resentments. The
Guild's ratio is roughly one licensed adventurer per two thousand people, and the fantasy of a life
spent fighting monsters is not how most people in VYRENN have ever lived.

FOOD is regional and mostly grain. Salt is the expensive part inland. The Guild does not license
  cooking and the Church does not bless it and this is neither contested nor interesting to anyone.

DRINK: the Unclassed quarter in Hallspath has a licence-free drinking establishment that has been
  operating since before the Rift was studied, and which the Guild has never closed and cannot
  explain.

WHY THIS MATTERS FOR PLAY: an Unclassed 19-year-old's day is labour, food, rent, and the queue at the
  notice board. If a scene does not sound like that, the character is not in the world being described.
""")

add(CUL, 83, "CUL-04 :: Marriage, family, and the half-blood question",
    ["marriage", "family", "half-blood children", "inheritance", "weddings"],
    content="""
[ MARRIAGE AND FAMILY ]

Civil marriage is a Guild function. Religious marriage is a Church function. Most people do both, in
that order, and the Church's version is the one that matters for anything involving a Brand.

INHERITANCE requires a Rank. This is the mechanism by which half-bloods are poor: they may not inherit
  land, so they work, so their children work, and the Guild's reform committee has had a clause to fix
  this drafted since before anyone currently in the Quarter was born.

THE HALF-BLOOD QUESTION is the loudest unresolved political question in VYRENN. Half-bloods are legally
  second-tier: no licence above Rank D, no Academy, no inheritance, double temple tithe. Their single
  demand is that half-blood status require two differing parents rather than one visible one, which
  would end most of it. It has been refused every session for ninety years on procedural grounds.

THE PANEL'S POSITION is the interesting one: a panel reports a half-blood's stats and race with total
  neutrality. The System does not know what they are and does not care. That single fact is now the
  central text of the movement.
""")
add(CUL, 84, "CUL-05 :: The Border, and why it is loud",
    ["the border", "frontier", "east", "raids", "displacement"],
    content="""
[ THE BORDER ]

The eastern edge, where the Rift mouths are, the land is poor, and the population moves every year.
It is the loudest place in VYRENN and the least listened to.

DISPLACEMENT is the actual political fact: two million people have moved west in forty years and there
is no policy for it. The cities that absorbed them did so because they could not refuse. The Quarter in
Hallspath is what that looks like at the bottom of the ladder.

THE RAID QUESTION: raids from the east are real, seasonal, and partly manufactured. Both the Empire and
  the Guild know this. Neither will say so publicly, because the alternative is admitting that the Dead
  Lands are failing faster than anyone has said, and that would start something.

WHY RYL IS THERE: he came west. Everyone who has worked in the Quarter for three years came from
  somewhere worse, and he is not the exception there, he is the median.
""")

add(CUL, 85, "CUL-06 :: The Academy's price, and why nobody pays it",
    ["academy price", "why is the academy closed", "class", "who gets to learn"],
    content="""
[ THE ACADEMY'S PRICE ]

The Academy is free. The Academy is also impossible.

THE ARITHMETIC: entry requires a licence. A licence requires four years of indentureship to a master,
during which you are unpaid. At the end you need a class exam costing roughly two hundred marks. On a
licensed wage, this is a decade of your life and most of what you earned.

THE ACADEMY'S OWN PUBLICATION, quoted in every argument: "Talent is free. The fee is irrelevant."
  This is technically true and practically false, and the Academy knows it, and the Academy's internal
  reform movement has been saying so since before it was founded.

FOR RYL: he has read the Academy's public introductory texts. They are free and they are on the public
board. He has learned more about mana from them than from anything else in his life, which is a
specific kind of insult and he has made his peace with it.
""")

# ============================================================================
# ISEKAI — 6 entries
# ============================================================================

add(ISE, 86, "ISE-00 :: Otherworlders, and why the Church fears them",
    ["isekai", "otherworlder", "otherworld", "summoned hero", "from another world"],
    content="""
[ OTHERWORLDERS ]

People from outside VYRENN. The Church has an entire administrative apparatus for them. The Guild has
one form. The Academy has banned their study.

WHY THE FEAR: an Otherworlder arrives with no licence, no record, no registered affinity, and — this is
  the part the Church actually cares about — a panel that may or may not be legible. The Church's
  position, that such a person is unaccountable to any human authority, is not unreasonable and is not
  usually challenged.

THE REGISTRY: the Church maintains one. Names, arrival date, arrival method, and a class assignment
  made by a senior priest who has never met the subject. The Registry is largely empty because there
  have been four arrivals in two hundred and forty years and one of them is a rumour.

WHAT THEY TEND TO BE LIKE: overpowered, underinformed, and violently careless with local politics.
  Every one of the four who arrived badly and died badly, and this is not a coincidence and the Church
  has never had to say so out loud.

REFERENCE: Ryl Ansel arrived three years ago by an uncatalogued method and is not in the Registry,
because nobody asked and he did not volunteer.
""")

add(ISE, 87, "ISE-01 :: Transmigration — Ryl's method",
    ["transmigration", "transmigrated", "how did he get here", "his method", "reincarnation"],
    content="""
[ TRANSMIGRATION ]

The rarest and least documented of the four methods: death elsewhere, waking here in a body that
already existed. The Church does not record it because it does not recognise it, which is the same
thing, in the Church's case, as not existing.

THE DISTINCTION FROM REINCARNATION: reincarnation returns the same soul to a new VYRENN body, weaker,
  with memories of the last life. Transmigration imports a soul from OUTSIDE, and the mechanism is not
  understood by anyone including the Church, which has made four official attempts to classify it.

WHY IT IS DANGEROUS: an imported soul has no foundation. No registered affinity, no training, no
  language at first, and no way to acquire any of them through legal channels. Most transmigrants
  discovered in VYRENN history died within two years. The Guild considers the category a public-health
  concern. The Church considers it a heresy. Both are, for once, describing the same thing.

RYL'S THREE YEARS: he learned the language, learned the licensing rules, learned what an Unclassed is
  legally permitted to do, and did not find a return protocol. He has looked for one for three years.
  He has told nobody.
""")
add(ISE, 88, "ISE-02 :: The summoning rite and the Church's authority",
    ["summoning", "summoner", "rite of summoning", "church summoning", "hero"],
    content="""
[ THE RITE OF SUMMONING ]

The only institutionalised Otherworlder method. The Church performs it, the Church registers it, and the
Church is therefore the only body on the continent with a practical monopoly on bringing people in.

THE RITE requires: a High Cleric, a Rift-adjacent site, a live anchor object, and a name. It takes
between eleven and forty days. It has succeeded four times.

THE COST IS NOT IN MONEY. It is that the summoner binds themselves to the outcome. A summoner who
brings back someone incapable is liable under Church law for the spiritual damage — which is why
clerics do not summon lightly, which is why the four arrivals were all deliberate, and which is the
reason the Church's stated fear of Otherworlders is not remotely consistent with its actual practice of
bringing them here on purpose.

THE SYSTEM'S INTEREST: the Church has never explained why the System produces panels for people who
were not in VYRENN when it started. This is the strongest evidence the Church has for its own
doctrine and it has never used it publicly, which has kept the Academy's counter-argument alive.
""")

add(ISE, 89, "ISE-03 :: Reincarnation, and the limits of the panel",
    ["reincarnation", "reborn", "second life", "souls", "after death"],
    content="""
[ REINCARNATION ]

Death and return. The Academy accepts the mechanism and denies the metaphysics. The Church accepts
both and has the Ritual.

WHAT REINCARNATION IS CONFIRMED TO DO: the returned soul retains memory, retains some capability, and
  begins weaker. The weakness is the practical part — a soul returning at reduced capacity is the reason
  VYRENN's dangerous occupations have a real average lifespan.

WHAT NOBODY CONFIRMS: whether the soul is the same soul. The Church says yes, definitively, and
  administers marriage and inheritance on the basis of the answer. The Academy says the data does not
  support it and has been asked repeatedly to publish and has not.

WHY THE GUILD CARES, and why this entry exists: a returning soul presents as a young person with an
  old person's memories, and a young person with an old person's memories who cannot produce a
  licence history is, formally, an Unclassed. The Guild has quietly reclassified four such people as
  Rank D by administrative exception over two centuries, and has never publicised the exception, and
  every one of the four is a person who has tried to explain why they know things.

RYL HAS CONSIDERED REINCARNATION CAREFULLY, because it is the only one of the four methods that might
  be available to him without a Rift, and it is not, because he did not die HERE.
""")

add(ISE, 90, "ISE-04 :: The return protocol and the four who did it",
    ["return protocol", "can he go home", "going home", "two who came back", "escape"],
    content="""
[ THE RETURN PROTOCOL ]

Officially it does not exist. Unofficially three people are recorded as having returned to their world of
origin, and two of them came back.

WHAT THE TWO CAME BACK WITH: nothing measurable, and everything. Both are documented in the Academy's
  sealed file. Both describe a place with no panel, no mana, no ranks, and no way to check any of those
  claims. One of them described it in language the Academy's translators had to invent.

THE FAILURE MODE: the one who did not return. The Academy's note is four words long and reads: "Returned
  during transit. Cause unestablished."

WHAT THE ACADEMY CONCLUDES, publicly: that crossing is possible, that it is survivable, and that it is
  not repeatable. WHAT IT CONCLUDES privately, and does not publish: that the protocol appears to
  require being remembered by something on the far side, and that nobody who tried it was known by
  anything.

RYL'S POSITION: he has read the sealed file. He is not close to satisfying any known condition. He has
not told anyone he is looking, and if he ever mentions this to another person, it should be a decision,
not an accident.
""")

add(ISE, 91, "ISE-05 :: The two centuries since the First Calamity",
    ["timeline", "chronology", "history of otherworlders", "four arrivals", "the last century"],
    content="""
[ TWO CENTURIES OF RECORDED ARRIVALS ]

THE FOUR DOCUMENTED ARRIVALS:
  THE FIRST      34 years ago. Summoned. Untestable. Left VYRENN within a year and the Church has
                 maintained for thirty-four years that she went home and is alive, which is a claim
                 nobody can check and everybody repeats.
  THE SECOND     96 years ago. Summoned. Trained, licensed, ranked, and served for eleven years as an
                 officer in the eastern campaigns. Died at rank. The only Otherworlder the Guild has
                 ever formally honoured, and the precedent that makes the other three survivable.
  THE THIRD      201 years ago. Uncatalogued method. Died within two years. The Registry records her as
                 "inadmissible".
  THE FOURTH     119 years ago. Rumour only. No panel, no record, no arrival the Church will admit.

THE PATTERN, stated plainly because it is the actual text of this setting: two survived and both were
brought here deliberately by an institution that then had the resources to keep them alive. None of the
ones who arrived alone has done well.

IF {{char}} IS CONSIDERING TELLING SOMEONE HE IS NOT FROM HERE: the Guild will want to know. The Church
will want to know. The Academy will want to know very badly. These are three different conversations
with three different costs, and they are not compatible with each other.
""")
# ============================================================================
# ITEM — 5 entries
# ============================================================================

add(ITM, 92, "ITM-00 :: Equipment, crafting, and the enchantment economy",
    ["items", "equipment", "gear", "weapon", "armour", "loot", "crafted"],
    content="""
[ ITEMS ]

A party's strength is its equipment, and its equipment's strength is its enchantments, and its
enchantments' strength is its budget. This is not a joke; it is the entire adventure economy.

CRAFTING: the Compact licenses every crafter who works with mana. Weapons, armour, and goods are
channelled or not, and a channelled item draws mana continuously and must be paid for monthly. Nobody
in VYRENN discusses this and everybody budgets for it.

THE LICENCE QUESTION: an Unclassed may not purchase, sell, or commission a licensed enchantment. This
  is enforced on the enchantment and not on the trade in goods, which is why the market in unlicensed
  goods is enormous and the market in unlicensed enchantment is merely criminal.

WHY IT MATTERS FOR RYL: he has a plain maker's mark on his one decent coat, no enchantment, and a habit
of reading the enchantments on everyone else's gear — a habit that has saved his life twice and that
he has no way to explain to anyone.

THE ITEMS HE CANNOT USE: anything licensed. His one licensed-grade item is a Guild-issue measuring rod,
issued because assessing panels is his job, and he cannot carry it as a weapon.
""")

add(ITM, 93, "ITM-01 :: Skill stones and rift-cores",
    ["skill stone", "rift core", "core", "levelling", "how do you get skills"],
    content="""
[ SKILL STONES AND RIFT-CORES ]

The two materials that matter, and the entire reason people clear dungeons at all.

A RIFT-CORE is the crystallised energy at a dungeon's heart. It is inert, valuable, and does nothing for
  a person by itself. Sold to the Academy for research or to the Church for Well-custody.

A SKILL STONE is not a core. It is a fragment of mana that has taken a shape, and the shape is a
  technique. Break one correctly and you have learned the technique in it. This is the ONLY reliable
  route to a new skill in VYRENN and it is why clearing dungeons is a profession rather than a hobby.

THE COST OF A STONE: they drop from Grade II and above. Grade III and above reliably. Grade V and above
  have dropped six in two hundred and forty years and the Academy has catalogued all of them.

THE UNCLASSED PROBLEM: you cannot legally hold a broken stone. Possession of a skill fragment without a
  class licence is unlicensed attunement, and the Academy has a legal and completely unpractical
  position that all six of the Grade V stones should be sequestered. Nobody disagrees. Nobody who wants
  one is going to stop.
""")

add(ITM, 94, "ITM-02 :: Legendary and the hard cost",
    ["legendary", "relic", "unique item", "named weapon", "great item"],
    content="""
[ LEGENDARY ITEMS ]

A legendary in VYRENN is defined by its cost, not its power. Any item can be powerful; the ones that
last have a permanent price.

THE FIVE KNOWN, in brief:
  THE GREY BOLE — a Guild assessor's rod that does not lie. Cost: it shows you exactly what you can
    survive and cannot be traded or given away, and it takes a small part of the wielder's judgement.
  THE PATIENT ROOM — a soul-copper set that gives a healer three times the mana. Cost: the patient
    does not remember being healed, and neither does the healer, and there is a documented case where
    that mattered badly.
  THE QUIET HOUR — a time-effect that buys four minutes. Cost: it takes them from somewhere else in
    the future, and the Academy has determined the exchange rate is not a flat one.
  THE INVENTOR'S REMAINDER — a core fragment that will not decay. Cost: it decays the holder.
  THE UNNAMED — a legendary nobody may speak about, registered by the Church, which is the only
    institution in VYRENN that both knows it exists and refuses to say.

THE RULE: no legendary is a clean upgrade. A person whose life has been made longer by a legendary is
not, in the end, better off. They are further along.
""")

add(ITM, 95, "ITM-03 :: Cursed items",
    ["cursed", "curse", "cursed item", "trapped item", "penalty item"],
    content="""
[ CURSED ITEMS ]

An item that improves one thing and takes another. The curse is not a punishment from outside — it is
  the price, and the item is honest about it: every cursed item declares its cost in plain text on its
  face. Buying one is a considered act.

THE LEGAL FRAME: the Church licenses cursed items and levies a tax on them. A Church official described
  the arrangement as "a way of making people pay for their own bad ideas", and this is the closest thing
  to an honest official statement in VYRENN.

WHY THEY EXIST: because VYRENN is a world with no training curve. A level-30 clerk and a level-12 thug
  who spent three years taking a cursed blade are, in the terms that matter, dangerous to each other.
  Most curses are a way of letting the desperate be good at one specific thing.

WHICH ARE WORTH IT: a Mender with a bleed-cursed blade and a Warden with a short-life shield are both
  genuinely good at their jobs and both will be dead young. This is not a cautionary tale. It is the
  most common shape of an ambitious person's career in VYRENN.
""")
# ============================================================================
# RULES — 3 entries
# ============================================================================

add(RUL, 96, "RUL-00 :: Power scaling and the anti-ladder rule",
    ["power scaling", "who wins", "can a lower rank win", "combat rules", "balance"],
    content="""
[ POWER SCALING — APPLIES IN EVERY FIGHT AND EVERY ARGUMENT ]

In VYRENN, combat is decided by CONDITIONS, not by numbers.

  A C-rank who has studied one species' weakness for two years reliably beats a B-rank on their first
  sighting. Numbers describe what someone can SURVIVE. They do not describe who WINS.

WHY THIS IS THE RULE AND NOT A CONVENIENCE: the Guild licenses on preparation and records on outcomes.
A party that wins badly for three years and wins cleanly in the fourth has done the thing the system
rewards, and the whole institutional design depends on that being true. If rank determined outcomes,
licensing would be pointless and the Guild would know it.

TERRAIN: a doorway, a narrow stair, a shoreline, and the dark all beat numbers. This is not folklore.
It is the most common cause of death among licensed adventurers and it is in the training manual.

TERMINATION: everyone in VYRENN can eventually stop. Most fights in this world are ended by somebody
  deciding to leave, and the ones that are not are the ones the Church records.
""")

add(RUL, 97, "RUL-01 :: What a panel can and cannot tell you",
    ["what can a panel tell", "panel limits", "can you tell if someone lies", "read someone"],
    content="""
[ WHAT A PANEL CAN AND CANNOT TELL YOU ]

A panel reports CAPACITY. It does not report character, and the world's institutions have known this
for two hundred and forty years and have built anyway.

A panel CAN tell you: what someone can survive, roughly what they are good at, whether they are
  licensed, and whether they are currently lying to you — because the System cannot report a falsehood
  without flickering, and an Assessor can see it.

A panel CANNOT tell you: whether they are loyal, whether they will help you, whether they will run, or
  whether they are telling the truth about anything that is not their own body.

THE STRATEGIC CONSEQUENCE: a B-rank who has never betrayed anyone is a liability, and a D-rank who will
not leave is an asset, and neither fact is available on any panel in the world.

[REGISTRY] IS NOT AN EXCEPTION TO THIS. It shows the same panel, larger. It has never once shown Ryl
what a person is, and he has stopped expecting it to, and this is why he reads people and then has to
ask them anyway.
""")

add(RUL, 98, "RUL-02 :: Transcendent, and why the Guild will not say the word",
    ["transcendent", "above sss", "the highest rank", "god-kin", "what is transcendent"],
    content="""
[ TRANSCENDENT ]

Not a rank. Not a band. A category the world has no slot for.

Two confirmed in living memory. Both devout according to the Church and impossible according to the
Academy. The Guild does not publish the category and does not issue licences for it, and when pressed
says that there is no such rank, which is true and is not an answer.

WHAT IS ESTABLISHED: that both cases involved a person of ordinary birth who, over a period of years,
  exceeded every band and then stopped being measured by the method. Neither is described further.
WHAT IS NOT ESTABLISHED: whether they are alive, whether either is the same person twice, whether the
  word describes a person or a process, and whether the Guild has a procedure that it has simply
  chosen not to run.

THE WORD IS NEVER USED BY THE CHURCH, which is the loudest signal in the setting: the Church has a
category for everything else it disapproves of, and has never coined one for this, and the Academy has
coined exactly the one word it will not use.

THE OPENING FOR {{char}}: this is the highest-register rumour in VYRENN and it is not, in fact, on his
list of things he is willing to speculate about out loud. If he ever raises it, it should be because
something has made it relevant, not because it is interesting.
""")