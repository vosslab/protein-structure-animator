#!/usr/bin/env node
// Native Mol* experiments shared by the three documented examples.
import fs from "node:fs/promises";
import path from "node:path";
import { chromium } from "playwright";

const example = process.argv[2];
if (!["appearance_3n0g", "hexokinase_closure", "groel_rotation"].includes(example)) {
  throw new Error("Choose appearance_3n0g, hexokinase_closure, or groel_rotation");
}
const alpha = process.argv[3] === "--alpha";
if (process.argv.length > 4 || (process.argv[3] && !alpha)) {
  throw new Error("The only optional argument is --alpha");
}
if (alpha && example !== "hexokinase_closure") {
  throw new Error("--alpha is available for hexokinase_closure");
}
const source = path.resolve("output", example);
const output = alpha ? `${source}_alpha` : source;
const started = Date.now();
await fs.mkdir(path.join(output, "frames"), { recursive: true });
const input =
  example === "appearance_3n0g"
    ? `${source}/selected.cif`
    : example === "hexokinase_closure"
      ? `${source}/protein_loop.pdb`
      : "output/inputs/1oel_assembly1.cif";
const coordinates = await fs.readFile(input, "utf8");
const ligand =
  example === "hexokinase_closure" ? await fs.readFile(`${source}/glucose.cif`, "utf8") : null;
