# Hexokinase visibility specification review

## Verdict

**PASS.** The implementation and recorded evidence meet the selected 0.75 opacity scope in
[hexokinase_visibility.md](../workstreams/hexokinase_visibility.md). I found no blocking gap or
unsupported acceptance claim. This specification review does not replace the pending quality and
integration reviews.

## Coverage

| Requirement | Evidence |
| --- | --- |
| Make protein movement clearer with the selected 0.75 opacity | [render_molstar.mjs](../../../examples/render_molstar.mjs) applies one 0.75 surface opacity regardless of background mode. The approved comparison and manager's final playback inspection are recorded in the workstream. |
| Keep true background alpha, magenta glucose, camera, crop, timing and coordinates | The workstream records 125 native RGBA frames, unchanged imported-coordinate bytes and camera metadata, fixed crop `[190, 74, 497, 531]`, and a 360 by 540 gallery loop with 60 frames, 5000 ms duration and loop count 0. |
| Describe the visibility tradeoff and alpha option accurately | [Hexokinase README](../../../examples/hexokinase_closure/README.md) says both rendering commands use the same opacity, `--alpha` selects background and output, and glucose fades to a faint trace when closed. It separately identifies retained historical opaque files at 0.42. |
| Preserve inputs and unrelated products | `verification.json` records 152 protected files unchanged. The workstream identifies the preserved original inputs, prepared structures, prior opaque outputs, README and ATP/GroEL gallery assets. |
| Refresh the current gallery loop and poster | The workstream records the captured alpha output and matching poster. I recomputed SHA-256 for all six files listed in `frozen_products.json`; every digest matches. |

## Review checks

I inspected the approved workstream, renderer, README and changelog. I recomputed all six frozen
product hashes and confirmed they match `output/hexokinase_visibility/frozen_products.json`. I
relied on the recorded native render, alpha, protected-file and Chromium playback checks; I did not
rerun the render or browser capture.

The local Chromium evidence covers playback on light and dark backgrounds and the reduced-motion
poster through 6500 ms. It does not claim Firefox, Impress, or external publication behavior.
