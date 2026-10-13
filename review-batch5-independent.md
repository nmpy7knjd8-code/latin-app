# Independent review of content/batch5-cards.json
Reviewer: critic. Date: 13 Oct 2026, about 03:20 ET. The file had 50 cards; it now has 49.

## Method
- **Latin:** all 48 quotations checked against the Latin Library, Perseus, Wikisource and the Augsburg texts, and against my own knowledge of the editions. All match. Omissions are declared: -que in Pliny, and inquit.
- **Images:** Commons API check of all 50 licences; all match. PDM-owner counts as PDM.
- **Duplicates:** normalised Latin compared against cards.js, rome, medieval, learning and batch4.

## Dialectic
**Duplicate "Gallia est omnis"**
- *Thesis:* keep both. Unit 6 can re-teach dīvīsa as a perfect-passive preview.
- *Antithesis:* the base deck already has id q-caesar-gallia (U3). The loader skips any repeated id, so the batch5 card would never appear, and a repeated sentence wastes a slot in the spaced-repetition queue.
- *Synthesis:* removed it from batch5. Its context facts (the three peoples, Vercingetorix) could be merged into the base card later.

**Pluperfect in Martial 1.47 (fēcerat)**
- *Thesis:* a target can't name a tense the syllabus doesn't teach.
- *Antithesis:* hiding it misleads the learner.
- *Synthesis:* list it as a preview. I added `pluperfect` to TAUGHT as 99 (not yet scheduled), alongside perfect_infinitive.

## MUST-FIX (fixed)
- **q-caesar-gallia:** duplicate of the existing base card with the same id. Removed from batch5_cards.py.
- **q-martial-diaulus:** the CC BY 4.0 Wellcome credit said "by unknown". Now "Wellcome Collection".
- **q-seneca-aliena (rome-cards):** the image was a British Museum Pseudo-Seneca photo. Replaced with the Naples (MANN inv. 5616) Pseudo-Seneca bronze by Marie-Lan Nguyen (Jastrow), CC BY 2.5, as a new cut-out.
  - Updated: rome-cards.json, img/rome/licences.json, rome_meta.py and rome_build.py.
  - Added "CC BY 2.5" to the schema licence enum.
- **v-milites-aedificant, v-pontem-faciunt:** status set to "constructed", so the badge reads TEACHING SENTENCE.

## SHOULD-FIX
- **q-caesar-castra-movent:** the context said movent "takes its plural subject from the soldiers, not the camp", which treated castra as a possible subject when it is the object. Rewritten. **Fixed.**
- **q-benedict-mortem:** the translation dropped suspectam. Now "…before one's eyes as something to be expected." **Fixed.**
- **q-martial-diaulus:** pluperfect added as a preview. **Fixed.**
- **Open:**
  - q-lucretius-nil-creari prints "dē nihilō" as the Latin Library does, while Bailey reads "de nilo". Note it in the attribution note.
  - q-tacitus-christus says "earliest non-Christian Roman reference to Jesus's execution". That is defensible, but "Pliny 10.96 (c. 112) mentions Christ earlier" deserves a clause.
  - q-alcuin-vox-populi: "earliest known appearance" should read "earliest well-known appearance".
  - The two constructed U3 cards are close in theme (both about soldiers). That is acceptable.
  - The new Seneca cut-out keeps a sliver of plinth at the bottom edge (cosmetic).

## Wiring and checks
- **Loader:** "batch5-cards" added to the cards/index.html loader. All batch5 images are in manifest.json.
- **Schema:** batch4 (50), batch5 (49) and rome (64) all validate with 0 errors.
- **Overflow:** shot_mobile.py, 267 cards, at 390x844 and 430x932: overflow [], clamped 0. In the live page the badges render "teaching sentence".
