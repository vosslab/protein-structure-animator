# ATP synthase scientific feasibility

## Recommendation

Use one complete biological assembly of **8DBU**, the E. coli ATP synthase State 2 with epsilon
in the down conformation. Animate a rigid gamma/epsilon/c-ring rotor against the stationary
assembly, using a fixed camera, a schematic membrane band and a disclosed head cutaway. This
is **authored mechanical staging**, not an experimentally observed trajectory, catalytic-cycle
reconstruction, simulation or kinetic measurement. Keep the original assembly intact on disk.

Investigated on 2026-11-12. No graphics were launched. Input identity, geometry and scientific
interpretation are checked here; rendering, atom handoff, playback and reproduction of final
media belong to subsequent checks.

## Primary source evidence

- [8DBU structural record](https://www.rcsb.org/structure/8DBU): cryo-EM, 3.4 A, author-assigned
  biological assembly 1, 22 protein chains, E. coli. Released 2023-01-25; retrieved version 1.2.
- [Sobti et al. 2023](https://doi.org/10.1038/s42003-023-04414-z): enzyme exposed to 10 mM
  MgATP; central-stalk classification separates epsilon half-up and down substates. Additional
  Fo-focused refinement supports fitting the membrane domain. The paper identifies increased
  flexibility of the central stalk in the down state. It does not justify a perfectly rigid rotor
  moving through a frozen catalytic head.
- The paper's preparation uses a cysteine-free construct and a beta-subunit His tag. RCSB's
  headline says no mutations, but the mmCIF records 20 sequence conflicts: 19 Cys-to-Ala changes
  across copies and gamma Glu-to-Asp at label sequence position 6. Retain the deposited model;
  describe the experimental construct rather than claiming a fully wild-type sequence.
- The paper describes synthesis-direction rotation as clockwise viewed from the membrane.
  Equivalently, it is counterclockwise viewed from F1 toward Fo. The same viewpoint convention
  appears explicitly in [Guo et al. 2019](https://doi.org/10.7554/eLife.43128).

Full article XML is saved from Europe PMC in the investigation directory. Source URLs, retrieval
date and SHA-256 hashes are in `output/atp_synthase_feasibility/source_manifest.json`.

## Candidate comparison

| Candidate | What was verified | Decision |
| --- | --- | --- |
| 6N2Y | Complete 22-chain PS3 assembly; 3.0 A; epsilon up | Retain as investigated alternative |
| 6N2Z/6N30 | Same primary paper's other resting rotational classes | No endpoint interpolation |
| 8HH1 | 2.9 A; only alpha3/beta3/gamma deposited despite FoF1 title | Reject for membrane motor |
| 8DBU | Complete 22-chain E. coli assembly; epsilon down; 3.4 A | Select for mechanical staging |

The PS3 paper describes epsilon-up inhibition of hydrolysis while proposing synthesis-direction
rotation remains possible. Its three classes are resting-state structures; whole-complex linear
interpolation would not establish a pathway. The cleaner epsilon-down 8DBU input avoids using
that inhibition-specific extended epsilon geometry for this first illustration.

## Preserved inputs

All originals are under `output/atp_synthase_feasibility/` and remain unmodified.

| File | SHA-256 |
| --- | --- |
| `8dbu.cif` | `059f777a8eec8f207f45aa034b786ca2c3299eefef8470760937747471c6c971` |
| `8dbu_assembly1.cif` | `f9eff1ab7ae60a201fd23fa8f265bca48b76926ee457b8dde8a5f6cad4ea2f40` |
| `6n2y.cif` | `cd24029e8075a2dc36413fc67565d06df98f75ed0460d2c8907df9c2159a3984` |
| `6n2y_assembly1.cif` | `c7e71f847c6a6ce2142b6fcde3b175d9339264a1393d799f7834baea331cca6d` |
| `8hh1.cif` | `628adc887d500e65c6706f0f4cf0d3af8755371dd21d4d84b9e061ef70b85734` |

For 8DBU, native and downloaded assembly contain exactly the same 36,917 atom rows, atom
identities and coordinates. The native assembly instruction is identity operation 1 over all
33 label asym IDs, including ligand IDs. It already contains the entire assembly; do not expand
it a second time. The biological 22-mer counts protein chains rather than ligand asym IDs.

## Chain partition

Select using `_atom_site.label_asym_id`. Author IDs differ in the c-ring and stator chains.

| Component | Label chains | Author chains | Modeled residues | Atom rows | Action |
| --- | --- | --- | --- | --- | --- |
| Alpha3 | A, B, C | A, B, C | 508, 513, 510 | 11,552 | Stationary head |
| Beta3 | D, E, F | D, E, F | 458, 460, 460 | 10,586 | Stationary head |
| Gamma | G | G | 284 | 2,186 | Rotor shaft |
| Epsilon | H | H | 134 | 1,021 | Rotor coupling |
| c10 | I, J, K, L, M, N, O, P, Q, R | I, J, L, M, N, O, P, Q, R, S | 769 total | 5,565 | Rotor ring |
| Delta | S | W | 173 | 1,320 | Stationary cap |
| b2 | T, U | X, Y | 154, 156 | 2,400 | Stationary peripheral stalk |
| a | V | a | 266 | 2,104 | Stationary membrane subunit |

The moving set is labels `GHIJKLMNOPQR`: 12 protein chains and 8,772 atom rows. The stationary
protein set is labels `ABCDEFSTUV`: 10 chains and 27,962 atom rows. All 183 ligand/ion rows
remain stationary, giving 28,145 stationary rows if every deposited atom is rendered.

Ligands are four ATP (labels W, Y, AA, DA), two ADP (EA, GA) and five Mg (X, Z, BA, CA, FA).
These occupy head-associated sites and must not move with the rotor. Alpha-associated ATP is
not evidence of ATP synthesis in this animation. If the cutaway hides the associated protein,
hide its ligand consistently and list that display omission. No phosphate conversion, proton
transport, nucleotide exchange, ATP production or reaction stoichiometry is animated.

## Structural completeness

- All eight distinct protein subunit types and the expected alpha3/beta3/gamma/epsilon/delta/
  a/b2/c10 stoichiometry are present. This means complete subunit assembly, not every residue.
- The model has 4,845 modeled of 4,895 deposited residues. The 50 explicitly unobserved residue
  records are recorded by chain and author number in `8dbu_inventory.json`.
- Eight explicitly missing atom records: six phenyl-ring atoms of alpha A Phe409 and the Cys21
  sulfur atoms on the two b chains. Do not repair or invent these atoms for this illustration.
- One model, all 36,917 occupancies equal 1.00, no alternate conformers and no hydrogen atoms.
- Retain deposited residue numbering, including zero-based starts and unusual chain mapping.
  The inventory records author numbers separately from label sequence IDs.
- Epsilon's atoms lie at local axial coordinates 29.11 to 58.19 A; gamma extends to 145.86 A.
  This compact epsilon geometry agrees with the down-state classification.

## Rotation geometry

The axis is inferred from the plane of the ten c-chain C-alpha centroids, with its sign chosen
toward the F1 head. The plane fit RMS residual is 0.12348 A. Centroid radial distances are
17.6184 to 18.0279 A. This geometry gives a sensible common ring/shaft axis: gamma terminal
helical C-alpha centroids for label residues 1-20 and 260-284 are 2.95 and 3.64 A from it.

In the original 8DBU coordinates, Angstrom units:

```text
origin = [226.7205553486, 238.3251447539, 210.9326034176]
+axis  = [-0.5151796419, -0.8166696025, -0.2600782517]  toward F1
x      = [-0.5155561936,  0.5376905864, -0.6671511407]  toward subunit a
 y     = [0.6846836845, -0.2096177323, -0.6980463154]
z      = +axis
local  = (original - origin) @ [x y z]  (vectors are matrix columns)
```

The basis is orthonormal with determinant +1. Positive right-hand rotation around +axis gives
the synthesis-direction convention above. A fixed side view with image vertical along local z
and depth along local y places subunit a and the peripheral stalk to the right. The full local
bounds are x -52.61 to 76.20 A, y -64.08 to 52.08 A and z -36.43 to 192.12 A. Keep the same
origin, camera, projection and framing in every frame.

A schematic membrane band near local z -20 to +17 A covers the principal hydrophobic spans;
this placement is an illustrative choice, not an experimentally fitted lipid boundary. In the
model, c-ring C-alpha residues 10 and 77 average z -19.85 and -20.00 A; residue 50 averages
+17.02 A and the turn near residue 40 averages +23.75 A. No lipids or membrane are deposited.

## Physical and display limits

A full rigid turn through a completely frozen head is physically invalid. A bounded C-alpha
screen of gamma/epsilon against alpha3/beta3 at 15-degree increments gives minimum separation
5.004 A initially, 0.393 A at 120 degrees, and up to eight pairs below 2 A at 150 degrees.
`rigid_staging_CA_screen.json` preserves all 24 sampled angles. This is a deliberately coarse
screen that demonstrates a limit; it is not a full heavy-atom clash analysis.

The head's conformational changes, central-stalk torsion and peripheral-stalk flexing are omitted.
A head cutaway can expose the shaft and reduce visual occlusion, but does not establish physical
validity. Apply the cutaway as a documented display mask on stationary head atoms, consistently
across all frames. Preserve the full input and all moving chains. A whole-chain or spatial mask
must state exactly which head and associated ligand atoms are hidden in the final example record.
Do not describe hidden atoms as missing from the experimental assembly.

Suggested short delivery statement:

> Authored mechanical illustration based on E. coli ATP synthase 8DBU. Rotor motion and membrane
> are staged; the stationary head is cut away to expose the shaft. This is not a sterically
> validated catalytic trajectory and playback speed does not represent enzyme kinetics.

The near-symmetric c10 ring may appear stationary in one color. Differentiate one existing c
chain in the moving set as a visual marker, with a legend identifying the color choice. This
adds no invented geometry and makes rotation legible.

## Reproduction and checks

Retrieve the selected sources from the repository root:

```bash
mkdir -p output/atp_synthase_feasibility
curl --fail --location --proto '=https' https://files.rcsb.org/download/8DBU.cif \
  -o output/atp_synthase_feasibility/8dbu.cif
curl --fail --location --proto '=https' https://files.rcsb.org/download/8DBU-assembly1.cif \
  -o output/atp_synthase_feasibility/8dbu_assembly1.cif
source source_me.sh && python3 output/atp_synthase_feasibility/inspect_8dbu.py
shasum -a 256 output/atp_synthase_feasibility/8dbu*.cif
```

The saved inspection script checks the 22-chain/36,917-row count, complete identity-column
agreement with the assembly file, finite coordinates and a proper rotation basis. It writes
`8dbu_inventory.json` with detailed residues, missing atoms, source conflicts, ligand identities,
counts, coordinates and axis. Observed runtime versions are Biopython 1.88 and NumPy 2.5.4;
these observations are not dependency pins.

eLife HTML/PDF retrieval returned a JavaScript challenge. Its response was retained as
`elife_block_response.html`, not represented as a PDF. Europe PMC full-text XML supplied both
primary papers successfully. The full final media, native rendering fidelity, collision-free
motion, browser playback, Impress behavior and final example replay are not checked here.
