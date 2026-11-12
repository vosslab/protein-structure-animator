# Canonical Goodsell rendering

Use the native CLI from sibling `goodsell-oxillustrate-rs` as the canonical renderer and visual
gold standard for Goodsell figures and animations. Its native output is static atom-sphere PNG
or lossless WebP. This repository scripts native scenes for GroEL rotation and an authored ATP motor;
the renderer itself does not implement an animation timeline or molecular surfaces.

The initial integration covers the 3N0G still and complete GroEL rotation. The ATP synthase motor
example adds authored mechanical staging with a fixed camera, stator cutaway and schematic membrane.
Native rendering and coordinate-handoff reports are recorded; see the accepted
[atp_synthase_alpha.md](../archive/atp_synthase_alpha.md) for its acceptance status.
Mol* remains the route for smooth surfaces and interactive views: see [MOLSTAR.md](MOLSTAR.md).
Hexokinase preparation and interpolation remain unchanged; its native alpha delivery is separate.

## Build current source

From this repository root, with a current Rust toolchain and sibling checkout present:

```bash
cargo build --release --manifest-path ../goodsell-oxillustrate-rs/Cargo.toml
source source_me.sh && python3 -m pip install --upgrade -r pip_requirements.txt
bash examples/download_inputs.sh
```

The default external binary is `../goodsell-oxillustrate-rs/target/release/illustrate`.
The GroEL helper accepts `--illustrate PATH` for another built binary. Do not add a fixed revision
requirement: retain tested revision/version, dirty-source provenance and binary hashes as
observations. No Node.js, browser, Fortran compiler or Blender is needed for this route.

## Render the examples

From the repository root after building and downloading:

```bash
source source_me.sh && python3 examples/appearance_3n0g/prepare.py
mkdir -p output/appearance_3n0g/oxillustrate
../goodsell-oxillustrate-rs/target/release/illustrate output/appearance_3n0g/selected.cif \
  --scene examples/appearance_3n0g/oxillustrate.json \
  --output output/appearance_3n0g/oxillustrate/still.png
source source_me.sh && python3 examples/groel_rotation/render_oxillustrate.py
source source_me.sh && python3 tools/encode_loop.py output/groel_rotation_oxillustrate/frames
```

For new transparent GroEL source frames, use
`source source_me.sh && python3 examples/groel_rotation/render_oxillustrate.py --alpha`.
These go to `output/groel_rotation_alpha/`, preserving the existing opaque deliveries. The default
route remains opaque. Rebuild the current sibling source before using the updated helper: it
requires the crop-origin metadata interface.

The verification run preserved build provenance under
`output/groel_rotation_oxillustrate/provenance/`: `build.json`, the source diff and a copy of native
build inputs. The helper records executable, input and settings hashes in its metadata; it does
not create the source snapshot. Retain that snapshot and binary hash alongside HEAD for a dirty
source checkout.

The GroEL helper retains `frames/frame_000.png` through `frame_124.png`, corresponding native
`scenes/frame_000.json` through `frame_124.json`, `illustrate.log` and `render.json`. The encoder
adds MP4, GIF, animated WebP and a poster in the same parent directory.

## Native scene contract

The CLI takes positional local input, `--scene` JSON and `--output` PNG/WebP. Native input support
includes mmCIF, PDB and PDBML; model and assembly selection are explicit native capabilities.
Scene rules control selection/coloring, orientation and framing. Current native output always
trims; `trim:false` is obsolete and rejected. Optional `--metadata PATH` writes
`{"canvas":[width,height],"crop_origin":[left,top]}`. The native `render_with_bounds` API preserves
the same image and crop origin; the existing `render` API keeps its image-only contract. Reinsert
each cropped RGBA image at that origin on the declared common canvas without an extra alpha mask.
Keep one rotation origin, scale and depth-safe framing across frames; never independently center
trimmed images. Current source subtracts `framing.center`; use current implementation
rather than stale additive descriptions when translating a world-space rotation origin.

The 3N0G/GroEL scenes use model 1, no assembly expansion, opaque white and a declared 640 x 640
canvas. Direct 3N0G CLI output is trimmed, so its PNG dimensions can differ. GroEL's
helper reconstructs that canvas from metadata; `--alpha` requests native transparent background.
`background:null` or an omitted background yields straight alpha; explicit RGB yields opaque
output. Do not derive transparency by removing white molecular pixels.
The GroEL framing uses a fixed rotated origin plus positive depth. Native depth-fog normalization
varies per frame; equal front/back lightness of 1 disables that fog while retaining native shadows.
[Scientific verification](../active_plans/reports/oxillustrate_science.md) independently confirms
native identities, coordinate fidelity and all-frame geometry. Visual and playback evidence are
separate.

The 1OEL input already contains the complete fourteen-chain assembly; do not expand it twice.
Keep original structural inputs unchanged and retain their hashes. Per-frame native JSON scenes
are editable replay sources, distinct from Mol* `.molj` plugin state.

Historical commands and measured render/replay evidence are recorded in
[oxillustrate_render.md](../active_plans/reports/oxillustrate_render.md). The observed version was
`illustrate 26.11.0`, built from a dirty current checkout whose build inputs and binary were
preserved. The full GroEL replay took 54.08 seconds, with 340,590,592 bytes maximum RSS; encoding
took 17.67 seconds. All 125 PNGs, encoded media, poster and still reproduced byte-for-byte on
this Mac. That historical build supported disabled trimming; its receipt does not establish
current-source replay or acceptance of the new alpha/metadata route. This is an observed local
result, not a cross-platform pixel-identity requirement.

Example selections, commands and settings are recorded in the
[GroEL example](../../examples/groel_rotation/README.md),
[3N0G example](../../examples/appearance_3n0g/README.md) and
[integration ledger](../active_plans/workstreams/oxillustrate_integration.md).
Rendering, scientific fidelity, playback and fresh-process reproduction remain separate checks;
completed historical Mol* checks do not establish new Rust output acceptance. The historical Rust
integration passed actual Chromium WebP/GIF/MP4 motion and natural MP4 loop checks, plus actual
LibreOffice 26.2.7.3 MP4 slideshow motion. Exact Impress pacing and animated WebP in Impress were not measured
for this integration. Fresh specification, quality and integration review remain separate.

The [ATP example](../../examples/atp_synthase_motor/README.md) retains full and display-cutaway
mmCIF handoffs, native protein pixels and labels/membrane context on one 480 x 720 RGBA canvas.
Its camera determinant is +1, preserving molecular handedness. A reflected camera can preserve
distances while mirroring molecules. See
[atp_synthase_render.md](../active_plans/reports/atp_synthase_render.md) and
[atp_synthase_science_verification.md](../active_plans/reports/atp_synthase_science_verification.md).

Current [atp_synthase_replay.md](../active_plans/reports/atp_synthase_replay.md) separately records
local fresh-process reproduction of the ATP delivery and both native-alpha source sequences from
preserved inputs. Scientific handoffs, frames, ATP media and gallery reproduce exactly; elapsed
metadata, appended logs, generated Mol* state and independent diagnostics have explicit limits.
This is not clean-install or cross-platform pixel-identity evidence.

## Licenses and attribution

The sibling implementation's source is AGPL-3.0-only; its documentation is CC-BY-4.0. It is built
and invoked externally, not bundled or relicensed under this repository's LGPL source license.
Retain the renderer's own license and attribution when distributing it. The method follows
Goodsell, Autin and Olson (2019), *Illustrate: Software for Biomolecular Illustration*.
[ILLUSTRATE.md](ILLUSTRATE.md) preserves the historical Fortran reference and its separate terms.
