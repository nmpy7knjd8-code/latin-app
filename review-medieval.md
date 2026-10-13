# Review: content/medieval-cards.json (29 cards) + medieval-cards-notes.md
_Reviewer agent, Oct 13 2026. Quotes checked against standard texts (Vulgate/Weber, Latin Library, Bibliotheca Augustana). All 29 image licences were re-queried through the Commons API and **all match** the stated licence. All files exist. `late_medieval` is now in the schema era enum._

**Overall:** the selection is strong. The notes correctly dropped *ora et labora*, *memento mori* and *Gaudeamus*, and replaced *Sic transit* with the Kempis line. The Vulgate and Augustine lines are excellent beginner input. The big gaps are structural: there are no glosses, and the metadata format doesn't match the Rome file.

## ERRORS
1. **None of the 29 cards has a `gloss` array.** The design depends on tap-to-gloss. Every Rome card has word-by-word lemma, meaning and parse; the medieval cards have only `vocab_lemmas`. **Fix:** generate glosses (LatinCy/Whitaker), then hand-check them, using the same `{word, lemma, meaning, parse}` format as rome-cards.json.
2. **The metadata format differs from the Rome file.**
   - `teaching_value.score` runs 1–10 here and 1–5 in Rome.
   - The field names differ: `notes`/`dickinson_core_pct`/`non_core_lemmas` here, `note`/`dcc_core_pct`/`non_core` in Rome.
   - Medieval has `vocab_lemmas`; Rome has `vocab_ids`. There's no `rank`.
   - Lemma spellings use u-for-v (`uanitas`, `uariabilis`, `peruolo`), while Rome strips macrons but keeps v.
   - Merging the files will break the sorting, unlock rules and vocab joins.
   - **Fix:** settle on one format (Rome's). Add `teaching_value` to card-schema.json so this is validated. Normalise the lemma keys to v-spelling and no macrons.
3. **q-kempis-transit context is chronologically wrong.** "The later papal formula *Sic transit gloria mundi* echoes it." The papal-coronation formula is attested **from 1409** (Alexander V). That is the same time as the Imitation (c. 1418–27) or earlier, so it can't be "later". **Fix:** "The similar *Sic transit gloria mundi* was chanted at papal coronations from the early 1400s." (See Wikipedia, *Sic transit gloria mundi*, and its sources.)
4. **q-aug-tolle-lege teaching note is wrong.** It says "Two 2nd-conjugation/3rd-conjugation singular imperatives". Both *tollō* and *legō* are **3rd conjugation**. **Fix:** correct the note. The image is also Gozzoli's *Departure for Milan*, not the garden scene. The notes admit this. Gozzoli's San Gimignano cycle includes the actual conversion scene, *Saint Augustine Reading the Epistle of St Paul* (WGA), so use that.
5. **q-ag-dei teaches *misereri* + dative.** That is ecclesiastical usage; classical Latin uses *misereor* + **genitive** (*miserēre meī*). The tag `dative_with_misereri` would teach a non-classical rule as if it were standard. **Fix:** rename it to `misereri_dative_eccl`. Add a note: "classical: + genitive (cf. Ps 50 *miserēre meī*)."

## SHOULD-FIX
6. **q-heloise-meretrix has no context for "his".** The full sentence begins *Etsi uxoris nomen sanctius…* and mentions **Augustus, ruler of the world**, offering marriage. Without that, *illīus imperātrīx* is opaque. **Fix:** say in the context that "his" means the emperor Augustus, as a hypothetical suitor. Also normalise *Kārius* (MS spelling *karius*) to *Cārius* and note the spelling.
7. **q-magna-carta-39 needs notes on its edits.**
   - The ellipsis hides five verbs (*aut disseisiātur, aut utlagētur…*).
   - The MS spelling *terre* has been normalised to *terrae*.
   - *imprisonētur* and *disseisiātur* are Anglo-Norman legal coinages. Say so, so learners don't treat them as Latin vocabulary.
   - *homo* should be *homō*.
8. **q-bede-sparrow is a fragment.** The *cum*-clause is cut off, which hides that *pervolāverit* is a **perfect subjunctive** ("when … has flown through"). The translation "flies" and the tags miss this. **Fix:** give the full *cum* clause, or tag `cum_subjunctive (preview)`.
9. **Some cards are too hard for the "Later" units they sit in.**
   - q-boethius-rota: 25% core vocabulary.
   - q-einhard-aachen: 43%, and it's a noun phrase, not a sentence.
   - q-vulg-vanitas: 29%, though that is one repeated rare word, which is fine.
   - q-abelard-dubitando: 50%.
   - **Fix:** keep these as preview/reading items, or drop Einhard. The Rome review proposed the rule "anchor if core ≥80% and the target grammar has been taught"; apply it here too.
10. **Check these readings against a print edition:**
    - Abelard, *Sic et non* prol.: many editions read *Dubitando **enim**…* rather than *quippe*. Check against Boyer & McKeon.
    - Dante, *Monarchia*: "1.14.11 (Latin Library numbering)". Give the standard Shaw/Ricci numbering. The idea that mankind is best off ruled by one runs through 1.5–1.8, so check the exact locus.
    - Einhard: the MSS have *genetrīcis* where the card prints *genitrīcis*.
11. **Images:**
    - **Crops:** five images need crops before the 3:4 layout (Monte Cassino 16:9, Magna Carta 3:2, Benedict 1:1, Alcuin 1:1, Angelico 1:2).
    - **TIFFs:** Cleveland is a .tif, so convert it.
    - **CC BY-SA 4.0:** the Abelard/Héloïse painting photo needs the photographer credited and a share-alike notice on the derivative.
    - **Reuse:** the Bede St Petersburg image is used twice.
    - **Off-period images:** a 1634 Vanitas still life, Rembrandt and Champaigne aren't medieval. That's acceptable as reception art, but label them "later depiction" so the card doesn't imply they're contemporary.
12. **Attribution confidence is inconsistent.** Dies irae is "traditional", which is fine since the Thomas of Celano authorship is uncertain, but `person` should say "attrib. Thomas of Celano". Aquinas *De modo studendi* is "traditional", correctly, but explain in a note that its authenticity is doubtful. Bede's Gregory anecdote is correctly "traditional", and it rightly avoids the misquote *non Angli sed angeli*. Add that as a teaching note.
13. **Unit 9 grammar:** the passive-voice unit has many Vulgate perfects and imperatives, but only *fīat … facta est* and *sānctificētur* actually show the passive. That's fine as review, but add *facta est lūx* (perfect passive) as U9's first-sighting anchor.

## NITS
14. Benediktbeuern is where the Codex Buranus was **found**. It was probably **written** in South Tyrol or Carinthia.
15. Bede's "first history of the English" should be "first history of the English church and people". He entered Wearmouth at seven, then moved to Jarrow.
16. Orff's *Carmina Burana* premiered in 1937. The context is correct.

## Dialectic: medieval selection
- **Thesis:** liturgical and Vulgate Latin plus famous medieval lines give the "medieval West" layer. They are repetitive, simple, high-frequency and culturally central. They are *easier* than Virgil, so a learner can read real texts sooner.
- **Antithesis:**
  - Most of these cards are religious texts. That's a narrow picture of the medieval West: it leaves out law, science, letters, student satire and chronicles.
  - Ecclesiastical Latin differs from classical Latin (*miserēre nōbīs*, *quia* for indirect statement, Vulgate Hebraisms). Mixing the two without labels teaches inconsistent rules.
  - Lines known through Orff or liturgy ("O Fortuna", "Dies irae") risk being recognised as songs rather than read as Latin.
  - Without glosses, the cards are just quotes with a picture.
- **Synthesis:**
  1. Add a `register` field (classical / ecclesiastical / medieval-legal) and show a small badge. Make grammar notes register-aware.
  2. Diversify about 30% of the cards: Magna Carta (kept), a university statute, Gesta Romanorum stories, the Archpoet's *Estuans*, a Hildegard letter, a colophon, and a Bede miracle narrative as a CI reading.
  3. Use the repetitive Vulgate passages (John 1, Genesis 1) as **multi-sentence graded readings**, not one-liners. They are ideal comprehensible input.
  4. For song texts, unlock the audio only after the learner has parsed the line, so recognising the tune doesn't replace reading the Latin.
