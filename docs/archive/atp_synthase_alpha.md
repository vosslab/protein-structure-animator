# ATP synthase and alpha WebP

## Goal

Add a transparent animated WebP delivery and a canonical Rust Goodsell ATP synthase example. The
animation keeps a fixed camera while the rotor moves against the stator, uses a membrane band and a
cutaway that exposes the shaft, includes only a few labels, and uses one aspect ratio suited to the
tall complex. Improve gallery framing with one crop that contains the full motion, keeps the protein
the same apparent size, and clips no atoms. Adjust pale hexokinase contrast only if a simple change
is supported by visual evidence.

The user approved these outcomes with "I like your ideas do it." Follow
[ANIMATION_GUIDANCE.md](../ANIMATION_GUIDANCE.md): keep scientific interpretation, coordinate
fidelity, visual quality, playback, and fresh-process reproduction as separate evidence. The current
gallery and native Rust integration have passed scoped reviews. A historical full Python run records
an unrelated documentation Unicode failure; retain that as a baseline limitation when reporting
broader checks.

## Approach

1. Resolve the feasibility reports for ATP synthase structure and motion, native true-alpha
   output, and transparent media/crop behavior. Preserve structural inputs and hashes. Select the
   structure only after checking the primary record, biological assembly, chains, missing regions,
   ligands, and what the deposited state supports. Treat authored rotor motion as illustration, not
   measured kinetics or a reaction pathway.
2. Implement the smallest native rendering and encoding changes needed for decoded WebP alpha to
   remain transparent. Add the ATP synthase example under `examples/atp_synthase_motor/`, with a
   fixed camera, stable framing and scale, documented cutaway, membrane band, sparse labels, and
   one fixed canvas. Keep generated structures, frames, and media in ignored `output/`.
3. Update the gallery capture path to derive one framing crop from the union of the protein bounds
   across the complete motion. Keep canvas dimensions and protein scale fixed; reject a crop that
   clips content. Check hexokinase contrast and make a small palette change only if it improves
   visibility without weakening existing concept cues.
4. Render from a fresh process, inspect representative frames and the full loop seam, decode and
   inspect the WebP alpha, and verify browser playback over light and dark backgrounds, reduced
   motion, and narrow and desktop layouts. Replay the documented example from preserved inputs and
   commands. Record actual results in the example and task ledger.
5. Complete independent specification, quality, and integration reviews in that order. Fix findings
   and repeat the affected evidence. Close this plan only after each required review passes.

## File scope

- `tools/encode_loop.py` and its caller, only if the alpha feasibility check shows a gap.
- `examples/atp_synthase_motor/` for the new structural preparation, native scene/render inputs,
  example README and native provenance.
- `tests/test_atp_synthase_geometry.py` for stable rotor/camera invariants and
  `tests/e2e/e2e_encode_alpha.py` for explicit real-codec delivery verification.
- Existing GroEL native helper/scene and Mol* hexokinase render caller for opt-in true-alpha
  sources. Preserve original opaque outputs; write new sources into separate alpha directories.
- Sibling `goodsell-oxillustrate-rs` renderer/API and CLI for native crop-origin metadata only;
  preserve its human-required unconditional trim behavior.
- `devel/capture_readme_visuals.py`, gallery README markup, and its focused checks for shared crop
  and alpha presentation behavior.
- Central animation and native/media tool guides, `docs/CHANGELOG.md`, `docs/HUMAN_GUIDANCE.md`,
  and `docs/DESIGN_DECISIONS.md` for the current contract, observed work, human-stated guidance,
  and decisions that have actually settled.
- `docs/active_plans/workstreams/atp_synthase_alpha.md` for task ownership and evidence status.
- Generated structures and media stay in ignored `output/`. Preserve original structures,
  historical gallery assets and prior verification receipts. Deliberately replace the current
  gallery presentation with newly named alpha assets and tighter framing; retain old files.

## Completion checks

- ATP synthase structure, assembly, selected components, omissions, and supported interpretation
  are documented from primary structural evidence.
- Native scenes keep one camera, canvas, and molecular scale. The cutaway and membrane band clarify
  the rotor/stator relationship without implying that the staged motion is measured.
- Decoded animated WebP contains real transparent pixels and displays correctly over light and
  dark backgrounds. Dimensions, duration, loop seam, reduced-motion poster, and browser playback
  are checked separately.
