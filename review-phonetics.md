# Review: content/phonetics.py + phonetics.json (135 entries)
_Reviewer agent, Oct 13 2026. Spot-checked ~38 words with the engine against Wiktionary's classical IPA and W. S. Allen, *Vox Latina*. The built-in test passes 36/36._

**Correct:** Vēnī vīdī vīcī, Caesar, Cicerō, cēnsuit, magnus/ignis [ŋn], anguis/lingua [gʷ], urbs [rps], iacta ālea est, Iūlius, cuius [jj], patrem/tenebrae/volucris (stop+liquid onset), philosophia/Achillēs/triumphus (aspirates), nihil, mihi, deinde [ei̯], quī, virumque (enclitic stress), itaque (exception list), ancilla [ŋk], prōmptus, Rōmānum, Danaōs, Ūnum.

## ERRORS
1. **exspectō → /ɛkss.ˈpɛk.toː/** has a doubled s. *x* + *s* should collapse to /ks/: **/ɛk.ˈspɛk.toː/**. The same applies to *exsilium, exsul, exstinguō*. Source: Wiktionary *exspectō* [ɛkˈspɛktoː].
2. **Gnaeus → /ˈŋnae̯.ʊs/ "NGNEYE-us".** Initial gn is [gn]. The [ŋn] rule applies only between vowels. **Fix:** /ˈgnae̯.ʊs/. Source: Wiktionary *Gnaeus* [ˈɡnae̯ʊs].
3. **suāvis → /sʊ.ˈaː.wɪs/** has the wrong syllables and stress. After *s*, the *u* in suāvis/suādeō/suēscō is consonantal. **Fix:** /ˈswaː.wɪs/ "SWAH-wis". The engine already uses *suādēre* in the Lucretius card. Source: Wiktionary *suāvis*.
4. **euge → /ˈɛ.ʊ.gɛ/.** This should be the diphthong eu: /ˈeu̯.gɛ/. Add *euge* (and Greek-derived *eu-* words) to EU_WORDS. Source: Wiktionary *euge*.

## SHOULD-FIX
5. **Hidden quantity before consonantal i.** For *māior → /ˈmaːj.jɔr/, Pompēius, Trōiae*, the vowel before intervocalic *i* (= jj) is **short**; the syllable is heavy by position (Allen, *Vox Latina*, pp. 38–39). Wiktionary has *maior* [ˈmajjɔr], *Pompeius* [pɔmˈpɛjjʊs] and *Troia* [ˈtrɔjja]. **Fix:** shorten V before jj in the IPA, or drop the macron from the input.
6. **huic → "hweek".** The diphthong ui̯ sounds like "hooik", not like *wee*. The same applies to *cui*. **Fix:** RESP_V ui̯ → "oo-ee" (glided), e.g. "HOO-eek".
7. **The respelling loses vowel length,** which is the main thing learners must hear. *a* and *ā* both become "ah", and short *u* becomes "u", which reads as English "cut". **Fix:** mark long vowels (e.g. "ahh/AH" vs "a", or a ¯ in the respelling), and use "oo" for ʊ with a note. Alternatively, show short vowels in a lighter weight.
8. **Final -m and elision are ignored.** That's fine for prose, but wrong for verse cards: Aeneid 1.1 *multum ille* → *mult' ille*, and x-meter scansion depends on elision. **Fix:** add a `--verse` mode that does elision, nasalised final -m (Allen pp. 30–31) and synaloepha.
9. **rhētor → /ˈreː.tɔr/** drops the aspiration (rh = [r̥] or [rʰ]). In the respelling, *ph → p* makes "philosophia" look odd to English readers. Add a note: "p (aspirated, not f)."

## NITS
10. Z → /dz/ follows Allen. Wiktionary gives [zː] between vowels. Either choice is fine, but document it.
11. Wiktionary marks dentals [t̪ d̪ n̪] and velarised [ɫ]. Omitting them is fine for learners.
12. Respellings like "KUY-yus" and "PAYY-yus" are hard to read. Use "KOOY-yus" and "pom-PAY-yus".
13. The ecclesiastical toggle in the design has no engine yet. Add Italianate rules: c/g before e/i → [tʃ]/[dʒ], ae → [ɛ], v → [v], gn → [ɲ], ti+V → [tsi].

## Dialectic
- **Thesis:** a deterministic rule-based engine (Allen) gives consistent IPA and respellings for every card, with no recorded audio needed.
- **Antithesis:**
  - Rules miss hidden quantities and lexical exceptions (*suāvis*, *euge*, *Gnaeus*).
  - The macrons in the input are only as good as the macronizer.
  - Respellings anchor learners to English vowel habits, and the research says audio matters more.
  - IPA is opaque to most of the target users.
- **Synthesis:**
  - Keep the engine as the source of truth for the TTS lexicon. Feed its IPA (SSML `<phoneme>`) to the TTS so the audio matches.
  - Add an exceptions dictionary checked against Wiktionary, and expand the test set with every case above.
  - Show the respelling by default, with long vowels marked, and IPA on tap.
  - Have a Latinist record the top ~50 quotes.
