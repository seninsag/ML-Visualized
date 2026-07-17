from manim import *
import numpy as np


class FeatureSpaceGrid(VGroup):
    """
    A deformable mesh grid that visualizes feature space transformations.
    Horizontal and vertical lines intersect at grid points.
    """

    def __init__(self, x_range=(-3, 3), y_range=(-3, 3), steps=10,
                 line_color=GREY, line_opacity=0.4, line_width=1):
        super().__init__()

        self.x_vals = np.linspace(x_range[0], x_range[1], steps)
        self.y_vals = np.linspace(y_range[0], y_range[1], steps)

        self.h_lines = VGroup()
        self.v_lines = VGroup()

        for y in self.y_vals:
            points = [[x, y, 0] for x in self.x_vals]
            line = VMobject()
            line.set_points_as_corners(points)
            line.set_stroke(line_color, opacity=line_opacity, width=line_width)
            self.h_lines.add(line)
            self.add(line)

        for x in self.x_vals:
            points = [[x, y, 0] for y in self.y_vals]
            line = VMobject()
            line.set_points_as_corners(points)
            line.set_stroke(line_color, opacity=line_opacity, width=line_width)
            self.v_lines.add(line)
            self.add(line)

    def transform_to(self, transform_fn, run_time=2):
        animations = []

        for line, y in zip(self.h_lines, self.y_vals):
            new_points = [transform_fn(x, y) for x in self.x_vals]
            new_line = VMobject()
            new_line.set_points_as_corners(new_points)
            animations.append(Transform(line, new_line))

        for line, x in zip(self.v_lines, self.x_vals):
            new_points = [transform_fn(x, y) for y in self.y_vals]
            new_line = VMobject()
            new_line.set_points_as_corners(new_points)
            animations.append(Transform(line, new_line))

        return AnimationGroup(*animations, lag_ratio=0)