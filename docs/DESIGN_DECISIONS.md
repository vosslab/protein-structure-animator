# Design decisions

<!-- VENDORED HEADER: START -->
Record each durable decision about how this code and repository are shaped, once it is settled, with
the reasoning a later reader needs. Guidance Neil Voss states belongs in
[HUMAN_GUIDANCE.md](HUMAN_GUIDANCE.md), dated history in `docs/CHANGELOG.md`, open discussion in
`docs/active_plans/decisions/`. [PROPAGATED HEADER - ENTRIES BELOW ARE YOURS]
<!-- VENDORED HEADER: END -->

Write each decision as a level-three heading with these four fields. `Owner` names the
authoritative code or contract document, rather than a person.

```markdown
### <decision title>

**Decision.** <the durable direction>

**Why.** <the reason it was chosen>

**Consequence.** <the constraint a future change preserves>

**Owner.** <the authoritative code or contract doc>
```

### Fixed-aspect README motion previews

**Decision.** Present existing verified examples as continuous five-second WebP previews, each
with one fixed aspect and a matching reduced-motion poster. Current tighter framing uses 4:3
GroEL and 2:3 hexokinase/ATP synthase. Retain molecular proportions and downsize-only fixed framing.

**Why.** The human requested looping examples and varied protein-appropriate canvas shapes, with
exactly one aspect per video.

**Consequence.** The gallery derives lightweight presentation assets from existing native frames.
Scientific motion and source coordinates stay owned by the original examples. Native transparent
rerenders use separate generated directories; retain historical gallery assets and their receipts.
The gallery itself adds no molecular or renderer capability claim.

**Owner.** [animation_gallery.md](archive/animation_gallery.md) and
[capture_readme_visuals.py](../devel/capture_readme_visuals.py).

### Preserve native alpha and registration

**Decision.** Preserve native straight alpha through PNG, animated WebP and posters. Reconstruct
fixed Rust animation canvases using the native crop origin while retaining unconditional trimming.
Use one whole-motion union crop and padding, with fixed scale and aspect. MP4 and GIF composite
explicitly onto white.

**Why.** Native alpha preserves white atoms and outline coverage. Independently centering trimmed
frames can introduce wobble; equal image dimensions alone do not establish registration.

**Consequence.** Require the current sibling metadata interface rather than obsolete `trim:false`
scenes. Avoid chromakey and fake structural anchors. Native GroEL and Mol* hexokinase alpha
opt-ins write separate output directories, preserving opaque example deliveries. Verify real
decoded RGBA, light/dark playback and fresh-process replay separately.

**Owner.** [OXILLUSTRATE.md](tools/OXILLUSTRATE.md), [MEDIA.md](tools/MEDIA.md),
[encode_loop.py](../tools/encode_loop.py) and
[capture_readme_visuals.py](../devel/capture_readme_visuals.py).

### Authored ATP synthase motor

**Decision.** Use one complete 8DBU epsilon-down E. coli assembly. Rotate label chains G-R as one
rigid rotor against a frozen head/stator and stationary ligands, with a fixed stator cutaway,
schematic membrane and sparse labels.

**Why.** Primary structural evidence supports this complete subunit assembly and compact epsilon
state, while a simple rotor illustration makes the motor relationship visible.

**Consequence.** Preserve the original input, uncut per-frame coordinates and explicit omitted-atom
identities. Describe the engineered construct and missing residues honestly. The motion is authored
mechanical illustration, not a sterically validated catalytic trajectory, kinetics or chemistry;
rigid rotation through a frozen head can clash. Do not infer nucleotide conversion from head ATP.

**Owner.** [atp_synthase_alpha.md](archive/atp_synthase_alpha.md) and
[atp_synthase_science_feasibility.md](active_plans/reports/atp_synthase_science_feasibility.md).

### Preserve molecular handedness in cameras

**Decision.** Use a proper determinant +1 ATP camera rotation, with column equal to negative local
x. Reject the exploratory reflected view and regenerate all coordinate handoffs before rendering.
Display the final 480 x 720 ATP gallery canvas at 360 pixels wide in the README.

**Why.** A reflected camera preserves distances but reverses molecular handedness and apparent
rotation. Corrected native frames and teaching-size inspection support the chosen composition.

**Consequence.** Check camera orientation as well as distances. Preserve the fixed cutaway, source
axis and signed rotor motion. Keep the complete native canvas and one aspect at every display size.

**Owner.** [render_oxillustrate.py](../examples/atp_synthase_motor/render_oxillustrate.py),
[test_atp_synthase_geometry.py](../tests/test_atp_synthase_geometry.py) and
[atp_synthase_render.md](active_plans/reports/atp_synthase_render.md).

### Documented capability collection

**Decision.** Organize the project around accessible tools, reproducible examples, and agent
guidance. Examples are adaptable references; the agent chooses how to combine capabilities.

**Why.** The human explicitly prefers well-documented tools over designing a perfect workflow.

**Consequence.** Select tools through concrete experiments. Keep Blender optional, and defer any
universal orchestration framework or renderer interface until a demonstrated need exists.

**Owner.** [HUMAN_GUIDANCE.md](HUMAN_GUIDANCE.md) and the
[toolbox plan](archive/protein_animation_toolbox.md).

