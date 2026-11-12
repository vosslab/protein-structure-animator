# Delivery media

FFmpeg encodes frame sequences; it does not establish correct science or successful playback.
Sources: [FFmpeg documentation](https://ffmpeg.org/ffmpeg.html),
[formats](https://ffmpeg.org/ffmpeg-formats.html), and
[licensing](https://ffmpeg.org/legal.html). The local Homebrew build includes GPL components;
no FFmpeg executable is bundled here.

## Encode a five-second loop

```bash
source source_me.sh && python3 tools/encode_loop.py output/hexokinase_closure/frames
source source_me.sh && python3 tools/encode_loop.py output/groel_rotation_oxillustrate/frames
```

[encode_loop.py](../../tools/encode_loop.py) requires exactly 125 contiguous, equally sized PNGs
with even dimensions. It writes H.264 MP4 with yuv420p and faststart, lossless animated WebP,
palette GIF, and a static WebP poster. At 25 fps each frame occupies 40 ms, giving five seconds.
GIF and WebP request infinite looping; an MP4 player must enable repeat separately.

Animated WebP and its poster retain source alpha. MP4 and GIF explicitly composite onto white
before encoding; neither is the transparent delivery. Use native transparent source frames rather
than removing white from opaque molecular images. The real-codec regression command is
`source source_me.sh && python3 tests/e2e/e2e_encode_alpha.py`; its synthetic 125-frame probe
checks exact decoded WebP/poster RGBA, opaque GIF, and white-composited MP4. See
[atp_synthase_encoder.md](../active_plans/reports/atp_synthase_encoder.md) for measured limits.
Native ATP delivery also verifies exact alpha, exact RGB wherever alpha is nonzero and exact
light/dark composites. Lossless WebP can normalize invisible RGB under alpha zero; raw RGBA
identity at fully transparent pixels is not promised for native sources.

Transparent source examples use `output/groel_rotation_alpha/frames` and
`output/hexokinase_closure_alpha/frames`; ATP uses `output/atp_synthase_motor/frames`.
The gallery uses 60 samples totaling five seconds at 12 fps average, quality-90 color and exact
source alpha. Fixed canvases are 480 x 720 ATP, 640 x 480 GroEL and 360 x 540 hexokinase. See
[atp_synthase_gallery.md](../active_plans/reports/atp_synthase_gallery.md) for crops and checks.
A preview uses one union crop across the full motion, including outlines and labels, with one
fixed aspect and scale. Paste RGBA without an extra mask: applying alpha twice changes edge
coverage. Inspect all decoded frames and composites over light
and dark backgrounds. Actual browser motion, reduced-motion fallback and replay remain separate
acceptance checks; a synthetic codec pass does not establish them.

The helper overwrites these generated media files in the frame directory's parent. Preserve edits
elsewhere. Keep the input frames and native sessions until delivery and reproduction checks pass.
Modern FFmpeg versions can differ in animated WebP decoding; Pillow is also used to inspect frame
count and per-frame durations. GIF palette conversion can introduce color changes and larger files.

The canonical GroEL frames come from [OXILLUSTRATE.md](OXILLUSTRATE.md). The retained Mol*
alternative uses `output/groel_rotation/frames`. The historical Rust integration passed Chromium
WebP, GIF and MP4 motion checks, including a natural MP4 loop, and actual LibreOffice 26.2.7.3
MP4 slideshow motion.
Exact Impress pacing and new animated WebP insertion were not tested. The GIF/blank-WebP Impress
observations below describe the earlier Mol* outputs.

The current [atp_synthase_playback.md](../active_plans/reports/atp_synthase_playback.md) records
actual Chromium/Firefox alpha gallery motion, reduced-motion posters and responsive layout PASS,
plus visible new ATP MP4 motion in a real Impress slideshow. These application checks do not
measure exact display pacing or establish animated WebP/alpha support in Impress.

## Check each delivery separately

Inspect a poster, intermediate frames, endpoint geometry and the seam. Decode all MP4 frames with
FFmpeg; inspect GIF/WebP frame count, total duration, dimensions and loop flags with Pillow.
Then check real browser image animation and MP4 playback. A browser's successful image load alone
does not establish animation playback.

LibreOffice Impress slideshow is a separate check. Its media support depends on the installed
application and operating system. Animated GIF is the first teaching-slide candidate; WebP can
import as a still, and MP4 playback can depend on system codecs. In LibreOffice 26.2.7.3 on macOS,
the tested GIF and MP4 probes visibly played in slideshow mode, while animated WebP embedded as an
ODP image shape showed a blank area. This is specific to that insertion route and installation.
GIF pacing appeared slower than MP4, so prefer MP4 when paced presentation matters; the actual
slideshow frame rate was not measured. Record the observed application and format rather than
claiming support from successful encoding or a document import.
