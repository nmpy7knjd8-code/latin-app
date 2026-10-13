# Review: live site https://nmpy7knjd8-code.github.io/latin-app/ (commit bc0f33b)
_Reviewer agent, Oct 13 2026. Checked with curl against the live site, the repo's cards/index.html, and live.png. I did not test on a real phone; the mobile notes come from preview-mobile*.png and the CSS._

## ERRORS
1. **Audio is not connected.** index.html:188 fetches `../content/audio-map.json` or `../audio/audio-map.json`. **Both return 404**, so `window.AUDIO` is never set. Meanwhile 8 mp3s sit in `audio/` and are reachable (e.g. audio/veni-vidi-vici.mp3 returns 200), and there are no `<audio>` or `new Audio` calls anywhere. **Fix:** commit `audio/audio-map.json` mapping card id → {classical, ecclesiastical, credit}. Render a ▶ button only when an entry exists, with the clip's credit on the card back.
2. **Learning cards show broken or empty images.** For cards that only have `image_idea`, index.html:179 sets `src:""`. That makes an empty `<img>` (broken icon or blank) on all 65 learning cards. **Fix:** don't render `<img>` when src is empty. Show an era-coloured typographic placeholder instead: a large initial or icon plus the `image_idea.description`. Or hide those cards until the images are verified.
3. **"TODO:" images are hotlinked, uncut originals.** index.html:181 rewrites `TODO:` to `Special:FilePath/...?width=600`. Many rome-cards are marked `transparent:true` and `kind:statue_cutout`, so rectangular photos with backgrounds get rendered with the cut-out style (128% height, overflowing the frame). This also hotlinks Wikimedia on every view. **Fix:** treat a TODO image as a framed (`arch`) image regardless of `transparent`. Better, run the rembg pipeline and self-host WebP files.
4. **The public footer leaks internal licence-status text.** live.png shows: *"Public domain / CC0 / PD-art / CC BY-SA 4.0 / PD-art likely; verify file page / CC BY-SA likely; verify / … BM licence varies; verify / verify"*. It's clutter, and it tells users that licences are unverified. It also implies BM material that may be non-commercial. **Fix:** make the footer one line, "Images: public domain & open licences · Credits", linking to a generated credits page. Never publish cards whose licence is still "verify" (filter them in the build).

## SHOULD-FIX
5. **CC BY-SA attribution is incomplete.** Cards show "CC0 · credit on back", and that's fine. For CC BY-SA images and audio, though, the licence requires the author, a licence link and an indication of changes. Cut-outs are derivatives. **Fix:** give the card back an author, a licence link, a source and "background removed". Put the same on the credits page.
6. **Respelling line clutter.** The front face now stacks Latin, respelling, person, era and licence (live.png). The respelling is the same size and colour as the person line. **Fix:** front = image + Latin + a small 🔊/respelling chip. Move person, era and licence to a single small meta row, or to the back.
7. **Mobile.**
   - Cards are `min(82vw,320px)` and look good on a phone (preview-mobile).
   - Swiping has no affordance on desktop: the scrollbar is hidden and there are no arrows or dots.
   - The Learn/Review toggle has no `aria-pressed`.
   - The tap targets for the source link and gloss words are below 44px.
   - **Fix:** add pagination dots and arrow keys, use `aria-pressed` on the toggle, and make gloss targets at least 44px.
8. **Era label overlap.** It still collides with tall cut-outs. Check this against the earlier review-cards.md #2 on the live build; live.png shows the label moved into the meta row, which fixes it if that change is applied everywhere.
9. **Missing pieces.** There are no deep links per card (`#q-caesar-veni`), no loading state while the 3 JSON files load, and no error state if a fetch fails.
10. **Audio clip choice.** Files such as `carpe-diem-fr-speaker.mp3` and `fiat-lux-fr-speaker.mp3` are likely French-accented, not restored classical. **Fix:** label the pronunciation style on each clip, or don't attach them to the "classical" slot.

## NITS
11. The root index.html is a meta-refresh to `cards/`. It works, but it's slow and bad for SEO. Serve the app at the root, or use a JS redirect plus a canonical link.
12. There is no favicon, no `<meta name="description">` and no Open Graph image.

## Dialectic: ship now or ship clean
- **Thesis:** publish early and show all content, so Garrett can see progress.
- **Antithesis:** a public site with broken images, unverified licences and dead audio undercuts the project's "source-checked" promise, and carries real licensing risk (non-commercial BM images, incomplete CC BY-SA attribution).
- **Synthesis:**
  - Run two builds. The **public** build includes only cards with a verified licence, an image or placeholder, and passing lints.
  - A `?draft=1` view shows everything, with "verify" badges, for review.
  - The CI step that generates the deploy also generates the credits page and the audio map.
