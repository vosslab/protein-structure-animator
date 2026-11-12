# Changelog

## 2026-11-11

### Additions and New Features

- Add native-tool guides, an agent animation guide, structure preparation, Mol* render examples and
  a media encoder for the documented 3N0G, hexokinase and GroEL examples.
- Update README status to describe the completed examples, format-specific playback evidence and
  accepted reviews; add a central verification report and a file-backed execution ledger.
- Record native-tool, structure-preservation, evidence-boundary and forward dependency decisions.
- Approve separate npm aliases for the latest TypeScript compiler and the TypeScript 6 runtime
  required by the current typescript-eslint compiler API. Clean-install, compiler, ESLint and
  Prettier evidence is recorded; the full shell gate stops at its empty TypeScript lint globs.
- Correct Mol* screenshot dimensions through the native viewport values setter; verify 640 x 640
  3N0G images and require fresh replay and re-encoding of the other examples before accepting all
  delivery outputs.

### Fixes and Maintenance

- Correct example links to point to the central toolbox verification report.
- Archive the accepted M1-M4 toolbox plan after integration review and manager-authorized closeout;
  update its links and the README, verification report and ledger to reflect completion.
- Remove only the unused temporary npm copy at `LOCAL_ONLY/render/`; retain documented clone and
  all output, native-session, media and structural-reference evidence.

### Developer Tests and Notes

- Structural, dependency, render-delivery and Impress reports are recorded. GIF and MP4 played in
  actual Impress slideshows; animated WebP embedded as an ODP image was blank in the tested version.
  GIF appeared slower than MP4; exact slideshow frame rate was not measured.
  M1-M4 passed specification, quality and integration reviews within the documented limits.
- Focused README, guidance-format and verification/ledger/review Markdown-link checks: 20 passed,
  39 deselected; `git diff --check` passed. The broader suite reported 938 passed, 1 skipped and
  3 failed; see the verification report for the transient link failures and remaining unchanged
  Unicode failure in the research report.
- Quality review checks: encoder pytest 1 passed; Node and shell syntax, canonical ESLint and
  Prettier, `git diff --check`, and the quality-report link check passed (1 passed, 50 deselected).
- The tested ChimeraX mmCIF trajectory export repeated coordinates; the checked PDB handoff is
  documented as a release-specific observation, with original mmCIF inputs preserved.
- Final closeout checks: all Markdown-link, README-first-paragraph and guidance-format tests passed
  (60 passed); `git diff --check` passed. The broader suite result remains 938 passed, 1 skipped
  and 3 failed, including the
  unchanged research-report Unicode citation-marker failure and earlier transient link failures.
  The TS18003 empty-TypeScript-glob gate limitation and 10 moderate dependency advisories remain.

### Additions and New Features

- Add a README landing page describing the teaching use cases, research-stage status, toolbox
  approach, and routes to the plan and project notes.
- Save the protein animation toolbox plan in
  [protein_animation_toolbox.md](archive/protein_animation_toolbox.md), covering tool
  research, teaching examples, evidence boundaries, and acceptance checks.
- Record human guidance and the capability-collection design direction, including optional Blender
  use after reported Mac instability and a possible future Rust port of Illustrate.

### Fixes and Maintenance

- Synchronized shared style guides, tests, and repository support files from the starter template.

### Developer Tests and Notes

- README paragraph and Markdown link checks: 33 passed; `git diff --check` passed.
- Documentation only; no tools installed, renderers launched, or animations generated.
- Leave the existing untracked root research report unchanged.
