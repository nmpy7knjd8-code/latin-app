# Review: card UI prototype (cards/index.html, cards.js, previews)
_Reviewer agent, Oct 13 2026. Licences checked through the Wikimedia Commons API and the Met Collection API. See review-1.md for the content errors these cards inherit._

## Licence and source check (all pass)
| Card | Source | Verified licence |
|---|---|---|
| Caesar | Commons, Head_of_Julius_Caesar_from_Tusculum_MAntTorino_2089_n01.jpg (photo Marie-Lan Taÿ Pamart / Jastrow) | Public domain ✔ |
| Gallia | Met 248033 "Silver denarius of Julius Caesar, 47–46 BCE", Rogers Fund 1908 | isPublicDomain=true → CC0 ✔ |
| Cicero | Commons, M._Tullius_Cicero,_Capitoline_Museum,_Rome_(cropped).png (W. R. Rodriguez Hernandez) | CC0 ✔ |
| Horace | Commons, Horace,_Odes,_Florence,_Plut._34.1.jpg | Public domain ✔ |
| Augustine | Commons, Sandro_Botticelli_-_St_Augustine_-_WGA02709.jpg | Public domain (PD-art) ✔ |

The coin alt text (Aeneas carrying Anchises and the Palladium) matches the object. It no longer matches the schema example, which says "Gallic trophy". Update the schema example.

## ERRORS
1. **Content errors from review-1 are still on the cards.**
   - The Caesar context still says "report". It should say the words were a placard in his Pontic triumph (Suet. Iul. 37.2).
   - No Latin has macrons. It should read *Vēnī, vīdī, vīcī*; *dīvīsa in partēs trēs*; *Ō tempora, ō mōrēs*; *crēdula posterō*.
   - The Cicero context says "before the Senate". Add "in the Temple of Jupiter Stator". The Cicero bust itself is fine; it fixes the anachronistic Curia image from review-1.
   - **Fix:** update cards.js from the corrected schema.
2. **The era label overlaps the cut-out.** "ROMAN REPUBLIC" is drawn over the Caesar head (preview-mobile.png) and the Cicero bust, and the text-shadow doesn't make it legible. **Fix (choose one):**
   - (a) Put the label in a pill with a solid/blurred background: `background:rgba(0,0,0,.35);padding:2px 8px;border-radius:99px;backdrop-filter:blur(4px)`.
   - (b) Move it to the bottom strip next to the person's name.
   - (c) Keep the pop-out, but give `.art` a top margin of about 28px so the image only breaks the frame at the centre. Then put the label at top-right, away from the image's head.
   - (b) is the cleanest.
3. **Accessibility: both faces are read at once.** The back face is hidden only with `backface-visibility`, so screen readers read the front and back together. There is also no flip state. **Fix:**
   - Add `role="button"` and `aria-pressed` on `.card`.
   - Toggle `aria-hidden` and `inert` on the face that isn't showing.
   - Change the aria-label to "Quote card: {latin}, {person}. Press to reveal translation."

## SHOULD-FIX
4. **Credit and era text are too small and too faint.**
   - The credit is .56rem (about 9px) at opacity .7 on red. That is far below 4.5:1 contrast and hard to read on a phone.
   - The era label is .62rem.
   - **Fix:** use ≥.7rem at full opacity. Or move the full credit to the back face and keep only "© CC0 · source" on the front.
5. **The source link sits inside a clickable card.** That's a nested interactive control, the tap target is tiny, and `onclick=stopPropagation` is fragile. **Fix:** move it to the back face as a real ≥44px link and remove the stopPropagation hack.
6. **No `prefers-reduced-motion`.** **Fix:** add `@media (prefers-reduced-motion:reduce){.inner{transition:none}}`, or crossfade instead of flipping.
7. **Not all schema eras are styled.** Only republic, empire and late_antiquity have themes. Regal, early_medieval and high_medieval cards will render with no background. **Fix:** add their themes, or a default `--bg`.
8. **The renderer ignores some schema fields.** `aspect` and `focal_point` are never used (object-position is hard-coded), and neither are `gloss` and `attribution_note`. The design calls for tap-to-gloss. **Fix:** map `focal_point` to object-position, show `attribution_note` on the back, and make the Latin words tappable spans with `gloss`.
9. **The Augustine front was not captured.** In preview.png the card is shown flipped, so the arch-framed painting hasn't been checked visually. **Fix:** re-shoot with all cards on their front faces, plus one on its back.
10. **The cut-out edge has a hard fade.** The Caesar head ends in a soft gradient at the neck, so it reads as a vignetted photo rather than a cut-out. **Fix:** cut cleanly at the base of the bust or add a plinth shadow. QA the alpha mattes for halos on marble.
11. **`.coin .cut{border-radius:50%}` crops the coin.** The coin is already transparent, and the radius clips its irregular flan. **Fix:** remove it.

## NITS
12. The footer says "images public domain / CC0", which is correct for now. Generate this line from the data so it stays accurate.
13. Swipe has no affordance on desktop: the scrollbar is hidden and there are no arrows or dots. Add pagination dots.
14. The Horace MS (Plut. 34.1, Laurenziana, 10th c.) is a good choice. The torn mask works. Put the shelfmark and date in the alt text.

## Dialectic: visual approach
- **Thesis (current):** portrait 3:4 cards in era colours. Cut-out statues and coins break the top edge. Flat works get arched or torn masks. Minimal text on the front, translation and context on the back.
- **Antithesis:**
  - Cut-outs strip archaeological and museum context and can look like clip-art. Matte quality varies a lot (marble against a light background, halos).
  - Pop-out images clash with fixed UI (the era-label overlap is the first example).
  - Strong era colours lower text contrast.
  - Flip cards hide the translation. That's good for retrieval, but bad for the first exposure in CI reading.
  - Research on decorative images (Mayer's coherence principle) warns that "seductive details" that don't support the learning goal can hurt learning.
- **Synthesis:**
  - Keep cut-outs as the signature look, but use them only for 3D objects that pass a matte QA check.
  - Reserve a fixed "safe zone" (top-left label area and the text band) that images can't enter. Let only the centre ~60% of the top edge be broken.
  - Make the image do real teaching work: caption it in Latin (e.g. *Caesaris caput*), and offer "see in museum" for context.
  - Use two modes. **Learn mode** shows the translation and glosses on the front. **Review mode** shows the Latin only and the card flips.
  - Check every era palette for WCAG AA contrast against the body text before shipping.