### Native tools without a shared framework

**Decision.** Keep the toolbox as documented native tools and scripts. Add no new application,
API, adapter layer or recipe format without an example that demonstrates the need.

**Why.** The examples can combine existing native capabilities, while a shared abstraction would
add maintenance without demonstrated reuse needs.

**Consequence.** Each example records its own native commands and settings. The agent chooses the
combination that fits the scientific request.

**Owner.** [ANIMATION_GUIDANCE.md](ANIMATION_GUIDANCE.md) and the
[toolbox plan](archive/protein_animation_toolbox.md).

### Preserve structures and verify handoffs

**Decision.** Preserve original mmCIF inputs. Use the tested native PDB trajectory for the current
hexokinase renderer handoff because the tested ChimeraX mmCIF export repeated coordinates.

**Why.** Direct comparison found that PDB preserved atom identities and coordinates for this
trajectory while the local mmCIF export did not preserve motion.

**Consequence.** Compare identities and coordinates after export and import, including glucose
registration. Do not generalize this format failure to other releases or structures.

**Owner.** [CHIMERAX.md](tools/CHIMERAX.md) and the
[hexokinase example](../examples/hexokinase_closure/README.md).

### Separate playback and replay evidence

**Decision.** Record media decoding, browser playback, Impress playback and fresh-process replay as
separate checks. Keep the plan active until required checks pass and are reviewed.

**Why.** A successful render or encode does not show that an application plays the result or that
the documented commands reproduce it from a clean process.

**Consequence.** Do not claim M4 complete before playback and replay evidence is recorded. Complete
specification, quality and integration reviews before proposing archive.

**Owner.** [toolbox verification](active_plans/reports/toolbox_verification.md) and
[execution ledger](active_plans/workstreams/toolbox_execution.md).

### Keep dependency requirements forward-compatible

**Decision.** Specify current dependencies with open-ended `>=` minimums. Record tested versions as
observations rather than pins.

**Why.** The project requires current releases and does not want dependency requirements to block
forward updates.

**Consequence.** Refresh lockfiles forward and document the resolved versions used for each
verification run.

**Owner.** [TOOLS.md](TOOLS.md) and dependency requirements.

### Separate TypeScript runtime consumers

**Decision.** Keep the latest TypeScript compiler available through `@typescript/native` and give
`typescript-eslint` a separate TypeScript 6 compatibility alias through `typescript`.

**Why.** The latest compiler requirement is explicit, while the current `typescript-eslint` release
rejects TypeScript 7 when loading its compiler API.

**Consequence.** Keep both dependency floors open-ended and verify the latest compiler and the
TypeScript 6-backed lint integration independently. Do not claim full TypeScript 7 compatibility
for tools that consume the compatibility alias.

**Owner.** `package.json`, `package-lock.json` and
[dependency verification](active_plans/reports/dependency_verification.md).

### Override vulnerable development matching

**Decision.** Remove unused direct minimatch and require `minimatch >=11.0.8` through a root npm
override while retaining current ESLint, typescript-eslint and both TypeScript aliases.

**Why.** Current parent ranges still select vulnerable v10; npm's forced remediation proposes
downgrades. Their actual matching APIs pass focused v11 consumer checks and a clean installation.

**Consequence.** This crosses parent major-version ranges. Reassess when current parents accept
patched minimatch directly, and repeat consumer checks if an open-ended refresh changes its major.

**Owner.** `package.json`, `package-lock.json` and
[minimatch_remediation.md](active_plans/audits/minimatch_remediation.md).

### Set screenshot dimensions through Mol* state

**Decision.** Set screenshot dimensions through Mol*'s native viewport values setter and verify the
resulting PNG dimensions before accepting a render.

**Why.** The previous assignment produced 638 x 638 PNGs despite an intended 640 x 640 canvas.

**Consequence.** Verify output dimensions from the actual image files. Regenerate each example and
its encoded media after this fix before treating all outputs as final delivery.

**Owner.** `examples/render_molstar.mjs` and the
[render delivery report](active_plans/reports/render_delivery_verification.md).

### Canonical Goodsell rendering

**Decision.** Use the native CLI from sibling `goodsell-oxillustrate-rs` as the canonical renderer
and visual gold standard for Goodsell figures and animations. First integration scope is the
3N0G still and the complete GroEL rotation.

**Why.** The human chose this route. Demonstration checks establish its implemented capabilities
and delivery evidence; they do not reopen adoption as a renderer competition.

**Consequence.** Build the current sibling checkout and invoke its external binary. Preserve native
JSON scenes, original input hashes and observed source/binary provenance. Add no bindings, shared
renderer framework or automatic fallback. Mol* serves surfaces, interactive work and retained
alternatives; existing hexokinase work remains unchanged. Preserve Fortran reference attribution
and historical evidence. The external AGPL-3.0-only binary is not bundled or relicensed here.

**Owner.** [OXILLUSTRATE.md](tools/OXILLUSTRATE.md),
[ANIMATION_GUIDANCE.md](ANIMATION_GUIDANCE.md) and the
[oxillustrate integration plan](archive/oxillustrate_integration.md).
