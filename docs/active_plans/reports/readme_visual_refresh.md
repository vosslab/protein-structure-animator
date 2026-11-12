# README visual refresh receipt

Date: 2026-11-12

## Task ledger

| Work | Owner | Target | Evidence and completion |
| --- | --- | --- | --- |
| Refresh landing page and newcomer route | readme-docs | `README.md` | Completed; purpose, limits, completed examples, GroEL first success, and curated links are present. |
| Capture managed visual proof | screenshot-docs | README screenshot block; `docs/screenshots/` | Complete; one-play hexokinase animated WebP and static hexokinase/GroEL comparison added. |
| Review screenshot specification and accessibility | screenshot-docs / manager | README screenshot block and assets | PASS, 96/100; independent reviewer accepted the current README and WebP specification. The reviewer inspected both assets and relied on the current capture receipt for playback and repeat-capture evidence; no rendering or browser rerun. See [readme_specification.md](readme_specification.md). |
| Independent quality review | reviewer | `README.md`, this receipt | PASS, no actionable defects; one nonblocking import-order style note. See [readme_quality.md](readme_quality.md). The reviewer did not rerun rendering, playback, clean installation, Impress, or the full suite. |
| Fresh integration read | integrator | README, changelog, receipt, managed assets | PASS; no remaining task-level gap blocks closeout. The reviewer checked current content, asset hashes and metadata, scientific wording, score arithmetic, user guidance, and changelog consistency. See [readme_integration.md](readme_integration.md). The reviewer did not rerun capture, rendering, browser or Impress playback, clean installation, or the full suite. |
| Apply user format preference | screenshot-docs | README preview, capture helper, human guidance, receipts | Complete: direct quality-90 animated WebP; browser one-play check passed; superseded managed GIF removed afterward. Full example GIF exports remain unchanged. |

## Scope and evidence

The README now presents this repository as a documented collection of native protein-visualization
workflows. Its first-success route renders and encodes the complete GroEL biological assembly.
No application examples, tool guides, or source structures were changed for this refresh.
Dependency changes in the working tree belong to separate concurrent work. The screenshot sentinels remain owned by screenshot-docs.

The README opening is 162 characters. It names reproducible native workflows, teaching animations,
structural choices, editable sources, and playback evidence. Current capabilities and adoption
limits are linked to their example records and verification reports rather than generalized from
source code alone.

The GroEL command was run in this checkout. The first restricted browser launch failed with the
macOS `bootstrap_check_in` permission error; a run with normal macOS browser services completed.
It rendered all 125 frames with 53,858 protein atoms across the fourteen-chain assembly. The
documented encoder then completed. FFprobe measured the resulting MP4 at 640 x 640, 25 fps, 125
frames, and 5.000 seconds. All five downloaded structural inputs passed the recorded SHA-256
checks. This verifies the rendering and encoding path against already installed dependencies; a
fresh environment installation was not repeated.

Commands and checks:

```text
node examples/render_molstar.mjs groel_rotation                         PASS
source source_me.sh && python3 tools/encode_loop.py output/groel_rotation/frames  PASS
ffprobe ... output/groel_rotation/animation.mp4                          PASS: 640x640, 25 fps, 125 frames, 5 s
shasum -a 256 -c examples/input_hashes.sha256                            PASS: 5 inputs
source source_me.sh && pytest -q tests/test_readme_first_paragraph.py tests/test_markdown_links.py  PASS: 59
python3 tests/check_ascii_compliance.py -i README.md                    PASS
python3 tests/check_ascii_compliance.py -i docs/CHANGELOG.md             PASS
python3 tests/check_ascii_compliance.py -i docs/active_plans/reports/readme_visual_refresh.md  PASS
git diff --check                                                        PASS
```

Final receipt synchronization checks:

```text
source source_me.sh && python3 -m pytest tests/test_markdown_links.py tests/test_readme_first_paragraph.py tests/test_guidance_doc_format.py -q  PASS: 65
python3 tests/check_ascii_compliance.py -i README.md                     PASS
python3 tests/check_ascii_compliance.py -i docs/HUMAN_GUIDANCE.md         PASS
python3 tests/check_ascii_compliance.py -i docs/CHANGELOG.md              PASS
python3 tests/check_ascii_compliance.py -i docs/active_plans/reports/readme_specification.md  PASS
python3 tests/check_ascii_compliance.py -i docs/active_plans/reports/readme_quality.md        PASS
python3 tests/check_ascii_compliance.py -i docs/active_plans/reports/readme_integration.md    PASS
python3 tests/check_ascii_compliance.py -i docs/active_plans/reports/readme_visual_refresh.md PASS
git diff --check                                                        PASS
```

