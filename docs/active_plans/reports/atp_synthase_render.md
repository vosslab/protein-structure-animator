# ATP synthase native rendering

## Scope and interpretation

The new example stages the complete 8DBU gamma/epsilon/c10 rotor against a fixed stationary
housing. It uses canonical native Rust Goodsell protein pixels and preserves every deposited
atom in each full-coordinate handoff. The deliberately fixed stator wedge exposes the shaft;
the pale membrane band supplies schematic hydrophobic context, not a measured membrane boundary.
The movement is rigid mechanical staging from one experimental structure. Frozen catalytic-head
coordinates overlap the rotor at some angles; this is not a sterically validated trajectory,
catalytic cycle, reaction pathway, binding sequence, or measured kinetics.

## Sources and preparation

Original inputs are preserved in `output/inputs/8dbu.cif` and `8dbu_assembly1.cif`. Download
commands and exact SHA256 values are appended to
[download_inputs.sh](../../../examples/download_inputs.sh) and
[input_hashes.sha256](../../../examples/input_hashes.sha256). The expanded biological assembly
has the same 36,917 atom identities and coordinates as the deposition, and is not expanded again.
Primary record and construct caveats are documented in the example
[README.md](../../../examples/atp_synthase_motor/README.md).

Preparation command:

```bash
source source_me.sh && python3 examples/atp_synthase_motor/render_oxillustrate.py --prepare
```

This retains 125 complete moving mmCIF files plus 125 fixed-mask camera-coordinate mmCIF files,
all atom-site identity fields, 125 effective native scenes, `identity_mask.json` and
`preparation.json` under ignored `output/atp_synthase_motor/`. It omits no atom from the complete
frames. Label chains G-R form the 8,772-atom rotor. The remaining 28,145 atoms stay stationary.
Native full input has 22 polymer chains and 183 heteroatoms; missing residues/atoms stay missing.

The fixed wedge omits 7,643 stationary atoms and displays 29,274 atoms. All 8,772 rotor atoms
remain visible candidates. For this exact hashed input, the wedge intersects no ligand partially.
Retain complete ATP W/Y/DA (31 each), Mg X/Z/CA (one each), ADP GA (27): 123 heteroatoms.
Omit complete ATP AA (31), Mg BA (one), ADP EA (27), Mg FA (one): 60 heteroatoms. These IDs are
label-chain namespaces, distinct from author chains. Full frames retain all 183 heteroatoms.

## Corrected camera checkpoint

The first exploratory stills used a reflected camera basis (determinant -1). They were rejected
because a reflection reverses molecular handedness. The corrected mapping is
`row = -z*cos(8deg) + y*sin(8deg)`, `column = -x`,
`depth = y*cos(8deg) + z*sin(8deg)`, with determinant +1. The source axis basis, original
rotation origin, positive right-handed rotor motion, fixed cutaway and all source identities
remain unchanged. The corrected side stalk appears on the left.

Canonical preparation was rerun completely after the correction, replacing all 250 coordinate
handoffs, 125 effective scenes and metadata. Its measured file interval is 136.45 seconds,
from the newly created log birth time to the completed preparation metadata mtime; this includes
process startup and is not a process-profiler measurement. The timing record remains in
`output/atp_synthase_motor/preparation_timing.json`.

The corrected checkpoint command was:

```bash
source source_me.sh && python3 examples/atp_synthase_motor/render_oxillustrate.py --frames 0 15 31
```

It completed in 0.90 seconds as measured inside the helper. The quality-90 `three_stills.webp`
shows the corrected frames over white and dark backgrounds. The manager inspected and accepted
the proper view, exposed shaft, cutaway and label legibility before authorizing the full render.
The existing membrane, labels and caption remain legible with the side stalk on the left.
All checkpoint frames have the same 480 x 720 RGBA canvas, composed alpha bounds
`[19, 27, 461, 713]`, 168,979..171,355 fully transparent pixels and
36,204..36,348 partly transparent pixels.

Native automatic trimming remains enabled. JSON sidecars report the original canvas and exact
crop origin. The helper pastes straight RGBA pixels unscaled onto the fixed canvas, then adds
membrane context and sparse labels using Pillow. It does not key a matte, add fake registration
atoms, or replace native protein shading. Fixed light and equal fog endpoints avoid
frame-dependent lighting normalization.

## Focused verification

Two focused offline geometry tests pass: rigid rotor internal distances and axial positions,
fixed housing, a proper source axis basis, no duplicate 360-degree endpoint, camera distance
preservation, complete rotor retention under the cutaway, and the determinant +1 camera basis.
The determinant regression distinguishes a true rotation from a distance-preserving reflection.
The test lives in the normal `tests/` collection. Pyflakes passes the example source and test.

```bash
source source_me.sh && python3 -m pytest tests/test_atp_synthase_geometry.py -q
source source_me.sh && python3 -m pyflakes examples/atp_synthase_motor/ tests/test_atp_synthase_geometry.py
```

## Full native delivery

After checkpoint acceptance, run sequentially:

