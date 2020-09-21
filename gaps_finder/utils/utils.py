from typing import List

import numpy as np
from gaps_finder.vector3 import Vector3


def get_triangle_square_from_three_points(point1: Vector3, point2: Vector3, point3: Vector3):
    """
    Возвращает площадь треугольника по трём точкам

    :param point1:
    :param point2:
    :param point3:
    :return:
    """

    x1, y1, _ = point1
    x2, y2, _ = point2
    x3, y3, _ = point3

    square = 0

    return square


def dot_vector_product(vector1: Vector3, vector2: Vector3) -> float:
    """
    Возвращает скалярное произведение двух векторов.
    :param vector1:
    :param vector2:
    :return:
    """
    return vector1.x * vector2.x + vector1.y * vector2.y + vector1.z * vector2.z


def is_vectors_collinear(vector1: Vector3, vector2: Vector3) -> bool:
    """
    Возвращает True, если векторы коллинеарны.
    :param vector1:
    :param vector2:
    :return:
    """
    if dot_vector_product(vector1, vector2) == 1:
        return True
    else:
        return False


def get_plane_equation_coefficients(point1: Vector3, point2: Vector3, point3: Vector3):
    """
    Возвращает коэффициенты уравнения плоскости по трём точкам
    :param point1:точка 1
    :param point2:точка 2
    :param point3:точка 3
    :return:
    """
    # TODO Подумать над тем, должен ли быть у D минус?

    if is_vectors_collinear(point2 - point1, point3 - point1):
        a = 0
        b = 0
        c = 1
        d = 0
    else:
        x1, y1, z1 = point1.xyz
        x2, y2, z2 = point2.xyz
        x3, y3, z3 = point3.xyz

        a = y1 * (z2 - z3) + y2 * (z3 - z1) + y3 * (z1 - z2)
        b = z1 * (x2 - x3) + z2 * (x3 - x1) + z3 * (x1 - x2)
        c = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)
        d = -(x1 * (y2 * z3 - y3 * z2) + x2 * (y3 * z1 - y1 * z3) + x3 * (y1 * z2 - y2 * z1))

    return a, b, c, d


def get_mass_center_position(points: List[Vector3]):
    mass_center = Vector3()



    return mass_center