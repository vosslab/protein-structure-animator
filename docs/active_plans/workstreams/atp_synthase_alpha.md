# ATP synthase and alpha WebP ledger

Plan: [atp_synthase_alpha.md](../../archive/atp_synthase_alpha.md). Human approval: "I like your ideas
do it." Implementation, science, visual acceptance, decoding, playback and fresh-process
reproduction are separate evidence. The manager accepts the completed outcome after fresh ordered
specification, independent quality and integration PASS reviews on 2026-11-12.

## Work status

Models reflect manager assignments; no model substitution is inferred from a report.

| Work | Owner | Assigned model/reasoning | State and evidence |
| --- | --- | --- | --- |
| Plan, ledger and central guides | `atp_alpha_docs_reconcile` | Sol / medium | Complete; current evidence and final QA/playback receipts reconciled |
| Science feasibility | `atp_structure_feasibility` | Sol / high | Complete; primary assembly/construct/motion evidence recorded |
| Native alpha/cutaway feasibility | `rust_alpha_cutaway_feasibility` | Sol / high | Complete; fresh native true-alpha and composite probes |
| Media/crop feasibility | `alpha_crop_pipeline_feasibility` | Sol / medium | Complete; full-motion union and native-alpha requirements |
| Encoder | `alpha_encoder_implementation` | Sol / medium | Complete; 125-frame real-codec proof and 641 focused checks |
| Sibling crop-origin metadata | `rust_crop_metadata` | Sol / high | Complete; 54 Rust and 1,017 Python checks reported; unconditional trim preserved |
| Existing alpha source helpers | `existing_alpha_preview_sources` | Sol / high | Complete; 125 GroEL and 125 Mol* alpha sources; 437 historical files unchanged |
| Corrected ATP native example | `atp_camera_correction_render` | Sol / high | Complete; proper camera, 250 coordinate handoffs, 125 scenes/frames and full media |
| Independent coordinate/native science | `atp_native_science_verification` | Sol / high | PASS; all ATP/GroEL native scenes and sampled hexokinase import |
| Gallery framing and presentation | `alpha_gallery_implementation` | Sol / high | Complete; six alpha assets, two identical captures and 100 focused checks |
| 3N0G scene compatibility | Compatibility worker | Luna / medium | Complete; obsolete trim key removed, historical assets retained |
| Repository checks | `atp_alpha_repository_checks` | Sol / medium | Complete; focused checks pass, cleanup naming gate 5 PASS; Unicode baseline remains |
| Actual browser and Impress playback | `atp_alpha_playback` | Sol / high | PASS; actual Chromium/Firefox motion, reduced posters and Impress ATP MP4 |
| Fresh-process replay | `atp_alpha_replay` | Sol / medium | PASS; scientific handoffs, PNGs, ATP media and gallery reproduce exactly |
| Independent specification review | `atp_alpha_specification` | Luna / high | PASS; [atp_synthase_specification.md](../reports/atp_synthase_specification.md) |
| Independent quality review | `atp_alpha_quality` | Sol / medium | PASS after specification; [atp_synthase_quality.md](../reports/atp_synthase_quality.md) |
| Independent integration review | `atp_alpha_integration` | Luna / high | PASS after quality; [atp_synthase_integration.md](../reports/atp_synthase_integration.md) |
| Closeout | `atp_alpha_closeout` for root manager | Sol / medium | Manager accepted; durable evidence confirmed, owned temporary checks removed, plan archived with `git mv` |

## Settled direction

- D1: Select complete 8DBU epsilon-down E. coli ATP synthase: 22 protein chains, 36,917 rows.
  Label chains G-R form the 8,772-row rotor; head/stator and all hetero rows remain stationary.
  Preserve construct notes and missing regions. Primary paper: DOI 10.1038/s42003-023-04414-z.
- D2: Use 640 x 480 GroEL, 360 x 540 hexokinase and 480 x 720 ATP preview canvases. Measure all
  125 sources for one union plus margins, including outlines/labels; keep scale and aspect fixed.
