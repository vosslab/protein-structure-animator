"""Protect rigid rotor motion, fixed housing, and a rotor-preserving cutaway."""

import runpy

import numpy


#============================================
def test_rigid_rotor_and_fixed_housing() -> None:
	functions = runpy.run_path('examples/atp_synthase_motor/render_oxillustrate.py')
	points = numpy.array([[2., 1., 7.], [-3., 2., 4.], [4., -1., 2.]])
	rotor = numpy.array([True, True, False])
	move = functions['rotor_frame']
	for index in range(126):
		moved = move(points, rotor, index)
		assert numpy.array_equal(moved[~rotor], points[~rotor])
		assert numpy.allclose(numpy.linalg.norm(moved[0] - moved[1]), numpy.sqrt(35))
		assert numpy.allclose(moved[rotor, 2], points[rotor, 2])
	assert numpy.allclose(move(points, rotor, 125), points)
	assert not numpy.allclose(move(points, rotor, 124)[rotor], points[rotor])
	assert numpy.linalg.det(functions['BASIS']) > 0.999999


#============================================
def test_cutaway_preserves_rotor_and_camera_distance() -> None:
	functions = runpy.run_path('examples/atp_synthase_motor/render_oxillustrate.py')
	points = numpy.array([[0., 4., 2.], [0., 4., 2.], [3., -2., 1.]])
	rotor = numpy.array([True, False, False])
	assert functions['cutaway_mask'](points, rotor).tolist() == [True, False, True]
	view = functions['camera_coordinates'](points)
	assert numpy.allclose(numpy.linalg.norm(view[0] - view[2]), numpy.sqrt(46))
	assert numpy.allclose(numpy.linalg.det(functions['camera_coordinates'](numpy.eye(3))), 1)
