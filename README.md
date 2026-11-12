# protein-structure-animator

Reproducible native-tool workflows for protein illustrations and teaching animations, with structural choices, editable sources, and playback evidence documented.

**A documented tool collection, not a general-purpose animation app.** Three examples have completed reproduction and review within stated limits: a 3N0G appearance comparison, an interpolated hexokinase closure, and a complete GroEL assembly rotation. The examples preserve structural inputs and distinguish measured structures, constructed motion, and viewpoint changes.

## Screenshots

The hexokinase source animation illustrates closure and reopening around a fixed, experimentally positioned glucose pose. Its 125 distinct source frames at 25 fps make a five-second loop; the motion is endpoint interpolation, not a physical binding path or kinetics model. The GroEL view shows the complete fourteen-chain assembly rotating by viewpoint alone. The README animated WebP is a one-play, reduced-rate preview of the hexokinase animation.

<!-- screenshots:begin (managed by screenshot-docs) -->
![Hexokinase closes and reopens around fixed magenta glucose in an interpolated preview](docs/screenshots/hexokinase_closure_demo.webp)
![Static hexokinase open and closed endpoints beside the complete fourteen-subunit GroEL](docs/screenshots/protein_examples.webp)
<!-- screenshots:end -->

Browser playback of GIF, MP4, and WebP was verified for both animations. In the tested LibreOffice Impress version, GIF and MP4 played, while animated WebP inserted as an ODP image was blank. Prefer MP4 for paced presentations; exact Impress frame timing was not measured.

## What you can make

- Compare illustrated atom spheres with a smooth molecular surface using the 3N0G example.
- Show an explicitly staged interpolation between matched experimental hexokinase structures.
- Rotate the complete GroEL biological assembly without changing its coordinates.
- Render five-second, 640 x 640 media as MP4, GIF, and animated WebP, with posters and editable Mol* state.
- Reproduce the preparation, rendering, encoding, and verification steps from documented inputs.

## Quick start: render the GroEL assembly

This first success uses Mol* in Chromium, Playwright, FFmpeg, and the repository's Python environment with Pillow. It does not need ChimeraX, Illustrate, or Blender. Install Node.js, FFmpeg, and Python 3 first, then from the repository root install the current project dependencies and retrieve the fixed public inputs:

```bash
source source_me.sh && python3 -m pip install --upgrade -r pip_requirements.txt
npm install
./devel/setup_playwright.sh
bash examples/download_inputs.sh
```

Render and encode the animation:

```bash
node examples/render_molstar.mjs groel_rotation
source source_me.sh && python3 tools/encode_loop.py output/groel_rotation/frames
```

The output directory contains `animation.mp4`, `animation.gif`, `animation.webp`, `poster.webp`, 125 PNG frames, and editable `scene.molj` settings. The verified render is 640 x 640 pixels and five seconds at 25 fps. Downloaded input hashes are checked by the download script. Dependencies use open-ended minimum versions; the versions in example records describe observations, not pins.

## Choose an example

- [GroEL rotation](examples/groel_rotation/README.md): render the complete biological assembly and inspect its structural selections and rotation.
- [Hexokinase closure](examples/hexokinase_closure/README.md): prepare matched experimental structures with ChimeraX, then render the explicitly interpolated teaching illustration.
- [3N0G appearance comparison](examples/appearance_3n0g/README.md): compare Illustrate atom spheres, Mol* spheres, and a smooth Mol* surface.

For example, a request that fits the current collection is: "Show the complete GroEL assembly rotating once, with the chain colors and white background used in the documented example, and save an editable Mol* scene plus MP4 and GIF." The GroEL example changes the camera viewpoint only; it does not depict a conformational cycle.

## Guides and evidence

- [Tool selection and installation](docs/TOOLS.md): choose a demonstrated native capability and install only the tools it needs.
- [Scientific and delivery checks](docs/ANIMATION_GUIDANCE.md): keep structural fidelity, interpretation, visual review, playback, and fresh-process reproduction distinct.
- [Mol* rendering](docs/tools/MOLSTAR.md): rendering invocation, scene files, and settings.
- [ChimeraX preparation](docs/tools/CHIMERAX.md): structural alignment and the checked trajectory handoff.
- [Media encoding](docs/tools/MEDIA.md): loop encoding and format-specific behavior.
- [Verification report](docs/active_plans/reports/toolbox_verification.md): acceptance evidence, review results, and remaining limits.

## Requirements and limits

The GroEL quick start needs Python 3 with the declared Python dependencies, Node.js with npm dependencies, Playwright's Chromium browser, and FFmpeg. The appearance and hexokinase examples need their separately documented tools. ChimeraX is distributed under separate terms that distinguish noncommercial and commercial use; check its current license for your use. No external application is bundled. Tested versions and specific software behavior are recorded in the examples and reports.

The hexokinase illustration places closed-state glucose in the open-state structure, where a short contact is documented; its intermediate conformations are geometric constructs. GroEL shows the deposited construct and a viewpoint rotation, not folding dynamics. Animated WebP's tested Impress embedding path did not display. Read each example's structure and limitation notes before reusing its media scientifically.

## Licenses

Project source code is [LGPL-3.0](LICENSE.LGPL-3.0). Documentation, example materials, and generated previews are [CC-BY-4.0](LICENSE.CC-BY-4.0). Mol* is MIT licensed; other native tools and structural data retain their own terms, as noted in the guides.

## Project notes

- [Human guidance](docs/HUMAN_GUIDANCE.md): teaching and practical priorities.
- [Design decisions](docs/DESIGN_DECISIONS.md): settled direction for this collection.
- [Changelog](docs/CHANGELOG.md): repository changes and verification notes.
