# Alpha and crop feasibility

## Recommendation

The existing WebP encoder already retains true alpha. Rerender native transparent PNGs, preserve
RGBA through the gallery crop/canvas, and explicitly flatten only opaque delivery formats onto
white. No new dependency, encoder framework, background-removal algorithm or transparency CLI
flag is needed. Existing white source pixels cannot establish original molecular coverage.

Manager decision D2 selects one fixed 4:3 GroEL canvas (640 x 480), one fixed 2:3 hexokinase canvas
(360 x 540), and an ATP synthase portrait canvas determined after full-shape and label review.
Retain one camera scale and one union crop throughout each clip. Include outlines and labels in
the bounds and add modest fixed padding. Never fit individual frames separately or stretch them.

## Decisive local probes

Run with the repository bootstrap:

```bash
source source_me.sh && python3 output/atp_synthase_feasibility/media/probe.py
source source_me.sh && python3 output/atp_synthase_feasibility/media/rgb_probe.py
```

Probe scripts and JSON observations remain under ignored `output/atp_synthase_feasibility/media/`.
Versions observed: FFmpeg 9.0.2, Pillow 13.0.0. These are observations, not dependency pins.

| Check | Observed result |
| --- | --- |
| Existing shared encoder, 125 moving RGBA frames | 125 WebP frames, infinite loop |
| WebP decoded alpha | Exactly matches all source frames; values 0, 128, 255 |
| WebP container | VP8X flags 18: alpha and animation flags both set |
| Moving object disposal | No stale alpha trails across any decoded frame |
| Existing shared encoder, 125 RGB frames | 125 decoded frames, RGB pixels exactly match |
| Gallery Pillow encoding at quality 90 | All 125 decoded alpha planes exactly match |
| Current MP4 handling of RGBA | Transparent corner becomes black |
| Explicit white overlay before MP4 | Corner becomes white; half-alpha blue blends with white |
| Current GIF encoding | Alpha becomes binary 0/255; half-alpha cannot survive |

The [WebP container specification](https://developers.google.com/speed/webp/docs/riff_container)
defines animation, alpha and per-frame blending/disposal. Read container flags and decode every
frame with Pillow; a file extension or a single transparent poster is insufficient evidence.
The retained moving-object test checks decoded alpha across vacated regions, including the wrap
in its repeated motion. This is decode evidence, not browser or Impress playback evidence.

The successful explicit MP4 composite uses an additional FFmpeg white color source at the input
dimensions and 25 fps, then `[1:v][0:v]overlay=shortest=1:format=auto,format=yuv420p`. The production
owner can obtain dimensions from the existing frame check. Keep the RGB branch's current command
unchanged; add compositing only when input has transparency. Both source modes were exercised,
but no proposed production branch was implemented or integration-tested here.

For GIF choose an explicit delivery policy: a white composite before the existing palette filter
preserves the visible soft edge; transparent GIF needs a reserved transparent palette entry and
an explicit alpha threshold and still loses partial alpha. The smallest consistent delivery is
opaque white GIF and MP4, true-alpha WebP and poster. Existing palettegen/paletteuse already
produces binary transparency, but that does not make GIF a full-alpha alternative.

## Native rerender paths

- Rust scene `background: null` emits real straight-alpha PNG/WebP. Current source documents this
  in `SceneSettings` and `RenderedImage`; no chromakey is required.
- A native one-frame probe with the existing release binary succeeds after removing `trim` from
  its probe-only scene. It emits RGBA 511 x 552 with alpha extrema 0/255 and six alpha levels.
- The same binary rejects the current animator scene's `trim: false` as an unknown field.
  Its successful probe auto-trims and cannot serve fixed-dimension production animation.
  The manager has assigned that upstream/runtime mismatch separately. No binary was rebuilt.
- Mol* screenshot settings already expose `transparent`; the current shared renderer sets it
  to false. Change the requested animation route to native `transparent: true`, retain the
  molecular surface's separate material opacity, and verify actual exported alpha. No Mol*
  render was launched by this investigation.
- Existing GroEL frames are RGB. Existing hexokinase frames are RGBA containers with alpha
  fixed at 255. Both require native rerendering for true background transparency.

## Fixed crop measurements

All 125 existing PNG frames were scanned against exact white for geometry estimates only.
These white-pixel comparisons must not be reused as scientific alpha reconstruction.

| Clip | Union bounds, right/bottom exclusive | Content size |
| --- | --- | --- |
| GroEL Rust | 31, 40, 607, 586 | 576 x 546 |
| Hexokinase Mol* | 200, 84, 487, 521 | 287 x 437 |

Illustrative safe fixed crops with about 12 native pixels of padding are GroEL
`(19, 28, 619, 598)` and hexokinase `(188, 72, 500, 534)`. Recompute after native alpha rerender:
alpha may retain coverage absent from an exact-white difference. GroEL's whole-loop footprint is
nearly square, so the agreed 4:3 canvas will retain some horizontal margin; it substantially
improves on the current 16:9 preview. Hexokinase's footprint closely suits 2:3. The existing
gallery helper deliberately avoids enlargement; preserve that behavior or increase native render
resolution deliberately, rather than silently upscale source pixels.

ATP bounds remain unmeasured because no accepted 125-frame ATP sequence exists yet. Measure the
full sequence after scientific preparation and camera selection; reserve label clearance when
choosing its single portrait aspect. An early single frame does not establish whole-loop bounds.

## Production change scope

- [encode_loop.py](../../../tools/encode_loop.py): preserve existing WebP command and poster;
  explicitly composite transparent sources for MP4 and the selected opaque GIF policy.
- [capture_readme_visuals.py](../../../devel/capture_readme_visuals.py): retain RGBA, check bounds
  against alpha, crop once per clip, paste onto a transparent canvas, and use D2 fixed aspects.
  Use `paste` without a mask for straight RGBA placement: a second alpha mask would square opacity.
  Add the ATP entry only when its renderer and output are accepted.
- [render_oxillustrate.py](../../../examples/groel_rotation/render_oxillustrate.py) and its scene:
  use native alpha and the fixed-canvas renderer once the separate trim issue is resolved.
- [render_molstar.mjs](../../../examples/render_molstar.mjs): enable native transparent export for
  requested clips, retaining scientific selection, motion and existing material transparency.
- [test_encode_loop.py](../../../tests/test_encode_loop.py): retain frame-integrity protection;
  add one focused alpha/composite check for the new branch. Gallery crop checks should reject
  clipping and exercise semitransparent pixels instead of copying implementation details.
- Refresh affected example/media docs, gallery assets and posters, recorded hashes and runtime
  observations, README aspect wording, changelog, settled decisions and human guidance.

The existing encoder callers are the root README, GroEL and hexokinase example READMEs, and
[MEDIA.md](../../tools/MEDIA.md) plus [OXILLUSTRATE.md](../../tools/OXILLUSTRATE.md). Keep their
current positional frame-directory interface; adding transparency flags would duplicate facts
already available in the image data. Gallery updates currently use one script and fixed entries;
adding one third entry does not require a configuration framework.

## Verification limits

Investigation only: product files and current animation outputs were not changed. No browser or
Impress playback, new ATP rendering, complete native rerender or fresh-process full reproduction
was checked. Native alpha coverage is demonstrated for one trimmed GroEL frame only; fixed-canvas
native playback still depends on the separately owned upstream trim correction.
