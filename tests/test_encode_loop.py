"""Protect the delivery timing from missing or stale frames."""

import runpy
import pathlib

import pytest
import PIL.Image


def test_loop_rejects_missing_and_extra_frames(tmp_path: pathlib.Path) -> None:
	check_frames = runpy.run_path('tools/encode_loop.py')['check_frames']
	for index in range(125):
		PIL.Image.new('RGB', (4, 4)).save(tmp_path / f'frame_{index:03d}.png')
	check_frames(tmp_path)
	(tmp_path / 'frame_063.png').rename(tmp_path / 'frame_125.png')
	with pytest.raises(ValueError, match='exactly'):
		check_frames(tmp_path)
