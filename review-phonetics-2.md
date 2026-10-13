# Review 2: phonetics.py against review-phonetics.md
_Reviewer agent, Oct 13 2026. The built-in test now passes **70/70** (IPA, respellings and verse)._

| # | Item | Result | Output now |
|---|---|---|---|
| 1 | exspectō /ks/ | **PASS** | /ɛk.ˈspɛk.toː/ ek-SPEK-toh. *exsilium* → /ɛk.ˈsɪ.lɪ.ʊm/ ✔ |
| 2 | Gnaeus initial gn | **PASS** | /ˈgnae̯.ʊs/. Intervocalic *magnus* and *ignōscō* still give [ŋn] ✔ |
| 3 | suāvis | **PASS** | /ˈswaː.wɪs/ SWAH-wis. *suādēre* → swah-DAY-re ✔. *suus* stays /ˈsʊ.ʊs/ ✔ (correct: it isn't consonantal there) |
| 4 | euge diphthong | **PASS (IPA)** | /ˈeu̯.gɛ/. **Nit:** the respelling "EH-OO-ge" reads as two syllables. Use "EW-ge" or "EH⁀oo-ge". |
| 5 | Hidden quantity before jj | **PASS** | māior /ˈmaj.jɔr/, Pompēius /pɔm.ˈpɛj.jʊs/, Trōiae /ˈtrɔj.jae̯/, all matching Wiktionary. |
| 6 | huic/cui | **PASS** | hoo-eek, koo-ee. **The ecclesiastical engine still says "wee"** (review-medieval-3 #2). |
| 7 | Long-vowel respelling and legend | **PASS** | Short vowels are a e i o u ("u as in put"); long vowels are ah ay ee oh oo; CAPS marks stress. The legend ships in phonetics.json and phonetics.js. **Nit:** the legend entry "ngn = gn" is backwards in wording; say "gn sounds like ngn". "ay" for ē is diphthongal in English, so add "(pure, no glide)". |
| 8 | Verse mode: elision and final -m | **PASS** | `transcribe(..., verse=True)` correctly gives:<br>• *mult‿ill‿et* (Aen. 1.3)<br>• *ōd‿et*, *quār‿id*<br>• nasalised *faciã*<br>• prodelision *decōrum'st*<br>• a lacuna (…) blocks elision<br>Rhythmic medieval verse (Burana, Dies irae, Hildegard, Confessio) is correctly excluded. 22 entries have `ipa_verse`. |
| 8b | `--verse` command-line flag | **FAIL (minor)** | `python3 phonetics.py --verse "…"` raises `TypeError: 'NoneType' object is not subscriptable` at line 290. The flag isn't parsed, so "--verse" is transcribed as a word. **Fix:** parse the flag before calling `transcribe`. |
| 9 | rhētor aspiration | **PASS** | /ˈr̥eː.tɔr/. The legend now explains that ph/th/ch are breathy p/t/k, not f/th. |
| 10–12 | Z policy, dental marks, respelling clarity | **PARTIAL** | KUY/PAYY are fixed (pom-PAY-yus). The Z policy still isn't written into the legend. |
| 13 | Ecclesiastical engine | **PASS** | phonetics_eccl.py exists (review-medieval-3). |
| new | **Missing macrons in the input give wrong stress** | **ERROR** | *regina* → RE-gi-na (should be rē-GĪ-na). This applies to both engines. **Fix:** have the build warn on any card Latin with no macrons, and look words up in a macronized lexicon as a fallback. |

**Overall: 11 PASS, 1 PARTIAL, 1 minor FAIL (CLI), 1 new error (macron-dependence).**

## Dialectic
- **Thesis:** the engine is now accurate enough to be the source of truth for both display and TTS.
- **Antithesis:** its output can only be as good as the macrons it's given. The macrons are hand-applied and partly adopted from Alatius, and policies differ between files (*ōrn-*, *ānx-*, *ārd-*). A tool that's correct by rule can still give confidently wrong results.
- **Synthesis:**
  - Set one macron policy file (dictionary: L&S/OLD, with hidden quantities only where Allen is firm).
  - Normalise every card against it at build time, then run the phonetics.
  - Keep a regression list of the critic's cases. It's at 70 tests now; grow it every pass.
