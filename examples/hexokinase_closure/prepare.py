"""Run inside ChimeraX: prepare matched endpoints and an illustrative loop."""

import json
import pathlib

import numpy
from chimerax.atomic import AtomicStructure, Atoms
from chimerax.core.commands import run
from chimerax.std_commands.align import align


def atom_key(atom: object) -> tuple:
	residue = atom.residue
	return (residue.chain_id, residue.number, residue.insertion_code, residue.name, atom.name)


def main(session: object) -> None:
	out = pathlib.Path('output/hexokinase_closure')
	out.mkdir(parents=True, exist_ok=True)
	run(session, 'open output/inputs/3o80.cif')
	run(session, 'open output/inputs/3o8m.cif')
	opened, closed = session.models.list(type=AtomicStructure)
	if opened.chains[0].characters != closed.chains[0].characters:
		raise ValueError('Endpoint sequences differ')
	# Save the experimentally occupied alpha glucose before removing unmatched ligands.
	run(session, 'select #2/A:486')
	run(session, f'save {out}/glucose.cif models #2 selectedOnly true')
	run(session, 'select clear')
	record = {'method': 'ChimeraX internal-coordinate morph; illustrative, not kinetics',
		'glucose': '3O8M A:486 GLC alt A, occupancy 0.78; fixed in stable-region coordinates'}
	maps = []
	for structure in (opened, closed):
		protein = [a for a in structure.atoms if a.residue.polymer_type == a.residue.PT_AMINO]
		maps.append({atom_key(a): a for a in protein})
	common = set(maps[0]) & set(maps[1])
	if len(common) < 3000:
		raise ValueError('Unexpectedly few corresponding atoms')
	record['omitted_protein_atoms'] = [sorted(set(m) - common) for m in maps]
	for structure in (opened, closed):
		Atoms([a for a in structure.atoms if atom_key(a) not in common]).delete()
		run(session, f'altlocs clean #{structure.id_string}')
	# This contiguous part of the large lobe has a measurable stable fit.
	fit = align(session, closed.atoms.filter((closed.atoms.names == 'CA') &
		(closed.atoms.residues.numbers >= 250) & (closed.atoms.residues.numbers <= 450)),
		to_atoms=opened.atoms.filter((opened.atoms.names == 'CA') &
		(opened.atoms.residues.numbers >= 250) & (opened.atoms.residues.numbers <= 450)),
		move='structure atoms')
	record['alignment'] = {'chain': 'A', 'residues': '250-450 CA', 'rmsd_angstrom': fit[2]}
	# Apply exactly the same registration to glucose; it never follows a binding path.
	run(session, f'open {out}/glucose.cif')
	glucose = session.models.list(type=AtomicStructure)[-1]
	glucose.atoms.coords = fit[4] * glucose.atoms.coords
	run(session, f'save {out}/glucose.cif models #{glucose.id_string}')
	run(session, f'close #{glucose.id_string}')
	for structure, name in ((opened, 'open'), (closed, 'closed')):
		run(session, f'save {out}/{name}.cif models #{structure.id_string}')
	run(session, 'morph #1,2 frames 62 rate sinusoidal same true play false')
	forward = session.models.list(type=AtomicStructure)[-1]
	run(session, 'morph #2,1 frames 63 rate sinusoidal same true play false')
	backward = session.models.list(type=AtomicStructure)[-1]
	# Morph may discard disconnected side-chain atoms differently from each endpoint.
	paired = set(atom_key(a) for a in forward.atoms) & set(atom_key(a) for a in backward.atoms)
	for trajectory in (forward, backward):
		Atoms([a for a in trajectory.atoms if atom_key(a) not in paired]).delete()
	backward_indices = {atom_key(a): i for i, a in enumerate(backward.atoms)}
	order = [backward_indices[atom_key(a)] for a in forward.atoms]
	frames = []
	for trajectory, ids in ((forward, forward.coordset_ids),
		(backward, backward.coordset_ids[1:-1])):
		align(session, trajectory.atoms.filter((trajectory.atoms.names == 'CA') &
			(trajectory.atoms.residues.numbers >= 250) &
			(trajectory.atoms.residues.numbers <= 450)),
			to_atoms=opened.atoms.filter((opened.atoms.names == 'CA') &
			(opened.atoms.residues.numbers >= 250) & (opened.atoms.residues.numbers <= 450)),
			each='coordset', log_info=False)
		for coordset_id in ids:
			trajectory.active_coordset_id = coordset_id
			coords = trajectory.atoms.coords.copy()
			frames.append(coords[order] if trajectory is backward else coords)
	forward.remove_coordsets()
	forward.add_coordsets(numpy.array(frames), replace=True)
	if forward.num_coordsets != 125:
		raise ValueError('Expected 125 unique loop samples')
	forward.active_coordset_id = forward.coordset_ids[0]
	# Preserve the in-memory coordinates as independent handoff evidence.
	numpy.save(out / 'coordinates.npy', numpy.array(frames))
	# ChimeraX 1.10.1 mmCIF allCoordsets repeats the active frame; PDB preserves motion.
	run(session, f'save {out}/protein_loop.pdb models #{forward.id_string} allCoordsets true')
	run(session, f'save {out}/prepared.cxs')
	record['atoms_per_frame'] = forward.num_atoms
	record['frames'] = forward.num_coordsets
	record['atom_keys'] = [atom_key(a) for a in forward.atoms]
	(out / 'preparation.json').write_text(json.dumps(record, indent=2) + '\n')
	run(session, 'exit')


if 'session' in globals():
	main(globals()['session'])
