# Oxillustrate scientific verification

Independent data-handoff and geometry verdict: **PASS** for the 3N0G still and all 125 GroEL
native scenes on 2026-11-12. This verifies the parsed source atoms and actual `prepare_scene`
spheres. It makes no visual-quality, encoding, playback or rendered-reproduction claim.

## Method and scope

A disposable native Rust consumer called public `load_structure` and `prepare_scene` from the
current sibling `goodsell-oxillustrate-rs` library. It did not call `render`, alter upstream APIs,
expand the assembly, or use the renderer helper's assertions. Its separate target directory avoided
the renderer build. Target: `aarch64-apple-darwin`; Rust 1.99.1; Python 3.12.16.

A separate Python oracle parsed mmCIF atom-site tables with `Bio.PDB.MMCIF2Dict`. It checked every
loaded atom's source ID, author/label atom names, author/label chains, author/label residue numbers,
insertion code, alternate identifier, residue name, element, model, occupancy, chemical category
and coordinates. It then compared every native selected sphere's source index, assembly instance,
projected center and radius with independent NumPy rotation-matrix calculations. Comparison used
the actual scene files, rather than reconstructing them from the helper's metadata.

The native consumer borrowed the loaded `Structure` for each preparation; the resulting `Scene`
owned its spheres. All native parsing/preparation and file operations propagated errors. Compact
results remain under ignored `output/oxillustrate_science/`; disposable source, crate, build target,
loaded-atom JSON and per-frame binary coordinate dumps were removed after the checks.

## Source and build identity

All five original inputs passed `shasum -a 256 -c examples/input_hashes.sha256`. Relevant hashes:

| Input | SHA-256 |
| --- | --- |
| Original `3n0g.cif` | `9fa0ce05f9a62d55e10ba1427d156517bef1e941e3da984d7c985329f329fbba` |
| Prepared `selected.cif` | `0d31b4d5bdd505a3b5231f7711faa92b364eb5402e927d3b2e58efc525384e38` |
| Original `1oel_assembly1.cif` | `fb61ff7da5bafbd92f95a85876616cf5b7d43f8219af4260c81db295aa4ca49d` |

The sibling checkout reports HEAD `29d4e907efe6524eb78188edbdd4a500dc0e5260` with uncommitted
changes. Every source/manifest/lockfile hash in the renderer's captured
`output/groel_rotation_oxillustrate/provenance/build.json` matched the live source used by the
independent consumer. The renderer binary independently matched SHA-256
`9a2441d4383340bd2e16ae1aa0cf447f98543187655d4e430d7d42c2df9e3d17`.
These associate the checks with the observed dirty source; HEAD alone is insufficient.

`output/oxillustrate_science/provenance.json` records full source hashes, the disposable consumer
binary/source hashes, compiler identity and source/build association. `results.json` records the
SHA-256 of the actual still scene and each of the 125 GroEL scenes. Scene hashes were rechecked
against disk after comparison. The still scene hash is
`f0ea8e18ddd371075c4823d96f1d5e06441a7a71d13b9d52697f8ad51869180a`.

## 3N0G selection and fidelity

The original contains 8,987 atom records: 8,631 protein and 356 heterogen atoms. Independent
selection by author chain A, non-water residue and blank/A alternate gives exactly the prepared
input's 4,261 unique author-identity tuples:

| Selected component | Atoms | Author residue identity |
| --- | --- | --- |
| Protein | 4,244 | Chain A |
| DST substrate analog | 14 | A 601 |
| Magnesium | 3 | A 621, 622, 623 |

The preparation omits all 4,486 chain-B records, 169 chain-A waters and 71 chain-A alternate-B
records. The retained records comprise 4,190 blank alternate atoms and 71 alternate-A atoms.
Occupancies remain 4,174 at 1.0, 71 at 0.5 and 16 at 0.75. The input has only deposited model 1.
Native conformer selection therefore retains all 4,261 prepared records, including DST and Mg.
It neither drops a ligand nor selects a different conformer.

