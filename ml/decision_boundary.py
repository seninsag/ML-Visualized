from manim import *

from engine.theme import *


class DecisionBoundary(Line):

    def __init__(self, angle=20):
        super().__init__(
            start=LEFT * 4,
            end=RIGHT * 4,
            color=BOUNDARY_COLOR,
            stroke_width=BOUNDARY_WIDTH,
        )

        self.rotate(angle * DEGREES)

    
    def success(self):
        return self.animate.set_color(GREEN)