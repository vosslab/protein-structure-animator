# Toolbox verification

This report separates capabilities present in source, capabilities demonstrated by the current
examples, and capabilities reproduced from documented inputs in a fresh process. A render or
successful encode does not establish browser playback, Impress playback or reproducibility.

## Acceptance status

| Capability or check | Status | Evidence |
| --- | --- | --- |
| Native preparation and rendering examples | Demonstrated | Source and example guides cover three examples; see the structural and render reports below. |
| 3N0G appearance comparison | Demonstrated | [Render delivery](render_delivery_verification.md) records the Illustrate, Mol* sphere and surface comparisons and retained previews. |
| Hexokinase coordinate handoff | Demonstrated | [Structural verification](structural_verification.md) confirms 3,651 protein identities in all 125 frames, glucose registration, and imported identity/coordinate fidelity. |
| GroEL complete-assembly rendering | Demonstrated | [Structural verification](structural_verification.md) confirms all 14 protein chains and imported atom identities; [render delivery](render_delivery_verification.md) reviews the final rotation. |
| Final 640 x 640 render delivery | Demonstrated | All final 3N0G, hexokinase and GroEL PNG frames and encoded media were measured after corrected fresh renders. |
| Browser playback | Demonstrated | Chromium 158 and Firefox 159 played and looped MP4, GIF and WebP media for both animations. |
| Impress slideshow playback | Demonstrated for GIF and MP4 | [Impress verification](impress_verification.md) records visible motion for both formats in both examples. Animated WebP embedded as an ODP image produced blank, unchanged areas in this LibreOffice installation. |
| Fresh-process replay of both animations | Demonstrated | Final hexokinase and GroEL renders and encodes replayed from documented commands; native Mol* scene restoration was checked in fresh viewers. |
| M4 documentation and reproduction acceptance | Complete; specification, quality and integration reviews PASS | Fresh replay, browser playback and Impress GIF/MP4 playback are recorded. The plan is archived after manager-authorized closeout. |

The documented hexokinase preparation has been replayed in a fresh ChimeraX process. All 125 x
3,651 x 3 coordinate values match the pre-replay output exactly. This reproduces structural
preparation, not both finished animations or their application playback.

## Documentation checks

Earlier focused README, guidance-format and verification/ledger/review Markdown-link checks passed:
20 passed, 39 deselected. Final closeout ran the complete Markdown-link, README-first-paragraph and
guidance-format test files: 60 passed. `git diff --check` passed. A broader repository run reported
938 passed, 1 skipped and 3 failed. Two transient Markdown-link failures occurred before pending
reports existed; their targeted rerun passed after the reports landed (`2 passed, 48 deselected`).
The remaining failure is
the repository ASCII check on 196 Unicode citation-marker characters in the pre-existing
[protein deep research report](../protein-deep-research-report.md), unchanged from `HEAD`. This is
not a full-suite pass.

## Evidence reports

The reports below provide detailed evidence. Render, browser and supported Impress playback evidence
is complete; exact timings, output sizes and application limits are in the owner reports.

- [Structural verification](structural_verification.md): native structure preparation, atom and
  coordinate fidelity, scientific selections and limits, including final Mol* atom-identity and
  fixed-glucose import comparisons.
- [Render delivery verification](render_delivery_verification.md): rendered outputs, visual review,
  media decoding, browser playback and fresh-process replay.
- [Impress playback verification](impress_verification.md): actual GIF and MP4 slideshow playback
  passed; animated WebP as an ODP image shape showed a route-specific blank area.
- [Dependency verification](dependency_verification.md): current TypeScript floor, lockfile refresh
  and verified compiler/lint runtime split, with the full shell-gate limitation recorded.
- [Screenshot dimensions fix](screenshot_dimensions_fix.md): native viewport correction and measured
  640 x 640 3N0G output; all examples were freshly rendered at final dimensions in the render report.
- [Specification review](specification_review.md): PASS within the recorded scientific and
  application limits.
- [Quality review](quality_review.md): PASS with no actionable code or documentation quality
  findings.
- [Integration review](integration_review.md): PASS with no actionable integration gap; accepted
  M1-M4 and authorized final cleanup and archival.

## Known limits

- ChimeraX 1.10.1 wrote repeated coordinates for the tested multi-model mmCIF export. The checked
  PDB trajectory preserved the selected atoms and motion; original mmCIF inputs remain preserved.
- Hexokinase staging places closed-state glucose in the open endpoint, where the closest protein
  heavy-atom distance is 1.84 angstrom. The trajectory is an interpolated illustration, not a
  binding path or kinetic model.
- The hexokinase smooth surface is translucent and has overlapping front and back contours.
- Illustrate was tested as a still renderer. Its atom-sphere style is not a molecular surface.
- The first Mol* screenshot assignment silently left output at 638 x 638. The native viewport
  values setter fixed the issue; all final outputs were regenerated and measured at 640 x 640.
- GroEL depicts a viewpoint rotation of the complete deposited assembly, not a conformational cycle.
- LibreOffice 26.2.7.3 played both GIF and MP4 probes, but animated WebP inserted as an ODP image
  shape remained blank. Impress frame pacing was not measured; GIF appeared slower than MP4, so
  MP4 is preferred when paced presentation matters.

Update this report only from recorded observations. M1-M4 have acceptance evidence and all three
reviews passed. The archived plan records the completed scope; the limits above remain part of
that acceptance.
