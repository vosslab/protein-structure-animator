#!/usr/bin/env python3
"""Encode a 125-frame, five-second teaching loop into MP4, WebP, and GIF."""

import pathlib
import argparse
import subprocess

import PIL.Image


def check_frames(directory: pathlib.Path) -> tuple[int, int]:
	"""Reject gaps, stale extra frames, odd dimensions, and changing image size."""
	expected = [directory / f'frame_{i:03d}.png' for i in range(125)]
	if sorted(directory.glob('frame_*.png')) != expected:
		raise ValueError('Expected exactly frame_000.png through frame_124.png')
	with PIL.Image.open(expected[0]) as image:
		size = image.size
	if any(d % 2 for d in size):
		raise ValueError('H.264 requires even image dimensions')
	for filename in expected:
		with PIL.Image.open(filename) as image:
			if image.size != size:
				raise ValueError(f'Frame size changed: {filename}')
			image.verify()
	return size


def main() -> None:
	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument('frames', type=pathlib.Path)
	args = parser.parse_args()
	width, height = check_frames(args.frames)
	out = args.frames.parent
	command = ['ffmpeg', '-hide_banner', '-loglevel', 'error', '-y', '-framerate', '25',
		'-i', str(args.frames / 'frame_%03d.png')]
	# Opaque delivery formats need a matte before alpha is discarded.
	opaque_command = command + ['-f', 'lavfi', '-i',
		f'color=c=white:s={width}x{height}:r=25']
	composite = '[1:v][0:v]overlay=shortest=1:format=auto'
	# ASVS 1.2.5: pass paths as argv, without an interpolated shell command.
	subprocess.run(opaque_command + ['-filter_complex', composite,
		'-c:v', 'libx264', '-crf', '18', '-pix_fmt', 'yuv420p',
		'-movflags', '+faststart', str(out / 'animation.mp4')], check=True)
	subprocess.run(command + ['-c:v', 'libwebp_anim', '-lossless', '1', '-loop', '0',
		str(out / 'animation.webp')], check=True)
	subprocess.run(opaque_command + ['-filter_complex',
		composite + ',split[a][b];[a]palettegen=stats_mode=full[p];'
		'[b][p]paletteuse=dither=sierra2_4a',
		'-loop', '0', str(out / 'animation.gif')], check=True)
	with PIL.Image.open(args.frames / 'frame_000.png') as image:
		image.save(out / 'poster.webp', lossless=True)


if __name__ == '__main__':
	main()
