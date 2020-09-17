import numpy as np

from gaps_finder.Vector3 import Vector3


class Grid:
    def __init__(self, length: float = 1.0, width: float = 1.0, dots_per_length: int = 3, dots_per_width: int = 3):
        self._length = length if length > 0.0 else 1.0
        self._width = width if width > 0.0 else 1.0
        self._dots_per_length = dots_per_length if dots_per_length > 3 else 3
        self._dots_per_width = dots_per_width if dots_per_width > 3 else 3

        self._points = []

        x_values = np.linspace(0, self._length, self._dots_per_length)
        y_values = np.linspace(0, self._width, self._dots_per_width)
        z_values = np.random.normal(
            loc=0, #mu
            scale=0.1, #deviation
            size=(self._dots_per_length, self._dots_per_width)
        )

        i = 0
        for x in x_values:
            j = 0
            for y in y_values:
                point = Vector3(x, y, z_values[i][j])
                self._points.append(point)
                j += 1
            i += 1

    @property
    def grid_x_coordinates(self):
        """
        Возвращает двумерный массив, состоящий из значений x-координат сетки.
        :return:
        """
        x_coordinates = []

        for i in range(self._dots_per_length):
            x_values = []
            for j in range(self._dots_per_width):
                x_values.append(self._points[j + self._dots_per_length * i].x)
            x_coordinates.append(x_values)

        return x_coordinates

    @property
    def grid_y_coordinates(self):
        """
        Возвращает двумерный массив, состоящий из значений y-координат сетки.
        :return:
        """
        y_coordinates = []

        for j in range(self._dots_per_width):
            y_values = []
            for i in range(self._dots_per_length):
                y_values.append(self._points[i + self._dots_per_width * i].y)
            y_coordinates.append(y_values)

        return y_coordinates

    @property
    def grid_z_coordinate(self):
        """
        Возвращает двумерный массив, состоящий из значений z-координат сетки.
        :return:
        """
        z_coordinates = []

        for i in range(self._dots_per_length):
            z_values = []
            for j in range(self._dots_per_width):
                z_values.append(self._points[j + self._dots_per_width * i].z)
            z_coordinates.append(z_values)

        return z_coordinates

    @property
    def length(self):
        """
        Возвращает длину сетки.
        :return:
        """
        return self._length

    @property
    def width(self):
        """
        Возвращает ширину сетки.
        :return:
        """
        return self._width

    @property
    def dots_per_length(self):
        """
        Возвращает количество точек сетки на длину.
        :return:
        """
        return self._dots_per_length

    @property
    def dots_per_width(self):
        """
        Возвращает количество точек сетки на ширину.
        :return:
        """
        return self._dots_per_width
