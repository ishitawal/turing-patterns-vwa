from manim import *

title_rds = Text("Reaction-Diffusion System", font_size=40).shift(UP*3 + LEFT*3.5)
title_concept = Text("Key concepts of RDS", font_size=40).shift(UP*3 + LEFT*3.5)
sub_title1 = Text("1) Non - linearity:", font_size=30, weight=SEMIBOLD).shift(UP*2 + LEFT*3)

class non_linearity(Scene):
    def construct(self):
        increase_formula = MathTex(r'\uparrow  [A]    \rightarrow    \frac{d[A]}{dt}  \uparrow')

        self.add(title_concept, sub_title1,increase_formula)
        #self.play(ReplacementTransform(title_rds,title_concept))
        #self.play(Write(sub_title1))