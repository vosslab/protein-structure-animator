# Agent instructions

Read [docs/ANIMATION_GUIDANCE.md](docs/ANIMATION_GUIDANCE.md) before changing protein animation
examples or making capability claims. Keep scientific interpretation, coordinate fidelity, visual
quality, playback and fresh-process reproduction as separate evidence.

Follow the repository conventions in [docs/MARKDOWN_STYLE.md](docs/MARKDOWN_STYLE.md),
[docs/REPO_STYLE.md](docs/REPO_STYLE.md) and [docs/PYTHON_STYLE.md](docs/PYTHON_STYLE.md).
Record repository changes in [docs/CHANGELOG.md](docs/CHANGELOG.md), human-stated guidance in
[docs/HUMAN_GUIDANCE.md](docs/HUMAN_GUIDANCE.md), and settled design decisions in
[docs/DESIGN_DECISIONS.md](docs/DESIGN_DECISIONS.md).

Run repository Python as `source source_me.sh && python3`. Use native application runtimes for
their scripts. Preserve original structural inputs; generated structures and media belong in the
ignored `output/` directory. Keep dependency minimums open-ended and record tested versions as
observations, not pins. Do not launch Blender for the initial examples.
