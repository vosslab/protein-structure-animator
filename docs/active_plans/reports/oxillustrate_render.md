# Native Goodsell rendering evidence

Observed 2026-11-12 on this Mac. Rust oxillustrate is the canonical Goodsell renderer for the
3N0G still and GroEL rotation. Existing Fortran/Mol* comparisons and hexokinase outputs remain.
This report separates image/render/replay checks from native scientific inspection and application
playback. See [oxillustrate_science.md](oxillustrate_science.md) for independent native identity
and geometry evidence; playback has its own report.

## Executed commands

Build the current sibling checkout with `cargo build --release` in
`/Users/vosslab/nsh/goodsell-oxillustrate-rs`. The build completed successfully in 10.75 seconds.
`illustrate --help` and `illustrate --version` succeeded. Its native command takes a positional
structure path; there is no `render` subcommand.

From the animator repository root:

```bash
bash examples/download_inputs.sh
source source_me.sh && python3 examples/appearance_3n0g/prepare.py
mkdir -p output/appearance_3n0g/oxillustrate
../goodsell-oxillustrate-rs/target/release/illustrate output/appearance_3n0g/selected.cif \
  --scene examples/appearance_3n0g/oxillustrate.json \
  --output output/appearance_3n0g/oxillustrate/still.png
source source_me.sh && python3 examples/groel_rotation/render_oxillustrate.py
source source_me.sh && python3 tools/encode_loop.py output/groel_rotation_oxillustrate/frames
```

Original inputs were already downloaded; their complete hashes were rechecked against
[input_hashes.sha256](../../../examples/input_hashes.sha256). Existing `prepare.py` was executed
again for the fresh-process replay. No structural source was rewritten. The new example script
accepts only `-i`/`--illustrate` to override the default sibling release-binary path.

## Renderer identity

- Executed version: `illustrate 26.11.0`.
- Sibling HEAD: `29d4e907efe6524eb78188edbdd4a500dc0e5260` **with uncommitted changes**.
- Binary SHA-256: `9a2441d4383340bd2e16ae1aa0cf447f98543187655d4e430d7d42c2df9e3d17`.
- Observed toolchain: rustc 1.99.1 and cargo 1.99.1, as observations rather than requirements.

Ignored `output/groel_rotation_oxillustrate/provenance/` retains `build.json` with complete source
hashes/status, `source.patch`, native `help.txt`, and copies of Cargo.toml, Cargo.lock, VERSION and
every native `src/` file. Source build-input hashes and executable hash were unchanged after the
full replay. The dirty HEAD alone cannot reconstruct this executable; the saved source snapshot
records the actual build inputs. No sibling production file was edited by this workstream.

## Native scenes and inputs

The retained scenes are
[appearance_3n0g/oxillustrate.json](../../../examples/appearance_3n0g/oxillustrate.json) and
[groel_rotation/oxillustrate.json](../../../examples/groel_rotation/oxillustrate.json).
They explicitly retain native settings: 640 by 640, opaque white, model 1, `assembly: null`,
`trim: false`, sphere radii, shadow parameters and outline thresholds. Current CLI source honors
`trim: false` directly; `--no-trim` is an equivalent override, not an additional requirement.
Native fog front/back are both 1: the renderer normalizes unequal endpoints using each image's
visible depth range, so equal endpoints avoid that source of brightness changes during rotation.
Native screen-space shadows and black outlines provide depth/shape cues.

3N0G uses prepared `selected.cif` directly, without a PDB conversion: chain A's 4,244 protein atoms,
14 DST atoms and 3 Mg ions. The input includes blank and A alternate conformers selected by the
existing preparation. Native rules color protein blue, DST magenta and Mg green. Author chain A
contains the whole selection; label chain A alone would exclude the ligand and ions. Native z
orientation is 90 degrees, retaining the existing ligand-facing view. There is no transparency,
cutaway or invented atom. Only exposed parts of the retained ligand/ions are visible.

GroEL reads `output/inputs/1oel_assembly1.cif` unchanged:
SHA-256 `fb61ff7da5bafbd92f95a85876616cf5b7d43f8219af4260c81db295aa4ca49d`.
The Python check observes 53,858 ATOM rows, fourteen author chains A-G and A-2 through G-2,
3,847 protein atoms per chain, and precisely 298 HOH rows outside the protein. There are no
alternate conformers. Native defaults omit these waters. Leaving assembly null prevents a
second biological expansion. Atom identities, native selection and projected geometry receive
independent verification in the scientific report; successful PNG creation alone proves none
of those scientific properties. Deposited variants and missing residues remain as documented in
the example READMEs.

## Fixed rotation and framing

