# Feasibility assessment for an open protein-animation toolkit

## Executive assessment

The most durable version of this project is **not a new molecular graphics program**. It is a curated, reproducible collection of tools, recipes, scientific conventions, and example workflows that an LLM can later assemble into an animation pipeline from a request such as:

> “Show hexokinase closing around glucose using a Goodsell-style molecular surface, with glucose highlighted, a white background, and a seamless five-second loop.”

That distinction matters. ChimeraX, Blender, Molecular Nodes, ProteinBlender, Mol*, MDAnalysis, ProDy, OpenMM, FFmpeg, and related packages already solve most of the individual technical problems. The missing layer is a well-documented way to decide **which scientific source to use, what type of motion is justified, how to render it, and how to record provenance**. citeturn819152search1turn317019search3turn272979search0turn697611search0turn193242search0

My recommendation is therefore a **hybrid toolkit with a Python orchestration layer**, using ChimeraX for rapid scientific rendering and Blender plus Molecular Nodes or ProteinBlender for higher-end artistic rendering. Mol* should serve interactive web delivery rather than being the primary film renderer. FFmpeg should be the canonical output encoder. The repository should initially contain tested workflows rather than attempting to implement its own molecular viewer, trajectory engine, or renderer. citeturn819152search2turn166789search8turn697611search2turn166789search0

The timing is unusually favorable. Janet Iwasa's Animation Lab now develops **ProteinBlender**, a GPL-3.0-or-later Blender add-on specifically intended for researchers, educators, and scientific communicators. ProteinBlender builds on Molecular Nodes and MDAnalysis and already provides protein import, molecular styling, poses, puppets, and keyframing. That development substantially changes the landscape compared with even two years ago. citeturn272979search0turn272979search1

## The tool landscape

The following table reflects the current state in November 2026.

| Tool | Best role | Motion | Rendering/style | Automation | License situation | Main weakness |
|---|---|---|---|---|---|---|
| **ChimeraX** | Scientific animation and rapid rendering | Excellent morphing and trajectory playback | Very good AO, silhouettes, surfaces, orthographic views | Excellent commands/Python/headless | Free for academic/nonprofit use, **not OSI-open-source as an application** | Redistribution/commercial restrictions |
| **Blender + Molecular Nodes** | High-quality final animation | Excellent once coordinates exist | Outstanding NPR/cinematic control | Excellent Python/headless | GPL | More complicated scene construction |
| **ProteinBlender** | Researcher-friendly Blender animation | Poses, keyframes, molecular animation | Blender quality | Scriptable through Blender | GPL-3.0-or-later | Young project, rapidly evolving |
| **Illustrate** | Authentic Goodsell-style still frames | None intrinsically | Closest direct Goodsell appearance | Scriptable | Apache-2.0 | Legacy PDB-oriented program, mmCIF limitations |
| **Mol*** | Interactive web visualization | Trajectories, camera animation | Strong WebGL, toon styles | Excellent JS API | MIT | Less control for cinematic offline rendering |
| **PyMOL OSS** | Molecular graphics and scripting | Movies, trajectories | Strong conventional molecular graphics | Good Python API | Open-source core | Proprietary features such as RigiMOL live in commercial builds |
| **VMD** | Large MD trajectory visualization | Excellent | Good scientific rendering | Tcl/Python | Free but restricted, not conventional open source | Licensing and older UI/workflow |
| **NGL** | Lightweight browser viewer | Trajectories | Good WebGL | JavaScript | MIT | Largely superseded technologically by Mol* |
| **3Dmol.js** | Simple browser embed | Basic animation | Good | JavaScript | BSD | Less sophisticated structural workflow |
| **MDAnalysis / MDTraj** | Trajectory preparation | Excellent | None | Excellent Python | LGPL | Analysis, not rendering |
| **ProDy / Bio3D** | Normal modes and conformational analysis | Excellent for ENM/NMA | None | Python / R | MIT / GPL | Motions are models, not experimental trajectories |
| **OpenMM / GROMACS** | Generate MD | Full atomistic dynamics | None | Excellent | MIT/LGPL and LGPL | Computational cost and scientific setup |
| **FFmpeg** | Final output encoding | N/A | Encoding only | Excellent CLI | LGPL or GPL depending build | No molecular knowledge |

