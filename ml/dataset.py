from manim import *

from ml.datapoint import DataPoint
from engine.theme import *


class Dataset(VGroup):
    def __init__(self, red_points=None, blue_points=None):
        super().__init__()

        red_points = red_points or []
        blue_points = blue_points or []

        for point in red_points:
            self.add(DataPoint(point, CLASS_RED))

        for point in blue_points:
            self.add(DataPoint(point, CLASS_BLUE))

    def animate_in(self):
        return LaggedStart(
            *[
                GrowFromCenter(point)
                for point in self
            ],
            lag_ratio=0.2
        )