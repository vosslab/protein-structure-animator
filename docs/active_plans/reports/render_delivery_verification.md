# Render and browser verification

Observed on 2026-11-11. M1 appearance, final animation rendering, delivery decoding, fresh command
replay, native scene restoration and browser playback pass the checks below. These are separate
from scientific interpretation in [structural_verification.md](structural_verification.md) and
application slideshow evidence in [impress_verification.md](impress_verification.md).

## Appearance and framing

Illustrate and Mol* use blue protein, magenta DST, green magnesium and white backgrounds for 3N0G.
The corrected Illustrate wildcard retains the ligand and ions, and `zrot 90` matches the Mol* view.
The stills show green Mg next to magenta DST in the pocket. Illustrate has stronger black atom
contours; Mol* has softer sphere contours and useful depth shading. The separate Mol* molecular
surface smooths the atom silhouette and conceals more pocket detail. Both representations are
actually rendered; the surface result is not inferred from an API option.

The eight-view Mol* rotation retains the full structure, fixed orthographic projection and scale.
The ligand becomes hidden from some viewpoints, as expected for opaque geometry. Illustrate is
verified as a still renderer here; no Illustrate animation capability is claimed.

Retained 640 x 640 previews, encoded at WebP quality 90:

| Preview | Bytes |
| --- | ---: |
| [illustrate.webp](../../../examples/appearance_3n0g/illustrate.webp) | 33,952 |
| [molstar_spacefill.webp](../../../examples/appearance_3n0g/molstar_spacefill.webp) | 28,088 |
| [molstar_surface.webp](../../../examples/appearance_3n0g/molstar_surface.webp) | 19,530 |
| [preview.webp](../../../examples/hexokinase_closure/preview.webp) | 14,332 |
| [preview.webp](../../../examples/groel_rotation/preview.webp) | 44,526 |

Hexokinase uses a smooth molecular surface at alpha 0.42 and separately rendered fixed glucose.
The translucent surface makes glucose visible during closure, with its color attenuated near the
closed state. Transparent surface outlines are deliberately excluded, so contours are softer than
those of the opaque surface comparison. This is an interpolated conformational illustration;
transparency is a presentation choice, not a physical molecular property.

GroEL uses atom spheres colored by chain. The alternating ring and side views, central cavity and
chain colors make the full turn readable despite symmetry. The imported model contains 54,156
atoms; the rendered polymer component contains 53,858 atoms in fourteen protein chains. It is a
camera rotation of one structure, not a conformational animation.

I inspected the final 3N0G eight-view sheet; hexokinase and GroEL frames 0, 1, 31, 62, 93, 124; and
26 sampled stills spanning each complete loop. No structure touches a frame edge. The hexokinase
reversal and GroEL wrap retain framing, with no visible reset or change in apparent scale. Raw
adjacent-frame mean absolute RGB differences provide supporting seam evidence, not a quality gate:
hexokinase seam 0.211 versus median 0.414; GroEL seam 8.526 versus median 8.410, on the 0-255 scale.
The 125 coordinate samples and their scientific interpretation are checked separately.

## Final delivery files

All deliverables live under `output/<example>/` as `animation.mp4`, `animation.webp`,
`animation.gif` and `poster.webp`. The two animation examples each have 125 PNG source frames.
Pillow decoded every GIF/WebP frame and verified 640 x 640, 125 frames, 40 ms per frame, 5,000 ms
in total and loop value 0. FFprobe counted 125 H.264 frames, 25 fps, yuv420p, 640 x 640 and 5.000 s.
FFmpeg decoded each entire MP4 to the null sink without an error. Posters use source frame 0.

| Example | MP4 bytes | WebP bytes | GIF bytes | Poster bytes |
| --- | ---: | ---: | ---: | ---: |
| Hexokinase closure | 462,436 | 9,488,314 | 7,469,156 | 72,740 |
| GroEL rotation | 2,871,591 | 24,277,100 | 10,860,158 | 142,028 |

MP4 is substantially smaller here. The lossless animated WebP retains the PNG appearance but is
large; neither its size nor GIF's palette size is treated as an arbitrary acceptance threshold.

## Fresh command replay

Each command below launched a fresh Chromium process after the final source correction. The
checked coordinates were stable before rendering. No interactive adjustment was used.

```bash
node examples/render_molstar.mjs appearance_3n0g
node examples/render_molstar.mjs groel_rotation
node examples/render_molstar.mjs hexokinase_closure
source source_me.sh && python3 tools/encode_loop.py output/hexokinase_closure/frames
source source_me.sh && python3 tools/encode_loop.py output/groel_rotation/frames
```

