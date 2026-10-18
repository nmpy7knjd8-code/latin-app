# Independent review of content/batch7-cards.json
Reviewer: critic. Date: 18 Oct 2026, about 01:10 ET. The file had 78 cards; it now has 77. I did not rely on review-batch7.md.

## Method
- **Latin:** each text checked against the cached sources (Latin Library, Wikisource, the Harvard Bracton edition, corpusthomisticum, Gutenberg) and the standard editions as I know them (macrons, translations, citations, facts).
- **Images:** licences for all 78 checked live against the Commons API.
- **Duplicates:** normalised Latin and ids compared against **cards.js**, rome, medieval, learning and batches 4–6. The producer's check left out the base deck in cards.js.
- **Unit order:** batch7_build lint, plus a check of how much of each new unit's grammar its cards actually teach.

## Dialectic
**1. Apuleius 11.5, "rērum nātūra parēns"**
- *Thesis:* the card reading is a fine apposition: "I, nature, mother of things".
- *Antithesis:* the source reads *rērum nātūrae parēns*, Isis as "mother of the natural world". The card had silently changed a genitive into a nominative.
- *Synthesis:* follow the source. Latin, gloss, translation and context are corrected.

**2. New units: thematic or grammatical?**
- *Thesis:* XI–XIV are thematic sections (schools, kingdoms, law, science), so their themes are what matter.
- *Antithesis:* game-design §3 gives each unit a grammar load. A unit whose cards never target that grammar teaches none of it.
- *Synthesis:* the themes hold up well (see below). The grammar coverage is thin and needs retagging or new cards; I have not made those cards up.

## MUST-FIX (fixed in batch7_cards.py, rebuilt)
- **q-caesar-gallia:** a duplicate of the base-deck card with the same id in cards.js, the same problem as in batch5. The loader would have hidden it silently. Removed.
- **q-apuleius-isis:** *nātūra* corrected to *nātūrae*, with the gloss now "gen. sg." and the translation "mother of the natural world". A sentence on the genitive was added to the context.

## SHOULD-FIX
- **q-martin-miles (fixed):** "the emperor Julian". In 356 Julian was Caesar, not yet emperor. Now "Julian, then Caesar and later emperor".
- **q-more-utopia (fixed):** the citation repeated itself ("Utopia (title) title"). Now "More, Utopia, title page".
- **i-amymone (open):** the image is a Palmyrene loculus relief, which is not Roman and not linked to the inscription. A Roman funerary portrait of a woman would fit better.
- **q-vulg-petrus and q-vulg-reddite (open, nit):** both are marked era `empire`, while the other Vulgate cards are `late_antiquity`. The era should follow the text (Jerome, 4th century) consistently.
- **q-vulg-dominus-reget (open):** the future-tense target depends on the Stuttgart reading *reget*; the Clementine has *regit*. The card notes it, but *deerit* alone would carry the future more safely.
- **q-bernard-stat-roma (open):** the line number 1.952 depends on the edition, as the producer noted.
- **Licence nit:** Commons gives "No restrictions" for q-boethius-carmina; the card maps it to Public domain with a licence note. Acceptable.

## Verified (no change)
- **Classical:** Catullus 8.19 and 31.12, Cic. Att. 1.8.3, Phil. 2.113 and 12.5, Div. 2.119, Acad. 1.16, Off. 1.33, Cluent. 146, Juv. 14.47, Plaut. Aul. prol. 2, Cato Agr. 141.2, RG 34.3, Eutropius 8.2 and 8.5.3, Martial 1.38, Met. 2.137, Livy 22.51.4, Seneca Ep. 28.1 and 104.26, Brev. 7.3, Medea 199–200, Horace Sat. 1.1.24–25.
- **Christian and medieval:** Aug. Civ. 14.28, Vulgate Matt. 16:18 and 22:21, Gen. 3:19, Sulp. Sev. Mart. 4.3, Boethius 1 m.1, Patrick Conf. 1, Vexilla regis, Bede 4.24, ARF 801, RB 18.1, Hist. Britt. 56, Asser 23, Te Deum, Hrotsvit, CB 196, Stabat Mater, O quanta qualia, ST I q.2 a.3, Arbroath, Kempis 1.2.3 and 1.19.2, Philobiblon 1, DVE 1.1.4.
- **Legal:** XII Tables I.1, Inst. 1.1 pr., Dig. 1.1.10.1, 48.19.18, 50.17.56 and 40.9.12.1, CJ 5.59.5.2, Bracton f. 5b.
- **Early modern:** Copernicus 1.10, Sidereus Nuncius, Med. 2, Newton Lex I, Spinoza Eth. 4 praef., Columbus 1493, Utopia, Inter gravissimas §4, Orbis Pictus, Moriae encomium.
- **Facts:** dates and facts correct, e.g. 4 → 15 Oct 1582, Edward I's 1295 writ, Ulpian/Gaius, and *cōgitō ergō sum* in the Principia of 1644.
- **Images:** all 78 licences match Commons, with no British Museum, NC or ND images and no file reused from another deck.

