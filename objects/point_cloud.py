from manim import *
import numpy as np
from objects.data_point_3d import DataPoint3D
from engine.theme import *


class PointCloud(VGroup):
    """
    Collection of DataPoint3D objects with batch operations.
    Replaces Dataset for 3D scenes.
    """

    def __init__(self, points=None, colors=None):
        super().__init__()

        self.data_points = []
        points = points or []

        if colors is None:
            colors = [CLASS_BLUE] * len(points)

        for point, color in zip(points, colors):
            dp = DataPoint3D(point, color)
            self.data_points.append(dp)
            self.add(dp)

    # ---------------------------------
    # Factory Methods
    # ---------------------------------

    @classmethod
    def from_dataset(cls, red_points, blue_points):
        points = red_points + blue_points
        colors = [CLASS_RED] * len(red_points) + [CLASS_BLUE] * len(blue_points)
        return cls(points, colors)

    @classmethod
    def from_coordinates(cls, coords, colors):
        return cls(coords, colors)

    # ---------------------------------
    # Batch Animations
    # ---------------------------------

    def animate_in(self):
        return LaggedStart(
            *[dp.animate_in() for dp in self.data_points],
            lag_ratio=0.2,
        )

    def animate_to(self, target_coords, run_time=2):

        if len(target_coords) != len(self.data_points):
            raise ValueError(
                f"Expected {len(self.data_points)} coordinates, "
                f"got {len(target_coords)}."
            )

        animations = []

        for dp, coord in zip(self.data_points, target_coords):
            animations.append(dp.move_to_coordinate(coord))

        return AnimationGroup(
            *animations,
            lag_ratio=0,
            run_time=run_time
        )

    def fade_all(self):
        return AnimationGroup(*[dp.fade() for dp in self.data_points])

    def restore_all(self):
        return AnimationGroup(*[dp.restore() for dp in self.data_points])

    # ---------------------------------
    # Highlighting
    # ---------------------------------

    def highlight_cluster(self, indices):
        return AnimationGroup(*[self.data_points[i].highlight() for i in indices])

    def highlight_point(self, index):
        return self.data_points[index].highlight()

    def fade_dim_all(self):
        return AnimationGroup(*[dp.fade_dim() for dp in self.data_points])

    def restore_state_all(self):
        return AnimationGroup(*[dp.restore_state() for dp in self.data_points])

    # ---------------------------------
    # Color
    # ---------------------------------

    def change_colors(self, colors):
        animations = []
        for dp, color in zip(self.data_points, colors):
            animations.append(dp.change_color(color))
        return AnimationGroup(*animations)

    # ---------------------------------
    # Geometry
    # ---------------------------------

    def get_centroid(self):
        coords = [dp.get_center() for dp in self.data_points]
        return np.mean(coords, axis=0)

    def connect_lines(self, indices_pairs):
        lines = VGroup()
        for i, j in indices_pairs:
            line = Line(
                self.data_points[i].get_center(),
                self.data_points[j].get_center(),
                color=GREY,
                stroke_width=1,
            )
            lines.add(line)
        return lines

    # ---------------------------------
    # Trace (for later)
    # ---------------------------------

    def trace_all_on(self):
        traces = VGroup()
        for dp in self.data_points:
            trace = dp.trace_path_on()
            traces.add(trace)
        return traces

    def trace_all_off(self):
        return AnimationGroup(*[dp.trace_path_off() for dp in self.data_points])