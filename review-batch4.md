# Review: batch 4 (content/batch4-cards.json, 50 cards), 13 Oct 2026

The critic pass was run separately from production. Tools: `content/batch4_critic.py` checks the Latin against the online source text and compares macrons with Alatius. `batch4_check_urls.py` checks every link over HTTP. `batch4_build.py` lints unit order, raw_text, ids and licences. `tools_validate.py` checks the schema. The inscriptions were checked through the EDCS API (`batch4_edcs.py`) and RIB online. The images were checked by eye on a contact sheet (`batch4_src/contact.png`).

## Round 1: thesis, antithesis, synthesis

**Thesis (producer).**
- 50 cards across Units 1–10. Units 1 and 2 have 14 cards (7 each).
- 8 Vindolanda tablets: 154, 164, 291 ×2 (Severa's greetings, Lepidina's address), 310, 343, 346, 628.
- 6 EDCS-checked inscriptions: CIL VI 15346, IV 2457, IV 4342, IV 8623, VI 1527, VII 375 (RIB 818).
- 2 Bayeux captions. The rest are quotes chosen for core grammar.

**Antithesis (critic findings).**
1. **Macrons that Alatius disputed, real errors.**
   - *Ciceroniānus* should be *Cicerōniānus*, since Cicerō has a long o.
   - *Priscus* should be *Prīscus* (OLD).
   - *Atellāna* should be *Ātellāna*.
   - *residunt* is not a misspelling of *resident*. It is the regular form of *resīdō* ("settle, sit down"). The gloss and the note were wrong.
2. **Omissions not flagged.** Two quotes silently dropped *inquit*: Vespasian (Suet. Vesp. 23.4) and the aquilifer (BG 4.25).
3. **Source URL.** The Bernard of Chartres source_url was a Wikipedia page that does not contain the Latin.
4. **Learn-more links.** Three returned 404:
   - Pompeii_graffiti
   - Liber_Spectaculorum
   - Death_of_Nero
5. **Schema.**
   - q-gaius-gaia had no `person`.
   - The Ovid licence string "CC BY-SA 3.0 fr" is not in the enum.
6. **Images.**
   - The Cupid image was only a lips fragment, too weak for the card.
   - The Livia cut-out kept the museum plinth and label box.
7. **Date.** RIB 818 was dated "2nd c. AD". EDCS gives AD 122–138.
8. **Duplication risk.** Two cards come from tablet 291, plus the existing i-vindolanda card. Accepted: each tests different grammar (accusative and possessives, versus the farewell vocatives), and they are linked through related_cards.

**Synthesis (fixes applied).**
- Items 1–7 are fixed:
  - macrons corrected; the *resīdō* lemma, gloss and note rewritten
  - *inquit* omissions recorded in attribution_note
  - Bernard source_url now points to the Logic Museum text of Metalogicon 3.4
  - links replaced with Roman_graffiti, Inaugural_games_of_the_Flavian_Amphitheatre and Year_of_the_Four_Emperors
  - Gaia card given a person; licence normalised to CC BY-SA 3.0 with a `license_note` for the French port
  - images swapped: Eros, Toulouse Ra 184 (CC BY-SA 3.0 FR); Livia, Grumentum head (CC BY-SA 2.0)
  - RIB 818 date and EDCS-07801109 added
- **Alatius differences kept on purpose** (context beats the machine, policy §2):
  - *Hīc* (adverb)
  - *Gāia* (nominative, not Gāiā)
  - *habunt* (not hābunt)
  - *operā* (ablative)
  - *diūturna* (L&S/OLD)
  - *Collātīne* and *cāre* (vocative short e)
  - *gladīs* (contracted gladiīs)
  - *paria* (pār has a short a)
  - *subligāriōrum*
  - *rescrīpstī* (hidden quantity, scrīpsī)
  - *custōdiet* (OLD: custōs with a short u)
  - *cōdicellōs* (cōdex)
  - *Havē* (Suetonius's spelling of avē)
- **Expected "missing" results:**
  - constructed sentences
  - Brutus (apocryphal by design; Suetonius cited for the counter-evidence)
  - RIB and Vindolanda diplomatic texts with sublinear dots, brackets or expansions (each checked by hand against the RIB edition quoted in its attribution_note)
  - the Bayeux restored [MUS]

## Round 2 (re-check after the fixes)
- `batch4_build.py`: 50 cards, lint OK. This covers unit order, previews (no more than one in U1–3), raw_text on every i-/c- card, no id collisions, and related_cards resolving.
- `batch4_check_urls.py`: all 86 URLs return HTTP 200. `learn_more.verified_http` is stamped "200" on every card.
- `tools_validate.py`: 214/214 cards valid across all files, including batch 4.
- Images: all 50 come from Commons, and each licence was read from the Commons API. They are PD, CC0, CC BY or CC BY-SA, each with a full credit, a licence URL and a "modified" note. None is NC, ND or credited to the British Museum.
  - The Vindolanda tablets themselves are in the BM, so only third-party photos are used: Mike Peel (CC BY-SA 4.0) and Fæ's "own work" (CC BY-SA 3.0).
  - Cut-outs are used only for 3D objects. Paintings, manuscripts and inscriptions are not cut out.
- Phonetics: `phonetics.py --build` covers all 50 (218 entries). The tests pass 79/79.

**Verdict: PASS.**

## Open issues (not blocking)
- **Stand-in images**, all said so in the alt text: the distaff (Claudia), the Pompeian couple (Methe), the surgical kit (tablet 154), the fort ruins (tablets 164 and 343), and the Cicero bust (it repeats an existing card's statue, in a different crop).
- **Attribution levels**:
  - *traditional*: Gaius/Gaia (Plutarch's Greek), Constantine (Eusebius's Greek), the Hadrian poem (Historia Augusta) and Lucretia (Livy)
  - *apocryphal*: Et tu, Brute
- **Unmarked quantities** (policy §3): cervesa, Arepo, Carnotēnsis (the o).
- **Not yet on the site.** cards/index.html still loads only the three original files. batch4-cards.json must be added to its loader, or merged, before it shows on the site. Not done here: the site/UI worker owns index.html, and nothing was published.
- **Batch 5.** No batch5-cards.json existed when this pass ran. The validator and phonetics already pick it up automatically when it appears; it still needs its own critic pass.
