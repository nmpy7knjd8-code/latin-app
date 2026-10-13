# Review 3: 16 new Rome cards in Units 1–3, plus re-check of the round-3 fixes
_Reviewer agent, Oct 13 2026, 01:30 ET. Texts checked against the standard editions (Terence, Plautus, Martial, Caesar, Ovid and Virgil from the Latin Library/OCT). The graffiti texts come from the AGP readings quoted in each card's attribution_note, and the RIB texts from the RIB online numbers._

## A. New U1–U3 cards
| id (unit) | Wording / citation | Result | Notes |
|---|---|---|---|
| i-pompeii-felices (U1) | CIL IV 8657, AGP-EDR127399: *Ic sumus felices valiamus recte* | ✔ | The normalisation is disclosed. The macrons in *Hīc, fēlīcēs, valeāmus, rēctē* are right. Its only preview is the subjunctive, so it's a good U1 card. |
| q-ovid-urbis (U1) | Fasti 2.684 *Rōmānae spatium est urbis et orbis idem* | ✔ | The *urbis/orbis* pun makes it an excellent anchor. |
| q-virgil-moenia (U1) | Aen. 1.7 ✔ | ✔, with a should-fix | It's a fragment with no verb; it depends on *genus unde Latīnum* (1.6). Add "…" at the start. "Nominative" is correct only within *unde [sunt]*, so say "the subjects of an understood 'came'". The Servian Wall image is a good fit. |
| q-terence-quot (U1) | Phormio 454 ✔ | ✔ | |
| i-pompeii-romula (U2) | CIL IV 2060 ✔ | ✔ | *morātur* is deponent (preview). The translation "hangs out" is good. |
| q-plautus-lupus (U2) | Asinaria 495 ✔ | **should-fix** | The cut changes the meaning. The line continues *quom quālis sit nōn nōvit*: "a wolf, not a man, *when he doesn't know what the other is like*". It is not Hobbes's maxim. Add "…" and a note. The image is a Plautus manuscript of the *Mostellaria* (Vat. Pal. lat. 1615), so label it. |
| i-pompeii-admiror (U2) | CIL IV 1904 ✔ | **should-fix (placement)** | It needs indirect statement, a perfect infinitive, a relative clause and a subjunctive. That's four previews in U2. Make it a U8 card (indirect statement), or mark `card_role: preview_reading`. |
| i-rib-regina (U2) | RIB 1065 ✔ | ✔, with a nit | The *coniuge* error is noted, which is good. With dative, ablative and genitive all ahead of the unit, it's heavy for U2; score 3 is right. Consider U4. The quantity in *Barātēs* is unknown; drop that macron. The image file name ends "-Copyright.jpg", so confirm the CC BY 4.0 on its file page. |
| q-cornelia-ornamenta (U2) | ✔ | ✔ | It now uses *ōrnāmenta*, consistent with the other Rome cards. The learning story still has *ornāmenta*. |
| i-pompeii-cave, q-catullus-ave (U2) | ✔ | ✔ | |
| q-martial-sabidi (U3) | Epig. 1.32 ✔ | ✔ | The verbs are 1st conj. (*amō*), which fits U3. *possum* is a preview. |
| q-terence-homo (U3) | Heaut. 77 ✔ | ✔ | |
| q-terence-fortis (U3) | Phormio 203 ✔ | ✔ | The acc. pl. *fortīs* is correctly kept and should be explained in the gloss as "= fortēs". |
| q-caesar-belgae (U3) | BG 1.1.3 ✔ | ✔ | It fits the Legio theme. |
| i-pompeii-fullones (U3) | CIL IV 9131 ✔ | ✔ | It parodies Aen. 1.1. Link it to q-virgil-arma (U7) as the payoff card; that's very good design. |
| i-pompeii-successus (U3) | CIL IV 8259 ✔ | ✔ | Normalising *coponiaes* and *Hiredem* is disclosed. The relative clause is a preview, which is acceptable. |
| i-rib-facilis (U3) | RIB 200 ✔ | ✔ | The expansions are correct (Pollia tribe, centurion, *lībertī*). The Boudica hedge is good. |
| i-rib-flavinus (U3) | RIB 1172 ✔ | ✔ | The Bruce *Lapidarium* plate is PD. |

