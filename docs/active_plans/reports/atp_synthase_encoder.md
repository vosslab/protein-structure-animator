# Alpha encoder implementation

## Delivered behavior

[encode_loop.py](../../../tools/encode_loop.py) retains its positional frame-directory interface,
125-frame validation, 25 fps playback, lossless animated WebP, and lossless poster. MP4 and GIF now
composite their input onto an explicit white FFmpeg color source before encoding. This preserves
visible semitransparent edges while delivering an opaque background for those formats. No source
frames, dependencies, CLI flags, or existing example media were changed.

The existing frame validator returns the validated dimensions for the color source. The white
overlay also handles RGB inputs without an alpha-detection branch. A real-codec comparison finds
the decoded RGB MP4 identical to the previous encoding command on the moving RGB probe.

## Retained regression check

[e2e_encode_alpha.py](../../../tests/e2e/e2e_encode_alpha.py) invokes the actual encoder and codecs
inside a temporary directory. It creates 125 moving 96 x 64 RGBA PNGs with transparent background,
semitransparent moving red edges, an opaque red center, a semitransparent blue patch, and an opaque
white patch. It checks every decoded WebP frame against all source RGBA bytes, so a trail left in
vacated transparent pixels also fails. It checks exact poster RGBA, all GIF alpha values and white
backgrounds, 40 ms WebP/GIF timing, decoded MP4 frame count, 25 fps and five-second duration, white
MP4 background and white-object pixels, and the blue composite within 10 values per channel.

This permanent whole-system check protects the alpha/opaque delivery contract, which a mocked
FFmpeg call cannot establish. It belongs outside the fast pytest lane. Failure means the codec or
filter behavior changed; inspect decoded output and fix delivery before accepting replacement media.
It adds no new CI gate. The existing fast frame-integrity test remains unchanged.

## Observed commands and results

Run from the repository root on 2026-11-12. Observed versions: Python 3.12.16, Pillow 13.0.0,
FFmpeg 9.0.2. These are observations, not dependency pins.

```bash
source source_me.sh && python3 tests/e2e/e2e_encode_alpha.py
```

```text
PASS: 125 frames at 40 ms; WebP/poster exact RGBA; GIF opaque white; MP4 white background and semitransparent blue composite (tolerance 10).
```

The run exits successfully in under one second on this host. The equality checks cover alpha
values 0, 128, and 255, including the moving soft edge and opaque white object.

```bash
source source_me.sh && python3 output/atp_synthase_feasibility/media/encoder_implementation/check_rgb.py
```

The ignored local probe and its `results.json` remain under
`output/atp_synthase_feasibility/media/encoder_implementation/`. It encodes 125 moving RGB frames,
compares all decoded MP4 bytes with the original pre-overlay command, and checks all RGB WebP
pixels against source. Result: MP4 decoded bytes identical; 125 WebP frames exact; MP4 125 frames,
25/1 fps, duration 5.000000 seconds.

```bash
source source_me.sh && python3 -m pyflakes tools/encode_loop.py tests/e2e/e2e_encode_alpha.py
source source_me.sh && python3 -m bandit --severity-level medium --confidence-level medium tools/encode_loop.py tests/e2e/e2e_encode_alpha.py
```

Pyflakes exits 0 with no output. Bandit exits 0 with no medium/high findings; it reports 27 low
severity findings, including the test assertions and subprocess calls. No findings are suppressed.

```bash
source source_me.sh && python3 -m pytest tests/test_encode_loop.py tests/test_pyflakes_code_lint.py tests/test_bandit_security.py tests/test_function_typing.py tests/test_indentation.py tests/test_whitespace.py tests/test_shebangs.py tests/test_import_requirements.py tests/test_markdown_links.py -q
```

Result: `641 passed in 1.40s`. Repository hygiene discovery covers tracked files; the new untracked
E2E runner is additionally covered by the direct Pyflakes/Bandit commands above and executable mode
is set. The retained E2E runner was rerun successfully after its final timing and moving-edge checks.

## Evidence limits

These are synthetic real-codec delivery checks. Browser and Impress playback, ATP synthase visual
acceptance, scientific interpretation, structural fidelity, and full native example reproduction
belong to their separate workstreams. No full repository suite, Blender launch, commit, publication,
or overwrite of existing full-size example movies was performed.