Every native loaded coordinate equals its prepared mmCIF coordinate exactly at parsed f64
precision: maximum absolute error 0 Angstrom. All 4,261 selected author identities match the
original source selection. A proper rigid fit from those original coordinates to the prepared
coordinates has determinant 0.999999999999999, atom RMSD 0.0004992388810806044 Angstrom and
maximum atom residual 0.0008497722790300051 Angstrom. This is consistent with the existing
preparation's 0.001-Angstrom mmCIF rounding, with the protein, ligand and ions moved together.

The prepared writer renumbers atom-site IDs and label chains. Native loading preserves those
prepared identifiers exactly; the original-to-prepared comparison uses author chain/residue,
insertion code, residue/atom name, alternate and model instead. All share author chain A, while
native chain-outline identity distinguishes three label chains: protein A, DST B and Mg C.
There are 525 native residue identities, including the four heterogen residues.

For the actual still scene, all 4,261 native projected sphere centers match the independent
matrix calculation exactly in this run. The fitted scale is 8.572779945607188 pixels/Angstrom.
Sphere bounds lie in rows 30 to 610 and columns 38.992846 to 601.007154. The nearest sphere
surface is at z = -11.144614 pixels, safely behind the native zero-depth clipping plane.

## GroEL assembly and motion

The deposited assembly input loads 54,156 atom records exactly, including 298 waters. Every
loaded identity and coordinate matches the independent mmCIF table; maximum coordinate error
is 0 Angstrom. All records have model 1, blank alternate identifiers and occupancy 1.0.

Every one of the 125 scenes contains the same 53,858 protein source atoms: 3,847 each in author
chains A through G and A-2 through G-2. Native water omission accounts for the other 298 records.
Each sphere has `assembly_instance = 0`; `assembly: null` preserves the already expanded input.
There is no second expansion and no silent chain loss. All native atom indices, instance IDs,
chain IDs, residue IDs, colors and radii remain consistent across the turn.

Only orientation and the rotated-coordinate framing center vary between scenes. Canvas, scale,
model, assembly selection, translation, palette/rules, fog, outlines and shadows remain constant.
All scenes request 640 x 640, `trim: false`, white background and fog endpoints 1/1.

The independent matrix is `R = Rx(x) Ry(y) Rz(z)` acting on column coordinates. Native sphere
centers satisfy

```text
projected = (R p - center + translation) * scale + [height/2, width/2, 0]
center    = R origin + [0, 0, depth]
```

This confirms the current subtraction semantics of `Framing.center`. Settings use:

| Quantity | Value |
| --- | --- |
| Fixed molecular origin, Angstrom | `[-43.845, 0, 0]` |
| Full-turn bounding radius, Angstrom | `97.03907896971705` |
| Constant scale, pixels/Angstrom | `2.988486732139123` |
| Constant depth offset, Angstrom | `98.03907896971705` |
| Angles, degrees | `x = 15 + 360 i / 125`, `y = 25`, `z = 0` |

The bound is the maximum atom distance from the fixed origin plus 1.8 Angstrom, covering every
native radius in this input. Consequently the origin projects to the same canvas center and
depth for every angle, although the explicit framing center moves with the rotated origin.

All 6,732,250 native GroEL sphere centers match the independent projection to a maximum
absolute component error of **2.2737367544323206e-13 pixels**. Every projected radius also
matches the independently assigned native element radius times the fixed scale, within 1e-12
pixels. Across all angles, the minimum sphere-bound padding is **32.74894052975708 pixels**;
the nearest sphere surface is **z = -5.803645660223025 pixels**. Thus no sphere crosses the
viewport or zero-depth plane. This bounds molecular spheres, rather than measuring rasterized
outlines or final image pixels.

There are 125 unique orientations, separated by 2.88 degrees, with no duplicate full-turn
endpoint. An extra disposable native preparation at 375 degrees closes onto the initial
15-degree scene within 2.2737367544323206e-13 pixels. The last-to-first atom displacement
magnitudes match the first-to-second step within 3.375077994860476e-13 pixels; ordinary step
magnitudes range from 0.014466637159315222 to 14.213074448965122 pixels. This establishes the
geometric loop seam, independently of media timing or playback.

