# Batch 10: independent dialectical critic and grammar double-check

Date: Wed Oct 21, 2026, about 2:45 AM ET. Scope: content/batch10-cards.json, 50 cards:
- 12 constructed vocab cards, Units 1–2
- 38 quotes, Units 11–14

Fixed locally only. **No commit, no publish.**

## Dialectic
- **Thesis:** the producer's critic found the source for each quote, and the build lint is OK.
- **Antithesis:** in batch 9 the worst error was a quote the card had silently altered while its note admitted it, and a lint doesn't catch that. Context sentences that explain grammar or biography also go unchecked.
- **Synthesis:** I checked each card by hand against the saved sources in batch10_src and against standard texts. I found 5 real problems on 4 cards plus one broken link. All are fixed in batch10_cards.py and rebuilt with batch10_build.py ("lint OK").

## Errors fixed
| Card | Problem | Fix |
|---|---|---|
| q-oresme-subtilis | The quote was altered from *ad effigiendum* (Latin Library, De moneta 5) to *effigiandum*, and the note admitted it. Same issue as Kempis in batch 9. | Restored the verbatim *effigiendum*. The gloss now reads "effigiō (medieval effigiāre) … gerund acc. (= effigiandum)" and the note is rewritten. |
| q-anselm-doce | The context said the present subjunctives after *nisi* are there "because the condition is still open". That is wrong: an open condition takes the indicative. | Now explained as the "should … would" (ideal) condition: "unless you should teach me". |
| q-anselm-doce | The extra note said Anselm wrote the Proslogion "as abbot of Bec … around 1078". It dates to 1077–78, while he was still prior; he was elected abbot in 1078 and consecrated in 1079. | Changed to "at the abbey of Bec … around 1077 to 1078, just before he became its abbot". |
| q-dig-locupletiorem | The extra note said Pomponius's works "survive only in quotations in the Digest". | Changed to "almost entirely through quotations in the Digest". |
| q-erasmus-querela | The learn_more link `Querela_Pacis` returns 404. | Changed to `Querela_pacis` (HTTP 200 today). |

## Producer's unchecked facts
| Claim | Verdict |
|---|---|
| Pomponius, "2nd century AD", on cards 50.17.206 and .203 | **Correct.** Sextus Pomponius was active under Hadrian through Marcus Aurelius. Both inscriptions match the Latin Library text ("Pomponius 9 ex var. lect.", "Pomponius 8 ad q. muc."). |
| Magna Carta clause 1 "one of the three clauses still in force" | **Correct.** The three are the freedom of the English Church, the liberties of London, and due process (clauses 1, 9 and 29 of the 1297 statute). The context is right that clause 1 sits after *concessisse*. |
| Kempis "Beatus qui horam mortis…" is 1.23.2 | **Correct.** In the Latin Library text it follows *Utinam per unam diem* inside section 2 of chapter 23. The card's *cotīdiē* for *quotidie* is disclosed. |
| Javolenus, about AD 100, head of the Sabinians | **Correct.** Dig. 50.17.202 is "Iavolenus 11 epist.". Pomponius (Dig. 1.2.2.53) lists Iavolenus Priscus as successor to Caelius Sabinus at the head of the Sabinian school. |
| Melanchthon, De laude vitae scholasticae, 1536 | **Correct.** Library catalogues record it as delivered and printed in 1536 ("dicta a D. Melchiore Fendio in promotione Magistrorum"), so it was written by Melanchthon and spoken by Fendt. The opening sentence matches the Latin Library verbatim. |
| Moriae encomium dated 1511 | **Correct** as the date of the first printing (Paris, 1511). The context's "written in 1509 while staying with Thomas More" is also right. The opening sentence matches the Latin Library §1 verbatim. |

