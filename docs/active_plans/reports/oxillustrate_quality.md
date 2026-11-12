# Oxillustrate quality review

Owner: fresh gpt-6.1-sol high quality reviewer. Reviewed 2026-11-12.

What this change does: it invokes the external native Rust renderer for the 3N0G still and a
fixed-scale GroEL viewpoint rotation. Two native scenes and one small Python helper feed the
existing media encoder; the README capture uses the new GroEL image.

## Verdict

**PASS for quality. Looks good. Ship to the separate integration review.** No actionable quality
defect was found. This is an independent source, artifact and evidence review, not overall plan
acceptance or a repeated specification verdict.

## Review findings

- The helper's positive-angle Z/Y/X rotations agree with the current native
  `scene_preparation.rs`. Its subtracted center is the rotated molecular origin plus a fixed depth
  offset. One bounding sphere, including the current maximum native radius, protects all viewing
  angles against screen and zero-depth clipping without changing scale. The focused test uses an
  asymmetric translated molecule, so it protects meaningful centering and rigid-motion behavior.
- The input check is deliberately specific to this deposited assembly: fourteen named chains,
  53,858 protein atoms, 298 omitted waters, no alternate conformers and finite coordinates.
  `assembly: null` prevents a second expansion. The 3N0G scene reads the existing selected mmCIF,
  retains DST and Mg, and uses native coloring rules. The independent native data-handoff evidence
  in [oxillustrate_science.md](oxillustrate_science.md) addresses loaded identities and prepared
  spheres, beyond what the Python inventory alone establishes.
- Native calls use separate argument entries and propagate failures. Fixed generated paths stay
  under ignored `output/`; original structural inputs and retained Mol* outputs are preserved.
  The helper rejects extra frame names, and the unchanged encoder checks the complete contiguous
  sequence, dimensions and image validity before encoding. No new dependency, adapter, bindings,
  viewer or configuration framework is needed for this single-user, serial example workflow.
- Actual retained scenes, CLI source, encoder and capture callers agree with the documented
  commands. `trim: false` reaches the renderer, while equal fog endpoints remove per-frame fog
  normalization. The inspected 3N0G preview shows exposed magenta ligand and green ion surfaces;
  the nine-view GroEL contact sheet shows useful boundaries, stable framing and no visible edge
  clipping. The README composite clearly distinguishes Mol* interpolation from Rust Goodsell
  viewpoint rotation.
- Dirty-source provenance is candid: the source snapshot and binary hash identify the observed
  build, while HEAD alone does not. License guidance keeps the external AGPL renderer separate
  from this repository's code. Render/replay, scientific, capture and application-playback reports
  support distinct claims; none turns decoding into scientific fidelity or exact slideshow pacing.
  No further abstraction, option or permanent test is justified by this scope.

The specification review's nonblocking plan wording clarification remains appropriate: the exact
53,858 count describes protein atoms. The implementation and example documentation already say so.

## Independent checks

Run from the repository root:

```bash
source source_me.sh && python3 -m pytest -q tests/test_oxillustrate_rotation.py
source source_me.sh && python3 -m pyflakes examples/groel_rotation/render_oxillustrate.py devel/capture_readme_visuals.py
git diff --check
```

Results: one geometry test passed; pyflakes and diff checks passed. A read-only Python check using
the same bootstrap also verified all 130 retained PNG/still/media/poster hashes against
`baseline_sha256.json`, all 25 saved build-input hashes against both snapshot and live sibling
files, executable/input/template hashes against `render.json`, and the real frames through the
existing encoder's `check_frames`. All passed. These are current artifact checks, not another
rendering replay. The final report also passed its focused ASCII and Markdown-link checks.

Reviewed source includes the new helper/test/scenes, existing preparation and encoder, changed
capture helper, native CLI/scene preparation/shading, and current example/tool documentation.
Reviewed evidence includes [oxillustrate_render.md](oxillustrate_render.md),
[oxillustrate_science.md](oxillustrate_science.md),
[oxillustrate_capture.md](oxillustrate_capture.md),
[oxillustrate_playback.md](oxillustrate_playback.md) and
[oxillustrate_checks.md](oxillustrate_checks.md), plus retained provenance and validation records.

## Evidence limits

This review did not repeat rendering, native scientific preparation, encoding, browser/Impress
playback, installation, full upstream tests or the full repository suite. Those executed checks
are attributed to their separate reports. Mypy is unavailable. The historical full pytest result
remains 1,031 passed, one skipped and two failures; the later focused Bandit correction does not
establish a fresh green full run. The unchanged research-report Unicode failure remains recorded.

The observed renderer is external and mutable; a future build needs its own fidelity and output
checks. Cross-platform pixel identity, exact Impress pacing and Rust animated WebP in Impress
remain unverified. No new material risk was found within the reviewed scope.
