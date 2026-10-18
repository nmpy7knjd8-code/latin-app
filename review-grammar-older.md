# Grammar double-check of the older decks (base, rome, medieval, learning, batch4–6)

Date: Sun Oct 18, 2026 (ET). Reviewer: independent critic. Status: fixed locally. **Not published, not pushed.**

Scope: about 316 cards: base 5, rome 64, medieval 35, learning 65, batch4 50, batch5 49, batch6 48.
I checked each card on five points:
- the Latin against its source, including macrons;
- whether the translation is grammatically faithful;
- whether every grammar tag is present and correctly identified;
- whether the context, glosses and parses are correct;
- whether the unit order is right.

## Dialectic
- **Thesis:** these decks have already been through several reviews, so any errors left should be cosmetic.
- **Antithesis:** the earlier reviews focused on attribution and on unit order of targeted cards. The free-form tags on untargeted cards, the contexts that name a word, and the gloss parses had never been checked against the actual Latin. That kind of drift survives because it looks plausible. Examples:
  - a context names *excelsīs* or *auscultā* when the card's Latin has a different word;
  - vocatives in apposition are parsed as nominatives;
  - a note is copied over from another card.
- **Synthesis:** the antithesis held. I found 18 real errors. None of them break rendering. Several would teach wrong grammar or point to the wrong source. All 18 are fixed in the source files, with no stale generator run.

## Errors per deck
| Deck | Cards | Errors |
|---|---|---|
| base (cards/cards.js + card-schema.json examples) | 5 | 1 |
| rome-cards.json | 64 | 4 |
| medieval-cards.json | 35 | 3 |
| learning-cards.json | 65 | 7 |
| batch4 | 50 | 1 |
| batch5 | 49 | 0 |
| batch6 | 48 | 2 |
| **Total** | **316** | **18** |

## Fixes
| Card | Problem | Fix | Where |
|---|---|---|---|
| q-caesar-gallia | `preview` in grammar_tags is a role marker, not a grammar feature | Removed the tag | cards.js and the card-schema.json example |
| q-virgil-arma | The Ītaliam gloss was split on ';' into two malformed entries: the parse ended up as a "word" and the lemma as "acc. of motion" | Merged into one entry: lemma *Italia*, parse "acc. of motion (Ī lengthened for metre; normally Ĭtalia)" | rome |
| q-cicero-quousque | *ūsque* with a false long ū | Changed to *usque* in the Latin and the gloss | rome |
| q-ovid-expedit | *ut* + indicative (*expedit*) was rendered "since" | Changed to "as it is useful" | rome |
| q-cicero-cedant | The context had *Cedant* without its macron | Changed to *Cēdant* | rome |
| q-vulg-gloria | The context explains *in excelsīs*, but the card's Vulgate Latin has *in altissimīs* | The context now explains *altissimīs* and notes that the Mass has *excelsīs* | medieval |
| q-aug-da-mihi | The context explains *nōndum*, which is not in the Latin | The context now explains that *nōlī modo* means "not yet" | medieval |
| q-ben-ausculta | The context says *Auscultā*, but the Latin has *Obscultā* | The context now names *Obscultā* as the manuscript spelling of *auscultā* | medieval |
| l-bulla | grammar_preview held the malformed key "adjective_agreement (taught Unit 4)" | Changed to `adjective_agreement` | learning |
| x-whosays-cornelia | *ornāmenta* | Changed to *ōrnāmenta* / *ōrnāmentum* in the Latin and the gloss | learning |
| x-greek-flag | *Marcus* | Changed to *Mārcus* in the Latin and the gloss | learning |
| i-karolus | Typo "emperor., deliberately" | Changed to "emperor, deliberately" | learning |
| x-colophon | Tagged `relative_clause`, but there is no relative clause | Removed the tag | learning |
| l-monasterium | *monasterium* in the Latin, *monastērium* in the gloss lemma | Changed the Latin and the gloss word to *monastērium* | learning |
| i-pantheon-parse | The context had *Lūciī*, but the card glosses *Lūcī* | Changed to *Lūcī fīlius* | learning |
| q-vespasian-deus | The attribution_note was copied from the Gregory of Tours card | Replaced with the Suet. Vesp. 23.4 text ("vae, inquit, puto deus fio"; the card omits *inquit*) | batch4_cards.py → rebuilt |
| q-virgil-nate | *meae vīrēs, mea magna potentia, sōlus* were parsed as nom., but they are vocatives in apposition to *nāte*, on a card whose target is vocative | Parses changed to voc.; *sōlus* is marked "nom. sg. m. (used for voc.)" | batch6_cards.py → rebuilt |
| q-hannibal-ad-portas | The note and context claimed Phil. 1.11 reads "Hannibal ante portas". It actually reads "Hannibal, credo, erat ad portas" | Corrected both; "ante portās" is noted as a later variant | batch6_cards.py → rebuilt |

## How the fixes were applied
- **rome, medieval and learning JSON:** the new `content/grammar_older_fixes.py` patches them in place. It is idempotent: a second run makes 0 changes. Every replacement asserts that the expected old text is present. `rome_build.py` was **not** run.
- **batch4 and batch6:** edited `batch4_cards.py` and `batch6_cards.py`, then rebuilt them with their own build scripts. Both print "lint OK". The git diff of the built JSON shows only the intended lines.
- **Base deck:** cards.js has no generator, so I edited cards.js and the card-schema.json examples identically.

## Checked and correct
Every other card was checked on the same five points and is correct. Specific confirmations:
- **Batch5:** RG 4.1 without *et* and Lucretius *dē nihilō* both match the Latin Library.
- **Macron conflicts across decks:** apart from the fixes above, the remaining ones are legitimate case or quantity variants, or inscription spellings.

## Cards without grammar_target
The base deck, 27 of the 35 medieval cards and all 65 learning cards have no `grammar_target`, by design. They use free-form `grammar_tags`. I checked those tags against the Latin; only x-colophon was wrong.

The lint reports unknown preview keys on 9 medieval cards, for example `cum_subjunctive` and `ablative_of_means`. These are informational: the keys are not in the TAUGHT list. The keys themselves are grammatically accurate, so I left them as they are.

## Validation
- **Schema:** 0 errors in all 8 content decks and in the card-schema.json examples.
- **Unit-order lint:** 0 issues for the targeted decks (rome, batch4, batch5, batch6) and for the 8 targeted medieval cards.
- **Overflow check** at 390×844, 430×932, 375×667 and 390×664: 403 cards, no overflow, no clamped text, the picker fits, no console errors.
- **Re-verification:** all 18 fixes were confirmed in the built JSON or JS after rebuilding.
