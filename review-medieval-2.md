# Review 2: revised medieval-cards.json (v3, 28 cards) against review-medieval.md
_Reviewer agent, Oct 13 2026. Spot-checked 11 cards' glosses word by word. Image metadata for the two new images re-queried through the Commons API._

| # | Item from review-medieval.md | Result | Evidence / remaining issue |
|---|---|---|---|
| 1 | Glosses on all cards | **PASS** | All 28 have `gloss`. I spot-checked Héloïse, the sparrow, Magna Carta, Agnus Dei, Fiat lux, Alcuin, Dies irae, Dante, Abelard, Kempis and Tolle lege, and all parses are correct. Good catches: *Cārius* as a neuter comparative (its subject is the infinitive phrase); *domum* f.; *saeclum* syncopated; *in favīllā* abl. "= into"; *optimē* ← *bene*. |
| 2 | Same format as Rome (score 1–5, field names, vocab_ids) | **PASS** | teaching_value has {note, dcc_core_pct, non_core, score, rank} on every card, and no card has an empty `vocab_ids`. |
| 3 | Kempis "later papal formula" | **PASS** | Now reads "…chanted at papal coronations from the early 1400s." |
| 4 | Tolle lege conjugation and image | **PASS** | Both verbs are now glossed as 3rd conj. The image is File:TolleLege.jpg. Commons describes it as "Conversion of Augustine (Tolle Lege). St Augustine Reading the Epistle of St Paul", Benozzo Gozzoli, 1464–65, public domain. It is correctly labelled "Later depiction". |
| 5 | Agnus Dei *misereri* + dative | **PASS** | Register is ecclesiastical. The note and the gloss both say "classical uses gen. (miserēre meī)". |
| 6 | Héloïse "his" referent and spelling | **PASS** | Context names Augustus, the translation has [Augustus's], and *karius* → *cārius* is noted. |
| 7 | Magna Carta edit notes | **PASS** | The full omitted text is in the note, plus *terre*→*terrae* and the Anglo-Norman coinages, and *homō* now has its macron. |
| 8 | Bede sparrow cum-clause | **PASS** | Now *…cum … pervolāverit* "has flown". `grammar_preview` = cum_subjunctive and perfect_subjunctive. The note quotes the full clause. |
| 9 | Low-core cards | **PASS** | Einhard was dropped. Boethius, Abelard, Vanitas and the sparrow are marked `card_role: preview_reading`. |
| 10a | Abelard *quippe/enim* | **PARTIAL** | This is now flagged in the note but not resolved. It still needs a print check (Boyer & McKeon 1976–77) before release. |
| 10b | Dante Monarchia numbering | **PARTIAL** | The note admits it hasn't been checked. Look it up in Shaw (Cambridge 1995) or the Ricci edition. |
| 11a | Image crops | **PASS** | Five cards now have `focal_point` and `crop_note`. |
| 11b | CC BY-SA credit (Durupt) | **PASS** | Credit gives the painter, the photo source, the uploader and CC BY-SA 4.0. The license link and a "modified" note need to appear on the card back when it is rendered (see review-site.md #5). |
| 11c | Sutton Hoo image for the sparrow card | **PASS, with a should-fix** | Commons: "Cover illustration of the Ordnance Survey's 1966 … Map of Britain in the Dark Age", artist **Arthur Thomas Chester**, public domain (UK Crown copyright expires 50 years after publication). Thematically it's good: Rædwald of Sutton Hoo was Edwin's protector. **Fix:** credit "A. T. Chester / Ordnance Survey, 1966", and label it a *modern reconstruction drawing*, not a period artefact. Note that Crown-copyright PD status is a UK rule, so keep the Commons PD tag reference. |
| 11d | Bede image reuse | **PASS** | The St Petersburg Bede image is no longer used twice. |
| 11e | Post-medieval art labelled | **PASS** | Each one now has the "Later depiction:" prefix in its alt text. Add the prefix to the visible caption as well. |
| 12 | Dies irae / Aquinas / Bede Angli attributions | **PASS** | Person is now "attrib. Thomas of Celano". The Bede note explicitly says the popular phrase *non Angli sed angeli* is not in Bede. |
| 13 | U9 passive anchor (*facta est lūx*) | **PASS** | *facta est* is glossed as "perf. (passive form)". |
| 14–15 | Codex Buranus origin; Bede context | **PASS** | Both corrected. |
| — | **`register` calls** | **PARTIAL** | Ecclesiastical, medieval and medieval-legal are labelled correctly. Two labels are questionable:<br>• **Bede** (discere, angli, sparrow) is marked *classical*. Bede writes good Late/medieval Latin with medieval spelling and usage, so call it **medieval**.<br>• **Augustine** marked *classical* is defensible for style, but his Christian vocabulary (*confitērī*, etc.) argues for **ecclesiastical** or "late". The taxonomy mixes period with style.<br>**Fix:** split the field into `register` (classical / ecclesiastical / legal) and `period` (late_antique / medieval), or add a "late" register. |

## Summary
**15 PASS, 3 PARTIAL, 0 FAIL.**
- Before release: resolve the Abelard and Dante numbering checks, fix the Sutton Hoo credit, and refine the register labels.
- Remaining from earlier reviews: render the full CC BY-SA attribution on the card back (site review) and wire up audio.

## Dialectic, briefly
- **Thesis:** the revision follows the critique closely, and the content is now ready for the app.
- **Antithesis:** fixing what the critic listed only fixes what the critic happened to sample. Glosses written by hand across 28 cards (around 250 tokens) will contain errors that a spot-check of 11 cards can't rule out.
- **Synthesis:** run every gloss through LatinCy/Whitaker automatically and flag mismatches with the hand-written lemma or parse for human review. Add that check to the build next to the DCC script.
