# Existing alpha preview sources

## Scope and inputs

The existing GroEL and hexokinase examples gain separate transparent presentation source frames.
Historical scientific preparation and full deliveries remain in their original output directories.
The source-frame canvas stays 640 by 640; the gallery owner applies a fixed full-loop union crop
and the agreed 4:3 GroEL and 2:3 hexokinase presentation canvases.

Both renderers accept `--alpha`, selecting `output/groel_rotation_alpha/` or
`output/hexokinase_closure_alpha/`. The default routes keep opaque backgrounds; hexokinase's
default surface opacity remains 0.42. No new dependency, structural preparation, atom selection,
morph, camera change or original-input edit is introduced.

The pre-render manifest `output/existing_alpha_preservation_before.json` records SHA-256 for 437
historical files across `output/inputs/`, `output/groel_rotation_oxillustrate/` and
`output/hexokinase_closure/`. These include deposited inputs, prepared coordinates, native scenes,
saved states, full-resolution frames and encoded deliveries.

## Native crop registration

Current Rust rendering trims unconditionally. The helper drops obsolete `trim` from its scene,
requests CLI `--metadata`, and copies native straight RGBA at the reported `crop_origin` onto the
reported 640 by 640 canvas. It uses no mask, scaling, fake atoms or background removal. The helper
checks canvas dimensions and crop containment before writing. Its opaque route restores RGB.
Per-frame native metadata stays beside the effective scene as `frame_*_bounds.json`.

Observed renderer: `illustrate 26.11.0`, sibling HEAD
`6e7736a746efcde1ed65cea965aae86cbc8dfcee` with uncommitted crop-registration work. The binary SHA-256
is `ac4c51ab1f3e27e16b7ce888f4c8eb462b263249b310bf6f6d840b30934ba91f`.
It was built with `cargo build --locked --release`, rustc/cargo 1.99.1, aarch64-apple-darwin.
`output/groel_rotation_alpha/provenance/` preserves the source inputs, status and patch;
patch SHA-256 is `d9df6268257c9dc5716ad327f2e4a3f3bdb303cbdcf83a112a62f61bc4eb9903`.
The new native revision may differ visually from the historical renderer; that historical
appearance and its original provenance remain preserved.

## Hexokinase contrast decision

Two fresh native Mol* one-frame probes compare surface opacity 0.42 and 0.55, keeping the same
blue and magenta colors, camera, coordinates and twelve-atom fixed glucose. The retained
`output/hexokinase_closure_alpha/probes/comparison.webp` shows both over white and dark gray.
Manager visual review approved 0.55 for the alpha variant: blue lobes are more defined on both
backgrounds and magenta glucose remains readable. The default route retains 0.42.

The first sandboxed Chromium launch failed at native MachPort startup. The authorized command
then succeeded outside the sandbox. This is runtime access evidence, not a rendering-code fix.

## Commands and checks

Run from the repository root after preparing the original examples:

```bash
source source_me.sh && python3 examples/groel_rotation/render_oxillustrate.py --alpha
node examples/render_molstar.mjs hexokinase_closure --alpha
```

Completed pre-render checks: Node syntax, Prettier, ESLint, Python pyflakes, existing fixed-rotation
geometry test and an exact-RGBA reconstruction check with transparent, partial-alpha and opaque
pixels at a nonzero crop origin. No whole-suite result is implied.

## Full source-frame results

Both commands completed in fresh native processes: GroEL took 54.269 seconds and Mol* took 81.871
seconds. Observed Mol* 5.13.1, Playwright 1.65.0 and Chromium 158.0.8127.18. Both output directories
contain 125 distinct RGBA PNGs at 640 by 640. Every frame has transparent border pixels and real
partial alpha; none touches the canvas edge.

| Source | Full-loop alpha bounds, exclusive right/bottom | Alpha levels | Partial-alpha pixels/frame |
| --- | --- | --- | --- |
| GroEL | 31, 40, 607, 586 | 6 | 1,763-2,117 |
| Hexokinase | 200, 84, 487, 521 | 250 | 77,155-80,831 |

`output/existing_alpha_source_checks.json` retains the all-frame checks and SHA-256 manifests;
each output also has `source_frames_sha256.json`. Source scripts and settings, package versions,
and hashes are retained under each output's `provenance/` directory. All 437 historical-file
hashes still match the before manifest.

All 125 effective GroEL scenes match their historical counterparts exactly after removing the
obsolete `trim: false` and comparing `background: null` against the previous white background.
Orientation, framing center, scale, depth, outlines, shadows, selection and fog settings match.
The original assembly SHA-256 remains
`fb61ff7da5bafbd92f95a85876616cf5b7d43f8219af4260c81db295aa4ca49d`.
The input check retains fourteen chains and 53,858 protein atoms, omitting the same 298 waters.
This is source/settings preservation evidence; fresh native parser/geometry verification has a
separate owner.

Hexokinase's exported imported-coordinate record matches the historical record exactly, including
all atom keys, sampled positions at frames 0, 31, 62, 93 and 124, and the fixed twelve-atom glucose.
The native Mol* camera also matches exactly. The unchanged prepared trajectory still has 125
frames and 3,651 protein atoms per frame. Structural preparation was not rerun.

Manager inspected the full-phase light/dark sheet at
`output/hexokinase_closure_alpha/source_contact_sheet.webp` and accepted opacity 0.55. Closed-phase
glucose is less saturated but remains visibly identifiable as purple. A measurement counted 7-891
strong-magenta pixels across the frames; an initial arbitrary ten-pixel threshold was discarded
because saturation is not an atom-presence test. The scientific ligand record remains identical.
GroEL's corresponding `source_contact_sheet.webp` shows all five sampled orientations over light
and dark backgrounds. These are still-image observations, not live playback evidence.

Final focused checks passed: Node syntax, Prettier, ESLint, pyflakes and two Python checks (existing
rotation geometry plus temporary exact-RGBA canvas reconstruction). Temporary checks and probe
source copies were removed after recording their observations. No full suite was run here.

The graphics slot is released and the source directories are ready for gallery capture. Browser
playback, encoded-alpha verification, a second fresh-process replay and independent scientific
and quality reviews remain separate workstreams. Historical playback evidence is not reused as
acceptance for these new transparent sources.
