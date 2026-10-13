# Latin + Rome/Medieval West Learning App — Research Report
_Prepared Oct 13, 2026; revised the same day per review-1.md (see CHANGES.md). Sources marked [V] were checked during this research session; [K] are well-known canonical URLs. Check the [K] ones again before relying on them. AIC, Smithsonian, MDPI and Europeana return 403 to curl and metmuseum.org returned 429, so check those in a browser._

## 1. Language-learning science: what holds up

| Technique | Evidence | Design implication |
|---|---|---|
| **Spaced repetition (FSRS)** | Open Spaced Repetition's SRS Benchmark (~10k Anki users, ~727M reviews) puts FSRS far ahead of SM-2 at predicting recall. The benchmark leader is FSRS-7, which handles fractional (same-day) intervals. [V] https://github.com/open-spaced-repetition/srs-benchmark · algorithm: https://github.com/open-spaced-repetition/awesome-fsrs/wiki/The-Algorithm | Use **ts-fsrs** (TypeScript, open-spaced-repetition org) [V] https://github.com/open-spaced-repetition/ts-fsrs. It ships **FSRS-6**, not FSRS-7, which is fine for this app. Start on default parameters and optimize per user once they have enough reviews. **Synthesis (review-1):** schedule **lemmas and grammar skills**, not every surface form, and count reading exposures as implicit reviews. Target retention 0.85–0.9, adjustable by the user. |
| **Spacing for L2 vocabulary** | Kim & Webb (2022) meta-analysis: spaced beats massed practice, g=0.76 immediately and g=1.15 at a delay. [V] (cited in https://exa.ai/library/publication/6fq62h6c4p5) | Keep daily sessions short and spread reviews out. Don't let users cram. |
| **Retrieval practice** | Adesope, Trevisan & Sundararajan 2017, *Rev. Educ. Res.* 87(3), meta-analysis of **118 articles / 272 effect sizes**: testing beats restudy, the benefit is larger at delays over 1 day, and mixing MC with cued recall works best. [V] doi:10.3102/0034654316689306 (summary: https://www.learningscientists.org/blog/2017/2/9-1, whose title says "217 studies"; the paper's own figures are used here) | Mix question types (MC → typed recall → produce a form). Make the prompt look like the real task, which is reading actual Latin. |
| **Interleaving** | Brunmair & Richter 2019 (59 studies): g=0.42 overall, but **blocking beats interleaving for word lists (g=−0.39)**. Interleaving works best for similar-looking categories. [V] https://www.psychologie.uni-wuerzburg.de/fileadmin/06020400/2019/Brunmair_Richter_in_press__2019_META-ANALYSIS_OF_INTERLEAVED_LEARNING.pdf | Teach new vocabulary in blocks. **Interleave confusable grammar** (declensions, cases, tenses, -ō vs -iō verbs) during review. |
| **Comprehensible input** | Krashen's input hypothesis: Krashen, *Principles and Practice in Second Language Acquisition* (1982). The strong form is contested (Swain's output hypothesis; VanPatten's processing instruction; Norris & Ortega 2000 found explicit instruction > implicit). Ørberg's *Lingua Latina per se Illustrata* (Familia Romana) is the canonical Latin CI text, published by Focus/Hackett [K] https://www.hackettpublishing.com/ | Center the app on graded reading (with images and glosses) built on the core vocab, with drills supporting it. A known weakness of Familia Romana is uneven vocabulary pacing: chapters introduce about 35 new words, sometimes 88. [V] https://aemiliana.com/2026/03/30/legentibus-a-review.html Pace by frequency rank instead. **Synthesis (review-1):** input first, then a 30-second explicit *Nota bene* and processing-instruction drills (e.g. the case ending decides who did what to whom). |
| **Gamification** | Sailer & Homner 2020: small positive effects (cognitive g=.49, motivational g=.36, behavioral g=.25), with high heterogeneity. [V] https://link.springer.com/article/10.1007/s10648-019-09498-w A Korean EFL meta-analysis found g=.52, with points and badges significant. [V] https://www.mdpi.com/2071-1050/15/14/11325 | Use light gamification (streaks, XP, collectible "figure cards"). **Synthesis (review-1):** award XP for retention (stability gains) and reading minutes, not volume; make collectibles content-meaningful; leagues off by default; streak freezes. |
| **LLM tutors** | Promising for open-ended explanation, sentence-level feedback, and Socratic conversation. Main risk: hallucinated forms or macrons and invented quotes. | Use the LLM to explain and chat only. **Never use it as the source of truth for morphology or quotes**: check answers against a morphological analyzer and a curated quote database. **Synthesis (review-1):** the tutor only answers with forms checked by LatinCy/Whitaker, shows the analyzer output beside its text, and builds conversation prompts from vocabulary that is due. |
| **Speech / pronunciation** | Restored classical pronunciation is the norm in the living Latin movement. Duolingo's Latin audio is criticized. [V] https://classicalstudies.org/scs-blog/ashley-francese/review-duolingo-latin-course | Offer listening with synced audio (recorded or high-quality TTS), macrons always shown, and an optional classical/ecclesiastical toggle. Speech recognition is optional and low priority. |

## 2. Latin-specific landscape

**Living Latin / active methods:** LLPSI (Ørberg), Legentibus (graded readers with synced audio, tap-to-define, and an immersion course built on Familia Romana) [V] https://legentibus.com/. Other active-Latin groups worth knowing include SALVI and the Paideia Institute [K].

**Frequency vocabulary:** the **DCC Latin Core Vocabulary** has 1,000 lemmas, corresponding to the **65–70%** coverage level in typical texts. Rankings come from LASLA. It includes semantic groups and parts of speech, with **CC BY-SA 3.0** licensing, so it can be reused with attribution and share-alike. [V] https://dcc.dickinson.edu/vocab/core-vocabulary · list: https://dcc.dickinson.edu/latin-core-list1 Diederich's 1,500-word list (~85% coverage, includes medieval texts) is mentioned on the same page, which makes it a good extension for the medieval layer. **Synthesis (review-1):** comfortable reading needs ~95–98% coverage (Hu & Nation 2000; Nation 2006), so the 1k list is not enough on its own. Pace ~80% by frequency plus a ~20% themed unit lexicon (*gladius*, *castra* for the Legion), switch to Diederich/medieval lists for later units, and close the gap with full glosses.

**Morphology / NLP tools (for grading answers and generating paradigms):**
- Whitaker's Words, packaged as latincy-lexicon (paradigm generation): [V] https://github.com/latincy/latincy-lexicon
- LatinCy (spaCy lemmatizer, POS tagging): [V] https://latincy.github.io/latincy-book/lemmatization.html
- CLTK backoff lemmatizer: [V] https://v1.cltk.org/en/latest/_modules/cltk/lemmatize/lat.html
- Collatinus (GPL-3): [V] https://github.com/biblissima/collatinus
- LEMLAT 3 is CC BY-NC-SA, so it can't be used commercially [V via search summary].

**Corpora:**
- Perseus Digital Library / canonical-latinLit (CC BY-SA TEI XML) [K] https://github.com/PerseusDL/canonical-latinLit
- The Latin Library (texts on the site are public domain, but the site has no formal license) [K] https://www.thelatinlibrary.com/
- Corpus Corporum (large medieval corpus) [K] https://www.mlat.uzh.ch/
- PHI Latin Texts (classical up to 200 AD; **not openly licensed**, so use for reference only) [K] https://latin.packhum.org/
- Open Greek and Latin [K] https://opengreekandlatin.org/

**Existing apps and their gaps:**
- **Duolingo Latin** is short, mostly present tense, has no stories and thin grammar, and is weak on real texts. [V] SCS review above; https://kossecki.github.io/review/
- **Legentibus** is excellent for input, but hard for true beginners (needs 3–7 rereads), light on grammar, and paces vocabulary poorly. [V]
- **The gap Garrett can fill:** frequency-paced CI reading + FSRS + real authors' quotes + history/culture cards (Rome → medieval West). Nobody combines all of these.

## 3. Quotes, figures, and images

**Quotes and people:**
- Wikiquote (CC BY-SA, has Latin proverbs and per-author pages) [K] https://en.wikiquote.org/wiki/Latin_proverbs
- Wikidata (structured people, dates, and places, CC0, via a SPARQL endpoint) [K] https://query.wikidata.org/
- Attalus (sourced Roman history references) [K, unverified: timed out from the box; check in a browser] http://www.attalus.org/
- Every quote should link back to a Perseus or Latin Library passage, so users can "read the original" and so quotes can be verified.

**Images (license):**
- **The Met Open Access:** ~470,000 public-domain images (per metmuseum.github.io), CC0 when the record's `isPublicDomain` flag is true, with an API (`isPublicDomain=true`) and a bulk CSV. [V] https://metmuseum.org/openaccess · https://metmuseum.github.io/
- **Rijksmuseum:** CC0 for public-domain works, sometimes CC BY 4.0. The search API needs no key; check the per-record licence. [V] https://data.rijksmuseum.nl/tutorials/search/ · https://data.rijksmuseum.nl/policy/information-and-data-policy
- **Smithsonian Open Access:** CC0 2D **and 3D models** (glTF/OBJ), and 3D statues can be rendered with transparent backgrounds. [V] https://www.si.edu/openaccess/faq
- **Art Institute of Chicago:** only public-domain works are CC0 (check `is_public_domain` per record); images served through IIIF. [V] https://www.artic.edu/collection-information/open-access/open-access-images · https://aggregator-data.artic.edu/docs/
- **Getty Open Content:** free for any use without restriction (not formally labelled CC0); check each record is in the Open Content set. [K] https://www.getty.edu/projects/open-content-program/
- **British Museum:** CC BY-NC-SA 4.0, i.e. **non-commercial only**. Avoid unless the app stays non-commercial. [per review-1]
- **Wikimedia Commons:** licenses vary, so check CC BY-SA attribution per file. Commons has many sculpture photos and some user-made transparent PNGs, but no reliable dedicated "cutout" set. [K] https://commons.wikimedia.org/
- **Manuscript illuminations (medieval layer):** e-codices, British Library, BnF Gallica, and Europeana aggregate many PD/CC0 items. [K] https://www.europeana.eu/

**Cutouts:** none of the major museum APIs provides transparent PNGs. The recommended pipeline:
1. Pull CC0 JPEGs (Met, Rijks, AIC, Smithsonian).
2. Remove the background with **rembg** (open source, U²-Net/BiRefNet models) [V] https://github.com/danielgatis/rembg or render Smithsonian 3D models directly.
3. Save as WebP/PNG with alpha.
4. Add a soft drop shadow over the card background.

**Synthesis (review-1):** use cut-outs **only for 3D objects** (sculpture, coins, helmets, vessels) that pass a manual matte QA check (rembg can leave halos on low-contrast marble and coins). Every card links "see in museum" to restore context. For paintings, mosaics, and manuscript pages, use non-square "torn/arched" masks instead. Under CC0, modified derivatives are fine. Under CC BY-SA, derivatives must keep the attribution and license.

## 4. Top recommendations
1. **Core loop:** short graded Latin reading (CI, images, tap glosses) → retrieval quizzes → FSRS review. Vocabulary is paced by DCC Core rank.
2. **Scheduling:** ts-fsrs with mixed question types. Block new words, interleave confusable grammar.
3. **Content spine:** a timeline from Rome (Republic → Empire) into the medieval West, where each unit has a historical figure, an authentic quote (simplified at first, then original), and a culture card.
4. **AI:** an LLM tutor for explanations and conversation, with Whitaker's/LatinCy as the ground truth for forms and a curated, sourced quote database. No AI-generated quotes.
5. **Visuals:** CC0/PD museum images; rembg cut-outs for QA-passed 3D objects only; arched/torn masks for 2D works; Smithsonian 3D renders. Licence, credit and source URL are **required** on every card.
6. **Gamification:** light and tied to retention, e.g. collect "Personae" figure cards by mastering their quotes.
