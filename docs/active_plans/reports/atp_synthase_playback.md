# ATP synthase alpha playback

## Result and scope

2026-11-12: PASS for actual Chromium/Firefox gallery playback, alpha compositing, reduced-motion
posters, responsive layout and the new ATP MP4 in a real LibreOffice Impress slideshow. The
manager froze all delivery inputs and released the exclusive graphics slot before these runs.
The slot is released again; owned application processes have exited.

This is a prepublication local preview of the actual sanitized README in GitHub's live shell/CSS.
No repository was published, committed or remotely modified. Scientific interpretation, source
coordinate fidelity and fresh molecular reproduction remain separately owned evidence.

Frozen README SHA-256:
`3c0eec7e0cec82da3758fb30a62253ad86e942b324b1e8895623418bac45aa42`.
Gallery helper SHA-256:
`5af490f74d526dc68927a2129db9c1af7c5366d89123766f7e166761946b9b22`.
All thirteen README/helper/gallery/full-ATP delivery hashes remained unchanged through graphics
release, recorded in `cleanup.json`. A later post-release hash check observes only the generated
ATP `render.json` changing; every tested movie, gallery asset, README and helper byte remains
unchanged. `post_release_hash_check.json` retains both render-record hashes for the manager.

## Decode and alpha

Pillow decoded every stored frame. Independent RIFF parsing verified durations and loop metadata.
Each animated gallery WebP has 60 frames, 5,000 ms total duration and loop 0; each matching poster
has one static frame and the same intrinsic canvas. Every decoded frame contains alpha-zero,
partial-alpha and opaque pixels.

| Asset under docs/screenshots | Canvas | Frames | Bytes |
| --- | --- | --- | --- |
| `atp_synthase_motor.webp` | 480 x 720 | 60 | 2,780,856 |
| `atp_synthase_motor_poster.webp` | 480 x 720 | 1 | 71,800 |
| `groel_rotation_alpha.webp` | 640 x 480 | 60 | 4,346,884 |
| `groel_rotation_alpha_poster.webp` | 640 x 480 | 1 | 63,660 |
| `hexokinase_closure_alpha.webp` | 360 x 540 | 60 | 2,242,604 |
| `hexokinase_closure_alpha_poster.webp` | 360 x 540 | 1 | 30,776 |

For each clip, all 125 native source hashes match the capture manifest. The checker independently
reconstructs the recorded fixed crop, uniform downsize and centered canvas for each selected source
frame. Decoded alpha matches this expected source alpha exactly across all 180 animated frames and
three posters. This detects lost transparency and stale disposal trails, rather than inferring
transparency from white RGB pixels. Fully opaque molecular pixels remain opaque and colored.
The quality-90 gallery RGB is lossy: maximum per-frame mean opaque RGB errors against the fitted
native source are approximately 3.34, 3.53 and 4.14 on the 0-255 channel scale for ATP, GroEL and
hexokinase. These previews are not advertised as lossless RGB copies.

Decoded contact sheets inspect frames 59, 0, 1, 15, 30 and 45 over white and `#0d1117`. The complete
silhouettes and ATP labels remain within one fixed canvas. No disposal tails or changing framing
appear. Last-to-first RGB differences on white are 4.410 for ATP, 16.305 for GroEL and 0.812 for
hexokinase, comparable to their respective first/last adjacent steps of 3.912/4.017,
15.911/16.276 and 0.801/0.895. These support visual seam inspection, not exact display pacing.

## Actual browser playback

Observed versions: Chromium 158.0.8127.18 and Firefox 159.0, using existing Playwright runtimes.
GitHub's Markdown API returned HTTP 200 at `Thu, 12 Nov 2026 16:47:35 GMT`, request ID
`FBE7:264EFE:20692:677D3:6AF5EDA6`. Its sanitized output retains all three `picture` elements,
reduced-motion `source` elements, animated image widths/alt text and ordinary poster links.

Fresh browser contexts load the public repository shell and CSS, then replace only the Markdown
article with the actual API response. Unpublished image requests are fulfilled with exact local
asset bytes. This does not replace animation frames, seek media, animate a canvas or restart an
image to manufacture motion. The sandboxed Chromium launch fails at macOS `bootstrap_check_in`;
the authorized native-service launch succeeds. No automatic approval rejection occurs.

Chromium covers desktop and narrow viewports, light/dark themes, and normal/reduced motion.
Firefox covers the same themes and motion preferences at desktop size: twelve contexts and
36 clip cases total. All contexts have no page errors and no horizontal document overflow.

| Viewport | ATP display | GroEL display | Hexokinase display | Document/scroll width |
| --- | --- | --- | --- | --- |
| Desktop, 1280 x 1000 | 360 x 540 | 640 x 480 | 360 x 540 | 1280/1280 |
| Narrow, 390 x 844 | 324 x 486 | 324 x 243 | 324 x 486 | 390/390 |

All images retain their intrinsic aspect ratio and nonempty alt text. Actual `currentSrc` selects
the animated WebP in normal mode and the matching poster in reduced mode. Normal image captures
at approximately 0, 0.7, 1.6, 2.7, 4.7, 5.6 and 6.7 seconds contain seven distinct RGB images in
all eighteen clip cases; the final pair still differs beyond a full five-second duration.
Reduced-mode captures at approximately 0, 0.9 and 5.7 seconds are RGB-identical in all eighteen
poster cases. These are natural browser animation observations, not exact rendered-fps measurements.

