# Animation gallery capture

## Scope and status

Captured 2026-11-12 by `animation_gallery_implementation` (gpt-6.1-sol, high). This receipt covers
README presentation derivatives of previously verified native frames. It establishes neither a new
molecular render nor new scientific motion. Independent browser verification and fresh reviews are
separate manager-owned work; they were pending at this implementation handoff.

The approved [plan](../../archive/animation_gallery.md) and
[ledger](../workstreams/animation_gallery.md) record the fixed aspect contract: GroEL uses one
640 x 360 (16:9) widescreen canvas; hexokinase uses one 360 x 780 (6:13) phone-style portrait canvas,
displayed at 240 pixels wide. No exact device resolution is claimed. There are no alternate aspect
versions, aspect changes during playback or stretched molecules.

## Assets and encoders

All four files live in `docs/screenshots/`. Each poster uses the first logical animation sample
with the same framing. Posters are separate one-frame WebP images, not animations.

| Asset | Pixels | Bytes | Decoded frames | Playback |
| --- | --- | --- | --- | --- |
| `groel_rotation_demo.webp` | 640 x 360 | 1,997,696 | 60 unique | 5,000 ms, loop 0 |
| `groel_rotation_poster.webp` | 640 x 360 | 28,934 | 1 | Static |
| `hexokinase_closure_loop.webp` | 360 x 780 | 1,093,058 | 60 unique | 5,000 ms, loop 0 |
| `hexokinase_closure_poster.webp` | 360 x 780 | 14,216 | 1 | Static |

SHA-256 values:

```text
groel_rotation_demo.webp
33dce85f347f72b2bfb7ee5fc55249bc9e6933c186c0cd5f2fd245675422ce50
groel_rotation_poster.webp
3c7927d03ef44ef29a4005c65955711c39ec6681e9816431a3cc3c088e579260
hexokinase_closure_loop.webp
1647ffd9422aef6e96e2e715c2252e3357a64d8287b4e0c7c1afaf9b742e577d
hexokinase_closure_poster.webp
e7d6ccde5c1a93feb2ec5918ccc453142e37beee4fc42ed0a45669683f558b6f
README.md
2e75b96a4d0dfeab58367984be0a2ab02e531f7082f16a2e1b5b1533e5dda3c3
```

Observed tools: Pillow 13.0.0 and cwebp 1.6.0 (libsharpyuv 0.4.2). These are observations, not
dependency pins. Animated WebP uses Pillow `save_all=True`, quality 90, `loop=0`, explicit durations
and RGB white canvases. Observed Pillow animation defaults are lossy encoding, method 0,
`minimize_size=False`, `allow_mixed=False`, `kmin=3`, `kmax=5`; no metadata is supplied. Posters
use `cwebp -quiet -q 90` from temporary PNGs. GroEL reduction uses Pillow LANCZOS. The approved
quality/aspect/frame contract takes priority over the screenshot skill's approximate 1 MB hint;
both animations retain quality 90 rather than sacrificing molecular detail to meet that hint.

## Source fidelity and framing

Both source directories contain 125 native 640 x 640 PNGs. Concatenated, numerically ordered source
SHA-256 values are unchanged before and after capture:

```text
output/groel_rotation_oxillustrate/frames
e14a02f9f135f5380a3edf729276ad58c5ddc2c21f8ae643a4990bc9af2451e0
output/hexokinase_closure/frames
a0fe37c9b380e94abf2a920f576586f380a02f90e607ab84de90d96d996fc5de
```

All-pixel differences against white across all 125 frames give these nonwhite union bounds,
using exclusive right/bottom coordinates:

- GroEL: `(31, 40, 607, 586)`. Retain the entire 640 square source and reduce it to 360 square,
  centered at `(140, 0)` on the 640 x 360 canvas. No source crop occurs.
- Hexokinase: `(200, 84, 487, 521)`, fully inside fixed crop `(165, 50, 510, 580)`. The resulting
  345 x 530 image is placed without enlargement at `(7, 125)` on the 360 x 780 canvas. Minimum
  source margins are 35 left, 34 top, 23 right and 59 bottom pixels. The helper validates this
  containment for every source frame, including frames omitted from the preview.

Neither clip uses per-frame auto-cropping, zoom, overlays or baked text. Captions remain native
README text. The retained molecular image proportions match the sources.

The six full-quality animation exports and the two historical README assets are hash-unchanged.
Full-quality SHA-256 values, grouped by example and format:

