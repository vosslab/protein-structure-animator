# Protein animation toolbox plan

## Goal and direction

Build a collection of documented capabilities and reproducible examples that an LLM can combine
to create molecular illustrations and animations for teaching biochemistry. The agent chooses the
tools and approach for each request. Successful workflows are references, not mandatory procedures.

Target request:

> Show hexokinase closing around glucose using a Goodsell-style molecular surface, with glucose
> highlighted, a white background, and a seamless five-second loop.

Deliver the animation, editable sources, structural references, and a short explanation of the
method. Distinguish experimental endpoints, simulated trajectories, interpolated motion, and authored
staging. Resolve routine technical failures autonomously; report scientific ambiguity that the
available evidence cannot resolve.

The initial audience is an instructor creating visual teaching materials. Assume local macOS use
and document Linux portability where actually verified. Blender is optional: the user reports that
it can become unstable enough to require a reboot on their Mac. Do not make it a prerequisite or
launch Blender for initial experiments on this machine.

## Current evidence

Research date: 2026-11-11. This record summarizes documentation and selected source inspection,
not completed rendering experiments. ChimeraX 1.10.1 and FFmpeg were found locally; FFmpeg lists
GIF, animated WebP, and H.264 encoders. No animation has been generated or visually validated here.

### Rendering candidates

| Tool | Useful capabilities | Limits and proposed role |
| --- | --- | --- |
| Illustrate | Goodsell's own open-source renderer; scripted input and image output | First authentic-style candidate; legacy PDB, atom-count, chain-count, and mmCIF limitations need testing |
| Mol* | Illustrated spacefill, outlines, occlusion, saved scenes, spin/rock export | First browser-based appearance and rotation candidate; unattended invocation needs verification |
| ChimeraX | Alignment, morphs, trajectories, commands/Python, images and movies | First structure-preparation and morph candidate; also compare its rendering; noncommercial licensing and platform limits apply |
| FFmpeg | Encode frame sequences into GIF, WebP, and video | Shared delivery tool; check actual playback and timing |
| Blender + Molecular Nodes | Python, editable scenes, molecular imports, artistic rendering | Optional alternative; user-reported Mac instability and version coupling make it unsuitable as the default |
| ProteinBlender | Iwasa lab's domain/chain puppets, poses, keyframes | Optional Blender-based authoring tool; investigate when a scene benefits from staging |
| Molecular Animation | AmadeusBio's scripts, constrained morphs, Blender rendering examples | Optional reference or component source; its complete production workflow is not the repo architecture |

The Goodsell look does not require Blender. The supplied isoprene synthase image uses overlapping
atom spheres, dark outlines, restrained colors, soft depth shading, and a white background. Compare
illustrated spacefill separately from a smooth molecular surface; they communicate different detail.
Use the reference to judge appearance rather than assuming a generic surface is equivalent.

Illustrate's Apache-licensed Fortran could be ported to Rust if experiments establish a concrete
reason. First preserve reference renders and inputs. A port should retain visual fidelity and useful
scripted controls; modern format support is a separate, explicit change. Do not start a port merely
to use the toolbox, and do not assume the work is trivial before inspecting the implementation.

### Motion sources

| Source | Appropriate use | Scientific boundary |
| --- | --- | --- |
| One structure plus camera rotation | GroEL shape and assembly | Shows a changing viewpoint, not molecular dynamics |
| Two or more experimental states | Hexokinase closure | Intermediates are illustrative; endpoints do not establish pathway or kinetics |
| Normal modes / elastic networks | Collective flexibility | Predicted flexibility does not establish substrate-induced motion |
| Published MD trajectory | Dynamics with documented simulation conditions | Verify topology, atom order, provenance, conditions, and sampling |
| New MD simulation | A future need specifically requiring simulation | Preparation and sampling are substantial; ordinary fixed-bond MD does not provide enzyme reaction chemistry |
| Authored motion | Binding, explanatory staging, chemical illustrations | Identify which geometry and timing are illustrative |

MDAnalysis and related libraries can prepare and analyze trajectories; do not describe them as a
general replacement for conformational morphing algorithms. Start with existing simulations rather
than new MD. Chemical reaction animation is a later capability requiring mechanistic sources.

