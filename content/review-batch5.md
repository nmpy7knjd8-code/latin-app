# Batch 5 critic review (self-review; an independent critic follows)

Scope: 50 cards in content/batch5-cards.json. By unit: U3 5 · U4 5 · U5 2 · U6 6 · U7 1 · U8 9 · U9 11 · U10 11.

## Round 1: thesis (automated checks)
- batch5_build.py lint: unit-order (every grammar_target tag is taught at or before the card's unit); context ≤600 chars and 2–4 sentences; no game or internal wording ("Unit N", "preview", "card", "tap"…) in context or more; id collisions and duplicate Latin checked against rome, medieval, learning and batch4 decks. Result: OK.
- batch5_check_urls.py: 86 learn_more/source URLs, all HTTP 200.
- batch5_critic.py: Latin matched against the cached source text (Latin Library, Perseids, la.wikisource, hs-augsburg). 47/48 quotations match; 2 constructed cards n/a.
  - The 3 apparent misses are explained and noted on the cards: Tacitus Ann. 15.44 (the Latin Library misprint "Tibero"), Pliny Ep. 10.96 (card drops the enclitic -que), Seneca Ep. 108.23 (the source runs words together as "philologiaest").
- Alatius macron comparison. Every difference was reviewed and the card was kept, because context beats the automatic tool:
  - Garumna, Gallia omnis: nominative.
  - viā Sacrā: ablative of route.
  - Aemiliāne: vocative, short -e.
  - metimur: from metō, "reap", not mētior.
  - Vēnī, fēlīcem: correct.
  - manifestum, eius: hidden quantity, left unmarked.
  - Laecania, Brittania: left unmarked on purpose, with a note on the card.
  - tris was changed to trīs, accusative plural of an i-stem.
- tools_validate.py: schema 264/264. phonetics.py --build covers all 50 batch5 ids.

## Round 1: antithesis (manual fact/teaching review)
Problems found and fixed:
1. **Cicero, Tusc. 5.25.** The card said the line came from the historian Callisthenes. In fact Theophrastus praised the saying *in his book* Callisthenes. Person, context and note are corrected, and confidence is set to traditional.
2. **Seneca, Ep. 2.6.** The card said the line was Epicurus's. The Epicurus quotation is "honesta res est laeta paupertas"; the "non qui parum habet…" line is Seneca's own correction. Fixed.
3. **Second Catilinarian.** Date corrected to 9 November 63 BC.
4. **Anselm in 1077–78.** He was a monk (prior) of Bec, not yet its abbot. Fixed.
5. **De senectute.** Cato's age corrected to 84.
6. **Martial 5.43.** The false-teeth claim was softened to what the evidence supports (Etruscan and Roman gold dental bridges).
7. Removed internal wording from "more" texts ("taught in Unit 7", "a preview feature") and trimmed three contexts that ran to 5–6 sentences.
8. Images:
   - Six candidates were already used in other decks: wax tablet, Cicero GL 325, Catullus bust, Epicurus, Hatton/Benedict, Raban-Alcuin. All were replaced.
   - A second photo of the same "Sappho" fresco used in the learning deck was rejected.
   - The Anselm seal was rejected because of a British Museum credit.
   - The cut-outs for Dea Roma and Pliny failed on the contact sheet and now use plain crops.
   - Image kinds were mapped to the schema enum, and "PDM-owner" was normalised to "PDM".
9. The Creed card was missing the required `person` field; it now reads "The early Church (anonymous)".

## Round 2: synthesis
- Rebuilt and re-ran lint, URLs, the source check and schema validation: all pass.
- The contact sheet (/workspace/contact5.png) was checked by eye. The 9 cut-outs are clean.
- Remaining judgement calls for the independent critic:
  - The black swan photo is filed as kind "artifact", because the schema has no "photo" kind.
  - The two constructed U3 cards (v-milites-aedificant, v-pontem-faciunt) are close in theme.
  - U5 and U7 are thin (2 and 1 cards), as the brief did not prioritise them.
  - The Apostles' Creed is dated "8th c. (textus receptus)".
  - The source for q-alcuin-vox-populi is la.wikisource rather than a critical edition.

**Verdict: PASS (self-review).** Not published, not committed.
