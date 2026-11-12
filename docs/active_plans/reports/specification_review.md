# Specification compliance review

Status: PASS for specification compliance within the recorded scientific and application limits.
Reviewed 2026-11-11 against the approved
[protein_animation_toolbox.md](../../archive/protein_animation_toolbox.md).
This is a specification review, not the independent code-quality review or integration signoff.

## Scope and rules

Read the plan, repository agent instructions, applicable repository, Python, pytest and Markdown
rules, [ANIMATION_GUIDANCE.md](../../ANIMATION_GUIDANCE.md),
[HUMAN_GUIDANCE.md](../../HUMAN_GUIDANCE.md), example sources and READMEs, tool guides, and the
available evidence reports. Repository Python checks used `source source_me.sh && python3`.
No production source, tests or configuration were changed, and no browser or GUI was launched
by this reviewer. Other owners retain the serialized graphics work.

Apply **Keep it simple (KISS)**, **Use the scientific method**, **Reviews should simplify** and
**Focus on important issues** from [REPO_STYLE.md](../../REPO_STYLE.md). The pytest policy favors
stable behavior and regards tests tied to incidental structure, dates, defaults or external state
as fragile. The permanent encoder test protects the actual 125-frame delivery contract; native
and rendering experiments appropriately supply temporary evidence rather than third-party tests.

## Screenshot correction accepted

D7 is accepted for the renderer handback. In
[render_molstar.mjs](../../../examples/render_molstar.mjs), lines 151-157, the screenshot settings
now use `viewportScreenshot.behaviors.values.next`. The installed Mol* implementation exposes
`values` through a getter, reads that behavior in `getSize`, and uses the resulting custom size
in its draw path. This fixes the demonstrated ignored-assignment failure using the native API.

An independent bootstrap-Pillow read measured all eight current
`output/appearance_3n0g/frames/frame_000.png` through `frame_007.png` and `surface.png` at
640 x 640. Offline inspection of the first sphere frame and the surface preview shows the full
structure with whitespace around it. No crop change is required. This acceptance does not extend
to pre-fix hexokinase/GroEL outputs or establish final encoded timing or application playback.
The owner records its original correction evidence in
[screenshot_dimensions_fix.md](screenshot_dimensions_fix.md).

## Milestone coverage

The implementation matches the approved native-tool collection. It adds example scripts, focused
guides and one small encoder rather than a new application, framework, recipe schema or adapter
layer. Blender is excluded from the initial route. No architectural drift was found.

| Milestone | Implemented coverage | Acceptance boundary |
| --- | --- | --- |
| M1 | 3N0G selection, Illustrate command cards, eight fixed-camera Mol* views, separate surface and native snapshots; corrected PNG dimensions independently verified | Accepted from final appearance comparison and fresh repeated-render evidence |
| M2 | Same-protein endpoints, explicit selections and stable-region fit, native eased morph, separate fixed glucose, checked PDB fallback, encoder and all documented delivery paths | Scientific/native/import/render/media/browser checks accepted; shared Impress acceptance remains in M4 |
| M3 | Full 1OEL assembly mmCIF, fourteen-chain/53,858-protein-atom check, opaque chain-colored spheres and full-turn camera sequence using the same renderer | Assembly/import/rotation/media/browser checks accepted; shared Impress acceptance remains in M4 |
| M4 | Input downloader and hashes, example commands, native sources/settings, provenance, licensing, tool/agent guidance, fresh command replay, browser playback and actual Impress slideshow | Accepted from the final reports and synchronized status documentation; quality/integration reviews remain separate |

## Scientific and delivery boundaries

[structural_verification.md](structural_verification.md) records fresh native preparation with
identical coordinate hashes; 125 distinct samples; 3,651 matched protein atoms without further
morph loss; representable PDB identities; checked endpoint geometry; and independently compared
fixed-glucose registration. The PDB fallback follows an observed native mmCIF trajectory failure,
not a convenience-based loss of molecular information. All five original input hashes passed an
independent `shasum -a 256 -c examples/input_hashes.sha256` run during this review.

The 1.84 angstrom open-state glucose contact is explicitly disclosed in both the example and
evidence. Fixed glucose staging is required by the plan; retaining this qualified illustration
does not assert a physical open-state complex, binding pathway, energy or kinetics. Transparency
and overlapping front/back surface detail are disclosed.

GroEL uses biological assembly 1 and preserves the multi-character chain identities in mmCIF.
The structural report independently verifies the deposited assembly operators, fourteen subunits,
omitted waters and unresolved tails, and the construct mutations. Coordinate constancy is kept
separate from viewpoint motion. The final corrected renderer replay preserves all 54,156 imported
model keys, including waters, in exact source order. No structural identity or numeric handoff
acceptance item remains open.

