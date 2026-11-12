#!/usr/bin/env python3
"""Select one isoprene synthase chain and face its ligand toward the camera."""

import pathlib

import numpy
import Bio.PDB


class Chosen(Bio.PDB.Select):
	"""Keep chain A, its substrate analog and magnesium, and resolved alt A atoms."""

	def accept_chain(self, chain: object) -> bool:
		return chain.id == 'A'

	def accept_residue(self, residue: object) -> bool:
		return residue.resname != 'HOH'

	def accept_atom(self, atom: object) -> bool:
		return atom.altloc in (' ', 'A')


def main() -> None:
	structure = Bio.PDB.MMCIFParser(QUIET=True).get_structure('3n0g', 'output/inputs/3n0g.cif')
	chain = structure[0]['A']
	protein = numpy.array([a.coord for r in chain if r.id[0] == ' ' for a in r])
	ligand = numpy.array([a.coord for r in chain if r.resname == 'DST' for a in r])
	center = protein.mean(axis=0)
	z_axis = ligand.mean(axis=0) - center
	z_axis /= numpy.linalg.norm(z_axis)
	x_axis = numpy.cross([0, 1, 0], z_axis)
	x_axis /= numpy.linalg.norm(x_axis)
	y_axis = numpy.cross(z_axis, x_axis)
	rotation = numpy.array([x_axis, y_axis, z_axis]).T
	for residue in structure.get_residues():
		for atom in residue.get_unpacked_list():
			atom.coord = (atom.coord - center) @ rotation
	out = pathlib.Path('output/appearance_3n0g')
	out.mkdir(parents=True, exist_ok=True)
	for writer, extension in ((Bio.PDB.PDBIO(), 'pdb'), (Bio.PDB.MMCIFIO(), 'cif')):
		writer.set_structure(structure)
		writer.save(str(out / f'selected.{extension}'), Chosen())


if __name__ == '__main__':
	main()
