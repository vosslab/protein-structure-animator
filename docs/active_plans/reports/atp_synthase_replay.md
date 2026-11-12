# Fresh-process alpha replay

## Preparation checkpoint

2026-11-12. Scope: reproduce the corrected ATP motor, native GroEL alpha source, Mol* hexokinase
alpha presentation and six current gallery assets using their documented commands and preserved
inputs. This is separate from scientific interpretation, visual acceptance, decoding and browser or
Impress playback. The existing prepared hexokinase trajectory is the documented starting point for
its presentation-only `--alpha` variant; ChimeraX preparation is not rerun.

Read `AGENTS.md`, all repository style guides, animation/human guidance, current example READMEs,
and native/media guides. Apply the repository runtime `source source_me.sh && python3` and native
Node runtime. The latest changelog separates this work's acceptance from historical evidence.
Ponytail mode keeps this receipt and ignored evidence only; no product helper, dependency, binary,
source, shared documentation, ledger or original input is changed by this workstream.

The manager froze the corrected final sources and deliveries before this baseline. Graphics and
new-gallery writes are held until separately authorized, because browser/science verification reads
those files. The replay uses existing fixed output paths only after those readers release them.
No rendered image is copied as a substitute for reproduction.

## Preserved baseline

Ignored evidence lives in `output/atp_synthase_replay/`:

- `baseline.json`: SHA-256 and byte length for 1,483 new-output/gallery/README files, totaling
  1,227,764,019 bytes; includes every complete/cutaway coordinate, scene, native/restored/composed
  PNG, identity manifest, media, poster, provenance and alpha-source artifact present at freeze.
- `baseline_metadata.json`: pre-replay preparation/render records for semantic comparison when
  elapsed time changes.
- `historical_before.json`: all 437 entries from the existing preservation manifest match.
- `inputs.json`: current preserved original inputs; these are read, never downloaded or overwritten.
- `versions.json`: executable versions and native binary SHA-256.

Observed native executable: `illustrate 26.11.0`, SHA-256
`ac4c51ab1f3e27e16b7ce888f4c8eb462b263249b310bf6f6d840b30934ba91f`.
Its existing source/build snapshots retain the dirty native source identity; rebuilding would change
the subject of this local replay. Observed Python 3.12.16, Node v26.13.0, FFmpeg 9.0.2, cwebp 1.6.0.
These are observations, not dependency pins.

## Fresh-process commands

Run each in a fresh process from the repository root, capturing stdout/stderr, `/usr/bin/time -l`
wall time and child peak RSS where available. Native graphics commands run sequentially.

```bash
source source_me.sh && python3 examples/atp_synthase_motor/render_oxillustrate.py --prepare
source source_me.sh && python3 examples/atp_synthase_motor/render_oxillustrate.py
source source_me.sh && python3 tools/encode_loop.py output/atp_synthase_motor/frames
source source_me.sh && python3 examples/groel_rotation/render_oxillustrate.py --alpha
node examples/render_molstar.mjs hexokinase_closure --alpha
```

After a separate gallery-write release:

```bash
source source_me.sh && python3 devel/capture_readme_visuals.py
```

The ATP command must regenerate all 250 coordinate files and all 125 native/restored/composed frames.
GroEL and Mol* must each regenerate all 125 alpha PNGs. Expected local scientific/scene/image/media
bytes are compared directly; logs and elapsed fields may vary explicitly. If compressed image bytes
vary, compare decoded visible RGBA, with fully transparent RGB treated separately, and diagnose
before claiming equivalence. Compare saved Mol* states separately because generated identifiers can
vary. Rehash the historical 437-file manifest after replay; no historical artifact may change.

## Preparation replay

The CPU-only preparation ran after science finished reading all source/native files and before the
browser released graphics. All 377 preparation outputs reproduce byte-for-byte: 250 complete/cutaway
mmCIFs, 125 scenes, identity mask and preparation record. Elapsed time was 137.12 seconds.

The `/usr/bin/time -l` wrapper returned 1 after the child completed because sandboxed macOS rejected
`sysctl kern.clockrate: Operation not permitted`. This is a measurement failure: the complete child
stdout and exact 377 regenerated files establish completed preparation. Its original stdout/stderr
and wrapper return remain preserved. Later commands use direct subprocess exit status, monotonic
wall time and `resource.getrusage(RUSAGE_CHILDREN).ru_maxrss`; that peak is cumulative across the
sequential driver, not an independent per-stage measurement. No product workaround was added.

The fresh ATP native render exited 0 in 35.704 seconds. All 375 PNGs match the baseline bytes:
125 native trimmed frames, 125 reconstructed protein canvases and 125 composed frames. The encoder
exited 0 in 13.615 seconds; animated WebP, MP4, GIF and poster all match the original complete
encoded files byte-for-byte. GroEL alpha rendering exited 0 in 53.397 seconds; all 375 scene,
native-bounds and PNG files match exactly (125 of each).

The first fresh Mol* process failed before rendering because sandboxed Chromium could not register
its macOS `MachPortRendezvousServer` (`bootstrap_check_in ... Permission denied (1100)`). The failed
launch log is retained. The same documented Node command is rerun outside that sandbox, with no
renderer, preparation, browser flags or product-source change.

