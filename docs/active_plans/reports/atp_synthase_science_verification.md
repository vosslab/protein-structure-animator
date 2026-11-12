# ATP synthase science verification

Independent science and native coordinate-handoff verdict: **PASS**, dated 2026-11-12, for all
125 corrected ATP frames, all 125 GroEL alpha scenes and the sampled hexokinase alpha import.
Visual quality, browser playback, encoding and fresh rendered reproduction are separate evidence
and are not established by this report.

## Independent method

The disposable oracle and public Rust consumer are retained in ignored
`output/atp_synthase_science_verification/`. The Python oracle parses the preserved mmCIF directly,
fits the c-ring axis with an SVD, and applies a separate Rodrigues rotation in original Cartesian
coordinates. It imports no example helper functions. It checks every identity field in full and
cutaway files, the source-derived stationary mask and complete ligands, all-frame coordinates,
stationary positions, rotor axial/radial invariants and neighboring-atom distances.

The separate Rust crate uses public `load_structure` and `prepare_scene`. It compares every loaded
atom with the independent mmCIF identity and coordinate oracle, then uses each sphere's actual
`source_atom_index` to associate prepared geometry with its atom. Sphere traversal order changes
with appearance rules; it is not assumed to be source order. The consumer checks assembly instance,
complete selected membership, projection, radius, viewport bounds and zero-depth safety. It calls
neither `render` nor graphics APIs. Its offline release build took 10.33 seconds.

## Primary scientific interpretation

