#!/usr/bin/env python3
"""Stage the 8DBU rotor against a fixed, explicitly cut away stationary housing."""

# Standard Library
import os
import json
import time
import shutil
import pathlib
import argparse
import hashlib
import subprocess

# PIP3 modules
import numpy
import PIL.Image
import PIL.ImageDraw
import PIL.ImageFont
import Bio.PDB
import Bio.PDB.MMCIF2Dict


FRAME_COUNT = 125
ROTOR_CHAINS = set('GHIJKLMNOPQR')
ORIGIN = numpy.array([226.7205553485988, 238.32514475393032, 210.932603417635])
BASIS = numpy.array([
	[-0.5155561935798797, 0.6846836845224478, -0.5151796418825093],
	[0.5376905864405176, -0.20961773225451916, -0.8166696024572757],
	[-0.6671511406830374, -0.6980463154212888, -0.26007825170914306],
])
INPUT_HASH = 'f9eff1ab7ae60a201fd23fa8f265bca48b76926ee457b8dde8a5f6cad4ea2f40'


#============================================
def sha256(path: pathlib.Path) -> str:
	"""Identify preserved structural inputs, native sources and rendered artifacts."""
	digest = hashlib.sha256(path.read_bytes()).hexdigest()
	return digest


#============================================
def rotor_frame(local: numpy.ndarray, rotor: numpy.ndarray, index: int) -> numpy.ndarray:
	"""Rotate only the rotor about local +z, without duplicating the endpoint."""
	angle = 2 * numpy.pi * index / FRAME_COUNT
	sine, cosine = numpy.sin(angle), numpy.cos(angle)
	rotation = numpy.array([[cosine, -sine, 0], [sine, cosine, 0], [0, 0, 1]])
	result = local.copy()
	result[rotor] = local[rotor] @ rotation.T
	return result


#============================================
def camera_coordinates(local: numpy.ndarray) -> numpy.ndarray:
	"""Map an eight-degree elevated side view to native row/column/depth axes."""
	sine, cosine = numpy.sin(numpy.radians(8)), numpy.cos(numpy.radians(8))
	x, y, z = local.T
	# Native row-down cross column-right points toward the viewer: keep a proper rotation.
	result = numpy.column_stack((-z * cosine + y * sine, -x, y * cosine + z * sine))
	return result


#============================================
def cutaway_mask(local: numpy.ndarray, rotor: numpy.ndarray) -> numpy.ndarray:
	"""Open a fixed 118-degree front wedge of the stationary housing only."""
	front_wedge = local[:, 1] > 0.6 * numpy.abs(local[:, 0])
	visible = rotor | ~front_wedge
	return visible


#============================================
def write_coordinates(data: dict, coordinates: numpy.ndarray, keep: numpy.ndarray,
	path: pathlib.Path) -> None:
	"""Preserve every deposited atom-site identity field in a prepared mmCIF table."""
	selected = numpy.flatnonzero(keep)
	fields = {key: [values[i] for i in selected] for key, values in data.items()
		if key.startswith('_atom_site.')}
	for column, axis in enumerate('xyz'):
		fields[f'_atom_site.Cartn_{axis}'] = [f'{coordinates[i, column]:.6f}' for i in selected]
	fields['data_'] = '8dbu_rigid_staging'
	writer = Bio.PDB.MMCIFIO()
	writer.set_dict(fields)
	writer.save(str(path))


