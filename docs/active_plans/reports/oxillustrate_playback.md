# Rust GroEL playback verification

Status: the canonical Rust GroEL delivery decodes correctly, animates in Chromium, and plays as
an embedded MP4 in an actual LibreOffice Impress slideshow. Verified on 2026-11-12 after the
renderer released the exclusive graphics slot. Scientific fidelity and fresh rendering remain
separate evidence; this report does not establish either from playback.

## Files and decoding

The tested delivery is `output/groel_rotation_oxillustrate/`. Hashes agree with the renderer's
stable post-replay handoff. The ODP contains the exact MP4 bytes, checked by extracting and
hashing `Media/animation.mp4`.

| File | SHA-256 |
| --- | --- |
| `animation.webp` | `f8e3745e3505d50a08d69037119d25ede9b553e985363cfa202097c12d553396` |
| `animation.gif` | `39e35cc791964b122db68583a3d8f67d1a9500b54ead905186258ccae4e5118a` |
| `animation.mp4` | `f68e03790b383e45545a0f86ab9be2ae1fe375900377323c286ca75518d58020` |
| `poster.webp` | `b013364686f9a243ba89bc9954acd30e94e5e83a45a9f6959348ea2472ee52df` |
| `render.json` | `0e2162c91d79b930edaf5ab5b1f5ce83bf2187044d82a50424d712a0a4b0f4ba` |

The retained render record identifies input `output/inputs/1oel_assembly1.cif`, SHA-256
`fb61ff7da5bafbd92f95a85876616cf5b7d43f8219af4260c81db295aa4ca49d`, and native executable
SHA-256 `9a2441d4383340bd2e16ae1aa0cf447f98543187655d4e430d7d42c2df9e3d17`. Those
identifiers link the tested delivery to the renderer record; this verification does not re-audit
the molecular coordinates.

| Check | Observed result |
| --- | --- |
| PNG frames | All 125 load successfully; each is 640 x 640 |
| Animated WebP | 125 distinct decoded frames; 640 x 640; 40 ms each; 5000 ms; loop 0 |
| GIF | 125 distinct decoded frames; 640 x 640; 40 ms each; 5000 ms; loop 0 |
| MP4 probe | H.264, yuv420p; 640 x 640; 25/1 fps; 5.000000 seconds; 125 frames |
| Complete MP4 decode | FFmpeg decodes all 125 distinct frames with no error output |

Loop 0 means indefinite looping for these image formats. These are decoder and metadata
observations, not measured application frame rates. Exact per-frame image hashes, timings,
commands and file sizes are in `output/oxillustrate_playback/decoding.json`; the complete MP4
frame checksums are in `mp4_framemd5.txt` beside it.

## Actual browser playback

Chromium 158.0.8127.18 loads the original WebP, GIF and MP4 over HTTP from a probe-owned localhost
server. This is a real headless browser run, using the already installed browser. No frame
injection, canvas replacement, video seek or synthetic animation is used.

Seven screenshots at approximately 0.098, 0.701, 1.512, 2.950, 5.330, 5.926 and 7.258 seconds show
changing orientation in all three original media elements. Each format has seven distinct RGB
protein-area crops. Visual inspection of each retained contact sheet confirms visible GroEL
rotation, consistent white background and no apparent clipping.

The MP4 is 640 x 640, reports a five-second duration, and remains unpaused throughout 65 samples.
Its natural loop is directly observed: `currentTime` changes from 4.9534 to 0.0473 seconds while
the monotonic sampling clock advances from 4.932 to 5.037 seconds. The decoded-frame counter grows
from 5 to 184 over 7.174 seconds. Its final dropped-frame counter is 1; this observation supports
working playback and looping rather than a claim of perfectly paced 25 fps display.

Browser evidence in `output/oxillustrate_playback/`:

- `browser_playback.json`: browser version, HTTP URL, metadata, all timed samples and capture paths.
- `browser_webp_contact.webp`, `browser_gif_contact.webp`, `browser_mp4_contact.webp`: inspected
  quality-90 contact sheets and matching individual cropped captures.
- `browser_00.webp` through the seven recorded sample names: full browser screenshots, quality 90.

The source contact sheet `source_seam_midpoints.webp` compares frames 124, 0, 1, 31, 62 and 93.
The last-to-first transition has the expected small orientation step; the intermediate views
retain a consistent scale and unclipped silhouette. Together with the natural browser loop this
provides a seam check, without treating a screenshot as an exact frame-pacing measurement.

