# Review 3: 7 new medieval cards + phonetics_eccl.py / phonetics-eccl.json
_Reviewer agent, Oct 13 2026._

## A. New cards
| id | Text, citation and macrons | Result | Issues |
|---|---|---|---|
| r-vulg-john-1-5 | John 1:1–5. The wording matches the Vulgate (Weber spells *conprehendērunt*). The macrons are correct (*lūcet, tenebrīs, hominum*). | **PASS** | **Should-fix:** "did not overcome it" is a modern rendering of the Greek *katelaben*. For Jerome's Latin *comprehendērunt*, use "did not grasp / comprehend it" (Douay: "did not comprehend it"). Otherwise learners mis-gloss the verb. |
| r-vulg-genesis-1-5 | Gen. 1:1–5. Wording matches. Macrons checked and correct: *inānis, vacua, abyssī, spīritus, ferēbātur, vīdit, dīvīsit, Appellāvitque, vespere, māne, ūnus*. | **PASS** | Good preview tags (*quod esset* = ecclesiastical "that", imperfect passive). U9 is a fair placement for a graded reading. |
| q-gesta-latro | Gesta Romanorum 146 (Alexander and the pirate). The source trail (Cicero, Rep. 3 → Augustine, CD 4.4) is correct. | **PASS*** | **Should-fix:** gloss ***galea* = "galley" as medieval usage**. In classical Latin *galea* means **helmet**, so this is a register trap worth teaching. Also check the verb form *dīceris* against the Latin Library text; some editions have *vocāris*. |
| q-hildegard-aurora | *O nobilissima viriditas*: "Tu rubes ut aurora, et ardes ut solis flamma". Matches the Hildegard Society edition, and the manuscript references are correct. | **PASS** | The macron on *ārdēs* follows Wiktionary's hidden-quantity *ārdeō*. L&S has *ardeo*. Pick one policy (see the *ōrnāmenta* note in review-rome-2). |
| q-colophon-tres-digiti | A widespread colophon formula, sourced to Bibale 18684 (BnF lat. 12234). | **PARTIAL** | The common form is *Trēs digitī scrībunt, tōtum corpusque labōrat*, and *nāvigantibus* is plural in most witnesses. I couldn't load the Bibale record to confirm the singular *nāvigantī* or the *sed* wording. Give the exact Bibale transcription, or mark it "formula; wording varies". The disclosure that the image is a different scribe (Eadwine) is good. |
| q-archpoet-taberna | Archpoet, *Confessio* st. 12 (= CB 191). Wording and macrons are correct (*prōpositum, tabernā, ōrī*). | **PASS** | **Nit:** a better translation is "so that wine may be near the mouth of the dying man" (*morientis*, a substantive participle). |
| q-paris-statute-1215 | Courson's 1215 statutes, *Chartularium Univ. Paris.* I no. 20, p. 78. Wording correct; *legere* = "to lecture on" is well explained. | **PASS** | Note the manuscript spelling *methafisica*. The disclosure that the image shows Bologna is good, but caption it on the card as well. |

## B. phonetics_eccl.py, spot-check of 27 words against Liber Usualis rules
**Correct:** *caelum* CHEH-loom, *cēna*, *Cicerō* CHEE-cheh-roh, *gēns*, *agnus* AH-nyoos, *excelsīs* ehk-SHEHL-sees (xc + front vowel = ksh), *gratia/nātiō* tsee, *scientia* shee-, *suscipe* SOO-shee-peh, *accipiō* aht-CHEE-, *ecce* EHT-cheh, *mihi/nihil* -kee-, *hodiē*, *Christus*, *philosophia* f, *Iēsus* YEH-, *cuius*, *Ave* AH-veh, *lingua*, *quī*.

| # | Issue | Severity |
|---|---|---|
| 1 | **The engine depends on macrons in its input.** *regina* (no macrons) gives **REH-jee-nah**. It should be *rēgīna*, re-JEE-nah. Any medieval card text that lacks macrons will get the wrong stress. **Fix:** fail the build, or warn, when a card's Latin has no macrons, or look the word up in a macronized lexicon first. | error |
| 2 | *ui̯* → "wee". *huic* and *cui* inherit the classical respelling bug (review-phonetics #6). Use "oo-ee"/"KOO-ee". | should-fix |
| 3 | Intervocalic *s*: Italianate usage often voices it (*Iēsus* YEH-zoos, *misericordia*). The Liber Usualis prefers it unvoiced. Document the choice. | nit |
| 4 | It always outputs *x* = ks; *exaudī* is commonly "eg-ZOW-dee". This is documented as a simplification, which is fine. | nit |
| 5 | Vowel length isn't distinguished. That matches Italianate practice, but the UI legend should say so, so learners don't think the classical length marks are wrong. | nit |

## Dialectic: two pronunciations
- **Thesis:** offer an ecclesiastical toggle that follows each card's register. That's authentic for Vulgate, liturgy and Hildegard, and matches how these texts were actually sung.
- **Antithesis:** two systems double the cognitive load for beginners. Medieval Latin was in fact pronounced regionally (French, German and English usages), so "Italianate" is itself an anachronism for the Archpoet or the Paris statutes.
- **Synthesis:**
  - Make classical the default everywhere.
  - Offer ecclesiastical only on cards with `register: ecclesiastical`, labelled "Church (Italian) pronunciation".
  - For non-liturgical medieval texts, keep classical with a short note on regional practice.
