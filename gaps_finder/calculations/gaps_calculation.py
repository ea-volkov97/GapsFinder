"""
Расчет зазоров между плоскостью и поверхностью заготовки
"""

import numpy as np

from gaps_finder.Vector3 import Vector3
from gaps_finder.models import get_engine
# from gaps_finder.models import surface
from gaps_finder.plane import Plane
from gaps_finder.settings import DATABASE_SETTINGS
from gaps_finder.surface import Surface


def get_gaps(surface: Surface, plane: Plane):
    gaps = []

    surface_points = surface.points
    for surface_point in surface_points:
        gaps.append(plane.distance_to_point(surface_point))

    return gaps


def main():
    engine = get_engine(**DATABASE_SETTINGS)

    return 0


if __name__ == '__main__':
    main()
