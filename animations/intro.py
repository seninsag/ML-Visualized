from manim import *

from core.scene_objects import SceneObjects


class IntroAnimation:

    @staticmethod
    def play(
        scene,
        scene_objects: SceneObjects,
    ):

        scene.play(
            Create(scene_objects.axes),
            run_time=1,
        )

        scene.play(
            Create(scene_objects.grid),
            run_time=1.2,
        )

        # ---------------- Caption ---------------- #

        caption = Text(
            "Let's transform the data instead.",
            font_size=36,
        )

        caption.to_edge(UP, buff=0.6)

        scene.add_fixed_in_frame_mobjects(caption)

        scene.play(
            FadeIn(caption),
            run_time=0.5,
        )

        # ---------------- Data ---------------- #

        scene.play(
            scene_objects.cloud.animate_in(),
            run_time=1.5,
        )

        scene.wait(0.8)

        scene.play(
            FadeOut(caption),
            run_time=0.4,
        )

        scene.remove_fixed_in_frame_mobjects(caption)

        scene.wait(0.5)