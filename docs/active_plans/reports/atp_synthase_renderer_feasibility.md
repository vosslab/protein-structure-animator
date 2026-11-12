# ATP synthase renderer feasibility

Read-only investigation dated 2026-11-12. Native Rust source and a bounded synthetic probe
establish renderer capabilities; they do not establish a biological assembly, motor mechanism,
accepted protein view, animation playback, or completed ATP synthase delivery.

## Recommendation

Use the native Rust renderer for transparent atom-sphere frames. It already exports clean straight
alpha to PNG and lossless WebP. Preserve its intentional unconditional trimming and export the
native crop origin through a small metadata addition. Reconstruct a fixed transparent animation
canvas from that origin before adding membrane context and a few labels.

Use an explicitly authored, stationary stator cutaway and rigid rotor transforms in per-frame
mmCIF inputs. Native scenes cannot independently move a selected rotor or clip only the stator.
Preserve the complete original input and an identity manifest for every omitted atom. Classify the
result as authored motor staging, with the separate science investigation defining the actual
rotor/stator groups, axis and biological limits.

## Source snapshot and binary

Sibling checkout: `/Users/vosslab/nsh/goodsell-oxillustrate-rs`.

- HEAD at investigation/probe time: `6e7736a746efcde1ed65cea965aae86cbc8dfcee`.
- Working tree at both probe starts: clean (`git status --short` is empty).
- CLI version: `illustrate 26.11.0`.
- Preexisting executable SHA-256:
  `aa3fecdfcb195e53a8947a54fc6f258c80b7c9de6e201e7bbcc38100b793d572`.
- Fresh offline release build SHA-256:
  `6efc78b13a1e7f9d6c9996f0edc3c7b6726667f4e1451ee3a434d8d242270937`.
- Fresh build used the clean current source and an animator-owned target directory; no sibling
  source or configuration was changed. Its binary differs from the preexisting binary, so the
  preexisting binary is not claimed to be a byte-identical current-HEAD build. Both binaries
  produced byte-identical successful image artifacts for this probe.
- Source hashes, command argv, return codes, stderr, decoded image measurements and image hashes
  are retained in `output/atp_synthase_feasibility/rust/probe_results.json` and its
  `clean_head/probe_results.json` counterpart.

Commands run from the animator root:

```bash
source source_me.sh && python3 output/atp_synthase_feasibility/rust/probe.py
cargo build --release --offline --manifest-path ../goodsell-oxillustrate-rs/Cargo.toml \
  --target-dir output/atp_synthase_feasibility/rust/build
source source_me.sh && python3 output/atp_synthase_feasibility/rust/probe.py \
  output/atp_synthase_feasibility/rust/build/release/illustrate
```

The offline release build took 9.71 seconds. These are native CPU-only CLI operations; no GUI,
GPU session, browser or Blender was launched. Graphics probes ran sequentially in manager-granted
slots. Build output and probes stay in ignored `output/`.

## Current native contract

Source references below are sibling paths at the recorded HEAD, not animator source files.

| Capability | Native behavior and source evidence |
| --- | --- |
| Input and command | Local PDB, mmCIF or PDBML; `--scene JSON --output PNG/WEBP`; `src/command_line.rs:15-26,94-104` |
| Alpha background | `background: null` or absent is transparent; explicit RGB is opaque; `src/settings.rs:28-29,40-55` |
| CLI override | `--background transparent`, `white`, or `black`; `src/command_line.rs:40-50,86-91` |
| Alpha construction | Atom pixels have alpha 255; otherwise native outline coverage supplies alpha; `src/render.rs:27-34,40-60` |
| Encoding | Straight alpha packed into RGBA, PNG RGBA, lossless WebP RGBA; `src/rendered_image.rs:91-108,134-165` |
| Selection | Exact author/label chain, element, residue name/range, atom name and atom kind; `src/settings.rs:96-135` |
| Rule priority | First matching atom rule wins; unspecified properties retain defaults, not later rules; `src/scene_preparation.rs:199-212,223-240` |
| Omissions | Native defaults omit waters, hydrogen and deuterium; explicit rule `omit:false` restores matches; `src/scene_preparation.rs:205-212` |
| Coordinate transforms | Assembly transform, global rotation, subtract framing center, add translation, scale and viewport offset; `src/scene_preparation.rs:241-249,282-310` |
| Rotation | Right-handed positive-angle column matrices applied Z, Y, then X; `src/scene_preparation.rs:154-166` |
| Screen axes | Native x is image row/down; y is column/right; z points toward viewer; `src/scene.rs:5-7` |
| Framing | Explicit center is in rotated coordinates; explicit scale is pixels per Angstrom; `src/settings.rs:62-69` |
| Automatic fitting | Uses visible sphere bounds, with automatic depth burial; `src/scene_preparation.rs:270-299` |
| Output crop | Always trims to coverage plus up to three pixels; origin is computed then discarded; `src/render.rs:37-46,65-92` |
| Crop origin export | None in API or CLI; `RenderedImage` has width, height, dpi, pixels and alpha only; `src/rendered_image.rs:12-23` |
| Animation | CLI renders one static scene; no timeline or selection-specific transformation in scene settings; `src/command_line.rs:99-104`, `src/settings.rs:11-38,85-112` |

