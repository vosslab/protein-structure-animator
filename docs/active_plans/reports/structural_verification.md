# Structural verification

Verified 2026-11-11 against the retained deposited mmCIF inputs and a fresh ChimeraX 1.10.1
process. This report covers the scientific selections and coordinate handoff in milestones M2/M3
of [protein_animation_toolbox.md](../../archive/protein_animation_toolbox.md). It does not establish
measured dynamics, binding kinetics, energetic plausibility or application playback.
Scientific selections, native-session restoration and final renderer coordinate/identity handoff
checks pass with the explicit fixed-glucose limitation below.

## Evidence and replay

Original inputs pass `shasum -a 256 -c examples/input_hashes.sha256`. The checks read original
mmCIF metadata and atom tables directly using Biopython, rather than relying on the example prose.
Commands run from the repository root:

```bash
mkdir -p output/scientific_verification
cp output/hexokinase_closure/coordinates.npy output/scientific_verification/coordinates_before.npy
cp output/hexokinase_closure/preparation.json output/scientific_verification/preparation_before.json
shasum -a 256 output/hexokinase_closure/coordinates.npy output/hexokinase_closure/protein_loop.pdb output/hexokinase_closure/glucose.cif output/hexokinase_closure/open.cif output/hexokinase_closure/closed.cif > output/scientific_verification/before.sha256
/Applications/ChimeraX-1.10.1.app/Contents/bin/ChimeraX --nogui --exit examples/hexokinase_closure/prepare.py > output/scientific_verification/chimerax_replay.log 2>&1
source source_me.sh && python3 output/scientific_verification/verify.py > output/scientific_verification/summary.log
/Applications/ChimeraX-1.10.1.app/Contents/bin/ChimeraX --nogui --exit output/hexokinase_closure/prepared.cxs output/scientific_verification/check_session.py > output/scientific_verification/chimerax_restore.log 2>&1
shasum -a 256 -c examples/input_hashes.sha256
```

The native preparation replay exits successfully. Before and after `coordinates.npy` hashes are
both `4fde24271e6f19b5e149761e82be20f94486c5bdd4c5fbfb22abf062f852e4ba`; all 125 x 3,651 x 3
coordinate components are exactly equal. This is fresh-process scientific reproduction of the
documented script, with no interactive adjustment. ChimeraX uses its bundled Python and normal
application cache; the repository verification script uses the required bootstrap.

The saved native session is also restored in a separate fresh ChimeraX process. It contains
endpoint models #1/#2 (3,651 atoms, one coordinate set each), the final forward model #3
(3,651 atoms, 125 coordinate sets) and the intermediate return model #4 (3,651 atoms, 64 sets).
All forward atom identities and their order match `preparation.json`. Every restored forward
coordinate set matches `coordinates.npy` within **0.0000038143 angstrom per component**, the
measured native-session floating-point storage error. A first bitwise-equality check exposed
this limit; the repeat uses a 0.00001 angstrom tolerance and passes. The check changes no saved
session or production input. Glucose remains the documented separate mmCIF input.

ChimeraX returns process exit code 0 even when an opened Python script raises an error. Therefore
the fresh-session result requires both the successful generated `session_restore.json` and the
absence of `ERROR` in `chimerax_restore.log`; an exit code alone is insufficient evidence.

The one-time verification script, full numeric results, original-coordinate backup and native
replay log remain in ignored `output/scientific_verification/`. They are diagnostic artifacts,
not a new toolbox interface. The input hashes are retained in
[examples/input_hashes.sha256](../../../examples/input_hashes.sha256).

## Hexokinase source selections

The original 3O80/3O8M deposits report the same 485-residue sequence, chain A, UniProt P33284,
*Kluyveromyces lactis*, and no reported mutation. Their assembly metadata identifies monomers.
The actual source coordinate records give:

| Source | Resolved protein residues | Unique protein atom identities | Protein atom rows |
| --- | --- | --- | --- |
| 3O80 | 469, author residues 17-485 | 3,651 | 3,654 |
| 3O8M | 472, author residues 14-485 | 3,669 | 3,731 |
| Retained common set | 469, author residues 17-485 | 3,651 | 3,651 |

