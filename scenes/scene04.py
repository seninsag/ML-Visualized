from manim import *

from ml.feature_space import FeatureSpace
from datasets.xor import XOR
from ml.decision_boundary import DecisionBoundary
from engine.theme import *


class Scene04(Scene):

    def construct(self):

        # ==========================================================
        # Setup
        # ==========================================================

        feature_space = FeatureSpace()
        feature_space.shift(DOWN * 0.25)

        dataset = XOR()
        dataset.shift(DOWN * 0.25)

        # Neutral decision boundary
        boundary = DecisionBoundary(angle=0)
        boundary.shift(DOWN * 0.25)

        points = dataset.data_points

        # XOR ordering
        #
        # 0     3
        #
        # 2     1

        top_left = points[0]
        top_right = points[3]
        bottom_left = points[2]
        bottom_right = points[1]

        # ==========================================================
        # Error Ring (Hidden for now)
        # ==========================================================

        error_ring = Circle(
            radius=0.20,
            color=RED,
            stroke_width=5,
            fill_opacity=0,
        )

        # ==========================================================
        # Opening
        # ==========================================================

        self.play(
            FadeIn(feature_space),
            run_time=0.8,
        )

        self.play(
            FadeIn(dataset),
            run_time=0.8,
        )

        self.play(
            FadeIn(boundary),
            run_time=0.8,
        )

        caption = Text(
            "Let's find out.",
            font_size=30,
        )

        caption.to_edge(
            UP,
            buff=0.35,
        )

        self.play(
            FadeIn(caption),
            run_time=0.6,
        )

        self.wait(1)

        # ==========================================================
        # First Attempt
        # ==========================================================

        # Rotate into the first attempt
        self.play(
            boundary.rotate_to(45),
            run_time=1.2,
        )

        self.wait(0.2)

        # Fine-tune the position
        self.play(
            boundary.move_to_position(
                LEFT * 1 + DOWN * 0.25,
            ),
            run_time=0.8,
        )

        self.wait(0.5)

        # ==========================================================
        # First Mistake
        # ==========================================================

        error_ring.move_to(bottom_right)

        self.play(
            FadeIn(error_ring),
            run_time=0.4,
        )

        self.play(
            FadeOut(caption),
            run_time=0.2,
        )

        caption = Text(
            "Almost...",
            font_size=30,
        )

        caption.to_edge(
            UP,
            buff=0.35,
        )

        self.play(
            FadeIn(caption),
            run_time=0.4,
        )

        self.wait(1)

        # ==========================================================
        # Second Attempt
        # ==========================================================

        self.play(
            boundary.rotate_to(45),
            run_time=0.8,
        )

        self.wait(0.15)

        self.play(
            boundary.move_to_position(
                RIGHT * 1 + DOWN * 0.25,
            ),
            run_time=0.8,
        )

        self.wait(0.25)

        self.play(
            FadeOut(error_ring),
            run_time=0.2,
        )

        error_ring.move_to(top_left)

        self.play(
            FadeIn(error_ring),
            run_time=0.2,
        )

        self.wait(0.6)

        # ==========================================================
        # Third Attempt
        # ==========================================================

        self.play(
            boundary.rotate_to(135),
            run_time=0.8,
        )

        self.wait(0.15)

        self.play(
            boundary.move_to_position(
                LEFT * 1 + DOWN * 0.25,
            ),
            run_time=0.8,
        )

        self.wait(0.25)

        self.play(
            FadeOut(error_ring),
            run_time=0.2,
        )

        error_ring.move_to(top_right)

        self.play(
            FadeIn(error_ring),
            run_time=0.2,
        )

        self.wait(0.6)

        # ==========================================================
        # Fourth Attempt
        # ==========================================================

        self.play(
            boundary.rotate_to(135),
            run_time=0.8,
        )

        self.wait(0.15)

        self.play(
            boundary.move_to_position(
                RIGHT * 1 + DOWN * 0.25,
            ),
            run_time=0.8,
        )

        self.wait(0.25)

        self.play(
            FadeOut(error_ring),
            run_time=0.2,
        )

        error_ring.move_to(bottom_left)

        self.play(
            FadeIn(error_ring),
            run_time=0.2,
        )

        self.wait(0.8)

        # ==========================================================
        # Conclusion
        # ==========================================================

        # ==========================================================
        # Conclusion
        # ==========================================================

        self.wait(0.4)

        self.play(
            FadeOut(caption),
            run_time=0.2,
        )

        # ---------------------------------
        # Conclusion 1
        # ---------------------------------

        caption = Text(
            "Every adjustment fixes one mistake...",
            font_size=32,
        )

        caption.to_edge(
            UP,
            buff=0.35,
        )

        self.play(
            FadeIn(caption),
            run_time=0.5,
        )

        self.wait(1.3)

        self.play(
            FadeOut(caption),
            run_time=0.3,
        )

        # ---------------------------------
        # Conclusion 2
        # ---------------------------------

        caption = Text(
            "...but creates another.",
            font_size=32,
        )

        caption.to_edge(
            UP,
            buff=0.35,
        )

        self.play(
            FadeIn(caption),
            run_time=0.5,
        )

        self.wait(1.3)

        # ---------------------------------
        # End of Experiment
        # ---------------------------------

        self.play(
            FadeOut(error_ring),
            FadeOut(boundary),
            FadeOut(caption),
            run_time=0.7,
        )

        self.wait(0.2)

        # ---------------------------------
        # Final Conclusion
        # ---------------------------------

        caption = Text(
            "No straight line can separate XOR.",
            font_size=34,
            weight=BOLD,
        )

        caption.to_edge(
            UP,
            buff=0.35,
        )

        self.play(
            FadeIn(caption),
            run_time=0.7,
        )

        self.wait(2)

        self.play(
            FadeOut(feature_space),
            FadeOut(dataset),
            FadeOut(caption),
            run_time=1,
        )