The motion is a rigid viewpoint rotation of one experimental structure. It contains no
conformational interpolation, simulated trajectory, reaction pathway or measured kinetics.

## Deposited structural limits

The original primary mmCIF records retain experimental and construct limitations. They are
X-ray structures at 2.8 Angstrom resolution. Original 3N0G chain A lists unobserved author
residues 41-62, 73-80, 569-571 and 595; none was invented by preparation. Its construct metadata
records an expression tag and engineered N59D, K308R and C533W substitutions in author numbering.
N59 lies within an unobserved segment. Original 1OEL metadata records engineered R13G and A126V
substitutions in author numbering and unobserved terminal residues 526-548 in deposited chains
A-G. Assembly generation does not supply missing coordinates. These are illustrations of the
deposited constructs, with original ligands and missing regions, rather than repaired wild-type
models. `structural_annotations.json` retains the exact primary-record annotations.

The reduced 3N0G selected mmCIF carries atom-site records, rather than the original missing-region
and construct metadata. Those limitations are verified against the preserved original input;
the reduced file alone would not establish them.

## Executed checks and evidence

The check crate used a path dependency on the sibling library and its already available
`serde_json` dependency. The native main accepted `INPUT DESTINATION SCENE...`, wrote loaded-atom
JSON once, then little-endian sphere records containing center, radius, color, source index,
assembly instance, chain ID and residue ID. The Python oracle compared every record using the
independent mmCIF tables and matrix products described above. No production adapter or testing
framework was added.

The final successful commands were run from the repository root:

```bash
shasum -a 256 -c examples/input_hashes.sha256
cargo build --offline --release \
  --manifest-path output/oxillustrate_science/_check/Cargo.toml \
  --target-dir output/oxillustrate_science/_target
cargo fmt --manifest-path output/oxillustrate_science/_check/Cargo.toml -- --check
cargo clippy --offline --release \
  --manifest-path output/oxillustrate_science/_check/Cargo.toml \
  --target-dir output/oxillustrate_science/_target -- -D warnings
output/oxillustrate_science/_target/release/native_science_check \
  output/appearance_3n0g/selected.cif output/oxillustrate_science/still \
  examples/appearance_3n0g/oxillustrate.json
output/oxillustrate_science/_target/release/native_science_check \
  output/inputs/1oel_assembly1.cif output/oxillustrate_science/groel \
  output/groel_rotation_oxillustrate/scenes/frame_*.json
output/oxillustrate_science/_target/release/native_science_check \
  output/inputs/1oel_assembly1.cif output/oxillustrate_science/groel \
  output/oxillustrate_science/_check/full_turn.json
source source_me.sh && python3 output/oxillustrate_science/_check/verify.py
```

The extra full-turn scene copies frame 000, adds 360 to x and retains its identical mathematical
framing center. The consumer and oracle were disposable checks, so these historical commands
refer to source/build files deliberately removed after execution. Their retained hashes identify
the executed checks; this is not a claim that a permanent reusable verifier was delivered.

Retained compact evidence in `output/oxillustrate_science/`:

- `results.json`: per-scene hashes, counts, projection errors, bounds and depth; aggregate verdict.
- `verification.log`: human-readable aggregate measurements.
- `input_inventory.json` and `structural_annotations.json`: independent source counts and metadata.
- `input_hash_check.log`: all five original hashes passing.
- `native_still.jsonl`, `native_groel.jsonl`, `native_full_turn.jsonl`: native preparation summaries.
- `provenance.json`: source and binary associations plus temporary-check hashes.
- `cargo_build.log`, `cargo_fmt.log`, `cargo_clippy.log`: isolated consumer checks.

No blocker was found within this scientific/data-handoff scope. Graphics, encoded media, browser
and Impress playback, teaching-size visual acceptance and documented rendering replay belong to
the separate renderer/integration evidence. Full upstream Cargo tests and fresh installation were
not run for this independent check.