The open deposit lists residues 1-16 as unobserved; the closed deposit lists 1-13. The additional
18 atoms in closed residues 14-16 are omitted. Neither source lists missing protein atoms in
its unobserved-atom category; the open structure instead lists missing atoms in the ANP ligands.
Both prepared endpoint atom sets and both final morph directions retain all 3,651 common protein
identities: **zero further protein atoms lost by morphing**. No unresolved loops are constructed.

The three extra open atom rows are ASP260 side-chain alternatives A/B. Closed protein alternatives
occur at HIS28, SER38, ARG42, SER43, SER50, THR79, SER123, GLU124, SER128, GLU136, SER157, SER167,
PRO223, GLN224, LEU252, ASP256, VAL278, ARG281, SER333, SER347, LYS365, ARG381 and ASN439.
SER128 and SER347 have A/B/C alternatives; the others have A/B. The preparation uses ChimeraX's
selected conformer and removes alternatives. Equal-occupancy VAL278 CA alternatives differ by
about 0.014 angstrom; the selected A conformer must be used when reproducing the fit. Treating
the last deposited alternative as the selection would produce a small but measurable discrepancy.
Original alternatives remain in the input files.

Matching every retained coordinate to the original alternative positions confirms that closed
residues 50, 79, 124, 167, 223, 252, 256 and 281 use B; the other listed closed residues use A.
No retained alternate atom has lower occupancy than another available position for that identity.
Tied occupancies therefore require the actual selected coordinates, rather than a blanket choice
of A. After accounting for these ties, every native closed-endpoint protein component agrees
with its transformed original coordinate to less than 0.000000000001 angstrom; the native open
endpoint has the same precision of correspondence. All source identity and geometry are retained.

Omitted nonprotein coordinate records are explicit:

- 3O80: two partial ANP residues, author A:486 and A:487, with 23 resolved atoms each, plus
  99 waters. Each ANP residue lists eight unobserved atoms: PG, O1G, O2G, O3G, PB, O1B, O2B, N3B.
- 3O8M: 611 waters, four chloride ions (occupancies 1.0, 0.5, 0.75, 0.75), and the 12-atom BGC
  residue A:487, alt B, occupancy 0.22.
- Retained separately: 12 heavy atoms of GLC A:486, alt A, occupancy 0.78, from 3O8M. The two
  deposited glucose identities represent alternatives; they are not displayed together.

## Alignment and ligand registration

The deliberately selected alignment region is author chain A residues 250-450, 201 CA pairs.
An independent least-squares rigid fit reproduces ChimeraX's **0.8983841743 angstrom RMSD**.
This is a chosen stable region with residual flexibility, not a proof of a perfectly rigid domain.
The same-region CA RMSD between final endpoints remains 0.8983841743 angstrom, while the other
268 retained CAs differ by 7.1874240296 angstrom RMSD. Thus the registration removes overall
motion while retaining substantial relative lobe movement. The full-atom endpoint RMSD is
5.6958056611 angstrom.

The independent protein transform applied to the original glucose agrees with saved
`glucose.cif` within **0.0004774 angstrom per component**, consistent with mmCIF decimal rounding.
The ligand stays separate from protein coordinate sets and uses the same fixed registration.

The closest protein/glucose heavy-atom distance across all 125 native frames ranges from
**1.8405825165 angstrom at the open endpoint** to **2.8211460388 angstrom**; the closed endpoint is
**2.5684345251 angstrom**. These are geometric minima, not an interaction-energy calculation.
The open minimum is ASN236 CB to glucose O4; the closed minimum is GLU301 OE2 to glucose O1.
Thirty-one of the 125 frames contain a protein/glucose heavy-atom separation below 2 angstrom.
The short open-state contact limits the physical interpretation of the staged bound pose.
Glucose was not observed in the open deposit. The animation must remain explicitly labeled an
interpolated conformational illustration, with no invented binding path or catalytic-cycle claim.

## Export and loop geometry

Every exported PDB frame is parsed independently using its fixed-width identity and coordinate
fields. Its chain, author residue number, insertion code, residue name and atom name match the
recorded native identities and order exactly. All 125 frames contain 3,651 atoms. The identities
fit within PDB fields: one chain, ordinary residue/atom names, residues 17-485, and no insertion
codes. The format is adequate for this selected handoff; this says nothing about larger assemblies.

