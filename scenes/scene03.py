from manim import *

from ml.feature_space import FeatureSpace
from datasets.xor import XOR


class Scene03(Scene):

    def construct(self):

        # ---------------------------------
        # Feature Space
        # ---------------------------------

        feature_space = FeatureSpace()
        feature_space.shift(DOWN * 0.25)

        dataset = XOR()
        dataset.shift(DOWN * 0.25)

        # -------------------------------------------------
        # XOR Point Mapping
        #
        #        top_left (Red)      top_right (Blue)
        #
        #      bottom_left (Blue)   bottom_right (Red)
        # -------------------------------------------------

        top_left = dataset.data_points[0]
        top_right = dataset.data_points[3]
        bottom_left = dataset.data_points[2]
        bottom_right = dataset.data_points[1]

        caption = Text(
            "Let's look at the data.",
            font_size=26,
        )

        caption.to_edge(
            UP,
            buff=0.35,
        )

        # ---------------------------------
        # Fade In
        # ---------------------------------

        self.play(
            FadeIn(feature_space),
            FadeIn(dataset),
            run_time=1.5,
        )

        self.wait(0.5)

        self.play(
            FadeIn(caption),
            run_time=0.8,
        )

        self.wait(2)

        # ==========================================================
        # Beat 1
        # ==========================================================

        self.play(
            FadeOut(caption),
            run_time=0.35,
        )

        caption = Text(
            "Consider this red point.",
            font_size=26,
        )

        caption.to_edge(
            UP,
            buff=0.35,
        )

        others = [
            top_right,
            bottom_left,
            bottom_right,
        ]

        self.play(
            FadeIn(caption),

            top_left.highlight(),

            *[
                point.animate.set_opacity(0.35)
                for point in others
            ],

            run_time=0.8,
        )

        self.wait(2)

        # ==========================================================
        # Beat 2
        # ==========================================================

        self.play(
            FadeOut(caption),
            run_time=0.3,
        )

        caption = Text(
            "Notice its neighbors.",
            font_size=26,
        )

        caption.to_edge(
            UP,
            buff=0.35,
        )

        self.play(

            FadeIn(caption),

            top_right.animate
                .set_opacity(1)
                .scale(1.15),

            bottom_left.animate
                .set_opacity(1)
                .scale(1.15),

            run_time=0.8,
        )

        self.wait(2)
        
        # ==========================================================
        # Beat 3
        # ==========================================================

        self.play(
            FadeOut(caption),
            run_time=0.3,
        )

        caption = Text(
            "Now look for another red point.",
            font_size=26,
        )

        caption.to_edge(
            UP,
            buff=0.35,
        )

        # Step 1
        # Remove emphasis from the blue neighbors

        self.play(

            FadeIn(caption),

            top_right.fade_dim(),
            bottom_left.fade_dim(),

            run_time=0.6,
        )

        self.wait(0.4)

        # Step 2
        # Reveal the second red point

        self.play(
            bottom_right.focus(),
            run_time=0.6,
        )

        self.wait(2)
        
        # ==========================================================
        # Beat 4
        # ==========================================================

        self.play(
            FadeOut(caption),
            run_time=0.3,
        )

        caption = Text(
            "The same pattern appears again.",
            font_size=26,
        )

        caption.to_edge(
            UP,
            buff=0.35,
        )

        self.play(

            FadeIn(caption),

            # Red points return to normal
            top_left.restore(),
            bottom_right.restore(),

            # Blue points become the new focus
            top_right.focus(),
            bottom_left.focus(),

            run_time=0.9,
        )

        self.wait(2)

        # ==========================================================
        # Beat 5
        # Reveal the hidden pattern
        # ==========================================================

        self.play(
            FadeOut(caption),
            run_time=0.3,
        )

        caption = Text(
            "Points of the same class lie on opposite corners.",
            font_size=26,
        )

        caption.to_edge(
            UP,
            buff=0.35,
        )

        # Return blue points to normal
        self.play(
            top_right.restore(),
            bottom_left.restore(),
            FadeIn(caption),
            run_time=0.6,
        )

        # ----------------------------------------------------------
        # Diagonal Guides
        # ----------------------------------------------------------

        red_diagonal = Line(
            top_left.get_center(),
            bottom_right.get_center(),
            color=top_left.get_color(),
            stroke_width=3,
        )

        blue_diagonal = Line(
            top_right.get_center(),
            bottom_left.get_center(),
            color=top_right.get_color(),
            stroke_width=3,
        )

        red_diagonal.set_opacity(0.45)
        blue_diagonal.set_opacity(0.45)

        # ==========================================================
        # Reveal Red Pair
        # ==========================================================

        self.play(
            top_left.secondary(),
            bottom_right.secondary(),
            Create(red_diagonal),
            run_time=0.8,
        )

        self.play(
            top_left.restore(),
            bottom_right.restore(),
            run_time=0.25,
        )

        self.wait(0.3)

        # ==========================================================
        # Reveal Blue Pair
        # ==========================================================

        self.play(
            top_right.secondary(),
            bottom_left.secondary(),
            Create(blue_diagonal),
            run_time=0.8,
        )

        self.play(
            top_right.restore(),
            bottom_left.restore(),
            run_time=0.25,
        )

        self.wait(3)

        # ==========================================================
        # Final Question
        # ==========================================================

        self.play(
            FadeOut(caption),
            run_time=0.3,
        )

        caption = Text(
            "Can a straight line separate opposite corners?",
            font_size=28,
        )

        caption.to_edge(
            UP,
            buff=0.35,
        )

        self.play(
            FadeIn(caption),
            run_time=0.8,
        )

        # Let the audience think
        self.wait(2)

        # ==========================================================
        # Remove the feature space first
        # ==========================================================

        self.play(
            FadeOut(feature_space),
            run_time=0.9,
        )

        self.wait(0.3)

        # ==========================================================
        # Fade to black
        # ==========================================================

        self.play(
            FadeOut(caption),
            FadeOut(red_diagonal),
            FadeOut(blue_diagonal),
            FadeOut(dataset),
            run_time=1.2,
        )

        self.wait()