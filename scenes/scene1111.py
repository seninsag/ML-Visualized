from manim import *

from objects.representation_sequence import RepresentationSequence
from objects.feature_space_3d import FeatureSpace3D
from objects.feature_space_grid import FeatureSpaceGrid
from objects.point_cloud import PointCloud
from objects.space_bender import SpaceBender
from objects.activation_plane import ActivationPlane


class FoldPrototype(ThreeDScene):

    def construct(self):

        # ---------------------------------------------------------
        # Load exported representations
        # ---------------------------------------------------------

        rep = RepresentationSequence(
            "data/representations.json"
        )

        input_stage = rep.get("input")
        linear_stage = rep.get("linear1")

        # ---------------------------------------------------------
        # Camera
        # ---------------------------------------------------------

        self.set_camera_orientation(
            phi=70 * DEGREES,
            theta=-45 * DEGREES,
            zoom=1.0,
        )

        # ---------------------------------------------------------
        # Scene Objects
        # ---------------------------------------------------------

        axes = FeatureSpace3D()

        plane = ActivationPlane()
        plane.set_fill(opacity=0.18)

        grid = FeatureSpaceGrid(
            grid_data=input_stage.grid
        )

        cloud = PointCloud(
            input_stage.points,
            colors=rep.dataset["colors"]
        )

        # ---------------------------------------------------------
        # Build Scene
        # ---------------------------------------------------------

        self.play(Create(axes), run_time=1.0)

        self.play(Create(grid), run_time=1.2)

        self.play(
            cloud.animate_in(),
            run_time=1.5
        )

        self.wait(0.5)

        # ---------------------------------------------------------
        # Linear Transformation
        # ---------------------------------------------------------

        self.play(

            cloud.animate_to(
                linear_stage.points
            ),

            grid.animate_to(
                linear_stage.grid
            ),

            run_time=2.5

        )

        # Let students observe the transformed feature space
        self.wait(0.5)

        # ---------------------------------------------------------
        # Activation Plane
        # ---------------------------------------------------------

        self.play(
            FadeIn(plane),
            run_time=0.6
        )

        # Small pulse to attract attention
        self.play(
            plane.animate.set_fill(opacity=0.40),
            run_time=0.25
        )

        self.play(
            plane.animate.set_fill(opacity=0.18),
            run_time=0.25
        )

        self.wait(0.25)

        # ---------------------------------------------------------
        # ReLU Fold
        # ---------------------------------------------------------

        bender = SpaceBender(
            grid,
            cloud
        )

        self.play(
            bender.relu_fold(run_time=4)
        )

        # ---------------------------------------------------------
        # Remove Plane
        # ---------------------------------------------------------

        self.play(
            FadeOut(plane),
            run_time=0.6
        )

        self.wait(2)