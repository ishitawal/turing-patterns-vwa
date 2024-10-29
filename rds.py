from manim import *

class subtitle_rds_scene(Scene):
    def construct(self):
        title = Text("2) Reaction-Diffusion System", font_size=60)
        title2 = Text("Reaction-Diffusion System", font_size=40).shift(UP*3 + LEFT*3.5)
        self.wait(1)
        self.play(Write(title))
        self.wait(1)
        self.play(Transform(title,title2))
        self.wait(1)

class morphogens_scene(Scene):
    def construct(self):
        title = Text("Reaction-Diffusion System", font_size=40).shift(UP * 3 + LEFT * 3.5)
        title_reaction = title[:8]
        title_diffusion = title[9:18]
        box = Rectangle(width=7.0, height=4.0).shift(0.5*DOWN)

        act = Circle(fill_opacity=0, stroke_color=GREEN, radius=0.2)
        act_1 = act.copy().shift([-2.5,1,0])
        act_2 = act.copy().shift([-2, -0.85, 0])
        act_3 = act.copy().shift([1.75, -0.5, 0])
        act_4 = act.copy().shift([2.5, 0.8, 0])
        act_5 = act.copy().shift([-0.2, -2, 0])
        act_6 = act.copy().shift([2, -1.8, 0])
        act_legend = act.copy().shift([-3,-3,0]).scale(0.8)

        inb = Circle(fill_opacity=1, stroke_color=RED, radius=0.2)
        inb_1 = inb.copy().shift([1.25, 1, 0])
        inb_2 = inb.copy().shift([-1.25, 0.5, 0])
        inb_3 = inb.copy().shift([-3, -0.25, 0])
        inb_4 = inb.copy().shift([2.75, -0.75, 0])
        inb_5 = inb.copy().shift([-0.5, -0.75, 0])
        inb_6 = inb.copy().shift([1, -1.25, 0])
        inb_7 = inb.copy().shift([-2.25, -2, 0])
        inb_legend = inb.copy().shift([-2.5, -3, 0]).scale(0.8)

        legend_text = Text("... morphogens", font_size=20, weight=BOOK).shift([-1.25,-3,0])
        morphogens = VGroup(act, act_1, act_2, act_3,act_4,act_5, act_6, inb_1, inb_2, inb_3, inb_4, inb_5, inb_6, inb_7)

        act_inb_text  = Text("Activator-Inhibitor Dynamic:", font_size=30, weight=SEMIBOLD).shift(UP*2 + LEFT*3)

        self.add(title)
        self.wait(1)
        self.play(Create(box))
        self.wait(1)
        self.play(FadeIn(morphogens,act_legend, inb_legend), Write(legend_text))
        self.wait(3)
        self.play(Indicate(title_reaction, scale_factor=1.1))
        self.wait(2)
        self.play(Indicate(title_diffusion, scale_factor=1.1))
        self.wait(2)
        self.play(Write(act_inb_text))
        self.wait(1)
        self.play(FadeOut(morphogens))
        self.wait(1)

