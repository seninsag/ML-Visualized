from manim import *


class ActivationPlane(Surface):
    """
    Semi-transparent plane representing the ReLU activation boundary (z = 0).
    """

    def __init__(self):

        super().__init__(
            lambda u, v: np.array([u, v, 0]),
            u_range=[-3, 3],
            v_range=[-3, 3],
            resolution=(16, 16),

            fill_opacity=0.03,
            checkerboard_colors=[
                BLUE_E,
                BLUE_D
            ],

            stroke_color=BLUE_B,
            stroke_width=0.3,
        )

        self.set_shade_in_3d(True)