ChimeraX is unusually well suited for a first implementation because it already provides structure alignment, conformational morphing, scripting, movie recording, orthographic cameras, lighting modes, ambient shadowing, silhouette edges, transparent backgrounds, and server-side offscreen rendering. Its morph function explicitly generates interpolated intermediate structures and can wrap back to the first conformation for looping. citeturn830584search0turn819152search2turn819152search7turn751615search3

A ChimeraX scripted animation can be as compact as:

```text
open 2yhx
open 3b8a
match #2 to #1
morph #1,2 wrap true frames 75
camera ortho
set bgColor white
light soft
graphics silhouettes true
movie record
coordset #3 1,
wait 150
movie encode hexokinase.mp4 framerate 30
```

The exact model and coordinate-set identifiers would need to be verified in a tested recipe, so the example above should be regarded as design pseudocode rather than a guaranteed runnable workflow. ChimeraX itself documents morphs, wrapped interpolation, movie recording, silhouettes, ambient lighting, and MP4 encoding. citeturn830584search0turn830584search3turn819152search4

The principal drawback is licensing. ChimeraX source is publicly visible, but the overall application is governed by UCSF's non-commercial license. Academic, nonprofit, and government research use is permitted, but redistribution and commercial use are restricted. A toolkit can therefore **call an installed ChimeraX**, but describing the whole toolkit as entirely open source would be inaccurate if ChimeraX were a mandatory dependency. citeturn819152search0

VMD has a similar issue. It is free and source-available and remains excellent for MD trajectories and scripting, but its main license restricts use to academic, research, and internal business purposes unless a commercial license is negotiated. It should be treated as an optional backend, not an open-source foundation. citeturn966841search0turn966841search1

PyMOL occupies an intermediate position. Schrödinger describes PyMOL as a commercial product built on an open-source foundation, with most source under a permissive license. Commercial builds add packaging, support, and proprietary functionality such as RigiMOL. A toolkit should distinguish explicitly between **Open-Source PyMOL** and Incentive PyMOL recipes. citeturn966841search5turn966841search6turn966841search9

For the fully open path, Blender is the strongest rendering foundation. Blender is GPL software, its rendered artwork belongs to the creator without GPL restrictions, it runs headless from the command line, and it offers programmable non-photorealistic rendering through Freestyle and other compositing tools. citeturn166789search7turn166789search8turn317019search8

Molecular Nodes makes Blender far more relevant to structural biology than it was historically. The current release supports PDB and AlphaFold structures, MD trajectories, cryo-EM data, CellPack ensembles, and editable Geometry Nodes-based styles. It can also be used as a Python package, which is important for LLM-controlled pipelines. citeturn317019search1turn317019search2turn317019search3

ProteinBlender may be even closer to your intended audience. It explicitly targets molecular animation for researchers and educators and is being developed by Janet Iwasa's Animation Lab on top of Molecular Nodes. This is probably the project worth watching most closely before inventing a custom Blender layer. citeturn272979search0turn272979search1

One warning is version churn. Molecular Nodes made major architectural changes for Blender 5.2 in 2026, including coordinate scale changes, and ProteinBlender has an active issue discussing compatibility with these newer versions. The toolkit therefore needs environment pinning and tested compatibility matrices. citeturn272979search3

BioBlender should not be adopted. The project is officially discontinued, citing incompatibility with newer Blender versions and explicitly pointing users toward Molecular Nodes instead. citeturn317019search6turn317019search7

Mol* is the strongest browser-side component. It is MIT-licensed, actively developed, handles very large molecular systems and MD trajectories, and is designed to be embedded in third-party applications. It also contains camera-spin and trajectory animation infrastructure. Its main value here would be interactive preview, LMS embedding, structure inspection, and perhaps generation of browser-native teaching objects rather than master video production. citeturn697611search0turn697611search1turn697611search2

## Scientific motion and provenance

The most important design problem is not graphics. It is **what the movement means scientifically**.

