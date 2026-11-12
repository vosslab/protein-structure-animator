# protein-structure-animator

A growing toolbox for creating protein illustrations and animations for biochemistry teaching.
Documented tools and reproducible examples will help an LLM turn plain-language requests into
scientifically defensible visual materials.

**Status: research and planning.** Tool comparisons and an initial plan are available; working
animation examples and a runnable generator are not yet implemented.

<!-- screenshots:begin (managed by screenshot-docs) -->
<!-- screenshots:end -->

## From request to animation

The intended experience starts with a request such as:

> Show hexokinase closing around glucose with a Goodsell-style appearance, highlighted glucose,
> a white background, and a seamless five-second loop.

The goal is to deliver the animation together with editable sources, structural references, and
a short explanation of the method. The collection will support examples such as:

- Rotating a complete GroEL assembly to show its shape.
- Illustrating hexokinase closure between experimental structural states.
- Applying Goodsell-inspired spacefill or outlined molecular-surface styles.
- Rendering published molecular dynamics trajectories with their scientific context preserved.

Experimental structures, interpolated motion, simulations, and illustrative staging should remain
clearly distinguishable.

## Start here

Read the [toolbox plan](docs/active_plans/active/protein_animation_toolbox.md) for the researched
tool candidates, tradeoffs, first examples, and completion checks. The first planned milestone is
an agent-produced hexokinase animation, followed by a GroEL rotation to demonstrate reuse.

The repository brings tools together through documentation and examples. An LLM can choose how
to combine them; example workflows are adaptable references. Small helper scripts will fill
demonstrated gaps in existing tools.

Candidates include Illustrate, Mol*, ChimeraX, and FFmpeg, with Blender-based tools as optional
alternatives. Blender is not required for a Goodsell-style appearance. Installation and rendering
instructions will follow verified examples rather than an assumed universal setup.

## Project notes

- [docs/HUMAN_GUIDANCE.md](docs/HUMAN_GUIDANCE.md): project priorities and practical constraints.
- [docs/DESIGN_DECISIONS.md](docs/DESIGN_DECISIONS.md): settled direction for the collection.
- [docs/CHANGELOG.md](docs/CHANGELOG.md): repository changes and verification notes.

## License

Source code: [LICENSE.LGPL-3.0](LICENSE.LGPL-3.0).

Documentation and other non-code materials: [LICENSE.CC-BY-4.0](LICENSE.CC-BY-4.0).