## Final artifact comparison

Fresh replay passes for the documented preserved-input starting point on this Mac. All 125 new
hexokinase alpha PNGs and its imported-coordinate record reproduce byte-for-byte after the
unrestricted Node process exits 0. Both fresh gallery captures exit 0 and reproduce all six
WebP/poster assets, the complete capture manifest and README bytes. The measured repeat capture
takes 3.150 seconds. No decoded-pixel fallback or tolerance is needed: every regenerated PNG and
encoded delivery file is byte-identical, including their stored alpha. This is equality between original and replay artifacts; it does not
claim source-to-decoded equality of invisible RGB, which the decoder records separately.

The final `comparison.json` covers the same 1,483 baseline files: 1,475 are byte-identical and eight
are separately classified below. Every one of the historical 437 preserved files and all 21 entries
in the historical gallery/input/media manifest still match. All eight replay helper/template/input
hash-file hashes match. No structural input, scientific preparation for the existing examples,
historical media, old gallery asset, product source or native binary was overwritten.

| Changed file | Classification |
| --- | --- |
| ATP `render.json` | Only `wall_seconds` differs |
| GroEL alpha `render.json` | Only `wall_seconds` differs |
| Hexokinase alpha `render.json` | Only `elapsedSeconds` differs |
| ATP `illustrate.log` | Documented native command appends its render log |
| Hexokinase alpha `scene.molj` | Newly generated Mol* state snapshot; contains generated snapshot and transform IDs |
| ATP `check_delivery.py`, `check_delivery.log`, `delivery_checks.json` | Baseline overlaps independent diagnostic work; none is written by a replay command |

The three named diagnostic files are excluded from the product replay claim. The current
`delivery_checks.json` still references eight artifact SHA-256/size pairs, all of which match the
current retained files; `decoder_artifact_references.json` records this check.

Preparation metadata is entirely identical. Removing only the elapsed field from each of the three
render records makes every remaining field identical, including cameras, dimensions, input hashes,
atom counts, motion settings, helper/template hashes, native source hashes, executable hash and
native source HEAD. All ATP native provenance snapshots and crop-origin sidecars reproduce exactly.
Native HEAD remains `6e7736a746efcde1ed65cea965aae86cbc8dfcee`; the preserved 24 native build-input
hashes and 17,127-byte dirty-source patch remain identical. HEAD alone is not the build identity.

The 36,541,417-byte Mol* state file is retained freshly generated, but its old complete JSON was
not duplicated in this compact hash baseline, so no field-by-field old/new state equality is
claimed. Its new snapshot/transform IDs are visible in the retained file. The independent exact
125-frame PNG, imported-coordinate, camera/render-record and unchanged-source comparisons establish
the reproduced molecular delivery. This distinction does not turn a state-file hash mismatch into
a claim of byte-identical saved state.

## Timings and sizes

| Fresh process | Seconds | Observed peak RSS bytes | Result |
| --- | --- | --- | --- |
| ATP preparation | 137.12 | Unavailable from restricted time wrapper | 377 exact prepared files |
| ATP native render | 35.704 | 171,491,328 | Exit 0; 375 exact PNGs |
| ATP encoder | 13.615 | 236,339,200 | Exit 0; four exact encoded files |
| GroEL alpha render | 53.397 | 340,639,744 | Exit 0; 375 exact frames/scenes/sidecars |
| Hexokinase alpha render, unrestricted | 82.13 | 821,329,920 | Exit 0; 125 exact PNGs |
| Gallery capture repeat | 3.150 | 352,894,976 | Exit 0; six exact assets plus README/manifest |

The first three graphics RSS entries are cumulative child peaks in their sequential driver; the
unrestricted Mol* and gallery measurements have their own process measurements. Failed restricted
Mol* launch took 0.226 seconds and generated no replacement frames. Its failure is not included as
a successful render. Preparation's timing wrapper failure is retained separately above.

| Delivery | Bytes |
| --- | --- |
| ATP lossless animated WebP | 7,729,844 |
| ATP MP4 | 1,105,430 |
| ATP GIF | 2,785,531 |
| ATP lossless poster | 114,330 |
| ATP gallery WebP / poster | 2,780,856 / 71,800 |
| GroEL gallery WebP / poster | 4,346,884 / 63,660 |
| Hexokinase gallery WebP / poster | 2,242,604 / 30,776 |

Full file-level SHA-256 and sizes remain in `baseline.json` and `after.json`; command records,
stdout, original errors and resource measurements remain beside them. These compact manifests and
logs avoid duplicating the 1.2 GB output tree.

## Evidence limits

This verifies local fresh-process reproduction from retained structural inputs and the documented
prepared hexokinase trajectory. It does not rebuild native tools, redownload structural records,
repeat ChimeraX preparation, establish clean-install portability or guarantee pixel identity on
other systems. Scientific interpretation/coordinate review, visual acceptance, media decoding,
browser and Impress playback remain separately owned evidence. This workstream did not launch
Blender, run a full repository suite, commit or publish. No task-owned test files were created.
