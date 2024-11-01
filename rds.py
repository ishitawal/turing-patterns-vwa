from manim import *

act = Circle(fill_opacity=0, stroke_color=GREEN, radius=0.2)
inb = Circle(fill_opacity=1, stroke_color=RED, radius=0.2)
title_sub = Text("Reaction-Diffusion System", font_size=40).shift(UP*3 + LEFT*3.5)
act_inb_text  = Text("Activator-Inhibitor Dynamic:", font_size=30, weight=SEMIBOLD).shift(UP*2 + LEFT*3)
box = Rectangle(width=7.0, height=4.0).shift(0.5*DOWN)

class subtitle_rds_scene(Scene):
    def construct(self):
        title_main = Text("2) Reaction-Diffusion System", font_size=60)
        self.wait(1)
        self.play(Write(title_main))
        self.wait(1)
        self.play(Transform(title_main,title_sub))
        self.wait(1)

class morphogens_scene(Scene):
    def construct(self):
        act_legend = act.copy().shift([-3,-3,0]).scale(0.8)
        inb_legend = inb.copy().shift([-2.5, -3, 0]).scale(0.8)

        inb_pos = [
            [1.25, 1, 0],[-1.25, 0.5, 0],[-3, -0.25, 0],[2.75, -0.75, 0],[-0.5, -0.75, 0],[1, -1.25, 0],[-2.25, -2, 0]
        ]
        act_pos = [
                [-2.5,1,0],[-2, -0.85, 0],[1.75, -0.5, 0],[2.5, 0.8, 0],[-0.2, -2, 0],[2, -1.8, 0]
        ]

        morphogens = VGroup(*[act.copy().shift(pos) for pos in act_pos], *[inb.copy().shift(pos) for pos in inb_pos])

        legend_text = Text("... morphogens", font_size=20, weight=BOOK).shift([-1.25,-3,0])

        self.add(title_sub)
        self.wait(1)
        self.play(Create(box))
        self.wait(1)
        self.play(FadeIn(morphogens,act_legend, inb_legend), Write(legend_text))
        self.wait(3)
        self.play(Indicate(title_sub[:8], scale_factor=1.1))
        self.wait(2)
        self.play(Indicate(title_sub[9:18], scale_factor=1.1))
        self.wait(2)
        self.play(Write(act_inb_text))
        self.wait(1)
        self.play(FadeOut(morphogens))
        self.wait(1)

