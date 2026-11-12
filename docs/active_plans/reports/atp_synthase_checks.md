# ATP synthase repository checks

## Verdict and scope

Implementation checks pass. The full fast suite initially records 1,164 passed, one skipped
and two failures: the unchanged research-report Unicode baseline and an active browser worker's
temporary Playwright probe outside its required lane. The owner subsequently removed the probes;
all five affected naming-gate checks pass. No task-related repository failure remains.

This report covers repository source, fast tests, synthetic real-codec delivery, and focused
canvas/crop behavior. It does not establish scientific correctness, visual acceptance, native
render reproduction, browser playback or Impress behavior; those have independent owners.

## Rules receipt

Read AGENTS.md, docs/*_STYLE.md, the latest 2026-11-12 changelog entry, animation guidance,
the approved ATP plan, and the Ponytail and repo-rules-reader skills. Run repository Python as
`source source_me.sh && python3`. The latest changelog records ATP/alpha work as pending
independent acceptance. Fragile pytest ties success to transient context, incidental inventory,
tunable defaults, external fixture state, wall-clock delays or unseeded randomness. Stable
geometry and codec behavior already have meaningful tests; no duplicate permanent test was added.

## Commands and results

- `source source_me.sh && python3 -m pytest tests/test_atp_synthase_geometry.py
  tests/test_encode_loop.py tests/test_oxillustrate_rotation.py -q`: four passed in 0.30 s.
- `source source_me.sh && python3 tests/e2e/e2e_encode_alpha.py`: PASS. All 125 WebP frames
  preserve exact RGBA and 40 ms duration, poster preserves exact RGBA, GIF is opaque white,
  MP4 is 25 fps for five seconds with white background and correctly composited blue alpha.
- `node --check examples/render_molstar.mjs`: PASS.
- `npx eslint --max-warnings 0 examples/render_molstar.mjs`: PASS.
- `npx prettier --check --ignore-path .gitignore --ignore-path .prettierignore
  --ignore-path .prettierignore.local examples/render_molstar.mjs`: PASS.
- `bash -n examples/download_inputs.sh`: PASS.
- `git diff --check` and `git diff --cached --check`: PASS.

Direct temporary Python probes invoke existing hygiene helpers on the union of
`git diff --name-only HEAD` and `git ls-files --others --exclude-standard`, rather than relying
on tracked-file discovery. At source-check time 35 changed/new authored files pass ASCII,
whitespace, applicable function typing, shebang/executable alignment and line budget; scene JSON
parses successfully. All six changed/new Python files pass `python3 -m pyflakes` and
`python3 -m bandit -ll -ii -q` explicitly. The new renderer has 290 lines; the E2E runner has 72.
The staged test remains at tests/test_atp_synthase_geometry.py; no Git index change was made.

A direct Markdown-link probe covers 23 changed/new documents against both tracked and untracked
nonignored paths, including the six final gallery files: zero issues. The frozen README digest is
`3c0eec7e0cec82da3758fb30a62253ad86e942b324b1e8895623418bac45aa42`.

One-off synthetic checks pass: two widely separated RGBA poses fit the same union crop, padding
may extend outside the native canvas without discarding alpha, fitting does not enlarge poses,
registered native canvas restoration preserves straight RGBA bytes at the exact crop origin,
and invalid negative origins are rejected. A warning in this temporary probe concerns its
Pillow `getdata` use, deprecated for removal in Pillow 14 in 2027; product code is unaffected.

## Full fast suite

The initial `python3 -m pytest tests/ --no-ascii-fix -q` invocation exits 4 before collection:
`unrecognized arguments: --no-ascii-fix`. The hygiene gates read that switch but the repository
does not register it. A temporary plugin registers only the existing read-only switch:

```bash
source source_me.sh && PYTHONPATH=tests/_temp/atp_synthase_checks \
  python3 -m pytest tests/ -p read_only_pytest --no-ascii-fix -q
```

Actual output: `2 failed, 1164 passed, 1 skipped in 2.22s`.

- tests/test_ascii_compliance.py:473 fails for
  docs/active_plans/protein-deep-research-report.md: 196 non-ISO-8859-1 characters, including
  U+E200/U+E201/U+E202 citation markers. The entire file is byte-identical to HEAD before and
  after the suite, SHA256 `6f7bf2d2306dc910a814759684b2d7dd8bb519942a4d19de88710db756881fb7`.
  This is demonstrated pre-existing baseline evidence, not an assumed unrelated failure.
- tests/test_test_naming_conventions.py:422 fails because
  tests/_temp/atp_playback_probe.mjs imports Playwright outside tests/playwright/. Reported
  to the manager for its owning worker to clean up; no other worker's file was modified by this
  tester. After playback completed, the owner copied its two JS probes and one Python probe
  into ignored output and removed the temporary originals. The exact affected retest was
  `source source_me.sh && python3 -m pytest tests/test_test_naming_conventions.py -q`:
  `5 passed in 0.02s`. The broad suite was not repeated because product source stayed frozen;
  the initial counts remain the actual full-suite record, not an updated green-suite claim.

No native build/render, dependency update, empty TypeScript gate, Blender invocation or
publication was performed. Existing historical native/GroEL/hexokinase media were not changed
by this checking work. The full suite is not green while the Unicode baseline remains.

## Evidence handoff

Temporary logs live in tests/_temp/atp_synthase_checks/: focused.log, e2e_encode_alpha.log,
javascript.log, direct_source.log, canvas_crop.log, direct_links.log, baseline.log,
full_pytest.log and naming_cleanup.log. Preserve these under ignored output before removing the
temporary plugin. The manager/documentation owner copies this final report to the durable reports
directory. This tester edits only tests/.
