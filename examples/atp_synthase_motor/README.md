# ATP synthase motor

The complete rotor of *E. coli* ATP synthase turns inside a stationary cutaway housing, with a
fixed camera. The amber shaft and one amber physical c-subunit make the motion visible against
the blue stator and teal ten-subunit c-ring. A faint membrane band supplies schematic context;
its position near the c-ring and 44-Angstrom thickness are illustrative, not an experimentally
measured membrane boundary.

This is **rigid mechanical staging from one experimental structure**, not a catalytic cycle,
sterically validated trajectory, measured kinetics, or molecular dynamics. Frozen catalytic
head coordinates overlap the rotor at some staged angles; the cutaway improves visibility and
does not establish physical clearance. Five seconds per turn is a presentation choice.

## Reproduce

Build the sibling native renderer, preserving its current source and executable identity as
described in [OXILLUSTRATE.md](../../docs/tools/OXILLUSTRATE.md). Its CLI must support `--metadata`.
From this repository root:

```bash
cargo build --release --manifest-path ../goodsell-oxillustrate-rs/Cargo.toml
bash examples/download_inputs.sh
source source_me.sh && python3 examples/atp_synthase_motor/render_oxillustrate.py --prepare
source source_me.sh && python3 examples/atp_synthase_motor/render_oxillustrate.py
source source_me.sh && python3 tools/encode_loop.py output/atp_synthase_motor/frames
```

Use `--frames 0 31 62` to render selected prepared frames for a visual checkpoint. `--illustrate`
accepts a different executable within its native Git checkout. Preparation keeps all 125 complete
moving mmCIF files plus all 125 camera-oriented cutaway mmCIF files; it can take several minutes.
The original downloaded inputs remain unchanged. Two focused, offline geometry checks run with:

```bash
source source_me.sh && python3 -m pytest tests/test_atp_synthase_geometry.py -q
```

All generated artifacts stay in ignored `output/atp_synthase_motor/`: `coordinates/full_000.cif`
through `full_124.cif`, corresponding `cutaway_*.cif`, `identity_mask.json`, `preparation.json`,
native `scenes/`, trimmed `native/` PNGs and registration sidecars, reconstructed `protein/`
PNGs, composed `frames/`, `illustrate.log`, `render.json`, and `provenance/`. The unchanged
encoder interface adds `animation.webp`, compatibility GIF/MP4, and `poster.webp`.

## Structural source

Use [8DBU](https://www.rcsb.org/structure/8DBU), the epsilon-down *E. coli* ATP synthase structure,
and its expanded biological assembly 1. The native deposition and assembly contain the same
36,917 atom identities and coordinates: 36,734 polymer atoms in 22 chains and 183 heteroatoms.
The source is [Sobti et al., 2023](https://doi.org/10.1038/s42003-023-04414-z). The construct is
cysteine-free with Cys-to-Ala substitutions and a beta-subunit His tag; the mmCIF records 20
sequence conflicts despite the RCSB summary's mutation field. This example depicts the deposited
construct and resolved residues. Missing residues and atoms remain missing; no hydrogen atoms,
membrane lipids, missing loops or new ligands are fabricated. Original input hashes are in
[input_hashes.sha256](../input_hashes.sha256).

Label chains G/H are gamma/epsilon; I-R form the c10 ring. These 12 complete rotor chains contain
8,772 atoms. Stationary polymer chains A-F/S-V plus every deposited heteroatom total 28,145 atoms.
Label S is delta (author W), T/U are b subunits (author X/Y), and V is subunit a (author a).
The script deliberately uses label identities, preserving distinct author identities in every
coordinate file. Model 1 has no alternate conformers and all deposited occupancies are 1.0.

## Motion and cutaway

The axis is normal to the plane of the ten c-subunit centroids, passes through their common
centroid, and points toward F1. Its original-coordinate origin is
`[226.72055535, 238.32514475, 210.93260342]` Angstrom and unit direction is
`[-0.51517964, -0.81666960, -0.26007825]`. A positive right-handed turn corresponds to the
synthesis direction: counterclockwise viewed from F1 toward Fo. Only the complete G-R rotor moves.
The housing and retained nucleotides stay fixed; the illustration makes no binding-change claim.

The fixed coordinate cutaway removes stationary atoms satisfying
`local_y > 0.6 * abs(local_x)`, a viewer-facing wedge of approximately 118 degrees. It omits
7,643 atoms and displays 29,274, including every rotor atom. The cutaway selects deposited atom
spheres; it does not invent protein surfaces. All atom-site identity fields, the exact visible,
omitted and rotor IDs, and all full coordinates are retained for independent inspection.

Of the 183 stationary heteroatoms, retain complete ATP label chains W/Y/DA (31 atoms each),
Mg X/Z/CA (one each), and ADP GA (27): 123 visible heteroatoms. Omit complete ATP AA (31),
Mg BA (one), ADP EA (27) and Mg FA (one): 60 heteroatoms. No nucleotide is partially cut.
The full coordinate frames retain them all. These small pocket ligands may be occluded by the
housing; ligand visibility does not depict binding or catalysis.

## Fixed rendering and evidence

[render_oxillustrate.py](render_oxillustrate.py) maps a fixed eight-degree elevated side view
to native row/column/depth coordinates with a proper rotation (determinant +1), preserving
molecular handedness. The column coordinate is negative local x; the stator side stalk appears
on the left. One 480 x 720 canvas, camera center, orthographic scale,
palette, light and fog settings cover all 125 frames. Every sphere is buried safely behind the
native global depth cutoff. The all-frame bounds include the full uncut assembly and native
maximum atom radius. Native automatic trimming stays enabled: the CLI's exact
`{canvas: [480, 720], crop_origin: [left, top]}` sidecar restores straight RGBA at its original
pixel position without rescaling, matte-keying, or atom fiducials. Pillow adds only the membrane
context, three labels and staging caption; protein shading remains native Rust Goodsell output.

Angles are `360*i/125`, for `i = 0..124`, at 25 fps: a five-second full turn without a duplicate
endpoint. One amber c-subunit is an identity cue, not a distinct biological subtype. Source
JSON is editable in [oxillustrate.json](oxillustrate.json); effective scenes and source snapshots
stay beside the generated delivery. The native renderer is AGPL-3.0-only and is invoked externally.

See [atp_synthase_render.md](../../docs/active_plans/reports/atp_synthase_render.md) for observed
rendering and reconstruction evidence. Scientific coordinate verification, visual acceptance,
decoded-media behavior, browser/application playback, and fresh-process replay are separate checks.