const browser = await chromium.launch({ headless: true });
try {
  const page = await browser.newPage({ viewport: { width: 640, height: 640 } });
  page.on("pageerror", (error) => console.error(error));
  await page.setContent('<div id="viewer" style="position:absolute;inset:0"></div>');
  await page.addStyleTag({ path: "node_modules/molstar/build/viewer/molstar.css" });
  await page.addScriptTag({ path: "node_modules/molstar/build/viewer/molstar.js" });
  const initial = await page.evaluate(
    async ({ coordinates, ligand, example, alpha }) => {
      const viewer = await molstar.Viewer.create("viewer", {
        layoutIsExpanded: false,
        layoutShowControls: false,
        layoutShowSequence: false,
        layoutShowLog: false,
        layoutShowLeftPanel: false,
        viewportShowExpand: false,
        viewportShowControls: false,
        viewportShowSelectionMode: false,
        viewportShowAnimation: false,
      });
      const plugin = viewer.plugin;
      window.plugin = plugin;
      const data = await plugin.builders.data.rawData({ data: coordinates, label: example });
      const trajectory = await plugin.builders.structure.parseTrajectory(
        data,
        example === "hexokinase_closure" ? "pdb" : "mmcif",
      );
      const model = await plugin.builders.structure.createModel(trajectory);
      const structure = await plugin.builders.structure.createStructure(model, {
        type: { name: "model", params: {} },
      });
      const protein = await plugin.builders.structure.tryCreateComponentStatic(
        structure,
        "polymer",
      );
      const surface = example === "hexokinase_closure";
      window.proteinRepresentation =
        await plugin.builders.structure.representation.addRepresentation(protein, {
          type: surface ? "molecular-surface" : "spacefill",
          typeParams: {
            alpha: surface ? 0.75 : 1,
            resolution: 1,
            quality: "custom",
            ignoreLight: true,
          },
          color: "illustrative",
          colorParams: {
            style: {
              name: example === "groel_rotation" ? "chain-id" : "uniform",
              params: { value: 0x82b3d4 },
            },
            carbonLightness: 0.4,
          },
        });
      window.proteinComponent = protein;
      const ligandStructure = ligand
        ? await plugin.builders.structure.createStructure(
            await plugin.builders.structure.createModel(
              await plugin.builders.structure.parseTrajectory(
                await plugin.builders.data.rawData({ data: ligand, label: "Fixed bound glucose" }),
                "mmcif",
              ),
            ),
          )
        : structure;
      const ligands = await plugin.builders.structure.tryCreateComponentStatic(
        ligandStructure,
        ligand ? "all" : "ligand",
      );
      window.ligandStructure = ligandStructure;
      if (ligands) {
        await plugin.builders.structure.representation.addRepresentation(ligands, {
          type: "spacefill",
          color: "uniform",
          colorParams: { value: 0xe84393 },
        });
      }
      if (example === "appearance_3n0g") {
        const ions = await plugin.builders.structure.tryCreateComponentStatic(structure, "ion");
        await plugin.builders.structure.representation.addRepresentation(ions, {
          type: "spacefill",
          color: "uniform",
          colorParams: { value: 0x4fc47a },
        });
      }
      plugin.canvas3d.setProps({
        camera: { mode: "orthographic", manualReset: true },
        renderer: { backgroundColor: 0xffffff, ambientIntensity: 0.7, light: [] },
        postprocessing: {
          outline: {
            name: "on",
            params: {
              ...plugin.canvas3d.props.postprocessing.outline.params,
              scale: 1,
              threshold: 0.33,
              color: 0x20252b,
              includeTransparent: false,
            },
          },
          occlusion: {
            name: "on",
            params: {
              ...plugin.canvas3d.props.postprocessing.occlusion.params,
              samples: 32,
              radius: 5,
              bias: 0.8,
              blurKernelSize: 15,
              resolutionScale: 1,
            },
          },
        },
      });
      const sphere = structure.obj.data.boundary.sphere;
      const center = Array.from(sphere.center);
      const radius = sphere.radius * 1.15;
      const camera = {
        mode: "orthographic",
        target: center,
        position: [center[0], center[1], center[2] + radius * 2.8],
        up: [0, 1, 0],
        radius,
        radiusMax: radius,
        fog: 0,
      };
      plugin.canvas3d.camera.setState(camera, 0);
      window.model = model;
      window.baseCamera = camera;
      window.frameCount = trajectory.obj.data.frameCount;
      window.shot = plugin.helpers.viewportScreenshot;
      window.shot.behaviors.values.next({
        ...window.shot.values,
        resolution: { name: "custom", params: { width: 640, height: 640 } },
        transparent: alpha,
        axes: { name: "off", params: {} },
      });
      // FXAA and occlusion retain readable contours without 16 repeated renders per frame.
      window.shot.imagePass.setProps({ multiSample: { mode: "off" } });
      return {
        atoms: structure.obj.data.elementCount,
        proteinAtoms: protein.obj.data.elementCount,
        ligandAtoms: ligands ? ligands.obj.data.elementCount : 0,
        frames: window.frameCount,
        camera,
        chains: structure.obj.data.units.map((u) =>
          u.model.atomicHierarchy.chains.auth_asym_id.value(
            u.model.atomicHierarchy.chainAtomSegments.index[u.elements[0]],
          ),
        ),
      };
    },
    { coordinates, ligand, example, alpha },
  );
  console.log(initial);
  if (
    example === "groel_rotation" &&
    (new Set(initial.chains).size !== 14 || initial.proteinAtoms !== 53858)
  ) {
    throw new Error("Expected the complete 14-chain GroEL biological assembly");
  }
  if (example === "hexokinase_closure" && initial.ligandAtoms !== 12)
    throw new Error("Lost glucose");
  const count = example === "appearance_3n0g" ? 8 : 125;
  if (example === "hexokinase_closure" && initial.frames !== count)
    throw new Error("Lost trajectory frames");
  const importedCoordinates = {};
  if (example === "hexokinase_closure" || example === "groel_rotation") {
    Object.assign(
      importedCoordinates,
      await page.evaluate((example) => {
        function atomKeys(model) {
          const h = model.atomicHierarchy;
          return Array.from({ length: h.atoms._rowCount }, (_, i) => {
            const residue = h.residueAtomSegments.index[i];
            const chain = h.chainAtomSegments.index[i];
            return [
              h.chains.auth_asym_id.value(chain),
              h.residues.auth_seq_id.value(residue),
              h.residues.pdbx_PDB_ins_code.value(residue),
              h.atoms.auth_comp_id.value(i),
              h.atoms.auth_atom_id.value(i),
            ];
          });
        }
        const result = { atom_keys: atomKeys(window.model.obj.data) };
        if (example === "hexokinase_closure") {
          const ligandModel = window.ligandStructure.obj.data.models[0];
          const c = ligandModel.atomicConformation;
          result.ligand = {
            atom_keys: atomKeys(ligandModel),
            coordinates: [Array.from(c.x), Array.from(c.y), Array.from(c.z)],
          };
        }
        return result;
      }, example),
    );
  }
  for (let i = 0; i < count; i++) {
    const uri = await page.evaluate(
      async ({ i, count, example }) => {
        const p = window.plugin;
        if (example === "hexokinase_closure") {
          await p.state.data.build().to(window.model).update({ modelIndex: i }).commit();
        } else {
          const angle = (2 * Math.PI * i) / count;
          const c = window.baseCamera;
          const distance = c.position[2] - c.target[2];
          p.canvas3d.camera.setState(
            {
              ...c,
              position: [
                c.target[0] + distance * Math.sin(angle),
                c.target[1],
                c.target[2] + distance * Math.cos(angle),
              ],
            },
            0,
          );
        }
        p.canvas3d.commit(true);
        return window.shot.getImageDataUri();
      },
      { i, count, example },
    );
    await fs.writeFile(
      `${output}/frames/frame_${String(i).padStart(3, "0")}.png`,
      Buffer.from(uri.split(",")[1], "base64"),
    );
    if ([0, 31, 62, 93, 124].includes(i)) {
      importedCoordinates[i] = await page.evaluate(() => {
        const c = window.model.obj.data.atomicConformation;
        return [Array.from(c.x), Array.from(c.y), Array.from(c.z)];
      });
    }
    if (i % 25 === 0) console.log(`Rendered ${i + 1}/${count}`);
  }
  await page.evaluate(async (example) => {
    if (example === "hexokinase_closure") {
      await window.plugin.state.data.build().to(window.model).update({ modelIndex: 0 }).commit();
    }
    window.plugin.canvas3d.camera.setState(window.baseCamera, 0);
  }, example);
  const snapshot = await page.evaluate(() => window.plugin.state.getSnapshot());
  await fs.writeFile(`${output}/scene.molj`, JSON.stringify(snapshot));
  if (example === "appearance_3n0g") {
    const uri = await page.evaluate(async () => {
      const p = window.plugin;
      await p.state.data.build().delete(window.proteinRepresentation.ref).commit();
      await p.builders.structure.representation.addRepresentation(window.proteinComponent, {
        type: "molecular-surface",
        typeParams: { resolution: 1, ignoreLight: true },
        color: "uniform",
        colorParams: { value: 0x82b3d4 },
      });
      p.canvas3d.commit(true);
      return window.shot.getImageDataUri();
    });
    await fs.writeFile(`${output}/surface.png`, Buffer.from(uri.split(",")[1], "base64"));
    await fs.writeFile(
      `${output}/surface.molj`,
      JSON.stringify(await page.evaluate(() => window.plugin.state.getSnapshot())),
    );
  }
  await fs.writeFile(`${output}/imported_coordinates.json`, JSON.stringify(importedCoordinates));
  await fs.writeFile(
    `${output}/render.json`,
    JSON.stringify(
      {
        ...initial,
        renderedFrames: count,
        browser: browser.version(),
        dimensions: [640, 640],
        transparentBackground: alpha,
        elapsedSeconds: (Date.now() - started) / 1000,
      },
      null,
      2,
    ),
  );
} finally {
  await browser.close();
}
