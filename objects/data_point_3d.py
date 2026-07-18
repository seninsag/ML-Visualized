from manim import *
from engine.theme import *


class DataPoint3D(Dot):
    """
    3D data point matching the existing DataPoint API.
    Supports 3D coordinates, trace paths, and labels.
    """

    def __init__(self, position, color=CLASS_BLUE):
        super().__init__(
            point=position,
            radius=POINT_3D_RADIUS,
            color=color,
        )

        self.original_color = color
        self.original_radius = POINT_3D_RADIUS
        self.trace = None
        self.label = None

        # Save initial state for Restore
        self.save_state()

    # ---------------------------------
    # Position
    # ---------------------------------

    def move_to_coordinate(self, coord):
        return self.animate.move_to(coord)

    def animate_to_coordinate(self, coord, run_time=2):
        return self.animate.move_to(coord).set_run_time(run_time)

    # ---------------------------------
    # Visual States
    # ---------------------------------

    def animate_in(self):
        return GrowFromCenter(self)

    def animate_fade(self):
        return self.animate.scale(0.4).set_opacity(0.2)

    def restore(self):
        return Restore(self)

    def highlight(self):
        return self.animate.set_opacity(1).scale(1.30)

    def soft_highlight(self):
        return self.animate.set_opacity(1).scale(1.15)

    def fade_dim(self):
        return self.animate.set_opacity(0.35)

    def restore_state(self):
        return self.animate.set_opacity(1).scale(1 / 1.15)

    def change_color(self, color):
        return self.animate.set_color(color)

    def restore_color(self):
        return self.animate.set_color(self.original_color)

    def misclassified(self):
        return Succession(
            self.animate.set_stroke(RED, width=5).scale(1.2),
            self.animate.set_stroke(width=0).scale(1 / 1.2),
        )

    # ---------------------------------
    # Trace Path
    # ---------------------------------

    def trace_path_on(self):
        self.trace = TracedPath(self.get_center, stroke_color=self.get_color())
        return self.trace

    def trace_path_off(self):
        if self.trace:
            return FadeOut(self.trace)
        return Wait(0)

    # ---------------------------------
    # Label
    # ---------------------------------

    def show_label(self, text, font_size=20):
        self.label = Text(text, font_size=font_size, color=TEXT_COLOR)
        self.label.next_to(self, UP, buff=0.15)
        self.add(self.label)
        return FadeIn(self.label)

    def hide_label(self):
        if self.label:
            return FadeOut(self.label)
        return Wait(0)