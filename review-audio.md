# Review: audio (audio-sources.md, content/audio-map.json, audio/audio-map.json)
_Reviewer agent, Oct 13 2026, ~01:55 ET._

**Method:**
- **Licences:** Commons licences re-queried through the API for all 24 Commons files. LibriVox licences read from archive.org `metadata/licenseurl`.
- **Speech recognition:** every clip transcribed with **faster-whisper** (`/workspace/venv`), first `small`, then `medium` on the 19 sentence clips, with `language=la`.
- **Trim check:** start and end levels via ffmpeg (`volumedetect`, `silencedetect`, and the RMS of the first and last 50 ms).

**Caveat:** Whisper's Latin is weak. On short clips it often hallucinates in other scripts or in English. A *garbled* result therefore proves nothing. A *clean* result is good evidence of the words spoken, and its spelling (*w* for *v*, *ai* for *ae*) is weak evidence of the pronunciation style. Whisper cannot reliably tell hard from soft *c*, so the ecclesiastical labels for *c/g* could not be confirmed.

## A. Licences and attribution
| Check | Result |
|---|---|
| 24 Commons files: licence and author vs the map | **PASS.** All match (CC BY-SA 3.0 ×19, CC BY-SA 4.0 ×2, CC0 ×2, PD ×1). The authors are EncycloPetey, Erutuon, Robert.Baruch, Westofines27, Dan Palraz, SinaSabet28 and Membeth. |
| LibriVox items | **PASS.** Aeneid, Benedict, Confessions and Bellum Gallicum are **PD Mark 1.0**. Seneca *Epistulae* is **CC0**, and the map labels it correctly as "CC0 (LibriVox)". |
| Dies.irae.ogg "Public domain (as tagged)" | **SHOULD-FIX.** This is a performance recording. Commons' PD tag needs a basis: an old pre-1927 recording, or the uploader's own release. Check the file page for the reason before relying on it. |
| CC BY-SA attribution completeness | **SHOULD-FIX.** Entries give author and licence name only. BY-SA 3.0/4.0 also require a **licence URL**, the **source link** (present), and an **indication of modification**. Every clip was trimmed and loudness-normalised. Add `"modified": "trimmed, loudness-normalised"` and the licence URL, and show both in the card's credit and on the credits page. |
| Two maps | **SHOULD-FIX.** `audio/audio-map.json` (01:14, "Temporary map…", a different structure) disagrees with `content/audio-map.json` (31 entries). The site fetches content/ first, so the stale copy is harmless but confusing. Delete it or regenerate it from the content map. |