class act_inb_dynamics_scene(Scene):
    def construct(self):
        title_white = Text("Reaction-Diffusion System", font_size=40).shift(UP * 3 + LEFT * 3.5)

        title_reaction =MarkupText(
            f'Reaction<span fgcolor="{WHITE}">-Diffusion System</span>', color=YELLOW, font_size=40).shift(UP * 3 + LEFT * 3.5)
        
        legend_text = Text("... morphogens", font_size=20, weight=BOOK).shift([-1.25,-3,0])


        act_inb_text = Text("Activator-Inhibitor Dynamic:", font_size=30, weight=SEMIBOLD).shift(UP * 2 + LEFT * 3)
        act_text = Text("Activator", color=GREEN, font_size=26).shift(4.75*LEFT)
        inb_text = Text("Inhibitor", color=RED, font_size=26).shift(4.75*RIGHT)
        auto_cat = Text("'Autocatalysis'", color=GREEN, font_size=24, slant=ITALIC).shift(4.75*LEFT+DOWN)
        box = Rectangle(width=7.0, height=4.0).shift(0.5 * DOWN)
        act = Circle(fill_opacity=0, stroke_color=GREEN, radius=0.2)
        inb = Circle(fill_opacity=1, stroke_color=RED, radius=0.2)

        act_1 = act.copy().shift([-2.25, 0.75, 0])
        act_2 = act.copy().shift([-2, -0.75, 0])
        act_3 = act.copy().shift([-1.25, 0.5, 0])
        act_4 = act.copy().shift([-3, -0.25, 0])
        act_5 = act.copy().shift([-2.4, -1.75, 0])
        act_6 = act.copy().shift([-1, -1.5, 0])
        act_7 = act.copy().shift([-0.5, 0.15, 0])
        act_8 = act.copy().shift([-0.8, -0.5, 0])
        act_legend = act.copy().shift([-3,-3,0]).scale(0.8)

        inb_1 = inb.copy().shift([1.25, 0.6, 0])
        inb_2 = inb.copy().shift([1.75, -0.5, 0])
        inb_3 = inb.copy().shift([2.5, 0.8, 0])
        inb_4 = inb.copy().shift([2.75, -0.75, 0])
        inb_5 = inb.copy().shift([2, -1.8, 0])
        inb_6 = inb.copy().shift([1.2, -1.5, 0])
        inb_7 = inb.copy().shift([1, -0.5, 0])
        inb_legend = inb.copy().shift([-2.5, -3, 0]).scale(0.8)

        act_inb = VGroup(act_1, act_2, act_3, act_4, act_5, act_6, inb_1, inb_2, inb_3, inb_4, inb_5)
        act_new = VGroup(act_7, act_8)
        inb_new = VGroup(inb_6, inb_7)

        self.add(title_white, act_inb_text, box,inb_legend,act_legend,legend_text)
        self.wait(1)
        self.play(Transform(title_white,title_reaction))
        self.play(FadeIn(act_inb))
        self.wait(1)
        self.play(Write(act_text), Write(inb_text))
        self.wait(1)
        self.play(FadeIn(act_new))
        self.wait(1)
        self.play(Write(auto_cat))
        self.wait(2)
        self.play(act_8.animate.shift(1.5*RIGHT+0.5*DOWN))
        self.play(FadeOut(act_8), FadeIn(inb_new))
        self.wait(1)
        self.play(inb_7.animate.shift([-1.5, 0.65, 0]))
        self.wait(4)
        self.play(FadeOut(act_inb, act_7, inb_new, act_text, inb_text, auto_cat,inb_legend,act_legend,legend_text))
        self.wait(2)

class diffusion_scene(Scene):
    def construct(self):
        title_reaction =MarkupText(
            f'Reaction<span fgcolor="{WHITE}">-Diffusion System</span>', color=YELLOW, font_size=40).shift(UP * 3 + LEFT * 3.5)
        title_diffusion =MarkupText(
            f'Reaction-<span fgcolor="{YELLOW}">Diffusion</span> System', color=WHITE, font_size=40).shift(UP * 3 + LEFT * 3.5)

        act_inb_text = Text("Activator-Inhibitor Dynamic:", font_size=30, weight=SEMIBOLD).shift(UP * 2 + LEFT * 3)
        diffusion_text = Text("Diffusion:", font_size=30, weight=SEMIBOLD).shift(UP * 2 + LEFT * 4)

        box = Rectangle(width=7.0, height=4.0).shift(0.5 * DOWN)
        box_dif= Rectangle(width=8.0, height=2.0).shift(0.5*UP)

        tri_dif= Polygon([-4,-2.5,0],[4,-2.5,0],[-4,-1.5,0])
        tri_dif.set_color_by_gradient(BLUE)
        tri_dif.set_fill(opacity=0.5)
        tri_dif.set_stroke(color=WHITE)

        arrow = Arrow(start=[-4,-3,0], end=[4,-3,0], buff=0.0)
        arrow_text = Text("concentration gradient", font_size=20, slant=ITALIC).next_to(arrow, DOWN*0.75)


        self.add(title_reaction,box,act_inb_text)
        self.wait(1)
        self.play(Transform(title_reaction,title_diffusion), Transform(act_inb_text,diffusion_text))
        self.wait(1)
        self.play(ReplacementTransform(box,box_dif), Create(tri_dif))
        self.add(arrow,arrow_text)
        self.wait(3)