# Review 1: research.md, game-design.md, card-schema.json
_Reviewer agent, Oct 13 2026. URLs checked with curl from the box. Quotes checked against standard texts (Perseus / Latin Library editions)._

## ERRORS
1. **Cicero card image is anachronistic.** *In Catilinam I* (8 Nov 63 BC) was given in the **Temple of Jupiter Stator**, not the Curia. The Curia Julia was begun by Caesar in 44 BC and finished under Augustus. **Fix:** use a Temple of Jupiter Stator/Forum reconstruction, or a Cicero bust, or Maccari's fresco *Cicero Denounces Catiline* (1889, PD). Then rewrite the context line to say "in the Temple of Jupiter Stator." Source: Cic. Cat. 1.1 (*hic munitissimus habendi senatus locus*); Plut. Cic. 16.
2. **"Veni, vidi, vici" context is wrong.** Suetonius (Iul. 37.2) says the words were a **placard carried in his Pontic triumph (46 BC)**: *"in Pontico triumpho inter pompae fercula trium verborum praetulit titulum VENI·VIDI·VICI"*. The idea that Caesar sent them as a written report comes from Plutarch (Caes. 50, a letter to Amantius), and Plutarch writes in **Greek**. **Fix:** the context should say that after Zela (47 BC) Caesar displayed the words at his triumph (Suet. Iul. 37.2), and that Plutarch says he wrote them to a friend. The attribution_note should say Plutarch's version is Greek.
3. **Botticelli painting is set as a cut-out (`transparent:true`).** This contradicts research §3, which says paintings and frescoes get arched or torn masks, not background removal. Cutting a figure out of a fresco also looks bad. **Fix:** set `transparent:false` and add an arched mask. Botticelli's *St Augustine* (Ognissanti, 1480) is PD-art, so source it from Commons and state the licence.
4. **Macrons are missing on every example**, even though research says "macrons always shown." Correct forms: *Vēnī, vīdī, vīcī*; *Gallia est omnis dīvīsa in partēs trēs*; *Ō tempora, ō mōrēs!*; *Carpe diem, quam minimum crēdula posterō*; *Tolle, lege; tolle, lege* (no long vowels). **Fix:** add a `latin_macronized` field, or put the macrons into `latin` and strip them for display if the user wants. Source: Lewis & Short / Wiktionary headwords.
5. **Grammar sequencing conflicts.** The BG 1.1 anchor is in Unit 3, but it needs the 3rd declension (*partēs trēs*, Unit 5) and the perfect passive participle (*dīvīsa*, not in the plan). The Augustine card is in Unit 9 ("passive voice") but its text is imperatives with no passive. Caesar's *veni vidi vici* is placed in Unit 7 "Poets." **Fix:** label BG 1.1 as a "preview/exposure" quote with full glosses, or move it to Unit 5. Add an `imperative` tag and fix the Augustine unit or the grammar. Add a Caesar card to Unit 7 only as the perfect-tense "first sighting," or move the perfect earlier to Unit 6. These are the units' own grammar strands (game-design §3).
6. **Adesope et al. 2017 figure.** The Learning Scientists post title does say "217 studies," but the paper (Rev. Educ. Res. 87(3)) reports 118 articles and 272 effect sizes. **Fix:** cite the paper (doi:10.3102/0034654316689306) with "118 articles / 272 effects."

## SHOULD-FIX
7. **Several URLs carry trailing punctuation.** `latin-core-list1.`, `ts-fsrs.`, `rembg,`, `legentibus-a-review.html.` and `springer…09498-w.` all return 404 as written and 200 once the punctuation is removed. Hackett's `/lingua-latina-series` returns **404**. **Fix:** remove the punctuation and use https://www.hackettpublishing.com/ or Focus/Hackett's LLPSI product page.
8. **Unverified [K] links.** http://www.sdkrashen.com and http://www.attalus.org did not connect from the box (timeout). AIC, Smithsonian FAQ, MDPI and Europeana return 403 to curl (bot-blocking, probably fine). metmuseum.org returned 429 (rate limit). **Fix:** check these in a browser before relying on them. For Krashen, cite *Principles and Practice in SLA* (1982) instead.
9. **Met image count.** "492k+" doesn't match metmuseum.github.io, which currently says ~470,000. **Fix:** write "~470k" or "400k+".
10. **DCC coverage.** The DCC page says the 1,000-word list corresponds to the **65–70%** level. **Fix:** write "65–70%". The 1,000 lemmas and CC BY-SA licence were confirmed.
11. **FSRS line.** Confirmed: 10k Anki users, 727M reviews, FSRS-7 in the benchmark. But **ts-fsrs implements FSRS-6**, not 7. "FSRS-6 is the Rust baseline" is unclear. **Fix:** "Benchmark leader is FSRS-7; ts-fsrs (the planned library) ships FSRS-6, which is fine."
12. **Schema: licensing isn't enforced.** `image.license`/`credit`/`source_url` are optional, and the Caesar example has `"license":"check Wikimedia Commons"`. **Fix:** require `license`, `credit` and `source_url`. Add an enum of allowed licences (CC0, PDM, PD-art, CC BY 4.0, CC BY-SA 4.0). Fill these in on every example.
13. **Schema: quote cards can omit `source`/`attribution_confidence`.** **Fix:** add `if type=quote then required [source, person, attribution_confidence]`. Also, `image` is required on vocab/grammar cards that may not have one.
14. **Schema vs design mismatches:**
    - `context` maxLength is 280 chars, but the design says 40 words.
    - The design describes vocab `anchors`, but there is no vocab schema.
    - `unlock_rule.min_vocab_known` has no range, so 0.7 vs 70 is ambiguous. Add min 0 / max 1.
    - The era enum has no `late_medieval`, but Dante, Petrarch and the Scholastics are on the roadmap.
    - The research mentions Getty, AIC and Rijks, while the design lists Commons, the British Museum and others.
    - **The British Museum is not CC0.** It uses CC BY-NC-SA 4.0, which is non-commercial, so flag it or drop it.
