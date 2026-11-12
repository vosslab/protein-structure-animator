# Oxillustrate specification review

Owner: fresh Luna high specification reviewer. Reviewed 2026-11-12.

## Verdict

**PASS for specification coverage.** The approved scope is implemented and the evidence reports cover
its observable checks without conflating scientific fidelity, rendered appearance, media decoding,
application playback or fresh-process replay. No blocking specification gap remains. This review
does not provide the separate quality verdict or overall integration acceptance.

## Coverage

- **Chosen route and scope:** current guidance and commands use the sibling native Rust CLI as the
  canonical Goodsell renderer. The GroEL helper defaults to the sibling release binary and exposes
  `--illustrate`; the 3N0G still invokes the CLI directly. Mol* remains documented for surfaces and
  interactive views, while the existing hexokinase route and motion preview remain unchanged.
  Current guidance has no stale candidate or deferred-Rust wording; the old changelog entry is
  historical.
- **Inputs and structure:** original input hashes are retained and verified. The 3N0G report accounts
  for the protein, DST and three Mg ions, plus omitted records and alternate conformers. The GroEL
  input is already assembly 1; all fourteen chains and 53,858 protein atoms remain selected without
  a second expansion. The 298 deposited waters omitted by native selection are explicitly disclosed.
- **Native scenes and framing:** retained JSON scenes, logs and source/binary provenance support the
  still and 125-frame rotation. Current center-subtraction semantics, fixed origin and scale, depth
  bounds, no-trim dimensions and the non-duplicated full-turn endpoint are documented and independently
  checked. The motion is consistently described as a viewpoint rotation, not protein dynamics.
- **Appearance and delivery:** render evidence records full-size and teaching-size visual inspection,
  ligand visibility, contours, bounds, dimensions, timing and resources. Decoding and loop checks cover
  all three requested formats. Separate Chromium and actual Impress reports demonstrate motion in the
  tested applications.
- **Replay and handoff:** documented commands match the implemented examples; a fresh-process replay
  reproduced the PNGs, encoded media, poster and still byte-for-byte on this Mac. Dirty-source
  provenance includes the build inputs and binary hash, so the report does not imply that HEAD alone
  identifies the renderer. README imagery and first-run guidance reflect the implemented route.

## Clarification

The plan says `53,858 atoms` at
[oxillustrate_integration.md](../../archive/oxillustrate_integration.md#L15), while the exact count means
protein atoms: the input also contains 298 waters that native selection omits. The implementation,
helper and scientific report state this correctly, so it does not block this review. For a future plan
edit, say `53,858 protein atoms` to make the requirement unambiguous.

## Evidence limits

The reports correctly limit claims to the observed Mac and tested versions. They do not claim a fresh
dependency install, cross-platform byte identity, a Rust hexokinase trajectory, exact Impress frame
pacing, Rust WebP playback in Impress, or LMS and other-platform playback. The full pytest run records
1,031 passes, one skip and two unrelated existing failures; the later B108 correction has focused
evidence and does not turn that historical full run into a green result. Mypy was unavailable. These
limits are disclosed and do not contradict the approved scope.