A good toolkit should classify every animation segment into a small number of provenance categories:

| Motion class | Meaning | Appropriate teaching label |
|---|---|---|
| Experimental structural states | Two or more experimentally solved conformations | “Structures determined experimentally” |
| Interpolated morph | Geometric path between experimentally determined endpoints | “Interpolated transition” |
| Normal-mode/ENM motion | Predicted low-frequency collective motion | “Predicted mode of motion” |
| Molecular dynamics | Force-field simulation trajectory | “Molecular dynamics simulation” |
| Hypothesis / illustrative movement | Animator-created behavior | “Illustrative model” |

This distinction is essential because a smooth morph is visually convincing but does **not** demonstrate the physical pathway a protein actually follows. ChimeraX itself describes morphing as interpolation between input structures. citeturn830584search0

The PDB should be the preferred source for teaching examples whenever experimentally determined endpoints exist. PDB archive coordinate files are CC0, and the RCSB programmatic APIs expose experimental metadata, ligands, assemblies, and mmCIF-based annotations. citeturn865305search0turn865305search1

AlphaFold DB is useful for missing structures but should not be treated as a dynamics source. AlphaFold DB generally provides one predicted structure for a protein rather than alternative conformational states, and its confidence scores indicate confidence in predicted geometry rather than biological correctness or dynamics. citeturn865305search3turn865305search4

For conformational comparison, DynDom remains useful and currently contains more than 2,000 nonredundant domain-motion analyses. PDBFlex is still online but its own site states that its PDB dataset is based on the January 2017 PDB release, so it should be treated as a legacy reference rather than an authoritative current conformational database. citeturn865305search5turn865305search6

MolMovDB is especially problematic for a durable pipeline. Its maintainers acknowledged in 2020 that the system was already over 15 years old and needed an upgrade. The original `molmovdb.org` endpoint timed out during this research, although registry records still describe the resource. It should therefore be treated as a **historical motion catalogue**, not an operational dependency. citeturn865305search7turn307700view0

KINARI has a similar status. Published evaluations report that its code remains available but the original web visualization capabilities are no longer operational. citeturn865305search8

Normal-mode analysis is a much more durable computational fallback. ProDy is MIT-licensed and specifically designed for protein dynamics analysis, while Bio3D implements elastic-network and normal-mode models. These approaches can generate biologically plausible collective motions cheaply, but they must be labeled as modeled motions rather than observed transitions. citeturn193242search5turn193242search7

For actual MD trajectories, MDAnalysis and MDTraj are excellent Python interoperability layers. MDAnalysis 2.11 can read trajectories from GROMACS, CHARMM, Amber, NAMD, LAMMPS and other packages and can align trajectories reproducibly. MDTraj provides similarly broad format support and fast structural calculations. citeturn193242search0turn193242search2turn193242search3

OpenMM is probably the most approachable MD engine for a Python-oriented teaching toolkit. Its core APIs are MIT-licensed, GPU platforms are LGPL, and it integrates naturally with PDBFixer. GROMACS remains a powerful fully free alternative under LGPL. citeturn193242search8turn193242search9turn193242search10

However, **running MD should not be an MVP requirement**. Generating a scientifically defensible ligand-bound enzyme simulation involves protonation states, missing atoms, force-field choices, ligand parameters, solvent, equilibration, convergence, and trajectory interpretation. That is much more complicated than creating a teaching animation from two known conformations.

Public trajectory repositories are improving quickly. MDRepo currently reports more than one million trajectories, while the Anton Data Portal provides downloadable simulation data with detailed simulation metadata. MDDB and MDposit are emerging as broader European infrastructure, and the original MoDEL site now explicitly redirects users toward MDposit. citeturn841392search0turn841392search1turn841392search6turn841392search7

### Hexokinase is an excellent proof of concept

Hexokinase is unusually well suited because the structural story is classical and clean. RCSB's teaching material identifies **2YHX** as the open yeast hexokinase state. Experimental studies describe glucose-bound yeast hexokinase structures including **1HKG** and the higher-resolution **3B8A**, and comparison of holo and apo structures shows the characteristic domain closure. citeturn822897search0turn822897search1turn822897search2

