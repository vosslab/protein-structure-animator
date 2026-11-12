# Mol* rendering

Mol* is MIT-licensed. Its native spacefill representation and illustrative coloring support a
Goodsell-inspired appearance; `molecular-surface` is a distinct smooth representation. Primary
references: [illustrative style](https://molstar.org/viewer-docs/tips/illustrative-style/),
[source and license](https://github.com/molstar/molstar), and
[movie export](https://molstar.org/viewer-docs/tips/movie-export/).

## Native browser invocation

Install current npm dependencies and Playwright browsers using [TOOLS.md](../TOOLS.md).
The examples load the installed Mol* viewer bundle into a temporary Chromium page and use its
native structure builders, representations, camera, screenshot and snapshot APIs:

```bash
node examples/render_molstar.mjs appearance_3n0g
node examples/render_molstar.mjs hexokinase_closure
node examples/render_molstar.mjs groel_rotation
```

Preparation commands and source selections belong to each example README. Run graphics examples
sequentially on this Mac. Browser startup requires permission to use normal macOS application
services in restricted agent environments. Rendering itself needs no visible browser or manual
interaction. Do not use the user's everyday browser profile.

## Settings and handoffs

[render_molstar.mjs](../../examples/render_molstar.mjs) retains the native settings. It uses a
640 by 640 white canvas, orthographic projection, a fixed target and scale, outlines and ambient
occlusion. It turns off screenshot multisampling to avoid rendering every frame sixteen times;
native postprocessing still antialiases contours. No centering or fit operation runs between frames.

Original and selected mmCIF files load directly. The hexokinase trajectory uses a native multi-model
PDB export because ChimeraX 1.10.1's multi-frame mmCIF save repeated the active coordinates locally.
Glucose loads as a separate fixed mmCIF structure. Mol*'s `ligand` selection selects free ligands;
`non-standard` selects modified polymer residues and omitted glucose in the first experiment.

Generated `scene.molj` files contain native plugin state and input coordinates. Restore one through
Mol*'s state manager (`plugin.state.setSnapshot`) in a viewer; it is not a custom recipe. The 3N0G
comparison also preserves `surface.molj`. These large editable files remain in `output/`.
`render.json` records camera, counts, dimensions, browser version and elapsed time. Coordinate
samples imported by Mol* are retained for independent comparison with the exported trajectory.

The translucent hexokinase surface exposes glucose but superposes front and back contours. It is
an explicitly disclosed presentation choice. GroEL uses opaque illustrated spacefill with chain
colors, so rotation remains readable despite the near sevenfold symmetry.
