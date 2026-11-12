#!/usr/bin/env python3
"""Render a rigid full-turn GroEL view with the native oxillustrate CLI."""

# Standard Library
import os
import json
import time
import pathlib
import argparse
import hashlib
import subprocess
import collections

# PIP3 modules
import numpy
import Bio.PDB.MMCIF2Dict


#============================================
def rotated(point: numpy.ndarray, orientation: list[float]) -> numpy.ndarray:
	"""Apply the native positive-angle column rotations, Z then Y then X."""
	x, y, z = point
	for axis in (2, 1, 0):
		sine, cosine = numpy.sin(numpy.radians(orientation[axis])), numpy.cos(
			numpy.radians(orientation[axis]))
		if axis == 2:
			x, y = cosine * x - sine * y, sine * x + cosine * y
		elif axis == 1:
			x, z = cosine * x + sine * z, -sine * x + cosine * z
		else:
			y, z = cosine * y - sine * z, sine * y + cosine * z
	result = numpy.array([x, y, z])
	return result


#============================================
def fixed_framing(coordinates: numpy.ndarray) -> tuple[numpy.ndarray, float, float]:
	"""Bound every rotation by one sphere, including the largest native atom radius."""
	origin = (coordinates.min(axis=0) + coordinates.max(axis=0)) / 2
	radius = float(numpy.linalg.norm(coordinates - origin, axis=1).max()) + 1.8
	# Thirty pixels leave room for native outlines; positive z surfaces are clipped.
	scale = (640 / 2 - 30) / radius
	depth = radius + 1
	return origin, scale, depth


#============================================
def input_coordinates(filename: pathlib.Path) -> tuple[numpy.ndarray, dict]:
	"""Check this deposited assembly, without interpreting assembly operators again."""
	data = Bio.PDB.MMCIF2Dict.MMCIF2Dict(str(filename))
	groups = data['_atom_site.group_PDB']
	keep = [i for i, group in enumerate(groups) if group == 'ATOM']
	chains = collections.Counter(data['_atom_site.auth_asym_id'][i] for i in keep)
	expected = {chain: 3847 for base in 'ABCDEFG' for chain in (base, f'{base}-2')}
	if dict(chains) != expected or len(keep) != 53858:
		raise ValueError(f'Expected complete fourteen-chain GroEL assembly: {chains}')
	omitted = [data['_atom_site.label_comp_id'][i]
		for i, group in enumerate(groups) if group != 'ATOM']
	if collections.Counter(omitted) != {'HOH': 298}:
		raise ValueError('Expected only the 298 deposited waters outside the protein')
	if {data['_atom_site.label_alt_id'][i] for i in keep} != {'.'}:
		raise ValueError('Unexpected alternate conformers; inspect native selection before rendering')
	coordinates = numpy.array([[float(data[f'_atom_site.Cartn_{axis}'][i])
		for axis in 'xyz'] for i in keep])
	if not numpy.isfinite(coordinates).all():
		raise ValueError('Non-finite input coordinates')
	counts = {'protein_atoms': len(keep), 'chains': dict(chains), 'omitted_waters': 298}
	return coordinates, counts


#============================================
def sha256(filename: pathlib.Path) -> str:
	"""Identify the actual input, executable and retained scene."""
	digest = hashlib.sha256(filename.read_bytes()).hexdigest()
	return digest


#============================================
def main() -> None:
	parser = argparse.ArgumentParser(description=__doc__)
	root = pathlib.Path(subprocess.check_output(['git', 'rev-parse', '--show-toplevel'],
		cwd=pathlib.Path(__file__).resolve().parent, text=True).strip())
	parser.add_argument('-i', '--illustrate', type=pathlib.Path,
		default=root.parent / 'goodsell-oxillustrate-rs/target/release/illustrate')
	args = parser.parse_args()
	binary = args.illustrate.resolve()
	if not binary.is_file() or not os.access(binary, os.X_OK):
		parser.error(f'Build the native executable with cargo build --release: {binary}')
	source = root / 'output/inputs/1oel_assembly1.cif'
	if not source.is_file():
		parser.error('Run bash examples/download_inputs.sh before rendering')
	coordinates, counts = input_coordinates(source)
	input_hash, binary_hash = sha256(source), sha256(binary)
	origin, scale, depth = fixed_framing(coordinates)
	template_path = pathlib.Path(__file__).with_name('oxillustrate.json')
	template = json.loads(template_path.read_text())
	# ASVS 5.3.2: all generated names are fixed, repository-owned output paths.
	output = root / 'output/groel_rotation_oxillustrate'
	frames, scenes = output / 'frames', output / 'scenes'
	frames.mkdir(parents=True, exist_ok=True)
	scenes.mkdir(exist_ok=True)
	expected = {f'frame_{i:03d}.png' for i in range(125)}
	if any(path.name not in expected for path in frames.glob('frame_*.png')):
		raise ValueError('Stale extra PNG frames: inspect the dedicated frames directory')
	started = time.monotonic()
	with (output / 'illustrate.log').open('w') as log:
		for index in range(125):
			scene = dict(template)
			orientation = list(template['orientation'])
			# Native x is the vertical raster axis; rotate about that fixed view axis.
			orientation[0] += 360 * index / 125
			scene['orientation'] = orientation
			center = rotated(origin, orientation) + numpy.array([0, 0, depth])
			scene['framing'] = {'center': center.tolist(), 'scale': scale, 'margin': 30}
			scene_path = scenes / f'frame_{index:03d}.json'
			scene_path.write_text(json.dumps(scene, indent=2) + '\n')
			# ASVS 1.2.5: native command and paths are separate argv entries, never shell text.
			subprocess.run([str(binary), str(source), '--scene', str(scene_path),
				'--output', str(frames / f'frame_{index:03d}.png')],
				check=True, stdout=log, stderr=log)
			print(f'Rendered {index + 1}/125', flush=True)
	if sha256(source) != input_hash or sha256(binary) != binary_hash:
		raise ValueError('Input or renderer changed during rendering; repeat with stable files')
	metadata = {'input': str(source.relative_to(root)), 'input_sha256': input_hash,
		'executable': str(binary), 'executable_sha256': binary_hash,
		'version': subprocess.check_output([str(binary), '--version'], text=True).strip(),
		'template_sha256': sha256(template_path), 'counts': counts, 'frames': 125,
		'fps': 25, 'seconds': 5, 'dimensions': [640, 640],
		'motion': 'rigid viewpoint rotation; no conformational change or measured kinetics',
		'origin_angstrom': origin.tolist(), 'scale_pixels_per_angstrom': scale,
		'depth_angstrom': depth, 'wall_seconds': time.monotonic() - started}
	(output / 'render.json').write_text(json.dumps(metadata, indent=2) + '\n')


if __name__ == '__main__':
	main()