### Findings that affect selection

- ChimeraX documents saving morphs as coordinates separately from rendering. Verify one exported
  example in a second renderer rather than inventing a universal motion format.
- ChimeraX's windowless rendering is documented for Linux. Do not assume the same behavior on macOS.
- Molecular Nodes currently pairs Blender 5.2 with Python 3.13 and calls its Python API experimental.
  Its runtime should remain separate from the repo's configured Python environment.
- AmadeusBio's Molecular Animation has an Apache-licensed v0.3.0 release. Its authors report rendering
  tests on Windows/NVIDIA; macOS and Linux rendering remain unverified. Its CI runs without Blender.
- That project's matching helper requires caller-supplied atom identities and keeps unmatched atoms
  at reference coordinates. Its contact calculation also needs a memory check for large assemblies.
  Constrained interpolation is not evidence of a physically established pathway.
- MolMovDB's HTTP homepage and catalog responded, but its catalog's representative hexokinase morph
  returned "not found." Test individual downloads; preserve useful coordinates and provenance locally.
- Mol* v6's Prism assistant is work in progress. Existing MCP projects are candidates to evaluate,
  not prerequisites. Start with an existing coding agent and native tool interfaces.

## Approach and examples

### Document useful capabilities

Create a concise tool index and focused guides as evidence accumulates. For each tested capability,
record purpose, installation, native commands or Python interfaces, input/output formats, limitations,
licensing, working environment, and failure diagnosis. Distinguish documented support from local
verification. Document prerequisites per tool rather than requiring every package for every task.

Use native interfaces first. Add a small helper only when an example exposes a real gap. Keep any
helper's scope clear, with useful errors and a focused check for nontrivial new logic. Use
`source source_me.sh && python3` for repo Python work. Keep algorithm implementations in established
tools unless a measured need justifies replacing one.

Avoid a custom viewer, agent framework, common renderer API, workflow engine, or scene language in
the initial work. PNG sequences are a useful exchange format for encoding and inspecting frames,
but need not be mandatory intermediates for every tool.

### Establish the appearance

Use isoprene synthase 3N0G to match the supplied reference. Start with Illustrate and Mol*; compare
ChimeraX where useful. Keep camera, colors, displayed atoms, image size, and background comparable.
Save a spacefill example and an outlined smooth-surface example. Assess actual images at teaching
size, including contour clarity, depth, ligand visibility, and visual clutter.

Check Illustrate's batch invocation, fixed framing, color consistency, output dimensions, and
rendering cost before deciding whether any Rust port or format-conversion helper is warranted.
If legacy constraints prevent a requested example, record the concrete failure and try an existing
alternative; do not redesign the collection around hypothetical limits.

### First animation: hexokinase

Use 3O80 (open) and 3O8M (glucose-bound closed), both Kluyveromyces lactis hexokinase, as starting
candidates. Inspect correspondence and structural context before adopting them as a working pair.
The historical 2YHX/1HKG pair is not the default: PDB-101 warns that those structures are incomplete.

- Match protein atoms, resolve alternate conformers, and inspect missing regions and alignment.
- Record omitted components: 3O80 contains an ATP analog; 3O8M contains glucose alternatives.
- Treat glucose deliberately. A ligand present in only one endpoint can disappear from a morph.
  Retaining or moving it for illustration needs an explicit explanation.
- Choose a view that exposes the cleft. Check whether closure hides glucose; document a cutaway or
  transparency if needed rather than implying that occluded glucose is absent.
- Make the requested five-second loop close and reopen with smooth reversals. A sensible example
  setting is 25 frames/second, producing 125 frames at 40 ms each. Avoid an abrupt endpoint reset.
- Describe this as an illustrative conformational loop, not a complete catalytic cycle or measured
  binding trajectory. Preserve the motion independently of the final encoded file where practical.

Select the renderer from the appearance experiments. If a candidate fails to render consistently,
use another tested tool and document the result. The example should demonstrate a successful method,
not force one renderer on all future requests.

### Demonstrate reuse

