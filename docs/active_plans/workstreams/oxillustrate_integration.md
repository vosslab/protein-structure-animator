# Oxillustrate integration ledger

The [approved plan](../../archive/oxillustrate_integration.md) is complete, accepted and archived
after fresh specification, independent quality and integration reviews on 2026-11-12.
Statuses describe actual evidence for this Rust integration, separate from earlier Mol* acceptance.

| Task | Owner and model | Status | Evidence and dependency |
| --- | --- | --- | --- |
| Native source contract | oxillustrate_semantics; Sol medium | Complete read-only inspection | CLI, namespaces, center subtraction and dirty-source provenance inspected |
| Native rendering and visual inspection | oxillustrate_render; Sol high | PASS within recorded scope | [oxillustrate_render.md](../reports/oxillustrate_render.md) |
| Fresh-process replay | oxillustrate_render; Sol high | PASS on this Mac | Same render report; all 125 PNGs, media, poster and still byte-identical |
| Independent science | oxillustrate_science; Sol high | PASS | [oxillustrate_science.md](../reports/oxillustrate_science.md); native identities, coordinates and all-frame geometry |
| README capture | oxillustrate_capture; Sol medium | PASS within capture scope | [oxillustrate_capture.md](../reports/oxillustrate_capture.md); replay source hash matches, hexokinase preview byte-identical |
| Browser and Impress playback | oxillustrate_playback; Sol high | PASS within application scope | [oxillustrate_playback.md](../reports/oxillustrate_playback.md); Chromium images/MP4 and actual Impress MP4 slideshow |
| Policy and guides | oxillustrate_docs; Sol medium | Complete; reviewed | Canonical direction, exact native commands and measured evidence synchronized |
| Repository verification | oxillustrate_checks; Luna high | Complete with recorded baseline failure | [oxillustrate_checks.md](../reports/oxillustrate_checks.md); full run 1,031 passed, 1 skipped, 2 failed; later B108 fix checked separately |
| Fresh specification review | oxillustrate_specification; Luna high | PASS | [oxillustrate_specification.md](../reports/oxillustrate_specification.md) |
| Independent quality review | oxillustrate_quality; Sol high | PASS; no actionable defects | [oxillustrate_quality.md](../reports/oxillustrate_quality.md) |
| Fresh integration review | oxillustrate_integration_review; Luna high | PASS; ready to close | [oxillustrate_integration_review.md](../reports/oxillustrate_integration_review.md) |
| Capture temp correction | oxillustrate_temp_fix; Luna high | Complete | Focused Bandit 1 passed; combined checks 70 passed; two captures retained identical hashes |
| Authorized closeout | oxillustrate_closeout; Sol medium | Complete | Ledger reconciled, protein-atom wording clarified and accepted plan archived |

## Settled direction

- The human chose the Rust native CLI as canonical Goodsell renderer and visual gold standard.
  Initial scope is the 3N0G still and complete GroEL rotation. Mol* remains for smooth surfaces and
  interactive views; existing hexokinase work stays unchanged. Adoption is settled policy, while
  capability and delivery verification remain evidence-based.
- Current source is authoritative: center is subtracted after rotation. Use one world-space origin,
  fixed scale and depth-safe framing. Both scenes use model 1, `assembly:null`, opaque white and
  `trim:false`. Equal native fog endpoints disable frame-dependent normalization; native shadows
  and outlines remain. Original structural inputs are unchanged, with no second assembly expansion.
- Preserve original hashes, native scene per frame, logs and observed source/binary provenance.
  Tested version is 26.11.0, HEAD `29d4e907efe6524eb78188edbdd4a500dc0e5260` with substantial dirty
  changes. The verification snapshot retains actual build inputs and diff; HEAD alone is insufficient.
  Build current source with `cargo build --release`; this is an observation, not a revision pin.
- Keep the external AGPL-3.0-only binary separate from this project's LGPL source. Preserve
  historical Fortran attribution. Add no bindings, shared framework, automatic fallback or Blender.
- Serialize graphics. Keep scientific interpretation, coordinate fidelity, visual inspection,
  decoding, browser playback, Impress playback and fresh-process reproduction distinct.
- Model choices: Sol for implementation and readable evidence review; Luna for scoped repository
  checks, specification and integration review. Fresh independent assignments are recorded above;
  each uses the smaller capable model for its implementation, native analysis or requirement checks.

## Measured evidence and limits

- Independent native checks preserve all 4,261 selected 3N0G identities, including fourteen DST atoms
  and three Mg ions; all 125 GroEL scenes preserve 53,858 identities across fourteen chains with
  assembly instance zero. Native-vs-NumPy projection error is at most `2.274e-13` pixels. Minimum
  XY padding is `32.749` pixels and nearest sphere front Z is `-5.804` pixels. The seam is an ordinary
  rotation step. Deposited mutations/missing residues remain; this is viewpoint rotation, not dynamics.
- Rendered PNGs are 640 x 640; encoded media contain 125 frames at 25 fps, five seconds. Replay is
  byte-identical locally. Full replay took 54.08 s, maximum RSS 340,590,592 bytes; encoding 17.67 s.
  No cross-platform pixel-identity claim or fresh dependency-install claim is made.
- Chromium 158.0.8127.18 shows timed WebP/GIF/MP4 motion and a natural MP4 loop. LibreOffice
  26.2.7.3 shows actual MP4 slideshow motion across eight timed captures. Exact Impress frame rate,
  Rust WebP-in-Impress, other platforms and LMS playback remain unchecked. Owned apps were stopped.
- Static quality-90 capture shows Rust GroEL beside Mol* hexokinase endpoints. Its replay source
  frame hash matches; the hexokinase motion preview remains byte-identical. Capture added no UI.
- Documentation checks before freeze: 74 Markdown-link, README-opening and guidance-format tests
  passed; owned documentation ASCII and whitespace checks passed. The one full suite run reports
  1,031 passed, 1 skipped and 2 failed: unchanged research-report Unicode and the capture helper
  B108. A later minimal temp-location correction passes its focused Bandit check and combined
  70-check lane; two helper runs retain identical hashes. No fresh full-green result is claimed.
  The unchanged research-report Unicode failure remains; mypy is unavailable.
- Closeout checks: 78 Markdown-link, README-opening and guidance-format tests passed, including
  all eight new oxillustrate reports; seven closeout documents are ASCII. Working-tree and cached
  whitespace checks pass. Only the archived plan is staged; no commit was made.
- Accepted: specification PASS, independent quality PASS with no actionable defects and fresh
  integration PASS. Current-source center subtraction (D1) and the canonical renderer role are
  settled; no open question remains for this implemented scope. The accepted plan is archived.

## Historical evidence

[toolbox_verification.md](../reports/toolbox_verification.md) and
[toolbox_execution.md](toolbox_execution.md) preserve the accepted earlier Mol*/Fortran scope.
Their completed reviews and playback checks do not cover these new Rust outputs.
