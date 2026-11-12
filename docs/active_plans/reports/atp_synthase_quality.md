# ATP synthase quality review

## Verdict

**PASS. Verdict: Ship to integration review.** No required correctness, simplicity or regression
fix was found in the approved scope. This follows the specification PASS in
[atp_synthase_specification.md](atp_synthase_specification.md); integration review and plan closeout
remain separate work.

What this change does: it adds a fixed-camera, rigid ATP synthase rotor illustration and true-alpha
WebP delivery. Separate GroEL and hexokinase alpha sources feed three tighter gallery loops, with
one whole-motion crop per clip and matching reduced-motion posters.

## Reviewed scope

I applied the Ponytail and Ponytail review skills, read repository animation and style guidance,
and inspected the working-tree diff, staged geometry test, new ATP source/template/README, new
codec runner, gallery assets and new plan/report inventory. Connected source inspection covered
all encoder callers, both existing source-render paths, gallery framing/encoding, and the current
sibling Rust library/CLI metadata patch and tests. Expected use is one person running documented
local example commands sequentially, as required by the animation guidance.

The implementation follows the existing example scripts instead of adding a framework or new
dependency. The ATP helper keeps preparation, rendering and provenance in one bounded example.
Duplicating a few lines of canvas restoration between two standalone examples does not justify
a shared abstraction here. The added options serve the documented alpha and visual-checkpoint
workflows. No extra configuration, validation gate or speculative recovery layer is needed.

## Correctness and regression

- ATP selection rotates complete label chains G-R; the stationary mask is defined once in local
  coordinates. Full and cutaway coordinate handoffs remain separate. The source basis and camera
  preserve handedness, and the normal-lane camera test directly rejects the earlier reflection.
- Native `render_with_bounds` returns the existing rendered image plus the already computed
  `[left, top]` crop origin. `render` retains its image-only API and unconditional trimming.
  CLI metadata protects structural, scene and image destinations. Sidecar write errors propagate;
  the documented possibility of an already-written generated image is acceptable for this route.
- Both Rust consumers paste at the native origin without a mask or scaling. GroEL checks canvas
  and crop containment; ATP additionally requires RGBA. Scene/background changes remain explicit.
  The obsolete scene trim key is removed from both existing native scenes.
- Existing opaque routes and output directories remain available. Mol* alpha changes background,
  presentation opacity and destination while reusing the existing trajectory, camera and ligand.
  Encoder callers keep the positional interface; its validated dimensions supply the white matte.
  RGB sources also pass through the same compositing path without an unnecessary special branch.
- Gallery validation examines every source frame before sampling. Its alpha union includes labels
  and outlines, adds fixed padding, and uses one crop and scale for all poses. Pillow's transparent
  padding outside the source canvas is intentional for the ATP caption margin. Thumbnail fitting
  only downsizes. No color key, per-frame fit or alpha-squaring paste is present.

The permanent tests protect useful behavior rather than incidental file inventories. Two small
geometry tests cover rigid motion, stationary atoms, cutaway retention, loop closure and proper
camera orientation. The standalone real-codec test checks all 125 frames, moving alpha edges and
vacated pixels, timing, poster equality and actual opaque-format compositing. Native tests compare
asymmetric independent sphere coverage and CLI/library pixels, including opaque white atoms and
destination conflicts. The recorded full native science checks complement these small regressions;
repeating millions of coordinate comparisons in the fast suite would add little value.

## Fresh checks

Run from the repository root on 2026-11-12:

```bash
source source_me.sh && python3 -m pytest tests/test_atp_synthase_geometry.py \
  tests/test_encode_loop.py tests/test_oxillustrate_rotation.py -q
source source_me.sh && python3 tests/e2e/e2e_encode_alpha.py
source source_me.sh && python3 output/atp_synthase_quality/check_gallery.py
git diff --check
git diff --cached --check
```

Results: four focused tests pass in 0.24 seconds; the real-codec regression passes. Both diff
whitespace checks pass. The ignored read-only gallery probe checks all 375 source PNGs against
their recorded concatenated hashes and recomputes all three crops. It decodes 180 gallery frames
and three posters: every alpha channel equals the corresponding fixed-framed source exactly.
All loops contain 60 frames, total 5,000 ms and loop flag 0; canvases and crops match the manifest.
README regeneration is idempotent and its frozen hash matches. The native executable hash matches
`ac4c51ab1f3e27e16b7ce888f4c8eb462b263249b310bf6f6d840b30934ba91f`.
Probe source and results remain in ignored `output/atp_synthase_quality/`.

## Evidence and limits

The independent [atp_synthase_science_verification.md](atp_synthase_science_verification.md) covers
all ATP/GroEL native identities, coordinates, projection and registration, plus sampled Mol*
imports and unchanged glucose. [atp_synthase_gallery.md](atp_synthase_gallery.md) and
[atp_synthase_playback.md](atp_synthase_playback.md) separately establish inspected composition,
decoded alpha and actual browser/Impress motion. These are recorded receipts, not tests rerun by
this reviewer. Frozen-head overlaps, construct/missing-region limits and authored staging are
disclosed beside delivery; no pathway or kinetics claim is substituted for those limits.

[atp_synthase_replay.md](atp_synthase_replay.md) accurately limits exact reproduction to the core
scientific/image/media/gallery outputs. It classifies all eight nonidentical entries among 1,483
baseline files rather than claiming whole-tree equality. Protected historical files and source
hashes are separately checked. Local replay does not establish clean-install portability.

[atp_synthase_checks.md](atp_synthase_checks.md) records the actual broad result: 1,164 passed,
one skipped and two failures, followed by five passing naming checks after temporary-probe cleanup.
The unchanged research-report Unicode baseline remains; this is not a fully green suite claim.

Not checked again: full pytest, native builds/tests/renders, molecular preparation, live browser or
Impress playback, publication or cross-platform reproduction. These limits do not create a new
quality blocker; integration should reconcile the existing receipts and perform planned cleanup.
No product source, native sibling file, gallery asset or Git index was changed by this review.
