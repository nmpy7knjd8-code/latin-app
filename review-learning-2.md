# Review 2: revised learning-cards.json (65 cards) + learning-stories.json (10 stories)
_Reviewer agent, Oct 13 2026. Grammar sequence checked against the current game-design.md: U1 sum and 1st-decl. nominative · U2 1st/2nd decl. nom/acc · U3 1st/2nd conj. present · U4 gen/dat and adjectives · U5 3rd decl. and prep + abl · U6 imperfect, perfect and possum · U7 future, pronouns and imperative · U8 infinitives and indirect statement · U9 passive · U10 relatives._

## A. Pass/fail on review-learning.md
| # | Item | Result | Notes |
|---|---|---|---|
| 1 | Seneca 96.5 wording | **PASS** | *Atquī vīvere, Lūcīlī, mīlitāre est.* |
| 2 | g-impf had no imperfect | **PASS** | It now has two constructed imperfects. Suetonius stays in the context only. |
| 3 | g-imperative era | **PASS** | empire |
| 4 | Real coin legends | **PASS** | IMP·CAESAR·DIVI·F with RRC 538/1, and KAROLVS IMP AVG, both now verified. **Nit:** x-parse-signum (LEG XX VV) is also a real stamp formula, but it's still labelled "Constructed". |
| 5 | g-adj constructed vs cited | **PASS** | |
| 6 | Glosses and vocab_ids | **PASS** | 65/65 cards have a gloss, and none has empty vocab_ids. |
| 7 | Chi-Rho *Alpha et Omega* | **PASS** | |
| 8 | g-future deponent | **PASS** | It now leads with *regam, regēs, reget*. U7 is consistent with the current design. |
| 9 | g-perf-rg U6 | **PASS** | Under the current design the perfect is taught in U6. |
| 10 | Images and licences | **PASS** | Every card has a real image now: 29 PD, 4 CC0, and 32 CC BY / BY-SA (2.0–4.0). The credits name the author (e.g. Mike Peel, Sailko, Carole Raddato). The Vindolanda image is no longer a BM photo. **Remaining:** the BY-SA cut-outs need "modified" noted, and the credits page must give the licence version per file (2.0, 3.0 and 4.0 are mixed). |
| 11 | x-meter elision | **PASS** (engine) | Verse mode exists; see review-phonetics-2. Check that the meter card actually uses `ipa_verse`. |
| 12 | l-bulla agreement as preview | **FAIL** | `grammar_preview` is still None on l-bulla, a U2 card, even though agreement is taught in U4. |
| 13–15 | Nits | **PASS** | The signum translation is now English. "who are" is now used throughout. The g-acc emphasis note is added. |

## B. The 10 stories (Latin and unit fit)
The Latin is grammatical throughout and the macrons are correct (*Palātiō, Cūriā, sacerdōs, quadringentēsimō, monastēriō, Ēvangelium*). Each story is listed with forms beyond its unit.

| Story | Grammar fit | Issues |
|---|---|---|
| U1 Rōma | **Mostly fits** | *In urbe* (3rd decl. + abl., U5) and *in Palātiō* (abl.) are beyond U1, as are the adjectives *mala/bona/magna/longa* (U4). Mark *in + abl.* as a glossed chunk ("in the city"). Adjectives as predicates are hard to avoid in U1. Tag them as preview. |
| U2 Familia | **Fits** | *Haec* is a preview. **Consistency:** *ornāmenta* here, but rome-cards has *ōrnāmenta*. Settle on one. |
| U3 In castrīs | **Fits for verbs** | Nouns: *mīlitēs, centuriō, legiō* are 3rd decl. (U5), and *in castrīs* is abl. These are unavoidable in a Legion story. Teach them as vocabulary chunks (nominative and accusative plural *mīlitēs* look the same, which helps). Good: this partly fills the empty U3 rome unit. |
| U4 In Forō | **Fits** | The datives *senātōribus*/*Cicerōnī* are good. *rem pūblicam* is 5th decl.; gloss it as a chunk. **Accuracy nit:** "Senātus in Cūriā est" is fine generally, but the Catiline speech happened in the Temple of Jupiter Stator (review-1 #1). Keep the story from implying the speech was in the Curia, or add a line: *Cicerō in templō Iovis Statōris dīcit*. |
| U5 Templum Vestae | **Fits well** | **Should-fix:** *Ex templō aqua nōn venit, sed ignis* ("from the temple comes not water but fire") is odd. Use something meaningful, such as *Virginēs aquam ex fonte portant* (Vestals did fetch spring water). *ārdet*: same macron policy question as before. |
| U6 Augustus | **Fits** | Imperfect and perfect contrast plus *poterat* is a good fit. *eius*/*eum* are pronouns, which come in U7, so mark them as preview. *Urbem marmoream relīquī* is a fair adaptation, but flag it as adapted from Suet. Aug. 28.3. |
| U7 Poēta | **Fits** | The futures *erō* and *manēbunt* are good. *moriar* is fine as the authentic payoff. |
| U8 Philosophus | **Fits well** | *Dīcit vītam esse mīlitiam* is a clean indirect statement. |
| U9 Rōma capta | **Fits well** | The passives *capta est, territī sunt, laudātur* are good, and so is the ordinal *quadringentēsimō decimō*. |
| U10 Scrīptor | **Fits** | The relatives *quī/quem* are good. **Should-fix:** *Abbās, quī eum vidēbat, laudāvit* has no object for *laudāvit*. Use ***eum laudāvit*** and move the relative: *Abbās, quī monachum vidēbat, eum laudāvit*. |

## C. Dialectic
- **Thesis:** each story strings its unit's constructed sentences into one scene, which is exactly the synthesis review-learning proposed.
- **Antithesis:** six lines of mostly "X est Y" or subject–object–verb sentences is still thin input. Repetition is low, and the ratio of new words is high. The research's 95–98% coverage target can't be met in U1–U3 without heavy glossing.
- **Synthesis:**
  - Grow each story to 12–20 lines in Ørberg style: recycle every new word at least 3 times, and use an image strip for meaning.
  - Lint each story for (a) every form within the unit plus at most one preview, and (b) known-word coverage of at least 90% given earlier units' vocabulary.
