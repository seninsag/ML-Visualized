from manim import *

from ml.datapoint import DataPoint
from engine.theme import *


class Dataset(VGroup):

    def __init__(self, red_points=None, blue_points=None):
        super().__init__()

        red_points = red_points or []
        blue_points = blue_points or []

        # Store all DataPoint objects
        self.data_points = []

        # Create red points
        for point in red_points:
            data_point = DataPoint(point, CLASS_RED)
            self.data_points.append(data_point)
            self.add(data_point)

        # Create blue points
        for point in blue_points:
            data_point = DataPoint(point, CLASS_BLUE)
            self.data_points.append(data_point)
            self.add(data_point)

    # ---------------------------------
    # Entrance Animation
    # ---------------------------------

    def animate_in(self):
        return LaggedStart(
            *[
                point.animate_in()
                for point in self.data_points
            ],
            lag_ratio=0.2,
        )

    # ---------------------------------
    # Morph Into Another Dataset
    # ---------------------------------

    def morph_to(self, other_dataset):

        if len(self.data_points) != len(other_dataset.data_points):
            raise ValueError(
                "Both datasets must contain the same number of DataPoints."
            )

        animations = []

        for current, target in zip(
            self.data_points,
            other_dataset.data_points,
        ):
            animations.append(
                current.move_to_position(
                    target.get_center()
                )
            )

        return AnimationGroup(
            *animations,
            lag_ratio=0,
        )

    # ---------------------------------
    # Morph Selected Points
    # ---------------------------------

    def morph_selected(self, indices, target_dataset):

        if len(indices) != len(target_dataset.data_points):
            raise ValueError(
                "Number of selected points must match the target dataset."
            )

        animations = []

        for source_index, target_point in zip(
            indices,
            target_dataset.data_points,
        ):
            animations.append(
                self.data_points[source_index].move_to_position(
                    target_point.get_center()
                )
            )

        return AnimationGroup(
            *animations,
            lag_ratio=0,
        )

    # ---------------------------------
    # Fade Out Selected Points
    # ---------------------------------

    def fade_points(self, indices):

        return AnimationGroup(
            *[
                self.data_points[i].fade_out()
                for i in indices
            ]
        )

    # ---------------------------------
    # Highlight Selected Points
    # ---------------------------------

    def highlight_points(self, indices):

        return AnimationGroup(
            *[
                self.data_points[i].highlight()
                for i in indices
            ]
        )

    # ---------------------------------
    # Restore Selected Points
    # ---------------------------------

    def restore_points(self, indices):

        return AnimationGroup(
            *[
                self.data_points[i].restore()
                for i in indices
            ]
        )