DynDom explicitly compares 2YHX and 1HKG and reports approximately a 13° domain rotation with strong closure character. citeturn822897search5

One subtle problem illustrates why your repository should store curated knowledge rather than simply accept arbitrary PDB IDs. The historical 1HKG structure was crystallized in the presence of glucose, yet later literature notes that the glucose coordinates are not present in the deposited PDB file. By contrast, 3B8A is explicitly deposited as yeast hexokinase PI in complex with glucose. citeturn822897search1turn822897search2

For teaching, I would therefore prefer:

```text
open state: 2YHX
closed state: 3B8A
motion: aligned structural morph
glucose coordinates: from 3B8A
scientific label: interpolated transition between crystallographic endpoints
```

One complication is that these structures represent different yeast isoenzymes in some historical comparisons. That should be stated in the recipe metadata rather than hidden. citeturn822897search1

### GroEL is a different kind of test

GroEL is ideal for testing large assemblies, camera control, and rendering rather than simple ligand-induced domain closure. Structural literature identifies several experimentally determined states, including 4HEL, 1KP8, and 1AON for closed, ATP-associated, and open conformations in one comparative analysis. citeturn822897search8

GroEL-GroES complexes also exist in experimentally solved bullet and football assemblies. For example, 1AON is a classic bullet complex, while 3WVL is a football-shaped GroEL-GroES2 ATP complex. citeturn822897search9turn822897search10

For an initial “spinning GroEL” animation, however, no conformational modeling is needed at all. That makes it a useful control experiment for rendering quality, assembly handling, surface generation, lighting, camera paths, and output encoding.

## Getting the Goodsell and Iwasa appearance

The reference image you supplied is indeed a **David Goodsell** Molecule of the Month image. The September 2016 RCSB page credits Luigi Di Costanzo and David Goodsell and depicts isoprene synthase from PDB 3N0G. citeturn637531search0

This is worth distinguishing from Janet Iwasa's work. Goodsell created the Molecule of the Month series from 2000 through 2024. Janet Iwasa took over the series beginning in January 2025. citeturn637531search1

Goodsell's style is much easier to approximate automatically than Iwasa's cinematic animation style because Goodsell released the tool used to create the characteristic molecular illustrations. **Illustrate** is Apache-2.0 open-source software specifically designed for non-photorealistic biomolecular illustration. RCSB describes the style as flat pastel colors with black outlines. citeturn637531search3turn637531search5

Illustrate is therefore the first thing I would test for a `goodsell` style preset.

It does have serious limitations. Goodsell's own project page describes Illustrate as legacy code, notes that it does not work with mmCIF files, and warns about very large structures and high chain counts. Goodsell specifically points users toward Mol* toon rendering when Illustrate fails. citeturn637531search4

A durable Goodsell-style pipeline could therefore have two implementations:

```text
goodsell-authentic:
    backend: Illustrate
    use_when: structure can be represented safely as legacy PDB

goodsell-inspired:
    backend: Blender/Molecular Nodes
    use_when: mmCIF, large assembly, animation, or advanced compositing required
```

The Blender version should not try to reproduce watercolor literally at first. The recognizable visual grammar is more important:

- orthographic camera
- white or very pale background
- muted pastel molecular colors
- little or no specular reflection
- shallow, diffuse shading
- darker contact cavities
- clear object silhouettes
- restrained depth cueing
- simplified molecular geometry

Blender's Freestyle engine can generate line-based NPR outlines, including hand-drawn and painted-looking line styles, while Blender's material and compositing systems can provide flat shading, ambient occlusion, paper textures, and subtle color variation. citeturn317019search8

ChimeraX can get surprisingly close to the same visual vocabulary with `light soft`, ambient shadows, silhouette edges, orthographic projection, a white background, and smooth molecular surfaces. This might be sufficient for most undergraduate figures without ever opening Blender. citeturn819152search7turn830584search3turn751615search3

