# Batch 9: independent dialectical critic and grammar double-check

Date: Tue Oct 20, 2026, about 8:40 PM ET. Scope: content/batch9-cards.json, 50 cards (12 constructed vocab cards in Units 1–10, 38 quotes in Units 11–14). Fixed locally only. **No commit, no publish.**

## Dialectic
- **Thesis:** batch 9 was built with its own source checks (batch9_src, critic.json), and the build lint is OK, so the quotes and grammar should be sound.
- **Antithesis:** critic.json reports MISSING on 8 quotes. A lint can't tell whether a card has silently changed the grammar of a quote, whether a context sentence describes the grammar wrongly, or whether macrons are missing in prose. Batches 7 and 8 both had errors of exactly this kind.
- **Synthesis:** 7 of the 8 MISSING flags are disclosed spelling normalisations (ae/e, u/v, j/i, phylosophica, poenitentiam) or an inscription (Harvey) and are acceptable. The 8th, Kempis, was a real alteration of the quote. Reading every card closely turned up 4 more real errors. All 5 are now fixed in batch9_cards.py and rebuilt with batch9_build.py ("lint OK").

## Errors found and fixed (5 cards)
| Card | Problem | Fix |
|---|---|---|
| q-kempis-utinam | The Latin was changed from the source *per unam diem* to *ūnum*, which is not verbatim, and the gloss parsed it as m. | Restored *ūnam* and glossed *ūnam* / *diem* as acc. sg. f. The note now explains that *diēs* is feminine here. |
| q-kepler-sexangula | The context said the neuter plurals agree with "an understood word for 'stars' of snow". Kepler's word is *asterisci* (masc.), and *stellae* would be fem., so neither can take a neuter adjective. | The context now says *quīnquangula / septangula / sexangula* are neuter adjectives used as nouns, "five-cornered (shapes)". Checked against the Latin Library Strena. |
| q-xii-sepelito | The context had "nē … neve" without the macron. | Changed to *nē … nēve*. |
| q-gaius-omnes-populi | The context had "ius cīvīle" and "ius gentium". | Changed to *iūs cīvīle* and *iūs gentium*. |
| q-pico-adam | The gloss lemma was *peculiāris*. | Changed to *pecūliāris*. |

## Verified correct (45 cards, plus the rest of the 5 fixed ones)
- **Quotes checked word for word against the saved sources in batch9_src:**
  - Bernard, De laude 11.23
  - Oresme, De moneta 6
  - Petrarch, Fam. 24.4
  - Kepler, Strena
  - Kempis 1.23.2
  - Einhard 24
  - Asser 104
  - Arbroath
  - de Bury 1
  - Magna Carta 40
  - Dante, Mon. 3.16.10
  - XII Tables 10.1 and 4.2
  - Cic. Leg. 3.8
  - Dig. 1.4.1, 1.1.9, 50.17.54
  - Pliny 10.97.2
  - Tac. Germ. 12
  - Livy 3.34.6
  - Bacon NO 1.3
  - Spinoza 5.42
  - More, Utopia
  - Luther thesis 1
  - Pico
  - Vespucci
  - Copernicus
  - Aquinas ST I q.2 prologue
  - CB 143
  - Gaudeamus
- **Hymns and carols matched to their standard texts:**
  - Dies irae st. 7
  - Stabat Mater st. 5
  - Quem pastores
  - Puer nobis st. 5
  - Personent hodie st. 4
- **Grammar targets:** every grammar_target is genuinely present in the Latin. For example: *absit* (jussive), *duit* (archaic subjunctive), *mīlitiae* (locative, under future_imperative), *plūs iūris* (comparative + genitive), *cāsū*, *currentis* (present participle).
- **Unit order:** no unknown or out-of-order targets or previews against rome_meta TAUGHT.
- **Glosses:** every gloss word occurs in the Latin.
- **Facts in context:** all checked and correct, including:
  - Via Appia 312 BC
  - Middleton milestone M P LIII
  - Basilica of Maxentius c. 308 / 312
  - the Cloaca Maxima and the Tarquins (Livy)
  - Kindleben 1781
  - Piae Cantiones 1582
  - Einhard's four courses
  - Asser's 12-inch candles
  - Pope John XXII
  - de Bury as tutor of Edward III
  - Brutus denarius Cr. 433/1
- **Duplicates:** none against any other deck, checked by id, by Latin overlap (>60% shared words) and by image source URL.
- **Images:** every file exists. Licences are CC0, PD, CC BY 2.5/4.0 or CC BY-SA 2.0/3.0/4.0, with credit and licence URL for the CC licences. Each subject matches its card.

## Not changed (judgement calls)
- **q-bernard-plus-potuit:** *plūs* is glossed as a comparative adverb. Reading it as an internal accusative would also be defensible.
- **q-dante-monarchia:** "and of an emperor" renders the ablative after *opus fuit*, which the card's ellipsis leaves out. It is acceptable.
- **Image credits:** some read "Unknown authorUnknown author" (Commons scrape). This is cosmetic. Fix it in batch9_images if wanted.
- **q-gaudeamus learn_more:** it has no verified_http, because the build carries that field over only from the previous build. The URL returns HTTP 200 (checked today).

## Validation
- batch9_build.py: lint OK
- schema: 0 errors across the 50 cards
- unit order: 0 issues
- **Overflow:** `cards/shot_mobile.py` via /tmp/runshot.py, which points playwright at /usr/bin/google-chrome. I recreated that wrapper because /tmp had been cleared.
  - Sizes: 390×844, 430×932, 375×667, 390×664
  - 453 cards at each size
  - vertical overflow [], horizontal 0, clamped 0, page scroll equals the viewport

**Result: PASS after fixes.**
