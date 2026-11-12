# Human guidance

<!-- VENDORED HEADER: START -->
Record the durable guidance Neil Voss states, or approves for preservation here, in his own words:
first person or close paraphrase, one to three lines per bullet. Material he supplies as a source
may inform [DESIGN_DECISIONS.md](DESIGN_DECISIONS.md) once it is settled, and an entry of uncertain
origin belongs there too. Rules: [REPO_STYLE.md](REPO_STYLE.md).
[PROPAGATED HEADER - ENTRIES BELOW ARE YOURS]
<!-- VENDORED HEADER: END -->

- I want a collection of well-documented tools and example workflows that an LLM can combine for
  teaching animations; we do not need to design a perfect or mandatory workflow.
- I want to request animations in natural language and wait for the result, including examples
  such as hexokinase closing around glucose and a spinning GroEL.
- I like the Janet Iwasa and David Goodsell appearance and want to achieve it with free,
  open-source tools.
- I find Blender powerful, but it can be unstable enough to require a reboot on my Mac.
- Never pin dependency versions. Use current releases and open-ended `>=` minimums.

- For the README motion preview, use animated WebP instead of GIF.
- I want actual transparency in animated WebP, with tighter framing around each protein.
- I approved the ATP synthase motor proposal: a fixed camera, rotor moving against stator,
  membrane context, a shaft-revealing cutaway, and a few labels.

- Show the existing verified animation examples in the README and let their previews loop
  continuously.
- Not all animations should be square: a phone-style portrait or 16:9 widescreen can suit the
  protein. Use only one aspect per video, with some proteins tall and others wide.

- Use the sibling goodsell-oxillustrate-rs project as our gold standard method and canonical
  renderer for Goodsell figures and animations. Start with stills and GroEL; retain Mol* for
  surfaces and interactive views, and leave the existing hexokinase example unchanged.

- The current hexokinase protein is too transparent to see movement; make it more opaque so
  closure is clearer.