The live [8DBU record](https://www.rcsb.org/structure/8DBU) identifies the E. coli epsilon-down
State 2 reconstruction after MgATP exposure. The preserved deposited and assembly-1 mmCIF files
are the coordinate authority. The original contains 36,917 atom rows in 22 protein chains, with
one model, unit occupancy and no alternate conformers. Complete subunit assembly does not mean
complete residue or atom coverage.

The saved primary full text of
[Sobti et al.](https://doi.org/10.1038/s42003-023-04414-z) supports the cysteine-free construct,
beta His tag, epsilon conformations and central/peripheral stalk flexibility. The rigid whole turn
against a frozen head is authored mechanical staging. The membrane, playback speed and cutaway
do not establish a catalytic trajectory, steric validity, chemical conversion or enzyme kinetics.
Synthesis-direction rotation is counterclockwise viewed from F1 into Fo, equivalent to clockwise
viewed from the membrane. Sobti et al. and
[Guo et al.](https://doi.org/10.7554/eLife.43128) describe the viewpoint convention; the staged
positive right-hand rotation is checked separately against the signed axis.

## Proper camera correction

The first proposed camera map had determinant -1. Native coordinates are row down, column right
and depth toward the viewer; this is a right-handed frame. The reflected map would mirror the
molecule and its apparent rotation. Independent review identified this before final rendering.
The correction uses `column = -local_x`, preserving the stationary front wedge and giving a
proper determinant +1 camera transform. The membrane/stator appears on the opposite screen side.
All final checks below use the regenerated proper-camera handoffs; none uses the interrupted
mixed output.

## ATP assembly and omissions

The deposited and downloaded assembly have identical identity fields and coordinates: 36,917 rows,
36,734 protein atoms, 22 protein chains and 183 ligand/ion atoms. Assembly operation 1 is the
identity operation. Model 1 and `assembly: null` retain that complete assembly once.

| Preserved input | SHA-256 |
| --- | --- |
| Deposited `8dbu.cif` | `059f777a8eec8f207f45aa034b786ca2c3299eefef8470760937747471c6c971` |
| `8dbu_assembly1.cif` | `f9eff1ab7ae60a201fd23fa8f265bca48b76926ee457b8dde8a5f6cad4ea2f40` |

Label chains G-R contain the entire 8,772-atom rotor: gamma, epsilon and all ten c subunits.
The 27,962 protein atoms in label chains A-F/S-V and all 183 ligand/ion atoms stay stationary,
for 28,145 stationary atoms total. Author-chain identifiers differ from label IDs; selection
uses label IDs and preserves both namespaces in every full/cutaway handoff.

The source-derived fixed mask removes 7,643 stationary atoms and displays 29,274, retaining all
8,772 rotor atoms. Every omitted and selected ID agrees with `identity_mask.json`; it is a
display omission, not an experimentally absent atom. All eleven deposited ligand/ion entities
are either fully retained or fully omitted, with no split nucleotide:

| Displayed labels | Atom rows |
| --- | --- |
| W/Y/DA ATP, X/Z/CA Mg, GA ADP | 123 |
| Omitted AA ATP, BA Mg, EA ADP, FA Mg | 60 |

All full coordinate frames retain all 183 heterogen atoms unchanged. Four ATP, two ADP and five
Mg sites do not depict nucleotide exchange, phosphate conversion or ATP production.

The original records 4,845 modeled of 4,895 deposited residues: 50 explicitly unobserved residues.
Its eight missing-atom records comprise six Phe409 ring atoms on alpha A and the two b-subunit
Cys21 sulfur atoms. Twenty sequence-conflict records include nineteen Cys-to-Ala changes and
gamma Glu-to-Asp at label position 6. The construct, beta tag, missing regions and deposited
numbering are retained; no repaired wild-type model is claimed. Detailed original annotations
are in `structural_annotations.json`.

## ATP motion and handoff

The independent SVD fit gives origin `[226.7205553486, 238.3251447539, 210.9326034176]` Angstrom
and axis `[-0.5151796419, -0.8166696025, -0.2600782517]`, signed toward the F1 head. Both the
local basis and final camera have determinant +1. Every frame agrees with a positive right-hand
Rodrigues rotation of only the rotor around that axis, followed by the fixed camera transform.
Every stationary full-frame coordinate equals the deposited input exactly.

| All-frame measurement | Maximum error, Angstrom |
| --- | --- |
| Full coordinates against independent rigid rotation | 4.999998566290742e-7 |
| Selected camera coordinates against independent transform | 4.999997935684064e-7 |
| Rotor axial coordinate | 7.933734078591215e-7 |
| Rotor radial distance | 8.395896706758776e-7 |
| Neighboring rotor-atom distance | 1.5970554876343357e-6 |
| Last-to-first displacement versus first-to-second displacement | 1.277155953771647e-6 |

The handoffs use six-decimal Angstrom coordinates. These errors are consistent with that text
rounding. All 125 full coordinate files are unique; the step is 2.88 degrees, without a duplicated
360-degree endpoint. The logical frame 125 is the original pose. The reported seam checks geometry,
independently of encoding duration or playback.

All 125 scenes are identical: model, selection, orientation, translation, center, scale, canvas,
depth, appearance and background stay fixed. All 3,659,250 native selected spheres preserve the
expected source identity and assembly instance zero. Native imported coordinates agree exactly
with the selected CIF; native projected centers and radii agree exactly with the independent
projection calculation in this run. Minimum sphere padding is 50.794209107034234 pixels and
the nearest sphere surface is z = -65.61790235876526 pixels. No sphere crosses the viewport or
native zero-depth clipping plane.

For all 125 actual native PNGs, the RGBA pixel array copied at the native metadata origin equals
the saved protein canvas exactly, including transparent and partial-alpha pixels. The fixed
canvas is 480 by 720, the recorded origin is `[61, 46]`, and native crop sizes vary from 356 by
619 to 356 by 626. This changing trim height does not recenter the molecule. The composed source
alpha union is `[19, 27, 461, 713]`; membrane and labels require separate visual acceptance.

An independently recomputed coarse C-alpha screen gives minimum gamma/epsilon-to-head separation
5.003817 Angstrom initially, 0.393083 Angstrom at 120 degrees, and eight pairs below 2 Angstrom
at 150 degrees. This establishes an actual frozen-head overlap limitation, not full steric
validation. The displayed membrane band at local z approximately -22 to +22 Angstrom is schematic
context rather than a fitted lipid boundary. No lipids are deposited.

## Native source identity

The renderer executable independently matches SHA-256
`ac4c51ab1f3e27e16b7ce888f4c8eb462b263249b310bf6f6d840b30934ba91f`.
The current sibling source is HEAD `6e7736a746efcde1ed65cea965aae86cbc8dfcee` plus the seven-file
uncommitted crop-metadata patch. All 25 source/build hashes in the captured alpha build manifest
match current files. HEAD alone is not a complete source identity. `provenance.json` preserves
the source hashes, dirty status, compiler identity and independent consumer binary/source hashes;
the renderer snapshot retains the patch and complete build inputs.

The consumer binary SHA-256 is
`7bc92e988eee234717e11a79b11083227d979916350b224bc3e410a4f2a5c7a2`.
The executed oracle SHA-256 is
`9ee5110ecfa6dc8c511f590439f40e9e5ea6f45231f758b76c17c826f7928b64`.
Observed Rust is 1.99.1 on aarch64-apple-darwin. These identify the checks actually run; they are
not dependency pins.

## Existing alpha examples

The fresh native consumer checks all 125 GroEL scenes and all 6,732,250 prepared protein spheres.
The input contains 54,156 atom records: 53,858 protein atoms, 3,847 in each of 14 author chains,
and 298 omitted waters. Every native loaded identity and coordinate matches the preserved mmCIF
exactly. Every sphere has assembly instance zero; no second biological-assembly expansion occurs.

| GroEL measurement | Result |
| --- | --- |
| Native import coordinate error | 0 Angstrom |
| Maximum projection component error | 2.2737367544323206e-13 pixels |
| Maximum projected radius error | 0 pixels |
| Minimum sphere padding | 32.74894052975706 pixels |
| Nearest sphere surface depth | -5.803645660223025 pixels |
| Fixed source origin | `[-43.845, 0, 0]` Angstrom |
| Fixed scale | 2.988486732139123 pixels/Angstrom |
| Fixed depth offset | 98.03907896971705 Angstrom |

Only orientation and its corresponding rotated-coordinate framing center vary. Independent
matrix calculations verify the same fixed source origin for every scene; all remaining camera,
selection and appearance settings are constant. This is a rigid viewpoint turn with no
conformational change or measured kinetics.

Hexokinase's new alpha import has exactly the historical protein identity list and five imported
coordinate samples at frames 0, 31, 62, 93 and 124. The native preparation remains 125 by 3,651 by
3 coordinates. Maximum component errors against that preparation range from 3.784179682497779e-6
to 0.0005023412129503413 Angstrom, consistent with the PDB handoff and float32 import precision.
All 12 fixed glucose atoms, ligand identity and coordinates equal the historical import exactly.
This checks the new renderer handoff against the existing scientific preparation; it does not
reclassify the internal-coordinate interpolation as an observed pathway.

All 250 source PNGs are 640 by 640 RGBA with real zero-alpha and opaque pixels. GroEL has at least
216,038 fully transparent pixels per frame; hexokinase has at least 327,353. All 125 GroEL native
crop origins correspond to the reinserted alpha bounds with the native three-pixel crop padding.
This establishes fixed-canvas registration and source alpha, not encoded animation or playback.

## Commands and evidence

Run from the repository root:

```bash
cargo build --release --offline \
  --manifest-path output/atp_synthase_science_verification/consumer/Cargo.toml \
  --target-dir output/atp_synthase_science_verification/target
source source_me.sh && python3 output/atp_synthase_science_verification/verify.py
output/atp_synthase_science_verification/target/release/independent-science-consumer \
  output/atp_synthase_science_verification/native_manifest.json \
  output/atp_synthase_science_verification/native_results.json
```

Completed evidence includes `results.json`, `native_results.json`, `atp_registration_results.json`,
`groel_native_results.json` and `existing_alpha_pixel_results.json`. The standalone GroEL check uses
`groel_native_manifest.json` with the same consumer. Source hashes, input hashes and actual
consumer identity are retained alongside results. No dependencies are added to the repository.

## Evidence limits

This report does not establish collision-free motor motion, biological kinetics, accepted rendered
appearance, encoded WebP behavior, browser/Impress playback or a fresh rendering replay. Sphere
bounds measure molecular geometry; rasterized outlines, labels, membrane band and gallery crops
require their separate visual/media checks. No Blender, native image render, browser or full suite
is run in this science-verification workstream.