## B. Speech recognition vs card Latin, and trim boundaries
| Clip | Whisper heard | Card match | Trim | Style |
|---|---|---|---|---|
| arma-virumque | "Arma wi-rum quekano, troi aekwi prima saborese" (small) | ✔ full line through *ab ōrīs* | ✔ | **classical ✔** (v = w) |
| timeo-danaos | "Quid quidid est, Timeodan os, et dona ferentes" | ✔ | ✔ | classical (plausible) |
| tantae-molis | "Tantai mollus erat, Romanam condere gentem" | ✔ | ✔ | **classical ✔** (ae = ai) |
| lucretius-religio | "Tandum religio potuwit swadere malorum" | ✔ | ✔ | classical (*sw-*) |
| seneca-nusquam | "Nusquam est qui ubique est" | ✔ | ✔ | — |
| seneca-differtur | "Dum differtur vita transcurrit" | ✔ | ✔ | — |
| seneca-vindica | Only "…vindica te tibi" ("Wynne ka te tibi") was recognised. *Ita fac, mī Lūcīlī* in the first 2.5 s was not. | probably ✔ | **⚠ end** at −34 dB, only 18 dB below peak, so the final syllable may be clipped. Re-trim with about 150 ms of tail. | **classical ✔** (v = w) |
| seneca-aliena | not recognised | **unverified** | ✔ | — |
| veni-vidi-vici | "Wee wee wee" | ✔ (w- onsets) | **⚠ end** at −35 dB | **classical ✔** |
| **gallia-est-omnis-classical** | "Dalia/Gallia est omnis divisa." | **✘ TRUNCATED.** The clip ends after *dīvīsa*, with no *in partēs trēs*. The slow reader needs about 7 s, but the trim was 0:00–0:04.85. | **✘ start** at −37 dB, so the onset of *G-* is clipped | classical (assumed) |
| **gallia-est-omnis-ecclesiastical** | "Galia est omnes divisa" | **✘ TRUNCATED** (same problem, 0:00–0:05.1) | ✔ | not testable |
| gallia-est-omnis-librivox | "Galya omnis diwisa in …" (hallucinated repeats) | probably complete in 3.98 s. Confirm by ear. | ✔ | **classical ✔** (diwisa) |
| **fecisti-nos** | "**Quia** fecisti nos ad te, et inquietum est cor nostrum, donec requiescat in te" | **✘ starts with the extra word *quia***. The card begins at *Fēcistī*. | Re-trim the start by about 0.4 s | labelled ecclesiastical, "inferred". **Unconfirmed.** |
| ausculta-o-fili | "Ausculta o fili, praecepta magistri, et inclina aurem cordis tui" (small) | ✔ words. **Spelling mismatch:** the reader says ***Ausculta***, but the card prints the RB manuscript form ***Obscultā***. Note this on the card, or show "Ausculta" in the audio caption. | **⚠ end** at −37 dB | labelled ecclesiastical, "inferred". **Unconfirmed.** |
| **pater-noster-ecclesiastical** | "Pa[ter noster] kui es in celis, santificetur nomen tuum, **adveniet [regnum] tuum**" | **✘ overruns.** The card ends at *nōmen tuum*, but the clip goes on into *adveniat rēgnum tuum*. It's also used for g-relative, which ends even earlier. Trim to about 5.5–6 s or show the full text. | — | **ecclesiastical ✔** (ae = e, *celis*) |
| dies-irae-chant | "Dies irae, dies illa, solvet saeclum in favilla, teste David cum Sibylla" (medium) | ✔. It includes line 3 (*teste David cum Sibyllā*), which the card doesn't show. Fine, but show the full stanza with the audio. | ✔ | sung chant ✔ |
| memento-mori-classical | not recognised (English hallucination) | **unverified** | **⚠ end** at −31 dB, so it's likely cut | — |
| carpe-diem-fr-speaker | "Carpe Diem" | ✔ only 2 of 7 words | ✔ | French-accented. Keep it as a fallback only. |
| fiat-lux-fr-speaker | not recognised | unverified | ✔ | French |
| **words/** (55 single-word clips) | Whisper can't handle 1-second Latin words. Clean results: *regina, romanus, scribo, dico, non, dea, lararium, centurio* ("quinturio") | mostly **unverified** | — | These are EncycloPetey's **La-cls-** series, which is labelled classical by series. Accept as classical. |

**Errors:**
- The two Gallia clips are truncated.
- *Fecisti* starts with an extra *quia*.
- *Pater noster* overruns the card text.

**Should-fix:**
- Re-trim the 4 clips cut short at the end (vindica, veni, ausculta, memento).
- Add the *Ausculta/Obsculta* caption.
- Listen to aliena, memento, fiat lux and the two "inferred" ecclesiastical clips by ear.

**Suggested fix for the trims:** cut on word boundaries from Whisper `word_timestamps`, with 150 ms of padding. That would have caught all of the above. Add the ASR check to the audio build, and fail the build if the transcript is clean and covers less than about 80% of the card's tokens.

## C. pronunciation_style labels
- **Confirmed classical** (v = w or ae = ai heard): arma, veni, tantae, vindica, gallia-librivox, lucretius (sw-).
- **Confirmed ecclesiastical:** pater noster (ae = e).
- **Unconfirmable by ASR:** fecisti-nos and ausculta-o-fili. Both are "ecclesiastical (inferred)" from the reader *bedwere*, and the soft-*c* test isn't possible with Whisper.
  - Ausculta contains *praecepta*, the decisive word: an ecclesiastical reader says "pre-CHEP-ta", a classical one "prai-KEP-ta". One listen settles it.
- **Policy conflict:** audio-sources.md says "restored classical for every card", but q-ben-ausculta and q-aug-inquietum get ecclesiastical audio as their **primary** clip. Either list them as `alternates` (consistent with the policy), or change the policy to "audio follows card register" (consistent with review-medieval-3's synthesis).

## D. Dialectic: open clips vs one commissioned voice
- **Thesis (current):** stitch together open-licensed clips (Commons, Lingua Libre, LibriVox). It's free, legal with attribution, and real human voices.
- **Antithesis:**
  - So far there are about 6 different readers with different accents, speeds and mic quality.
  - Two French-accented fallbacks.
  - Style is inferred, not known.
  - Several clips are cut mid-word.
  - Only around 19 of about 150 sentence cards have audio.
  - Learners imitate whatever they hear, so inconsistent models undermine the restored-classical promise.
  - Every BY-SA clip adds attribution overhead.
- **Synthesis:**
  1. **Commission one voice** for all card Latin (around 150 lines at about 5 s each, under an hour of studio time).
     - The research's best candidate is Luke Ranieri or a Latinitium reader.
     - Licence the recordings **CC BY 4.0** or as a work-for-hire.
     - Get a classical and an ecclesiastical pass for the register-tagged cards.
     - Give the reader the phonetics.json IPA as a script, so the audio and the transcription agree.
  2. **Until then:** keep the open clips only where the words are verified by ear or ASR and the style is confirmed. Drop the French fallbacks.
  3. **Keep LibriVox** as "hear it in context" (longer passages, clearly credited). It suits graded readings even after a single voice handles the cards.
  4. **No TTS** for card audio, as audio-sources.md says. If TTS is ever used, use it only with the SSML `<phoneme>` from phonetics.json and label it "synthetic".