| Numeric comparison | Result, angstrom |
| --- | --- |
| PDB versus native, maximum component error across every frame | 0.0004999997 |
| PDB versus native, RMS atom displacement across every frame | 0.0004979191 |
| Native first frame versus saved open endpoint RMSD | less than 0.000000000001 |
| Native closed frame 62 versus saved closed endpoint RMSD | 0.0005018028 |
| Mol* samples 0, 31, 62, 93, 124 versus native, maximum component error | 0.0005023413 |

The imported-coordinate limit includes PDB rounding and Mol* floating-point storage. It is
appropriately below 0.00051 angstrom per component. PDB correspondence is verified in every frame;
Mol* coordinate samples cover both endpoints and representative intermediates.
Mol* independently extracted protein atom identities and order match all 3,651 native keys;
its twelve glucose keys and order match the saved ligand. Imported glucose coordinates agree
with saved ligand coordinates within **0.0000013428 angstrom per component**. The ligand is a
separate unchanged model while the protein model switches frames.

The native trajectory has **125 byte-distinct coordinate samples**, so neither endpoint appears
twice. Forward samples 0-62 contain 62 intervals; return interior samples 63-124 provide the
remaining 63 intervals including the seam to frame 0. Frame-to-frame full-protein RMS motion is:

| Location | RMS displacement, angstrom |
| --- | --- |
| First forward step, 0 to 1 | 0.0037682662 |
| Enter closed reversal, 61 to 62 | 0.0037022925 |
| Leave closed reversal, 62 to 63 | 0.0035857840 |
| Last return interior step, 123 to 124 | 0.0109399149 |
| Loop seam, 124 to 0 | 0.0036495406 |
| Largest interior step | 0.1491345789 |

The seam has no large reset; motion decreases near each endpoint and increases away from it.
The unequal half-durations are the one-sample consequence of an odd-length 125-sample loop.
These geometric checks support the intended sinusoidal easing; visual seam acceptance and
encoded 25 fps timing belong to the separate delivery review.

The earlier `protein_loop.cif` remains rejected: its multi-model export repeats one coordinate
frame (125 model labels, only one unique coordinate set). The final renderer reads the checked
PDB instead. Original deposited mmCIF inputs remain
unaltered.

## GroEL assembly verification

The original 1OEL metadata declares assembly 1 **tetradecameric**, count 14, generated by
operations 1 and 2. Its asymmetric unit has seven protein chains and 26,929 protein atoms.
The expanded `1oel_assembly1.cif` has author chain identities A-G and A-2 through G-2:
**14 chains x 3,847 resolved protein atoms = 53,858 protein atoms**. Each chain has 524 resolved
residues, author numbers 2-525. The deposited 547-residue construct is author-numbered 2-548;
unobserved C-terminal residues 526-548 stay absent. This is not a silently completed assembly.
Applying the deposited assembly operators to the asymmetric-unit atoms reproduces every
expanded protein coordinate exactly: operation 1 is identity, operation 2 maps `(x,y,z)` to
`(x,-y,-z)`, with zero translation. Maximum component error is **0.0 angstrom** across all
53,858 expanded protein atoms.

The deposit reports R13G and A126V mutations and UniProt P0A6F5 from *Escherichia coli*. The
rendered construct must retain this qualification. There are 298 waters in the expanded model;
the rendered polymer component omits them. There is no GroES, nucleotide or additional ligand.

Mol* imports the full model (54,156 atoms including waters) and selects the 53,858-atom polymer
component for display. Imported-coordinate samples at view indices 0, 31, 62, 93 and 124 are
identical to one another: maximum coordinate change **0.0 angstrom**. Against the expanded
source, maximum component storage error is **0.0000037842 angstrom**. The coordinate model
therefore remains fixed while the camera rotates; it does not depict a conformational cycle.
Multi-character expanded chain identities stay in mmCIF, avoiding PDB chain truncation.
The final corrected renderer replay independently extracts all 54,156 model atom keys, including
waters. Every chain, author residue number, insertion code, residue name, atom name and order
matches the expanded source exactly; all fourteen protein chain identities survive import.

## Verification boundary

The checks rerun successfully against both final import records after the renderer's dimension
correction. No identity or numeric handoff item remains pending in this report. Presentation work
does not require repeating the native preparation unless its coordinates or selections change.
No energy minimization, force-field assessment, experimental kinetics, GPU rendering validation,
visual acceptance or browser/Impress playback is established by these checks. Native preparation
and numeric handoff evidence do not by themselves close the full toolbox plan.
