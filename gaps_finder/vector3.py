from math import sqrt


class Vector3:
    """
    Класс Vector3 представляет вектор в трехмерном пространстве.
    """
    def __init__(self, x: float = 0, y: float = 0, z: float = 0):
        self._x = x
        self._y = y
        self._z = z

    @property
    def x(self):
        """
        Возвращает координату X вектора.
        """
        return self._x

    @property
    def y(self):
        """
        Возвращает координату Y вектора.
        """
        return self._y

    @property
    def z(self):
        """
        Возвращает координату Z вектора.
        """
        return self._z

    @property
    def xyz(self):
        """
        Возвращает кортеж, состоящий из X, Y и Z координат вектора.
        """
        return self._x, self._y, self._z

    @property
    def length(self):
        """
        Возвращает модуль (длину) вектора.
        """
        return sqrt(self._x ** 2 + self._y ** 2 + self._z ** 2)

    @property
    def normalized(self):
        """
        Возвращает нормализованное значение вектора.
        """
        return Vector3(self._x / self.length, self._y / self.length, self._z / self.length)

    def __repr__(self):
        return str(f'({self._x}, {self._y}, {self._z})')

    def __eq__(self, other):
        if self._x == other.x and self._y == other.y and self._z == other.z:
            return True
        else:
            return False

    @staticmethod
    def dot_product(vector1, vector2) -> float:
        """
        Возвращает скалярное произведение двух векторов.
        :param vector1:
        :param vector2:
        :return:
        """
        return vector1.x * vector2.x + vector1.y * vector2.y + vector1.z * vector2.z

    @staticmethod
    def is_collinear(vector1, vector2) -> bool:
        """
        Возвращает True, если векторы коллинеарны.
        :param vector1:
        :param vector2:
        :return:
        """
        if Vector3.dot_product(vector1, vector2) == 1:
            return True
        else:
            return False

    @staticmethod
    def is_orthogonal(vector1, vector2) -> bool:
        """
        Возвращает True, если векторы ортогональны.
        :param vector1:
        :param vector2:
        :return:
        """
        if Vector3.dot_product(vector1, vector2) == 0:
            return True
        else:
            return False

    def __add__(self, other):
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)
