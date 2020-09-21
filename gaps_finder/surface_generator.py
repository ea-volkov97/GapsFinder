from gaps_finder.grid import Grid


class SurfaceGenerator:

    @staticmethod
    def generate_grid(
            length: float,
            width: float,
            dots_per_length: int,
            dots_per_width: int,
            mu: float,
            deviation: float,
            sigma: float
    ):
        return Grid(length, width, dots_per_length, dots_per_width)