## Before and after score

Scores follow `readme-docs/references/scoring_rubric.md`; each category uses its allowed rubric
level. The initial score reflects the README before this refresh. The after score uses current
captured assets and verified browser behavior. Specification, quality, and integration reviews
passed for the final WebP state.

| Category | Before | After | Evidence / remaining work |
| --- | ---: | ---: | --- |
| Purpose, audience, and value (15) | 11 | 15 | Opening now names reproducible teaching workflows and evidence; completed scope is stated directly. |
| Distinctive project identity (15) | 8 | 15 | Native-tool collection and structural/scientific evidence shape the purpose, screenshot story, and examples. |
| Proof and demonstration (20) | 5 | 20 | Authentic endpoint motion and assembly comparison are visible before onboarding, with capture provenance, browser playback, static fallback, and equivalent science prose. |
| Meaningful first success (15) | 0 | 11 | Canonical prerequisites/install/run/outputs are documented and render/encode passed; fresh install was not repeated. Next step: verify this route in a clean environment. |
| Usage and conceptual orientation (10) | 8 | 10 | Representative natural-language request and interpretation boundaries precede deeper docs. |
| Documentation navigation (10) | 8 | 10 | Three example routes and six task/evidence guides are described for newcomer use. |
| Adoption context (5) | 4 | 5 | Tool requirements, ChimeraX license distinction, per-format playback limits, and code/material licenses are explicit. |
| Presentation, accessibility, and currency (10) | 8 | 10 | Current links, commands, alt text, readable 880 px visuals, bounded one-play media, and neighboring still/prose equivalents are checked. |
| **Total** | **52** | **96** | Sum of the eight exact supported rubric levels; specification, quality, and integration reviews passed. |

Strongest gain: proof and demonstration, 5 to 20. The 960 x 600 one-play animated WebP demonstrates the
hexokinase visual, and the 1280 x 800 static comparison provides an accessible motion-independent
view of the endpoints and GroEL assembly. README alt text and adjacent prose preserve the scientific
meaning and limitations.

The animated WebP encodes 60 logical 12 fps samples as 54 frames after identical endpoint
holds coalesce. It lasts 5,000 ms, uses loop field 1 for one play, and is 1,228,594 bytes
(60.3% smaller than the superseded GIF). The static WebP remains byte-identical at 95,118 bytes.
Chromium screenshots changed at about 2.2 seconds and matched after playback at about 5.5
and 6.1 seconds. Repeated capture preserved complete README and asset bytes. The WebP still
animates with reduced-motion preference active; the still and prose remain available.

The user requested animated WebP for the README preview. This supersedes the screenshot skill's
GIF default for this asset, with quality 90, a five-second one-play limit, and the existing
static fallback retained. Full native examples continue to export GIF normally. The capture
helper no longer creates the obsolete palette or temporary video. See
[readme_capture.md](readme_capture.md) for current timestamps, hashes, frame delays, and checks.

README score: 52/100 -> 96/100. The specification review passed at 96/100. The remaining
first-success deduction is a clean-install
verification gap. Follow-up owner: environment-check reviewer; target: the documented README
quick start; evidence: current render/encode passed against installed dependencies. Work: repeat
the listed dependency setup and exact rendering/encoding commands in a clean environment. Success means installing into a clean environment, running the exact GroEL render
and encoder commands, and confirming the documented 640 x 640, 125-frame, five-second output.
This refresh verified the existing installed environment; it does not claim that extra check.

## Completed visual proof

Outcome: show a short, accessible visual proof of the documented molecular workflows near the
README opening.

Owner: screenshot-docs. Completed in the managed block with the exact assets and checks above.

The final-format specification, quality, and integration reviews passed; no review remains open.
The bounded clean-install quick-start verification is the only follow-up recorded above. Final
receipt checks passed: 65 focused Markdown, README-opening, and guidance-format tests; ASCII
compliance for the README, human guidance, changelog, and four review/refresh reports; and
`git diff --check`.
