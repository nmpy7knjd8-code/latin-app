# Latin audio sources (human voices only, no TTS) — 2026-10-13
Pronunciation choice: **restored classical** for every card, medieval ones too. Ecclesiastical recordings are listed only as optional extras.
Licence status: **VERIFIED** means I read it from the Commons API metadata or LibriVox. **UNVERIFIED** means I didn't check the terms this session, so treat it as all rights reserved until checked.

## A. Clips obtained (/workspace/latin-app/audio/, mp3 mono, loudness-normalised; originals in audio/src/)
| file | card | style | source | licence (VERIFIED) | attribution |
|---|---|---|---|---|---|
| veni-vidi-vici.mp3 | caesar veni | classical? (not checked by ear) | https://commons.wikimedia.org/wiki/File:Veni,_Vidi,_Vici.wav | CC BY-SA 4.0 | Westofines27, Wikimedia Commons |
| gallia-est-omnis-classical.mp3 | Gallia est omnis… | restored classical, slow | https://commons.wikimedia.org/wiki/File:La-cls-de-bello-gallico.ogg trimmed 0:00–0:04.85 | CC BY-SA 3.0 | Robert.Baruch, Wikimedia Commons |
| memento-mori-classical.mp3 | q-memento-mori | classical | https://commons.wikimedia.org/wiki/File:Memento_mori_la.wav | CC0 | SinaSabet28 (credit not required) |
| *extra* gallia-est-omnis-ecclesiastical.mp3 | Gallia | ecclesiastical | File:La-ecc-de-bello-gallico.ogg 0:00–0:05.1 | CC BY-SA 3.0 | Robert.Baruch |
| *extra* pater-noster-ecclesiastical.mp3 | q-vulg-pater-noster | ecclesiastical | File:Pater-Noster.ogg 0:00–0:08.3 | CC0 | Dan Palraz |
| *extra* dies-irae-chant.mp3 | q-dies-irae (sung) | Gregorian chant | File:Dies.irae.ogg 0:00.5–0:17.9 | Public domain (as tagged) | Membeth |
| *fallback* carpe-diem-fr-speaker.mp3 | carpe diem (first 2 words only) | French-accented | File:LL-Q150 (fra)-WikiLucas00-carpe diem.wav | CC BY-SA 4.0 | WikiLucas00 / Lingua Libre |
| *fallback* fiat-lux-fr-speaker.mp3 | fiat lux (2 words only) | French-accented | File:LL-Q150 (fra)-LoquaxFR-fiat lux.wav | CC BY-SA 4.0 | LoquaxFR / Lingua Libre |
Trim points came from ffmpeg silence detection. **No one has listened to them yet, so check each by ear.** CC BY-SA means the app needs on-screen credit and any edited clip must also be shared under BY-SA. That works for audio files bundled as separate assets.
Also available, not downloaded: Pater noster.ogg (PD, Geremia), Ave Maria in Latin language.ogg (PD, Italian-style), De profundis.ogg (sung, CC BY-SA 3.0), and LibriVox *Regula Sancti Benedicti* in Latin (PD), https://librivox.org/regula-sancti-benedicti-by-saint-benedict-of-nursia/. The LibriVox recording's Prologue should start with "Ausculta, o fili", which would cover q-ben-ausculta, but the reader's style hasn't been checked and it needs a timestamp.

No usable open recording found yet: Ō tempora, tolle lege, the Confessions lines, Vulgate verses (except Pater noster), Abelard, Bede, Magna Carta, Aquinas, Boethius, Einhard, Heloise, Dante; Gaudeamus and O Fortuna as spoken text (only sung or MIDI versions exist).

