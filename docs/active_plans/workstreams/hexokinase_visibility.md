# Hexokinase visibility follow-up

Status: complete; manager accepted; products frozen.

## Approved request

The user says the current hexokinase protein is too transparent to see movement and asks to
"tweak it a bit". Make the protein more opaque so closure is clearer. Preserve the transparent
background, magenta glucose, camera, crop, timing and structural coordinates.

## Scope and provenance

Change the current Mol* surface opacity and refresh only the hexokinase gallery loop and poster.
Preserve original scientific inputs, prepared structures, historical full-quality outputs, README
and four ATP/GroEL gallery assets. Existing prior work remains intact. The completed earlier
workflow is [atp_synthase_alpha.md](../../archive/atp_synthase_alpha.md); its 0.55 observations
remain dated evidence. This follow-up supersedes only the current hexokinase appearance.

Evidence is under ignored `output/hexokinase_visibility/`. `protected_before.json` records 152
protected files. `before_render.json`, `before_imported_coordinates.json`, `before_scene.molj`
and `before_capture_manifest.json` retain the current camera, identity, coordinate and crop evidence.
Native probes use copied existing rendering code, changing only opacity, output path and sampled
frames 0, 31 and 62. Candidate opacities are 0.55, 0.75 and 0.85.

## Selection

The manager inspected `opacity_comparison_q90.webp` and selected 0.75. It gives firmer blue
lobes than 0.55 while retaining a faint closed-state glucose trace; 0.85 adds less definition and
nearly hides glucose. One shared 0.75 protein opacity applies to both background modes; `--alpha`
selects background/output only. Historical opaque files stay intact. The quality-90 comparison
contains native frames 0, 31 and 62 over white and dark backgrounds; sparse motion probes use
those actual frames in open/middle/closed/middle order and are not final motion/timing evidence.
All probe imported protein coordinates, atom keys and fixed 12-atom ligand match the prior record.

## Actual checks

- Rules and current renderer/gallery source read. No new dependencies or permanent tests.
- Initial sandboxed Chromium startup failed at macOS Mach-port bootstrap; authorized native
  Chromium probes run outside that sandbox. No product workaround was added.
- Full native Mol* render completes in 90.811 seconds: 125 RGBA frames, 640 by 640, saved native
  state at opacity 0.75 and updated render record. The imported-coordinate JSON is byte-identical
  to the previous record, including atom keys, sampled protein coordinates and fixed twelve-atom
  glucose. Every render field except elapsed time matches, including the fixed orthographic camera.
- Existing capture helper regenerates the gallery. Crop stays `[190, 74, 497, 531]`; hexokinase
  stays 360 by 540 with 60 frames, exactly 5000 ms and infinite loop count 0. Every native/gallery
  frame and the static poster contain alpha-zero background and partial alpha. The poster has
  one frame and matches the new opening appearance.
- All 152 protected file hashes remain unchanged: original inputs, complete historical hexokinase
  outputs, README and four ATP/GroEL gallery assets. The other two capture records are exact.
- Inspect native open/middle/closed/reopening/seam contact sheet and actual Chromium captures over
  white and dark backgrounds. The protein silhouette and lobe displacement are clearer at 0.75.
  Magenta glucose is bright open, partially occluded midway and a faint purple trace closed; no
  geometry, ligand pose or visibility trick changes.
- Actual Chromium 158.0.8127.18 playback samples run through 6500 ms on both backgrounds; images
  continue changing after the first loop. Reduced-motion uses the matching poster, whose six
  samples remain identical through 6500 ms. No browser page errors. See `playback.json` and
  `playback_contact_q90.webp`. This is local Chromium evidence, not Firefox or Impress playback.
- Node syntax, ESLint and Prettier pass. Markdown links pass 96 cases; scoped documentation is
  ASCII and working-tree whitespace checks pass. No new permanent tests, full-suite run,
  scientific re-preparation, Blender launch or historical opaque rerender.

## Commands and frozen assets

Run from the repository root:

```bash
node examples/render_molstar.mjs hexokinase_closure --alpha
source source_me.sh && python3 devel/capture_readme_visuals.py
source source_me.sh && python3 output/hexokinase_visibility/verify.py
node output/hexokinase_visibility/playback.mjs
node --check examples/render_molstar.mjs
npx eslint examples/render_molstar.mjs
npx prettier --check examples/render_molstar.mjs
source source_me.sh && python3 -m pytest -q tests/test_markdown_links.py
git diff --check
```

Native Chromium commands use the authorized unrestricted lane because macOS denies browser
Mach-port bootstrap in the sandbox. Probe commands are the same native rendering harness under
`output/hexokinase_visibility/probe_0.55.mjs`, `probe_0.75.mjs` and `probe_0.85.mjs`, each called
with `hexokinase_closure --alpha`. `verification.json`, logs and source frame hashes retain checks.

Current gallery assets (SHA256):

- `hexokinase_closure_alpha.webp`: 2563976 bytes;
  `f8bb1afeea04b5d1368c7e44eaf0c47b947885649db3352a651cb066477fdb40`.
- `hexokinase_closure_alpha_poster.webp`: 29882 bytes;
  `470635620b360ff08185e300f139047be2db70d8877403d1666892e03aa99460`.

The concatenated 125-frame source SHA256 is
`fe7d7e2dbd9c6ba6b23f32c0df41929e1d45a92265ae60105aa3bac21e3c96e8`.
`frozen_products.json` records current code, documentation and asset hashes for review.

## Review handoff

- Specification review: PASS ([report](../reports/hexokinase_visibility_specification.md), Luna medium).
- Independent quality review: PASS ([report](../reports/hexokinase_visibility_quality.md), Luna medium).
- Integration review: PASS ([report](../reports/hexokinase_visibility_integration.md), Luna low).
- Implementation: Sol medium. Manager accepted closeout after all three fresh reviews passed.
- Final check: all six source and asset hashes still match `frozen_products.json`; the 152-file
  protected set remains unchanged. No source or asset was modified for this closeout.
