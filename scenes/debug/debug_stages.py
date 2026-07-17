from manim import *

from objects.representation_sequence import RepresentationSequence
from objects.feature_space_grid import FeatureSpaceGrid
from objects.point_cloud import PointCloud
from objects.feature_space_3d import FeatureSpace3D


class DebugStages(ThreeDScene):

    def construct(self):

        rep = RepresentationSequence("data/representations.json")

        self.set_camera_orientation(
            phi=70 * DEGREES,
            theta=-45 * DEGREES,
            zoom=1
        )

        axes = FeatureSpace3D()

        self.add(axes)

        # -----------------------
        # CHANGE THIS NAME
        # -----------------------

        stage = rep.get("relu")

        grid = FeatureSpaceGrid(stage.grid)

        cloud = PointCloud(
            stage.points,
            colors=rep.dataset["colors"]
        )

        self.add(grid)
        self.add(cloud)

        self.wait()