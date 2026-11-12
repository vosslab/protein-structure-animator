"""Protect fixed molecular origin, rigid rotation and full-turn clipping safety."""

import runpy

import numpy


def test_fixed_origin_and_sphere_bounds_cover_full_turn() -> None:
	functions = runpy.run_path('examples/groel_rotation/render_oxillustrate.py')
	coordinates = numpy.array([[18., -12., 4.], [28., 9., -8.], [22., 3., 15.]])
	origin, scale, depth = functions['fixed_framing'](coordinates)
	rotated = functions['rotated']
	for index in range(125):
		orientation = [15 + 360 * index / 125, 25, 0]
		center = rotated(origin, orientation) + [0, 0, depth]
		points = numpy.array([rotated(point, orientation) - center for point in coordinates])
		assert numpy.allclose(rotated(origin, orientation) - center, [0, 0, -depth])
		assert numpy.allclose(numpy.linalg.norm(points[1] - points[0]),
			numpy.linalg.norm(coordinates[1] - coordinates[0]))
		assert ((numpy.abs(points[:, :2]) + 1.8) * scale <= 290).all()
		assert (points[:, 2] + 1.8 < 0).all()
	assert numpy.allclose(rotated(numpy.array([1., 0., 0.]), [0, 0, 90]), [0, 1, 0])
