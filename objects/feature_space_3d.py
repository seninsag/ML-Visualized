from manim import *
import numpy as np

from engine.theme import *


class FeatureSpace3D(VGroup):
    """
    Minimal 3D feature space.

    Uses three Line3D objects instead of ThreeDAxes so the axes
    match the visual style of previous scenes while remaining true
    3D objects that work with camera movement.
    """

    def __init__(
        self,
        x_range=(-4, 4),
        y_range=(-4, 4),
        z_range=(-2, 2),
        x_length=8,
        y_length=8,
        z_length=4,
    ):
        super().__init__()

        self.x_range = x_range
        self.y_range = y_range
        self.z_range = z_range

        self.x_length = x_length
        self.y_length = y_length
        self.z_length = z_length

        self.x_axis = None
        self.y_axis = None
        self.z_axis = None

        self.axes = None

        self.labels = VGroup()
        self.x_label = None
        self.y_label = None
        self.z_label = None

        self.title = None
        self.grid = None
        self.grid_steps = None

    # ---------------------------------------------------------
    # Axes
    # ---------------------------------------------------------

    def create_axes(self):

        self.x_axis = Line3D(
            start=LEFT * self.x_length / 2,
            end=RIGHT * self.x_length / 2,
            thickness=0.015,
            color=AXIS_COLOR,
        )

        self.y_axis = Line3D(
            start=DOWN * self.y_length / 2,
            end=UP * self.y_length / 2,
            thickness=0.015,
            color=AXIS_COLOR,
        )

        self.z_axis = Line3D(
            start=IN * self.z_length / 2,
            end=OUT * self.z_length / 2,
            thickness=0.015,
            color=AXIS_COLOR,
        )

        self.axes = VGroup(
            self.x_axis,
            self.y_axis,
            self.z_axis,
        )

        self.add(self.axes)

        return self

    # ---------------------------------------------------------
    # Labels
    # ---------------------------------------------------------

    def create_labels(self):

        self.x_label = Text(
            "X",
            font_size=24,
            color=AXIS_COLOR,
        )

        self.y_label = Text(
            "Y",
            font_size=24,
            color=AXIS_COLOR,
        )

        self.z_label = Text(
            "Z",
            font_size=24,
            color=AXIS_COLOR,
        )

        self.x_label.next_to(
            self.x_axis.get_end(),
            RIGHT,
            buff=0.15,
        )

        self.y_label.next_to(
            self.y_axis.get_end(),
            UP,
            buff=0.15,
        )

        self.z_label.next_to(
            self.z_axis.get_end(),
            OUT,
            buff=0.15,
        )

        self.labels.add(
            self.x_label,
            self.y_label,
            self.z_label,
        )

        self.add(self.labels)

        return self

    def animate_labels(self):

        return AnimationGroup(
            FadeIn(self.x_label),
            FadeIn(self.y_label),
            FadeIn(self.z_label),
        )

    # ---------------------------------------------------------
    # Grid
    # ---------------------------------------------------------

    def create_grid(self, steps=10):

        from objects.feature_space_grid import FeatureSpaceGrid

        self.grid_steps = steps

        self.grid = FeatureSpaceGrid(
            x_range=self.x_range,
            y_range=self.y_range,
            steps=steps,
        )

        self.add(self.grid)

        return self

    # ---------------------------------------------------------
    # Title
    # ---------------------------------------------------------

    def show_title(
        self,
        text,
        font_size=30,
        edge=UP,
        buff=0.35,
    ):

        self.title = Text(
            text,
            font_size=font_size,
            color=TEXT_COLOR,
        )

        self.title.to_edge(
            edge,
            buff=buff,
        )

        self.add(self.title)

        return FadeIn(self.title)

    def hide_title(self):

        if self.title:

            return FadeOut(self.title)

        return Wait()

    # ---------------------------------------------------------
    # Entrance
    # ---------------------------------------------------------

    def animate_in(self):

        animations = [
            Create(self.x_axis),
            Create(self.y_axis),
            GrowFromPoint(
                self.z_axis,
                ORIGIN,
            ),
        ]

        if self.grid:

            animations.append(
                FadeIn(self.grid)
            )

        if len(self.labels):

            animations.append(
                FadeIn(self.labels)
            )

        return AnimationGroup(
            *animations,
            lag_ratio=0.15,
        )

    def fade_out(self):

        return FadeOut(self)

    # ---------------------------------------------------------
    # Coordinate conversion
    # ---------------------------------------------------------

    def coords(self, *args):

        return self.coords_to_point(*args)

    def coords_to_point(
        self,
        x,
        y,
        z=0,
    ):
        """
        Data coordinates -> Manim coordinates.

        Current ranges map 1:1 to scene units.
        """

        return np.array([x, y, z])

    def point_to_coords(self, point):

        return point

    # ---------------------------------------------------------
    # Accessors
    # ---------------------------------------------------------

    def get_axes(self):

        return self.axes

    def get_grid(self):

        return self.grid

    def get_origin(self):

        return ORIGIN

    def get_bounds(self):

        return (
            self.x_range,
            self.y_range,
            self.z_range,
        )