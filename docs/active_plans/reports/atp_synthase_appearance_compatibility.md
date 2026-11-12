# 3N0G appearance scene compatibility

2026-11-12: removed the obsolete `trim:false` field from
`examples/appearance_3n0g/oxillustrate.json`. Current native oxillustrate always trims and rejects
that field. No selection, color, framing, or other scene setting changed. The prepared input
`output/appearance_3n0g/selected.cif` exists.

Focused checks confirmed valid JSON, absence of `trim`, retained 640 by 640 declared canvas and
DST/Mg selection rules, and a whitespace-clean diff. No render was run; current output is trimmed,
so the previous fixed-canvas description in the example README should be understood as historical
render evidence, not a claim about this current scene's output dimensions. Existing rendered assets
were left untouched.
