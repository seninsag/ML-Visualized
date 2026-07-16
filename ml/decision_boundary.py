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
    # Move Boundary
    # ---------------------------------

    def move_to_position(self, position):
        return self.animate.move_to(position)

    # ---------------------------------
    # Focus
    # ---------------------------------

    def focus(self):
        return self.animate.set_stroke(
            width=7,
            opacity=1,
        )

    # ---------------------------------
    # Restore
    # ---------------------------------

    def restore(self):
        return self.animate.set_stroke(
            width=5,
            opacity=1,
        )

    # ---------------------------------
    # Dim
    # ---------------------------------

    def fade_dim(self):
        return self.animate.set_opacity(0.35)

    # ---------------------------------
    # Fade In
    # ---------------------------------

    def fade_in(self):
        return FadeIn(self)

    # ---------------------------------
    # Fade Out
    # ---------------------------------

    def fade_out(self):
        return FadeOut(self)

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

    # ---------------------------------
    # Reset Color
    # ---------------------------------

    def reset(self):
        return self.animate.set_color(BOUNDARY_COLOR)