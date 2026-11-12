# An agent-operated protein animation toolbox

## Intent and boundaries

Enable an agent to turn a natural-language teaching request into a scientifically defensible
protein animation, with editable sources, structural references, documented native tools and
successful reusable examples. The agent chooses how to combine capabilities.

Apply **Keep it simple (KISS)** and **Use the scientific method** from
[REPO_STYLE.md](../REPO_STYLE.md). Use native molecular algorithms and interfaces. Small
experiments select routes for each example, without establishing a mandatory workflow.

The [research report](../active_plans/protein-deep-research-report.md) remains background material. Adopt
traceable primary-source findings, short provenance records, editable native settings and actual
coordinate handoff checks. Preserve human guidance separately from external LLM recommendations.
Use current releases and open-ended dependency minimums; tested versions record observations.

Scope: Illustrate, Mol*, ChimeraX and FFmpeg; a 3N0G appearance comparison, hexokinase closure,
GroEL rotation, tool guides and agent guidance. Deliver media, poster, native settings and commands.

Defer a new viewer, application, orchestration framework, adapters, YAML recipes, MCP server,
new MD simulation, reaction chemistry and an Illustrate Rust port. Blender stays optional and is
excluded from initial Mac experiments because of reported instability. Do not install every
research candidate or treat illustrative commands in the report as tested interfaces.

## Responsibilities and files

| Component | Responsibility |
| --- | --- |
| Tool guides | Native capabilities, installation, invocation, formats, licensing and measured limits |
| Examples | Scientific selections, motion interpretation, scripts/settings and reproduction |
| Agent guidance | Discovery, tool choice, scientific expectations, inspection and delivery |

Use [TOOLS.md](../TOOLS.md), focused guides beneath docs/tools/, descriptive snake_case
directories in examples/, and ignored output/<example_name>/ for coordinates, frames, logs,
sessions and delivery media. Retain small previews intentionally. Domain helpers belong in tools/;
maintainer diagnostics belong in devel/. No speculative application package is introduced.

## Milestones

| Milestone | Deliverable | Acceptance boundary |
| --- | --- | --- |
| M1 | 3N0G appearance comparison | Useful Blender-free appearance and documented automation |
| M2 | Hexokinase closure | Inspected scientific handoff, five-second loop and all deliveries |
| M3 | GroEL rotation | Correct fourteen-subunit assembly and demonstrated capability reuse |
| M4 | Reproduction and documentation | Fresh-process replay, browser and Impress playback evidence |

### M1: Establish rendering evidence

Compare Illustrate and Mol* illustrated atom spheres against the supplied isoprene synthase
reference. Test an outlined smooth surface separately; evaluate ChimeraX preparation and relevant
Mac rendering limits. Preserve comparable orientation, components, color, dimensions and background.
Inspect silhouettes, cavities, ligand visibility, clutter and readability at teaching size.

Check repeated scripted renders, fixed framing and consistency across a short rotation.
Automatic fitting must not cause drift or changes in apparent size. Preserve native inputs,
reference previews, versions and graphical-session requirements.

Prefer the route that meets the representation and appearance with fewer manual steps. Illustrate
is an authentic spacefill candidate; a surface request needs a demonstrated surface renderer.
Diagnose failed capabilities and try existing alternatives. Never silently discard molecular data
to satisfy a legacy parser. Structure preparation and documentation may proceed independently;
serialize graphics experiments on this Mac.

### M2: Deliver hexokinase closure

Depends on M1's demonstrated route. Start with 3O80 and 3O8M, both Kluyveromyces lactis hexokinase,
UniProt P33284. Inspect sequence correspondence, chain identity, missing atoms/residues, alternate
conformers and ligand context before acceptance. The report's 2YHX/3B8A pair maps to different
isoenzymes and is not adopted automatically.

Use native ChimeraX alignment and morphing first. Choose and document the stable alignment region
so whole-molecule drift is removed without suppressing relative lobe closure.

- Keep corresponding resolved protein atoms, record omissions and invent no missing loops.
- Inspect glucose identity, position, alternatives and occupancy before choosing a pose.
- Record omitted ATP analog, solvent and ions. Keep ligand handling separate from the protein morph.
- Use a fixed bound glucose pose registered to the chosen stable region. Invent no binding path.
- Inspect glucose throughout closure; disclose a cutaway or transparency if needed.
- Preserve native coordinates and test them in the selected renderer. Compare identities, frame
  count, endpoint geometry and ligand registration after import.
