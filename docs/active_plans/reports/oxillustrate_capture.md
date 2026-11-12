# Rust Goodsell README capture

## Capture and scope

Captured 2026-11-12 at 13:55:48 UTC and repeated at 13:56:00 UTC. The two runs produced
byte-identical README content and both managed assets. This refresh applies the
screenshot-docs visual CLI artifact route: genuine rendered results, without invented UI.
The user preference for animated WebP overrides the skill's GIF recipe for the retained
hexokinase preview. No renderer, structural input, or animation source was changed here.

The first README embed is a static comparison: unchanged Mol* hexokinase open/closed
endpoints on the left and the canonical native Rust Goodsell GroEL frame on the right.
The second embed is the unchanged five-second hexokinase close/reopen preview. The source
animation remains experimental endpoint interpolation around fixed magenta glucose;
GroEL is a fixed fourteen-subunit assembly viewed from a rotating camera. Neither image
establishes a physical transition path or kinetics.

## Assets and provenance

| Managed asset | Dimensions | Encoding | Bytes |
| --- | --- | --- | --- |
| `docs/screenshots/protein_examples.webp` | 1280 x 800 | cwebp quality 90 | 120,158 |
| `docs/screenshots/hexokinase_closure_demo.webp` | 960 x 600 | Pillow quality 90 | 1,228,594 |

Both canvases stay below the 1920 px edge ceiling. The static asset is below one MB;
the motion asset stays below the inherited five-MiB motion budget. Pillow 13.0.0 and
libwebp/cwebp 1.6.0 were observed, with libsharpyuv 0.4.2. No dependencies were installed.
The helper uses temporary PNGs under `/tmp`, encodes the static WebP using `cwebp -q 90`,
and copies only final named assets to the managed folder.

Sources are the existing native 640 x 640 PNGs: 125 frames under
`output/hexokinase_closure/frames/`, plus
`output/groel_rotation_oxillustrate/frames/frame_000.png`. Hexokinase removes only the
existing fixed white margins and reduces the result. GroEL reduces 640 px to 600 px.
No molecular anatomy is enlarged, redrawn, or rendered by the capture helper.

SHA-256 checksums:

```text
hexokinase PNG bytes concatenated in frame_000..frame_124 order:
a0fe37c9b380e94abf2a920f576586f380a02f90e607ab84de90d96d996fc5de
Rust GroEL frame_000.png:
0ece252c5d76e76695d54aea56a17399a4a15726a14c64d449f6c5e9ab1abf83
protein_examples.webp (refreshed):
c7247501c3a865cd784d5263fec7d77d7eae1aee1f59866c011c9a7e5bac66a8
hexokinase_closure_demo.webp (unchanged):
d6a0fd11e0cd2112303526945eec68011aac1e091d2fff3431dcca90d3de4b74
protein_examples.webp (preceding Mol* comparison):
f7fbf515256c22ad043ff9e29d98ea8aec449a78a82a6046c0ff3be3bd94c603
README.md after both capture runs, before surrounding documentation edits:
8bc3d580940731dad646370c84de998c92d8679a6c8d68ccb63245337a5b4082
```

The preceding static asset is retained in ignored
`output/readme_capture_history/protein_examples_molstar_f7fbf515.webp`; its previous
verification remains in [readme_capture.md](readme_capture.md). Existing Mol* output
directories and the original structural inputs remain intact. Both managed screenshot
files are embedded; no unreferenced managed assets or `reference_` assets need pruning.

## Reproduction and verification

Run from the repository root after reproducing the example source frames:

```bash
source source_me.sh && python3 devel/capture_readme_visuals.py
source source_me.sh && python3 -m pyflakes devel/capture_readme_visuals.py
source source_me.sh && python3 -m pytest -q tests/test_markdown_links.py tests/test_readme_first_paragraph.py tests/test_function_typing.py tests/test_ascii_compliance.py
```

- PASS: two capture runs preserved asset and README checksums. The managed sentinels
  remain literal; only their interior is replaced, with the static comparison first.
  Both alt texts describe their image, and README-relative paths resolve.
- PASS: native Rust source and encoded static composite were visually inspected, then
  the composite was inspected at 880 px README width. Labels, glucose, both endpoints,
  and the complete GroEL silhouette remain readable. Renderer attribution is explicit.
- PASS: direct pyflakes and syntax parse. A disposable check under `tests/_temp/`
  confirmed managed-block isolation/idempotence, local embeds, ASCII, dimensions, size
  budgets, and the retained motion checksum. It was removed after verification.
- PASS: the retained animation has 54 encoded frames, loop field 1, and exactly 5,000 ms
  total duration. Its bytes match the earlier verified preview; the helper's 60 logical
  samples at 12 fps and endpoint holds are unchanged.
- PASS: eight focused README, helper typing and README-link checks; `git diff --check`.
- PASS: all 144 repository shebang checks after restoring the helper's executable bit;
  the new capture report's link check and direct ASCII decode also pass.
- Broader focused selection: 234 passed and three failed during concurrent work. Two
  example README link failures referenced not-yet-created Rust preview/science/render
  reports. The third was the existing non-ISO-8859-1 research report. These are outside
  this capture change. After the files appeared, both affected example README link
  checks passed. The untouched research report's ASCII issue remains.

## Handoff and limits

Changelog-ready handoff: README static proof now shows canonical native Rust Goodsell
GroEL beside the unchanged Mol* hexokinase endpoints, with explicit method labels and
the static embed first. Capture is deterministic; the hexokinase motion preview is
byte-identical. The fixed source path and missing-input instructions now select the
Rust GroEL commands. This task writes no global changelog or surrounding README prose.

The rendering owner confirmed a fresh-process replay: all 125 PNGs and encoded media,
poster and still hashes exactly matched the first clean run; source and renderer binary
were unchanged. The stable frame-zero hash matches the capture source above. That replay
belongs to the rendering workstream; this task consumes its native output. Scientific fidelity,
native rendering, capture readability, browser playback, and Impress playback remain
separate evidence. This capture did not run a browser, Impress, a native renderer, or
live GitHub. Prior hexokinase playback observations remain historical evidence rather
than a new playback claim. The full repository suite was not run by this task.

## Temporary directory follow-up

On 2026-11-12, remove the helper's explicit `/tmp` directory argument and rerun the capture twice.
The standard library now selects the secure OS temporary location. Both runs preserved the native
GroEL source frame, both managed asset hashes, and the current README hash byte-for-byte. The
source and image processing, labels, encoding settings, and README behavior did not change. See
[oxillustrate_checks.md](oxillustrate_checks.md) for the focused Bandit, pyflakes, and diff checks.
