# Latin Through Rome & the Medieval West — Game Design Framework

## 1. Design principles (learning science)
- **Comprehensible input first** (Krashen; Ørberg's *Lingua Latina per se Illustrata* model): every lesson opens with a short, mostly-understandable Latin passage plus an image. Grammar gets named only after the learner has already met it in context.
- **Retrieval practice** (Roediger & Karpicke): learners produce answers instead of rereading. Recall comes before recognition whenever possible.
- **Spaced repetition**: FSRS (stability, difficulty, due date) schedules **lemmas and grammar skills**, not every surface form; reading exposures count as implicit reviews. Retention target 0.85–0.9, user-adjustable. A daily "Review" pulls due items from across all units.
- **Interleaving and varied practice**: within a session, exercise types and earlier topics are mixed.
- **Dual coding and elaboration**: each word or structure is tied to an image plus a historical anchor (person, quote, place).
- **Desirable difficulty with a safety net**: target about 85% success. The difficulty adjusts to the learner's accuracy.
- **Output and listening**: classical (restored) pronunciation audio, with an optional ecclesiastical toggle. Learners also speak and dictate.

## 2. Learner journey
1. **Onboarding (2 min)**: pick a goal (read Caesar / read medieval texts / general) and a pronunciation style, then a 5-item placement check.
2. **Map**: a timeline map moving from Republic → Empire → Late Antiquity → Medieval West. Each unit is a "province" or era node.
3. **Daily loop (5–15 min)**: Review due cards → one new lesson → a short "Codex" story read → a streak tick.
4. **Unit end**: a "Triumph" boss reading (an adapted authentic text) unlocks the next era plus a collectible artifact card.
5. **Long arc**: adapted texts → lightly glossed originals (Caesar, Martial, the Vulgate, Bede, Carmina Burana).

## 3. Structure
Unit (era/theme) → 5–7 Lessons → each lesson has 8–15 exercises. Each unit has:
- a **Grammar strand** (1–2 structures)
- a **Vocab strand** (40–60 words, frequency-ranked from the Dickinson College Core Latin Vocabulary)
- a **History strand** (3–6 anchor cards)

| # | Unit (setting) | Grammar | History anchors |
|---|---|---|---|
| 1 | Roma: The City | sum/est, 1st-decl. nom., word order freedom | SPQR, the Forum, Romulus & Remus |
| 2 | Familia | 1st/2nd decl. nom/acc, 3rd-person present | paterfamilias, domus, Cornelia "these are my jewels" (Valerius Maximus 4.4 pr., *haec … ornamenta sua*) |
| 3 | Legio | 1st/2nd conj. present, plurals | Caesar; *Gallia est omnis dīvīsa in partēs trēs* as a **preview/exposure** quote with full glosses (it needs the 3rd decl. and the perfect passive participle). Becomes a plain review card after Unit 5. |
| 4 | Forum & Senate | genitive/dative, adjectives | Cicero, *Ō tempora, ō mōrēs* (Temple of Jupiter Stator, 63 BC) |
| 5 | Gods & Temples | 3rd decl., prepositions + abl. | Pantheon, Vesta, Jupiter |
| 6 | Empire | imperfect & **perfect**, *possum* | Augustus, *Res Gestae*, coins; perfect-tense first sighting: Caesar's *Vēnī, vīdī, vīcī* |
| 7 | Poets | future, pronouns, imperative | Virgil, Horace *carpe diem* (imperative first sighting), Catullus |
| 8 | Philosophers | infinitives, indirect statement intro | Seneca, Marcus Aurelius (Greek!—flag it), Lucretius |
| 9 | Christian Rome & the Fall | passive voice; imperative review | Constantine *in hoc signo vinces*, Augustine *tolle, lege* (imperatives), Jerome's Vulgate |
| 10 | Monks & Manuscripts | relative clauses, review | Benedict *ora et labora* (later motto, flag it), Bede, Book of Kells, Charlemagne |
_Grammar moves per review-1 §5: perfect moved from Unit 7 to Unit 6; future moved from Unit 6 to Unit 7._

### Units 11–14 (later units: all earlier grammar may appear)
The medieval deck already had cards in units 11 and 12 (Abelard, Heloise, Hildegard, *O Fortuna*, *Dies irae*, the Archpoet; Magna Carta, Aquinas, the Paris statute of 1215, Kempis, Dante's *Monarchia*, *Gesta Romanorum*). Until now the viewer showed them under Unit X. Batch 7 adds four units on top of the original ten. The first two cover medieval material by period; the last two are themed units drawing on every era.

| # | Unit (setting) | Era / theme | Grammar strand | History anchors |
|---|---|---|---|---|
| 11 | **Scholae**: Schools, Universities & Songs | `high_medieval`, about 1100–1300 | subjunctive (jussive, hortatory), indirect questions, comparative & superlative, ablative of comparison | Anselm (*quō nihil maius*), Bernard of Chartres' dwarfs on giants, Abelard & Heloise, Hildegard, Carmina Burana (*O Fortuna*, *In taberna*, *Omittāmus studia*), *Dies irae*, *Stabat Mater*, Aquinas' five ways, Bernard of Cluny |
| 12 | **Rēgna**: Kings, Charters & Books | kings and their books from Charlemagne (800) to about 1450; mostly `late_medieval` | deponents (and ablative with *ūtor* etc.), gerundive, gerund, pluperfect, *dum* clauses | Charlemagne's coronation and his writing tablets (Einhard), Alfred and his children's books (Asser), Magna Carta, Declaration of Arbroath, Oresme on the king's coinage, Petrarch's letter to Cicero, Dante, Richard de Bury, Thomas à Kempis, *Gesta Romanorum* |
| 13 | **Iūs**: Law & Justice | thematic, all eras (Twelve Tables to Bracton) | future imperative (the "you shall" of laws), ablative absolute, impersonal verbs, perfect infinitive, review of subjunctive and deponents | Twelve Tables (*itō*, *estō*), Cicero, Tacitus on laws in a corrupt state, Ulpian, Paul & Gaius in the Digest (*oportet*, *licet*, *ūtitur*), Justinian's Institutes and Code, Bracton, *quod omnēs tangit* |
| 14 | **Scientia**: Humanists & Scientists | `early_modern`, about 1450–1700 (new era) | full review: all grammar | Erasmus, More's *Utopia*, Columbus' letter, Copernicus, Galileo, Descartes, Spinoza, Newton, Comenius, the Gregorian calendar |

Notes:
- The grammar tags for units 11–13 are now set in `content/rome_meta.py` `TAUGHT` (previously 99 = preview only); `gerund` was added at 12. The batch 7/8 builds still carry the same override.
- Unit XI–XIII cards target the grammar they actually contain: medieval-cards were given explicit `grammar_target` by `content/medieval_units_grammar.py`, and `batch8-cards.json` adds 11 cards built around the unit grammar. Moved: Bernard of Chartres (X→XI), Einhard's writing tablets (VIII→XII, extended with the gerundive *litterīs effigiendīs*), Charlemagne's acclamation and Asser's book contest (X→XII).
- `early_modern` was added to the era enum in `card-schema.json`.
- Some existing unit-12 cards (Magna Carta, Aquinas, the Paris statute) carry era `high_medieval`; unit = theme, era = date, so that is fine.
- Candidate themes for later units: Mottos & Phrases still in use, Church Latin in liturgy, Latin in science names (Linnaeus).

## 4. Exercise types
- **Read & See**: CI passage plus image. Tap any word for a gloss. Comprehension check comes after, then a 30-second explicit **Nota bene** and processing-instruction drills.
- **Match**: Latin ↔ English, or Latin ↔ image (fast warm-up).
- **Choose the ending**: pick the right case/verb ending in context. This drills morphology.
- **Build the sentence**: drag tiles. Several word orders are accepted, so learners absorb Latin's free word order.
- **Translate (typed)**: Latin→English and English→Latin, with fuzzy matching and synonym lists.
- **Listen & type**: dictation using restored-pronunciation audio.
- **Speak**: read aloud. Speech recognition gives a loose score that's optional.
- **Parse it**: identify case/number/person/tense (a grammar-nerd mode).
- **Quote completion (Cloze)**: fill the missing word in a famous quote. Reveals the history card.
- **Who said it?**: match a quote to a person or era (history recall that reinforces vocab).
- **Derivative detective**: Latin root → English/Spanish/French derivatives.
- **Inscription/Coin read**: decode abbreviations on a real artifact image (e.g., IMP CAESAR DIVI F).
- **Story choice**: a branching mini-story where comprehension choices change the outcome.

## 5. Progression and rewards
- **XP** rewards retention (FSRS stability gains) and reading minutes rather than raw volume, with a bonus for recall-type exercises. A **Streak** has one "Vestal flame" freeze per week.
- **Ranks** follow the *cursus honorum*: Civis → Quaestor → Aedilis → Praetor → Consul → Censor. Then medieval: Scriba → Monachus → Magister → Doctor.
- **Collectible cards (Museum)**: each history card unlocks the first time its quote or word is mastered. Sets complete era "galleries."
- **Mastery levels per card** are driven by SRS stability: Novus → Discipulus → Peritus → Perfectus (renamed so it doesn't clash with the *Magister* rank). Gold borders mark mastered cards.
- **Triumphs**: unit boss readings. A laurel wreath badge rewards completing them with ≥80% accuracy.
- **Weekly Leagues** (optional, off by default): named after Roman provinces.
- **No punishing hearts**: mistakes simply schedule an earlier review. Soft limits, positive tone.

## 6. How history attaches to language
- Every vocab item may have `anchors` → card IDs (e.g., *alea* → Caesar "alea iacta est").
- Every grammar point has a "first authentic sighting" card (e.g., the perfect tense → *veni, vidi, vici*).
- Quotes unlock at **≥70% vocab known, with full glosses for the remaining words** (a glossed preview exposure; 70% alone is not comprehensible, per Hu & Nation 2000). They become **plain, unglossed review** once **≥90%** is known (`unlock_rule.min_vocab_known` 0.7, `review_threshold` 0.9).
- Context blurbs are capped at 40 words (schema: `maxLength` 260 chars as a proxy). Optional "Lege plura" (read more) expands them.
- **Vocab anchors** are defined in the schema (`$defs/vocab`).
- **Authenticity flags**: `attribution_confidence` = verified | traditional | apocryphal, plus a note (e.g., *in hoc signo vinces* comes via Eusebius, originally Greek).

## 7. Card UI notes (for the UI agent)
- Portrait card, ~3:4. **Cut-outs only for 3D objects** (statues, coins, artifacts) that pass a matte QA check. 2D works (paintings, frescoes, manuscripts) get arched or torn-edge masks. Cut-outs may break only the centre ~60% of the top edge; the label area and text band are a **safe zone** images can't enter.
- **Two modes:** *Learn* shows translation and tappable glosses on the front; *Review* shows Latin only, and the card flips to reveal the answer.
- Every card has a "see in museum" link to restore the object's context.
- Layering: background color/texture keyed to era → cutout image → Latin (large serif) → translation → 1–2 line context → attribution footer.
- Sources: Wikimedia Commons, the Met, Rijksmuseum, Art Institute of Chicago, Getty, Smithsonian; check each record's PD flag. British Museum is CC BY-NC-SA (non-commercial), so avoid it. Do background removal offline; `image.license`, `image.credit` and `image.source_url` are required.

## 8. Tech sketch
Static PWA (e.g., SvelteKit/React + IndexedDB). Content lives as JSON (cards, lessons, vocab). The FSRS scheduler runs client-side via the `ts-fsrs` library. Audio is pre-generated. Works offline.
