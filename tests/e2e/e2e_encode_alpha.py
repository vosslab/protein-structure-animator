#!/usr/bin/env python3
"""Protect alpha WebP/poster and opaque white MP4/GIF delivery with real codecs."""

import sys
import json
import pathlib
import tempfile
import subprocess

import PIL.Image


def main() -> None:
	"""Run the encoder and decode every moving frame, including vacated pixels."""
	repo = pathlib.Path(subprocess.check_output(
		['git', 'rev-parse', '--show-toplevel'], text=True).strip())
	with tempfile.TemporaryDirectory(prefix='encode_alpha_') as directory:
		out = pathlib.Path(directory)
		frames = out / 'frames'
		frames.mkdir()
		sources = []
		for index in range(125):
			image = PIL.Image.new('RGBA', (96, 64), (0, 0, 0, 0))
			left = 8 + index % 64
			image.paste((255, 0, 0, 128), (left - 1, 7, left + 9, 17))
			image.paste((255, 0, 0, 255), (left, 8, left + 8, 16))
			image.paste((0, 0, 255, 128), (16, 32, 32, 48))
			image.paste((255, 255, 255, 255), (48, 32, 64, 48))
			image.save(frames / f'frame_{index:03d}.png')
			sources.append(image)
		subprocess.run([sys.executable, str(repo / 'tools/encode_loop.py'), str(frames)],
			check=True)
		with PIL.Image.open(out / 'animation.webp') as animation:
			assert animation.n_frames == 125 and animation.info['loop'] == 0
			for index, source in enumerate(sources):
				animation.seek(index)
				assert animation.convert('RGBA').tobytes() == source.tobytes(), index
				assert animation.info['duration'] == 40, index
		with PIL.Image.open(out / 'poster.webp') as poster:
			assert poster.convert('RGBA').tobytes() == sources[0].tobytes()
		with PIL.Image.open(out / 'animation.gif') as animation:
			assert animation.n_frames == 125 and animation.info['loop'] == 0
			for index in range(125):
				animation.seek(index)
				decoded = animation.convert('RGBA')
				assert decoded.getchannel('A').getextrema() == (255, 255), index
				assert decoded.getpixel((0, 0)) == (255, 255, 255, 255), index
				assert decoded.getpixel((24, 40)) == (127, 127, 255, 255), index
				assert animation.info['duration'] == 40, index
		decoded = subprocess.check_output(['ffmpeg', '-v', 'error', '-i',
			str(out / 'animation.mp4'), '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'])
		probe = json.loads(subprocess.check_output(['ffprobe', '-v', 'error',
			'-show_entries', 'stream=avg_frame_rate,duration', '-of', 'json',
			str(out / 'animation.mp4')]))
		assert probe['streams'][0]['avg_frame_rate'] == '25/1'
		assert float(probe['streams'][0]['duration']) == 5.0
		frame_bytes = 96 * 64 * 3
		assert len(decoded) == 125 * frame_bytes
		for index in range(125):
			frame = PIL.Image.frombytes('RGB', (96, 64),
				decoded[index * frame_bytes:(index + 1) * frame_bytes])
			assert min(frame.getpixel((0, 0))) >= 248, index
			assert min(frame.getpixel((56, 40))) >= 248, index
			pixel = frame.getpixel((24, 40))
			assert all(abs(value - expected) <= 10
				for value, expected in zip(pixel, (127, 127, 255))), (index, pixel)
		print('PASS: 125 frames at 40 ms; WebP/poster exact RGBA; GIF opaque white; '
			'MP4 white background and semitransparent blue composite (tolerance 10).')


if __name__ == '__main__':
	main()