- The gallery uses a single union crop per animation. Contact sheets show steady protein scale and
  no clipping throughout motion. Hexokinase color changes only if the evidence supports them.
- Fresh-process replay reproduces the documented delivery from preserved inputs. Scientific
  preparation, coordinate fidelity, visual acceptance, media decoding, browser playback, and replay
  each have distinct recorded evidence.
- Specification review passes, then independent quality review passes, then integration review
  passes. Remaining suite failures are reported with their actual scope and are not attributed to
  this work without evidence.

## Constraints

Use the sibling native Rust CLI as the canonical Goodsell renderer. Keep dependency minimums open
ended and report observed versions without pins. Run graphics experiments sequentially on this Mac.
Do not launch Blender, add a general animation framework, or publish or commit as part of this work.

## Settled direction

- Select one complete 8DBU assembly, epsilon down: 22 protein chains and 36,917 atom rows.
  Rotate label chains G-R rigidly; keep head/stator and deposited ligands stationary. Preserve
  the experimental construct notes, missing regions and complete original coordinates.
- Disclose authored mechanical illustration against a frozen head. It is not a sterically
  validated catalytic trajectory and depicts neither kinetics nor chemical conversion.
- Define the stator front-wedge omission once in fixed coordinates. Keep the rotor complete,
  retain every uncut per-frame structure and save an omitted-identity manifest.
- Preserve native straight alpha. Add optional native crop-origin metadata and reconstruct fixed
  canvases; do not add a trim toggle, sentinel atoms or white-background chromakey.
- Use 640 x 480 GroEL, 360 x 540 hexokinase and accepted 480 x 720 ATP synthase previews.
  Display ATP at 360 pixels wide in the README. Fit one union across all 125 frames
  with fixed padding, scale and aspect; never resize each pose independently.
- Keep lossless WebP alpha and transparent posters. Composite MP4 and GIF explicitly onto white.
  Native-source alpha uses symmetric `--alpha` opt-ins and separate generated directories.
- Use the corrected determinant +1 ATP camera (`column = -local_x`), preserving molecular
  handedness. Reject the exploratory reflected view and regenerate every coordinate handoff.
- Set the alpha hexokinase surface opacity to 0.55 after light/dark comparison, retaining blue
  protein, magenta glucose, default opacity 0.42 and unchanged scientific preparation.

## Evidence checkpoint

Feasibility, implementation, full native source rendering, independent coordinate/native handoff
verification, full ATP media decoding and gallery capture are recorded in the
[atp_synthase_alpha.md](../active_plans/workstreams/atp_synthase_alpha.md) ledger. The corrected ATP delivery has
125 frames on one 480 x 720 canvas, with native render time 36.783 seconds and encode time
14.322 seconds. These are local observations. All 437 historical preserved files remain unchanged.
Three gallery loops each contain 60 frames, five seconds, real alpha and a reduced-motion poster;
two captures reproduce the six assets and README byte-for-byte.

[atp_synthase_playback.md](../active_plans/reports/atp_synthase_playback.md) records actual Chromium/Firefox
light/dark motion, reduced-motion posters, responsive layouts and actual Impress ATP MP4 playback
PASS. Exact displayed pacing, animated WebP in Impress and post-publication behavior are not claimed.
[atp_synthase_replay.md](../active_plans/reports/atp_synthase_replay.md) records local fresh-process PASS from
preserved inputs/prepared hexokinase trajectory: scientific handoffs, regenerated PNGs, ATP encoded
media, six gallery assets, README and capture manifest reproduce byte-for-byte. Timing fields,
appended logs, generated Mol* saved state and independent diagnostics are separately classified;
whole-tree byte identity and clean-install/cross-platform portability are not claimed.

## Accepted closeout

The manager accepts the completed outcome after fresh ordered
[specification](../active_plans/reports/atp_synthase_specification.md), independent
[quality](../active_plans/reports/atp_synthase_quality.md) and
[integration](../active_plans/reports/atp_synthase_integration.md) PASS reviews on 2026-11-12.
The temporary gallery check and QA directory are removed after confirming durable evidence in
ignored `output/atp_synthase_checks/` and the reports. Permanent geometry and real-codec checks remain.
This plan is archived with `git mv`; product source, README, media and native binary stay frozen.
The broad suite's recorded 1,164 passed, one skipped and two failures remain historical counts;
the later five-check naming PASS does not establish a fresh green full suite. The unchanged Unicode
baseline, unpublished GitHub assets and local same-host replay limits remain disclosed.
