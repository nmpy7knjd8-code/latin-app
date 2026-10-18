# Review — batch 8 (11 cards) and the unit XI–XIII grammar fix
This answers review-batch7-independent.md, which found that the new units barely targeted their own grammar: XI 1/11, XII 0/11, XIII 2/11.

## Thesis
- **Coverage now:** counting cards whose `grammar_target` includes the unit's own new grammar:
  - **XI: 5/14.** archpoet (ut-purpose subjunctive), Heloise (comparative + subjunctive), In taberna, Anselm (comparative + ablative of comparison + subjunctive), *Omittāmus studia* (hortatory).
  - **XII: 5/18.** Einhard (gerundive), Kempis (deponent + dum), Oresme (gerund), Petrarch (deponent), Asser on Alfred's children (ablative with deponent).
  - **XIII: 6/16.** Twelve Tables *itō* and *estō* (future imperative), Medea (ablative absolute), Ulpian (*oportet* + perfect infinitive *nōsse*), Paul (*licet*), Tacitus (ablative absolute).
  - The other cards keep their themes and review earlier grammar.
- **Retagged, without changing any text:**
  - `medieval_units_grammar.py`, an idempotent patch, gave explicit targets to 8 medieval cards. These include Magna Carta 39 and the Paris statute (jussive passive subjunctive), the archpoet and Heloise; Abelard's *dubitandō* has the gerund as a preview.
  - Asser's book contest is now targeted at subjunctive + comparative in XII.
- **Moved:**
  - Bernard of Chartres' dwarfs and giants, X→XI (batch4).
  - Einhard's writing tablets, VIII→XII (batch4). The Latin was extended by the purpose clause containing the gerundive *litterīs effigiendīs*, verified against the Latin Library ch. 25.
  - Charlemagne's acclamation and Asser's book contest, X→XII (batch7).
- **Rules:**
  - All 11 new cards are verified quotations, with no constructed sentences.
  - Contexts are 2–4 sentences and at most 600 characters.
  - All 20 learn_more URLs return 200.
  - Licences are PD, CC0 or CC BY-SA only, with no British Museum, NC or reused images.
  - Lint is OK, schema validation is 399/399 and phonetics covers every card.
- **Duplicate check:** batch7_build and batch8_build now also compare against cards.js, the base deck the earlier check had missed. No duplicates were found.
- **Shared grammar table:** `rome_meta.py` TAUGHT now places the U11–13 tags at units 11, 12 and 13 instead of 99, and adds `gerund` at 12. `rome_build.py` was not run; the change only loosens its lint.
## Antithesis (critic findings)
- **Alatius macron check:** *fūrtum* fixed (long u, from fūr). The other differences are kept on purpose: *maius* is left unmarked by the house convention, as with *cuius*; *pūblicā* is a correct ablative; Alatius' *Saxōnicōs* and *lībrīs* are wrong.
- **Source differences, recorded in the notes:**
  - CB 75: the manuscript has *tenere*, normalised to *tenerae*.
  - Kempis has the future indicative *poteris* in an indirect question.
  - Petrarch and Asser cards start mid-sentence (after *quoniam* and *nam*).
  - The Twelve Tables text is a reconstruction (Macrobius).
- **Images:**
  - The Digestum Novum file turned out to be a book cover, so the Codex Florentinus page is used instead.
  - The broken Roman key was replaced with a Roman oil lamp, for the night thief.
  - The Oresme caption claimed an armillary sphere that is not visible; corrected.
- **Facts checked:**
  - Marcellus' well case is Digest 39.3.1.12.
  - The marriage line is Digest 23.2.42 (Modestinus).
  - Petrarch found the letters in Verona in 1345.
  - Ælfthryth married the count of Flanders.
  - Asser: "the only English king called the Great" was wrong (Cnut); now "English-born".
- **Other independent-review items fixed:**
  - The Amymone image was a Palmyrene relief; it is now the Roman funerary relief of the Vibii, from Rome, which includes a freedwoman wife.
  - The Vulgate cards Matthew 16:18 and 22:21 now have era `late_antiquity`.
- **Still open:**
  - XII is still the weakest unit at 5/18, because Magna Carta, Arbroath, Dante and Kempis carry little U12 grammar.
  - Bernard of Cluny's line number depends on the edition.
  - Three batch7 images use a 1:1 aspect, which the schema says to avoid but does not forbid.
## Synthesis
Every unit from XI to XIII now teaches its own grammar through real texts, and the themes are unchanged.
**Verdict: PASS.**