**Macrons:** I found no errors in the 16 cards. The one exception is *Barātēs*, a foreign name whose quantity is unknown.

**Licence error (carried over from rome-2 §D, still open):** 13 cards with CC BY / BY-SA images still credit only "Wikimedia Commons (CC BY…)" with no author. Five of them are new: i-pompeii-romula, i-pompeii-admiror, q-caesar-belgae, i-rib-facilis and i-rib-regina. `img/rome/licences.json` now has 64 entries, so the author data probably exists. **Fix:** copy `Artist` from licences.json into each card's `credit`, and add "background removed" to the cut-outs.

**Teaching value:** U1–U3 now have 6, 7 and 8 cards, compared with 2, 3 and 0 before. The empty Legio unit is fixed by the two RIB soldiers, Caesar's Belgae and the Pompeii army parody.

## B. Dialectic: early-unit design
- **Thesis:** fill U1–U3 with short, authentic, everyday Latin (graffiti, tombstones, comic one-liners). It is real, funny and human, and mostly uses simple *sum* and present-tense patterns.
- **Antithesis:**
  - Graffiti and epitaphs are full of non-standard spelling (*Ic, valiamus, coponiaes, coniuge*) and heavy abbreviation. Normalising them hides that, while leaving it in confuses beginners.
  - Several cards pile up previews (*admiror*, Regina).
  - Comic proverbs give strong cultural hooks but little reusable syntax.
  - Another risk is that U1–U3 become "Pompeii trivia" rather than input.
- **Synthesis:**
  1. Show the normalised text by default, with a "What the wall actually says" toggle that shows the AGP reading. That turns the spelling into a lesson on how Latin was really written and spoken.
  2. Allow at most one preview per card in U1–U3, and enforce it with a lint. Move *admiror* to U8 and Regina to U4.
  3. Pair each early card with a pattern drill, e.g. *Hīc sumus fēlīcēs* → *Hīc sumus laetī/miserī*.
  4. Feed the U1–U3 cards into the unit stories (e.g. the U3 story ends at Facilis's tombstone).

## C. Re-check of the producers' round-3 fixes (as of 01:30 ET)
| Area | Item | Result |
|---|---|---|
| Rome | Author credits for CC BY/BY-SA (rome-2 §D) | **FAIL / not yet landed.** rome-cards.json was last modified at 01:18, and 13 cards still have no author. |
| Rome | licences.json complete | **PASS** (64 entries) |
| Medieval | John 1:5 "comprehend" | **PASS** |
| Medieval | *galea* = medieval "galley" gloss | **PASS** |
| Medieval | Colophon wording | **PASS.** It now quotes the BnF lat. 12234 version exactly, with the variants listed. |
| Learning | l-bulla agreement as preview | **PASS** |
| Learning | Story U10 *eum laudāvit* | **PASS** |
| Learning | Story U5 odd water line | **PASS** (*Virginēs aquam ex fonte portant*) |
| Phonetics | Missing-macron stress (*regina*) | **PASS** (now /reː.ˈgiː.na/ ray-GEE-na through the lexicon) |
| Phonetics | `--verse` command-line flag | **PASS** (*MUL-t'IL-l'et*) |
| Phonetics | *euge* respelling | **PASS** (EW-ge) |
| Phonetics | Legend wording (gn, pure ay, z policy) | **PASS** |
| Phonetics | Ecclesiastical *huic* "wee" | **PASS** (OO-eek) |
| Phonetics | Test suite | **PASS** 70/70. While the producer was mid-edit, phonetics.py briefly had a syntax error at line 222 (01:25). It was fixed by 01:27. Keep `--test` in CI so a half-finished save can't be deployed. |

**Round 3 overall:** 12 of 13 items pass. The one open item is the author credits on the 13 Rome CC BY/BY-SA images.
