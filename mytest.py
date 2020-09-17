from gaps_finder.Vector3 import Vector3
from gaps_finder.graphics import init_3d_graphic
from gaps_finder.graphics import draw_surface

import matplotlib.pyplot as plot
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

x = np.linspace(-np.pi, np.pi, 50)
y = x
z = np.cos(x)



#plot = init_3d_graphic()
#draw_surface(plot, x, y, z)

draw_surface()

point1 = Vector3()
point2 = Vector3()

print(point1 == point2)