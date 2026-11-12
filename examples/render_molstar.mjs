#!/usr/bin/env node
// Native Mol* experiments shared by the three documented examples.
import fs from 'node:fs/promises';
import path from 'node:path';
import { chromium } from 'playwright';

const example = process.argv[2];
if (!['appearance_3n0g', 'hexokinase_closure', 'groel_rotation'].includes(example)) {
	throw new Error('Choose appearance_3n0g, hexokinase_closure, or groel_rotation');
}
const output = path.resolve('output', example);
await fs.mkdir(path.join(output, 'frames'), { recursive: true });
const input = example === 'appearance_3n0g' ? `${output}/selected.cif`
	: example === 'hexokinase_closure' ? `${output}/protein_loop.cif`
		: 'output/inputs/1oel_assembly1.cif';
const coordinates = await fs.readFile(input, 'utf8');
const ligand = example === 'hexokinase_closure'
	? await fs.readFile(`${output}/glucose.cif`, 'utf8') : null;
const browser = await chromium.launch({ headless: true });
try {
	const page = await browser.newPage({ viewport: { width: 640, height: 640 } });
	page.on('pageerror', error => console.error(error));
	await page.setContent('<div id="viewer" style="position:absolute;inset:0"></div>');
	await page.addStyleTag({ path: 'node_modules/molstar/build/viewer/molstar.css' });
	await page.addScriptTag({ path: 'node_modules/molstar/build/viewer/molstar.js' });
	const initial = await page.evaluate(async ({ coordinates, ligand, example }) => {
		const viewer = await molstar.Viewer.create('viewer', {
			layoutIsExpanded: false, layoutShowControls: false, layoutShowSequence: false,
			layoutShowLog: false, layoutShowLeftPanel: false, viewportShowExpand: false,
			viewportShowControls: false, viewportShowSelectionMode: false,
			viewportShowAnimation: false,
		});
		const plugin = viewer.plugin;
		window.plugin = plugin;
		const data = await plugin.builders.data.rawData({ data: coordinates, label: example });
		const trajectory = await plugin.builders.structure.parseTrajectory(data, 'mmcif');
		const model = await plugin.builders.structure.createModel(trajectory);
		const structure = await plugin.builders.structure.createStructure(model, {
			type: { name: 'model', params: {} },
		});
		const protein = await plugin.builders.structure.tryCreateComponentStatic(structure, 'polymer');
		const surface = example === 'hexokinase_closure';
		await plugin.builders.structure.representation.addRepresentation(protein, {
			type: surface ? 'molecular-surface' : 'spacefill',
			typeParams: { alpha: surface ? 0.42 : 1, resolution: 1, quality: 'custom' },
			color: 'illustrative',
			colorParams: { style: { name: example === 'groel_rotation' ? 'chain-id' : 'uniform',
				params: { value: 0x82b3d4 } }, carbonLightness: 0.4 },
		});
		const ligandStructure = ligand
			? await plugin.builders.structure.createStructure(await plugin.builders.structure.createModel(
				await plugin.builders.structure.parseTrajectory(
					await plugin.builders.data.rawData({ data: ligand, label: 'Fixed bound glucose' }), 'mmcif')))
			: structure;
		const ligands = await plugin.builders.structure.tryCreateComponentStatic(ligandStructure, 'non-standard');
		if (ligands) {
			await plugin.builders.structure.representation.addRepresentation(ligands, {
				type: 'spacefill', color: 'uniform', colorParams: { value: 0xe84393 },
			});
		}
		plugin.canvas3d.setProps({
			camera: { mode: 'orthographic', manualReset: true },
			renderer: { backgroundColor: 0xffffff, ambientIntensity: 0.7, light: [] },
			postprocessing: {
				outline: { name: 'on', params: { ...plugin.canvas3d.props.postprocessing.outline.params,
					scale: 1, threshold: 0.33, color: 0x20252b, includeTransparent: false } },
				occlusion: { name: 'on', params: { ...plugin.canvas3d.props.postprocessing.occlusion.params,
					samples: 32, radius: 5, bias: 0.8, blurKernelSize: 15, resolutionScale: 1 } },
			},
		});
		const sphere = structure.obj.data.boundary.sphere;
		const center = Array.from(sphere.center);
		const radius = sphere.radius * 1.15;
		const camera = { mode: 'orthographic', target: center,
			position: [center[0], center[1], center[2] + radius * 2.8], up: [0, 1, 0],
			radius, radiusMax: radius, fog: 0 };
		plugin.canvas3d.camera.setState(camera, 0);
		window.model = model;
		window.baseCamera = camera;
		window.frameCount = trajectory.obj.data.frameCount;
		window.shot = plugin.helpers.viewportScreenshot;
		window.shot.values = { ...window.shot.values,
			resolution: { name: 'custom', params: { width: 640, height: 640 } },
			transparent: false, axes: { name: 'off', params: {} },
		};
		return { atoms: structure.obj.data.elementCount, frames: window.frameCount, camera,
			chains: structure.obj.data.units.map(u => u.model.atomicHierarchy.chains.auth_asym_id.value(
				u.model.atomicHierarchy.chainAtomSegments.index[u.elements[0]])) };
	}, { coordinates, ligand, example });
	console.log(initial);
	const count = example === 'appearance_3n0g' ? 8 : 125;
	if (example === 'hexokinase_closure' && initial.frames !== count) throw new Error('Lost trajectory frames');
	for (let i = 0; i < count; i++) {
		const uri = await page.evaluate(async ({ i, count, example }) => {
			const p = window.plugin;
			if (example === 'hexokinase_closure') {
				await p.state.data.build().to(window.model).update({ modelIndex: i }).commit();
			} else {
				const angle = 2 * Math.PI * i / count;
				const c = window.baseCamera;
				const distance = c.position[2] - c.target[2];
				p.canvas3d.camera.setState({ ...c, position: [c.target[0] + distance * Math.sin(angle),
					c.target[1], c.target[2] + distance * Math.cos(angle)] }, 0);
			}
			return window.shot.getImageDataUri();
		}, { i, count, example });
		await fs.writeFile(`${output}/frames/frame_${String(i).padStart(3, '0')}.png`,
			Buffer.from(uri.split(',')[1], 'base64'));
		if (i % 25 === 0) console.log(`Rendered ${i + 1}/${count}`);
	}
	const snapshot = await page.evaluate(() => window.plugin.state.getSnapshot());
	await fs.writeFile(`${output}/scene.molj`, JSON.stringify(snapshot));
	await fs.writeFile(`${output}/render.json`, JSON.stringify({ ...initial, renderedFrames: count,
		browser: browser.version(), dimensions: [640, 640] }, null, 2));
} finally {
	await browser.close();
}
