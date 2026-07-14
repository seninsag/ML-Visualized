from manim import *

from ml.feature_space import FeatureSpace
from datasets.xor import XOR


class Scene01(Scene):

    def construct(self):

        # -----------------------------
        # Question
        # -----------------------------
        question = Text(
            "Can a straight line\nseparate every dataset?",
            font_size=42
        )

        self.play(FadeIn(question), run_time=2)
        self.wait(2)

        self.play(
            question.animate.scale(0.65).to_edge(UP, buff=0.6),
            run_time=1.5,
        )

        # -----------------------------
        # Feature Space
        # -----------------------------
        feature_space = FeatureSpace()
        feature_space.shift(DOWN * 0.7)

        self.play(
            Create(feature_space),
            run_time=2,
        )

        # -----------------------------
        # Dataset
        # -----------------------------
        dataset = XOR()
        dataset.shift(DOWN * 0.7)

        self.play(
            dataset.animate_in(),
            run_time=2,
        )

        self.wait(2)