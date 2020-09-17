from typing import List

from gaps_finder.Vector3 import Vector3
from gaps_finder.surface import Surface
from gaps_finder.plane import Plane

from itertools import combinations


def is_stable(surface: Surface, fulcrum_points: List[Vector3:3], gravity_vector: Vector3 = Vector3(0, 0, -9.81)):

    return 0


def get_tangent_plane(surface: Surface):
    surface_points = surface.points
    surface_points_triplets = list(combinations(surface_points, 3))

    # TODO Проверка на устойчивость (находится ли центр масс вне треугольника) и на касание
    for surface_points_triplet in surface_points_triplets:
        break

    tangent_plane = Plane()

    return tangent_plane