## B. Source survey
| source | URL | licence/terms | style | app use |
|---|---|---|---|---|
| Wikimedia Commons "Latin pronunciation" | commons.wikimedia.org/wiki/Category:Latin_pronunciation | per file, mostly CC BY-SA 3.0 (VERIFIED) | La-cls- = classical, La-ecc- = ecclesiastical | **Yes**, with attribution |
| Lingua Libre (Latin) | Category:Lingua_Libre_pronunciation-lat | CC BY-SA 4.0 (VERIFIED) | mixed; only 213 words, mostly 2 speakers | Yes |
| Wiktionary | en.wiktionary.org | audio is just the Commons files above | — | same as Commons |
| LibriVox Latin | librivox.org | public domain (VERIFIED) | varies by reader, often ecclesiastical or national style | **Yes, free**. Check each reader's style |
| Forvo | forvo.com | UNVERIFIED. Their API terms are known to restrict commercial use / caching | mixed | **Needs a licence from Forvo** |
| Latinitium (Daniel Pettersson) | latinitium.com | UNVERIFIED, commercial | restored classical, high quality | **Permission needed** |
| Legentibus (same team) | legentibus.com | UNVERIFIED, subscription | classical | **Permission needed** |
| Luke Ranieri (ScorpioMartianus / Polymathy) | youtube.com/@ScorpioMartianus; lukeranieri.com | UNVERIFIED, YouTube standard licence | very accurate restored classical; has full LLPSI readings | **Permission needed**. Best single candidate for one consistent voice |
| Satura Lanx, Quomodo Dicitur | podcasts | UNVERIFIED | conversational, mostly classical | Permission needed |
| Nuntii Latini (YLE; ended 2019) / Radio Bremen Nuntii Latini | yle.fi, radiobremen.de | UNVERIFIED, broadcaster copyright | Finnish/German-accented classical | Permission needed. Topical news, low value for these cards |
| Vatican Radio / Vatican News Latin | vaticannews.va | UNVERIFIED | ecclesiastical | Permission needed (extras only) |
| Evan der Millner, Latinum | latinum podcast / YouTube | UNVERIFIED; some material has been described as free, not confirmed | English-classical | Ask |
| SORGLL | sorgll.org (was Cornell/Bakersfield) | UNVERIFIED | classical, metrically read verse (Catiline, Horace, Vergil) | Permission needed. Strong for Cicero and Horace |
| LLPSI audio (Ørberg, Hackett/Domus Latina) | — | commercial | classical | Permission needed |
| Wheelock / Cambridge Latin Course audio | publishers | commercial | classical | Permission needed |
| Dickinson College Commentaries Core Vocab | dcc.dickinson.edu/latin-core-list1 | site content CC BY-SA (UNVERIFIED for audio) | — | **I found no audio on the list page** |

## C. Is there ONE source covering ~all words in one consistent classical voice?
Measured against the DCC core list (975 headword lemmas, macrons stripped, j→i):
- Commons La-cls (classical): **236/975 (24%)**. 320 of the 593 files come from a single uploader, EncycloPetey, so there's a partially consistent voice. Robert.Baruch has 36 and Erutuon 13.
- Commons La-ecc: 10/975. Lingua Libre Latin: 213 words total.
- Everything open combined: **239/975 (25%)**.
- Wiktionary: no separate pool. It uses the same Commons files.
**Answer: there is no openly licensed source that comes close.** The realistic paths are:
1. License a single speaker. Best fits: Luke Ranieri, or Latinitium/Legentibus, both precise restored classical. Ask them for the 1,000 core lemmas plus the card quotes, as a paid commission or licence.
2. Commission a classicist (a grad student, say) to record about 1,000 words and around 80 quotes under CC BY-SA or a work-for-hire. Roughly one or two days of studio time.
3. In the meantime, use the EncycloPetey classical files (CC BY-SA 3.0) for about 24% of the core words.

## D. Who to contact (not contacted)
Luke Ranieri (lukeranieri.com contact form), Latinitium/Legentibus (Daniel Pettersson & Amelie Rosengren, latinitium.com contact), SORGLL, Forvo (API/commercial licensing), Evan der Millner (Latinum), Satura Lanx / Quomodo Dicitur hosts, Hackett Publishing / Domus Latina (LLPSI audio).

