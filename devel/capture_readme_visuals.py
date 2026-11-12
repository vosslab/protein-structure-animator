#!/usr/bin/env python3
"""Refresh the README gallery from verified native example frames.

Run: source source_me.sh && python3 devel/capture_readme_visuals.py
Requires the declared Pillow dependency with WebP support and cwebp on PATH. Each clip keeps
one fixed canvas and framing; molecular images are never enlarged or re-rendered here.
"""

# Standard Library
import shutil
import hashlib
import pathlib
import tempfile
import datetime
import subprocess

# PIP3 modules
import PIL.Image
import PIL.features
import PIL.ImageChops

# ASVS 5.3.2: generated paths are fixed relative to this repository.
ROOT = pathlib.Path(subprocess.run(
	["git", "rev-parse", "--show-toplevel"], cwd=pathlib.Path(__file__).resolve().parent,
	check=True, capture_output=True, text=True,
).stdout.strip())
BEGIN = "<!-- screenshots:begin (managed by screenshot-docs) -->"
END = "<!-- screenshots:end -->"
GALLERY = '''## Animation gallery

### GroEL: see the assembly

<a href="examples/groel_rotation/README.md">
  <picture>
    <source media="(prefers-reduced-motion: reduce)"
      srcset="docs/screenshots/groel_rotation_poster.webp">
    <img src="docs/screenshots/groel_rotation_demo.webp" width="640"
      alt="Rust Goodsell view rotates the complete fourteen-subunit GroEL assembly">
  </picture>
</a>

The complete fourteen-subunit chaperonin provides a compartment for protein folding. This
**16:9 widescreen** Rust Goodsell loop changes viewpoint only; it shows neither GroES nor a folding
cycle.
Try: "Rotate the complete GroEL assembly once, keeping the chain colors and white background."
Reproduce: [examples/groel_rotation/README.md](examples/groel_rotation/README.md) |
[Static poster](docs/screenshots/groel_rotation_poster.webp).

### Hexokinase: see the closure

<a href="examples/hexokinase_closure/README.md">
  <picture>
    <source media="(prefers-reduced-motion: reduce)"
      srcset="docs/screenshots/hexokinase_closure_poster.webp">
    <img src="docs/screenshots/hexokinase_closure_loop.webp" width="240"
      alt="Mol* transparent hexokinase surface closes and reopens around fixed magenta glucose">
  </picture>
</a>

Hexokinase's lobes close around glucose: a teaching illustration of induced fit. This **phone-style
portrait** Mol* loop interpolates experimental protein endpoints around a fixed, staged glucose
pose; it is not a measured binding path or a catalytic cycle.
Try: "Show hexokinase closing and reopening, with glucose visible through the surface."
Reproduce: [examples/hexokinase_closure/README.md](examples/hexokinase_closure/README.md) |
[Static poster](docs/screenshots/hexokinase_closure_poster.webp).

Both previews loop continuously over five seconds. Reduced-motion preferences select the matching
static posters; the poster links also work independently.

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
	path: pathlib.Path, size: tuple[int, int], crop: tuple[int, int, int, int] | None,
) -> PIL.Image.Image:
	"""Fit a source into one fixed canvas, preserving its proportions and white margins."""
	with PIL.Image.open(path) as image:
		if image.size != (640, 640):
			raise ValueError(f"Expected a native 640 x 640 example frame: {path}")
		protein = image.convert("RGB")
	if crop is not None:
		# shortcut: fixed camera margins; review the crop when the example camera changes.
		bounds = PIL.ImageChops.difference(
			protein, PIL.Image.new("RGB", protein.size, "white"),
		).getbbox()
		if bounds and any((
			bounds[0] < crop[0], bounds[1] < crop[1],
			bounds[2] > crop[2], bounds[3] > crop[3],
		)):
			raise ValueError(f"Fixed gallery crop would remove visible content: {path}")
		protein = protein.crop(crop)
	protein.thumbnail(size, PIL.Image.Resampling.LANCZOS)
	frame = PIL.Image.new("RGB", size, "white")
	frame.paste(protein, ((size[0] - protein.width) // 2, (size[1] - protein.height) // 2))
	return frame


#============================================
def main() -> None:
	"""Encode two fixed-aspect loops and their posters, then refresh the managed gallery."""
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
	with tempfile.TemporaryDirectory(prefix="protein_readme_") as temporary:
		work = pathlib.Path(temporary)
		for example, animation, size, crop in (
			("groel_rotation_oxillustrate", "groel_rotation_demo", (640, 360), None),
			("hexokinase_closure", "hexokinase_closure_loop", (360, 780), (165, 50, 510, 580)),
		):
			directory = ROOT / "output" / example / "frames"
			sources = [directory / f"frame_{index:03d}.png" for index in range(125)]
			# Validate every frame, including those omitted from the smaller preview.
			frames = []
			for index, source in enumerate(sources):
				frame = framed_image(source, size, crop)
				if index in indices:
					frames.append(frame)
			poster = animation.rsplit("_", 1)[0] + "_poster.webp"
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
	if readme.read_text() != updated_readme:
		readme.write_text(updated_readme)
	print(f"Captured {datetime.datetime.now(datetime.UTC).isoformat()}")


if __name__ == "__main__":
	main()
