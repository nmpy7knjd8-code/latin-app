# Grammar double-check: batch7 (77), batch8 (11), 8 retagged medieval cards, Einhard
Reviewer: independent critic, Oct 18 2026, ET. Status: not published, not pushed.

## Method (dialectic)
- **Thesis:** a tag counts if the form occurs somewhere in the Latin.
- **Antithesis:** a learner who is told "this is X" must find a genuine, correctly named X. A loose label, such as calling an ablative of respect "means", or a command acc.+inf. "indirect statement", teaches the wrong thing.
- **Synthesis:** a tag stays only when it is the correct category for that form in this context.
  - Where the source's syntax differs from the excerpt (CJ's *ut*-clause, Kempis' indicative indirect question), the card keeps the tag and states the difference in the note.
  - Translations follow the Latin tense, mood and case unless the English idiom is clearly flagged.

## Checks
- **Latin text:**
  - batch8: all 11 texts were checked against the cached sources in content/batch8_src (Anselm Prosl. 2, CB 75, Kempis 1.23.4, Oresme ch. 6, Petrarch Fam. 24.4, Asser 75, Dig. 1.1.1 pr / 50.17.55 / 50.17.144, Tac. Ann. 3.27, XII Tab. VIII.12).
  - Dante, Mon. 1.14.11 ("Unde sequitur humanum genus optime se habere cum ab uno regitur") was checked against la.wikisource / Treccani.
  - Einhard 25, including the extended "ut, cum vacuum tempus esset, … adsuesceret" clause, matches the Latin Library.
  - CJ 5.59.5.2 matches.
  - Macrons are correct throughout.
- **Unit order:** lint is OK for batch4/7/8. The medieval retags respect TAUGHT: U11 cards use only U≤11 targets, with deponent and gerund as previews only.
- **rome_meta.py schedule:** the spot-check passed.
  - Participles come in U9 before the ablative absolute in U13.
  - Subjunctive (U11) comes before jussive and indirect question (U11) and before the dum, gerund and gerundive group (U12).
  - The pluperfect is in U12.
  - batch7_build overrides match.

## Errors found → fixed
| card | issue | fix |
|---|---|---|
| q-asser-codicem | comparative *citius* translated "fastest" | "more quickly" |
| q-te-deum | *Deum* is acc. in apposition to *tē*; translation used a vocative ("O God"); gloss muddled | translation "We praise you as God"; gloss "as God, acc. (in apposition to tē)"; context explains both and notes the traditional "O God" |
| q-bernard-stat-roma | *nōmine* is an ablative of respect, tagged ablative_means | target → `ablative`; gloss/context "in name … ablative of respect" |
| q-seneca-medea | perfect *statuit* translated as present "decides" | "Whoever has decided … even if what he decided was fair" |
| q-xii-in-ius | *itō* glossed 2nd sg. only; in the law it is (also) 3rd sg. | gloss "2nd/3rd sg."; context notes both persons |
| q-cj-omnes-tangit | in the Code the clause depends on *ut* (purpose/result subj.), not jussive | note added explaining that it reads as jussive only as a detached maxim |
| q-xii-nox-furtum | *iūre* is an ablative of manner, tagged ablative_means; *occīsit* is subjunctive like *faxsit* | target → `ablative`; gloss "(manner)" and "archaic 3rd sg. subj." |
| q-archpoet-taberna | context said "Mihi est prōpositum … dative of possession", but the Latin is *Meum est* | context now names the possessive adjective *meum* and *ōrī* as a dative after *proxima* |
| q-aquinas-tardiloquum | *iubeō tē esse* is a command (acc.+inf.), not indirect statement | target → infinitive, accusative; stale tag dropped; context explains |

## Verified correct (no change)
- **batch7 U11–U14:** all other cards. Notable correct points:
  - ablative of comparison: Felicior, Anselm
  - gerundives: Seneca discendum, Aquinas dīcendum, Dig. benigniōra praeferenda
  - deponents: patitur, loquitur
  - Galileo perf. pass. inf.
  - Newton gerunds
  - Gravissimas jussive
  - Columbus *habitātās*
- **batch8:**
  - Anselm: *quō* is an ablative of comparison; *possit* is a characteristic subjunctive.
  - Omittāmus/carpāmus are hortatory.
  - Kempis: *operārī* is a deponent; dum + indic. The note on the indicative indirect question was already present.
  - Oresme: a gerund with a direct object.
  - Petrarch: *īrāscimur* deponent vs *dēlectāmur* passive.
  - Asser: *ūtuntur* + abl.; *didicēre*.
  - Dig. operam: *nōsse* is a perfect form with present meaning; *dēscendat* is an indirect question; *oportet* is impersonal.
  - Licet and suō iūre are correct.
  - Tacitus: a verbless ablative absolute.
- **Medieval:**
  - Magna Carta *capiātur* and Paris *nōn legantur* are true independent jussives.
  - Heloise: *vidērētur* is impf. subj.; comparatives.
  - Abelard: gerunds in the ablative of means.
  - Mon. unum: acc.+inf. after *sequitur*; *optimē* is a superlative.
  - Gesta: ablatives of means.
- **Einhard (U12):**
  - The gerundive *litterīs effigiendīs* is dat. after *adsuēsceret*.
  - The purpose *ut*, *cum … esset* and the imperfects of repeated action are correct.

## Build / QA
- Rebuilt with:
  - medieval_units_grammar.py (idempotent; reran twice)
  - batch7_build
  - batch8_build
  - batch4_build
  - Lint is OK.
- Schema: 0 errors across all 8 decks.
- Overflow at 390x844, 430x932, 375x667 and 390x664:
  - 403 cards; all 88 batch7+8 cards load.
  - No overflow and no clamped text.
  - No horizontal page scroll.
  - The picker fits.
  - No JS errors.
- Fixes were re-verified in the built JSON.