#============================================
def prepare(root: pathlib.Path, output: pathlib.Path, template: dict) -> dict:
	"""Retain complete moving coordinates, an explicit identity cutaway, and one camera."""
	source = root / 'output/inputs/8dbu_assembly1.cif'
	# ASVS 2.2.1: exact inspected input identity bounds this structure-specific staging.
	if sha256(source) != INPUT_HASH:
		raise ValueError('8DBU assembly input differs from the inspected source hash')
	data = Bio.PDB.MMCIF2Dict.MMCIF2Dict(str(source))
	coordinates = numpy.array([[float(value) for value in data[f'_atom_site.Cartn_{axis}']]
		for axis in 'xyz']).T
	labels = data['_atom_site.label_asym_id']
	rotor = numpy.array([chain in ROTOR_CHAINS for chain in labels])
	if len(coordinates) != 36917 or rotor.sum() != 8772:
		raise ValueError('Expected 36,917 total atoms, including 8,772 complete rotor atoms')
	if not numpy.isfinite(coordinates).all():
		raise ValueError('Non-finite structural input')
	local = (coordinates - ORIGIN) @ BASIS
	visible = cutaway_mask(local, rotor)
	minimum, maximum = numpy.full(3, numpy.inf), numpy.full(3, -numpy.inf)
	for index in range(FRAME_COUNT):
		view = camera_coordinates(rotor_frame(local, rotor, index))
		minimum = numpy.minimum(minimum, view.min(axis=0) - 1.8)
		maximum = numpy.maximum(maximum, view.max(axis=0) + 1.8)
	center = (minimum + maximum) / 2
	center[2] = maximum[2] + 2
	# Reserve lower space for the compact staging caption and membrane label.
	scale = min((template['height'] - 100) / (maximum[0] - minimum[0]),
		(template['width'] - 66) / (maximum[1] - minimum[1]))
	template['framing'] = {'center': center.tolist(), 'scale': float(scale), 'margin': 22}
	identities = []
	for i in range(len(coordinates)):
		identities.append({key: data[f'_atom_site.{key}'][i] for key in
			('id', 'label_asym_id', 'auth_asym_id', 'label_seq_id', 'auth_seq_id',
			'label_comp_id', 'label_atom_id', 'label_alt_id', 'pdbx_PDB_model_num')})
	mask = {'definition': 'stationary atoms omitted where local_y > 0.6 * abs(local_x)',
		'visible_atom_ids': [data['_atom_site.id'][i] for i in numpy.flatnonzero(visible)],
		'omitted_atom_ids': [data['_atom_site.id'][i] for i in numpy.flatnonzero(~visible)],
		'rotor_atom_ids': [data['_atom_site.id'][i] for i in numpy.flatnonzero(rotor)],
		'atom_identities': identities}
	(output / 'identity_mask.json').write_text(json.dumps(mask, indent=2) + '\n')
	for index in range(FRAME_COUNT):
		moved = rotor_frame(local, rotor, index)
		world = moved @ BASIS.T + ORIGIN
		# Keep stationary positions bit-identical before the six-decimal text handoff.
		world[~rotor] = coordinates[~rotor]
		write_coordinates(data, world, numpy.ones(len(rotor), dtype=bool),
			output / 'coordinates' / f'full_{index:03d}.cif')
		write_coordinates(data, camera_coordinates(moved), visible,
			output / 'coordinates' / f'cutaway_{index:03d}.cif')
		(output / 'scenes' / f'frame_{index:03d}.json').write_text(
			json.dumps(template, indent=2) + '\n')
	metadata = {'input': str(source.relative_to(root)), 'input_sha256': INPUT_HASH,
		'original_atoms': len(coordinates), 'rotor_atoms': int(rotor.sum()),
		'stationary_atoms': int((~rotor).sum()), 'visible_atoms': int(visible.sum()),
		'cutaway_omitted_atoms': int((~visible).sum()), 'rotor_label_chains': sorted(ROTOR_CHAINS),
		'axis_origin_angstrom': ORIGIN.tolist(), 'basis_columns_x_y_z': BASIS.tolist(),
		'view_elevation_degrees': 8, 'camera_center': center.tolist(),
		'scale_pixels_per_angstrom': float(scale), 'all_frame_sphere_minimum': minimum.tolist(),
		'all_frame_sphere_maximum': maximum.tolist(), 'dimensions': [480, 720],
		'frames': FRAME_COUNT, 'fps': 25, 'seconds': 5,
		'motion': 'rigid mechanical staging from one experimental structure; frozen housing; '
		'not a sterically validated trajectory, catalytic cycle, pathway or measured kinetics'}
	(output / 'preparation.json').write_text(json.dumps(metadata, indent=2) + '\n')
	return metadata