## Actual Impress slideshow

The probe is an editable, one-slide ODP with native text and a native LibreOffice media object.
The original MP4 is embedded, with `Loop=true` and `Mute=true`. Package XML parses, and the
embedded media SHA-256 equals the tested MP4 SHA-256. The generated deck SHA-256 is
`8a09390ae936bb5f007d8953d06f41e564e796c96aae6f04fec16998b392a5ed`.

LibreOffice 26.2.7.3, build `08dfbf04dcac895fc3a8d30dbf5a00de1b9dda5e`, opens the probe through
macOS LaunchServices with its own disposable profile. After a 15-second startup allowance,
CoreGraphics identifies the on-screen window `Presenting: groel_rotation_oxillustrate_mp4`,
owned by the launched LibreOffice PID 79673. Its bounds are 1920 x 1080. Native window captures
include shadows and measure 1966 x 1126.

Eight captures at 0.100, 1.132, 2.134, 3.124, 4.123, 5.125, 6.138 and 7.150 seconds after the
capture clock starts show visible orientation changes in the actual slideshow. The central RGB
protein crops contain five distinct images; later images repeat the approximately five-second
rotation, rather than staying on the poster. Visual inspection of the full first capture and
the eight-image contact sheet confirms the media is visible and rotating. The movie starts
without a click in this probe.

These sparse captures establish actual slideshow motion. They do not measure exact 25 fps
playback or establish exact wall-clock timing in Impress.

Impress evidence in `output/oxillustrate_playback/`:

- `groel_rotation_oxillustrate_mp4.odp`: editable probe with original embedded MP4.
- `input_manifest.json` and `deck_verification.json`: source and embedded-media hashes.
- `groel_rotation_oxillustrate_mp4_windows.json`: native window identity and ownership.
- `groel_rotation_oxillustrate_mp4_captures.json`: exact LaunchServices command and timed captures.
- `groel_rotation_oxillustrate_mp4_00.webp` through `_07.webp`: native window captures, quality 90.
- `impress_mp4_contact.webp` and `capture_comparison.json`: inspected contact sheet and RGB checks.

## Reproduction commands

The disposable scripts adapt the proven method in
[impress_verification.md](impress_verification.md). No new dependency or production helper is
added. Commands run from the repository root, in this order:

```bash
source source_me.sh && python3 output/oxillustrate_playback/decode_media.py
source source_me.sh && python3 output/oxillustrate_playback/build_deck.py
node output/oxillustrate_playback/browser_playback.mjs
source source_me.sh && python3 output/oxillustrate_playback/capture_playback.py \
  groel_rotation_oxillustrate_mp4.odp
source source_me.sh && python3 output/oxillustrate_playback/analyze_captures.py
```

The native window helper is copied unchanged from the previous verified probe. Its source is
retained as `output/oxillustrate_playback/list_windows.swift`; rebuild when needed with:

```bash
swiftc output/oxillustrate_playback/list_windows.swift \
  -o output/oxillustrate_playback/list_windows \
  -module-cache-path /Users/vosslab/.cache/protein_animation_swift
```

Environment observations: macOS 27.2.1 build 26B131, FFmpeg/ffprobe 9.0.2, Pillow 13.0.0 and
Node.js 26.13.0. These are tested versions, not dependency pins. Browser and Impress launches
use normal graphical-session access through approved execution. No automatic approval review
rejection occurs. The later sandboxed `ps` cleanup check is denied by the filesystem sandbox;
the same read-only check succeeds with normal-session access.

## Cleanup and limits

The browser closes, its localhost server closes, and the owned LibreOffice process exits with
status 0 after capture. A read-only process listing confirms PID 79673 and matching verification
browser/server processes are absent. Only the generated ODP lock and disposable profile are
removed after the owning process exits. No normal LibreOffice profile or user application is
terminated. Capture PNG intermediates are removed after quality-90 WebP conversion.

Only the new Rust GroEL delivery is tested. Other browsers, PowerPoint, Keynote, exact Impress
frame pacing, older examples and alternative media insertion routes are outside this check.
Animated WebP-in-Impress is not retested; the previously recorded blank-image limitation in
[impress_verification.md](impress_verification.md) remains. MP4 is the demonstrated presentation
delivery here; animated WebP is demonstrated in Chromium. No Blender, molecular rerender, full
suite or fresh-process rendering replay runs in this verification track.
