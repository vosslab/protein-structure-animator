# protein-structure-animator

A growing toolbox for creating protein illustrations and animations for biochemistry teaching.
Documented tools and reproducible examples will help an LLM turn plain-language requests into
scientifically defensible visual materials.

**Status: completed examples within documented limits.** The 3N0G appearance comparison is
demonstrated. Both the hexokinase and GroEL animations have fresh replay, media decoding, browser
playback, and Impress GIF/MP4 slideshow evidence. Animated WebP embedded as an ODP image was blank
in the tested Impress version. Specification, code-quality and integration reviews passed. See the
[verification report](docs/active_plans/reports/toolbox_verification.md) and
[archived toolbox plan](docs/archive/protein_animation_toolbox.md). This is a documented tool
collection, not a general-purpose animation app.

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

Start with [docs/TOOLS.md](docs/TOOLS.md) to find available native capabilities and examples. Read
the [agent guidance](docs/ANIMATION_GUIDANCE.md) for scientific and delivery checks. The
[archived toolbox plan](docs/archive/protein_animation_toolbox.md) and
[execution ledger](docs/active_plans/workstreams/toolbox_execution.md) record completed acceptance
evidence and its limits.

The repository brings tools together through documentation and examples. An LLM can choose how
to combine them; example workflows are adaptable references. Small helper scripts will fill
demonstrated gaps in existing tools.

The current examples use Illustrate, Mol*, ChimeraX and FFmpeg. Blender remains optional and is not
required for the demonstrated Goodsell-inspired appearance. Tested versions are observations;
install current releases as described in the tool guides.

## Project notes

- [docs/HUMAN_GUIDANCE.md](docs/HUMAN_GUIDANCE.md): project priorities and practical constraints.
- [docs/DESIGN_DECISIONS.md](docs/DESIGN_DECISIONS.md): settled direction for the collection.
- [docs/CHANGELOG.md](docs/CHANGELOG.md): repository changes and verification notes.

## License

Source code: [LICENSE.LGPL-3.0](LICENSE.LGPL-3.0).

Documentation and other non-code materials: [LICENSE.CC-BY-4.0](LICENSE.CC-BY-4.0).
