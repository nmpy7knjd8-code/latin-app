# Review 2: revised rome-cards.json (48 cards) against review-rome.md
_Reviewer agent, Oct 13 2026. I checked the 12 new cards against the standard texts. I made a contact sheet of 33 distinct cut-outs on the card red (/tmp/cutouts.png), measured their alpha coverage, and checked the licence and credit fields._

## A. Pass/fail on review-rome.md
| # | Item | Result | Notes |
|---|---|---|---|
| 1 | Catullus 5 context (death, not night of love) | **PASS** | "once our brief light sets, there is one endless night to sleep". |
| 2 | Titus: *Titus* macron, F(ILIO), Vespasiano gloss | **PASS** | Parentheses are now used. |
| 3 | Horace placeholder credit/URL | **PASS** | Both now use real Laurenziana / Commons credits. |
| 4 | Unit/grammar fit | **PASS** (against the current design) | `grammar_preview` has been added. Arma is in U7, Tacitus in U5, Docent in U8, Alea in U6 with perfect_passive as preview. See section C. |
| 5 | *Quintili Vare, legiones redde* restored | **PASS** | Suet. Aug. 23.2. Correctly "traditional" (*ferunt*). |
| 6 | Inflated scores | **PASS** | Historia and Arma were 5 and are now 4. |
| 7 | Horace "Well begun…" | **PASS** | Now "He who has begun has half the deed done". |
| 8 | Odi et amo indirect question | **PASS** | Now "Why I do this, perhaps you ask." |
| 9 | Alea / Erasmus *esto* | **PASS** | |
| 10 | Cedant *laudī/linguae* | **PASS** | |
| 11 | Agricola *atque ubi*, 30.5 | **PASS** | |
| 12 | Unit balance | **FAIL** | U3 has **0** cards, U1 has 2, U2 has 3. U5 has 11 and U7 has 10. See section D. |
| 13 | Images: 1:1, sarcophagus cut-out, .tif, stand-ins, reuse | **PARTIAL** | Every image is now local WebP, with no TODO left. Pseudo-Seneca, lamp-for-Martial and Octavian-for-Exegi are replaced (Exegi now uses a pyramid, which is a good fit). But reuse remains: `img/cicero.webp` ×2, the cuirass for Cēdant. Muses (2:1) and Titus (2:1) are wide strips; they're fine as framed images but need a strip layout. |
| 14 | `tu + -que` vocab id | **PASS** | No "+" left in vocab_ids. |
| 15 | text_verified vs speaker_historicity | **NOT DONE** | Still a single `attribution_confidence`. The notes explain it in prose. Acceptable for now. |
| 16 | Pantheon *Lūcī* | **PASS** | |
| 17–20 | Nits (Ītaliam, 390 BC, salūs motto, Juvenal "it") | not re-checked | low priority |

## B. The 12 new cards
Each card's text and citation was checked against the standard edition.

| id | Text and citation | Result |
|---|---|---|
| q-suetonius-vare | *Quīntilī Vāre, legiōnēs redde!* Aug. 23.2 | ✔ The translation adds "me" ("give me back"), which is acceptable. The image is the **Rufus Sita** tombstone, a Thracian auxiliary cavalryman from Gloucester, not one of Varus's legionaries. Caption it as "a Roman soldier's tombstone (Britain)" so it doesn't imply the Teutoburg dead. |
| i-pompeii-cave | CAVE CANEM, House of the Tragic Poet VI.8.3–5 | ✔ The macron on *Cavē* is right, and it rightly overrides Alatius. |
| i-sttl | S·T·T·L *Sit tibi terra levis* | ✔ *levis* "light" has a short e (*lēvis* means "smooth"), so the producer is right. **Should-fix:** cite one real tombstone (for example a CIL number via EDCS) instead of only Wikipedia, so the "verified" label means something. |
| q-seneca-prope | Ep. 41.1 *prope est a te deus, tecum est, intus est* | ✔ |
| i-spqr | Formula | ✔ |
| q-virgil-tantaene | Aen. 1.11 | ✔ *animīs* is a dative of possession. Add that to the parse. |
| q-ovid-vesta | Fasti 6.267 | ✔ *utrīque* is dat. sg. ✔ |
| q-virgil-musa | Aen. 1.8 *Mūsa, mihi causās memorā* | ✔ **Nit:** it's tagged `indirect_question`, but the *quō nūmine laesō* clause isn't in the excerpt. Drop the tag. |
| q-virgil-facilis | Aen. 6.126 *facilis dēscēnsus Avernō* | ✔ Note that some manuscripts read *Avernī*, and Mynors prints *Averno*. |
| c-brutus-eidmar | EID·MAR, denarius of Brutus 43–42 BC (pileus between two daggers) | ✔ The macrons in *Īdibus Mārtiīs* are right. EID is the old spelling of ĪD-. The catalogue number was removed honestly. Add **RRC 508/3** (Crawford), which is the standard reference. |
| c-octavian-aegypto | AEGVPTO CAPTA, crocodile, 28 BC | ✔ It's an ablative absolute. Standard reference: RIC I² 275 (Octavian denarius). |
| q-ovid-expedit | Ars 1.637 *Expedit esse deōs, et, ut expedit, esse putēmus* | ✔ *putēmus* is right, so keeping it over Alatius was correct. |