## Coherence of units XI–XIV (77 batch7 cards plus 12 medieval-cards that now surface in units 11 and 12)
The viewer used to cap every unit at 10, so those 12 medieval cards with unit 11 or 12 were showing in X.

- **Themes are coherent:**
  - XI Scholae: Carmina Burana, Abelard and Heloise, Aquinas, hymns.
  - XII Rēgna: Magna Carta, Arbroath, de Bury, Dante, Kempis, the Paris statute.
  - XIII Iūs: Twelve Tables to Bracton.
  - XIV Scientia: Erasmus to Newton.
  - The weakest fits are Kempis in "Kings, Charters & Books" (a devotional book) and Bernard of Cluny's *Stat Rōma* in "Schools & Songs" (a satire). Both are defensible.
  - U10 still holds the strongest "kings" cards (Charlemagne's acclamation, Asser on Alfred, Arthur). Moving one or two of them to XII would strengthen it.
- **Grammar coverage is weak (should-fix, open):** counting the unit's own new grammar in grammar_target:
  - XI: 1/11 cards (q-cb-in-taberna).
  - XII: 0/11.
  - XIII: 2/11 (Twelve Tables future imperative, Medea ablative absolute).
  - XIV: full review, as designed.
  - **Suggestions:** tag the jussive subjunctives in Magna Carta 39 (*capiātur, imprisōnētur…*) and add a cross-reference from *Stabat Mater*'s *dum* to XII.
  - For XII, add cards that actually carry deponents, gerunds and gerundives, e.g. Philobiblon or Kempis passages with gerunds, *dum* clauses or *ūtor*. Moving q-dig-cogitationis (*patitur*, deponent) or q-dig-benigniora (*praeferenda*, gerundive) into XII would also work.
  - Those fixes touch medieval sources or the curriculum, so I have left them to the producer.

## Viewer changes (cards/index.html)
- **UNITS:** added XI Scholae (Schools & Songs, high_medieval colour), XII Rēgna (Kings, Charters & Books, late_medieval), XIII Iūs (Law & Justice, late_antiquity colour) and XIV Scientia (Humanists & Scientists, early_modern).
- **Hardcoded 10s:** unitOf now clamps to UNITS.length, and prev/next wrap at UNITS.length. Tested: XIV → next → I, and I → prev → XIV.
- **Era:** new `early_modern` colour theme (#1f5f7a → #143f52, panel #0d2a37, accent #f3dca0; text contrast above 4.5:1) and the label "Early Modern". The overlay's era regex was updated too.
- **Loader:** added "batch7-cards". All batch7 images are in manifest.json.
- **Section picker:** a compact 2-column grid (button 46px, 40px when the screen height is 720px or less) and smaller ring numerals. The pane has max-height 100dvh − 12px with internal scrolling as a fallback.
  - At all four sizes the pane fits with no internal scroll and the page height equals the viewport height.
  - Screenshots: shots/picker-390x844.png, picker-430x932.png, picker-375x667.png, picker-390x664.png.
- **cards/shot_mobile.py:** now loops over UNITS.length instead of 10.

## Checks
- **Schema:** 0 errors in batch4 (50), batch5 (49), batch6 (48), batch7 (77), rome (64), medieval (35) and learning (65). Build lint OK.
- **Overflow:** 392 cards in 14 sections. Front and back of every card checked vertically and horizontally at 390x844, 430x932, 375x667 and 390x664: overflow [], clamped contexts 0, page scrollWidth equal to the viewport width, no page errors.
