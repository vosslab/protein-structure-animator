# Isoprene synthase appearance

Use native oxillustrate atom spheres as the canonical Goodsell method; retain the earlier
Fortran Illustrate and Mol* comparisons, including the outlined smooth surface.
The visual reference is [Goodsell's PDB-101 isoprene synthase illustration](https://pdb101.rcsb.org/motm/201):
blue protein, a contrasting substrate analog, green magnesium, soft depth shading and a white
background. This comparison preserves those cues without claiming a pixel match or identical pose.

## Reproduce

Build the sibling Rust renderer as described in [OXILLUSTRATE.md](../../docs/tools/OXILLUSTRATE.md),
then run from this repository root:

```bash
bash -c 'cd ../goodsell-oxillustrate-rs && cargo build --release'
bash examples/download_inputs.sh
source source_me.sh && python3 examples/appearance_3n0g/prepare.py
mkdir -p output/appearance_3n0g/oxillustrate
../goodsell-oxillustrate-rs/target/release/illustrate output/appearance_3n0g/selected.cif \
  --scene examples/appearance_3n0g/oxillustrate.json \
  --output output/appearance_3n0g/oxillustrate/still.png
```

Native [oxillustrate.json](oxillustrate.json) retains the canonical settings. The CLI reads the
prepared mmCIF directly, with no PDB conversion. The scene declares a 640 by 640 opaque canvas;
the current CLI trims the output to content, so the written PNG dimensions can differ. Retained
assets were not rerendered for this compatibility correction. The preview is
[oxillustrate_preview.webp](oxillustrate_preview.webp). The existing [prepare.py](prepare.py)
owns coordinate selection and ligand-facing orientation. It does not rebuild missing residues.

The earlier native [illustrate.inp](illustrate.inp) file retains the Fortran settings. The comparison
command `node examples/render_molstar.mjs appearance_3n0g` saves
an eight-view rotation check, `scene.molj`, a separate `surface.png` and `surface.molj`, camera
settings and counts. Fixed projection and scale are shared across the short Mol* rotation.
The canonical full-assembly rotation is demonstrated separately in
[groel_rotation/README.md](../groel_rotation/README.md).

## Structure and interpretation

[3N0G](https://www.rcsb.org/structure/3N0G), retrieved 2026-11-11, is the gray poplar isoprene
synthase complex with dimethylallyl-S-thiolodiphosphate (DST) and three Mg ions.
[Primary structural paper](https://pubmed.ncbi.nlm.nih.gov/20624401/).
The deposit reports N59D, K308R and C533W mutations. This illustrates the deposited construct.

Keep chain A, DST A:601 and magnesium A:621-623. Omit chain B and solvent. Use blank or A alternate
locations, giving 4,244 protein atoms, fourteen DST atoms and three Mg atoms. Chain A's missing
residues are 41-62, 73-80, 569-571 and 595; do not reconstruct them. Protein atoms lacking resolved
side chains remain as deposited. Original mmCIF is retained in `output/inputs/3n0g.cif`, with its
hash in [input_hashes.sha256](../input_hashes.sha256).

[prepare.py](prepare.py) rotates resolved coordinates to face the ligand toward +z. It transforms
every alternate-location child before selecting a conformer; transforming only a Biopython
DisorderedAtom wrapper left some atoms at their old locations in an early rejected experiment.
PDB and mmCIF exports use the same selection. The native illustrated-sphere axis convention uses
90 degrees about z to match the Mol* view. Historical renders use 640 by 640 pixels, blue protein,
magenta DST and green Mg. The Rust scene keeps native sphere radii, shadows and contours, with
equal fog endpoints and no transparency or cutaway. Only exposed ligand/ion surfaces are visible.

## Appearance decision

Native Rust oxillustrate is the selected Goodsell method for this still and the GroEL rotation.
Its typed appearance rules select DST and Mg without fixed-column wildcard cards. Native parsing
and sphere identity are checked separately from image appearance; see
[oxillustrate_science.md](../../docs/active_plans/reports/oxillustrate_science.md).

The earlier Fortran Illustrate comparison provides strong black atom contours and flat shading. Its
fixed-column selection needs careful inspection; the first ligand wildcard was one column short
and silently omitted DST/Mg. The corrected input retains them.

Mol* provides illustrated spheres and smooth molecular surfaces through the same tested browser
invocation. A smooth surface hides more pocket detail than atom spheres. Use transparency when a
buried ligand must remain visible. Mol* remains the surface and hexokinase-trajectory renderer.
Its historical outputs stay available.

See [toolbox_verification.md](../../docs/active_plans/reports/toolbox_verification.md) for images, comparison
observations and timing. Tested Mol* 5.13.1, Playwright 1.65.0; Illustrate upstream revision
`e469df4f794f8edbca992a9b2ab534d11d27cdd6` records the tested checkout, not a version requirement.
Rust oxillustrate is AGPL-3.0-only, Mol* is MIT, Fortran Illustrate Apache-2.0; original reference art
remains attributed to PDB-101/Goodsell
and is not redistributed. Our generated previews are CC-BY-4.0.

| Renderer | Preview |
| --- | --- |
| Canonical Rust oxillustrate spheres | [oxillustrate_preview.webp](oxillustrate_preview.webp) |
| Illustrate atom spheres | [illustrate.webp](illustrate.webp) |
| Mol* illustrated spheres | [molstar_spacefill.webp](molstar_spacefill.webp) |
| Mol* smooth surface | [molstar_surface.webp](molstar_surface.webp) |