#============================================
def overlay(protein: PIL.Image.Image, metadata: dict) -> PIL.Image.Image:
	"""Add an illustrative membrane and sparse labels without altering protein pixels."""
	canvas = PIL.Image.new('RGBA', protein.size)
	draw = PIL.ImageDraw.Draw(canvas)
	center = numpy.array(metadata['camera_center'])
	scale = metadata['scale_pixels_per_angstrom']
	# The membrane band is context centered on the deposited c-ring, not modeled lipids.
	upper = int((camera_coordinates(numpy.array([[0, 0, 22]]))[0, 0] - center[0]) * scale + 360)
	lower = int((camera_coordinates(numpy.array([[0, 0, -22]]))[0, 0] - center[0]) * scale + 360)
	draw.rounded_rectangle((20, upper, 460, lower), radius=10, fill=(101, 132, 157, 38),
		outline=(101, 132, 157, 140), width=2)
	canvas.alpha_composite(protein)
	draw = PIL.ImageDraw.Draw(canvas)
	font_path = '/System/Library/Fonts/Supplemental/Arial Bold.ttf'
	font = PIL.ImageFont.truetype(font_path, 16)
	caption_font = PIL.ImageFont.truetype(font_path, 13)
	for text, position in (('STATOR CUTAWAY', (24, 28)), ('ROTOR', (25, 420)),
		('MEMBRANE', (27, lower + 12))):
		x, y = position
		bounds = draw.textbbox(position, text, font=font)
		draw.rounded_rectangle((bounds[0] - 5, bounds[1] - 4, bounds[2] + 5, bounds[3] + 4),
			radius=4, fill=(246, 248, 251, 242))
		draw.text((x, y), text, font=font, fill=(37, 52, 71, 255))
	draw.line((94, 432, 178, 432, 213, 406), fill=(144, 89, 30, 255), width=2)
	draw.text((24, 696), 'Rigid mechanical staging | 8DBU', font=caption_font,
		fill=(68, 82, 101, 255), stroke_width=2, stroke_fill=(246, 248, 251, 230))
	return canvas


#============================================
def render(output: pathlib.Path, binary: pathlib.Path, indices: list[int]) -> None:
	"""Restore the native trimmed PNG at its exact sidecar origin, without resampling."""
	metadata = json.loads((output / 'preparation.json').read_text())
	with (output / 'illustrate.log').open('a') as log:
		for index in indices:
			native = output / 'native' / f'frame_{index:03d}.png'
			sidecar = native.with_suffix('.json')
			# ASVS 1.2.5: pass native arguments separately, without a shell interpreter.
			subprocess.run([str(binary), str(output / 'coordinates' / f'cutaway_{index:03d}.cif'),
				'--scene', str(output / 'scenes' / f'frame_{index:03d}.json'),
				'--output', str(native), '--metadata', str(sidecar)],
				check=True, stdout=log, stderr=log)
			registration = json.loads(sidecar.read_text())
			if registration['canvas'] != metadata['dimensions']:
				raise ValueError('Native sidecar canvas differs from the fixed delivery canvas')
			left, top = registration['crop_origin']
			with PIL.Image.open(native) as image:
				if image.mode != 'RGBA' or left < 0 or top < 0:
					raise ValueError('Native renderer did not supply registered true RGBA')
				if left + image.width > 480 or top + image.height > 720:
					raise ValueError('Native crop exceeds the fixed canvas')
				protein = PIL.Image.new('RGBA', (480, 720))
				protein.paste(image, (left, top))
			protein.save(output / 'protein' / f'frame_{index:03d}.png')
			overlay(protein, metadata).save(output / 'frames' / f'frame_{index:03d}.png')
			print(f'Rendered {index + 1}/{FRAME_COUNT}', flush=True)


