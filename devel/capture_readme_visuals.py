#!/usr/bin/env python3
"""Refresh the README gallery from verified native example frames.

Run: source source_me.sh && python3 devel/capture_readme_visuals.py
Requires the declared Pillow dependency with WebP support and cwebp on PATH. Each clip keeps
one fixed canvas and framing; molecular images are never enlarged or re-rendered here.
"""

# Standard Library
import json
import shutil
import hashlib
import pathlib
import tempfile
import datetime
import subprocess

# PIP3 modules
import PIL.Image
import PIL.features

# ASVS 5.3.2: generated paths are fixed relative to this repository.
ROOT = pathlib.Path(subprocess.run(
	["git", "rev-parse", "--show-toplevel"], cwd=pathlib.Path(__file__).resolve().parent,
	check=True, capture_output=True, text=True,
).stdout.strip())
BEGIN = "<!-- screenshots:begin (managed by screenshot-docs) -->"
END = "<!-- screenshots:end -->"
GALLERY = '''## Animation gallery

### ATP synthase: see the motor

<a href="examples/atp_synthase_motor/README.md">
  <picture>
    <source media="(prefers-reduced-motion: reduce)"
      srcset="docs/screenshots/atp_synthase_motor_poster.webp">
    <img src="docs/screenshots/atp_synthase_motor.webp" width="360"
      alt="Rust Goodsell ATP synthase rotor turns inside a fixed stator cutaway across a membrane">
  </picture>
</a>

ATP synthase couples rotation to ATP production. This authored Rust Goodsell
illustration turns the rotor against a fixed stator; a cutaway exposes the shaft. The camera stays
fixed. It illustrates neither measured kinetics, validated steric motion nor the full reaction.
Try: "Turn the ATP synthase rotor inside a fixed stator, exposing the shaft through a cutaway."
Reproduce: [examples/atp_synthase_motor/README.md](examples/atp_synthase_motor/README.md) |
[Transparent WebP](docs/screenshots/atp_synthase_motor.webp) |
[Static poster](docs/screenshots/atp_synthase_motor_poster.webp).

### GroEL: see the assembly

<a href="examples/groel_rotation/README.md">
  <picture>
    <source media="(prefers-reduced-motion: reduce)"
      srcset="docs/screenshots/groel_rotation_alpha_poster.webp">
    <img src="docs/screenshots/groel_rotation_alpha.webp" width="640"
      alt="Rust Goodsell view rotates the complete fourteen-subunit GroEL assembly">
  </picture>
</a>

The complete fourteen-subunit chaperonin provides a compartment for protein folding. This Rust
Goodsell loop changes viewpoint only; it shows neither GroES nor a folding cycle.
Try: "Rotate the complete GroEL assembly once, keeping its chain colors and a transparent background."
Reproduce: [examples/groel_rotation/README.md](examples/groel_rotation/README.md) |
[Transparent WebP](docs/screenshots/groel_rotation_alpha.webp) |
[Static poster](docs/screenshots/groel_rotation_alpha_poster.webp).

### Hexokinase: see the closure

<a href="examples/hexokinase_closure/README.md">
  <picture>
    <source media="(prefers-reduced-motion: reduce)"
      srcset="docs/screenshots/hexokinase_closure_alpha_poster.webp">
    <img src="docs/screenshots/hexokinase_closure_alpha.webp" width="360"
      alt="Mol* transparent hexokinase surface closes and reopens around fixed magenta glucose">
  </picture>
</a>

Hexokinase's lobes close around glucose: a teaching illustration of induced fit. This Mol* loop
interpolates experimental protein endpoints around a fixed, staged glucose
pose; it is not a measured binding path or a catalytic cycle.
Try: "Show hexokinase closing and reopening, with glucose visible through the surface."
Reproduce: [examples/hexokinase_closure/README.md](examples/hexokinase_closure/README.md) |
[Transparent WebP](docs/screenshots/hexokinase_closure_alpha.webp) |
[Static poster](docs/screenshots/hexokinase_closure_alpha_poster.webp).

All three transparent previews loop continuously over five seconds. Reduced-motion preferences
select matching static posters; the poster links also work independently. Each clip keeps one
fixed canvas and protein scale through the complete motion.

### Appearance options

These **static 3N0G stills** compare representation choices for the same isoprene synthase example.
Choose spheres for atom detail or a smooth surface for overall shape.

<p>
  <a href="examples/appearance_3n0g/README.md"><img
    src="examples/appearance_3n0g/oxillustrate_preview.webp" width="240"
    alt="Rust oxillustrate: canonical Goodsell atom spheres"></a>
  <a href="examples/appearance_3n0g/README.md"><img
    src="examples/appearance_3n0g/molstar_spacefill.webp" width="240"
    alt="Mol*: illustrated atom spheres"></a>
  <a href="examples/appearance_3n0g/README.md"><img
    src="examples/appearance_3n0g/molstar_surface.webp" width="240"
    alt="Mol*: smooth molecular surface"></a>
</p>

In order: **Rust oxillustrate spheres** (canonical Goodsell), **Mol\\* spheres**,
**Mol\\* smooth surface**. Blue protein, contrasting ligand and magnesium retain the example palette.

Reproduce: [examples/appearance_3n0g/README.md](examples/appearance_3n0g/README.md).'''


