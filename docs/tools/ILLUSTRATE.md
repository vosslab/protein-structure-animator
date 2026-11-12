# Illustrate historical reference

This guide preserves the earlier Fortran comparison and its attribution. Use
[OXILLUSTRATE.md](OXILLUSTRATE.md) for the canonical Goodsell renderer; compiling Fortran is not
required for the default route. The commands and limitations below describe the historical run.

Goodsell's Fortran renderer produces atom spheres, depth shading and black contours. It does not
produce a solvent molecular surface. Upstream code is Apache-2.0; do not relabel or bundle it under
this repository's source license. Sources: [project](https://ccsb.scripps.edu/illustrate/),
[documentation](https://ccsb.scripps.edu/illustrate/documentation/), and
[source and license](https://github.com/ccsb-scripps/Illustrate).

## Compile and invoke

Tested here with Homebrew gfortran on Apple silicon. Install a current GCC/gfortran if needed;
fetch current upstream source into the ignored local dependency directory:

```bash
mkdir -p LOCAL_ONLY
git clone https://github.com/ccsb-scripps/Illustrate.git LOCAL_ONLY/illustrate
gfortran -O2 LOCAL_ONLY/illustrate/illustrate.f -o LOCAL_ONLY/illustrate/illustrate
source source_me.sh && python3 examples/appearance_3n0g/prepare.py
cd output/appearance_3n0g
../../LOCAL_ONLY/illustrate/illustrate < ../../examples/appearance_3n0g/illustrate.inp > illustrate.log
magick illustrate.pnm illustrate.webp
```

The program reads native command cards from stdin and writes PNM. The retained input file is
editable rendering source. ImageMagick only converts the result for convenient inspection.
Input atom descriptions match fixed PDB columns; a shifted wildcard can silently hide a ligand.
Check the rendered ligand and the reported atom count.

## Framing and limitations

Use fixed positive dimensions and a constant scale. `center auto` recomputes bounding-box centering
for each input, which can cause drift in animation; a successful still is not a tested trajectory
renderer. This example uses a single chain and a checked PDB compatibility export from original
mmCIF. Illustrate's x axis points down the page and y points across; `zrot 90` matches the Mol* view.

Upstream source inspected here allocates 350,000 coordinate slots and at most 3000 pixels per axis.
Its legacy parser and one-character chain assumptions still need data-specific checking. The
earlier complete GroEL example used Mol* directly from mmCIF. No Fortran Illustrate animation or
GroEL conversion was validated in that work. The Rust integration supersedes the former deferral;
its separate evidence belongs to [OXILLUSTRATE.md](OXILLUSTRATE.md).
