# Impress slideshow verification

Status: actual LibreOffice Impress slideshow playback verified for both teaching animations as
GIF and MP4. The embedded animated WebP probes present blank image areas.

## Observed results

All six ODP probes open in actual slideshow windows titled `Presenting: <probe_name>`, owned by
the launched LibreOffice process. Their CoreGraphics bounds are 1920 x 1080; window captures
include shadows and measure 1966 x 1126. No browser or document-export screenshot substitutes for
this evidence. Final source media are 640 x 640 and match source hashes retained in
`output/impress_verification/input_manifest.json`.

| Probe | Document opens | Visible media | Actual slideshow playback | Capture span |
| --- | --- | --- | --- | --- |
| Hexokinase GIF | YES | YES | YES: closure/reopening changes | 0.073-7.278 s |
| GroEL GIF | YES | YES | YES: orientation changes | 0.072-7.341 s |
| Hexokinase MP4 | YES | YES | YES: closure/reopening changes | 0.439-7.577 s |
| GroEL MP4 | YES | YES | YES: orientation changes | 0.087-7.412 s |
| Hexokinase animated WebP | YES | NO: blank image area | NO visible playback | 0.069-7.152 s |
| GroEL animated WebP | YES | NO: blank image area | NO visible playback | 0.068-7.089 s |

Each probe has eight native window captures, a `*_windows.json` ownership record and a
`*_captures.json` record with exact commands and monotonic capture times. GIF and MP4 each have
eight distinct RGB protein-area crops; each blank WebP probe has one unchanged RGB crop across
all eight captures. The comparison converts captures to RGB before comparing pixels; alpha-only
difference bounds would incorrectly miss color changes. Results are retained in
`output/impress_verification/capture_comparison.json`.

The retained quality-90 WebP contact sheets were visually inspected:

- `output/impress_verification/hexokinase_closure_gif_contact.webp`
- `output/impress_verification/groel_rotation_gif_contact.webp`
- `output/impress_verification/mp4_contact.webp`
- `output/impress_verification/webp_contact.webp`

GIF and MP4 are demonstrated teaching-slide choices on this installation. MP4 starts without a
click in these probes, with the native media object's `Loop` parameter enabled. Source timing
and frame counts are decoder checks owned by the renderer workstream. These approximately
one-second slideshow samples verify actual motion; they do not measure precise 25 fps playback
or guarantee a five-second wall-clock cycle in Impress. GIF pacing appears slower than MP4 in
the inspected samples, so do not infer playback timing from encoded delays alone.

The WebP result is specific to embedding the original animated file as an ODP image shape. The
ODP container opens; that does not establish successful WebP image decoding. No claim is made
about other insertion routes, static WebP, other LibreOffice releases, or other operating systems.

## Environment and method

- Application: LibreOffice 26.2.7.3, build `08dfbf04dcac895fc3a8d30dbf5a00de1b9dda5e`.
- Operating system: macOS 27.2.1, build `26B131`.
- Source deliveries: `output/hexokinase_closure/animation.{gif,webp,mp4}` and
  `output/groel_rotation/animation.{gif,webp,mp4}`.
- Probe artifacts: `output/impress_verification/`, intentionally ignored generated output.
- Each probe is an editable, one-slide ODP with the original media embedded. GIF and WebP use
  image shapes; MP4 uses the native LibreOffice media plugin, with looping enabled.
- Each launch uses a separate temporary profile beneath the probe output directory. The runner
  terminates only the process it launches; it does not use the user's normal profile.
- The native CoreGraphics helper lists only windows owned by the launched process. The runner
  captures the largest on-screen window eight times, sleeping 0.8 seconds between captures.
  Capture and encoding overhead makes actual intervals approximately one second.
- Successful package creation, import, static display, and changing slideshow frames are separate
  evidence classes. Only observed changes to the protein in slideshow captures count as playback.

The generator parses all package XML after writing and records the exact source hashes in
`output/impress_verification/input_manifest.json`. This is a package check, not application evidence.

## Commands

The probes ran sequentially after final encoding and an exclusive graphics-slot grant:

```bash
source source_me.sh && python3 output/impress_verification/build_decks.py
swiftc output/impress_verification/list_windows.swift \
  -o output/impress_verification/list_windows \
  -module-cache-path /Users/vosslab/.cache/protein_animation_swift
source source_me.sh && python3 output/impress_verification/capture_playback.py hexokinase_closure_gif.odp
```

Repeat the last command for `groel_rotation_gif.odp`, the two `_webp.odp` probes, and the two
`_mp4.odp` probes. Exact launch commands and capture times are retained in each `*_captures.json`.

## Known automation limits

The sandboxed read-only AppleScript application lookup fails with a
`com.apple.hiservices-xpcservice` connection-invalid error and AppleScript error -1728. The
slideshow method therefore uses macOS LaunchServices and PID-scoped CoreGraphics capture.
Normal graphical-session access and window capture were authorized and succeeded; no approval
review rejection occurred.

The initial direct-executable probe checked for windows after only five seconds and found none.
Its log included `Task policy set failed: 4 ((os/kern) invalid argument)`. It was stopped, leaving
a lock on its disposable ODP. A subsequent LaunchServices launch displayed a `Document in Use`
dialog for that probe. After confirming its owning process had exited, only that generated probe
lock was removed. LaunchServices with a 15-second startup wait then succeeded for all six probes.
The initial result does not establish that direct executable launch is unsupported; the experiment
changed both launch method and startup allowance.

The runner stops only each owned process after capture. Since SIGTERM leaves its generated ODP
lock behind, the finished runner removes that one disposable lock after the process exits. All
six locks from this verification were removed only after confirming no soffice process remained.
The user's normal profile and documents were not modified.

PythonUNO attempts preceding this work failed in the application's Python runtimes (exit 137) and
with a system-Python path experiment (segmentation fault). They are not repeated. ODP package
creation uses the Python standard library and does not depend on UNO.

## Result boundary

The Impress playback acceptance item is demonstrated for both final teaching examples through
GIF and MP4. Browser, decoder, scientific interpretation and fresh-process reproduction remain
separate evidence classes. Exact slideshow frame pacing and alternative WebP insertion routes
were not tested. This report does not declare the overall toolbox plan complete.
