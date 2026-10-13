# Review: content/rome-cards.json (36 cards) + rome-cards-notes.md
_Reviewer agent, Oct 13 2026. Every quote was checked against standard texts. I re-fetched Agricola 30 and Valerius Maximus 4.4 from the Latin Library. All 22 image licences were re-queried through the Commons API, and **all of them match** (CC0 / Public domain)._

**Overall:** the Latin wording and citations are accurate. All 36 quotes and their book/line numbers are correct. The main problems are which unit each card sits in compared with the grammar sequence, a couple of wrong context blurbs, and a few metadata placeholders.

## ERRORS
1. **q-catullus-vivamus, the context misreads the poem.** "our night lasts forever" is wrong. *nox est perpetua ūna dormienda* (5.6) means **death**: one never-ending night of sleep. It is not a night of love. **Fix:** "…suns can set and rise; for us, once our brief light sets, there is one endless night to sleep. So kiss me."
2. **i-titus-spqr has a macron error and a bracket error.**
   - *Tītus* should be **Tĭtus/Titus** (short i).
   - `F[ILIO]` uses square brackets, which in Leiden convention mark **restored lost text**. An abbreviation that has been expanded goes in parentheses: `F(ILIO)`.
   - The gloss is also missing *VESPASIANO*.
   - Source: Leiden conventions; L&S *Titus*.
3. **q-horace-sapere has placeholder image metadata.** It has `credit: "see existing horace card"` and `source_url: "https://commons.wikimedia.org/"`, and q-horace-modus is the same. **Fix:** copy the full credit and URL from the Horace card in cards.js (File:Horace,_Odes,_Florence,_Plut._34.1.jpg).
4. **Many cards don't fit the unit grammar sequence.** The design's sequence is U1 sum · U2 1st/2nd decl. · U3 1st/2nd conj. · U4 gen/dat · U5 3rd decl., prep+abl · U6 impf/fut, possum · U7 perfect · U8 infinitives · U9 passive · U10 relatives.
   - **q-virgil-arma (U3)** needs the perfect (*vēnit*), a relative clause, ab + abl and a 3rd-conj. verb (*canō*).
   - **q-tacitus-solitudinem (U3)** needs 3rd-decl. accusatives (*pācem, sōlitūdinem*) and *faciunt*, which is 3rd -iō.
   - **q-seneca-docent:** the note says it is "usable from Unit 3", but *discunt* is 3rd conj. That fits U5 at the earliest.
   - **q-tacitus-urbem (U6)** and **i-pantheon (U1, *fēcit*)** use the perfect, which is taught in U7.
   - **q-suetonius-alea (U6)** uses the perfect passive, which is taught in U9.
   - **q-virgil-forsan (U7)** uses the future. That is taught in U6 per game-design.md, so the note's "Unit 7 future sighting" contradicts the design.
   - **q-ovid-gutta** and **q-catullus-odi (U7)** use the passive (U9).
   - **q-cicero-historia (U4)** uses 3rd-decl. genitives (U5).
   - About 8 cards use relative clauses before U10.
   - **Fix:** split `grammar_tags` into `target` (must already be taught) and `preview` (glossed, not tested). Then re-home each card so its unit is at least the latest of its `target` tags. Either way, add a build-time lint for this.
5. **Notes: *Quintili Vare, legiones redde* was dropped by mistake.** The quote does exist in **Suetonius, Aug. 23.2**. The Latin Library text spells it *Quintili/Quinctili*, so the string match probably failed on the spelling. It's a perfect vocative + imperative card for U7. **Fix:** search for "legiones redde" and restore the card as `verified`.

## SHOULD-FIX
6. **Some teaching_value scores are inflated.**
   - **q-cicero-historia** scores 5 with only 58% core vocabulary and five non-core words. It is also a fragment, because it continues *quā vōce aliā nisi ōrātōris…*. Make it score 4 and add "…".
   - **q-virgil-arma** scores 5 but hides *fātō profugus Lāvīniaque* behind the ellipsis.
   - **Fix:** apply the rule "score 5 only if core ≥80% and all target grammar is taught by the card's unit".
