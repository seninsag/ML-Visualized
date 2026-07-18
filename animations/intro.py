from manim import *

from core.scene_objects import SceneObjects


class IntroAnimation:

    @staticmethod
    def play(
        scene,
        scene_objects: SceneObjects,
    ):

        # ---------------------------------------------------------
        # X & Y Axes
        # ---------------------------------------------------------

        scene.play(
            AnimationGroup(
                Create(scene_objects.axes.x_axis),
                Create(scene_objects.axes.y_axis),
                lag_ratio=0.15,
            ),
            run_time=1,
        )

        # ---------------------------------------------------------
        # XOR Points
        # ---------------------------------------------------------

        scene.play(
            scene_objects.cloud.animate_in(),
            run_time=1.2,
        )

        # ---------------------------------------------------------
        # Caption
        # ---------------------------------------------------------

        caption = Text(
            "Then what if we transform the data instead?",
            font_size=36,
        )

        caption.to_edge(UP, buff=0.3)

        scene.add_fixed_in_frame_mobjects(caption)

        scene.play(
            FadeIn(caption),
            run_time=0.5,
        )

        scene.wait(0.5)

        # ---------------------------------------------------------
        # Reveal Feature Space
        # ---------------------------------------------------------

        scene.move_camera(
            phi=60 * DEGREES,
            theta=-25 * DEGREES,
            zoom=1.0,
            run_time=2.5,
        )

        scene.play(
            FadeIn(
                scene_objects.grid,
                shift=OUT * 0.3,
            ),
            run_time=0.6,
        )

        # ---------------------------------------------------------
        # Reveal Z Axis
        # ---------------------------------------------------------


        scene.play(
            GrowFromPoint(
                scene_objects.axes.z_axis,
                ORIGIN,
            ),
            run_time=0.8,
        )

        scene.wait(0.3)

        scene.play(
            FadeOut(caption),
            run_time=0.4,
        )

        scene.remove_fixed_in_frame_mobjects(caption)

        scene.wait(0.3)