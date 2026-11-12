# GroEL rotation

A full-turn view of the complete fourteen-subunit GroEL assembly. Only the viewpoint changes;
this does not show a conformational cycle, ATP hydrolysis, folding dynamics or measured kinetics.

Canonical Goodsell preview: [oxillustrate_preview.webp](oxillustrate_preview.webp).
The earlier Mol* comparison remains in [preview.webp](preview.webp).

## Reproduce

Build the sibling native Rust renderer as described in
[OXILLUSTRATE.md](../../docs/tools/OXILLUSTRATE.md), then run from this repository root:

```bash
bash -c 'cd ../goodsell-oxillustrate-rs && cargo build --release'
bash examples/download_inputs.sh
source source_me.sh && python3 examples/groel_rotation/render_oxillustrate.py
source source_me.sh && python3 tools/encode_loop.py output/groel_rotation_oxillustrate/frames
```

[render_oxillustrate.py](render_oxillustrate.py) invokes the native `illustrate` CLI once per frame;
`--illustrate /path/to/illustrate` overrides its sibling release-binary location. No bindings or
rendering adapter is involved. [oxillustrate.json](oxillustrate.json) retains native scene settings.
Outputs in `output/groel_rotation_oxillustrate/` include primary `animation.webp`, compatibility
`animation.gif` and `animation.mp4`, `poster.webp`, 125 PNG frames, each effective native JSON scene,
`illustrate.log` and `render.json`. The encoder supplies five seconds at 25 fps.

The previous Mol* route remains available with `node examples/render_molstar.mjs groel_rotation`
and outputs to `output/groel_rotation/`; existing Mol* media are preserved.

For the transparent gallery variant, run:

```bash
source source_me.sh && python3 examples/groel_rotation/render_oxillustrate.py --alpha
```

This writes 125 true-alpha PNG frames to `output/groel_rotation_alpha/frames/`, with native
`background: null`. Current native rendering always trims; the helper requests `--metadata`, then
copies each native crop at its exact `crop_origin` into the original 640 by 640 canvas without
resampling. Each `scenes/frame_*_bounds.json` retains that native offset. The gallery derives one
fixed union crop from all 125 frames and presents them in one 4:3 canvas. Historical opaque media
remain under `output/groel_rotation_oxillustrate/`.

## Structure and assembly

Retrieve [1OEL](https://www.rcsb.org/structure/1OEL) **biological assembly 1**, using RCSB's expanded
`1OEL-assembly1.cif`, rather than rendering the asymmetric unit as a complete complex.
Original asymmetric-unit and assembly files were retrieved 2026-11-11; hashes are in
[input_hashes.sha256](../input_hashes.sha256). Both original files remain in `output/inputs/`.
Primary structural paper: [Braig et al., 1995](https://pubmed.ncbi.nlm.nih.gov/8846220/).

The asymmetric unit has seven protein chains; the expanded biological assembly has A-G and
A-2 through G-2. Fourteen chains each contain 3,847 resolved protein atoms: 53,858 total.
The deposited construct reports R13G and A126V mutations. Its unobserved C-terminal residues
526-548 are absent in every subunit and remain absent. The example shows the deposited construct,
not an asserted wild-type model. Omit the 298 assembly waters. There is no GroES, nucleotide or
invented ligand. 1AON is a different GroEL/GroES complex and is not substituted.

## Rotation and settings

[render_oxillustrate.py](render_oxillustrate.py) checks fourteen chain identities and 53,858 protein
atoms in the expanded mmCIF. Native default selection omits its 298 waters; `assembly: null`
prevents a second expansion. Native parsing and prepared sphere identity are checked separately
in [oxillustrate_science.md](../../docs/active_plans/reports/oxillustrate_science.md).

Use opaque illustrated atom spheres with native warm chain colors, black contours and screen-space
shadows on white. Chain colors and an oblique structural view make the assembly easier to read.
Native Euler rotation is Z then Y then X, with x angles `15 + 360*i/125`, for `i = 0..124`,
and fixed y/z angles 25/0 degrees. Native x is the vertical raster axis.
The final sample precedes the first by one ordinary angular step; there is no duplicated 360-degree
frame. Original molecular coordinates stay fixed. One bounding-sphere radius fixes orthographic
scale and safe negative depth for the entire turn. Each scene's subtracted rotated center maps
the same molecular origin to the same image point. Native crop metadata restores 640 by 640
pixels. Equal fog endpoints disable frame-dependent fog normalization; shadows and outlines stay
fixed.

## Verification and licensing

See [oxillustrate_render.md](../../docs/active_plans/reports/oxillustrate_render.md) for native
rendering, framing, timing and replay evidence. The historical Mol* checks remain in
[toolbox_verification.md](../../docs/active_plans/reports/toolbox_verification.md).
Tested oxillustrate 26.11.0 from a dirty working tree: the report records executable and source
hashes, rather than treating HEAD as the complete source identity. The renderer is AGPL-3.0-only;
RCSB inputs follow its data policies. Our scripts are LGPL-3.0 and documentation and generated
previews CC-BY-4.0. No external application is redistributed.