## A2. Update, 2026-10-13 01:40: LibriVox clips and audio-map.json
**Mapping (superseded, see A3):** the former `content/audio-map.json` is keyed by card id, with fields {file, style, pronunciation_style, source_url (+timestamps), licence, attribution, note?, words?, alternates?}. It covers **31 of 135 cards: 26 classical, 5 ecclesiastical** (q-ben-ausculta, q-aug-inquietum, q-vulg-pater-noster, g-relative, q-dies-irae). Cards with an ecclesiastical recording should show the note.
The French-accented "carpe diem" and "fiat lux" clips are **excluded from the map**. They're neither restored classical nor ecclesiastical, and they cover only part of each quote.

**LibriVox Latin readers.** Every book licence below was read from archive.org metadata (PD Mark 1.0, or CC0 for the Seneca):
- **Malone (1945–2023):** Aeneid, Seneca's *Epistulae*, Lucretius. **Restored classical**: v is pronounced as w, c is always hard. Clear voice, the best fit.
- **Christoph Merlein:** *De Bello Gallico*. Classical.
- **bedwere:** *Regula Benedicti*, *Confessiones*, *De Civitate Dei*. Italianate/ecclesiastical. I inferred this from ti→tsi; it hasn't been checked by ear.

**Clips cut** with Whisper-assisted search plus ffmpeg silence detection (timestamps also in the map). **Still need a check by ear.**
| card | file | source file @ time |
|---|---|---|
| q-virgil-arma, x-meter | arma-virumque.mp3 | aeneidis_01 0:55.0–1:01.5 (Arma … ab oris only) |
| q-virgil-tantae | tantae-molis.mp3 | aeneidis_01 4:04.1–4:10.35 |
| q-virgil-timeo | timeo-danaos.mp3 | aeneidis_03 5:31.7–5:37.65 |
| q-seneca-vindica | seneca-vindica.mp3 | epistulae_01 0:58.5–1:02.9 |
| q-seneca-differtur | seneca-differtur.mp3 | epistulae_01 2:29.6–2:33.5 |
| q-seneca-aliena | seneca-aliena.mp3 | epistulae_01 2:34.6–2:40.8 |
| q-seneca-nusquam | seneca-nusquam.mp3 | epistulae_01 5:45.2–5:48.4 |
| q-lucretius-religio | lucretius-religio.mp3 | rerum_01 10:00.1–10:04.6 |
| q-caesar-gallia (alternate) | gallia-est-omnis-librivox.mp3 | bellumgallicum_01 0:29.85–0:33.8 |
| q-ben-ausculta (eccl.) | ausculta-o-fili.mp3 | regulasanctibenedicti_01 0:30.4–0:36.6 |
| q-aug-inquietum (eccl.) | fecisti-nos.mp3 | confessionum_01 1:09.65–1:15.95 |
Vocabulary cards (14: v-urbs, v-via, v-pater, v-filius, v-deus, v-amo, v-tempus, v-animus, v-rex, v-liber, d-dico, d-video, d-crux, d-scribo) use Commons La-cls word files saved in `audio/words/`. These are CC BY-SA 3.0/4.0, mostly by EncycloPetey; attribution is stored per word.

**Next targets, located but not cut.** Each needs a timestamp search in the same LibriVox sets:
- Aeneid: forsan 1.203 (file 01, after about 15:00), regere 6.851 (file 12)
- Georgics: fugit 3.284 (georgica_dm, file 5 or 6)
- Seneca: docent, Ep. 7 (epistulae_01, about 19–23 min). The first pass didn't find it.
- *Confessiones* 8.12.29 tolle lege, 8.7.17 da mihi, 10.27.38 sero te amavi (bedwere, ecclesiastical)
- *Regula* ch. 48 otiositas (file 06) and ch. 53 hospites (file 07, about 0:30–0:50)
- Boethius 2 pr. 2 rota (de_consolatione file 03)
- Other LibriVox Latin sets: Vulgate Psalms (Ps 22 only, so no De profundis), *Imitatio Christi* (sic transit, 1.3), Livy book I (Mario Morales, CC BY 3.0, archive.org/details/LivyAbUrbeConditaLiberI)
Sources with **no audio for these cards**: Cicero (Catilinarians), Catullus, Horace, Ovid, Juvenal, Tacitus, Martial, Res Gestae, inscriptions, Abelard, Bede, Magna Carta, Aquinas, Heloise, Einhard, Dante. These need commissioned or licensed recordings (see D).

