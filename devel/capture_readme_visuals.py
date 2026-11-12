#!/usr/bin/env python3
"""Refresh README proof from rendered examples; run after the example README commands.

Run: source source_me.sh && python3 devel/capture_readme_visuals.py
Requires the declared Pillow dependency with WebP support and cwebp on PATH. Molecular frames are
only cropped to remove white margins or reduced, never enlarged or re-rendered here.
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
import PIL.ImageDraw
import PIL.ImageFont

# ASVS 5.3.2: generated paths are fixed relative to this repository.
ROOT = pathlib.Path(subprocess.run(
	["git", "rev-parse", "--show-toplevel"], cwd=pathlib.Path(__file__).resolve().parent,
	check=True, capture_output=True, text=True,
).stdout.strip())
BEGIN = "<!-- screenshots:begin (managed by screenshot-docs) -->"
END = "<!-- screenshots:end -->"
EMBEDS = (
	"![Mol* hexokinase open and closed endpoints beside the Rust Goodsell fourteen-subunit GroEL]"
	"(docs/screenshots/protein_examples.webp)\n"
	"![Hexokinase closes and reopens around fixed magenta glucose in an interpolated preview]"
	"(docs/screenshots/hexokinase_closure_demo.webp)"
)


#============================================
def label(image: PIL.Image.Image, xy: tuple[int, int], text: str, size: int) -> None:
	"""Draw readable annotation using Pillow's bundled font."""
	PIL.ImageDraw.Draw(image).text(
		xy, text, font=PIL.ImageFont.load_default(size=size), fill="#18374c",
	)


#============================================
def hexokinase(frame_path: pathlib.Path) -> PIL.Image.Image:
	"""Remove only the empty margins surrounding the protein and glucose."""
	with PIL.Image.open(frame_path) as image:
		# shortcut: fixed camera margins; review this crop when the example camera changes.
		return image.convert("RGB").crop((165, 50, 510, 580))


#============================================
def update_readme(text: str) -> str:
	"""Replace exactly the managed interior, preserving the surrounding README."""
	if text.count(BEGIN) != 1 or text.count(END) != 1:
		raise ValueError("README must contain exactly one screenshot sentinel pair.")
	before, remainder = text.split(BEGIN)
	_, after = remainder.split(END)
	return f"{before}{BEGIN}\n{EMBEDS}\n{END}{after}"


#============================================
def main() -> None:
	"""Compose source-frame proof, encode final assets, and refresh managed embeds."""
	readme = ROOT / "README.md"
	updated_readme = update_readme(readme.read_text())
	hex_frames = ROOT / "output/hexokinase_closure/frames"
	groel = ROOT / "output/groel_rotation_oxillustrate/frames/frame_000.png"
	sources = [hex_frames / f"frame_{index:03d}.png" for index in range(125)] + [groel]
	for source in sources:
		if not source.is_file():
			raise FileNotFoundError(
				f"Missing {source.relative_to(ROOT)}; reproduce the example with the commands "
				"in examples/hexokinase_closure/README.md and the canonical Rust commands in "
				"examples/groel_rotation/README.md."
			)
	if shutil.which("cwebp") is None:
		raise RuntimeError("Install cwebp before capturing README visuals.")
	if not PIL.features.check("webp"):
		raise RuntimeError("Install Pillow with WebP support before capturing README visuals.")
	for source in sources:
		with PIL.Image.open(source) as image:
			if image.size != (640, 640):
				raise ValueError(f"Expected a native 640 x 640 example frame: {source}")
	assets = ROOT / "docs/screenshots"
	with tempfile.TemporaryDirectory(prefix="protein_readme_") as temporary:
		work = pathlib.Path(temporary)
		poster = PIL.Image.new("RGB", (1280, 800), "white")
		for index, state in ((0, "open"), (62, "closed")):
			x = 20 if index == 0 else 350
			protein = hexokinase(hex_frames / f"frame_{index:03d}.png")
			protein.thumbnail((310, 560))
			poster.paste(protein, (x, 160))
			label(poster, (x, 105), f"Hexokinase: {state}", 25)
		with PIL.Image.open(groel) as image:
			assembly = image.convert("RGB")
			assembly.thumbnail((600, 600))
			poster.paste(assembly, (680, 125))
		label(poster, (30, 30), "Experimental endpoints and a complete assembly", 33)
		label(poster, (710, 105), "Rust Goodsell: GroEL (14 subunits)", 25)
		label(poster, (30, 720), "Mol* surface; fixed glucose (magenta).", 23)
		label(poster, (30, 755), "Protein motion is interpolated.", 23)
		label(poster, (710, 720), "Assembly coordinates stay fixed.", 23)
		label(poster, (710, 755), "Only the viewpoint rotates.", 23)
		poster.save(work / "poster.png")
		# ASVS 1.2.5: pass command arguments directly, without a shell interpreter.
		subprocess.run([
			"cwebp", "-quiet", "-q", "90", str(work / "poster.png"),
			"-o", str(work / "protein_examples.webp"),
		], check=True)
		# Hold the source endpoints briefly while keeping the full close/reopen sequence.
		indices = [0] * 3 + [round(index * 124 / 53) for index in range(54)] + [124] * 3
		frames = []
		for index in indices:
			frame = PIL.Image.new("RGB", (960, 600), "white")
			protein = hexokinase(hex_frames / f"frame_{index:03d}.png")
			protein.thumbnail((500, 530))
			frame.paste(protein, (545, 35))
			label(frame, (35, 100), "Hexokinase", 36)
			label(frame, (35, 155), "Open > closed > open", 25)
			label(frame, (35, 240), "Experimental endpoints", 22)
			label(frame, (35, 280), "Interpolated protein motion", 22)
			label(frame, (35, 320), "Fixed glucose pose (magenta)", 22)
			label(frame, (35, 360), "Transparent molecular surface", 22)
			label(frame, (35, 500), "One play / 5 seconds", 22)
			frames.append(frame)
		# WebP loop=1 is one play; integer millisecond delays preserve exactly five seconds.
		frames[0].save(
			work / "hexokinase_closure_demo.webp", save_all=True, append_images=frames[1:],
			quality=90, loop=1,
			duration=[round((index + 1) * 1000 / 12) - round(index * 1000 / 12)
				for index in range(len(frames))],
		)
		assets.mkdir(exist_ok=True)
		for name in ("protein_examples.webp", "hexokinase_closure_demo.webp"):
			shutil.copyfile(work / name, assets / name)
	if readme.read_text() != updated_readme:
		readme.write_text(updated_readme)
	print(f"Captured {datetime.datetime.now(datetime.UTC).isoformat()}")
	for directory in (hex_frames, groel.parent):
		selected = [source for source in sources if source.parent == directory]
		# ASVS 11.4.1: source provenance uses a SHA-256 checksum.
		digest = hashlib.sha256(b"".join(source.read_bytes() for source in selected)).hexdigest()
		print(f"Source SHA256 ({len(selected)} frames): {directory.relative_to(ROOT)} {digest}")
	for name in ("protein_examples.webp", "hexokinase_closure_demo.webp"):
		path = assets / name
		print(f"Wrote {path.relative_to(ROOT)} ({path.stat().st_size} bytes)")


if __name__ == "__main__":
	main()
