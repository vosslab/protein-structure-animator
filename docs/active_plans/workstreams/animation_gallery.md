# Animation gallery ledger

## Ownership and state

| Work | Owner | Model | State | Dependency / evidence |
| --- | --- | --- | --- | --- |
| Scope and D1 framing | Root manager | Parent session | Settled | Approved conversation and active plan |
| Helper, README, previews and capture receipt | animation_gallery_implementation | gpt-6.1-sol, high | Implemented; text corrections complete | Original capture receipt plus correction addendum |
| Caption and link corrections | animation_gallery_correction | gpt-6.1-sol, medium | Complete | Two identical corrected captures, 76 focused passes, fresh GitHub sanitation and caption checks; full Python: 1,109 passed, 1 skipped, 1 existing failure |
| Independent browser verification | animation_gallery_browser | gpt-6.1-sol, high | PASS; caption findings resolved separately | Historical browser report plus capture correction addendum; unchanged assets and picture markup |
| Fresh specification review | animation_gallery_specification | gpt-6-luna, high | PASS | Specification report; no blocking finding |
| Fresh quality review | animation_gallery_quality | gpt-6.1-sol, medium | PASS | Quality report; no required fixes; 77 focused cases |
| Fresh integration review | animation_gallery_integration | gpt-6-luna, high | PASS | Integration report; no blockers |
| Final closeout | animation_gallery_closeout | gpt-6.1-sol, medium | Complete; plan archived | Records reconciled; two task-owned temporary checks removed; no publication or commit |

## Settled decisions

- D1: exactly one fixed aspect per clip. GroEL is 640 x 360 widescreen; hexokinase is 360 x 780
  phone-style portrait, displayed at 240 pixels wide. Center with white padding and preserve
  molecular ratios; do not stretch, enlarge, switch aspect or generate aspect variants.
- D2: continuous five-second quality-90 WebP loops, 60 logical samples at 12 fps, with matching
  static posters selected by reduced-motion media queries and independently linked in text.
- D3: native GitHub README gallery before setup, canonical Rust first, Mol* hexokinase second,
  then three clearly labeled static 3N0G appearances. No website or catalog/configuration schema.
- D4: preserve all verified molecular inputs/full-quality deliveries and both historical README
  assets. Reuse existing source frames; preview capture is not a fresh molecular-render claim.

## Evidence boundaries

Source science, coordinate fidelity and previous full-quality playback remain owned by the example
records. This work verifies presentation derivatives only. The capture receipt records observed
checks; browser and independent review results must be recorded by their respective owners.
Actual unpublished GitHub page playback remains untested until the human publishes the changes.

## Correction handoff

The fresh correction worker escaped the literal star in bold Mol* appearance labels, changed the
wrapping-row legend to "In order" and moved `Reproduce:` outside the three path-like link labels.
Two corrected captures are byte-identical; final README SHA-256 is
`1c8cc379a46e60b644c3734bd3881616b6886fbbaf960ec76b9be44394d5df71`. All four media hashes,
source-frame hashes and both literal picture blocks remain unchanged. The fresh GitHub sanitation
and desktop/narrow caption checks pass; 76 focused tests, direct pyflakes and Bandit pass. The full
Python lane records 1,109 passed, 1 skipped and the single existing Unicode research-report failure;
that report is unchanged from HEAD. Product files remain frozen and all three fresh reviews pass.

## Completed closeout

The accepted scope is complete and the plan is archived. The browser's original README hash and
caption findings remain historical observations; the capture correction addendum records the fresh
HTTP-200 sanitation and desktop/narrow caption checks that resolved them. No post-correction
motion rerun is claimed. Scientific preparation, coordinate fidelity, visual quality, playback and
fresh-process reproduction retain their separate example evidence.

Only the task-owned, ignored `tests/_temp/test_animation_gallery.py` and
`tests/_temp/verify_animation_gallery.py` were removed. Disposable captures, logs, probes and contact
sheets remain under ignored `output/`. Historical test counts describe their actual runs before
cleanup; no new full-suite result is claimed. Four new WebPs remain intentional reviewable additions
outside ignored output; historical assets remain intact. Only the archived plan is staged.

Final receipt checks cover 85 focused cases: the grouped Markdown-link, README-opening and
guidance-format run passed 84 cases and found one stale design-decision archive link; after its
target was corrected, that exact case passed. Eight closeout documents pass ASCII checks;
working-tree and cached whitespace checks pass. Final README, helper and four asset hashes match
the frozen correction/capture receipt. No source, asset or unrelated change was staged or committed.

Publication and a live published README check remain deferred until the human pushes. Actual
iPhone/Safari, new previews in Impress and molecular rerendering were outside this task's checks.

## Links

- [animation_gallery.md](../../archive/animation_gallery.md).
- [Capture receipt](../reports/animation_gallery_capture.md).
- [Browser verification](../reports/animation_gallery_browser.md).
- [animation_gallery_specification.md](../reports/animation_gallery_specification.md).
- [animation_gallery_quality.md](../reports/animation_gallery_quality.md).
- [animation_gallery_integration.md](../reports/animation_gallery_integration.md).