- D3: Preserve unconditional native trimming. `render_with_bounds` and optional CLI `--metadata`
  expose `{canvas:[W,H],crop_origin:[left,top]}`. Paste native RGBA at its true origin without a
  mask; reject obsolete `trim:false`. No trim toggle, sentinel atoms or chromakey.
- D4: Fix the stationary front-wedge cutaway in source coordinates; retain all rotor atoms,
  full per-frame coordinates and omission identities. Actual frozen-head overlaps are documented.
  Caption authored mechanical illustration, not a sterically validated trajectory, kinetics,
  catalytic cycle or chemistry. Membrane context is schematic; deposited ATP is not conversion.
- D5: Preserve WebP/poster alpha; composite GIF/MP4 onto explicit white. Synthetic RGBA equality
  does not imply native raw-RGBA identity under alpha zero: native ATP checks exact alpha, visible
  RGB and light/dark composites. Gallery quality-90 color is lossy, while alpha remains exact.
- D6: Symmetric `--alpha` opt-ins write separate GroEL/hexokinase directories, preserving opaque
  deliveries and historical assets. Light/dark comparison selects hexokinase alpha opacity 0.55;
  retain default 0.42, original colors, trajectory, camera and fixed glucose coordinates.
- D7: Use a proper ATP camera rotation, determinant +1, with `column = -local_x`. Reject the
  reflected exploratory camera and regenerate all 250 coordinate files and 125 scenes before
  rendering. The corrected side stalk appears on the left; molecular handedness is preserved.
- D8: Display the ATP 480 x 720 preview at 360 pixels wide in the README. Full-motion and
  teaching-size inspection supports its labels, membrane and exposed shaft; keep one aspect.

The abandoned `restore_rust_fixed_canvas` workstream made no edits. Crop metadata supplies
registration while honoring unconditional trim. No dependency, pin, Blender launch, framework,
commit or publication is in scope.

## Recorded evidence

- [atp_synthase_science_feasibility.md](../reports/atp_synthase_science_feasibility.md): primary
  records, original hashes, assembly, ligands, construct and missing-region inventory.
- [atp_synthase_renderer_feasibility.md](../reports/atp_synthase_renderer_feasibility.md): native
  alpha, cutaway and composite probes with distinct preexisting/fresh binary identities.
- [atp_synthase_media_feasibility.md](../reports/atp_synthase_media_feasibility.md): 125 synthetic
  frames and full-motion crop requirements.
- [atp_synthase_encoder.md](../reports/atp_synthase_encoder.md): exact synthetic decoded RGBA,
  white GIF/MP4, unchanged RGB comparison and 641 focused checks; not a full-suite result.
- [atp_synthase_existing_previews.md](../reports/atp_synthase_existing_previews.md): 125 frames per
  alpha source, current dirty native-source provenance and 437 unchanged historical files.
- [atp_synthase_render.md](../reports/atp_synthase_render.md): corrected camera, all handoffs,
  125 native/composed frames, full media, alpha/composite/seam checks and inspected proof sheets.
  Native rendering took 36.783 seconds and encoding 14.322 seconds. Media is 125 frames at 25 fps,
  five seconds, 480 x 720. Geometry checks live in `tests/test_atp_synthase_geometry.py`.
- [atp_synthase_science_verification.md](../reports/atp_synthase_science_verification.md): PASS
  for all 250 ATP coordinate files, all 125 scenes and 3,659,250 native selected spheres, with
  zero native projection error; all GroEL native scenes and sampled hexokinase handoffs pass.
  This does not establish collision-free motion or biological activity.
- [atp_synthase_gallery.md](../reports/atp_synthase_gallery.md): three 60-frame loops, 5,000 ms,
  loop 0; all 183 decoded frames/posters preserve exact source alpha. Two captures reproduce six
  new assets and README; 100 focused checks pass. README SHA-256 is
  `3c0eec7e0cec82da3758fb30a62253ad86e942b324b1e8895623418bac45aa42`.
- [atp_synthase_checks.md](../reports/atp_synthase_checks.md): focused source/codec checks pass;
  broad run records one known baseline and one transient temporary-probe failure; after owner
  cleanup, the affected naming gate passes all five checks. No task-related failure remains.
  Logs and the read-only switch plugin are preserved in `output/atp_synthase_checks/`.
