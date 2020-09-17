import numpy as np

from gaps_finder.surface import Surface


def init_3d_graphic():
    """
    Инициализация библиотеки matplotlib. Возвращает объекты AXES и PLOT.
    :return:
    """
    import matplotlib.pyplot as plot

    return plot


def draw_surface(plot, x, y, z, title: str = 'Поверхность', x_label: str = 'x', y_label: str = 'y', z_label: str = 'z'):
    fig = plot.figure()
    axes = fig.add_subplot(projection='3d')
    axes.plot(x, y, z)

    axes.set_title(title)
    axes.set_xlabel(x_label)
    axes.set_ylabel(y_label)
    axes.set_zlabel(z_label)

    plot.show()


def draw_surface():
    import matplotlib.pyplot as plot
    fig = plot.figure()
    axes = fig.add_subplot(111, projection='3d')

    #u, v = np.mgrid[0:2 * np.pi:20j, 0:np.pi:10j]
    #x = np.cos(u) * np.sin(v)
    #y = np.sin(u) * np.sin(v)
    #z = np.cos(v)

    #points = [Vector3(-1, -1, 3), Vector3(-1, 0, 4), Vector3(-1, 1, 3), Vector3(0, -1, 1), Vector3(0, 0, 2), Vector3(0, 1, 1)]
    #x_grid = np.ndarray
    #for point in points:
    #    x_grid = []


    #TODO: подумать, как преобразовать массив точек в такой же формат
    # может стоить добавить поверхности неоторый Grid?
    x_grid = [(-1.0, -1.0, -1.0), (0.0, 0.5, 0.0), (1.0, 1.0, 1.0)]
    y_grid = [(-1.0, 0.0, 1.0), (-1.0, 0.0, 1.0), (-1.0, 0.0, 1.0)]
    z_grid = np.array([(3, 4, 3), (1, 2, 1), (2, 2, 2)])

    axes.plot_surface(x_grid, y_grid, z_grid)

    plot.show()


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