class act_inb_dynamics_scene(Scene):
    def construct(self):
        title_reaction =MarkupText(
            f'Reaction<span fgcolor="{WHITE}">-Diffusion System</span>', color=YELLOW, font_size=40).shift(UP * 3 + LEFT * 3.5)
        
        legend_text = Text("... morphogens", font_size=20, weight=BOOK).shift([-1.25,-3,0])

        act_text = Text("Activator", color=GREEN, font_size=26).shift(4.75*LEFT)
        inb_text = Text("Inhibitor", color=RED, font_size=26).shift(4.75*RIGHT)
        auto_cat = Text("'Autocatalysis'", color=GREEN, font_size=24, slant=ITALIC).shift(4.75*LEFT+DOWN)
        act = Circle(fill_opacity=0, stroke_color=GREEN, radius=0.2)
        inb = Circle(fill_opacity=1, stroke_color=RED, radius=0.2)

        act_7 = act.copy().shift([-0.5, 0.15, 0])
        act_8 = act.copy().shift([-0.8, -0.5, 0])
        act_legend = act.copy().shift([-3,-3,0]).scale(0.8)

        inb_6 = inb.copy().shift([1.2, -1.5, 0])
        inb_7 = inb.copy().shift([1, -0.5, 0])
        inb_legend = inb.copy().shift([-2.5, -3, 0]).scale(0.8)

        act_new = VGroup(act_7, act_8)
        inb_new = VGroup(inb_6, inb_7)

        inb_pos = [
            [1.25, 0.6, 0],[1.75, -0.5, 0],[2.5, 0.8, 0],[2.75, -0.75, 0],[2, -1.8, 0]
        ]
        act_pos = [
                [-2.25, 0.75, 0],[-2, -0.75, 0],[-1.25, 0.5, 0],[-3, -0.25, 0],[-2.4, -1.75, 0],[-1, -1.5, 0]
        ]

        act_inb = VGroup(*[act.copy().shift(pos) for pos in act_pos], *[inb.copy().shift(pos) for pos in inb_pos])

        self.add(title_sub, act_inb_text, box,inb_legend,act_legend,legend_text)
        self.wait(1)
        self.play(Transform(title_sub,title_reaction))
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

        diffusion_text = Text("Diffusion:", font_size=30, weight=SEMIBOLD).shift(UP * 2 + LEFT * 4)

        box_dif= Rectangle(width=8.0, height=2.0).shift(0.5*UP)

        tri_dif= Polygon([-4,-2.5,0],[4,-2.5,0],[-4,-1.5,0])
        tri_dif.set_color_by_gradient(BLUE)
        tri_dif.set_fill(opacity=0.5)
        tri_dif.set_stroke(color=WHITE)

        arrow = Arrow(start=[-4,-3,0], end=[4,-3,0], buff=0.0)
        arrow_text = Text("concentration gradient", font_size=20, slant=ITALIC).next_to(arrow, DOWN*0.75)

        molecule = Circle(fill_opacity=0, stroke_color=BLUE, radius=0.1)

        no_dif_pos = [
            [-2.125,1.375,0],[-2,0.625,0],[-1.625,1.25,0],[-2.5,0.875,0],[-2.2,0.125,0],[-1.5,0.25,0]
        ]
        dif_pos = [
            [-3.5, 1.0, 0],[-2.5, -0.2, 0],[-1.75, 1.25, 0],[0.0, 0.75, 0],[2.25, -0.25, 0],[3.5, 1.0, 0]  
        ]

        no_dif_group = VGroup(*[molecule.copy().shift(pos) for pos in no_dif_pos]).shift(LEFT+0.25 *DOWN)
        dif_group = VGroup(*[molecule.copy().shift(pos) for pos in dif_pos])

        parameteres_text = MarkupText(f'''
                                      - substance
                                      - size
                                      - medium
                                      ''', font_size=26).shift(RIGHT*0+DOWN*2)
        
        Dc = MarkupText('diffusion coefficient ... D<sub>c</sub>  :', font_size=28).shift(LEFT*3.75+ DOWN*2)

        dif_condition = MarkupText('D<sub>I</sub> > D<sub>A</sub>', font_size= 35, weight=SEMIBOLD).shift(RIGHT*3.5+DOWN*2)

        highlight = Rectangle(color=YELLOW).surround(dif_condition, buff=0.5)

        self.add(title_reaction,box,act_inb_text)
        self.wait(1)
        self.play(Transform(title_reaction,title_diffusion), Transform(act_inb_text,diffusion_text))
        self.wait(1)
        self.play(ReplacementTransform(box,box_dif), Create(tri_dif))
        self.wait(1)
        self.play(Create(arrow),Write(arrow_text))
        self.wait(1)
        self.play(FadeIn(no_dif_group))
        self.wait(1)
        self.play(*[
             ReplacementTransform(no_dif_group[i], no_dif_group[i].copy().move_to(dif_group[i].get_center()))
            for i in range(len(no_dif_group))
            ],run_time=2.5)                    #Transform not quite right - position change wrong --> change later
        self.wait(1)
        self.play(FadeOut(tri_dif,arrow,arrow_text))
        self.wait(1)
        self.play(Write(parameteres_text))
        self.play(Write(Dc))
        self.wait(1)
        self.play(Write(dif_condition))
        self.play(Create(highlight))
        self.wait(3)