## The "Unknown authorUnknown author" credit edits in older decks
I compared each deck with HEAD, card by card and key by key:
- batch4 (3 changes), batch5 (1), batch6 (2), batch7 (5), batch8 (2), batch9 (16), learning (5), rome (4).
- **Only `image.credit` changed.** No ids were added or lost, and no other field moved.
- All new strings are clean, for example "Unknown author · Public domain · via Wikimedia Commons" and "Metropolitan Museum of Art · CC0".
- Schema: 499/499 valid.

Two caveats:
- **Rebuilds will undo the edits.** batch9_build.py and batch10_build.py now contain `fix_artist`, but batch4–8_build.py do not. Rebuilding any of batch4–8 would bring back the doubled credits unless the same function is ported to those scripts. The rome and learning edits are safe, because those decks are only patched directly.
- **One cosmetic leftover:** learning l-bulla reads "Anonymous (Category:Etruscans)". It is harmless and I left it unchanged.

## Verified correct
- **Every quote matches its source verbatim** apart from disclosed spelling normalisations:
  - Fulbert (*dulcidinem*)
  - Bernard of Cluny 1.1
  - Anselm, Proslogion 1
  - Aquinas, ST I q.2 a.3
  - Dies irae st. 10
  - Angelus ad virginem
  - Adeste st. 3
  - Theodulf
  - CB 138 and CB 70
  - Einhard 22 and 25
  - Kempis
  - Magna Carta 1
  - Asser 24 (checked against the Latin Library section markers)
  - Oresme 5 (now verbatim)
  - Petrarch, Fam. 24.4
  - XII Tables 5.3 and 1.2
  - Cic. Leg. 3.2 and 3.5
  - Dig. 50.17.202, .203, .206, .207, .208, with the right jurists (Javolenus, Pomponius, Pomponius, Ulpian, Paul)
  - Newton: General Scholium, Rule 1, Law 3
  - Descartes, Med. 1.1 and 2.1
  - Spinoza 4.67
  - Luther thesis 27
  - Pico
  - Querela pacis
  - Moriae 1
  - Galileo's dedication (*Medicea Sidera*)
  - Melanchthon
- **Grammar targets:** every target is present in the Latin. For example:
  - *prōmat*, *vigilēmus*, *nōn sit* (jussive and hortatory)
  - *legāssit*, *estō*, *iacitō*
  - *pāruerit* + *necesse est*
  - *dēsīsse*
  - *quibus* as an ablative of comparison
  - *ineunte aetāte*
  - *illud … hanc* (demonstratives)
- **Unit order:** the build lint is OK.
- **Glosses:** every gloss word occurs in its Latin.
- **Facts in context and extra notes:** all checked and correct, including:
  - Trajan's Column AD 113, with St Peter on top since 1587–88
  - Ara Pacis 13 BC, reassembled in 1938
  - Caracalla's baths, AD 216
  - Augustus's height limit of about 70 feet
  - Crepereia Tryphaena's doll
  - 225 denarii a year
  - Vespasian's urine tax
  - Chartres fire, 1020
  - Eco and the last line of Bernard of Cluny
  - Dublin Troper and Chaucer's Miller's Tale
  - Oakeley's translation, 1841
  - Newton 1713
  - Spinoza at Rijnsburg 1661–63, died 1677 aged 44
  - Pico aged 23
  - Cosimo II
- **Duplicates:** none against any deck, checked by id, by Latin overlap and by image source URL.
- **Images:** all files exist, and the licences and credits are consistent.
- **Minor, not changed:** the image on q-dig-locupletiorem is a statue of Papinian on a Pomponius card. The alt text labels it correctly, so it is a stand-in rather than a misidentification.

## Validation
- batch10_build.py: lint OK
- tools_validate.py: schema 499/499 valid; manifest 539 images
- **Overflow:** cards/shot_mobile.py via /tmp/runshot.py, at 390×844, 430×932, 375×667 and 390×664.
  - 503 cards at each size
  - overflow [], horizontal 0, clamped 0
  - page scroll equals the viewport

**Result: PASS after fixes.**
