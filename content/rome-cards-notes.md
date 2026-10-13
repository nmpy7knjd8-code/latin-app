# Rome cards: notes (batch 2, 13 Oct 2026)

**Output:** `rome-cards.json` has 48 cards, all valid against `card-schema.json`, and the build lint passes.

**Build:** `python3 content/rome_build.py`. It reads `rome_cards.py` (the texts), `rome_meta.py` (unit placement, grammar, images, learn_more) and `data/dcc-core.json` (the Dickinson Core list). Nothing depends on /tmp any more.

**Images:** `rome_images_fetch.py` downloads from Commons and re-checks each licence through the API. `rome_images_process.py` (run with the /workspace/venv Python) does the following:
- rembg with the `isnet-general-use` model for 3D objects, cropped to the object's edges and saved as WebP
- crop to the target aspect ratio for flat images

Results go to `img/rome/`.

## Review-rome.md: what was applied
- **Unit placement (synthesis adopted).**
  - Each card now has `grammar_target`, which is tested and must already be taught, and `grammar_preview`, which is glossed only.
  - `grammar_tags` is target + preview.
  - The lint fails if any target tag is taught after the card's unit.
  - The `TAUGHT` map follows **game-design.md** (perfect in U6, future in U7). The reviewer listed perfect in U7 and future in U6; game-design.md is treated as the source of truth here.
  - Cards were moved to fit:
    - Arma: U3 → U7
    - Tacitus solitudinem: U3 → U5
    - Historia: U4 → U5
    - Horace sapere: U7, with the infinitive as a preview
- **Scoring.**
  - The rule "score 5 only if core vocabulary ≥80%" is enforced automatically.
  - `teaching_value.role` is `anchor` when core ≥80% and the card has a target tag; otherwise it is `preview`. 22 cards are anchors.
- **Text and metadata fixes.**
  - Catullus 5 context (the "night" is death)
  - Titus: short i, `F(ILIO)` instead of `F[ILIO]`, *VESPASIANO* added to the gloss
  - Horace placeholder metadata now uses the real cards.js image data
  - *sapere audē* and *ōdī et amō* translations
  - Historia now ends with "…"
  - Pantheon: *Lūcī*
  - Gloss note on *Ītaliam* (vowel lengthened for the metre)
  - *tu + -que* split into two vocab entries
  - Erasmus note on *alea esto*
  - *laudī / linguae* variant for *cēdant arma togae*
  - Agricola 30.5 vs 30.4
  - Livy's Varronian date
  - Locke for *salūs populī*
  - Juvenal: *populus* is the subject of *optat*
- ***Quīntilī Vāre, legiōnēs redde!* (Suet. Aug. 23.2) restored.** It is in the Latin Library text, which is UTF-16 encoded; that's why the earlier string match failed. The spelling there is *Quintili*. It is marked `traditional` because Suetonius says *ferunt* ("they say").
- **Images.**
  - No image is used twice.
  - Memento-mori mosaic cropped to 3:4.
  - Sarcophagus frieze is now 2:1 with no cut-out.
  - Pantheon .tif converted to WebP.
  - Swaps:

    | Card | New image |
    |---|---|
    | Martial | wax writing tablet |
    | Lucretius | bust of Epicurus |
    | *Exēgī* | Pyramid of Cestius |
    | Catullus 101 | funerary altar of Cominia Tyche |
    | *mēns sāna* | bronze Mercury |
    | *cēdant arma* | armoured torso |
    | Calgacus | Gallic warrior statue (loose match: not Caledonian) |
    | *vae victīs* | Brennus illustration |
    | *tantae mōlis* | Aeneas denarius |
    | *fugit tempus* | sundial |
    | Titus | the real attic inscription. The earlier file was the modern "ARCO DI TITO" sign, now fixed. |
    | women's portraits | front views; the first set were photos of the back of the head |

- **Not done.**
  - Separate `text_verified` and `speaker_historicity` fields (review item 15). The point is covered in `attribution_note` instead.
  - Adapted Latin lead-ins (synthesis item 2). That is a content task for later.

## New cards (12)
- **Unit 5, Gods (now 11 cards):**
  - Seneca *Prope est ā tē deus* (Ep. 41.1)
  - Aen. 1.8 *Mūsa, mihi causās memorā*
  - Aen. 1.11 *Tantaene animīs caelestibus īrae?*
  - Ovid Fasti 6.267 (Vesta)
  - Ars 1.637 *Expedit esse deōs*
  - Aen. 6.126 *Facilis dēscēnsus Avernō*
  - EID MAR coin
- **Coins:** EID MAR (Brutus) and AEGVPTO CAPTA (Octavian). The legends come from Wikipedia articles; I removed the RRC/RIC catalogue numbers because I couldn't verify them.
- **Inscriptions and graffiti:**
  - SPQR (U1)
  - *Cave canem* (Pompeii mosaic, U2)
  - S·T·T·L *Sit tibi terra levis* (U4)

## Verification
- **EDCS/EDR: not completed.**
  - EDCS has moved to edcs.hist.uzh.ch. Its `/api/search` returned `[]` for every query I tried.
  - EDR timed out.
  - So the Pantheon (CIL VI 896) and Titus (CIL VI 945) texts are still checked only against Wikipedia, which cites CIL.
- **Pompeii graffiti: not added.** The Ancient Graffiti Project was unreachable, and I couldn't find a verifiable online CIL IV text. The Pompeii item included is the mosaic inscription.
- **Macronizer.** All 48 Latin lines, with macrons stripped, were run through the Alatius macronizer (alatius.com/macronizer). There were 21 differences:
  - **Adopted:** *ōrnāmenta*, *ānxius*, and *Īdibus* (the coin's EID is the old spelling).
  - **Kept, Alatius wrong in context:**
    - *legis* (present tense)
    - *hīc* (adverb)
    - *Agrippa* (nominative)
    - *Cavē* (imperative)
    - *vēnit* (perfect)
    - *fugit* (present)
    - *putēmus*
    - *ūsque*
    - *abūtēre* (future)
    - *aere* (from *aes*)
    - *Trōiae*
  - Inscriptions are kept in capitals with no macrons.
- **learn_more:** every card has one. All learn_more and source URLs return HTTP 200.

## Gaps
- **U3 (Legio) now has 0 cards**, because the review's grammar rules pushed its old cards later. It needs simple present-tense military Latin, such as tombstones of legionaries.
- U1 has 2 cards and U2 has 3.
- `img/rome/licences.json` only lists the last re-fetch. Every licence was checked through the API at download time.
