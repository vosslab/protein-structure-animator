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

### Set screenshot dimensions through Mol* state

**Decision.** Set screenshot dimensions through Mol*'s native viewport values setter and verify the
resulting PNG dimensions before accepting a render.

**Why.** The previous assignment produced 638 x 638 PNGs despite an intended 640 x 640 canvas.

**Consequence.** Verify output dimensions from the actual image files. Regenerate each example and
its encoded media after this fix before treating all outputs as final delivery.

**Owner.** `examples/render_molstar.mjs` and the
[render delivery report](active_plans/reports/render_delivery_verification.md).