Janet Iwasa's visual language is different. Her historical workflow commonly combined molecular structure tools such as Chimera with professional 3D animation software such as Maya and compositing software such as After Effects. Her work treats animations as “visual hypotheses,” which is an important conceptual model for your toolkit. citeturn713681search5turn713681search7

The open-source analogue today is essentially:

```text
ChimeraX / Molecular Nodes / ProteinBlender
                ↓
             Blender
                ↓
        Blender compositor
                ↓
             FFmpeg
```

This is especially compelling because the Iwasa lab itself is now building ProteinBlender rather than trying to maintain a standalone animation application. A recent profile of the lab explicitly notes that their earlier Molecular Flipbook standalone application became difficult to maintain because operating-system compatibility required essentially full-time software engineering. The lab's present strategy is to build tools within existing animation software. citeturn713681search10turn272979search0

That history strongly supports your idea of assembling durable existing tools rather than writing a new renderer.

## Recommended repository and LLM architecture

The repository should be thought of as a **cookbook plus machine-readable scientific production system**.

I would separate it into four layers:

```text
protein-animation-toolkit/
│
├── tools/
│   ├── chimerax/
│   ├── blender/
│   ├── molecular-nodes/
│   ├── proteinblender/
│   ├── illustrate/
│   ├── molstar/
│   ├── mdanalysis/
│   ├── prody/
│   └── ffmpeg/
│
├── workflows/
│   ├── structure-spin/
│   ├── two-state-morph/
│   ├── normal-mode-motion/
│   ├── md-trajectory/
│   ├── ligand-binding/
│   └── interactive-web/
│
├── examples/
│   ├── hexokinase-closure/
│   ├── groel-spin/
│   └── ...
│
└── styles/
    ├── goodsell.yaml
    ├── goodsell-inspired.yaml
    ├── iwasa-inspired.yaml
    ├── textbook-flat.yaml
    └── publication-neutral.yaml
```

Each tool directory should contain installation information, license status, supported platforms, known bugs, tested version, example commands, and explicit statements of what it does **not** do.

Each workflow should be renderer-agnostic where possible. For example:

```yaml
workflow: two-state-morph

scientific_model:
  type: interpolated_structure_transition
  endpoints:
    start:
      source: rcsb
      pdb_id: 2YHX
    end:
      source: rcsb
      pdb_id: 3B8A

alignment:
  selection: protein_backbone

ligand:
  source_structure: 3B8A
  residue_name: GLC
  emphasize: true

motion:
  interpolation: structural_morph
  direction: forward_reverse
  duration_seconds: 5
  seamless_loop: true

style:
  preset: goodsell-inspired
  background: white
  projection: orthographic

output:
  width: 1280
  height: 720
  fps: 30
  formats:
    - mp4
    - webm
    - webp
    - gif

provenance:
  disclosure: >
    End states are experimentally determined structures.
    Intermediate frames are interpolated and do not represent
    an experimentally measured trajectory.
```

The key design principle is that this YAML describes **intent and scientific meaning**, not Blender node trees or ChimeraX command syntax.

A backend adapter turns the recipe into actual commands.

For example:

```bash
proteinanim render hexokinase.yaml --backend chimerax
```

or:

```bash
proteinanim render hexokinase.yaml --backend blender
```

The eventual LLM does not need to understand Blender deeply. It needs to convert a request into a valid recipe and choose among documented workflows.

Your proposed prompt could therefore be translated approximately as follows:

```yaml
request: >
  Show hexokinase closing around glucose using a Goodsell-style
  molecular surface, with glucose highlighted, a white background,
  and a seamless five-second loop.

workflow: two-state-morph
subject: yeast hexokinase

evidence_preference:
  experimental_structures: required
  simulated_motion: avoid_if_unnecessary

style:
  preset: goodsell-inspired
  representation: molecular_surface
  ligand_emphasis: high
  background: white

animation:
  duration_seconds: 5
  loop: seamless
```

The LLM's actual work would then be:

```text
natural language
      ↓
identify biological target
      ↓
retrieve or choose curated structural states
      ↓
select appropriate workflow
      ↓
validate scientific provenance
      ↓
generate recipe
      ↓
execute tested backend
      ↓
encode outputs
      ↓
emit provenance report
```