- Use PDB only when needed and only when identities and coordinates remain representable.
- Deliver a five-second close-and-reopen loop: 25 fps, 125 samples, 40 ms each, eased reversals,
  no abrupt reset and no extra duplicated endpoint.

Label the result an interpolated conformational illustration. Reopening and timing are explanatory
choices, not measured kinetics or a catalytic cycle. Deliver inspected WebP, GIF, MP4, poster,
editable sources and reproduction instructions without undocumented human adjustments.

Correct correspondence, invocation or presentation failures using evidence. If the endpoints or
morph remain unsuitable, investigate another documented same-protein pair and record the failed
candidate. Scientific preparation and encoding research can proceed independently; final rendering
depends on accepted coordinates and style.

### M3: Demonstrate GroEL reuse

Depends on M1 and capabilities documented during M2. Use 1OEL biological assembly 1: verify fourteen
subunits rather than assuming the seven-chain asymmetric unit is complete. 1AON includes GroES and
ADP and remains a separately named future complex example.

Render one full turn with fixed projection, target, scale and framing. Keep changing viewpoint
distinct from conformational motion. Check stable shading and whether chain colors or viewpoint
make rotation readable despite assembly symmetry.

Produce and inspect a second animation through documented capabilities, adding only example
settings and demonstrated missing functions. If Illustrate cannot represent the complete assembly
safely, change renderer; never split or truncate the requested complex to fit it.

### M4: Reproduce and document

Replay both animations from documented inputs in fresh tool processes. A disclosed graphical
session is acceptable; undocumented interactive adjustments are not. Reproduce scientific content,
timing and intended appearance, recording variability and application playback limits.

Complete tool guides, provenance records, agent guidance and an accurate README status that
distinguishes planned, demonstrated and reproduced capabilities. Repair missing instructions or
settings and repeat only affected checks. Archive this plan only when all required milestones
are complete; final replay is sequential and depends on complete sources and documentation.

## Verification strategy

Keep these evidence classes distinct:

| Check | Evidence | Failure response |
| --- | --- | --- |
| Scientific interpretation | Correct target, assembly, states, correspondence and motion class | Repair preparation or qualify the example |
| File handoff | Preserved identities, coordinates, frame count and ligand registration | Repair export/import or change native format |
| Visual quality | Reviewed stills, intermediates, moving surfaces and seam | Adjust settings or change renderer |
| Delivery | Decode, timing, dimensions, browser and Impress slideshow playback | Re-encode or document application limits |
| Reproduction | Replay from retained sources and commands | Remove hidden state or complete instructions |

Use temporary experimental checks. Retain permanent tests only for important new helper behavior,
such as selected-atom preservation or requested animation timing. Do not test third-party internals
or require identical pixels across platforms. Record elapsed rendering time, output size and peak
resource use where practical; do not invent performance gates.

Each example README records structural sources and retrieval date, hashes, selections/omissions,
motion method, native settings, versions, commands, licenses and actual checks. This is a short
provenance record, not a metadata schema or configuration language.

## Compatibility and risks

Repo Python uses source source_me.sh && python3. External applications retain their own runtimes.
Do not modify system Python for Blender, bundle ChimeraX, pin exact dependency requirements, or
assume Linux headless rendering proves the same capability on macOS. Preserve original mmCIF;
legacy exports require actual fidelity checks.

| Risk | Trigger | Responsible component | Mitigation |
| --- | --- | --- | --- |
| Unsupported motion | Attractive interpolation implies mechanism | Example author | Preserve endpoint context and label motion class |
| Missing/misregistered glucose | Morph/export drops or moves it | Preparation | Separate ligand and check coordinates/visibility |
| Graphics instability | Unattended invocation fails | Tool experiment | Keep Blender optional and disclose session needs |
| Legacy format loss | Identities or assembly members disappear | Export | Compare files and change renderer |
| Scope expansion | Toolbox becomes a framework | Plan owner | Require an example-level gap before new infrastructure |
| Untraceable claims | External recommendations become authority | Documentation | Use primary sources and local evidence |

## Close-out record

Preserve research material, human guidance and original inputs. Update changelog changes,
verification and failed approaches. Remove disposable experiments after retaining useful evidence.
Record execution status in
[toolbox_verification.md](../active_plans/reports/toolbox_verification.md).

M1-M4 are complete within the limits recorded in the verification report. The specification,
quality and integration reviews passed, and the plan is archived at this path.

Published MD, normal modes, interactive teaching objects, MCP exposure, Blender authoring and
a Rust renderer remain non-blocking follow-ons.
