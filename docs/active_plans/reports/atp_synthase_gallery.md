# ATP synthase alpha gallery

## Scope and status

2026-11-12, `alpha_gallery_implementation`: applying the user-invoked `readme-docs` skill, followed
by `screenshot-docs`. The approved [plan](../../archive/atp_synthase_alpha.md) uses native rendered
protein artifacts as the evidence. A window capture or invented application interface would not
demonstrate these outputs. Existing static appearance comparisons and the native Rust quick start
remain discoverable. Historical opaque example media and all six previous gallery assets remain
untouched; their pre-capture hashes are recorded locally.

Captured twice after the manager froze all three final native sequences and issued the capture
go-ahead. The ATP sources use the corrected proper camera rotation, determinant +1. Six new assets
and README are frozen for independent browser checks and reviews. This receipt establishes decoded
alpha/framing and inspected contact sheets; it does not establish application playback, scientific
coordinate validation or fresh molecular replay.

## Framing and layout

The gallery opens with ATP synthase, followed by GroEL, hexokinase and the retained static 3N0G
appearance options. Teaching captions name the motion class and its scientific limits. Each example
has a prompt, reproduction link, transparent WebP link and independently accessible static poster.
Each picture selects its own matching poster when the reader requests reduced motion.

| Example | Native source directory under `output/` | Gallery canvas | README width |
| --- | --- | --- | --- |
| ATP synthase | `atp_synthase_motor/frames` | 480 x 720 | 360 |
| GroEL | `groel_rotation_alpha/frames` | 640 x 480 | 640 |
| Hexokinase | `hexokinase_closure_alpha/frames` | 360 x 540 | 360 |

The capture helper validates all 125 sequential RGBA sources per clip, including frames omitted
from the preview. It derives one alpha-bound union containing every nonzero-alpha atom, outline,
membrane element and label, and adds ten source pixels on each side. It applies this single crop to
every sampled frame, uniformly downsizes only if necessary, and centers the result on one fixed
transparent canvas. White atoms retain their native alpha. No white-pixel keying, independent frame
recentering, enlargement or molecular stretching occurs. The ATP 480 x 720 canvas retains every
label and the complete membrane/staging annotation.

New tracked assets use distinct names:

- `atp_synthase_motor.webp` and `atp_synthase_motor_poster.webp`.
- `groel_rotation_alpha.webp` and `groel_rotation_alpha_poster.webp`.
- `hexokinase_closure_alpha.webp` and `hexokinase_closure_alpha_poster.webp`.

All are under `docs/screenshots/`. The helper records source directories, crops and concatenated
125-frame hashes in ignored `output/atp_synthase_gallery/capture_manifest.json`.

The measured crops use exclusive right/bottom coordinates. These are whole-motion alpha crops,
not independent per-frame molecular centers:

| Example | Padded source crop | Crop after downsize | Fixed placement |
| --- | --- | --- | --- |
| ATP synthase | `(9, 17, 471, 723)` | 462 x 706, unchanged | `(9, 7)` |
| GroEL | `(21, 30, 617, 596)` | 505 x 480 | `(67, 0)` |
| Hexokinase | `(190, 74, 497, 531)` | 307 x 457, unchanged | `(26, 41)` |

ATP's crop includes three transparent rows beyond the original source to preserve the full
ten-pixel annotation margin. Pillow pads those rows transparently. Only GroEL needs downsampling;
all frames in each clip use the same crop, scale and placement.

## Encoding and preservation

The existing 60-sample contract remains: source index `round(index * 125 / 60)` for indices 0-59,
without a duplicated endpoint. Durations `[83, 84, 83]` repeated twenty times sum to 5,000 ms.
Animated WebP uses Pillow at quality 90 and loop 0. Matching posters use `cwebp -q 90`, starting
from the same cropped first source sample. Temporary PNGs stay in the OS temporary directory.

The fixed internal paths and direct subprocess argument lists retain ASVS 5.3.2 and 1.2.5 handling.
No new dependency, recipe schema, renderer or application is introduced. The helper only writes its
six new gallery assets, its capture manifest and the README managed block.

The pre-capture manifest in ignored `output/atp_synthase_gallery/preservation_before.json` records
all six previous gallery assets, eight full-quality GroEL/hexokinase media/poster files and seven
downloaded structural inputs. These twenty-one existing files will be rehashed after capture.
All twenty-one files remain byte-identical after both captures. Before/after hashes also confirm
all 375 native PNGs remain unchanged. Original structural inputs remain outside this worker's edit
scope. The broader source-owner preservation inventory is separate evidence.

Observed tools are Pillow 13.0.0 and cwebp 1.6.0 (libsharpyuv 0.4.2), not dependency pins. The three
animations exceed the screenshot skill's approximate 1 MB hint because the approved quality-90,
60-frame and fixed-canvas contract preserves molecular detail. No quality reduction or extra
configuration was introduced to meet that hint.

## Assets and repeatability