This is far safer and easier to maintain than allowing an LLM to invent arbitrary ChimeraX or Blender scripts from scratch.

A GroEL recipe can be substantially simpler:

```yaml
workflow: structure-spin

structure:
  source: rcsb
  pdb_id: 1AON
  assembly: biological

camera:
  projection: orthographic
  motion:
    type: turntable
    axis: y
    degrees: 360

animation:
  duration_seconds: 5
  loop: seamless

style:
  preset: goodsell-inspired
  background: white

output:
  formats: [mp4, webm, webp, gif]
```

For browser teaching objects, the same recipe could target Mol*. Mol* is MIT licensed, embeddable, and already supports structures, large assemblies, trajectories, and saved visualization states. citeturn697611search0turn697611search3

For final assets, FFmpeg should handle conversion from rendered frames or a master video. FFmpeg supports animated GIF and WebP and conventional video formats, and its command-line interface is well suited to deterministic pipelines. citeturn166789search1turn166789search2

GIF should be treated as a compatibility target, not the master format. GIF supports only a 256-color palette, while WebP, MP4, and WebM preserve better image quality and usually achieve much smaller files for molecular surfaces and smooth shading. ImageMagick also supports animated GIF and WebP workflows if additional image manipulation is needed. citeturn166789search6turn166789search10

## Decision matrix and recommended implementation

| Criterion | ChimeraX | Blender + Molecular Nodes | ProteinBlender | Mol* |
|---|---:|---:|---:|---:|
| Scientific structure handling | Excellent | Very good | Very good | Excellent |
| Two-state morph | Excellent | Requires preparation/keyframing | Good conceptual fit | Possible but less convenient |
| MD trajectories | Excellent | Excellent via Molecular Nodes | Based on Molecular Nodes/MDAnalysis | Excellent |
| Goodsell-like look | Good | Excellent potential | Excellent potential | Good toon approximation |
| Iwasa-like animation | Moderate | Excellent | Excellent | Limited |
| Headless automation | Excellent | Excellent | Likely through Blender scripting | Browser/server dependent |
| Python friendliness | Excellent | Excellent | Blender/Python ecosystem | JS-first |
| Web embed | No | No | No | Excellent |
| Fully open-source stack | No | Yes | Yes | Yes |
| Ease for a scientist | Excellent | Moderate | Promising | Excellent |
| Long-term renderer flexibility | Moderate | Excellent | Excellent if project remains active | Excellent for web |
| Recommended role | Fast scientific backend | Premium renderer | User-facing Blender workflow | Web viewer |

The most sensible architecture is therefore:

**Primary orchestration:** Python.

**Fast/default renderer:** ChimeraX for academic teaching workflows.

**Fully open renderer:** Blender plus Molecular Nodes.

**Artist-friendly Blender layer:** ProteinBlender, evaluated carefully as it matures.

**Goodsell reference renderer:** Illustrate for compatible still-image cases.

**Interactive renderer:** Mol*.

**Scientific motion preparation:** MDAnalysis and ProDy.

**Simulation:** OpenMM only when necessary.

**Video/image encoding:** FFmpeg, with Pillow or ImageMagick for special image tasks.

This approach also avoids creating a false binary choice between “ChimeraX or Blender.” They solve different stages of the problem.

A useful workflow might actually be:

```text
PDB structures
     ↓
ChimeraX
alignment / chain selection / morph
     ↓
trajectory or coordinate frames
     ↓
Blender + Molecular Nodes / ProteinBlender
     ↓
materials / lighting / outlines / camera
     ↓
FFmpeg
     ↓
MP4 + WebM + animated WebP + GIF
```

MDAnalysis can serve as the interchange layer whenever trajectories need alignment, frame reduction, atom selection, or format conversion. citeturn193242search0turn193242search2

### What should not be attempted initially

Do not write a molecular renderer.

Do not create a new WebGL viewer.

Do not build your own MD engine.

Do not make general-purpose natural-language generation the first milestone.

Do not attempt automatic molecular dynamics from arbitrary PDB structures.

Do not promise that morphing represents physical transition pathways.

