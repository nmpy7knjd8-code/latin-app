# CHANGES — Oct 13 2026 (fixes from review-1.md and review-cards.md)

## Dialectical syntheses adopted
- **Quote unlock:** a quote unlocks at ≥70% of its vocab known, with full glosses for the rest. It becomes a plain review card at ≥90%. Schema: `unlock_rule.min_vocab_known` 0.7 and `review_threshold` 0.9, both limited to 0–1. (Hu & Nation 2000)
- **FSRS:** schedules lemmas and grammar skills rather than every word form. Reading counts as an implicit review. Retention is 0.85–0.9 and the user can change it.
- **Teaching method:** input comes first, then a short explicit *Nota bene* and processing-instruction drills. Krashen is now cited as the 1982 book, and the debate around his theory is noted.
- **Vocab pacing:** about 80% follows the DCC frequency list and about 20% is a themed unit lexicon. Later units use the Diederich and medieval lists, and glosses cover the 95–98% coverage gap.
- **Gamification:** XP rewards retention and reading minutes. Leagues are off by default.
- **AI tutor:** only uses forms checked by LatinCy/Whitaker and shows the analyzer output.
- **Images:** cut-outs only for 3D objects that pass matte QA. 2D works get masks instead. Every card has a "see in museum" link.
- **Card modes:** **Learn** shows the translation on the front with tappable glosses. **Review** shows Latin only and the card flips (index.html has a toggle).

## Content fixes (research.md, game-design.md, card-schema.json, cards.js)
- **Caesar:** the context now says the words were a placard in his Pontic triumph of 46 BC, after Zela in 47 BC (Suet. Iul. 37.2). The note quotes Suetonius and says Plutarch (Caes. 50) has a letter to Amantius, written in Greek.
- **Cicero:** the speech is now set in the Temple of Jupiter Stator, 8 Nov 63 BC (Cic. Cat. 1.1; Plut. Cic. 16). The Curia Julia image is replaced by the Capitoline bust.
- **Augustine:** shown as a framed painting (`transparent:false`, arch frame), licence PD-art. The schema now rejects transparent paintings, manuscripts and inscriptions. Added the note *quasi pueri an puellae*.
- **Macrons** added throughout: Vēnī, vīdī, vīcī · dīvīsa in partēs trēs · Ō tempora, ō mōrēs · crēdula posterō. Every card has word-by-word glosses, with *posterō* glossed as (diēī).
- **Grammar and unit order:**
  - The perfect tense moved to Unit 6, so *Vēnī, vīdī, vīcī* (unit 6) is its first sighting.
  - The future moved to Unit 7, and the imperative was added there (*carpe diem*).
  - BG 1.1 is now a glossed preview in Unit 3.
  - Augustine (Unit 9) is tagged `imperative`.
  - Added Val. Max. 4.4 pr. for the Cornelia story.
  - The mastery level Magister is renamed Perfectus.
- **Corrected figures:**
  - Adesope et al. 2017: 118 articles / 272 effects, doi:10.3102/0034654316689306.
  - The Met has ~470k images.
  - The DCC core list gives 65–70% coverage.
  - ts-fsrs ships FSRS-6; FSRS-7 leads the benchmark.
- **Links:** removed trailing punctuation that broke URLs. The dead Hackett link now goes to the Hackett homepage. Unverified links are flagged (Krashen site, Attalus, sites that blocked automated checks).
- **Licences:**
  - The Met, AIC and Rijks are "check the per-record PD flag."
  - Getty is listed as "free, not formally CC0."
  - British Museum is flagged CC BY-NC-SA (non-commercial only) and dropped from the design's source list.
- **Horace:** the alt text now gives the Laurenziana shelfmark Plut. 34.1 and the 10th-century date, and drops "papyrus." The coin example shows Aeneas and Anchises (as on Met 248033), not the Gallic trophy.

## Schema
- **Required fields:**
  - Images: `license` (from a fixed list), `credit`, `source_url` and `transparent`.
  - Quote cards: `source`, `person`, `attribution_confidence` and `image`.
  - `image` is no longer required for vocab and grammar cards.
- **Limits:** `context` is capped at 260 characters (about 40 words). `focal_point` must be between 0 and 1.
- **New fields:** `late_medieval` era, `$defs/vocab` (with `anchors` and `dcc_rank`), `caption_la` and `museum_url`.
- All 5 examples pass jsonschema validation, and a transparent painting correctly fails. cards.js is now generated from the schema examples.

## UI (cards/index.html)
- **Era label:** moved out of the image area into the text band next to the name. Cut-outs are limited to the centre of the top edge (the safe zone).
- **Screen readers:** a card in review mode is `role=button` with `aria-pressed`. The hidden face gets `aria-hidden` and `inert`, and the aria-label reads "Quote card: …, …. Press to reveal translation."
- **Text size and contrast:** text is now ≥.72rem at full opacity. The full credit is on the back, along with a ≥44px "See in museum" link. The nested link on the front and the stopPropagation workaround are gone.
- **Reduced motion:** `prefers-reduced-motion` now crossfades instead of flipping.
- **Era themes:** all 7 eras have a theme, plus a default. Pale text sits on dark backgrounds. The colours were chosen to be dark, but contrast hasn't been measured with a tool.
- **Rendering:** uses `focal_point` and shows `attribution_note` on the back. In Learn mode, each word is a tappable gloss button.
- **Other:** removed the coin border-radius. Added pagination dots. The footer licence line is generated from the data.

## Screenshots
preview.png (all fronts, including Augustine), preview-back.png (Caesar back), preview-learn.png, preview-mobile.png, preview-mobile-augustine.png. The script is shot.py.

## Still open
- The Caesar cut-out still fades softly at the neck instead of having a clean edge or plinth. The image needs a new matte (review-cards #10), and all mattes still need a halo check.
- Check the [K]/403 links in a real browser.
- Measure WCAG contrast with a tool.
- No vocab data file exists yet.