Both captures, at 2026-11-12 16:46:19 UTC and 16:46:33 UTC, reproduce all six assets and README
byte-for-byte. Each animation decodes to 60 unique frames, 5,000 ms total and loop flag 0. Posters
are one-frame files with matching canvas/framing. All 183 decoded images have genuine alpha 0 in
the background. Each decoded alpha channel equals the fixed-framed source sample pixel-for-pixel,
including partially transparent edges and white atom pixels. No color-based background removal
is involved.

| Asset | Pixels | Bytes |
| --- | --- | --- |
| `atp_synthase_motor.webp` | 480 x 720 | 2,780,856 |
| `atp_synthase_motor_poster.webp` | 480 x 720 | 71,800 |
| `groel_rotation_alpha.webp` | 640 x 480 | 4,346,884 |
| `groel_rotation_alpha_poster.webp` | 640 x 480 | 63,660 |
| `hexokinase_closure_alpha.webp` | 360 x 540 | 2,242,604 |
| `hexokinase_closure_alpha_poster.webp` | 360 x 540 | 30,776 |

SHA-256 values:

```text
atp_synthase_motor.webp
a631b8f51f7da10c7fe17ee78562df868aac8cead1ddfa1ad5f26bfc6344956c
atp_synthase_motor_poster.webp
19a6ee4a0f63855179548996ffe32e8f9179595677c3dc83d6bb97ef5dc981a1
groel_rotation_alpha.webp
f983565b9b9c31dad1fc8e55d2395e664ca5509a8cedef179c1a94ff9de80dfa
groel_rotation_alpha_poster.webp
8c232fb67d1b08a1795fb367266dccb3c29fccf98324bc7fbec6f6c5d251dcec
hexokinase_closure_alpha.webp
f331a55d7375304c852f45bf5fb87bc9395d95cce30440bca8b3dd74b204c2d7
hexokinase_closure_alpha_poster.webp
4f894c5103bc029ef300ff5f418ab76617e0929b7605281a84699703eaa936e8
README.md
3c0eec7e0cec82da3758fb30a62253ad86e942b324b1e8895623418bac45aa42

125 native ATP frames, concatenated in order
10555d1df2968660c11301baf8a046c2e368b089345c419940df9a357c3c3881
125 native GroEL frames, concatenated in order
27ec42998864a19b1bfb695ea003b124f533094404c3bace0f081e66b31669cd
125 native hexokinase frames, concatenated in order
da2408f17284fd77ff9ca70e93e2a9ff28813600f0587bd9ec3134de4353be3a
```

## Visual inspection

Decoded samples 0, 12, 24, 36, 48 and 59 were inspected over white and GitHub dark `#0d1117`.
GroEL and hexokinase native/display sizes are identical (640 x 480 and 360 x 540). ATP was inspected
at native 480 x 720 and README display 360 x 540. Eight contact sheets remain in ignored
`output/atp_synthase_gallery/`, named by asset, width and light/dark background.

All three proteins fill their fixed canvases without clipped outlines. GroEL retains chain colors
and complete assembly contours while its silhouette rotates. ATP's stationary housing, labels and
membrane keep their registration while the amber shaft and c-subunit marker move; labels remain
legible at 360 pixels wide. Hexokinase's blue lobes and fixed magenta glucose remain visible over
both themes. Surface occlusion changes glucose's apparent intensity during closure, as in the
native source. No additional palette edit was made in capture. These sampled visual observations
do not substitute for continuous browser playback or molecular checks.

## Reproduction and checks

Two disposable checks in `tests/_temp/test_atp_synthase_gallery.py` pass: the all-motion union keeps
a moving opaque white atom and transparent padding without enlargement; the managed README block
is idempotent and includes three reduced-motion fallbacks plus retained appearance options.

```bash
source source_me.sh && python3 -m pytest -q tests/_temp/test_atp_synthase_gallery.py
source source_me.sh && python3 -m pyflakes devel/capture_readme_visuals.py
source source_me.sh && python3 -m bandit --severity-level medium \
  --confidence-level medium -q devel/capture_readme_visuals.py
source source_me.sh && python3 -W error devel/capture_readme_visuals.py
source source_me.sh && python3 output/atp_synthase_gallery/verify_capture.py
source source_me.sh && python3 -m pytest -q tests/_temp/test_atp_synthase_gallery.py \
  tests/test_readme_first_paragraph.py tests/test_markdown_links.py tests/test_guidance_doc_format.py
```

The final grouped focused run passes 100 tests. Direct pyflakes, medium/medium Bandit, owned-file
ASCII checks and `git diff --check` pass. An earlier preparation run had 94 passes and one missing
link to the concurrently unfinished ATP render report; the final run includes that report and
passes. Four scoped helper checks for typing, indentation, whitespace and source-file line budget
also pass. The first README prose paragraph stays plain and below 350 characters, and the native
GroEL quick start remains intact. This worker did not rerun it because molecular replay belongs
to the separately assigned replay check.

Ignored local evidence includes capture logs, initial/final hashes, `capture_manifest.json`,
`source_before.json`, `determinism.json`, `preservation_before.json`, `verification.json`,
`verification_summary.json`, the eight contact sheets and the disposable verification script.
The manager will remove or promote the task-owned temporary tests during final closeout.

Browser playback, fresh molecular replay, scientific verification and independent reviews are
separate manager-owned evidence. This worker has not performed them.
