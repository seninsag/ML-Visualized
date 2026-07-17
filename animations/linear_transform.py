from manim import *

from core.scene_objects import SceneObjects


class LinearTransform:

    @staticmethod
    def play(
        scene,
        scene_objects: SceneObjects,
        stage,
        run_time=2.5,
    ):

        scene.play(

            scene_objects.cloud.animate_to(
                stage.points
            ),

            scene_objects.grid.animate_to(
                stage.grid
            ),

            run_time=run_time,
        )

        scene.wait(0.5)