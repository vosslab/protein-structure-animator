# Toolbox execution ledger

Statuses describe evidence available in this checkout. A task is complete only when its named
evidence exists and has been reviewed.

| Task | Scope and dependency | Status | Evidence and review |
| --- | --- | --- | --- |
| documentation_ledger | README, guidance pointer, decisions, changelog, report index and ledger; uses other reports | Complete | This ledger and [toolbox verification](../reports/toolbox_verification.md) record accepted M1-M4 evidence, review results and the documented WebP insertion limitation. |
| scientific_verification | Structure preparation, scientific selections, coordinate fidelity; native replay | Complete | [Structural verification](../reports/structural_verification.md) confirms the fresh preparation replay, all 3,651 hexokinase protein identities, glucose registration, and imported identity/coordinate fidelity for hexokinase and all GroEL atoms. |
| renderer_delivery | Final renders, visual review, browser playback, fresh-process replay and preview WebPs | Complete | [Render delivery verification](../reports/render_delivery_verification.md) records all final renders, media decoding, actual Chromium/Firefox playback and native scene restoration. |
| impress_playback | Actual Impress slideshow playback | Complete within documented format limits | [Impress verification](../reports/impress_verification.md) records visible motion in GIF and MP4 for both examples; animated WebP embedded as an ODP image stays blank on this installation. |
| typescript_runtime | Verify current dependency minimums, latest compiler and supported lint runtime | Verified with a separate repository gate limitation | [Dependency verification](../reports/dependency_verification.md) records clean install, TS7 compiler, TS6-backed ESLint integration and lint/format gates. Full shell gate stops at TS18003 because configured TypeScript source globs are empty; 10 moderate minimatch audit advisories remain. |
| screenshot_dimensions_fix | Correct Mol* PNG output dimensions through the native viewport API | Complete | The correction report records 3N0G output; the final render report measures every animation frame and delivery at 640 x 640. |
| closeout_cleanup | Remove only task-created disposable experiments after final evidence review | Complete | Removed the unused temporary npm copy at `LOCAL_ONLY/render/`. Kept ignored `LOCAL_ONLY/illustrate/`, generated evidence, native sessions, referenced logs, and `output/experiments/reference.jpg`. Final Markdown, README paragraph and guidance-format checks: 60 passed; `git diff --check` passed. |
| fresh_specification_review | Review plan and documentation against acceptance criteria | PASS | [Specification review](../reports/specification_review.md) accepts M1-M4 within recorded limits. Quality and integration reviews also passed. |
| fresh_quality_review | Independent quality review of completed docs and evidence | PASS | [Quality review](../reports/quality_review.md) found no actionable code or documentation quality issue. |
| integration_review | Check the integrated result and remaining acceptance gaps | PASS | [Integration review](../reports/integration_review.md) found no actionable integration gap and accepted M1-M4 within documented limits. |

## Settled decisions

- **D1:** Keep this as a collection of native scripts and tools. Add no application, API or recipe
  framework.
- **D2:** Preserve original mmCIF. Use the checked native PDB trajectory only for the tested
  hexokinase handoff because ChimeraX 1.10.1 repeated coordinates in its mmCIF export.
- **D3:** Serialize graphics work on this Mac. Require fresh-process replay; treat application
  playback as separate evidence.
- **D4:** Use current dependencies and open-ended `>=` requirements. Record tested versions as
  observations, not pins.
- **D5:** Retain native atom keys, fixed-glucose keys and coordinates, and GroEL atom keys alongside
  imported coordinates so identity and ligand registration can be compared after import.
- **D6:** Provide latest TypeScript as `@typescript/native` and a TypeScript 6 compatibility alias
  as `typescript` for the current `typescript-eslint` compiler API. Verify each runtime independently.
- **D7:** Set Mol* screenshot dimensions through its native viewport values setter; the former
  assignment produced 638 x 638 PNGs despite the intended 640 x 640 canvas. The corrected setter was
  reviewed, then all examples were rerendered and re-encoded with measured final dimensions.

## Completion boundary

M1-M4 are complete within the recorded scientific, application and repository-gate limits.
Specification, quality and integration reviews passed. The manager authorized cleanup and archive;
all seven settled decisions are closed. See the [archived plan](../../archive/protein_animation_toolbox.md).
