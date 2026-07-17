from manim import *
import numpy as np
from engine.theme import *


class FeatureSpaceGrid(VGroup):
    """
    Deformable mesh grid for visualizing feature space transformations.
    Handles coordinate conversion internally via coordinate_mapper.
    """

    def __init__(
        self,
        grid_data=None,
        x_range=(-3, 3),
        y_range=(-3, 3),
        steps=10,
        coordinate_mapper=None,
    ):
        super().__init__()

        self.h_lines = VGroup()
        self.v_lines = VGroup()
        self.fold_indicator = None

        if grid_data is not None:
            self._build_from_grid_data(grid_data)
        else:
            self.x_range = x_range
            self.y_range = y_range
            self.steps = steps
            self.coordinate_mapper = coordinate_mapper or (
                lambda x, y, z=0: [x, y, z]
            )

            self.x_vals = np.linspace(x_range[0], x_range[1], steps)
            self.y_vals = np.linspace(y_range[0], y_range[1], steps)

            self._generate_mesh()

    def _build_from_grid_data(self, grid_data):

        rows, cols = grid_data["shape"]
        points = grid_data["points"]

        self.rows = rows
        self.cols = cols

        # Source of truth
        self.vertex_positions = np.array(points, dtype=float)

        # Horizontal lines
        for r in range(rows):

            start = r * cols
            end = start + cols

            line = VMobject()
            line.set_points_as_corners(points[start:end])
            line.set_stroke(
                GRID_COLOR,
                opacity=GRID_OPACITY,
                width=GRID_WIDTH,
            )

            self.h_lines.add(line)
            self.add(line)

        # Vertical lines
        for c in range(cols):

            column_points = [
                points[r * cols + c]
                for r in range(rows)
            ]

            line = VMobject()
            line.set_points_as_corners(column_points)
            line.set_stroke(
                GRID_COLOR,
                opacity=GRID_OPACITY,
                width=GRID_WIDTH,
            )

            self.v_lines.add(line)
            self.add(line)
    # ---------------------------------
    # Generation
    # ---------------------------------

    def _generate_mesh(self):

        self.rows = self.steps
        self.cols = self.steps

        self.vertex_positions = np.array(
            [
                self.coordinate_mapper(x, y)
                for y in self.y_vals
                for x in self.x_vals
            ],
            dtype=float,
        )

        for y in self.y_vals:
            points = [self.coordinate_mapper(x, y) for x in self.x_vals]
            line = VMobject()
            line.set_points_as_corners(points)
            line.set_stroke(GRID_COLOR, opacity=GRID_OPACITY, width=GRID_WIDTH)
            self.h_lines.add(line)
            self.add(line)

        for x in self.x_vals:
            points = [self.coordinate_mapper(x, y) for y in self.y_vals]
            line = VMobject()
            line.set_points_as_corners(points)
            line.set_stroke(GRID_COLOR, opacity=GRID_OPACITY, width=GRID_WIDTH)
            self.v_lines.add(line)
            self.add(line)

    # ---------------------------------
    # Transform
    # ---------------------------------

    def animate_to(self, grid_data, run_time=2):
        """
        Smoothly interpolate the grid geometry to a new set of vertices.
        """

        rows, cols = grid_data["shape"]
        target_vertices = np.array(grid_data["points"], dtype=float)

        # Save current geometry
        original_vertices = self.vertex_positions.copy()

        # Update metadata
        self.rows = rows
        self.cols = cols

        def updater(mob, alpha):

            vertices = (
                (1 - alpha) * original_vertices
                + alpha * target_vertices
            )

            mob.vertex_positions[:] = vertices
            mob.rebuild_mesh()

        return UpdateFromAlphaFunc(
            self,
            updater,
            run_time=run_time,
        )

    # ---------------------------------
    # Wireframe Toggle
    # ---------------------------------

    def show_wireframe(self):
        return self.animate.set_opacity(GRID_OPACITY)

    def hide_wireframe(self):
        return self.animate.set_opacity(0)

    # ---------------------------------
    # Fold Highlight
    # ---------------------------------

    def highlight_fold(self, start, end, color=YELLOW, width=4):
        self.fold_indicator = Line(start, end, color=color, stroke_width=width)
        self.add(self.fold_indicator)
        return FadeIn(self.fold_indicator)

    def hide_fold(self):
        if self.fold_indicator:
            return FadeOut(self.fold_indicator)
        return Wait(0)

    # ---------------------------------
    # Geometry
    # ---------------------------------

    def rebuild_mesh(self):
        """
        Rebuild all grid lines from self.vertex_positions.
        """

        # Horizontal lines
        for r, line in enumerate(self.h_lines):
            start = r * self.cols
            end = start + self.cols
            line.set_points_as_corners(
                self.vertex_positions[start:end]
            )

        # Vertical lines
        for c, line in enumerate(self.v_lines):

            column = [
                self.vertex_positions[r * self.cols + c]
                for r in range(self.rows)
            ]

            line.set_points_as_corners(column)

    # ---------------------------------
    # State
    # ---------------------------------

    def reset(self):
        if self.fold_indicator:
            self.remove(self.fold_indicator)
        self.remove(*self.h_lines, *self.v_lines)
        self.h_lines = VGroup()
        self.v_lines = VGroup()
        self.fold_indicator = None
        self._generate_mesh()
        return self

    def copy_state(self):
        return self.copy()