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