7. **q-horace-sapere translation:** "Well begun is half done" is a proverb, not a translation. Use "He who has begun has half the deed done; dare to be wise, begin!"
8. **q-catullus-odi:** "Why do I do this, you perhaps ask?" turns an **indirect** question into a direct one. Use "Why I do this, perhaps you ask." That keeps the subjunctive *faciam* meaningful.
9. **q-suetonius-alea:** add to the note that the manuscripts read *iacta alea est*, while Erasmus emended it to *iacta alea esto* ("let the die be cast"). That matches the Greek in Plutarch. It is good material for teaching the textual tradition.
10. **q-cicero-cedant:** Off. 1.77 reads *laudī*. The famous version, ending *linguae*, is in Pis. 72–74 and is also quoted by Quintilian. Mention both in attribution_note.
11. **q-tacitus-solitudinem:** the text begins *atque ubi…*. Most editions number it **Agr. 30.5**, with some using 30.4. Keep 30.5 and note the variation.
12. **Unit coverage is uneven.** U1 has 1 card, U5 has 2 and U3 has 3, while U7 has 9 and U6/U8 have 6–7 each. The early units need the most easy authentic material. **Fix:** source U1–U3 from inscriptions (SPQR, tombstones such as *D·M*, *S·T·T·L*), simple coin legends and Ørberg-style adapted lines.
13. **Images:**
    - **1:1 aspect:** the Pompeii memento-mori mosaic is 1:1, which the schema says to avoid. Crop it to 3:4.
    - **Wrong treatment:** the sarcophagus (a 2:1 relief) is marked `transparent:true`. A frieze should use a mask or strip treatment, not a cut-out.
    - **Pantheon file:** the Pantheon image is a .tif, so convert it.
    - **Stand-in images:** Pseudo-Seneca, the lamp, "know thyself" (Greek) and the Octavian coin for *Exēgī* teach nothing about the quote. They are the swaps the notes already flag.
    - **Reused images:** the cuirass torso is used for both Tacitus and Juvenal *mēns sāna*, the Cicero bust ×4, Seneca ×4 and the Virgil mosaic ×3. Reused images weaken image-to-memory links, which are the whole point of dual coding.
14. **Malformed vocab_ids:** `"tu + -que"` (Ovid edax). Split it into `tu` and `-que`.
15. **Confidence labelling:** *verified* is used for speeches the author composed (Tacitus/Calgacus, Laocoön). "verified" should mean the *text*. Consider separate `text_verified` and `speaker_historicity` fields.

## NITS
16. The Pantheon expansion *Lūciī* should be the classical **Lūcī** (gen. of -ius nouns in republican/Augustan Latin).
17. *Ītaliam* has a long Ī only for the metre (normally Ĭtalia). Add a gloss note so learners don't absorb it.
18. Livy's 390 BC is the Varronian date. The real date is probably 387/386 BC.
19. *salūs populī*: "17th-c. motto" is a bit vague. Name Selden or Locke.
20. Juvenal *panem*: say that "it" (*optat*) refers to *populus*.

## Dialectic: is the selection serving Latin or trivia?
- **Thesis:** famous, sourced lines, ranked by grammar value and core vocab %, give motivation (cultural payoff) plus authentic input. Every card has a grammar tag. Most of the quotes are excellent sentence patterns.
- **Antithesis:**
  - Famous quotes are a *biased* sample. They are poetic, compressed and full of rare forms (gerundives, subjunctives, deponents, archaic *-ēre*).
  - Read in isolation they are **decontextualised fragments**. Learners memorise the English gist ("tempus fugit") rather than processing the Latin, which makes them cultural trivia in Latin clothing.
  - 15 of the 36 cards need grammar that hasn't been taught yet in their unit.
  - Vocabulary-coverage research (Nation; Hu & Nation 2000) suggests that 50–67% coverage cards (*Gutta*, *edāx*, *Exēgī*, *Vae victīs*) cannot be read; they can only be decoded with the gloss.
- **Synthesis:**
  1. **Two roles.** Use *anchor* quotes, each with a `target` grammar the unit has already taught and core ≥80%, as tested material. Use *preview* quotes as glossed exposure only, not drilled for production.
  2. **Context around every quote.** Wrap each quote in a 2–4 sentence adapted Latin lead-in using known vocabulary. Ørberg-style: *Caesar ad Rubicōnem venit. Exercitus exspectat…*. That turns trivia into input.
  3. **Recycle rather than collect.** Drill a pattern from each anchor (e.g. *sunt bona, sunt mala* → learner builds *sunt magna, sunt parva*), and schedule both the pattern and the lemmas in FSRS.
  4. **Weight the early units with simple real Latin** (inscriptions, coins, epitaphs), and keep Virgil and Horace for U6+.
  5. **Lint in build.py:** unit ≥ max(taught unit of the target tags), core% ≥ threshold, and no placeholder metadata.