#============================================
def provenance(root: pathlib.Path, output: pathlib.Path, binary: pathlib.Path) -> dict:
	"""Snapshot the actual dirty native build inputs as well as executable identity."""
	folder = output / 'provenance'
	folder.mkdir(exist_ok=True)
	native_root = pathlib.Path(subprocess.check_output(['git', '-C', str(binary.parent),
		'rev-parse', '--show-toplevel'], text=True).strip())
	paths = [native_root / 'Cargo.toml', native_root / 'Cargo.lock']
	paths.extend(sorted((native_root / 'src').rglob('*.rs')))
	source_hashes = {}
	for path in paths:
		relative = path.relative_to(native_root)
		destination = folder / 'native_source' / relative
		destination.parent.mkdir(parents=True, exist_ok=True)
		shutil.copyfile(path, destination)
		source_hashes[str(relative)] = sha256(path)
	diff = subprocess.check_output(['git', '-C', str(native_root), 'diff', '--binary'])
	(folder / 'native.diff').write_bytes(diff)
	record = {'executable': str(binary), 'executable_sha256': sha256(binary),
		'version': subprocess.check_output([str(binary), '--version'], text=True).strip(),
		'native_head': subprocess.check_output(['git', '-C', str(native_root), 'rev-parse',
			'HEAD'], text=True).strip(), 'native_source_sha256': source_hashes,
		'helper_sha256': sha256(pathlib.Path(__file__)),
		'template_sha256': sha256(pathlib.Path(__file__).with_name('oxillustrate.json')),
		'repository': str(root)}
	(folder / 'build.json').write_text(json.dumps(record, indent=2) + '\n')
	return record


#============================================
def parse_args() -> argparse.Namespace:
	"""Expose only preparation and bounded visual checkpoints needed by this example."""
	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument('-i', '--illustrate', dest='illustrate', type=pathlib.Path)
	parser.add_argument('-p', '--prepare', dest='prepare', action='store_true',
		help='write all coordinate handoffs and fixed scenes without rendering')
	parser.add_argument('-f', '--frames', dest='frames', type=int, nargs='+',
		help='render selected prepared frame indices; omitted renders all 125')
	args = parser.parse_args()
	return args


#============================================
def main() -> None:
	args = parse_args()
	root = pathlib.Path(subprocess.check_output(['git', 'rev-parse', '--show-toplevel'],
		cwd=pathlib.Path(__file__).resolve().parent, text=True).strip())
	output = root / 'output/atp_synthase_motor'
	# ASVS 5.3.2: generated paths use fixed repository-owned names and bounded indices.
	for name in ('coordinates', 'scenes', 'native', 'protein', 'frames'):
		(output / name).mkdir(parents=True, exist_ok=True)
	if args.prepare:
		template = json.loads(pathlib.Path(__file__).with_name('oxillustrate.json').read_text())
		metadata = prepare(root, output, template)
		print(json.dumps(metadata, indent=2))
		return
	binary = args.illustrate
	if binary is None:
		binary = root.parent / 'goodsell-oxillustrate-rs/target/release/illustrate'
	binary = binary.resolve()
	if not binary.is_file() or not os.access(binary, os.X_OK):
		raise ValueError(f'Build the native executable before rendering: {binary}')
	indices = list(range(FRAME_COUNT)) if args.frames is None else args.frames
	if not indices or any(index < 0 or index >= FRAME_COUNT for index in indices):
		raise ValueError('Frame indices must be in 0..124')
	if not (output / 'preparation.json').is_file():
		raise ValueError('Run with --prepare before rendering')
	if sha256(root / 'output/inputs/8dbu_assembly1.cif') != INPUT_HASH:
		raise ValueError('Original structural input changed after preparation')
	started = time.monotonic()
	record = provenance(root, output, binary)
	render(output, binary, indices)
	if sha256(binary) != record['executable_sha256']:
		raise ValueError('Native executable changed during rendering')
	record['rendered_indices'] = indices
	record['wall_seconds'] = time.monotonic() - started
	(output / 'render.json').write_text(json.dumps(record, indent=2) + '\n')


if __name__ == '__main__':
	main()
