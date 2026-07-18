from manim import *
import numpy as np

from engine.theme import *
from ml.linear_classifier import LinearClassifier


class DecisionBoundary(Line):
    """
    Draws the decision boundary learned by a Linear SVM.
    """

    def __init__(self, start, end):
        super().__init__(
            start=start,
            end=end,
            color=GREEN,
            stroke_width=3,
        )

        self.set_opacity(0.75)

    def success(self):
        return self.animate.set_color(GREEN)

    def failure(self):
        return self.animate.set_color(RED)

    @classmethod
    def from_cloud(cls, cloud):
        classifier = LinearClassifier().fit(cloud)

        w = classifier.normal
        b = classifier.bias

        # Average z level of all points
        z = np.mean([
            dp.get_center()[2]
            for dp in cloud.data_points
        ])

        # Plane equation:
        # w0*x + w1*y + w2*z + b = 0
        c = w[2] * z + b

        # Prevent division by zero
        if abs(w[1]) < 1e-8:
            w[1] = 1e-8

        # Draw a long line across the scene
        x_min = -5
        x_max = 5

        y_min = -(w[0] * x_min + c) / w[1]
        y_max = -(w[0] * x_max + c) / w[1]

        start = np.array([x_min, y_min, z])
        end = np.array([x_max, y_max, z])

        return cls(start, end)