import numpy as np

from gaps_finder.surface import Surface


def init_3d_graphic():
    """
    Инициализация библиотеки matplotlib. Возвращает объекты AXES и PLOT.
    :return:
    """
    import matplotlib.pyplot as plot

    return plot


def draw_surface(surface: Surface):
    """
    Выполняет построение трехмерного графика поверхности.
    :param surface:
    :return:
    """
    plot = init_3d_graphic()

    figure = plot.figure()
    axes = figure.add_subplot(111, projection='3d')

    x, y, z = surface.get_points_coordinates

    axes.plot_surface(np.array(x), np.array(y), np.array(z))
    plot.show()
