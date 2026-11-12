# Animation gallery browser verification

## Result and scope

2026-11-12: PASS for the frozen gallery assets, native WebP motion, reduced-motion posters,
responsive sizing and visual readability. Two appearance-caption corrections remain below.
This is a prepublication local DOM preview using GitHub's live shell/CSS and actual GitHub API
sanitation. The new gallery was not published or checked as a live repository README.

The checked source is [README.md](../../../README.md), SHA-256
`2e75b96a4d0dfeab58367984be0a2ab02e531f7082f16a2e1b5b1533e5dda3c3`.
The implementation owner froze README, helper and assets before this verification. README and
all seven displayed image hashes remained unchanged through the browser run.

## Caption findings

Resolved 2026-11-12: [animation_gallery_capture.md](animation_gallery_capture.md#correction-addendum)
records corrected sanitation and desktop/narrow caption checks. The original hash and observations
below remain historical; assets and picture markup are unchanged, and motion was not rerun.

- [README.md](../../../README.md), lines 67-68: the internal star in `**Mol* spheres**` and
  `**Mol* smooth surface**` conflicts with Markdown emphasis. GitHub's actual sanitized output is
  `<em><em>Mol</em> spheres</em>*` and `<em><em>Mol</em> smooth surface</em>*`. The visible labels
  put the literal star after the representation instead of after Mol. Escape the internal star.
- The same caption starts "Left to right", but the three images form a vertical column at
  390 pixels. "In order" accurately describes both arrangements.

These findings were sent to the manager and implementation owner without changing product files.
The manager assigned a fresh correction worker, including a separate link-label style correction.
The worker should recheck corrected sanitation, links and responsive caption layout. The image
and motion evidence below remains applicable if the assets and picture markup stay unchanged.

## GitHub sanitation and setup

An unauthenticated `POST https://api.github.com/markdown` used the complete frozen README with
`mode=gfm` and `context=vosslab/protein-structure-animator`. The response was HTTP 200 at
`Thu, 12 Nov 2026 15:56:47 GMT`, request ID `DAB6:3287C8:1B01C3:557924:6AF5E1BF`.
The response retained both `picture` elements, both `source` elements with
`media="(prefers-reduced-motion: reduce)"` and poster `srcset`, the animated `img` elements,
their widths and alt text, and ordinary poster/reproduction anchors. GitHub wrapped each picture
in `themed-picture`.

Installed Playwright drove Chromium `158.0.8127.18`, headless, with fresh contexts for each case.
Each context loaded the actual public GitHub repository page and its CSS, replaced only the
Markdown article with the API response, and mapped image requests to exact local file bytes.
The mapping used an unpublished `raw.githubusercontent.com/.../gallery-preview/` route fulfilled
by Playwright; it did not publish files, change animation frames or simulate animation. There was
no local server to leave running. Browser contexts and browser were closed.

The sandboxed launch hit macOS `bootstrap_check_in ... Permission denied`. The authorized
unrestricted native-service launch succeeded. No browser or dependency installation was needed.
The source/alt/anchor checks concern retained markup and existing repository targets. Remote
navigation to the unpublished poster URLs was not tested. In the injected fixture, API-relative
anchors alone do not reproduce GitHub's later repository-path rewriting, so their resolved DOM
URLs are not a link-navigation acceptance result.

## Asset decode

Pillow decoded every stored frame, and an independent RIFF parser read animation durations and
loop metadata. Every decoded frame retained its clip's one fixed canvas. Each poster is static
and has exactly its associated clip's intrinsic dimensions.

| Asset in docs/screenshots | Pixels | Frames | Duration | Loop | Bytes |
| --- | --- | --- | --- | --- | --- |
| [groel_rotation_demo.webp](../../screenshots/groel_rotation_demo.webp) | 640 x 360 | 60 | 5,000 ms | 0, infinite | 1,997,696 |
| [groel_rotation_poster.webp](../../screenshots/groel_rotation_poster.webp) | 640 x 360 | 1 | Static | None | 28,934 |
| [hexokinase_closure_loop.webp](../../screenshots/hexokinase_closure_loop.webp) | 360 x 780 | 60 | 5,000 ms | 0, infinite | 1,093,058 |
| [hexokinase_closure_poster.webp](../../screenshots/hexokinase_closure_poster.webp) | 360 x 780 | 1 | Static | None | 14,216 |

SHA-256, in the same order:

```text
33dce85f347f72b2bfb7ee5fc55249bc9e6933c186c0cd5f2fd245675422ce50
3c7927d03ef44ef29a4005c65955711c39ec6681e9816431a3cc3c088e579260
1647ffd9422aef6e96e2e715c2252e3357a64d8287b4e0c7c1afaf9b742e577d
e7d6ccde5c1a93feb2ec5918ccc453142e37beee4fc42ed0a45669683f558b6f
```

## Browser results

The desktop viewport was 1280 x 1000; the narrow viewport was 390 x 844. Both normal and
`prefers-reduced-motion: reduce` contexts passed. The actual GitHub shell supplied its viewport
metadata and responsive Markdown styling.

| Viewport | GroEL display | Hexokinase display | Document width / scroll width |
| --- | --- | --- | --- |
| Desktop, both preferences | 640 x 360 | 240 x 520 | 1280 / 1280 |
| Narrow, both preferences | 324 x 182.25 | 240 x 520 | 390 / 390 |

All clip/poster rectangles preserve 16:9 or 6:13 respectively, fit inside the viewport and remain
unsquashed. All five displayed images have nonempty alt text. The three appearance images wrap
on narrow screens. All four contexts reported no page errors.

For each normal-motion clip, native `img` screenshots were sampled naturally at approximately
0, 0.7, 1.6, 2.7, 4.7, 5.6 and 6.6 seconds after sampling began. No seeking, image replacement,
canvas animation, frame injection or animation restart was used. Desktop samples contained six
distinct RGB images per clip; narrow samples contained seven. The 5.6-to-6.6-second captures still
differ, demonstrating continuing browser animation after a full five-second interval. RGB
comparisons explicitly discard alpha, avoiding an alpha-only difference claim.

For reduced motion, `currentSrc` selected the corresponding poster for both clips. Three native
captures at approximately 0, 0.9 and 5.6 seconds were RGB-identical in all four clip/viewport cases.
Normal mode selected the animated asset. Source selection and intrinsic dimensions were read
from the browser's actual image elements.

The native image crops and quality-90 WebP readability crops show a complete, unclipped colored
GroEL assembly and the pale blue hexokinase surface with distinguishable magenta glucose.
Headings, short teaching descriptions and ordinary poster/reproduction links remain readable at
both widths. The tall hexokinase canvas has white margins consistent with the requested fixed
phone aspect. The real GitHub sticky README navigation appears in whole-article screenshots;
isolated native-image captures and gallery readability crops were also inspected.

Decoded frame contact sheets include frames 0, 15, 30, 45, 59 and 0 again. Both seams are visually
consistent with adjacent steps. Whole-image RGB mean absolute differences for last-to-first are
9.400 for GroEL versus 9.153/9.368 for its first/last adjacent steps, and 0.656 for hexokinase versus
0.560/0.839. These support the visual seam inspection; they do not establish exact display fps.

## Commands and retained evidence

Commands, from the repository root:

```bash
node output/animation_gallery_browser/probe.mjs > output/animation_gallery_browser/probe.log 2>&1
source source_me.sh && python3 output/animation_gallery_browser/analyze.py > output/animation_gallery_browser/analyze.log
```

Ignored `output/animation_gallery_browser/` retains the API HTML, fetched public shell, probe,
decode/RGB analysis, exact browser timing and source-selection JSON, logs, native image samples,
full-article screenshots, gallery readability crops and seam contact sheets. All retained named
captures/contact sheets are quality-90 WebP; transient PNG captures were removed after conversion.

This check did not rerender molecules, regenerate product assets, run a full test suite, replay
structural preparation, test Impress, publish the gallery or test a newly published GitHub page.
The corresponding scientific and source-preservation evidence remains separately owned.
