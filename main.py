from manim import *

class Intro(Scene):
    def construct(self):
        title = Text("Machine Learning Visualized")

        self.play(Write(title))
        self.wait(2)