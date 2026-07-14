from manim import *

from ml.feature_space import FeatureSpace
from datasets.xor import XOR
from ml.decision_boundary import DecisionBoundary
from engine.theme import BOUNDARY_COLOR


class Scene02(Scene):

    def construct(self):

        # ---------------------------------
        # Continue from Scene 1
        # ---------------------------------

        feature_space = FeatureSpace()
        feature_space.shift(DOWN * 0.25)

        dataset = XOR()
        dataset.shift(DOWN * 0.25)

        boundary = DecisionBoundary(angle=18)
        boundary.shift(DOWN * 0.25)
        boundary.set_color(BOUNDARY_COLOR)

        self.add(feature_space, dataset, boundary)

        self.wait(1)

        # ==========================================================
        # Hypothesis 1
        # ==========================================================

        self.play(boundary.rotate_to(12), run_time=0.35)
        self.wait(0.2)

        self.play(boundary.animate.shift(RIGHT * 0.10), run_time=0.25)
        self.wait(0.4)

        self.play(boundary.rotate_to(6), run_time=0.4)
        self.wait(0.2)

        self.play(boundary.animate.shift(LEFT * 0.08), run_time=0.25)
        self.wait(0.6)

        # ==========================================================
        # Hypothesis 2
        # ==========================================================

        self.play(boundary.rotate_to(-28), run_time=0.6)
        self.wait(0.25)

        self.play(
            boundary.animate.shift(
                LEFT * 0.22 + DOWN * 0.08
            ),
            run_time=0.35,
        )

        self.wait(0.7)

        self.play(boundary.rotate_to(-38), run_time=0.45)
        self.wait(0.2)

        self.play(
            boundary.animate.shift(
                LEFT * 0.10 + DOWN * 0.10
            ),
            run_time=0.30,
        )

        self.wait(0.8)

        # ==========================================================
        # Hypothesis 3
        # ==========================================================

        self.play(boundary.rotate_to(15), run_time=0.6)
        self.wait(0.2)

        self.play(
            boundary.animate.shift(RIGHT * 0.12),
            run_time=0.30,
        )

        self.wait(0.8)

        # ==========================================================
        # Final Confirmation
        # ==========================================================

        self.play(boundary.rotate_to(18), run_time=0.45)
        self.wait(0.2)

        self.play(
            boundary.animate.shift(
                LEFT * 0.04 + UP * 0.05
            ),
            run_time=0.25,
        )

        self.wait(2)

        # ==========================================================
        # Search Failed
        # ==========================================================

        self.play(boundary.failure(), run_time=1.2)

        self.wait(2)

        self.play(
            FadeOut(feature_space),
            run_time=1.2,
        )

        self.wait(1)

        self.play(
            FadeOut(boundary),
            run_time=0.7,
        )

        self.wait(0.15)

        # ==========================================================
        # Draw attention to XOR points
        # ==========================================================

        self.play(
            AnimationGroup(
                *[
                    point.animate.scale(1.15)
                    for point in dataset.data_points
                ],
                lag_ratio=0.08,
            ),
            run_time=0.6,
        )

        self.play(
            AnimationGroup(
                *[
                    point.animate.scale(1 / 1.15)
                    for point in dataset.data_points
                ],
                lag_ratio=0.08,
            ),
            run_time=0.45,
        )

        self.wait(0.35)

        # ==========================================================
        # Ending Message
        # ==========================================================

        message1 = Text(
            "No straight line can\nseparate this dataset.",
            font_size=26,
            t2c={
                "straight line": BOUNDARY_COLOR,
            },
        )

        message1.move_to(UP * 2.6)

        message2 = Text(
            "What makes this\ndataset different?",
            font_size=28,
        )

        # Center of the XOR dataset
        message2.move_to(DOWN * 0.30)

        # ---------------------------------
        # Show statement
        # ---------------------------------

        self.play(
            FadeIn(message1),
            run_time=1,
        )

        self.wait(0.55)

        # ---------------------------------
        # Show question
        # ---------------------------------

        self.play(
            FadeIn(message2),
            run_time=1.2,
        )

        self.wait(2.5)

        # ---------------------------------
        # End of Chapter 1
        # ---------------------------------

        self.play(
            FadeOut(message1),
            FadeOut(message2),
            FadeOut(dataset),
            run_time=1.5,
        )

        self.wait()