**Macronizer overrides:** all 11 kept forms are correct in their context:
- *legis*: present tense, short e.
- *hīc*: the adverb.
- *Agrippa*: nominative.
- *Cavē*, *vēnit* (perfect) and *fugit* (present).
- *putēmus*.
- *ūsque*: long ū in L&S.
- *abūtēre*: future.
- *aere* from *aes*.
- *Trōiae*.

Two of the adopted forms are disputable:
- ***ōrnāmenta***: the vowel quantity is hidden. L&S and OLD give *ŏrnāmentum*, and Allen gives ō before *rn* only on uncertain evidence. Either is defensible, but be consistent: rome uses *ōrn-*, while the medieval cards and game-design use *orn-*.
- ***ānxius***: the long a is by Lachmann-type lengthening before *nx*. Most dictionaries print *anxius*. Both are acceptable; document the policy.

## C. Unit-order conflict (perfect U6, future U7)
game-design.md now reads: U6 "imperfect & **perfect**, possum", U7 "**future**, pronouns, imperative". The producer followed it. My review-rome.md was written against the earlier design (U6 future, U7 perfect).

**Judgement: the producer is right to follow the current design, and the order itself is good.**
- The perfect is far more frequent than the future in the narrative prose learners will read: Caesar, Livy, Suetonius and the *Res Gestae*. Moving it earlier unlocks most of the historical anchors (*vēnī vīdī vīcī*, *gessī*, *comparāvī*).
- Ørberg's *Familia Romana* also brings in the perfect before most future forms.
- **Remaining fix:** learning-cards g-future (U7, now consistent) and the old note in review-learning #8/#9 are superseded. Update the CHANGES log so the critic and the producer are working from one design version.

## D. Images: cut-out QA (33 sheets) and licences
- **Good:** Augustus Prima Porta, Jupiter, Juno, Vesta, Laocoön, the wolf, young woman, woman, boy, Cicero (the cut-out version), soldier, the cup, both coin pairs, Mercury. Their edges are clean on red.
- **Needs a redo:**
  - `tablet.webp` is a dark rectangle that hasn't been cut out. Use framed mode or redo the cut.
  - `romulus.webp` has a faint, ghostly matte, typical of rembg on low-contrast relief. Use a mask instead.
  - `epicurus.webp` is tiny and has a leftover rectangular shadow below it.
  - `seatedmuse.webp` fades out at the bottom.
  - `womanhead.webp` and `cicero2.webp` have pedestal or background residue at the base.
  - `caesar.webp` has a soft vignette at the neck (the same note as review-cards #10).
- **Licence error: CC BY credits are incomplete.** Eight cards use CC BY / CC BY-SA images: q-cicero-salus, q-tacitus-solitudinem, i-pompeii-cave, i-titus-spqr, q-virgil-fugit, c-brutus-eidmar, q-cicero-quousque and q-horace-exegi (CC BY 4.0). Every one has the credit "Wikimedia Commons (CC BY-SA 4.0)" with **no author**. CC BY 4.0 §3(a) requires the creator's name, the licence link, and an indication of changes; the cut-outs are modified. **Fix:** pull `Artist` from the Commons extmetadata into `credit`, and add `modified: "background removed"`.
- **licences.json** only lists 4 entries. Regenerate it for all 48 cards with author, licence and source URL; it is the credits page source.
- **Calgacus image:** `Musee-romanite-guerrier-casque` is a Gallic warrior statue (Nîmes), not a Caledonian. Caption it "Gallic warrior, used as a stand-in".

## E. Dialectic: unit balance
- **Thesis:** follow the grammar sequence strictly. Cards go to the first unit where all their target grammar has been taught. That's what emptied U3 and stacked U5 and U7.
- **Antithesis:** the early units are where learners decide whether to keep going, and the design promises authentic Rome from day one. An empty "Legio" unit, plus 2–3 cards in U1 and U2, breaks the history spine; the Legion theme gets no Latin. Strict placement also misplaces cards that need only one unfamiliar form, which a gloss could handle.
- **Synthesis:**
  1. **Allow one glossed preview form** per anchor card in U1–U3, as long as the card's other target grammar is already taught. For example, *Gallia est omnis dīvīsa* can come back to U3 with *dīvīsa* as a preview.
  2. **Mine simple authentic Latin for U3:**
     - legionary tombstones (e.g. *mīles legiōnis … hīc situs est*, from a real CIL text);
     - stamped tiles (LEG XX VV);
     - Vegetius-style short maxims (*Igitur quī dēsīderat pācem, praeparet bellum*: Veg. 3 praef. As a preview subjunctive, it's better in U4);
     - Caesar BG present-tense narrative (*Caesar … castra movet*, as historic presents in BG).
  3. **Cap each unit at 6–10 anchors.** Move U5/U7 overflow to optional "Lege plūra" sets.
  4. Make unit balance a build-time warning: fewer than 4 or more than 10 cards per unit.
