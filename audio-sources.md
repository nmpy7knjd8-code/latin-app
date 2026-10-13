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
