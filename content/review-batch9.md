# Batch 9 review (50 cards)

**Built from:** `batch9_cards.py` + `batch9_images.py` → `batch9-cards.json` (`batch9_build.py`).
- The build checks unit order, and no lint errors remain.
- The duplicate check covers ids and Latin against every deck, including batch7, batch8 and `cards/cards.js`. It found no duplicates.

## Counts by unit
| Unit | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| batch 9 | 3 | 3 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 9 | 9 | 9 | 9 |
| total, all decks | 27 | 28 | 34 | 37 | 42 | 37 | 40 | 35 | 44 | 36 | 23 | 27 | 25 | 19 |

## Card sources
**Units 1–10 (14 cards):** constructed vocabulary sentences, marked `constructed`, covering Roman daily life and buildings.

**Units 11–14 (36 cards):** verified quotations. Each phrase was checked in the cached or fetched source text, from The Latin Library, la.wikisource or corpusthomisticum. The `source_url` points at that text.

**Normalised or shortened quotations** each carry an `attribution_note`:
- Ecce gratum, Kempis (ūnum), Arbroath, Magna Carta 40, Dante (philosophica)
- More (spliced), Luther (spelling), Asser (omission), Bacon (omission)
- Harvey: the motto is taken from the frontispiece.

## Checks
- **Context:** 2–4 sentences and at most 600 characters, with no internal or game wording.
- **Links:** all learn_more and source URLs return HTTP 200 (`batch9_check_urls.py`). The one 404, for Gaudeamus, was fixed to `Gaudeamus_igitur`.
- **Macrons (critic):** fixed pecūliāre and nēve. The other flags are false positives: malō is not mālō, and vendō and lege are correct.
- **Phonetics:** rebuilt; all 50 batch 9 entries were generated, and none of them is flagged.
- **Validation:** `tools_validate.py` reports 449/449 cards valid.

## Images
- All 50 images are new and none is reused; `/workspace/used_images.txt` now lists 442.
- All licences are free (PD, CC0, CC BY or CC BY-SA). None is NC/ND and none is credited to the British Museum.
- There are no cut-outs and no 1:1 crops.
- I checked contact sheets by eye and replaced these: the Arbroath field photo, the wrong Petrarch crop (it showed Pippo Spano), the Gauckler drawing, an unclear Codex Buranus "master" image, and the Giusto crowd scene.

## Critic pass fixes
- Stabat stanza number changed to 5.
- de Bury's library: much of it was sold to pay his debts.
- Magna Carta: annulled within months.
- Dante: the 1329 burning.
- XII Tables: Cicero's reason about fire.
- Removed the doubtful claim about senators voting *placet*.
- Trajan: softened to "one of the earliest" documents.
- Codex Aesinas: brought from Germany to Rome.
- Kepler conjecture: credited to Hales.
- Pont du Gard: the 2.5 cm drop applies to the bridge.

**Verdict: PASS.** Not run: `rome_build.py`. Nothing was committed or published.
