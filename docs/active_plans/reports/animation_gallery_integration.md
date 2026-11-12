# Animation gallery integration review

## Verdict

2026-11-12: PASS. The frozen README, capture helper, media records and prior reviews compose into
the approved gallery. No integration finding blocks manager closeout and archival.

Reviewer: `animation_gallery_integration`, gpt-6-luna, high. This is a fresh cross-document and
scope review; it does not replace the specification, quality, capture or browser checks.

## Coverage

- The README leads with the existing canonical Rust GroEL loop, then the existing Mol* hexokinase
  loop, followed by three explicitly static 3N0G appearance choices. The quick start remains below.
- Each animation has one fixed canvas: 640 x 360 (16:9) for GroEL and 360 x 780 (6:13) for
  hexokinase, shown at 240 pixels wide. Captions, previews and matching posters follow the same
  ratios; no square variant, stretch or aspect change appears.
- The helper uses existing 125-frame sources, validates every frame and crop bounds, samples 60
  frames, and writes quality-90, five-second, infinite WebP loops with matching static posters.
  It does not invoke a molecular renderer. The README continues to distinguish these presentation
  previews from 640-square full-quality deliveries.
- GitHub-native `picture` markup selects the poster for reduced motion; preview images have
  descriptive alt text, and each poster has a separate link. Captions remain selectable text.
- Scientific wording identifies GroEL as a viewpoint rotation with no folding cycle. Hexokinase is
  an induced-fit teaching illustration using interpolated protein endpoints and a fixed staged
  glucose pose, not a measured binding path or catalytic cycle. The static row labels all three
  rendering choices and links to their example guide.
- Reproduction and image links use repository-relative paths. The three example README targets are
  tracked; the four new WebPs reside in `docs/screenshots/`, outside ignored `output/`. Those WebPs
  are currently untracked pending normal closeout, so they must remain in the human-review patch.

## Evidence and limits

I read the approved [plan](../../archive/animation_gallery.md) and
[animation guidance](../../ANIMATION_GUIDANCE.md), the final [README](../../../README.md) and
[capture helper](../../../devel/capture_readme_visuals.py), the
[workstream ledger](../workstreams/animation_gallery.md), and the
[capture](animation_gallery_capture.md), [browser](animation_gallery_browser.md),
[specification](animation_gallery_specification.md) and [quality](animation_gallery_quality.md)
reports. The implementation and corrections match the settled D1-D4 decisions. The reports provide
the final README hash, repeated-capture hashes, unchanged source and full-quality media hashes,
decoded dimensions/timing/loop/poster checks, and corrected GitHub-sanitized desktop/narrow
rendering. The quality reviewer independently checked all 250 source frames, media metadata and 77
focused cases. I did not repeat those media, browser or focused-test experiments.

The recorded full Python run is 1,109 passed, 1 skipped and 1 failure in an unchanged research
report with 196 non-ISO-8859-1 characters. This is unrelated to the gallery; this review did not
rerun the suite. The new gallery remains unpublished. No actual iPhone/Safari, Impress, molecular
rerender or newly published README acceptance is claimed. The ledger's pending-review and temporary
check cleanup entries are manager-owned closeout bookkeeping, not missing integration evidence.

## Handoff

Proceed with ledger reconciliation, review-file archival and removal of the two disposable checks
under `tests/_temp/` according to the approved plan. Keep the new gallery WebPs in the reviewable
patch. No product correction or extra validation gate is recommended.
