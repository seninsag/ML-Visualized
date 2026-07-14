from manim import *
from engine.theme import *

class FeatureSpace(VGroup):

    def __init__(self):
        super().__init__()

        x_axis = Line(
            LEFT * 4,
            RIGHT * 4,
            stroke_color=AXIS_COLOR,
            stroke_width=AXIS_WIDTH,
        )

        y_axis = Line(
            DOWN * 3,
            UP * 3,
            stroke_color=AXIS_COLOR,
            stroke_width=AXIS_WIDTH,
        )

        self.add(x_axis, y_axis)