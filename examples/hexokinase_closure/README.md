# Hexokinase closure

An interpolated conformational illustration of *Kluyveromyces lactis* hexokinase closing and
reopening around a fixed, experimentally bound glucose pose. The five-second timing and reopening
are explanatory choices. This is neither a simulated binding path nor a complete catalytic cycle.

Preview: [preview.webp](preview.webp).

## Reproduce

Start at the repository root with the installations in [TOOLS.md](../../docs/TOOLS.md):

```bash
bash examples/download_inputs.sh
/Applications/ChimeraX-1.10.1.app/Contents/bin/ChimeraX --nogui --exit examples/hexokinase_closure/prepare.py
node examples/render_molstar.mjs hexokinase_closure
source source_me.sh && python3 tools/encode_loop.py output/hexokinase_closure/frames
```

Use the installed ChimeraX path on your machine; the application name records the tested version,
not a required pin. No interactive adjustments are needed. Do not run `prepare.py` with system
Python: ChimeraX supplies its runtime and session. Other Python commands use the repo bootstrap.

Outputs live in `output/hexokinase_closure/`: `animation.webp`, `animation.gif`, `animation.mp4`,
`poster.webp`, native `prepared.cxs`, `scene.molj`, matched endpoint and glucose mmCIF files,
`protein_loop.pdb`, independent in-memory `coordinates.npy`, selections in `preparation.json`,
render settings/evidence in `render.json`, and PNG frames. These generated files are ignored by Git.

## Scientific sources and selections

Retrieved 2026-11-11 from RCSB: [3O80](https://www.rcsb.org/structure/3O80), open state with an ATP
analog, and [3O8M](https://www.rcsb.org/structure/3O8M), glucose-bound closed state. Both identify
KlHxk1, UniProt P33284, with the same 485-residue sequence and no reported mutations. Primary paper:
[Kuettner et al., 2010](https://pubmed.ncbi.nlm.nih.gov/20943665/). Original mmCIF files remain intact;
byte hashes are retained in [input_hashes.sha256](../input_hashes.sha256).

- Use chain A in each structure. Open residues 1-16 and closed residues 1-13 are unobserved.
  Keep corresponding resolved atoms in residues 17-485: 469 residues and 3,651 atoms per frame.
  Closed-only residues 14-16 contribute 18 atoms and are omitted. No loops or atoms are invented.
- ChimeraX selects its default highest-occupancy protein conformers and `altlocs clean` removes
  alternatives. Original deposits retain the alternatives for inspection. Record exact retained
  identities and omissions in `preparation.json`.
- Omit 3O80's two partial ANP residues, 486 and 487. Each has 23 resolved atoms and eight missing
  phosphate atoms; neither is treated as a complete molecule. Also omit 99 waters. Omit 3O8M's
  611 waters, four chloride ions and the
  12-atom BGC alternative at residue 487, alt B, occupancy 0.22.
- Display 3O8M GLC A:486, alt A, occupancy 0.78: twelve heavy atoms. Preserve its experimental pose
  and apply the protein's alignment transform. It stays fixed in stable-region coordinates during
  the entire illustration. Glucose was not experimentally observed in the open endpoint.

## Motion and presentation

[prepare.py](prepare.py) uses the native ChimeraX least-squares fit of chain A residues 250-450 CAs
to register the large lobe: 201 pairs, RMSD 0.8984 angstrom. The region is an explicit example
choice, not an automatically asserted biological rigid domain. Its measured residual flexibility
remains in the morph. Fit every frame to the same region to remove whole-protein drift while
retaining relative closure.

Two native internal-coordinate morphs use sinusoidal easing: 62 forward intervals and 63 return
intervals. Keep the forward open and closed endpoints once and omit the repeated endpoints of the
return trajectory. This gives 125 distinct samples at 25 fps and a smooth seam. The forward and
return half-durations differ by one frame because 125 is odd. Intermediates are geometric constructs.

The fixed ligand has a closest protein heavy-atom distance of 1.84 angstrom at the opening
endpoint, versus 2.57 at closure. This short open-state contact is a limitation of staging a
closed-state ligand in the open protein, not evidence of a physical complex. Do not use these
intermediates for interaction energies or mechanistic inference.

Mol* renders a pale blue smooth molecular surface at alpha 0.42 over magenta glucose, on white.
Transparency keeps the ligand visible through closure, with overlapping front/back surface detail.
The camera, scale and orthographic projection stay fixed. Native settings are in
[render_molstar.mjs](../render_molstar.mjs) and the saved Mol* state.

## Verification record

Native PDB export has 125 frames, 3,651 corresponding atoms per frame, representable identities,
and maximum coordinate error below 0.00051 angstrom against retained NumPy positions. Endpoint
RMSDs against the aligned source coordinates are below 0.001 angstrom. Glucose is separate and
does not disappear from the trajectory.

The first native multi-frame mmCIF export repeated the opening coordinates; it is rejected for
rendering. See [CHIMERAX.md](../../docs/tools/CHIMERAX.md). The PDB handoff was selected only after
comparison, without changing original structural inputs.

Visual and playback observations and the final replay result are recorded in
[toolbox_verification.md](../../docs/active_plans/reports/toolbox_verification.md).
Tested tools: ChimeraX 1.10.1, Mol* 5.13.1, Playwright 1.65.0, FFmpeg 9.0.2; repo Python 3.12.16,
NumPy 2.5.4, Biopython 1.88 and Pillow 13.0.0. Versions record observations; install current releases.

ChimeraX has separate noncommercial/commercial terms. Mol* is MIT; source inputs follow
[RCSB data policies](https://www.rcsb.org/pages/policies). Our scripts are LGPL-3.0 and explanatory
material/figures CC-BY-4.0. No third-party application or original Goodsell artwork is bundled.