Native CXS restoration in a separate process retains the forward trajectory's 125 coordinate
sets and all 3,651 identities in order. Maximum component difference is 0.0000038143 angstrom,
measured native-session storage rounding. Glucose remains the separate documented mmCIF input.
The report checks actual outputs and logs because ChimeraX process exit 0 alone can hide a
script exception.

This reviewer also inspected the final hexokinase and GroEL contact sheets and the restored
hexokinase still in `output/render_delivery/`. Glucose remains visible in the sampled open,
intermediate and closed views. The pale translucent surface overlaps front and back detail as
disclosed. Both objects remain inside the frame. GroEL retains its ring cavity and visibly
changing chain-colored viewpoints, with near-matching first/last samples. These stills support
visual acceptance; they do not establish temporal playback or timing.

The media helper specifies 25 fps, 125 frames, GIF/WebP infinite looping, MP4 repeat as a player
setting, and a poster. Source intent is not accepted as proof of encoding or application playback.
Documented application-specific format limits are allowed by the plan. Successful media import
alone is insufficient evidence of playback.

[render_delivery_verification.md](render_delivery_verification.md) now supplies final measured
media evidence: 640 x 640, 125 decoded frames, five seconds, 40 ms GIF/WebP samples and infinite
image loops, H.264/yuv420p MP4 at 25 fps with a full error-free decode, and frame-0 posters.
Fresh Chromium command replays reproduce all three rendered examples, with no interactive
adjustments. Retained native scenes restore in separate fresh viewers with intended components,
representations, alpha and camera framing. Mol* recalculates clip/fog radius values, while actual
foreground bounds stay identical and raw image differences remain very small. This disclosed
native variability is compatible with the plan; exact pixel/state identity is not required.

Chromium and Firefox both demonstrate advancing MP4 time and decoded frames plus native loop
wrap. GIF/WebP screenshots change inside each media rectangle in both browsers for both examples.
The review inspected the final report and underlying media, browser-playback and native-restoration
JSON; these application observations establish browser playback separately from file decoding.

[impress_verification.md](impress_verification.md) records actual slideshow playback for both
animations as GIF and MP4. This reviewer independently viewed their native-window contact sheets,
PID/title/timed capture records and RGB crop comparison. Both formats have eight distinct
protein-area captures for each animation in real LibreOffice `Presenting:` windows. Final source
hashes are retained in the probe manifest. This satisfies the useful teaching-slide delivery gate.

Animated WebP embedded as an ODP image shape instead displays a blank area in this tested route
and installation. The report correctly makes no broader claim about all WebP import routes or
LibreOffice releases. Exact slideshow fps and wall-clock cycle duration are unmeasured; GIF
appeared slower than MP4. These application limits do not contradict the separately verified
five-second, 25-fps encoded deliveries or require every format to play in every application.

## Documentation and dependencies

The root README labels working examples with final reviews in progress. A final claim correction
now separates the demonstrated 3N0G appearance comparison from the hexokinase/GroEL playback
evidence; this reviewer rechecked the corrected wording. Example guides
record structural records, dates, hashes, omissions, motion interpretation, native settings,
commands, tested versions and licenses. ChimeraX's separate license is explicit; it is an approved
preparation component, not represented as open source. Original Goodsell reference art is
attributed and not redistributed.

[dependency_verification.md](dependency_verification.md) records open-ended current compiler and
compatibility aliases, clean installation and lint evidence. Its separate TS18003 empty-TypeScript-
glob shell-gate limitation does not establish an animation failure and does not justify dummy
application source. It must remain disclosed rather than being described as a full gate pass.

The central report, ledger, media guide and changelog now reflect the final technical evidence and
its WebP/pacing limits. The remaining review references are bookkeeping for separate quality and
integration acceptance. Do not archive the active plan while those required reviews are outstanding.

## Final verdict

M1-M4 meet the approved specification within the explicit scientific and application limits.
No specification blocker or architectural drift remains. D7 is accepted both as a bounded native
correction and through the final all-example corrected render/encoding checks. Original structural
inputs and research material remain preserved. No unplanned application or framework was added.

The specification review is complete. Code-quality and integration approval, disposable experiment
cleanup, and final plan archival are separate closeout responsibilities. The record must not claim
a full repository test or shell-gate pass: the preserved research-report Unicode failure and
empty-TypeScript-glob TS18003 limitation remain separately disclosed.

Skipped here: independent GUI/browser launches and a broad test-suite rerun. Retained captures and
owner-run results were reviewed directly; exact Impress pacing and alternative WebP insertion
routes remain unverified.
