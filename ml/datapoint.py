from manim import *
from engine.theme import *

class DataPoint(Dot):

    def __init__(self, position, color=CLASS_BLUE):
        super().__init__(
            point=position,
            radius=POINT_RADIUS,
            color=color,
        )