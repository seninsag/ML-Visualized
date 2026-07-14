from manim import *

from engine.theme import *


class DataPoint(Dot):
    def __init__(self, position, color=CLASS_BLUE):
        super().__init__(
            point=position,
            radius=POINT_RADIUS,
            color=color,
        )

    # ---------------------------------
    # Entrance Animation
    # ---------------------------------
    def animate_in(self):
        return GrowFromCenter(self)

    # ---------------------------------
    # Move Animation
    # ---------------------------------
    def move_to_position(self, position):
        return self.animate.move_to(position)

    # ---------------------------------
    # Fade Out (for simplifying datasets)
    # ---------------------------------
    def fade_out(self):
        return AnimationGroup(
            self.animate.set_opacity(0.2).scale(0.4),
            FadeOut(self),
        )

    # ---------------------------------
    # Highlight
    # ---------------------------------
    def highlight(self):
        return self.animate.scale(1.3)

    # ---------------------------------
    # Reset Highlight
    # ---------------------------------
    def restore(self):
        return self.animate.scale(1 / 1.3)