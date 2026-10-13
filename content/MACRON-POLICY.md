# Macron policy (all card files: rome, medieval, learning)

Decided 13 Oct 2026. Use it for every new card and every fix.

1. **Mark every long vowel, including hidden quantities.** Hidden quantity means a vowel that is long by nature in a syllable that is already heavy by position. Follow the **Alatius macronizer**, with the **Oxford Latin Dictionary** as the tiebreaker:
   - *ōrnāmenta*, *ānxius*, *ārdēs*
   - *Quīntilius*, *scrīptor*, *rēctē*, *Mārcus*, *Mārtius*, *prīnceps*, *nūntius*, *ūsque*
   - the regular lengthening before *ns*/*nf*: *cōnsul*, *dēscēnsus*, *īnfāns*
2. **Context beats the machine.** When Alatius picks the wrong lemma or form for the sentence, keep the contextually correct form and record it in the card notes. Known overrides in the Rome batch:
   - *legis* (present tense, short e) vs Alatius *lēgis*
   - *hīc* (adverb)
   - *Agrippa* (nominative)
   - *Cavē* (imperative)
   - *vēnit* (perfect) and *fugit* (present)
   - *putēmus*
   - *abūtēre* (future)
   - *aere* (from *aes*)
   - *Trōiae*
   - *idem* (neuter, short i)
   - *Fortīs* (accusative plural)
   - *levis* "light" (short e; *lēvis* means "smooth")
3. **Greek names:** mark a vowel long only where the Greek has η/ω or a long ι/υ that the OLD records: *Ōmega*, *Dionȳsius*. When unsure, leave the vowel unmarked and say so in a note.
4. **Inscriptions and coins** keep the original capitals (no macrons, V for U). They are followed by ` — ` and a lower-case macronized expanded reading. Examples:
   - `CAVE CANEM — Cavē canem!`
   - `IMP·CAESAR·DIVI·F — Imperātor Caesar Dīvī fīlius`

   Abbreviations expanded in the original text use parentheses: `F(ILIO)`. Square brackets mean restored lost text (Leiden convention), not expansion.
5. **Metrical lengthening** (e.g. *Ītaliam* in Aeneid 1.2) is kept as printed. Add a gloss note giving the normal quantity.
6. **Medieval texts** follow the same classical quantities. The spoken realisation is handled by the ecclesiastical audio and IPA in `phonetics.py`, not by removing macrons.
7. **Check:** before shipping, run the Latin through Alatius (alatius.com/macronizer) with the macrons stripped, then review every difference against this policy. `phonetics.py --build` writes `macron-report.md` listing cards with no macrons at all.