```text
GroEL MP4: f68e03790b383e45545a0f86ab9be2ae1fe375900377323c286ca75518d58020
GroEL GIF: 39e35cc791964b122db68583a3d8f67d1a9500b54ead905186258ccae4e5118a
GroEL WebP: f8e3745e3505d50a08d69037119d25ede9b553e985363cfa202097c12d553396
Hexokinase MP4: 39ebc079e4ecffe4f7b60a5878bd5a5a6f4aeb369a34da6bfa05ad49d5396eff
Hexokinase GIF: b9ee09a0da9d521a5fd8bcc70e854d31821688430e4a2f3f1f9a0e402f1b8c89
Hexokinase WebP: 0d1c71089a485c03c431fcaeb7353a5bdd87c64aaa413b8d54f93100c8205c78
protein_examples.webp: c7247501c3a865cd784d5263fec7d77d7eae1aee1f59866c011c9a7e5bac66a8
hexokinase_closure_demo.webp: d6a0fd11e0cd2112303526945eec68011aac1e091d2fff3431dcca90d3de4b74
```

The historical assets remain because earlier reports reference them; the capture helper no longer
regenerates them. Original structural inputs and example implementations were not edited.

## Samples and timing

Each loop uses 60 logical samples from 125 native frames, selected by `round(index * 125 / 60)`
for indices 0 through 59. This samples the whole turn/close-reopen sequence without duplicating
the loop endpoint. Source frame indices are:

```text
0, 2, 4, 6, 8, 10, 12, 15, 17, 19, 21, 23, 25, 27, 29,
31, 33, 35, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60,
62, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 88, 90, 92,
94, 96, 98, 100, 102, 104, 106, 108, 110, 112, 115, 117, 119, 121, 123
```

Integer delays use `round((index + 1) * 1000 / 12) - round(index * 1000 / 12)`: the exact sequence
is `[83, 84, 83]` repeated 20 times, totaling 5,000 ms. Both encoded files decode to 60 distinct
frames with these delays; no logical samples were coalesced. WebP loop flag 0 means infinite
playback. Decode/timing evidence alone does not establish actual browser pacing or loop behavior.

## Reproduction and observed checks

From the repository root, after the existing example frames are available:

```bash
source source_me.sh && python3 devel/capture_readme_visuals.py
```

Two final complete captures at 2026-11-12 15:55:36 UTC and 15:56:11 UTC reproduced all four assets
and README byte-for-byte. Earlier exploratory captures were superseded after caption/layout
refinement. Temporary PNG work uses the OS `TemporaryDirectory` location. No renderer was launched.

Implementation observations:

- Decode all preview frames; verify canvas dimensions, 60 unique frames, exact durations and
  infinite-loop metadata. Verify one-frame static posters and matching canvas dimensions.
- Compare all 250 source-frame bytes, six full-quality animations and both historical README
  assets with the pre-capture hashes; all are unchanged.
- Inspect decoded quarter-turn GroEL frames at native 640 x 360 and hexokinase open, intermediate,
  closed and reopening states at native 360 x 780 and README 240 x 520. Assembly contours and
  chain palette are retained, glucose stays visibly magenta and no molecular content is clipped.
  Portrait whitespace is deliberate; faint transparent blue matches the existing Mol* source.
- Two temporary behavior tests pass: crop containment/no enlargement and managed-block sentinel
  preservation/idempotence. They are implementation proof, not a permanent third-party encoder test.

Focused repository checks run:

```bash
source source_me.sh && python3 -m pytest -q \
  tests/test_pyflakes_code_lint.py tests/test_bandit_security.py \
  tests/test_function_typing.py tests/test_indentation.py tests/test_whitespace.py \
  tests/test_markdown_links.py tests/test_readme_first_paragraph.py \
  tests/test_guidance_doc_format.py tests/test_source_file_line_limit.py
source source_me.sh && python3 -m pyflakes devel/capture_readme_visuals.py
source source_me.sh && python3 -m bandit --severity-level medium \
  --confidence-level medium -q devel/capture_readme_visuals.py
git diff --check
```

The grouped pytest run records **528 passed, 1 failed**. The one failure identifies three
path-like README link labels prefixed with `Reproduce:`; the repository requires that prefix
outside the link text. Direct pyflakes, medium-severity/medium-confidence Bandit, `git diff --check`
and ASCII checks on all eight implementation source/document files pass. No full-suite result is
claimed; the manager will run the existing Python lane after correction/review reports settle.

Disposable logs, hashes, decoded contact sheets and metadata are in ignored
`output/animation_gallery/`; temporary checks are in ignored `tests/_temp/`. These paths are local
working evidence, not public download links or a new recipe format.

## Limits and remaining work

This worker did not run new molecular rendering, scientific preparation, Impress or live published
GitHub playback. Browser normal/reduced-motion behavior, natural repeated loops, sanitized markup,
desktop/narrow layout and link behavior are independently assigned. Fresh specification, quality
and integration verdicts remain separate from this capture receipt. The plan stays active until
the manager reconciles those checks and removes or promotes the temporary tests.