Do not try to reproduce watercolor brush texture before solving geometry, lighting, composition, and scientific provenance.

Do not make MolMovDB, PDBFlex, KINARI, BioBlender, or other aging web services hard dependencies. MolMovDB has acknowledged maintenance problems, PDBFlex's data are explicitly based on a 2017 release, KINARI's web visualization has ceased functioning, and BioBlender is formally discontinued. citeturn865305search7turn865305search6turn865305search8turn317019search6

## Proof of concept and development path

The first milestone should consist of exactly **two animations**.

The first should be hexokinase closure. Use 2YHX and 3B8A, align the structures, preserve glucose from the bound structure, generate a forward-reverse structural morph, render a white-background molecular surface with outlines, and produce MP4, WebM, animated WebP, and GIF. The final asset should contain metadata stating that the endpoints are experimental and the intermediate path is interpolated. citeturn822897search0turn822897search2

The second should be a GroEL turntable. Use a clearly documented biological assembly from an RCSB structure, render one full 360° orthographic rotation, and test both ChimeraX and Blender backends. That test isolates rendering and scene automation from conformational modeling.

Those two examples exercise nearly the entire architecture:

```text
                    Hexokinase        GroEL
PDB retrieval           yes             yes
ligand selection         yes             no
alignment                yes             no
morph                    yes             no
large assembly           no              yes
camera animation         modest          yes
style preset             yes             yes
seamless loop            yes             yes
encoding                  yes             yes
provenance                yes             yes
```

A solo professor comfortable with Python could reasonably build the initial repository without writing much original rendering code. The main work is documentation, testing, normalization of recipes, and determining how each tool behaves across versions. A limited prototype with two workflows is likely a **several-week side project**, while a polished cross-platform package with automatic dependency handling, renderer adapters, documentation, tests, and an LLM front end is more plausibly a **multi-month project**. That estimate is an engineering judgment rather than a figure reported by the cited projects.

The largest maintenance burden will not be the Python orchestration code. It will be Blender, Molecular Nodes, ProteinBlender, and ChimeraX version changes. Molecular Nodes' substantial 2026 changes illustrate why each recipe needs a tested version lock. citeturn272979search3

Containerization can help with FFmpeg, MDAnalysis, ProDy, OpenMM, and other conventional command-line components. Blender can also run headless. ChimeraX supports `--offscreen`, including rendering without a graphical display through EGL or Mesa, although its licensing means distribution within a public container requires careful review rather than assumption. citeturn819152search2turn166789search8

Every completed animation should ideally ship with a small provenance file:

```yaml
animation: hexokinase_closure.mp4

structures:
  - pdb: 2YHX
    role: open endpoint
    evidence: x-ray structure
  - pdb: 3B8A
    role: glucose-bound endpoint
    evidence: x-ray structure

motion:
  type: geometric interpolation
  physically_simulated: false

render:
  backend: Blender
  molecular_nodes: "pinned-version"
  blender: "pinned-version"

style:
  preset: goodsell-inspired
  note: >
    Visual styling is inspired by non-photorealistic
    molecular illustration and is not an experimental observable.
```

This feature may ultimately be more important educationally than any particular renderer.

The broader idea is technically feasible now because nearly every required capability already exists. The genuinely valuable contribution would be the **curated scientific workflow layer** connecting those capabilities. The recent appearance of ProteinBlender from Iwasa's own group strengthens that conclusion. Iwasa's lab has effectively reached the same architectural insight: maintaining an entire standalone animation program is expensive, while building molecular tools inside a mature 3D ecosystem is much more sustainable. citeturn713681search10turn272979search0

The highest-value initial repository would therefore not say “this is the protein animation program.” It would say:

```text
Here are the reliable ways to make protein animations.
Here is when each method is scientifically justified.
Here are tested examples.
Here are the exact versions and licenses.
Here is how to reproduce each result.
Here is what is experimental, simulated, interpolated, or illustrative.
```

Once that corpus exists, the LLM layer becomes comparatively straightforward. The LLM's job is then not molecular graphics. It is **workflow selection and recipe construction**. That is a much more durable and tractable problem.