15. **Image licences.**
    - **Getty:** Open Content images are free for any use with no restriction (not formally labelled CC0).
    - **AIC:** only public-domain works are CC0. Check `is_public_domain`.
    - **Rijks:** CC0 for PD works. Correct as stated.
    - **Met:** CC0 when `isPublicDomain`. Correct, and met.py already filters on this.
    - **Fix:** say "check the per-record PD flag" for every museum.
16. **Plutarch's "Caesar 50"** is correct. Valerius Maximus's Cornelia story is at **4.4 pr.** (*haec … ornamenta sua*). Add that citation.

## NITS
17. "Magister" is used both as a rank and as a mastery level. Rename the mastery level (e.g. *Perfectus*).
18. Horace card: the id/filename says "papyrus" but the alt text says manuscript leaf. No Horace papyrus survives in usable form, so use a medieval MS or an early printed edition.
19. *postero* = *posterō (diēī)*. Add a gloss.
20. Augustine: the voice is *"quasi pueri an puellae,"* a boy's or a girl's, from a neighbouring house. The current "a child chanting" is OK. "Milan garden" is correct.
21. Odes 1–3 date to 23 BC. The "empire" era is OK (after 27 BC).

## Dialectical review of major decisions
| Decision | Thesis (current) | Antithesis (best counter-evidence) | Synthesis |
|---|---|---|---|
| FSRS scheduling | ts-fsrs, retention 0.9 | The benchmark measures flashcard **recall prediction**, not reading ability. Item-level SRS splits language into fragments, and Latin morphology means one lemma has many forms, so per-card scheduling over-counts. | Schedule **lemmas and grammar skills** (not every surface form) with FSRS. Let reading exposures count as implicit reviews. Use 0.85–0.9 retention and let users lower it. |
| Reading-first CI | Ørberg-style passage first | Krashen's strong input hypothesis is contested (Swain's output hypothesis; VanPatten's processing instruction). Adult classical learners often do better with explicit grammar (Norris & Ortega 2000 meta-analysis: explicit > implicit). | Keep input first, but add a 30-second explicit "Nota bene" after the passage, plus processing-instruction drills (e.g. case-marking decides who did what to whom). |
| Frequency pacing (DCC) | Introduce words by DCC rank | Frequency lists ignore thematic coherence, so a Legion unit needs *gladius*, *castra*, etc. Medieval texts also have a different frequency profile. The 1k list only gives 65–70% coverage, while about 95–98% is needed for comfortable reading (Nation 2006; Hu & Nation 2000). | Mostly frequency (~80%) plus a themed "unit lexicon" (~20%). Switch to the Diederich/medieval list for later units. Glossed reading fills the coverage gap. |
| Gamification | Streaks, XP, cards, ranks | Effects are small and vary widely (Sailer & Homner 2020). Duolingo-style streaks push people to grind easy items (overjustification). | Award XP for **retention** (stability gains) and reading minutes. Make collectibles content-meaningful. Keep leagues off by default. Use streak freezes. |
| AI tutor | Explanations and chat, never the source of truth | Even explanations can contain made-up macrons or grammar. Chat without structure doesn't sit inside the SRS loop. | The tutor answers only with forms checked by LatinCy/Whitaker. It shows the analyzer output alongside its text. Conversation prompts reuse vocabulary that's due. |
| Quote unlock at 70% vocab | Cloze when ≥70% known | At 70% coverage a text is incomprehensible (Hu & Nation 2000 put the threshold at 95–98%). | Unlock at ≥70% known **plus** full glosses for the rest, then a "pure" review once ≥90% is known. Treat early quotes as preview exposures. |
| Image approach | CC0 museum photos + rembg cutouts | Cutouts strip archaeological context. rembg fails on low-contrast marble and coins (halos). Licences vary per record. Inconsistent cutout quality makes the app look cheap. | Use cutouts only for sculpture, coins and objects that pass a manual QA check. Use masks for 2D works. Make licence fields mandatory. Add a "see in museum" link to restore the context. |
