from typing import List

from gaps_finder.vector3 import Vector3
from gaps_finder.grid import Grid
from gaps_finder.utils.utils import get_mass_center_position


class Surface:
    """
    Класс Surface представляет собой поверхность, заданную массивом точек.
    """
    def __init__(self, points: List[Vector3], mass_center: Vector3 = Vector3()):
        self._points = points

        # TODO подумать над тем, чтобы рассчитывать центр масс,
        #  чтобы можно было считать не только прямоугольные поверхности,
        #  а также задавать его положение вручную.
        # if mass_center == Vector3():
        #    mass_center = get_mass_center_position(self._points)
        # else:
        #    mass_center = Vector3()

    def __init__(self, grid: Grid):
        self._grid = grid

    @property
    def get_points_coordinates(self):
        """
        Возвращает кортеж, состоящих из двумерных массивов значений X, Y и Z координат точек, образующих поверхность.
        :return:
        """
        return self._grid.grid_x_coordinates, self._grid.grid_y_coordinates, self._grid.grid_z_coordinate

    @property
    def points_count(self):
        """
        Возвращает кол-во точек, образующих поверхность.
        """
        return len(self._points)

    @property
    def points_coordinates(self):
        """
        Возвращает кортеж, состоящих из массивов значений X, Y и Z координат точек, образующих поверхность.
        """
        x = []
        y = []
        z = []

        for point in self._points:
            x.append(point.x)
            y.append(point.y)
            z.append(point.z)

        return x, y, z
