# ChimeraX preparation

ChimeraX provides alignment, native internal-coordinate morphing, coordinate export and editable
sessions. Invoke an installed application; do not bundle it. The
[license](https://www.rbvi.ucsf.edu/chimerax/docs/licensing.html) permits qualifying noncommercial
use and has separate commercial terms. It is not an open-source-only component of this route.
Use [Mol*](MOLSTAR.md) and [Illustrate](ILLUSTRATE.md) for the open-source rendering experiments.

## Tested native invocation

The installed Mac application is ChimeraX 1.10.1, dated 2025-07-24. This is an environment
observation, not a version pin. The examples use its own Python runtime and bundled NumPy:

```bash
/Applications/ChimeraX-1.10.1.app/Contents/bin/ChimeraX --nogui --exit \
  examples/hexokinase_closure/prepare.py > output/hexokinase_closure.log 2>&1
```

Use your installed application's path. Start from a fresh process and the repository root.
ChimeraX needs its normal user data and cache directories. The agent sandbox initially denied
cache creation; the same command succeeded with ordinary application access.

ChimeraX executes scripts with an injected `session`, rather than `__name__ == '__main__'`.
The retained script uses this native entry point. Do not run it with repository Python or install
ChimeraX into the system Python. Other repo Python commands use `source source_me.sh && python3`.

## Motion and export

The example first selects corresponding protein atoms, deliberately aligns a stable region, and
then uses native `morph` with internal coordinates and sinusoidal rates. It registers every frame
to the same region afterward. Coordinate slots can retain deleted-atom holes; use active atom
coordinates instead of assuming that `coordset.xyzs` has one row per current atom.

**Observed export failure:** `save trajectory.cif allCoordsets true` wrote 125 models with identical
coordinates in this installation. The native `save trajectory.pdb allCoordsets true` preserved the
motion. All selected atom names, residue numbers and chain IDs fit legacy PDB; coordinate error
against in-memory positions is below 0.00051 angstrom per component. Original mmCIF endpoints and
the native CXS session remain available. Recheck this failure on newer ChimeraX releases rather
than assuming it is universal.

Primary references: [morph](https://www.rbvi.ucsf.edu/chimerax/docs/user/commands/morph.html),
[align](https://www.rbvi.ucsf.edu/chimerax/docs/user/commands/align.html),
[save](https://www.rbvi.ucsf.edu/chimerax/docs/user/commands/save.html), and
[startup options](https://www.rbvi.ucsf.edu/chimerax/docs/user/options.html).
The installed manual documents windowless rendering on Linux. The Mac `--nogui` preparation result
does not establish windowless image rendering.
