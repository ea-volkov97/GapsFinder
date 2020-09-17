"""
Генерация поверхности
"""

from itertools import combinations
from typing import List

import numpy as np

from gaps_finder.Vector3 import Vector3
from gaps_finder.grid import Grid

from gaps_finder.settings import (
    DATABASE_SETTINGS,
    GENERATION_TRIES_COUNT,
    SURFACE_LENGTH,
    SURFACE_WIDTH,
    DOTS_PER_LENGTH,
    DOTS_PER_WIDTH,
    DEVIATION,
    MU,
    SIGMA
)
from gaps_finder.surface import Surface


#def _get_points_from_coordinates(x: np.ndarray[float], y: np.ndarray[float], z: np.ndarray[float]):
#    points = []
#
#    for index, zn in np.ndenumerate(z):
#        xn = x[index]
#        yn = y[index]
#        points.append(Vector3(xn, yn, zn))
#
#    return points


def _get_xy_grid(length: float, width: float, dots_per_length: int, dots_per_width: int):
    """
    Возвращает двумерную сетку координат
    :param width:
    :param length:
    :param dots_per_length:
    :param dots_per_width:
    :return:
    """

    x_values = np.linspace(0, length, dots_per_length + 1)
    y_values = np.linspace(0, width, dots_per_width + 1)

    return np.meshgrid(x_values, y_values)


def generate_rectangle_surface(
        length=SURFACE_LENGTH,
        width=SURFACE_WIDTH,
        dots_per_length=DOTS_PER_LENGTH,
        dots_per_width=DOTS_PER_WIDTH,
        deviation=DEVIATION,
        mu=MU
):
    x, y = _get_xy_grid(length, width, dots_per_length, dots_per_width)
    z = np.random.normal(
        loc=mu,
        scale=deviation,
        size=(dots_per_length + 1, dots_per_width + 1)
    )

    return Surface(_get_points_from_coordinates(x, y, z))


def generate_surface_and_plane():
    x, y, z = generate_rectangle_surface()
    points = _get_points_from_coordinates(x, y, z)

    possible_combinations = list(combinations(points, 3))


def main():
    print('Запуск процесса генерации поверхностей.\n\n')
    print(f"Параметры генерации:\n"
          f"кол-во генерируемых поверхностей: {GENERATION_TRIES_COUNT}\n"
          f"длина генерируемых поверхностей: {SURFACE_LENGTH}\n"
          f"ширина генерируемых поверхностей: {SURFACE_WIDTH}\n"
          f"кол-во точек на длину поверхности: {DOTS_PER_LENGTH}\n"
          f"кол-во точек на ширину поверхности: {DOTS_PER_WIDTH}\n"
          f"величина допуска: {DEVIATION}\n"
          f"математическое ожидание: {MU}\n"
          f"значение сигма: {SIGMA}\n\n")

    surfaces = []

    for surface_number in range(GENERATION_TRIES_COUNT):
        grid = Grid(SURFACE_LENGTH, SURFACE_WIDTH, DOTS_PER_LENGTH, DOTS_PER_WIDTH)
        surface = Surface(grid)
        surfaces.append(surface)

    print("Генерация поверхностей успешно завершена!")


if __name__ == '__main__':
    main()
