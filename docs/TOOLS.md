# Molecular animation tools

Use the smallest demonstrated capability that fits the request. The examples use native tool
interfaces; there is no common scene language or renderer API.

| Capability | Guide | Local evidence |
| --- | --- | --- |
| Canonical Goodsell figures and animations | [OXILLUSTRATE.md](tools/OXILLUSTRATE.md) | 3N0G still and GroEL integration |
| Historical Fortran reference | [ILLUSTRATE.md](tools/ILLUSTRATE.md) | Earlier scripted 3N0G still |
| Smooth surfaces, interactive views and retained illustrated spheres | [MOLSTAR.md](tools/MOLSTAR.md) | 3N0G comparison and animation examples |
| Align structures and interpolate conformations | [CHIMERAX.md](tools/CHIMERAX.md) | Matched hexokinase endpoints and trajectory |
| Encode teaching media | [MEDIA.md](tools/MEDIA.md) | Five-second MP4, WebP and GIF from 125 frames |

Start with [examples/appearance_3n0g/README.md](../examples/appearance_3n0g/README.md),
[examples/hexokinase_closure/README.md](../examples/hexokinase_closure/README.md), or
[examples/groel_rotation/README.md](../examples/groel_rotation/README.md).
See [ANIMATION_GUIDANCE.md](ANIMATION_GUIDANCE.md) for scientific and delivery checks.

## Install only what you use

For canonical Goodsell rendering, build the current sibling Rust checkout as described in
[OXILLUSTRATE.md](tools/OXILLUSTRATE.md); Node.js, Chromium and Fortran are not needed for that
route. FFmpeg and repository Python encode its frames. Install browser dependencies only for Mol*.

Run commands from the repository root. On this Mac, Python runs through:

```bash
source source_me.sh && python3 -m pip install --upgrade -r pip_requirements.txt
npm install
./devel/setup_playwright.sh
bash examples/download_inputs.sh
```

Dependencies use current releases and open-ended `>=` minimums. The npm lockfile records the
resolved installation; refresh it forward with `npm update`. Tested versions belong in example
records, not exact dependency requirements. ChimeraX and the external rendering tools are separate installations.
Original RCSB mmCIF files, large trajectories, native sessions, frames and delivery files live in
ignored `output/`. Small selected reference previews live beside the example sources.