For fixed-camera motor staging, keep one global orientation, rotation axis/origin, framing center,
scale and native canvas across all frames. Use a positive framing-center z beyond every rotated
atom center plus radius to avoid accidental native zero-plane clipping. Use common bounds across
the whole motion rather than fitting each pose independently. Keep fog endpoints equal to one
to avoid pose-dependent depth-fog normalization, while retaining native shadows as desired.

## Zero-plane cutaway limits

The native zero plane is global, after the full geometry/framing transformation:

1. A sphere whose prepared center z is greater than or equal to zero is discarded entirely
   (`src/raster.rs:52-56`).
2. A retained sphere uses its full projected circular silhouette and front-hemisphere surface
   depth, `center_z + sqrt(radius_squared - distance_squared)` (`src/raster.rs:70-90`).
3. Nearest ownership is chosen with that raw surface depth. Stored depths are then clamped to
   at most zero (`src/raster.rs:95-102`).

This is not an arbitrary clipping-plane interface or a selectively capped solid cutaway. It
cannot expose a rotor while protecting rotor atoms in front of the same plane. Native atom
selectors contain no position predicate, plane, angle wedge, per-atom alpha or local transform.

The smallest selective cutaway is external preparation: in one fixed body/view coordinate frame,
choose the stationary front wedge once, omit only the designated stator atoms, and keep the
complete rotor selection. Save a derived cutaway mmCIF and the omitted identities beside the
original hash. Then rotate only the rotor atoms about the independently established motor axis in
derived per-frame mmCIF files. Do not reevaluate the stationary omission mask as the rotor moves.
Whole-chain stator omission can instead use native `omit:true` rules if the scientific/visual
design accepts that coarser cutaway. A partial wedge requires the derived input.

## Alpha probe evidence

Three synthetic carbon spheres use white, red and blue chain colors, fixed radius 2 Angstrom,
scale 4 pixels per Angstrom, no shadows, default native outlines and a requested 96 x 64 canvas.
The synthetic fixture is a renderer probe, not a protein model.

| Measurement | Both preexisting and fresh-HEAD binaries |
| --- | --- |
| Transparent PNG and WebP | RGBA; decoded pixel arrays identical |
| Native trimmed output | 65 x 45 pixels |
| Alpha histogram | 0:2094, 55:84, 110:24, 164:24, 219:36, 255:663 |
| Fully opaque white pixels | 109; white object survives unchanged |
| Partial-alpha pixels | Black RGB outline pixels; no white or colored matte |
| Composite over white | Exact match to native opaque-white RGB, maximum channel delta 0 |
| Composite over black | Exact match to native opaque-black RGB, maximum channel delta 0 |
| Zero-plane variant | 45 x 45; front red sphere disappears, retained blue/white remain |
| Scene `trim:false` | Rejected with `unknown field trim`; no output produced |

Native alpha is the reliable matte. White chroma keying would destroy the 109 legitimate opaque
white pixels in this probe and cannot recover original edge coverage from an opaque render.
No chroma keying, matte inference, fake sentinel atoms or background-removal algorithm is needed.

## Fixed-canvas handoff

Sibling human guidance explicitly requires unconditional trimming:
`docs/HUMAN_GUIDANCE.md:14-15`; the settled contract is
`docs/DESIGN_DECISIONS.md:149-164`. Existing animator `trim:false` scenes are now incompatible
with this native source. Preserve historical receipts, and omit that obsolete key in new scenes.

The manager selected a narrow upstream follow-on: optional `--metadata PATH`, with
`{"canvas":[width,height],"crop_origin":[left,top]}` directly from the already computed native
bounds. Preserve unconditional cropping and all image pixels. Consumer preparation should paste
each cropped RGBA image at `[left,top]` on the common transparent canvas, with one common crop or
scale for the final aspect if needed. Centering each cropped frame independently can make the
motor wobble; equal dimensions alone do not prove registration.

Implementation sites are `src/render.rs:65-92` for retaining origin and
`src/command_line.rs:99-112` for optional metadata delivery. A backward-compatible API option is
`render_with_bounds(&Scene) -> Result<(RenderedImage, [u32; 2]), Error>` plus the existing
`render(&Scene)` wrapper. It avoids changing every `RenderedImage` literal and keeps one copy
of the renderer's coverage/outline logic. The follow-on owner chooses the concrete API shape.
The diagnostic example `examples/render_passes.rs:31-110` can already emit full-canvas images,
but privately includes renderer internals and repeats composition/bounds logic; it is evidence
tooling, not a suitable animator production dependency.

Stationary stator or membrane extrema might keep all frame crops identical, but that is a
measurement-dependent optimization. Native crop-origin metadata works even when extrema change
and does not require fake structural anchors.

## Evidence still outstanding

This investigation does not render ATP synthase, select its biological assembly, establish a
motor axis, validate cutaway interpretation, or accept labels/membrane placement. Static alpha
round trips do not prove animated WebP alpha, loop behavior or browser/Impress playback. Those
checks belong to the requested example's science, rendering, encoding and playback workstreams.

No sibling product changes, dependencies, version pins, full suites or external primary-record
research were performed here. The source contract and tiny fresh-process CPU reproducer are the
verified scope.