Current native `scene_preparation.rs` applies positive-angle column rotations Z, then Y, then X:
`R = Rx Ry Rz`. It then uses `p = (R p_source - center + translation) * scale`, adding half the
canvas dimensions to the first two coordinates. The center is **subtracted**, correcting the
earlier plan's stale additive-center description. Native coordinate 0 is the vertical raster
axis; rotation about that axis gives the desired full-turn viewpoint sequence.

One origin is the selected protein coordinate bounding-box midpoint `[-43.845, 0, 0]` Angstrom.
One radius bounds the distance of every atom from that origin plus the maximum native radius,
1.8 Angstrom. Every frame uses scale `2.988486732139123` pixels/Angstrom and depth
`98.03907896971705` Angstrom. The center is `R(origin) + [0, 0, depth]`, mapping that same origin
to a fixed image point and safely negative depth across the entire turn. Native positive z is
clipped; the radius/depth margin protects whole spheres throughout rotation.

Frame i uses native orientation `[15 + 360*i/125, 25, 0]` degrees, i=0..124. The final-to-first
interval is one ordinary 2.88-degree step, with no duplicate endpoint. This is rigid viewpoint
rotation, not a conformational cycle, physical trajectory or evidence of kinetics. The native
CLI receives the original mmCIF on every invocation; the script does not write transformed
structures. Every effective scene is retained in `scenes/frame_000.json` through
`scenes/frame_124.json` next to its PNG. Scale, projection, shadow/outline parameters, dimensions
and palette stay fixed.

## Render and replay observations

The first complete clean render and its complete fresh-process replay both succeeded. The
replay used the final documented example script in a new Python process, which launched a new
native CLI process for every frame. The existing preparation and native still command were
also rerun, followed by all three existing encoder outputs. Every one of the 125 PNG hashes,
the 3N0G PNG, animated WebP, GIF, MP4 and poster matched the first complete run byte-for-byte on
this machine. This is local determinism evidence, not a requirement of cross-platform pixel
identity. The baseline manifest is retained in ignored `baseline_sha256.json`; `validation.json`
and `validate_render.py` record the checks. Two interrupted exploratory runs preceded the clean
run and are not counted as accepted renders.

- All 125 PNGs decode as 640 by 640 RGB with opaque white background.
- Combined nonwhite image bounds are `[31, 40, 607, 586]`, with no clipped image-edge contours.
- WebP and GIF decode all 125 frames at 40 ms each, five seconds total, infinite loop.
- FFprobe reports MP4 640 by 640, yuv420p, 25/1 fps, 125 frames, 5.000000 seconds.
- Fresh full render: 54.08 s wall, 50.41 s user, 3.33 s system; maximum resident set size
  340,590,592 bytes and peak memory footprint 112,771,720 bytes in macOS `time -l` output.
- Existing encoding command: 17.67 s wall. The still command completed in about 0.1 s.

The full-turn contact sheet (frames 0, 15, 31, 47, 62, 78, 94, 109 and 124), selected full-size
frames, poster and final quality-90 WebP previews were viewed. The complete assembly remains
legible and centered, with warm chain colors, black boundaries and useful shape shading. No
edge clipping or apparent scale pumping was observed. The 3N0G preview shows the magenta DST
and exposed green Mg surfaces against blue protein; retaining all three ions does not imply
all three are individually visible. Image/contact-sheet inspection is separate from animated
browser and Impress playback, assigned to the independent playback workstream.

Output sizes and SHA-256 hashes:

| File | Bytes | SHA-256 |
| --- | --- | --- |
| animation.webp | 22986818 | f8e3745e3505d50a08d69037119d25ede9b553e985363cfa202097c12d553396 |
| animation.gif | 14900690 | 39e35cc791964b122db68583a3d8f67d1a9500b54ead905186258ccae4e5118a |
| animation.mp4 | 3722780 | f68e03790b383e45545a0f86ab9be2ae1fe375900377323c286ca75518d58020 |
| poster.webp | 170816 | See retained baseline manifest |

Frame 000 SHA-256: `0ece252c5d76e76695d54aea56a17399a4a15726a14c64d449f6c5e9ab1abf83`.
3N0G PNG SHA-256: `e639eb2803a2b28146c5923393c2619f8864504019b3da47eaf92c3674851a4a`.

## Focused checks and limits

[test_oxillustrate_rotation.py](../../../tests/test_oxillustrate_rotation.py) protects the
fixed-origin invariant, distance preservation, full-turn screen/depth bounds and native rotation
axis convention with an asymmetric translated synthetic molecule. Failure requires correcting
the rotation/framing math before rendering; weakening the bounds would conceal clipping.
Pyflakes, function typing, indentation, imports and shebang checks were run with this test.
Mypy was not installed in the configured Python runtime, so no mypy result is claimed.

No new dependency, adapter, bindings, recipe schema or generalized rendering framework was added.
No Blender process was launched. Browser/Impress playback and independent scientific acceptance
are recorded by their owners, not inferred from decoding or local replay here.
