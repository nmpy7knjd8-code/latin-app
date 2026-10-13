# Review: content/learning-cards.json (65 cards), current state
_Reviewer agent, Oct 13 2026. The producer is still verifying quotes and images. This reviews the file as it stands now._

**Status:** 0 of 65 images are verified (every `license_status` says "verify"). No card has a `gloss` array. 44 of 65 cards have an empty `vocab_ids`, so FSRS and the unlock rules have nothing to work with.

## ERRORS
1. **g-infinitive has the wrong wording.** Seneca Ep. 96.5 reads ***Atqui vīvere, Lūcīlī, mīlitāre est.*** There is no *mī*. **Fix:** "(Atquī) vīvere, Lūcīlī, mīlitāre est." Source: Latin Library, sen/seneca.ep16 (Ep. 96).
2. **g-impf teaches the imperfect but its quote contains none.** The Suetonius line (Aug. 28.3, wording correct) has an infinitive (*relinquere*) and a pluperfect subjunctive (*accēpisset*). Only the constructed sentence has *-bā-*. **Fix:** use the Suetonius line as context only. Use an authentic imperfect instead, e.g. Livy 1.4 *…lupam … ad puerīlem vāgītum cursum flexisse* is not suitable either. Simplest: two constructed imperfects plus a real one such as *Rōmae … rēgēs habēbat*. Or move this card to a pluperfect unit.
3. **g-imperative has the wrong era.** It is tagged `era: "republic"`, but Odes 1 is from 23 BC, and rome-cards uses "empire". **Fix:** change it to empire.
4. **Real legends are labelled as constructed.** i-coin-divi-f (CAESAR DIVI F, Octavian's denarii, RRC 534–540) and i-karolus (KAROLVS IMP AVG, Charlemagne's portrait deniers) are authentic legends. They are marked "Constructed teaching sentence". **Fix:** give each a real source (e.g. RRC/RIC/MEC number) and set attribution "verified".
5. **g-adj mixes a constructed example with a real citation.** The Latin is constructed (*vir bonus, fēmina bona, templum bonum*), yet the card carries `source` Quintilian 12.1.1 + "verified". **Fix:** mark the Latin as constructed and put the Cato/Quintilian line in `context` with its citation.
6. **No glosses, and two-thirds of the cards have no vocab_ids.** Tap-to-gloss and SRS scheduling can't work. **Fix:** generate them, the same blocker as the medieval review.

## SHOULD-FIX
7. **i-chirho:** the Vulgate spells it ***Ego sum Alpha et Omega*** (Apoc. 1:8), not with Greek letters. Keep ☧/α/ω for the coin image only.
8. **g-future, *Nōn omnis moriar*:** *morior* is a 3rd-*iō* **deponent**, so *-ar* is a passive-form ending. That's a confusing first future. **Fix:** lead with a regular active form (e.g. *regam, regēs, reget*). Keep Horace as the "sighting". It is in unit 7, but the design teaches the future in unit 6.
9. **g-perf-rg** (perfect, unit 6) is out of step with the design (perfect = unit 7). Same issue as review-rome #4.
10. **Image licences:** the Vindolanda tablet uses BM photos, which are **CC BY-NC-SA 4.0** (non-commercial). There are also 6 CC BY-SA candidates. **Fix:** use Vindolanda Trust or Commons PD/CC0 photos. If not, flag the card as non-commercial.
11. **x-meter** (Arma virumque, a scansion card) needs elision and final-*m* handling. The phonetics engine ignores both (see review-phonetics.md).
12. **l-bulla** (unit 2) teaches adjective agreement, but agreement is in unit 4. Move the agreement point to "preview".

## NITS
13. In x-parse-signum, the `translation` is the Latin expansion. Put the English, "Twentieth Legion, Valeria Victrix", there and move the expansion to `context`.
14. g-relative says "who art" while the medieval card says "who are". Pick one register.
15. g-acc says "(same meaning)". Add "different emphasis".

## Dialectic
- **Thesis:** constructed micro-sentences (52 of 65) plus a few authentic anchors give clean, controlled grammar input, and mix-cards (map, who-said-it, true/false, parse) add variety.
- **Antithesis:**
  - Isolated constructed sentences ("Rōma urbs est") are the textbook pattern CI advocates criticise. They are low in meaning and quickly forgotten.
  - The vocab cards are dictionary entries, not input.
  - Without glosses or vocab links, the "learning" cards are mostly flashcards with trivia contexts.
- **Synthesis:**
  1. Chain each unit's constructed sentences into a single 6–10-line micro-story using the unit's vocabulary (Ørberg-style). The story becomes the "Read & See" item and the cards become its drills.
  2. Each grammar card names one authentic anchor (from the rome or medieval cards) as the payoff.
  3. Require `vocab_ids` and `gloss` before a card can ship (a lint).
