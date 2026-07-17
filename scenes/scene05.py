from manim import *

from objects.representation_sequence import RepresentationSequence
from builders.scene_builder import SceneBuilder

from animations.intro import IntroAnimation
from animations.linear_transform import LinearTransform
from animations.relu_activation import ReLUActivation


class Scene05(ThreeDScene):

    def construct(self):

        # ---------------------------------------------------------
        # Load exported representations
        # ---------------------------------------------------------

        rep = RepresentationSequence(
            "data/representations.json"
        )

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
        # Build Scene
        # ---------------------------------------------------------

        scene_objects = SceneBuilder.from_representation(
            rep,
            stage_name="input",
        )

        # Optional override
        scene_objects.plane.set_fill(opacity=0.05)


        # ---------------------------------------------------------
        # Intro
        # ---------------------------------------------------------

        IntroAnimation.play(
            self,
            scene_objects,
        )

        # ---------------------------------------------------------
        # Linear Layer
        # ---------------------------------------------------------

        LinearTransform.play(
            self,
            scene_objects,
            linear_stage,
        )

        # ---------------------------------------------------------
        # ReLU Activation
        # ---------------------------------------------------------

        ReLUActivation.play(
            self,
            scene_objects,
        )

        self.wait(2)