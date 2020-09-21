"""
Расчет зазоров между плоскостью и поверхностью заготовки
"""

from gaps_finder.plane import Plane
from settings import DATABASE_SETTINGS
from gaps_finder.surface import Surface


def get_gaps(surface: Surface, plane: Plane):
    gaps = []

    surface_points = surface.points
    for surface_point in surface_points:
        gaps.append(plane.distance_to_point(surface_point))

    return gaps


def main():

    return 0


if __name__ == '__main__':
    main()