- [atp_synthase_appearance_compatibility.md](../reports/atp_synthase_appearance_compatibility.md):
  obsolete 3N0G trim key removed; declared canvas differs from current trimmed CLI dimensions.
  Historical assets remain unchanged; no new still render is claimed.

## Playback and replay

[atp_synthase_playback.md](../reports/atp_synthase_playback.md) records actual playback PASS:
Chromium desktop/narrow and Firefox desktop cover light/dark and normal/reduced motion. All
18 normal clip cases show seven distinct RGB captures beyond five seconds; all 18 reduced-motion
cases remain static on the correct posters. Actual browser alpha-zero/opaque pixels match exactly;
partial-alpha compositing differs only by measured rounding. There is no horizontal overflow.

Actual LibreOffice 26.2.7.3 ATP MP4 slideshow captures show eight distinct rotor crops over
7.176 seconds against the stationary housing; the embedded MP4 hash matches. The owned process
exited and its temporary profile was removed. This establishes visible playback, not exact pacing,
Firefox narrow layouts, animated WebP in Impress or newly published GitHub behavior.

[atp_synthase_replay.md](../reports/atp_synthase_replay.md) records preserved-input local replay
PASS. All 377 ATP prepared files, 375 native/restored/composed PNGs, four ATP media/poster files,
125 GroEL PNGs/scenes/bounds each, 125 hexokinase alpha PNGs and imported coordinates reproduce
exactly. Six gallery assets, README and capture manifest reproduce exactly; historical 437-file
and 21-entry manifests remain unchanged. Fresh preparation took 137.12 seconds; native ATP render
35.704 seconds, encoding 13.615 seconds, GroEL 53.397 seconds and Mol* 82.13 seconds.

Of 1,483 baseline files, 1,475 match byte-for-byte. Three render records differ only in elapsed
time; a native log appends; Mol* generates a fresh saved state; three independent diagnostic files
are excluded from the replay product claim. Full old/new Mol* state JSON equality is not claimed.
The exact molecular delivery is established by PNGs, imported coordinates, camera/render metadata
and unchanged source. Replay uses the preserved hexokinase trajectory, without rerunning ChimeraX,
rebuilding native tools or establishing clean-install/cross-platform reproduction.

## Baseline and acceptance

Historical gallery/native integration receipts remain valid for their recorded sources and media,
including the old disabled-trim contract. They do not establish current-source compatibility.
The fresh broad Python run records 1,164 passed, 1 skipped and 2 failures: the HEAD-identical
research-report Unicode issue and a temporary browser probe naming issue. After its owner removed
the probe, the affected naming gate passed all five checks. No full-suite rerun or full-green claim
is inferred. Final QA report/logs are preserved; focused source and real-codec checks found no
product defect. Documentation ASCII, whitespace and direct links pass for all eleven owned files;
94 focused Markdown/guidance checks pass.

Ordered independent specification, quality and integration reviews pass; the root manager accepts
the implementation. Closeout removes only `tests/_temp/test_atp_synthase_gallery.py` and
`tests/_temp/atp_synthase_checks/` after comparing every QA log/plugin byte to its durable copy in
`output/atp_synthase_checks/` and the temporary report to the durable QA report. Permanent
`tests/test_atp_synthase_geometry.py` and `tests/e2e/e2e_encode_alpha.py` remain. The archived plan
and existing geometry regression are the only staged paths; no commit or publication is made.

Closeout verification passes 108 Markdown-link, README-opening, guidance-format and naming checks.
Eight closeout documents pass ASCII and whitespace checks; working-tree and cached diff checks pass.
The frozen README, six gallery assets, native executable and eight replay helpers retain their
recorded SHA-256 values. These are read-only checks, with no new render, capture or full-suite run.

## Related records

- [ANIMATION_GUIDANCE.md](../../ANIMATION_GUIDANCE.md)
- [animation_gallery.md](animation_gallery.md)
- [oxillustrate_integration.md](oxillustrate_integration.md)
- [oxillustrate_science.md](../reports/oxillustrate_science.md)
