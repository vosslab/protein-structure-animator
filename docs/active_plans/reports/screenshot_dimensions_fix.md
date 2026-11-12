# Screenshot dimensions fix

## Result

Mol* exposes `viewportScreenshot.values` as a getter. Assigning to it silently left the helper at
its viewport-sized default. The renderer now updates the native `behaviors.values` observable with
the requested 640 x 640 custom resolution. The helper's draw path uses the full-frame crop; no crop
change was needed.

## Verification

`node examples/render_molstar.mjs appearance_3n0g` completed in Chromium 158.0.8127.18 with Mol*
5.13.1. Pillow measured all eight frame PNGs and `surface.png` at 640 x 640. I inspected
`frame_000.png` and `surface.png`; both show the full structure with whitespace around its edges.

The installed Mol* `viewport-screenshot.js` confirms `values` is getter-only and `behaviors.values`
is the writable behavior used by the screenshot helper.

Scoped checks passed:

- `npx prettier --check examples/render_molstar.mjs`
- `npx eslint --config eslint.config.local.js examples/render_molstar.mjs`
- Pillow dimensions check through `source source_me.sh && python3`

The renderer also exports imported atom identities for GroEL in `imported_coordinates.json`; that
identity output was added for the main renderer's later GroEL replay and was not verified here.
