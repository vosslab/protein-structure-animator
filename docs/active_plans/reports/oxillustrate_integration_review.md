# Oxillustrate integration review

Owner: fresh Luna high integration reviewer. Reviewed 2026-11-12.

## Verdict

**PASS for integration; ready for closeout and archive.** The approved 3N0G still and complete
GroEL rotation are implemented as the canonical Goodsell route. The composed examples, guides,
README and evidence reports agree on the route and its limits. No blocking integration gap remains.
This review does not itself update the ledger or archive the plan.

## Integration findings

- **Scope and route align.** The human-selected Rust oxillustrate CLI is canonical for Goodsell
  figures and animations. The initial scope remains the 3N0G still and complete 1OEL GroEL assembly.
  Mol* remains documented for smooth surfaces and interactive work; existing hexokinase work and
  outputs remain intact. The external AGPL renderer is invoked separately and is not redistributed.
- **Commands reach the shipped examples.** The README quick start, [OXILLUSTRATE.md](../../tools/OXILLUSTRATE.md),
  [3N0G example](../../../examples/appearance_3n0g/README.md) and
  [GroEL example](../../../examples/groel_rotation/README.md) describe the implemented build,
  preparation, native rendering and encoding commands. The GroEL helper defaults to the sibling
  release binary and offers the bounded `--illustrate` override. Native per-frame scenes and
  generated outputs stay in their documented locations.
- **Scientific claims match the inputs and motion.** The evidence identifies the selected 3N0G
  protein, DST and Mg records, and the 1OEL deposited assembly with fourteen chains, 53,858 protein
  atoms and 298 omitted waters. Assembly expansion is not repeated. The GroEL example is consistently
  labeled as a viewpoint rotation, not protein dynamics. Independent native checks report matching
  atom identities and coordinates, plus geometry for all 125 scenes.
- **Visual and delivery claims have separate support.** Native render inspection, byte-identical
  fresh-process replay, browser playback and actual Impress MP4 playback have distinct reports.
  The README composite pairs the Rust GroEL still with unchanged Mol* hexokinase endpoints, and its
  motion preview remains unchanged. Limits include no cross-platform pixel-identity claim, no exact
  Impress frame-rate claim, no Rust animated-WebP-in-Impress claim and no fresh-install claim.
- **Verification reporting is candid.** The recorded full pytest run has 1,031 passes, one skip and
  two existing failures. The later focused Bandit correction is reported separately; it does not
  become a claim of a green full suite. Mypy is unavailable. These limits do not contradict the
  scoped implementation or its focused checks.

## Closeout notes

The specification review's one wording clarification is valid: in
[oxillustrate_integration.md](../../archive/oxillustrate_integration.md), change `53,858 atoms` to
`53,858 protein atoms`; the selection and all implementation evidence already use the precise
meaning. This is a nonblocking plan edit for closeout.

The workstream ledger still labels repository verification as in progress and all three fresh
reviews as pending. The check report and completed specification, quality and this integration
review provide the actual results, so those ledger statuses are stale bookkeeping rather than
unmet implementation work. Closeout should record the observed check result and review verdicts,
then archive the approved plan. The plan should remain active until that authorized archival step.

## Evidence and limits

Reviewed the approved plan, animation guidance, repository and Markdown conventions, README,
canonical tool guide, both example READMEs, workstream ledger, and the render, science, capture,
playback, checks, specification and quality reports. This was a composition and evidence-alignment
review; it did not rerun rendering, application playback, the full test suite or external tools.
