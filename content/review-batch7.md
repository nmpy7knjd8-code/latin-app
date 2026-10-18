# Review — batch 7 (78 cards)
## Thesis
- By unit: U1 3, U2 4, U3 3, U4 3, U5 3, U6 3, U7 3, U8 8, U9 9, U10 8, and in the new units U11 5, U12 5, U13 11, U14 10.
- 70 quotes or inscriptions: 69 `verified`, plus 3 `traditional` (*Ōrā et labōrā*, *Te Deum*, *Stabat Mater*). There are also 6 constructed vocab sentences and 2 artifacts (the ROMA AETERNA coin and the Amymone epitaph, CIL VI 11602).
- No id or Latin text duplicates rome, medieval, learning, batch4, batch5 or batch6. No image file is reused from any existing deck (checked against `used_images.txt`).
- Every context is 2–4 sentences and at most 600 characters, with no internal or game wording. Lint is OK.
- Every `learn_more` link returns HTTP 200 (143 URLs checked).
- Images are PD, CC0 or CC BY(-SA) only, with no British Museum or NC images. There are 12 cut-outs, all of 3D objects (busts and statues).
- New units XI–XIV are documented in `game-design.md` §3. The era `early_modern` was added to `card-schema.json`.
## Antithesis (critic findings and fixes)
- Alatius macron pass: fixed Patricius (short a), dabō, itō (future imperative of eō), ūnifōrmiter, revertēris (future deponent), Vēxilla and Gandeshemēnsis. The other differences are correct as written in the card: case endings (victōriā after ūtor, alterā, perpolītā, summa/iniūria nominative), cuius/iūxtā conventions, and the adverb inclūsīvē.
- Source differences (`MISSING` hits), each recorded in the card's notes:
  - Seneca 104.26: the Latin Library runs two words together ("audemusdifficilia").
  - Arbroath: the source spells "set … diuicias"; normalised.
  - Hrotsvit: Wikisource has "Gandeishermensis".
  - Galileo: the source spells "inêquali".
  - More: the title uses "reipublicæ".
  - Psalm 22: reget/regit.
  - Columbus: "reperi".
  - Bernard of Cluny: Rōma vs Eco's rosa.
- Images:
  - The Tombstone of Nertus showed no rider. Replaced with a cavalry tombstone at the Grosvenor Museum in Chester.
  - The Charlemagne coronation had a junk credit (a URL as the artist). Replaced with Fouquet's *Sacre de Charlemagne* (Grandes Chroniques).
  - The coin was re-cropped to remove the scale rulers. Its alt text now says "worn, corroded".
  - The de Bury image is a seal; the alt text was corrected to say so.
  - The Ambrose mosaic had a non-schema "Attribution" licence. Replaced with Lochner's *Ambrose, Augustine and Cecilia* (PD).
  - The Flickr Commons "No known copyright restrictions" licence was mapped to Public domain, with a licence note.
- Facts softened: Colosseum (begun 70s, opened 80); Coke/James I "around 1608"; de Bury's library ("a chronicler claimed…", left to Durham College but mostly sold to pay his debts); Piazza del Popolo obelisk ("An Egyptian obelisk").
- Still open, all low risk:
  - Bernard of Cluny's line number 1.952 depends on the edition.
  - *Stultitia loquitur* has no long vowels, so it is flagged "no macrons" in macron-report (correct).
  - `phonetics_eccl.py` covers only the rome and medieval decks, as for batches 4–6.
## Synthesis
Every critic finding is fixed or explained. Lint is OK, schema validation is 389/389, the manifest is regenerated and phonetics is rebuilt (392 entries).
**Verdict: PASS.** The viewer needs changes before units XI–XIV display separately; see the final report.
