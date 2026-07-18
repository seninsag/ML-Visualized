from manim import *

from core.scene_objects import SceneObjects
from objects.space_bender import SpaceBender
from ml.decision_boundary import DecisionBoundary


class ReLUActivation:

    @staticmethod
    def play(
        scene,
        scene_objects: SceneObjects,
        run_time=4,
    ):

        # ---------------------------------------------------------
        # Caption 1
        # ---------------------------------------------------------

        caption = Text(
            "Neural networks do this using activation functions.",
            font_size=34,
        ).to_edge(DOWN, buff=0.5)

        scene.add_fixed_in_frame_mobjects(caption)

        scene.play(
            FadeIn(caption),
            run_time=0.5,
        )

        # Give viewers time to read
        scene.wait(2.3)

        # ---------------------------------------------------------
        # Caption 2
        # ---------------------------------------------------------

        scene.play(
            FadeOut(caption),
            run_time=0.3,
        )

        scene.remove_fixed_in_frame_mobjects(caption)

        caption = Text(
            "Watch what ReLU does.",
            font_size=34,
        ).to_edge(DOWN, buff=0.5)

        scene.add_fixed_in_frame_mobjects(caption)

        scene.play(
            FadeIn(caption),
            run_time=0.3,
        )

        # Small pause before the fold starts
        scene.wait(0.9)

        # ---------------------------------------------------------
        # ReLU Folding
        # ---------------------------------------------------------

        bender = SpaceBender(
            scene_objects.grid,
            scene_objects.cloud,
        )

        scene.play(
            bender.relu_fold(
                run_time=run_time
            )
        )

        # Let viewers observe the transformed space
        scene.wait(0.8)

        # ---------------------------------------------------------
        # Decision Boundary
        # ---------------------------------------------------------

        decision_boundary = DecisionBoundary.from_cloud(
            scene_objects.cloud
        )

        scene.play(
            FadeIn(
                decision_boundary,
                scale=0.9,
            ),
            run_time=1.2,
        )

        # Let viewers notice the separator before changing caption
        scene.wait(0.8)

        # ---------------------------------------------------------
        # Final Caption
        # ---------------------------------------------------------

        scene.play(
            FadeOut(caption),
            run_time=0.3,
        )

        scene.remove_fixed_in_frame_mobjects(caption)

        caption = Text(
            "Now, a linear classifier can separate the classes.",
            font_size=34,
        ).to_edge(DOWN, buff=0.5)

        scene.add_fixed_in_frame_mobjects(caption)

        scene.play(
            decision_boundary.success(),
            FadeIn(caption),
            run_time=0.8,
        )

        # Let the final message sink in
        scene.wait(2.5)


        # ---------------------------------------------------------
        # Fade everything to black
        # ---------------------------------------------------------

        scene.play(
            FadeOut(scene_objects.axes),
            FadeOut(scene_objects.grid),
            FadeOut(scene_objects.cloud),
            FadeOut(decision_boundary),
            FadeOut(caption),
            run_time=1.5,
        )

        scene.remove_fixed_in_frame_mobjects(caption)

        scene.wait(0.5)