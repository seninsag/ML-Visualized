from manim import *

from core.scene_objects import SceneObjects
from objects.space_bender import SpaceBender


class ReLUActivation:

    @staticmethod
    def play(
        scene,
        scene_objects: SceneObjects,
        run_time=4,
    ):

        scene.play(
            FadeIn(scene_objects.plane),
            run_time=0.6,
        )

        scene.play(
            scene_objects.plane.animate.set_fill(
                opacity=0.15
            ),
            run_time=0.3,
        )

        scene.play(
            scene_objects.plane.animate.set_fill(
                opacity=0.05
            ),
            run_time=0.3,
        )

        scene.wait(0.25)

        bender = SpaceBender(
            scene_objects.grid,
            scene_objects.cloud,
        )

        scene.play(
            bender.relu_fold(
                run_time=run_time
            )
        )

        scene.play(
            FadeOut(scene_objects.plane),
            run_time=0.6,
        )

        scene.wait(1)