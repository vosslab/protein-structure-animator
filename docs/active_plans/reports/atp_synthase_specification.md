# ATP synthase specification review

## Verdict

**PASS.** The implementation and recorded evidence meet the approved scope in
[atp_synthase_alpha.md](../../archive/atp_synthase_alpha.md). I found no blocking specification gap
or unsupported acceptance claim. This review covers specification compliance; it does not replace
the separate quality and integration reviews.

## Coverage

| Requirement | Evidence |
| --- | --- |
| Use canonical native Rust Goodsell rendering for the new ATP example | [atp_synthase_render.md](atp_synthase_render.md) and [atp_synthase_replay.md](atp_synthase_replay.md) record the renderer identity, source snapshot, native pixels and replay. |
| Show a fixed-camera rotor moving against a stationary stator with a useful cutaway, membrane context and sparse labels | [atp_synthase_science_verification.md](atp_synthase_science_verification.md) verifies the proper determinant +1 camera, complete G-R rotor, stationary assembly, fixed scenes and coordinate handoffs. The render and playback reports cover the cutaway, membrane, labels, framing and inspected motion. |
| Deliver transparent animated WebP and posters | [atp_synthase_gallery.md](atp_synthase_gallery.md) records genuine source alpha, decoded alpha equality, 60-frame loops and posters. [atp_synthase_playback.md](atp_synthase_playback.md) records browser composition and motion. |
| Use one shape-appropriate aspect and one whole-motion crop per clip | The gallery report records 480 x 720 ATP, 640 x 480 GroEL and 360 x 540 hexokinase canvases, one union crop over all 125 source frames, fixed placement and no enlargement. |
| Describe motion and structural limits accurately | [atp_synthase_motor/README.md](../../../examples/atp_synthase_motor/README.md) and the gallery text identify authored rigid staging and disclose frozen-head clashes; neither claims catalytic dynamics, kinetics or a validated trajectory. |
| Preserve inputs and established outputs, then reproduce the delivery | The final replay report records all 437 protected historical files and 21 prior gallery/input/media entries unchanged, all eight replay helper/template/input hashes matching, and exact reproduction of the core prepared files, rendered frames, encoded media, six gallery assets and README. |

## Independent checks

I inspected the approved plan, task ledger, animation guidance, ATP source and example README,
gallery/encoder changes, existing alpha callers, and the science, rendering, gallery, playback and
final replay receipts. I recomputed SHA-256 values for the README, gallery helper and six tracked
WebP/poster assets. The README hash is
`3c0eec7e0cec82da3758fb30a62253ad86e942b324b1e8895623418bac45aa42`; all seven values match the
recorded gallery/playback evidence.

The replay report classifies its eight non-identical baseline entries individually: three render
records differ only in elapsed time, the ATP renderer appends its documented log, Mol* writes a
fresh state snapshot with generated IDs, and three diagnostic files overlap independent work.
Those differences do not weaken the claimed equality for source frames, final media, gallery assets,
README or preserved historical files. The report does not claim a blanket byte-identical result for
all 1,483 files.

## Limits

Playback evidence covers actual Chromium/Firefox motion and reduced-motion posters using the
sanitized README with local unpublished image bytes, plus actual Impress playback of the ATP MP4.
It establishes neither behavior after publication nor animated WebP playback in Impress or exact
display pacing. The recorded broad Python run is not fully green: one unchanged research-report
Unicode failure remains; the temporary naming issue was repaired and its focused gate passes.
These limits are disclosed and do not contradict the approved acceptance scope.

No tests or renders were run for this review. The verdict relies on the recorded evidence plus the
source and hash inspection above.
