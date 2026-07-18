from manim import *
from engine.theme import *

class FeatureSpace(VGroup):

    def __init__(self):
        super().__init__()

        self.x_axis = Line(
            LEFT * 3,
            RIGHT * 3,
            stroke_color=AXIS_COLOR,
            stroke_width=AXIS_WIDTH,
        )

        self.y_axis = Line(
            DOWN * 3,
            UP * 3,
            stroke_color=AXIS_COLOR,
            stroke_width=AXIS_WIDTH,
        )

        self.z_axis = Line(
            ORIGIN,
            OUT * 3,
            stroke_color=AXIS_COLOR,
            stroke_width=AXIS_WIDTH,
        )

        # Start with only X and Y
        self.add(
            self.x_axis,
            self.y_axis,
        )