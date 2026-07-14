from manim import *

from engine.theme import *


class DataPoint(Dot):
    def __init__(self, position, color=CLASS_BLUE):
        super().__init__(
            point=position,
            radius=POINT_RADIUS,
            color=color,
        )

        # Store original appearance
        self.original_color = color
        self.original_radius = POINT_RADIUS

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
    # Fade Out
    # ---------------------------------

    def fade_out(self):
        return AnimationGroup(
            self.animate.scale(0.4).set_opacity(0.2),
            lag_ratio=0,
        )

    # ---------------------------------
    # Fade In Again
    # ---------------------------------

    def fade_in(self):
        return self.animate.scale(2.5).set_opacity(1)

    # ---------------------------------
    # Primary Focus
    # ---------------------------------

    def focus(self):
        return self.animate.set_opacity(1).scale(1.30)

    # ---------------------------------
    # Secondary Focus
    # ---------------------------------

    def secondary(self):
        return self.animate.set_opacity(1).scale(1.15)

    # ---------------------------------
    # Dim
    # ---------------------------------

    def fade_dim(self):
        return self.animate.set_opacity(0.35)

    # ---------------------------------
    # Restore Appearance
    # ---------------------------------

    def restore_state(self):
        return self.animate.set_opacity(1).scale(1 / 1.15)

    # ---------------------------------
    # Highlight (Backward Compatibility)
    # ---------------------------------

    def highlight(self):
        return self.focus()

    # ---------------------------------
    # Restore Highlight (Backward Compatibility)
    # ---------------------------------

    def restore(self):
        return self.animate.scale(1 / 1.30)

    # ---------------------------------
    # Change Color
    # ---------------------------------

    def change_color(self, color):
        return self.animate.set_color(color)

    # ---------------------------------
    # Restore Original Color
    # ---------------------------------

    def restore_color(self):
        return self.animate.set_color(self.original_color)