```bash
source source_me.sh && python3 examples/atp_synthase_motor/render_oxillustrate.py
source source_me.sh && python3 tools/encode_loop.py output/atp_synthase_motor/frames
source source_me.sh && python3 output/atp_synthase_motor/check_delivery.py
```

The full native render completed all 125 frames in 36.783 seconds, measured inside the helper.
Encoding MP4, animated WebP, GIF and the transparent poster took 14.322 seconds, measured around
the real encoder subprocess. The final `render.json` contains every index 0..124. All 125 native
trimmed PNGs and metadata sidecars, reconstructed protein-only PNGs and composed RGBA PNGs are
present. The failed interrupted one-time camera-refresh script was removed; canonical preparation
is the documented path.

All source canvases remain 480 x 720. Every native crop origin is `[61,46]`; the all-frame protein
alpha union is `[64,49,414,669]`. The composition union, including membrane, labels and caption,
is `[19,27,461,713]` for every frame. No alpha touches a canvas edge. There are
168,547..172,718 fully transparent pixels and 36,068..36,375 partly transparent pixels per frame.
This provides one fixed union and padding without individual-frame rescaling or recentering.

The one-time delivery check decodes every animated WebP frame and confirms exact alpha and exact
RGB wherever alpha is nonzero, plus byte-identical white and dark composites against each source
PNG. Every frame lasts 40 ms, the file loops continuously, and the poster preserves exact alpha
and visible RGB. Lossless WebP may rewrite invisible RGB beneath alpha zero: 45,555..50,301 pixels
per animated frame. Consequently the claim is exact visible RGBA and compositing, not raw RGBA
byte identity at fully transparent pixels. The poster has the same invisible-RGB caveat.

All 125 GIF frames are opaque with white backgrounds and 40 ms timing. FFprobe decodes 125 MP4
frames, 480 x 720, 25/1 fps, duration 5.000000 seconds and yuv420p. The MP4 is explicitly composited
onto white before encoding; its corner is white throughout. These decode checks are separate from
actual application playback.

Quality-90 proof sheets are `all_frames.webp` (all 125 frames), `seam.webp` (122,123,124,0,1,2
over white/dark) and `teaching_size.webp` (0,31,62,93 at 320-pixel width over white/dark). This
worker inspected all three: fixed housing, steady scale, an exposed moving amber shaft, complete
ring within frame, and readable labels at teaching size. The original 480 x 720 presentation is
retained. Seam mean absolute RGBA difference after white compositing is 1.865 byte values, within
the ordinary adjacent-frame range 1.740..2.075; 123-to-124 is 1.805 and 0-to-1 is 1.775. This
supports a visually continuous seam, while browser motion is verified separately.

`delivery_checks.json` and `seam_checks.json` retain measured results. Observed output storage at
this checkpoint is 1,050,377,751 bytes, including all 250 handoffs, native source snapshots, frames,
media and proof sheets; the native PNG set alone is 20,604,774 bytes. No peak-memory measurement
was made. Observed versions are Python 3.12.16, Pillow 13.0.0, NumPy 2.5.4, Biopython 1.88 and
FFmpeg 9.0.2, reported as observations rather than pins.

## Build and artifact identity

The invoked external renderer is `illustrate 26.11.0`, native checkout HEAD
`6e7736a746efcde1ed65cea965aae86cbc8dfcee`, executable SHA256
`ac4c51ab1f3e27e16b7ce888f4c8eb462b263249b310bf6f6d840b30934ba91f`.
`provenance/build.json` records every native source/Cargo hash, the helper and template hashes;
`provenance/native_source/` preserves those files and `provenance/native.diff` retains the dirty
patch. The binary is checked unchanged before/after rendering. Protein pixels use this canonical
native build; no Blender process was launched.

Final artifacts under `output/atp_synthase_motor/`:

| Artifact | Bytes | SHA256 |
| --- | --- | --- |
| `animation.webp` | 7,729,844 | `eb530fc3b42bd1935bccaa42a3a157a7712c498131d91e6591e7bed0ff0de718` |
| `animation.mp4` | 1,105,430 | `5f93cff23e9c8974e7c7bb86d691caf49ac28cfd6bb331f1dc0cf9616a1a7caf` |
| `animation.gif` | 2,785,531 | `9bcc25931d66c3367e10d7ceb35a5bdd63c1d803f47b3a5afba0af3c622e40f9` |
| `poster.webp` | 114,330 | `e8dec10c00a442e8b7d9deafd2fb40018a2b326ae3bd69d9a320e1d3828be31c` |

Pyflakes passes. Bandit at medium severity/confidence reports no qualifying findings (11 low
severity subprocess/path observations, none suppressed). Two geometry tests pass in 0.17 seconds.
The final Markdown-link and geometry command reports 93 passed in 0.24 seconds; the five
owned source/document files pass ASCII and whitespace checks. No broader suite result is
inferred from these focused checks.

Independent scientific coordinate/native-handoff checks, browser/application playback and a second
fresh-process replay remain separate evidence owned by their corresponding workstreams. The
scientific staging caveats above remain even when rendering and decode checks pass. No commit or
publication was performed.
