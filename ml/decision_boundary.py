from manim import *

from engine.theme import *


class DecisionBoundary(Line):

    def __init__(self, angle=18):
        super().__init__(
            LEFT * 4,
            RIGHT * 4,
            color=BOUNDARY_COLOR,
            stroke_width=5,
        )

        self.current_angle = angle
        self.rotate(angle * DEGREES)

    # ---------------------------------
    # Rotate to an absolute angle
    # ---------------------------------

    def rotate_to(self, target_angle):

        delta = target_angle - self.current_angle
        self.current_angle = target_angle

        return Rotate(
            self,
            angle=delta * DEGREES,
            about_point=self.get_center(),
            rate_func=smooth,
        )

    # ---------------------------------
    # Success Animation
    # ---------------------------------

    def success(self):
        return self.animate.set_color(GREEN)

    # ---------------------------------
    # Failure Animation
    # ---------------------------------

    def failure(self):
        return self.animate.set_color(RED)