| Example | Render seconds | Frames | Encoding seconds |
| --- | ---: | ---: | ---: |
| 3N0G comparison | 5.816 | 8 plus surface still | Not applicable |
| GroEL rotation | 36.870 | 125 | 19.397 |
| Hexokinase closure | 83.005 | 125 | 14.517 |

Times include process setup and file writes for this machine. Peak resource use was not measured.
Illustrate was also rerun from its retained native input and produced a 640 x 640 still. Its
elapsed time was not instrumented.

## Native scene restoration

A separate temporary checker launched a new browser for each final `scene.molj`, created an empty
Mol* viewer and called `plugin.state.setSnapshot(savedSnapshot)`. It did not rerun structure
preparation or reconstruct the scene from example settings. The restored hexokinase scene contains
3,651 protein atoms plus twelve glucose atoms, with surface alpha 0.42 and glucose spacefill. The
GroEL scene restores all 54,156 model atoms and the polymer spacefill representation.

Both retain orthographic mode, field of view, position, target and up vector. Native Mol* restore
recomputes radius/radiusMax from 51.5301 to 46.7776 for hexokinase and from 112.8502 to 104.8175 for
GroEL. Inspection of the installed camera implementation shows that orthographic zoom depends on
field of view and camera-target distance; radius controls clip/fog bounds. The restored stills
have exactly the same measured foreground bounds as frame 0 and show the full intended geometry.
Raw PNG mean absolute RGB differences were 0.00783 and 0.00331 respectively. This supports native
editability and preserved framing; it is not a claim of byte-identical state restoration.

## Actual browser playback

A temporary local gallery served both examples' three formats over loopback HTTP. Chromium
158.0.8127.18 and Firefox 159.0 each decoded and played both MP4s. Native video dimensions are
640 x 640 and duration is 5 s. `paused` stays false, `currentTime` and decoded-frame counts advance,
and seeking near the end results in a native loop wrap while playback remains active.

| Browser | Example | MP4 time progression | Decoded frames |
| --- | --- | --- | --- |
| Chromium | Hexokinase | 0.517 to 1.803 s | 17 to 49 |
| Chromium | GroEL | 0.516 to 1.808 s | 18 to 50 |
| Firefox | Hexokinase | 0.560 to 1.800 s | 14 to 45 |
| Firefox | GroEL | 0.520 to 1.764 s | 13 to 44 |

For WebP and GIF, browser screenshots were captured about 1.2 s apart and compared within each
image rectangle. All four example/browser combinations change in both animated image formats:
WebP differences cover 83,485-138,033 pixels; GIF differences cover 81,371-137,639 pixels. The
captured gallery images show the intended molecular geometry. This verifies actual animated image
playback, beyond a successful image load. These are headless browser observations on this Mac;
other browsers, operating systems, LMS embedding and slideshow behavior are separate checks.

## Corrections and evidence

The first native screenshot assignment wrote the getter-only `viewportScreenshot.values`
property, so images were 638 x 638 even though `render.json` claimed 640. An actual pixel assertion
caught the mismatch before final encoding. The corrected native `behaviors.values.next(...)`
assignment is independently reviewed in
[screenshot_dimensions_fix.md](screenshot_dimensions_fix.md). All final images and formats above
were measured again after corrected fresh replays. Earlier dimensions claims are rejected.

The imported coordinate record now also retains native atom keys as
`[auth chain, residue number, insertion code, residue name, atom name]`, fixed glucose keys and
coordinates, and five sampled protein coordinate arrays. This lets the independent scientific
check test identity rather than relying on atom counts alone.

Raw local evidence is retained in `output/render_delivery/`: `media_checks.json`,
`browser_playback.json`, `browser_image_changes.json`, `native_restoration.json`,
`restored_image_comparison.json`, replay logs, quality-90 WebP screenshots and contact sheets.
Temporary verification runners use `_temp_` names. These diagnostics are not a new viewer or
permanent test framework. Final source checks pass through the canonical root configuration:

```bash
npx eslint --max-warnings 0 examples/render_molstar.mjs eslint.config.local.js
npx prettier --check --ignore-path .gitignore --ignore-path .prettierignore \
  --ignore-path .prettierignore.local examples/render_molstar.mjs eslint.config.local.js
node --check examples/render_molstar.mjs
```

Observed tools: macOS 27.2.1 arm64; Node 26.13.0; Mol* 5.13.1; Playwright 1.65.0; FFmpeg 9.0.2;
Python 3.12.16; Pillow 13.0.0; NumPy 2.5.4. Chromium needs an unrestricted graphics process on this
managed Mac: sandboxed launch fails at `bootstrap_check_in` with permission denied. The successful
runs used the same installed browser outside that sandbox; no rendering fallback was added.
