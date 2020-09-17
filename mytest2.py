from gaps_finder.graphics import draw_surface
from gaps_finder.grid import Grid
from gaps_finder.settings import (
    SURFACE_LENGTH,
    SURFACE_WIDTH,
    DOTS_PER_LENGTH,
    DOTS_PER_WIDTH
)
from gaps_finder.surface import Surface

grid = Grid(SURFACE_LENGTH, SURFACE_WIDTH, DOTS_PER_LENGTH, DOTS_PER_WIDTH)
surface = Surface(grid)
draw_surface(surface)