#============================================
def update_readme(text: str) -> str:
	"""Replace exactly the managed interior, preserving the surrounding README."""
	if text.count(BEGIN) != 1 or text.count(END) != 1:
		raise ValueError("README must contain exactly one screenshot sentinel pair.")
	before, remainder = text.split(BEGIN)
	_, after = remainder.split(END)
	return f"{before}{BEGIN}\n{GALLERY}\n{END}{after}"


#============================================
def framed_image(
	path: pathlib.Path, size: tuple[int, int], crop: tuple[int, int, int, int],
) -> PIL.Image.Image:
	"""Fit a whole-motion crop into one transparent canvas without enlarging it."""
	with PIL.Image.open(path) as image:
		protein = image.convert("RGBA").crop(crop)
	protein.thumbnail(size, PIL.Image.Resampling.LANCZOS)
	frame = PIL.Image.new("RGBA", size, (0, 0, 0, 0))
	frame.paste(protein, ((size[0] - protein.width) // 2, (size[1] - protein.height) // 2))
	return frame


#============================================
def union_crop(sources: list[pathlib.Path]) -> tuple[int, int, int, int]:
	"""Validate all RGBA frames and retain every visible pixel with ten-pixel padding."""
	with PIL.Image.open(sources[0]) as image:
		size = image.size
	left, top, right, bottom = size[0], size[1], 0, 0
	for path in sources:
		with PIL.Image.open(path) as image:
			if image.size != size or image.mode != "RGBA":
				raise ValueError(f"Expected fixed-size native RGBA frames: {path}")
			alpha = image.getchannel("A")
			bounds = alpha.getbbox()
			if bounds is None or alpha.getextrema()[0] != 0:
				raise ValueError(f"Expected visible content and true transparent background: {path}")
			left, top = min(left, bounds[0]), min(top, bounds[1])
			right, bottom = max(right, bounds[2]), max(bottom, bounds[3])
	return left - 10, top - 10, right + 10, bottom + 10


#============================================
def main() -> None:
	"""Encode three true-alpha loops and matching posters, then refresh the gallery."""
	readme = ROOT / "README.md"
	updated_readme = update_readme(readme.read_text())
	if shutil.which("cwebp") is None:
		raise RuntimeError("Install cwebp before capturing README visuals.")
	if not PIL.features.check("webp"):
		raise RuntimeError("Install Pillow with WebP support before capturing README visuals.")
	# Sample the five-second source uniformly without duplicating the loop endpoint.
	indices = [round(index * 125 / 60) for index in range(60)]
	durations = [round((index + 1) * 1000 / 12) - round(index * 1000 / 12)
		for index in range(60)]
	assets = ROOT / "docs/screenshots"
	records = []
	with tempfile.TemporaryDirectory(prefix="protein_readme_") as temporary:
		work = pathlib.Path(temporary)
		for example, animation, size in (
			("atp_synthase_motor", "atp_synthase_motor", (480, 720)),
			("groel_rotation_alpha", "groel_rotation_alpha", (640, 480)),
			("hexokinase_closure_alpha", "hexokinase_closure_alpha", (360, 540)),
		):
			directory = ROOT / "output" / example / "frames"
			sources = [directory / f"frame_{index:03d}.png" for index in range(125)]
			if sorted(directory.glob("frame_*.png")) != sources:
				raise ValueError(f"Expected exactly 125 sequential native frames: {directory}")
			crop = union_crop(sources)
			frames = [framed_image(sources[index], size, crop) for index in indices]
			poster = animation + "_poster.webp"
			animation += ".webp"
			frames[0].save(
				work / animation, save_all=True, append_images=frames[1:],
				quality=90, loop=0, duration=durations,
			)
			frames[0].save(work / "poster.png")
			# ASVS 1.2.5: pass command arguments directly, without a shell interpreter.
			subprocess.run([
				"cwebp", "-quiet", "-q", "90", str(work / "poster.png"),
				"-o", str(work / poster),
			], check=True)
			assets.mkdir(exist_ok=True)
			for name in (animation, poster):
				shutil.copyfile(work / name, assets / name)
				print(f"Wrote docs/screenshots/{name} ({(assets / name).stat().st_size} bytes)")
			digest = hashlib.sha256(b"".join(source.read_bytes() for source in sources)).hexdigest()
			print(f"Source SHA256 (125 frames): {directory.relative_to(ROOT)} {digest}")
			records.append({"source": str(directory.relative_to(ROOT)), "source_sha256": digest,
				"crop": crop, "size": size, "animation": animation, "poster": poster})
	evidence = ROOT / "output/atp_synthase_gallery"
	evidence.mkdir(exist_ok=True)
	(evidence / "capture_manifest.json").write_text(json.dumps(records, indent=2) + "\n")
	if readme.read_text() != updated_readme:
		readme.write_text(updated_readme)
	print(f"Captured {datetime.datetime.now(datetime.UTC).isoformat()}")


if __name__ == "__main__":
	main()