Two bounded presentation corrections were handed to the manager's fresh correction worker while
the product files remained frozen: escape the literal star in bold Mol* appearance labels after
the independent browser found Markdown consuming it, and move `Reproduce:` outside the three
path-like link labels. Recheck affected markup/layout and Markdown links, then update the README
hash and capture repeatability record for the corrected final state. The four asset hashes above
remain valid unless a later explicit visual correction changes them.

## Correction addendum

2026-11-12, `animation_gallery_correction`: corrected only the managed gallery text and its helper
constant. Escape the literal star in both bold Mol* labels using a doubled backslash in the Python
string, use "In order" for the wrapping appearance row, and put `Reproduce:` outside all three
path-like link labels. The README outside its managed block and both literal `picture` blocks are
unchanged from the implementation handoff. The original observations above remain historical.

Two complete warning-as-error captures at 16:00:53 UTC and 16:01:31 UTC reproduce all four media
files byte-for-byte against their hashes above and produce the same corrected README SHA-256:

```text
1c8cc379a46e60b644c3734bd3881616b6886fbbaf960ec76b9be44394d5df71
```

Both captures report the same two 125-frame source hashes recorded above. No encoder, framing,
source, scene, renderer or dependency changes were made. The independent
[animation_gallery_browser.md](animation_gallery_browser.md) image/motion results therefore retain
their asset and picture-markup basis; no repeat motion claim is made by this correction worker.

A fresh unauthenticated GitHub Markdown API POST returned HTTP 200 at 16:01:48 UTC, request ID
`DE1C:15C90F:B67B:248B6:6AF5E2EC`. Its sanitized HTML contains exact
`<strong>Mol* spheres</strong>` and `<strong>Mol* smooth surface</strong>` labels without a trailing
star, the "In order" caption, and all three reproduction anchors with the prefix outside the link.
Their relative source targets exist in the repository; both pictures and reduced-motion sources
remain present. No gallery link targets ignored `output/` files.

Installed Chromium 158.0.8127.18 displayed that fresh HTML inside the actual GitHub shell/CSS using
the original read-only local-image routing technique. At 1280 x 1000 and 390 x 844, corrected caption
text is exact, screenshots are readable, document width equals scroll width and there are no page
errors. Both contexts used reduced motion for stable caption inspection. The sandbox initially
blocked Chromium's macOS service; the authorized unrestricted launch passed. Browser closed and
no server was started. This is prepublication evidence, not live published README acceptance.

Commands and checks:

```bash
source source_me.sh && python3 -W error devel/capture_readme_visuals.py
node output/animation_gallery_correction/probe.mjs
source source_me.sh && python3 -m pytest -q tests/test_markdown_links.py tests/_temp/test_animation_gallery.py
source source_me.sh && python3 -m pyflakes devel/capture_readme_visuals.py
source source_me.sh && python3 -m bandit --severity-level medium --confidence-level medium -q devel/capture_readme_visuals.py
```

The focused run passes all 76 tests; direct pyflakes and medium-severity/medium-confidence Bandit
pass. Capture logs, before/after hashes, read-only API HTML, browser JSON and caption crops are
retained in ignored `output/animation_gallery_correction/`. The full Python lane follows after
the capture, browser and ledger records settle; its actual result follows.

The one full Python run, `source source_me.sh && python3 -m pytest tests/`, records **1,109 passed,
1 skipped, 1 failed** in 2.15 seconds. The sole failure is the existing Unicode violation in
[protein-deep-research-report.md](../protein-deep-research-report.md), with 196 non-ISO-8859-1
characters. `git diff --exit-code HEAD -- docs/active_plans/protein-deep-research-report.md` passes;
the file is unchanged from HEAD. The earlier B108 and README-link failures do not recur. No
suppression or unrelated research-report edit was made. Full-suite output is retained locally as
`output/animation_gallery_correction/full_pytest.log`.

The five correction source/document files pass ASCII checks; `git diff --check` passes. A direct
before/after comparison confirms the README outside the managed block is unchanged. All four
asset hashes were rechecked after browser and Python checks and still match the original receipt.
Product files are frozen for the manager's fresh specification, quality and integration reviews.
After the final result/status edits, the Markdown-link and guidance-format check passes all
76 tests, the five-file ASCII check passes again and `git diff --check` remains clean. The unchanged
research report's SHA-256 is `6f7bf2d2306dc910a814759684b2d7dd8bb519942a4d19de88710db756881fb7`
in both HEAD and the working tree.

## Final closeout

2026-11-12: fresh specification, independent quality and integration reviews all PASS. The
[animation_gallery.md](../workstreams/animation_gallery.md) ledger records completed closeout and
the archived plan. The two task-owned disposable Python checks were removed; the historical counts
above remain the actual earlier runs. Frozen product/media bytes and ignored working evidence are
preserved. Publication and live published README acceptance remain deferred until the human pushes.
