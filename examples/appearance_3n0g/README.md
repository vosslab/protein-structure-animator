# Isoprene synthase appearance

Compare illustrated atom spheres with an outlined smooth surface before choosing a renderer.
The visual reference is [Goodsell's PDB-101 isoprene synthase illustration](https://pdb101.rcsb.org/motm/201):
blue protein, a contrasting substrate analog, green magnesium, soft depth shading and a white
background. This comparison preserves those cues without claiming a pixel match or identical pose.

## Reproduce

From the repository root, follow [TOOLS.md](../../docs/TOOLS.md) and compile Illustrate as described
in [ILLUSTRATE.md](../../docs/tools/ILLUSTRATE.md):

```bash
bash examples/download_inputs.sh
source source_me.sh && python3 examples/appearance_3n0g/prepare.py
node examples/render_molstar.mjs appearance_3n0g
cd output/appearance_3n0g
../../LOCAL_ONLY/illustrate/illustrate < ../../examples/appearance_3n0g/illustrate.inp > illustrate.log
magick illustrate.pnm illustrate.webp
```

The native [illustrate.inp](illustrate.inp) file retains the Fortran settings. The Mol* script saves
an eight-view rotation check, `scene.molj`, a separate `surface.png` and `surface.molj`, camera
settings and counts. Fixed projection and scale are shared across the short Mol* rotation.
Illustrate is tested as a still renderer here. Mol* supplies the animation route.

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
PDB and mmCIF exports use the same selection. Illustrate's axis convention needs `zrot 90` to match
the Mol* view. Both renders use 640 by 640 pixels, blue protein, magenta DST and green Mg.

## Appearance decision

Illustrate provides the strongest black atom contours and authentic flat sphere shading. Its
fixed-column selection needs careful inspection; the first ligand wildcard was one column short
and silently omitted DST/Mg. The corrected input retains them.

Mol* provides illustrated spheres and smooth molecular surfaces through the same tested browser
invocation. A smooth surface hides more pocket detail than atom spheres. Use transparency when a
buried ligand must remain visible. Mol* is selected for the first animations because it reads the
complete assembly mmCIF directly and accepts the checked native trajectory, with fixed framing.

See [toolbox_verification.md](../../docs/active_plans/reports/toolbox_verification.md) for images, comparison
observations and timing. Tested Mol* 5.13.1, Playwright 1.65.0; Illustrate upstream revision
`e469df4f794f8edbca992a9b2ab534d11d27cdd6` records the tested checkout, not a version requirement.
Mol* is MIT, Illustrate Apache-2.0; original reference art remains attributed to PDB-101/Goodsell
and is not redistributed. Our generated previews are CC-BY-4.0.

| Renderer | Preview |
| --- | --- |
| Illustrate atom spheres | [illustrate.webp](illustrate.webp) |
| Mol* illustrated spheres | [molstar_spacefill.webp](molstar_spacefill.webp) |
| Mol* smooth surface | [molstar_surface.webp](molstar_surface.webp) |
