# Rome content mining: notes (units 1–8)

**Output:** `rome-cards.json` has 36 cards, all valid against `card-schema.json`. Each card has:
- `teaching_value` with `score` (1–5), `dcc_core_pct`, `non_core` and `rank`.
- `source_url` pointing to the online text the card was checked against.

The file is sorted by rank. To regenerate it, run `build.py` (it reads `cards.py` plus the scraped DCC list in /tmp/ll/dcc.json, which is from dcc.dickinson.edu/latin-core-list1).

## How cards were selected (Garrett's priority: learning over trivia)
- **Score** is a judgement call. 5 means short, a clear demonstration of a grammar point in the unit sequence, and a sentence pattern you can reuse.
- **Rank** sorts by score first, then by the % of non-proper-noun lemmas that are in the DCC Core 1000.
- Every card drills a named grammar tag (see `teaching_value.note`).
- I dropped trivia-only lines. Examples: Twelve Tables *si in ius vocat* (archaic forms) and *Quintili Vare, legiones redde* (not found in the Latin Library text).
- **Top 9 (score 5):**
  - Seneca *hominēs dum docent discunt*; can be used from Unit 3
  - Seneca *omnia … aliēna sunt, tempus tantum nostrum est*
  - Martial *sunt bona, sunt … mala plūra*
  - Tacitus *ubi sōlitūdinem faciunt, pācem appellant*
  - Cicero *salūs populī suprēma lēx estō*
  - Virgil *arma virumque canō*
  - Cornelia *haec ornāmenta sunt mea*
  - Horace *sapere audē, incipe*
  - Cicero *historia … magistra vītae*: five genitives in a row

## Verification
- Every literary quote was string-matched in the Latin Library text at its `source_url`.
- Citations: book and line/section numbers come from the page's markers. For Seneca, the letter number was counted from the SENECA LUCILIO headers.
- The two inscriptions (Pantheon, CIL VI 896; Arch of Titus, CIL VI 945) were checked against Wikipedia, which cites CIL. They should be double-checked in EDCS/EDR.
- **Macrons are my own.** They follow standard dictionary quantities. Please run them through a macronizer (e.g. Alatius) as a second check.
- **Spelling differences in the Latin Library text:**
  - *ferentīs* (we print *ferentēs*)
  - *inreparabile* (we print *irreparābile*)
  - *u* for *v* in some texts

## Attribution flags
- **traditional:**
  - *Iacta ālea est*: Plutarch says Caesar spoke Greek
  - *Vae victīs*: Livy reporting a Gaul ~350 years later
  - Cornelia's jewels: Valerius Maximus, ~150 years later
- **Speech written by the author, not the speaker:** Tacitus/Calgacus and Virgil/Laocoön.
- *Salūs populī*: the original text begins *Ollīs …*, and the motto form is a trimmed version.
- *Cēdant arma togae*: Cicero is quoting his own lost poem.

## Images
- All are on Wikimedia Commons. Licences come from the Commons API `extmetadata` (CC0, Public domain or PD) and are within the schema's enum.
- `src` is `TODO:<file>` until someone downloads the image and cuts it out. Cards whose image is already in the app use its `img/*.webp`.
- **Good 3D cut-out candidates (Met CC0):**
  - Augustus portrait
  - helmeted soldier head
  - bronze cuirass torso
  - Venus Genetrix
  - bust of a woman and bust of a boy
  - glass cup
  - Octavian denarius
  - Romulus & Remus
  - Commons CC0 objects: Capitoline Wolf and Laocoön
- **Weak or stand-in matches; swap them later:**
  - lamp image for Martial and Seneca *nusquam*
  - "know thyself" mosaic for Lucretius
  - Octavian coin for Horace *Exēgī*
  - boy bust for Catullus 101
  - "Pseudo-Seneca" is not really Seneca (the label already says so)
- **Rejected:** CC BY-SA 2.x/3.0 images (Pantheon photos, Curia, *Cave canem*, *Iudaea capta*), because they're outside the schema's licence enum.

## Gaps / next steps
- **Pompeii graffiti and coin legends:** not done. I couldn't verify a CIL text online in the time I had, and the Met's API returned 410 Gone.
- **Unit 5 (Gods) is thin:** only *timeō Danaōs* and *est modus*. It needs Vesta/Jupiter material.
- **Ecl. 10.69 *omnia vincit Amor*:** the Latin Library page is missing, so it's not verified.
- `vocab_ids` are lemma strings with macrons stripped. They aren't mapped to vocab-record ids yet.
