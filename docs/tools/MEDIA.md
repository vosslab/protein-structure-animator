# Delivery media

FFmpeg encodes frame sequences; it does not establish correct science or successful playback.
Sources: [FFmpeg documentation](https://ffmpeg.org/ffmpeg.html),
[formats](https://ffmpeg.org/ffmpeg-formats.html), and
[licensing](https://ffmpeg.org/legal.html). The local Homebrew build includes GPL components;
no FFmpeg executable is bundled here.

## Encode a five-second loop

```bash
source source_me.sh && python3 tools/encode_loop.py output/hexokinase_closure/frames
source source_me.sh && python3 tools/encode_loop.py output/groel_rotation/frames
```

[encode_loop.py](../../tools/encode_loop.py) requires exactly 125 contiguous, equally sized PNGs
with even dimensions. It writes H.264 MP4 with yuv420p and faststart, lossless animated WebP,
palette GIF, and a static WebP poster. At 25 fps each frame occupies 40 ms, giving five seconds.
GIF and WebP request infinite looping; an MP4 player must enable repeat separately.

The helper overwrites these generated media files in the frame directory's parent. Preserve edits
elsewhere. Keep the input frames and native sessions until delivery and reproduction checks pass.
Modern FFmpeg versions can differ in animated WebP decoding; Pillow is also used to inspect frame
count and per-frame durations. GIF palette conversion can introduce color changes and larger files.

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
