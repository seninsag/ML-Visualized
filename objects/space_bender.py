from manim import *
import numpy as np


class SpaceBender:
    """
    Applies mathematical transformations to a FeatureSpaceGrid.
    """

    def __init__(self, grid, point_cloud=None):
        self.grid = grid
        self.point_cloud = point_cloud

    def relu_fold(self, run_time=2):
        """
        Smoothly apply ReLU:
            z -> max(0, z)
        """

        # Save original coordinates
        original_vertices = self.grid.vertex_positions.copy()

        # Save original point positions
        original_point_positions = None

        if self.point_cloud is not None:
            original_point_positions = [
                dp.get_center().copy()
                for dp in self.point_cloud.data_points
            ]

        def updater(mob, alpha):

            # Start from original geometry every frame
            vertices = original_vertices.copy()

            z = vertices[:, 2]

            # Vertices closer to z=0 start folding first.
            # Deep negative vertices fold later.
            delay = np.clip(np.abs(z) * 0.15, 0.0, 0.8)

            local_alpha = np.clip(
                (alpha - delay) / (1.0 - delay),
                0.0,
                1.0,
            )

            # Smooth interpolation
            target_z = np.maximum(0, z)

            vertices[:, 2] = (
                (1 - local_alpha) * z
                + local_alpha * target_z
            )

            mob.vertex_positions[:] = vertices
            mob.rebuild_mesh()

            # Fold the point cloud using the same ReLU transformation
            if self.point_cloud is not None:

                for dp, original in zip(
                    self.point_cloud.data_points,
                    original_point_positions
                ):

                    x, y, z = original

                    # Use the same delayed animation as the grid
                    delay = min(abs(z) * 0.15, 0.8)

                    local_alpha = np.clip(
                        (alpha - delay) / (1.0 - delay),
                        0.0,
                        1.0,
                    )

                    target_z = max(0, z)

                    new_z = (
                        (1 - local_alpha) * z
                        + local_alpha * target_z
                    )

                    dp.move_to(
                        np.array([x, y, new_z])
                    )


        return UpdateFromAlphaFunc(
            self.grid,
            updater,
            run_time=run_time,
        )