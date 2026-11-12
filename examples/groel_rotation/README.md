# GroEL rotation

A full-turn view of the complete fourteen-subunit GroEL assembly. Only the viewpoint changes;
this does not show a conformational cycle, ATP hydrolysis, folding dynamics or measured kinetics.

Preview: [preview.webp](preview.webp).

## Reproduce

From the repository root, use the current dependencies in [TOOLS.md](../../docs/TOOLS.md):

```bash
bash examples/download_inputs.sh
node examples/render_molstar.mjs groel_rotation
source source_me.sh && python3 tools/encode_loop.py output/groel_rotation/frames
```

No ChimeraX, Illustrate or Blender is needed for this example. The native Mol* script is shared
with the first example; only the input, representation and viewpoint sequence differ.
Outputs in `output/groel_rotation/` include `animation.webp`, `animation.gif`, `animation.mp4`,
`poster.webp`, PNG frames, editable `scene.molj` and `render.json`.

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

[render_molstar.mjs](../render_molstar.mjs) selects the expanded coordinate model and its polymer
component. It checks fourteen chain identities and 53,858 protein atoms before rendering.
The PDB format's single-character chain field is avoided entirely.

Use opaque illustrated spacefill with chain colors, black contours and depth shading on white.
Chain colors and an oblique structural view make the near sevenfold symmetry easier to read.
The orthographic camera orbits the fixed target through angles `2*pi*i/125`, for `i = 0..124`.
The final sample precedes the first by one ordinary angular step; there is no duplicated 360-degree
frame. Projection, scale, target, dimensions and molecular coordinates stay fixed.

## Verification and licensing

See [toolbox_verification.md](../../docs/active_plans/reports/toolbox_verification.md) for assembly counts,
visual checks, application playback, timing and the fresh-process replay result. Tested Mol* 5.13.1,
Playwright 1.65.0 and FFmpeg 9.0.2, with current-release `>=` dependency requirements.
Mol* is MIT; RCSB inputs follow its data policies. Our scripts are LGPL-3.0 and documentation and
generated previews CC-BY-4.0. No external application is redistributed.
