from manim import *
from engine.theme import *


class FeatureSpace3D(VGroup):
    """
    3D feature space with configurable axes, grid, and coordinate conversion.
    Wraps ThreeDAxes with the project's visual style.
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

        self.axes = None
        self.x_label = None
        self.y_label = None
        self.z_label = None
        self.labels = VGroup()
        self.title = None
        self.grid = None
        self.grid_steps = None

    # ---------------------------------
    # Axes
    # ---------------------------------

    def create_axes(self):
        self.axes = ThreeDAxes(
            x_range=[self.x_range[0], self.x_range[1], 1],
            y_range=[self.y_range[0], self.y_range[1], 1],
            z_range=[self.z_range[0], self.z_range[1], 1],
            x_length=self.x_length,
            y_length=self.y_length,
            z_length=self.z_length,
            axis_config={"include_tip": True, "include_numbers": False},
        )

        self.axes.x_axis.set_color(AXIS_X_COLOR)
        self.axes.y_axis.set_color(AXIS_Y_COLOR)
        self.axes.z_axis.set_color(AXIS_Z_COLOR)

        self.add(self.axes)
        return self

    # ---------------------------------
    # Labels
    # ---------------------------------

    def create_labels(self):
        if self.axes is None:
            raise RuntimeError("Axes have not been created. Call create_axes() first.")

        self.x_label = Text("X", color=AXIS_X_COLOR, font_size=24)
        self.y_label = Text("Y", color=AXIS_Y_COLOR, font_size=24)
        self.z_label = Text("Z", color=AXIS_Z_COLOR, font_size=24)

        self.x_label.next_to(self.axes.x_axis.get_end(), DOWN)
        self.y_label.next_to(self.axes.y_axis.get_end(), RIGHT)
        self.z_label.next_to(self.axes.z_axis.get_end(), OUT)

        self.labels.add(self.x_label, self.y_label, self.z_label)
        self.add(self.labels)

        return self

    def animate_labels(self):
        if len(self.labels) == 0:
            raise RuntimeError("Labels have not been created. Call create_labels() first.")
        return AnimationGroup(
            FadeIn(self.x_label),
            FadeIn(self.y_label),
            FadeIn(self.z_label),
        )

    # ---------------------------------
    # Title
    # ---------------------------------

    def show_title(self, text, font_size=30, edge=UP, buff=0.35):
        self.title = Text(text, font_size=font_size, color=TEXT_COLOR)
        self.title.to_edge(edge, buff=buff)
        self.add(self.title)
        return FadeIn(self.title)

    def hide_title(self):
        return FadeOut(self.title) if self.title else Wait(0)

    # ---------------------------------
    # Grid
    # ---------------------------------

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

    # ---------------------------------
    # Entrance / Exit
    # ---------------------------------

    def animate_in(self):
        animations = []
        if self.axes:
            animations.append(Create(self.axes))
        if self.grid:
            animations.append(FadeIn(self.grid))
        if len(self.labels) > 0:
            animations.append(FadeIn(self.labels))
        return AnimationGroup(*animations, lag_ratio=0.1)

    def fade_out(self):
        return FadeOut(self)

    # ---------------------------------
    # Coordinate Conversion
    # ---------------------------------

    def coords(self, *args):
        return self.coords_to_point(*args)

    def coords_to_point(self, x, y, z=0):
        if self.axes is None:
            raise RuntimeError("Axes have not been created. Call create_axes() first.")
        return self.axes.coords_to_point(x, y, z)

    def point_to_coords(self, point):
        if self.axes is None:
            raise RuntimeError("Axes have not been created. Call create_axes() first.")
        return self.axes.point_to_coords(point)

    # ---------------------------------
    # Accessors
    # ---------------------------------

    def get_axes(self):
        return self.axes

    def get_grid(self):
        return self.grid

    def get_origin(self):
        return self.coords(0, 0, 0)

    def get_bounds(self):
        return (self.x_range, self.y_range, self.z_range)

    # ---------------------------------
    # Range Changes
    # ---------------------------------

    def change_ranges(self, x_range=None, y_range=None, z_range=None):
        if x_range:
            self.x_range = x_range
        if y_range:
            self.y_range = y_range
        if z_range:
            self.z_range = z_range
        return self.rebuild()

    def rebuild(self):
        self.remove(self.axes, self.labels, self.grid)
        self.axes = None
        self.x_label = None
        self.y_label = None
        self.z_label = None
        self.labels = VGroup()
        self.grid = None

        self.create_axes()
        self.create_labels()

        if self.grid_steps is not None:
            self.create_grid(self.grid_steps)

        return self