from manim import *

from ml.feature_space import FeatureSpace
from datasets.easy import Easy
from datasets.xor import XOR
from ml.decision_boundary import DecisionBoundary
from engine.theme import BOUNDARY_COLOR


class Scene01(Scene):

    def construct(self):

        # ---------------------------------
        # Question
        # ---------------------------------

        question = Text(
            "Can a straight line\nseparate every dataset?",
            font_size=42,
        )

        self.play(
            FadeIn(question),
            run_time=2,
        )

        self.wait(2)

        self.play(
            question.animate.scale(0.65).to_edge(UP, buff=0.25),
            run_time=1.5,
        )

        # ---------------------------------
        # Feature Space
        # ---------------------------------

        feature_space = FeatureSpace()
        feature_space.shift(DOWN * 0.25)

        self.play(
            Create(feature_space),
            run_time=2,
        )

        # ---------------------------------
        # Easy Dataset
        # ---------------------------------

        dataset = Easy()
        dataset.shift(DOWN * 0.25)

        self.play(
            dataset.animate_in(),
            run_time=2,
        )

        self.wait(0.8)

        # ---------------------------------
        # Separator
        # ---------------------------------

        boundary = DecisionBoundary(angle=18)
        boundary.shift(DOWN * 0.25)

        self.play(
            Create(boundary),
            run_time=1.3,
        )

        self.wait(0.5)

        self.play(
            boundary.success(),
            run_time=0.8,
        )

        self.wait(1)

        # ---------------------------------
        # Rearrange the data
        # ---------------------------------

        rearrange = Text(
            "What if we arrange the data differently?",
            font_size=30,
        )

        rearrange.to_edge(DOWN, buff=0.25)

        self.play(
            FadeIn(rearrange),
            run_time=0.8,
        )

        self.wait(1)

        self.play(
            dataset.fade_points([1, 4]),
            run_time=1.5,
        )

        self.wait(0.5)

        self.play(
            FadeOut(rearrange),
            boundary.animate.set_color(BOUNDARY_COLOR),
            run_time=0.6,
        )

        # ---------------------------------
        # Morph into XOR
        # ---------------------------------

        xor = XOR()
        xor.shift(DOWN * 0.25)

        self.play(
            dataset.morph_selected(
                indices=[0, 2, 3, 5],
                target_dataset=xor,
            ),
            run_time=2,
        )

        # Let the audience absorb the new arrangement
        self.wait(1.2)

        # The opening question has served its purpose
        self.play(
            FadeOut(question),
            run_time=0.8,
        )

        self.wait(0.4)