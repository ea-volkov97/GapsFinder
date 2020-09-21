from gaps_finder.vector3 import Vector3
from gaps_finder.utils.utils import get_plane_equation_coefficients


class Plane:
    def __init__(self):
        self._a = 0
        self._b = 0
        self._c = 1
        self._d = 0

    def __init__(self, point1: Vector3, point2: Vector3, point3: Vector3):
        self._a, self._b, self._c, self._d = get_plane_equation_coefficients(point1, point2, point3)

    @property
    def normal(self):
        """
        Возвращает координаты вектора нормали к плоскости.
        :return:
        """
        normal = Vector3(self._a, self._b, self._c)
        return normal.normalized

    @property
    def distance_to_point(self, point: Vector3):
        """
        Возвращает расстояние от плоскости до указанной точки.
        :param point:
        :return:
        """
        return abs(self._a * point.x + self._b * point.y + self._c * point.z + self._d) / self.normal

    def get_z_coordinate_by_x_y_value(self, x: float, y: float) -> float:
        """
        Возвращает z-координату плоскости по заданным x и y.
        :param x:
        :param y:
        :return:
        """
        return (self._a * x + self._b + self._d) / self._c
