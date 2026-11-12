# Oxillustrate checks

Scoped repository checks for the canonical Rust oxillustrate GroEL integration, run 2026-11-12.
Scientific, native render/replay, capture, and playback evidence remains in the linked reports.

## Results

| Check | Result |
| --- | --- |
| `pyflakes` on the GroEL renderer and README capture helper | PASS |
| No-write syntax compilation of the renderer and rotation test | PASS |
| Focused rotation geometry test | PASS, 1 passed |
| Full `tests/` pytest lane | 1,031 passed, 1 skipped, 2 failed |
| `git diff --check` | PASS |

The focused test checks fixed-origin centering, rigid distances, bounds over 125 rotation steps,
and the native rotation direction. The full suite also collected and passed this test.

The two full-suite failures are scoped as follows:

- `test_ascii_compliance[docs/active_plans/protein-deep-research-report.md]` reports 196
  private-use characters (197 reported violations). The file is unchanged from `HEAD`; the same
  196 characters are present in the committed version.
- `test_bandit_security[devel/capture_readme_visuals.py]` reports B108 for the existing
  `TemporaryDirectory(..., dir="/tmp")` call. That call is unchanged from `HEAD`; its line moved
  from 87 to 88 because of an unrelated earlier insertion in that helper.

Neither failure is in the oxillustrate renderer or rotation test. No workaround or exclusion was
used.

## Commands

All Python commands use the repository bootstrap. The full pytest lane ran once after the docs
freeze was confirmed.

```sh
source source_me.sh && pyflakes examples/groel_rotation/render_oxillustrate.py devel/capture_readme_visuals.py
source source_me.sh && python3 -c "from pathlib import Path; paths=['examples/groel_rotation/render_oxillustrate.py','tests/test_oxillustrate_rotation.py']; [compile(Path(path).read_text(), path, 'exec') for path in paths]"
source source_me.sh && PYTHONDONTWRITEBYTECODE=1 python3 -m pytest tests/test_oxillustrate_rotation.py -q
source source_me.sh && PYTHONDONTWRITEBYTECODE=1 python3 -m pytest tests/
git diff --check
```

The full pytest output is retained at `output/oxillustrate_checks/full_pytest.txt`; scoped command
outputs are in the same ignored directory.

## Evidence boundaries

- Scientific input and coordinate checks: [oxillustrate_science.md](oxillustrate_science.md).
- Native rendering and fresh-process replay: [oxillustrate_render.md](oxillustrate_render.md).
- Playback: [oxillustrate_playback.md](oxillustrate_playback.md).
- README image capture: [oxillustrate_capture.md](oxillustrate_capture.md).

This check run did not launch a native renderer or UI, rerun playback, run mypy, or invoke npm
gates. No JavaScript or dependency configuration changed in this integration; mypy is unavailable.

## 2026-11-12 follow-up

The full-suite result above is historical. After it, remove the explicit `dir="/tmp"` from
`devel/capture_readme_visuals.py`; `TemporaryDirectory` now uses the standard library's default
secure OS temp selection. The focused Bandit node for that helper passes (1 passed), as do
pyflakes on the helper and `git diff --check`. The unchanged research-report Unicode failure was
not rerun or edited.

Two helper runs completed at 14:05 UTC. Both retained the source GroEL frame hash
`0ece252c5d76e76695d54aea56a17399a4a15726a14c64d449f6c5e9ab1abf83`, static asset hash
`c7247501c3a865cd784d5263fec7d77d7eae1aee1f59866c011c9a7e5bac66a8`, motion asset hash
`d6a0fd11e0cd2112303526945eec68011aac1e091d2fff3431dcca90d3de4b74`, and current README hash
`b7a79988fe55b9c8b56ea0a80af869169560fd017d726f252708f285709bfc55` unchanged. No full suite,
native renderer, or UI was rerun.
