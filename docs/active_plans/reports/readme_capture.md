# README capture verification

## Current capture

Captured 2026-11-12 at 06:38:16 UTC; repeated at 06:39:01 UTC with byte-identical assets
and README content. The user requested animated WebP instead of GIF for the README motion
preview. This overrides the screenshot skill's GIF recipe for this asset only. Full native
example GIF exports are unchanged.

Classification: a visual CLI artifact/tool collection. The examples produce molecular
images directly; capture shows their results without inventing an application interface.
Storyboard: start with open hexokinase, show interpolated closure around fixed glucose,
and finish reopened after one five-second play. A separate still compares both hexokinase
endpoints with complete fourteen-subunit GroEL. These are annotated authentic Mol* render
frames: empty margins are cropped and pixels reduced where needed; molecular imagery is
never enlarged, redrawn, or simulated by the capture helper.

## Assets and provenance

| Managed asset | Dimensions | Encoding | Size |
| --- | --- | --- | --- |
| `docs/screenshots/hexokinase_closure_demo.webp` | 960 x 600 | Pillow quality 90, 54 encoded frames, 5,000 ms, one play | 1,228,594 bytes |
| `docs/screenshots/protein_examples.webp` | 1280 x 800 | cwebp quality 90 | 95,118 bytes |

Both canvases are 16:10 and their longest edges stay below 1920 px. The animated asset
is below the inherited five-MiB motion budget; the static asset is below one MB.
The preview is 1,864,606 bytes (60.3%) smaller than its superseded 3,093,200-byte GIF.

The helper composes 60 RGB samples on a 12 fps timeline and encodes them directly with
Pillow 13.0.0, without a GIF, palette conversion, or transient video. WebP coalesces
identical endpoint-hold samples into 54 encoded frames: first and last delays are 333 ms;
the 52 interior delays are 83 or 84 ms. Total duration is exactly 5,000 ms. The ANIM loop
field is 1, meaning one play; Chromium stopping behavior was checked separately. It samples
the 125-frame hexokinase source with brief endpoint holds; it is a reduced-rate preview
of the 25 fps source, whose full timing and distinct-frame count are stated separately.

Sources: existing 125 native 640 x 640 frames in `output/hexokinase_closure/frames/`
and freshly reproduced `output/groel_rotation/frames/frame_000.png`. The README refresh
replayed GroEL's renderer and encoder before releasing its frame for capture. Hexokinase
frames were inspected and reused; capture did not repeat preparation or rendering.
Original structural inputs and example output files were unchanged by capture.

SHA-256 provenance checksums:

```text
hexokinase PNG bytes concatenated in frame_000..frame_124 order:
a0fe37c9b380e94abf2a920f576586f380a02f90e607ab84de90d96d996fc5de
GroEL frame_000.png:
21f0a6e38ca5129b1f0ee9cd26a31427682d0e648c23cee709317ac5d2fee011
hexokinase_closure_demo.webp:
d6a0fd11e0cd2112303526945eec68011aac1e091d2fff3431dcca90d3de4b74
protein_examples.webp:
f7fbf515256c22ad043ff9e29d98ea8aec449a78a82a6046c0ff3be3bd94c603
```

## Rerun and checks

The self-contained [capture_readme_visuals.py](../../../devel/capture_readme_visuals.py)
uses declared Pillow with WebP support plus installed cwebp, keeps temporary files in
`/tmp`, copies only final assets into the managed folder, and replaces only the README
screenshot sentinel interior. Repository discovery uses `git rev-parse --show-toplevel`
from the helper's directory. Run after reproducing the documented examples:

```bash
source source_me.sh && python3 devel/capture_readme_visuals.py
source source_me.sh && python3 -m pyflakes devel/capture_readme_visuals.py
source source_me.sh && python3 -m pytest tests/test_function_typing.py tests/test_import_dot.py tests/test_import_requirements.py tests/test_markdown_links.py tests/test_readme_first_paragraph.py -q
```

- PASS: repeat capture preserved complete README bytes and both asset checksums. Missing,
  duplicated, and reversed sentinels were rejected. Source files, dimensions, cwebp, and
  Pillow WebP support are checked before writing assets.
- PASS: a disposable assert check under `tests/_temp/` verified every source frame's
  nonwhite content fits the crop, image budgets, WebP dimensions, frame count, loop field,
  per-frame delays, exact total duration, motion, static fallback, canonical root, and
  malformed sentinel handling. It was removed after the current-run checks.
- PASS: final animated WebP first/middle/final frames inspected at full size; the animated
  and static assets were inspected in an ephemeral rendering of the actual README
  screenshot section at 880 px image width. Reopened final state and fixed glucose remain
  visible. Encoding is lossy; decoded opening and final pixels need not be identical.
- PASS: Chromium 158.0.8127.18 screenshots differed at opening versus approximately
  2.2 seconds; screenshots at approximately 5.5 and 6.1 seconds were byte-identical.
  This establishes motion and stopping separately from container metadata.
- PASS: a second browser context activated `prefers-reduced-motion: reduce`; the WebP
  still animated, the static comparison loaded at its 1280 px native width, and equivalent
  interpolation/viewpoint prose remained present. Ordinary Markdown image embeds do not
  automatically honor the preference; the neighboring still and prose explain the result.
- PASS: direct pyflakes and syntax compilation; 201 typing/import/local-link/README
  checks; all six changed text files pass ASCII compliance; diff whitespace checks pass.
- Prior baseline observation: the broader pyflakes/ASCII command yielded 159 passes and
  one failure for existing non-ISO-8859-1 characters in the untouched
  `docs/active_plans/protein-deep-research-report.md`. No unrelated repair was made.

The exact sentinels survived; each interior line is a descriptive Markdown image embed
with a README-relative path. Alt text describes closure/reopening with fixed glucose,
and the static endpoint comparison beside complete GroEL. Adjacent prose identifies
experimental endpoint interpolation and viewpoint rotation separately, and states that
the hexokinase illustration establishes neither a binding path nor kinetics.

## Freshness and limits

Both current assets were captured and verified in this run. The static WebP is byte-identical
to its preceding capture. The superseded managed `docs/screenshots/hexokinase_closure_demo.gif`
was removed only after the new WebP passed visual, metadata, browser, and repeat checks and
its live README embed was updated. No live embed references the removed GIF. No `reference_`
assets exist. Dependencies were neither installed nor changed by capture; concurrent package
changes belong to separate work. Application implementation stayed read-only.

Playback evidence is local Chromium evidence, not live GitHub rendering or a new Impress
test. The earlier animated-WebP ODP-image embedding failure remains documented; this README
format change makes no new Impress claim. Structural fidelity and scientific preparation
retain the example verification record. The fixed crop requires review if the hexokinase
camera changes. A fresh dependency installation and full-suite baseline repair were skipped.