Produce a GroEL rotation using 1OEL biological assembly 1, the complete 14-subunit assembly. Verify
assembly selection rather than assuming that the asymmetric unit is complete. Distinguish the camera
rotation from a later GroEL conformational-cycle animation. Use this second request to check whether
the documentation and agent guidance generalize beyond the hexokinase example.

A later trajectory example can use a published dataset with matching topology, documented conditions,
and clear provenance. Select and inspect that dataset when trajectory support becomes active work.
Keep enhanced or biased sampling distinguishable from unbiased dynamics.

## Files and acceptance

Expected implementation artifacts, created only as needed:

- `docs/TOOLS.md` and focused guides under `docs/tools/`: capabilities and native invocation examples.
- `examples/`: self-contained examples with inputs or retrieval instructions, scripts, settings,
  editable sources, outputs, citations, and a record of actual verification.
- Concise agent guidance pointing to those resources and explaining scientific and visual expectations.
- Small gap-filling helpers, plus relevant checks and changelog entries, only where demonstrated useful.

First milestone: given the documented tools and a natural-language request, an agent produces the
hexokinase animation, inspects it, and delivers reproducible sources and an accurate method summary.
Then use the GroEL request to check reuse. Successful examples should demonstrate:

- Reproduction from the documented starting point without undocumented interactive adjustments.
- Correct protein identity, assembly, endpoint correspondence, ligand treatment, and provenance.
- Visual inspection of stills, intermediate frames, moving surfaces, and the loop boundary.
- Correct duration, frame timing, dimensions, and readable colors at teaching size.
- WebP, GIF, and MP4 deliveries where useful, plus a static poster and editable sources.
- Playback in the target browser and LibreOffice Impress slideshow, checked separately from encoding.

Automatic measurements help detect clipping, missing frames, or abrupt changes. They do not establish
biological correctness or replace visual review. Do not claim local tests, documented capabilities,
successful encoding, or earlier examples as evidence of an unattended end-to-end result.

## Source references

- [Goodsell's Illustrate](https://ccsb.scripps.edu/illustrate/) and
  [source code](https://github.com/ccsb-scripps/Illustrate).
- [Mol* illustrative style](https://molstar.org/viewer-docs/tips/illustrative-style/) and
  [movie export](https://molstar.org/viewer-docs/tips/movie-export/).
- [ChimeraX morph tutorial](https://rbvi.github.io/chimera-tutorials/presentations/modules/chimerax-comp-structures/index.html),
  [startup options](https://github.com/RBVI/ChimeraX/blob/develop/docs/user/options.html), and
  [license](https://github.com/RBVI/ChimeraX/blob/develop/License.md).
- [Isoprene synthase reference](https://pdb101.rcsb.org/motm/201),
  [hexokinase historical discussion](https://pdb101.rcsb.org/motm/50),
  [3O80](https://www.rcsb.org/structure/3O80), [3O8M](https://www.rcsb.org/structure/3O8M), and
  [1OEL](https://www.rcsb.org/structure/1OEL).
- [Molecular Nodes API](https://bradyajohnston.github.io/MolecularNodes/api/) and
  [ProteinBlender](https://animation-lab.github.io/ProteinBlender/).
- [Molecular Animation](https://github.com/AmadeusBio-ai/Molecular_Animation),
  [setup](https://github.com/AmadeusBio-ai/Molecular_Animation/blob/main/docs/setup.md),
  [matching](https://github.com/AmadeusBio-ai/Molecular_Animation/blob/main/molanim/structure.py), and
  [morph implementation](https://github.com/AmadeusBio-ai/Molecular_Animation/blob/main/molanim/morph.py).
- [MolMovDB](http://www.molmovdb.org/), [MDverse](https://mdverse.eu/), and
  [MDDB API](https://mmb.mddbr.eu/api/rest/docs/).
- [Mol* v6 status](https://molstar.org/docs/v6/) and
  [Prism assistant](https://molstar.org/docs/v6/prism-viewer/assistant/).

Tool versions and online documentation will change. Recheck the selected installation instructions
and capabilities when executing each experiment. The supplied external LLM research is background
material; its recommendations do not override the human's toolbox direction or establish validation.