Actual native-image/contact-sheet inspection confirms clean transparent edges over both themes,
steady molecular scale, an unclipped ATP shaft/membrane and readable stator/rotor/membrane labels.
Blue hexokinase lobes and magenta glucose remain distinguishable. Caption screenshots at desktop
and narrow sizes retain the actual 16 px text, method limits and ordinary reproduction/poster
links without clipping or stretching.

### Native alpha pixel comparison

A separate native-size static `img` fixture positions each exact poster at integer CSS coordinates
on white and `#0d1117`; it isolates compositing from fractional inline layout in GitHub. Actual
Chromium PNG pixels are compared before their quality-90 WebP conversion. Across all six probes,
alpha-zero and opaque pixels match the expected RGB exactly. Partial-alpha mean RGB differences
are only 0.288-0.547 channel levels, consistent with compositor rounding. Hexokinase dark is 0.454.
There is no measured white rectangular background or opaque white fringe. The manager separately
inspected the actual dark teaching-size hexokinase capture and agreed its blue edges are clean.
A white-ish block seen when a tool directly displays the transparent poster is not reproduced in
these real browser composites; no product pixel change was needed.

Useful inspected evidence under `output/atp_synthase_playback/`:

- `chromium_desktop_dark_no-preference_hexokinase_03.webp`: actual dark teaching-size image.
- `chromium_desktop_dark_reduce_hexokinase_native_alpha.webp`: native-size dark alpha fixture.
- `chromium_desktop_dark_no-preference_hexokinase_contact.webp`: natural motion beyond one cycle.
- `chromium_narrow_light_no-preference_atp_03.webp`: narrow ATP label/shape inspection.
- `narrow_dark_atp_caption.webp`: actual narrow caption and links.
- `browser.json`, `browser_rgb.json`, `native_alpha_browser.json`: all versions, source selections,
  dimensions, timings, RGB comparisons and alpha pixel measurements.

## Actual Impress slideshow

The new ATP MP4 is H.264/yuv420p, 480 x 720, 25/1 fps, 5.000000 seconds and 125 frames.
FFmpeg fully decodes all 125 distinct frames without errors. These are metadata/decoder results.
MP4 SHA-256:
`5f93cff23e9c8974e7c7bb86d691caf49ac28cfd6bb331f1dc0cf9616a1a7caf`.

The editable one-slide probe uses the existing native LibreOffice media plugin, an embedded MP4,
`Loop=true`, `Mute=true` and a 2:3 media frame. Extracted `Media/animation.mp4` has the exact source
hash. Probe deck SHA-256:
`dbe77ef56612885aadac9c9f88c8ccb1dd458827a685dc22cd5aed4a3acfb1a7`.

LibreOffice 26.2.7.3 opens the probe through LaunchServices with its own disposable profile.
CoreGraphics identifies the on-screen 1920 x 1080 window `Presenting: atp_synthase_motor_mp4`,
owned by the launched PID 75454. After the startup allowance, eight actual window captures at
0.097, 1.122, 2.129, 3.144, 4.156, 5.160, 6.161 and 7.176 seconds show the orange/teal rotor
changing against the fixed blue stator. All eight central RGB crops are distinct. Inspection of
`atp_synthase_motor_mp4_00.webp` and `impress_contact.webp` confirms visible movie playback,
including after a five-second interval. The movie starts without a click in this probe.
Sparse captures establish visible motion and continued playback; they do not measure exact
Impress frame rate or exact movie phase at the screenshot time.

The original window capture is uniformly bounded to a 1920 px long edge before quality-90 WebP
encoding. `atp_synthase_motor_mp4_captures.json`, `_windows.json`, `deck_verification.json`,
`mp4_probe.json`, `mp4_framemd5.txt` and `impress_rgb.json` retain the native ownership, timing,
embedded-media and decoder evidence.

## Reproduction and cleanup

Ignored `output/atp_synthase_playback/` retains all probes, exact hashes, sanitized HTML, fetched
shell, logs and quality-90 WebP evidence. Disposable browser/analysis sources were removed from
`tests/_temp/` after retaining their copies in that ignored evidence directory. No permanent test,
dependency, product UI or repository ignore rule was added.

Commands from the repository root, run sequentially with exclusive graphics access:

```bash
node output/atp_synthase_playback/atp_playback_probe.mjs
node output/atp_synthase_playback/atp_alpha_pixels.mjs
source source_me.sh && python3 output/atp_synthase_playback/test_atp_playback_evidence.py
source source_me.sh && python3 output/atp_synthase_playback/build_deck.py
source source_me.sh && python3 output/atp_synthase_playback/capture_playback.py \
  atp_synthase_motor_mp4.odp
```

The original run builds the probe deck before browser capture; equivalent order above keeps each
native graphics application sequential. The native window helper was reused from the previous
verified capture. Environment observations: macOS 27.2.1 build 26B131, Python 3.12.16, Pillow 13.0.0,
Node 26.13.0 and FFmpeg 9.0.2. These are tested observations, not pins.

Both browsers and their contexts close normally; no localhost server was started. The owned
LibreOffice process exits with status 0 after capture and is independently confirmed absent before
its disposable profile is removed. The probe document lock is removed only after its owner exits.
All transient PNG captures are removed after pixel analysis/conversion. No ordinary user document,
LibreOffice profile or unrelated application process is changed or terminated.

This track does not rerender molecules, validate the staged mechanical science, replay the native
render pipeline, run the full repository suite, test exact pacing, test Firefox narrow layouts,
retest animated WebP in Impress, or publish/check the newly published GitHub gallery. MP4 playback
in Impress is demonstrated; WebP alpha/motion is demonstrated in browsers.
