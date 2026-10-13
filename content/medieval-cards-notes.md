# Medieval cards: notes (v2)
- There are 29 cards. All pass card-schema.json. They are sorted by teaching_value.score, then by dickinson_core_pct.
- Text: every Latin text has been checked against an online source. The source is listed in `text_check` and `source_url`: Latin Library, la.wikisource, Bibliotheca Augustana, or drbo.org for the Vulgate.
- Dropped because they have no verifiable source text: 'Ora et labora', 'Memento mori', 'Gaudeamus igitur' (which is also 1781, not medieval). 'Sic transit' was replaced by the verified Kempis line 'O quam cito transit gloria mundi' (Imitation of Christ 1.3.6).
- Added: Bede HE 5.24 'semper aut discere aut docere aut scribere dulce habui' and Alcuin's epitaph 'quod nunc es fueram … tuque futurus eris'.
- Not added (nothing found that both verified and scored well enough): Gregory the Great's own writings, Bernard, colophons.
- Dickinson %: the content-word lemmas were assigned by hand (`vocab_lemmas`). They are matched against data/dcc-latin-core.csv, the official DCC CSV (CC BY-SA), downloaded today. Recompute with medieval_dcc.py. Proper nouns are excluded. Citō counts as core because DCC lists it under citus.
- Images: every licence comes from Wikimedia Commons API metadata (PD, CC0 or CC BY-SA 4.0), and every file URL returns HTTP 200. None are cut-outs; all have transparent=false. Some aspects need cropping: Monte Cassino 16:9, Magna Carta 3:2, the Benedict and Alcuin manuscripts 1:1. The tolle-lege image is Gozzoli's 'Augustine departing for Milan' detail, not the conversion scene itself. The sparrow card reuses the St Petersburg Bede image.
- learn_more: English Wikipedia links. Every one returns 200, though some are redirects (e.g. 'Vanity of vanities').
- Build scripts: medieval_build.py (one-time v1→v2 transform, already applied), medieval_dcc.py, medieval_finish.py. content/build.py and cards.py belong to the Rome agent.

## v3 (review-medieval.md applied)
- 28 cards. Einhard dropped: it is a noun phrase and only 43% core.
- Every card has a `gloss` array (word, lemma, meaning, parse), written by hand in medieval_glosses.txt.
- Format now follows rome-cards.json: `teaching_value` {note, dcc_core_pct, non_core, score 1–5, rank}, and `vocab_ids` without macrons and spelled with v, taken from the gloss lemmas.
- New fields: `grammar_preview` (grammar seen but not yet taught), `register`, and `card_role: preview_reading` for Boethius, Abelard, Vanitas and the Bede sparrow.
- card-schema.json now has optional teaching_value, register, grammar_preview and learn_more properties. Both card files validate.
- Fixes applied: Kempis context, the Tolle lege conjugation note and image (now the Gozzoli reading scene), the Agnus Dei register tag and note, the Héloïse "his" (Augustus) referent and the cārius spelling, the Magna Carta edit notes, the full Bede sparrow cum-clause, the Bede context, the Codex Buranus origin, and the Dies irae attribution.
- Images: five crops now have a focal_point and crop_note. Cleveland .tif is served as a JPEG with ?width=1200. The Durupt image has full CC BY-SA credit plus a share-alike note. Post-medieval art is labelled "Later depiction". The sparrow card now uses the Sutton Hoo helmet (1966 OS illustration, PD), so the Bede manuscript image is no longer reused.
- Scripts: medieval_normalize.py (applies the review), medieval_dcc.py (recomputes core % and rank from the gloss lemmas).

## v4 (variety, readings, ecclesiastical phonetics, review-2)
- Now 35 cards. Seven are new: the Archpoet (Confessio st. 12), the Gesta Romanorum pirate story (ch. 146), the Paris statute of 1215 (CUP I no. 20), a scribe's colophon (BnF lat. 12234 via IRHT Bibale), Hildegard's 'O nobilissima viriditas' verse, and two graded readings with card_role graded_reading (John 1:1–5, Genesis 1:1–5).
- Readings are separate from the one-line anchor cards. Every new card is glossed, sourced, has a verified image and a learn_more link.
- phonetics_eccl.py writes content/phonetics-eccl.json with respelling_eccl (Italianate church rules; listed in the docstring) for all cards with register=ecclesiastical. Classical phonetics are unchanged.
- review-2 fixes:
  - Abelard: 'quippe' is the Boyer & McKeon critical reading; Migne has 'enim'.
  - Dante: 1.14.11 confirmed (Augustana chapter text).
  - Sutton Hoo drawing is now credited to A. T. Chester / OS 1966 as a modern reconstruction.
  - Bede and Alcuin are now register medieval; Augustine is ecclesiastical.
- Run order: medieval_variety.py → medieval_review2.py → medieval_dcc.py → phonetics.py --build → phonetics_eccl.py --build.

## v5 (review-medieval-3)
- John 1:5 now reads "did not comprehend it". In the Gesta card, galea is glossed "galley (medieval; classical = helmet)", and diceris is confirmed against the Latin Library. The colophon was checked word for word against Bibale 18684, so the singular nāvigantī and "sed tōtum corpus" stay, with a note that the formula varies. The Archpoet translation now uses the substantive morientis. The Paris image has a "Bologna, not Paris" caption.
- phonetics_eccl.py: cui/huic = KOO-ee/OO-eek. The build warns when a card has no macrons. The script now documents unvoiced intervocalic s and that vowel length is not marked. Run medieval_review3.py after medieval_review2.py.