## C2. Single source for all words: final numbers
DCC core list: 975 distinct headword lemmas. I matched on the first principal part, ignoring macrons and treating j as i.
- Commons La-cls (classical): **237/975 = 24.3%**, spread across the alphabet. 320 of the 593 files come from one speaker, EncycloPetey.
- All Commons (cls + ecc) plus Lingua Libre Latin: **247/975 = 25.3%**.
- Wiktionary: 0 extra, because it reuses the Commons files.
- Forvo, Latinitium/Legentibus dictionaries, Ranieri, LLPSI, Wheelock and Cambridge audio: I couldn't measure coverage because they're proprietary, and none is openly licensed. There's no evidence that any of them publishes a recording of every DCC lemma.
**Conclusion: no single open source exists.** To get one consistent restored-classical voice, commission or license about 1,000 words plus all quotes from a single reader. Luke Ranieri or Latinitium would be best. LibriVox's Malone (died 2023) can't be commissioned, but his public-domain readings already cover many Vergil, Seneca and Lucretius quotes and match the classical style.

## A3. Update, 2026-10-13 ~02:10: single map at audio/audio-map.json
- **`audio/audio-map.json` is the only map.** `cards/index.html` reads it. `content/audio-map.json` has been merged into it and removed.
- **Schema:** each card id maps to a list of entries {file (relative to audio/), style (button label), pronunciation_style classical|ecclesiastical|other, credit, license, license_url, source, changes (with trim timestamps), note?, word?}.
- **Totals:** 66 cards, 90 entries. 24 cards have a phrase recording; the rest have word recordings only. Every file exists.
- **Word recordings:** 64 entries on 43 vocab, grammar and other cards. Each is labelled "Word: X". They're Commons La-cls files under CC BY-SA, mostly from EncycloPetey; 53 files are in audio/words/.
- **New LibriVox clips** (public domain):
  - forsan-et-haec.mp3: Aen. 1.203, aeneidis_01 21:46.6–21:51.05, Malone, classical
  - fugit-irreparabile.mp3: Georg. 3.284, georgics_6 0:50.4–0:56.8, Malone, classical
  - omnes-hospites.mp3: RB 53.1, regula_07 0:14.85–0:21.8, bedwere, ecclesiastical
  - tolle-lege.mp3: Conf. 8.12.29, confessionum_15 22:47.2–22:49.6, bedwere, ecclesiastical. Used for both q-aug-tolle-lege and q-augustine-tolle.
- **Not found this pass.** Speech recognition on these files mostly returned garbage, so these still need a manual listen:
  - Aen. 6.851 regere (aeneidis_12)
  - Seneca Ep. 7 docent (epistulae_01, after 17:30)
  - Conf. 8.7.17 da mihi (likely confessionum_15, before 19:10)
  - Conf. 10.27.38 sero (confessionum_20)
  - RB 48 otiositas (regula_06, roughly 8:00–13:00; ch. 43 is at about 5:00)
  - Boethius 2 pr. 2 rota (consolatione_03)
  - Imitatio 1.3.6 "O quam cito transit gloria mundi" (imitationechristi_01). That's a different wording from the "Sic transit" card.
- **French-accented clips:** the carpe diem and fiat lux clips are still in the map as the viewer had them, but now marked pronunciation_style "other". Consider removing them under the classical-first rule.
