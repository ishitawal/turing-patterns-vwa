from manim import *

class SquareToCircle(Scene):
    def construct(self):
        square = Square()
        circle = Circle()
        self.play(Create(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))


class LaTeXExample(Scene):
    def construct(self):
        tex = Tex(r"Hello, \LaTeX!")
        self.play(Write(tex))
        self.wait(2)


        act_11 = act.copy().shift([-2.25, 0.75, 0])
        act_22 = act.copy().shift([-2, -0.75, 0])
        act_33 = act.copy().shift([-1.25, 0.5, 0])
        act_44 = act.copy().shift([-3, -0.25, 0])
        act_55 = act.copy().shift([-2.4, -1.75, 0])
        act_66 = act.copy().shift([-1, -1.5, 0])

        inb_11 = inb.copy().shift([1.25, 0.6, 0])
        inb_22 = inb.copy().shift([1.75, -0.5, 0])
        inb_33 = inb.copy().shift([2.5, 0.8, 0])
        inb_44 = inb.copy().shift([2.75, -0.75, 0])
        inb_55 = inb.copy().shift([2, -1.8, 0])
        inb_66 = inb.copy().shift([1, -1.25, 0])

        act_inb = VGroup(act_11, act_22, act_33,act_44,act_55, act_66, inb_11, inb_22, inb_33, inb_44, inb_55, inb_66)