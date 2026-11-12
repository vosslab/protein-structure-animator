# Oxillustrate integration plan

Approved scope: make sibling `goodsell-oxillustrate-rs` the canonical renderer and visual gold
standard for Goodsell figures and animations. Implement the 3N0G still and complete GroEL
rotation first. Mol* remains for surfaces and interactive work; existing hexokinase work stays
unchanged. Adoption is settled human direction, distinct from capability verification.

Completed and accepted 2026-11-12 after fresh specification, independent quality and integration
reviews. This archived plan records the implemented initial scope; see the
[execution ledger](../active_plans/workstreams/oxillustrate_integration.md) for actual evidence and limits.

## Native implementation

- Build the current sibling checkout and invoke its native CLI; use the sibling release binary
  by default with an explicit `--illustrate` override. Record observed revision, dirty source,
  binary hash and version, without requiring a fixed revision.
- Preserve original mmCIF inputs and hashes. Keep the same 3N0G selections, visible ligands and
  comparable view. Use native JSON for orientation, rules and explicit framing.
- Render all 14 GroEL chains and 53,858 protein atoms from deposited assembly 1 of 1OEL without expanding
  it twice. Produce 125 distinct frames at 640 x 640, white background, 25 fps and five seconds.
  Rotate the viewpoint once with a fixed origin and scale; exclude a duplicate 360-degree endpoint.
- Check current source framing semantics. Current `scene_preparation.rs` subtracts `framing.center`;
  earlier additive descriptions are stale. Maintain depth-safe bounds and consistent shading.
- Retain native per-frame JSON scenes, logs, source provenance, settings and small source previews.
  Generated media and structures stay under ignored `output/`.
- Keep the external binary external. Its source is AGPL-3.0-only and its documentation CC-BY-4.0;
  preserve historical Fortran attribution without requiring that compiler for the default route.
- Add no bindings, shared framework, automatic fallback or Blender dependency. Expose an upstream
  gap through a bounded reproducer. Do not claim a Rust hexokinase trajectory.

## Observable completion checks

1. Inspect native scene support and selection/framing semantics; record current-source evidence.
2. Implement the smallest native CLI examples and meaningful focused geometry checks. Render the
   still and GroEL serially; inspect ligands, assembly, bounds, contours, depth and teaching-size
   readability. Record actual timing and resources.
3. Independently verify unchanged inputs, selected atom identities/counts, rotation geometry,
   fixed framing and native scene replay. A rotation is a viewpoint change, not conformational
   dynamics.
4. Encode MP4, GIF and animated WebP. Check decoding, frame count/durations, dimensions, loop seam,
   real browser motion and real MP4/Impress playback separately. Previous Mol* playback evidence
   does not establish playback of these outputs.
5. Replay documented commands in fresh processes, retaining evidence and limits. Refresh README
   first success and visuals to match executed commands and actual media; no fresh-install claim
   without fresh installation evidence.
6. Obtain a fresh specification review, a different quality review and a fresh integration review.
   Update the ledger with actual verdicts. Keep this plan active until acceptance and authorized
   closeout; historical plans and reports retain their original scope.

## Coordination

The manager delegates file ownership. Serialize graphics on this Mac. Use Sol for implementation
and readable evidence review; use Luna for prose/specification work when assigned. Keep one compact
[execution ledger](../active_plans/workstreams/oxillustrate_integration.md) with owners, dependencies, questions,
settled decisions and report links. Challenge consequential uncertainty before claiming acceptance.
