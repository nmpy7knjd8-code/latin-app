# Independent review of content/batch6-cards.json (48 cards)
Reviewer: critic. Date: 14 Oct 2026, about 00:45 ET. I did not rely on review-batch6.md.

## Method
- **Latin:** each text checked against the cached Latin Library, RIB and EDCS sources, and against the standard editions as I know them (macrons, translations, citations).
- **Images:** licences for all 48 checked live against the Commons API.
- **Unit order:** checked with the build lint (OK) and a manual read.
- **Layout:** overflow checked vertically and horizontally on the front and back of every card, and page width, at 390x844, 430x932 and 375x667.

## Dialectic
**Ovid, Heroides 1.1: "Haec" versus "Hanc"**
- *Thesis:* "Hanc (epistulam)" is the familiar reading, so change the text.
- *Antithesis:* the Latin Library and Loeb print "Haec", and the card's gloss (acc. pl. n.) fits it.
- *Synthesis:* keep "Haec". Fix the context, which wrongly said "this (letter)"; haec is neuter plural, "these (words)", and is the object of mittit. Note the "Hanc" variant in the attribution note.

**12 constructed sentences**
- *Thesis:* that's too many for a quotation app.
- *Antithesis:* units 1, 3 and 5 need simple sentences on the army and religion, which real texts rarely give at that level.
- *Synthesis:* acceptable. They are all honestly labelled "constructed" (TEACHING SENTENCE), and each sits next to real texts on the same theme.

## MUST-FIX
- **q-eutropius-augustus:** the image (Via Labicana Augustus) was a plain crop that still showed the exhibition text "POTERE". Replaced with Augustus of Prima Porta (File:Statue-Augustus.jpg, Till Niermann, public domain) as a clean cut-out. **Fixed.**

## SHOULD-FIX (fixed)
- **q-ovid-penelope:** context gloss corrected as above, and the Hanc variant noted.
- **q-sulpicia-tandem:** the citation repeated itself ("[Tibullus] 3.13 (Sulpicia) 3.13.1"). It is now "Corpus Tibullianum (Sulpicia) 3.13.1".

## Open (nits)
- **q-hannibal-ad-portas:** the context says Cicero uses it "in this form" in De finibus. His actual wording there is "si Hannibal ad portas venisset"; the note says so, but the context could be more exact.
- **q-cicero-silent-leges:** grammar_target neuter_plural only fits *arma*, since *lēgēs* is feminine. That's fine, but the context doesn't point it out.
- **i-pompeii-felicitas:** Commons gives "PDM-owner" and the card gives "PDM". Equivalent.

## Verified (no change)
- **Quotations:** Aen. 1.664, Cat. 1.2, Verr. 2.5.162, Rosc. Am. 84, Juv. 10.122, Quint. 12.1.1, Mil. 11, Catullus 3.1, 5.7, 13.1 and 34.1–2, Lucr. 1.1–2, Ecl. 1.1 and 3.60, Hor. Odes 1.10.1, 1.38.1, 2.14.1–2 and 3.1.1, Carm. Saec. 1, Fasti 1.65 and 6.5, Tristia 1.1.1, Met. 1.558, Prop. 1.1.1, Suet. Iul. 37.2, Cal. 30.1, RG 13 and 20.4, HA Hadr. 11.2, Eutropius 7.8 and 7.21.
- **Inscriptions:** CIL IV 1454, CIL X 874, RIB 1534 and RIB 1545.
- **Macrons:** correct, including short Dĭāna in the glyconic and Sapphic lines, which is left unmarked.
- **Images:** all 48 licences match Commons, with no British Museum images.

## Also done
- **batch5:** v-milites-aedificant and v-pontem-faciunt are "constructed". I rebuilt from the current sources; it has 49 cards.
- **q-seneca-aliena:** confirmed. It uses the Naples Pseudo-Seneca photo by Marie-Lan Nguyen, CC BY 2.5. No reference to "Pseudo-Seneca_BM" remains in rome-cards.json or licences.json.
- **Loader:** "batch6-cards" added to the cards/index.html loader. All batch6 images are in manifest.json.
- **Schema:** batch4 (50), batch5 (49), batch6 (48) and rome (64) all validate with 0 errors.
- **Overflow:** 315 cards, all 48 batch6 cards loaded. No overflow and no clamped contexts at 390x844, 430x932 and 375x667. Page scrollWidth equals the viewport width at all three sizes.
