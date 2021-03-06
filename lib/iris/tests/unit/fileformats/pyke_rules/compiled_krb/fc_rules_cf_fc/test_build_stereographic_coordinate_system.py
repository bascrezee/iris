# (C) British Crown Copyright 2016, Met Office
#
# This file is part of Iris.
#
# Iris is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the
# Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Iris is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Iris.  If not, see <http://www.gnu.org/licenses/>.
"""
Test function :func:`iris.fileformats._pyke_rules.compiled_krb.\
fc_rules_cf_fc.build_sterographic_coordinate_system`.

"""

from __future__ import (absolute_import, division, print_function)
from six.moves import (filter, input, map, range, zip)  # noqa

# import iris tests first so that some things can be initialised before
# importing anything else
import iris.tests as tests

import numpy as np

import iris
from iris.coord_systems import Stereographic
from iris.fileformats._pyke_rules.compiled_krb.fc_rules_cf_fc import \
    build_stereographic_coordinate_system
from iris.tests import mock


class TestBuildStereographicCoordinateSystem(tests.IrisTest):
    def test_valid(self):
        cf_grid_var = mock.Mock(
            spec=[],
            latitude_of_projection_origin=0,
            longitude_of_projection_origin=0,
            false_easting=-100,
            false_northing=200,
            scale_factor_at_projection_origin=1,
            semi_major_axis=6377563.396,
            semi_minor_axis=6356256.909)

        cs = build_stereographic_coordinate_system(None, cf_grid_var)

        expected = Stereographic(
            central_lat=cf_grid_var.latitude_of_projection_origin,
            central_lon=cf_grid_var.longitude_of_projection_origin,
            false_easting=cf_grid_var.false_easting,
            false_northing=cf_grid_var.false_northing,
            ellipsoid=iris.coord_systems.GeogCS(
                cf_grid_var.semi_major_axis,
                cf_grid_var.semi_minor_axis))
        self.assertEqual(cs, expected)

    def test_inverse_flattening(self):
        cf_grid_var = mock.Mock(
            spec=[],
            latitude_of_projection_origin=0,
            longitude_of_projection_origin=0,
            false_easting=-100,
            false_northing=200,
            scale_factor_at_projection_origin=1,
            semi_major_axis=6377563.396,
            inverse_flattening=299.3249646)

        cs = build_stereographic_coordinate_system(None, cf_grid_var)

        expected = Stereographic(
            central_lat=cf_grid_var.latitude_of_projection_origin,
            central_lon=cf_grid_var.longitude_of_projection_origin,
            false_easting=cf_grid_var.false_easting,
            false_northing=cf_grid_var.false_northing,
            ellipsoid=iris.coord_systems.GeogCS(
                cf_grid_var.semi_major_axis,
                inverse_flattening=cf_grid_var.inverse_flattening))
        self.assertEqual(cs, expected)


if __name__ == "__main__":
    tests.main()
