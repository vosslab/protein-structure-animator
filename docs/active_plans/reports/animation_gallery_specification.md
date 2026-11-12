# Animation gallery specification review

## Verdict

2026-11-12: PASS. The frozen README gallery meets the approved scope and the later fixed-aspect
correction. No specification finding blocks the next review.

## Scope checks

- [README.md](../../../README.md), lines 10-70, places the existing GroEL loop first and the
  existing Mol* hexokinase loop second, then labels three 3N0G images as static appearance choices.
  The original quick start remains below the gallery.
- The clips use one canvas each: GroEL is 640 x 360 (16:9); hexokinase is 360 x 780 (6:13),
  displayed at 240 pixels wide. The capture helper preserves proportions, downsizes without
  enlargement, uses one crop for the hexokinase frames, and rejects crop loss. No alternate aspect
  versions are generated.
- README markup uses native `picture` elements with reduced-motion poster sources, linked preview
  images, selectable captions, ordinary poster links, and reproduction links. The managed
  screenshot sentinels remain intact.
- The captions distinguish viewpoint rotation from protein folding and describe hexokinase as an
  induced-fit teaching illustration with a staged glucose pose, not a measured binding path or
  catalytic cycle. The appearance row identifies the Rust canonical still and both Mol* choices.
- No new website, JavaScript, configuration schema, renderer invocation, or ignored `output/` link
  appears in this README implementation.

## Evidence and limits

I independently inspected the current README, helper, active plan, workstream ledger, and capture
and browser records. Current SHA-256 values match the frozen correction receipt: README
`1c8cc379a46e60b644c3734bd3881616b6886fbbaf960ec76b9be44394d5df71`; capture helper
`3c31f89300d7a189cb8663d5f2ec6301146000ae87336a444abf36c6240b007e`. The four preview/poster
hashes also match the capture and browser receipts.

The capture receipt reports two byte-identical final captures, unchanged source frames and
full-quality exports, and correct dimensions, frame counts, timing, loop metadata, and static
posters. The browser receipt reports natural repeated playback and reduced-motion poster selection
at desktop and narrow widths. Its correction addendum records fresh GitHub Markdown sanitation and
caption layout checks after the earlier caption findings were corrected. These are prepublication
checks: the gallery has not been published or checked on the newly published repository README.
I relied on those recorded media/browser experiments and did not rerun them.

The recorded full Python suite result is 1,109 passed, 1 skipped, and 1 failure: the unchanged
`docs/active_plans/protein-deep-research-report.md` contains 196 non-ISO-8859-1 characters. This
existing failure does not indicate a gallery specification mismatch.
