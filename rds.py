from manim import *

#ffmpeg -i forest_example_scene.mp4 frame_%04d.png

act = Circle(fill_opacity=0, stroke_color=GREEN, radius=0.2)
inb = Circle(fill_opacity=1, stroke_color=RED, radius=0.2)
title_sub = Text("Reaction-Diffusion System", font_size=40).shift(UP*3 + LEFT*3.5)
title_reaction =MarkupText(
            f'Reaction<span fgcolor="{WHITE}">-Diffusion System</span>', color=YELLOW, font_size=40).shift(UP * 3 + LEFT * 3.5)
title_diffusion =MarkupText(
            f'Reaction-<span fgcolor="{YELLOW}">Diffusion</span> System', color=WHITE, font_size=40).shift(UP * 3 + LEFT * 3.5)
act_inb_text  = Text("Activator-Inhibitor Dynamic:", font_size=30, weight=SEMIBOLD).shift(UP*2 + LEFT*3)
diffusion_text = Text("Diffusion:", font_size=30, weight=SEMIBOLD).shift(UP * 2 + LEFT * 4)
forest_text = Text("Forest Fire Example:", font_size=30, weight=SEMIBOLD).shift(UP*2 + LEFT*3)
comparison_text = Text("Comparison - Diffusion:", font_size=30, weight=SEMIBOLD).shift(UP*2 + LEFT*3)
box = Rectangle(width=7.0, height=4.0).shift(0.5*DOWN)
box_dif= Rectangle(width=8.0, height=2.0).shift(0.5*UP)
inset_frame = Rectangle(height=1.5 , width=3, stroke_color=WHITE, fill_opacity=0)


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
                [-2.5,1,0],[-2, -0.85, 0],[1.75, -0.5, 0],[2.5, 0.8, 0],[-0.2, -2, 0],[2, -1.8, 0],[0,0,0]
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
        legend_text = Text("... morphogens", font_size=20, weight=BOOK).shift([-1.25,-3,0])

        act_text = Text("Activator", color=GREEN, font_size=26).shift(4.75*LEFT)
        inb_text = Text("Inhibitor", color=RED, font_size=26).shift(4.75*RIGHT)
        auto_cat = Text("'Autocatalysis'", color=GREEN, font_size=24, slant=ITALIC).shift(4.75*LEFT+DOWN)

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
            ],run_time=2.5)                                                                                             
                                                                                                                        #Transform not quite right - position change wrong --> change later
        self.wait(1)
        self.play(FadeOut(tri_dif,arrow,arrow_text))
        self.wait(1)
        self.play(Write(parameteres_text))
        self.play(Write(Dc))
        self.wait(1)
        self.play(Write(dif_condition))
        self.wait(1)
        self.play(Create(highlight))
        self.wait(1)
        self.play(FadeOut(no_dif_group,parameteres_text,Dc,dif_condition,highlight))
        self.wait(3)

class forest_example_scene(Scene):
    def construct(self):
        box = Rectangle(width=7.0, height=4.0, stroke_color=LIGHT_BROWN, fill_color=YELLOW_D, fill_opacity=0.5).shift(0.5*DOWN)
        inb = Circle(fill_opacity=1, color=BLUE, radius=0.2)
        fire = ImageMobject("C:/Users/walia/Documents/manim_projects/vwa_manim_video/media/images/rds/fire.png")
        tree = ImageMobject("C:/Users/walia/Documents/manim_projects/vwa_manim_video/media/images/rds/burnt_tree.png")

        fire_pos = [
            [-2.5, 1, 0],[-2, -0.85, 0],[-0.2, -2, 0],
            [0, 0, 0],[1.75, -0.5, 0],[2, -1.8, 0],[2.5, 0.8, 0]
          ]
           #same positions as in act_pos(morphogen_scene)

        inb_pos = [
            [-2.5, -0.85, 0],[-1.5, -0.85, 0],[-2, -0.35, 0],   #fighter1
            [-0.5, 0, 0], [0.5, 0, 0], [0, 0.5, 0],             #fighter2
            [1.25, -0.5, 0],[2.25, -0.5, 0],[1.75, 0, 0],       #fighter3
            [1.25, 1, 0],[-0.5, -0.75, 0],[-2.25, -2, 0]        #fighter-start
           ]

        fire_group = Group(*[fire.copy().shift(pos).scale(0.2) for pos in fire_pos])
        fighter_group = VGroup(*[inb.copy().shift(pos).scale(0.7) for pos in inb_pos])
        tree_group = Group(*[tree.copy().shift(pos).scale(3) for pos in fire_pos])

        fire_legend = fire.scale(0.2).next_to(box, DOWN+2.5*LEFT)
        inb_legend = inb.scale(0.5).next_to(fire_legend, DOWN*0.5)
        tree_legend = ImageMobject("C:/Users/walia/Documents/manim_projects/vwa_manim_video/media/images/rds/white_tree.png").scale(2).next_to(inb_legend, DOWN*0.5)

        fire_text = Text('fire  (activator)',font_size=20, weight=BOOK).next_to(fire_legend, RIGHT*1.5)
        inb_text = Text('fire fighter  (inhibitor)',font_size=20, weight=BOOK).next_to(inb_legend, RIGHT*1.5)
        tree_text = Text('burned trees',font_size=20, weight=BOOK).next_to(tree_legend, RIGHT*1.5)
       
## reaction dynamics 
        self.add(title_diffusion,diffusion_text,box_dif)
        self.wait(1)
        self.play(Transform(title_diffusion,title_sub), Transform(box_dif,box), ReplacementTransform(diffusion_text, forest_text))
        self.wait(1)
        self.play(FadeIn(fire_legend,inb_legend,tree_legend,fire_text,inb_text,tree_text))
        self.wait(1)
        self.play(FadeIn(fire_group[3], fighter_group[9:]))
        self.wait(1)
        self.play(FadeIn(fire_group[1], fire_group[4]))
        self.wait(1)
        self.play(ReplacementTransform(fighter_group[9:],fighter_group[:9]))
        self.wait(1)
        self.play(FadeOut(fire_group[3],fire_group[1], fire_group[4],fighter_group[:9]), FadeIn(tree_group))
        self.wait(2)
        self.play(FadeOut(tree_group))

## diffusion (1)
        numbering1 = Text('(1)', font_size=30, weight=SEMIBOLD).next_to(forest_text)
        inb_ring = Circle(stroke_color=BLUE, fill_opacity=0, radius=0.3)
        inb_legend_ring = Circle(stroke_color=BLUE, fill_opacity=0, radius=0.1).next_to(fire_legend, DOWN*0.5)
        inb_group = Group(*[inb_ring.copy().shift(pos) for pos in fire_pos])

        grow_animation = [
            [GrowFromPoint(inb_ring, inb_ring.get_center()) for inb_ring in inb_group]
            ]
        scale_animation = [
            fire.animate.scale(1.2, about_point=fire.get_center()) for fire in fire_group 
        ]

        self.play(ReplacementTransform(inb_legend,inb_legend_ring), FadeIn(numbering1))
        self.wait(1)
        self.play(FadeIn(fire_group))
        self.wait(1)
        self.play(
            AnimationGroup(
                *scale_animation, rate_func=exponential_decay, run_time=2
            )
        )
        self.play(
                    AnimationGroup(
                        *grow_animation, run_time=1, rate_func=linear
                        )
        )
        self.wait(1)
        self.play(FadeOut(fire_group),FadeIn(tree_group), FadeOut(inb_group))
        self.wait(1)
        self.play(FadeOut(tree_group))
        
# diffusion (2)    
        numbering2 = Text('(2)', font_size=30, weight=SEMIBOLD).next_to(forest_text)
        for fire in fire_group:
            fire.scale(1/1.2, about_point=fire.get_center())
        inb_ring_2 = Circle(stroke_color=BLUE, fill_opacity=0, radius=0.5)
        inb_group_2 = Group(*[inb_ring_2.copy().shift(pos) for pos in fire_pos])
        grow_animation = [
            [GrowFromPoint(inb_ring_2, inb_ring_2.get_center()) for inb_ring_2 in inb_group_2]
            ]
        scale_animation = [
            fire.animate.scale(2, about_point=fire.get_center()) for fire in fire_group 
        ]
        for tree in tree_group:
            tree.scale(2, about_point=tree.get_center())
        
        self.wait(2)
        self.play(ReplacementTransform(numbering1,numbering2))
        self.wait(1)
        self.play(FadeIn(fire_group))
        self.wait(1)
        self.play(
            AnimationGroup(
                *scale_animation, rate_func=exponential_decay, run_time=4
            )
        )
        self.play(
            AnimationGroup(
                    *grow_animation, run_time=2, rate_func=linear
            )
        )
        self.wait(1)
        self.play(FadeOut(fire_group),FadeIn(tree_group), FadeOut(inb_group_2))
        self.play(FadeOut(tree_group))
        self.wait(3)
        
# diffusion (3)   
        numbering3 = Text('(3)', font_size=30, weight=SEMIBOLD).next_to(forest_text)
        for fire in fire_group:
            fire.scale(0.5, about_point=fire.get_center())
        scale_animation = [
            fire.animate.scale(3, about_point=fire.get_center()) for fire in fire_group                                             #scaling could be more extreme
        ]
        box_burned = Rectangle(width=7.0, height=4.0, stroke_color=GRAY_C, fill_color=GRAY_D, fill_opacity=0.9).shift(0.5*DOWN)

        self.wait(2)
        self.play(ReplacementTransform(numbering2,numbering3))
        self.wait(1)
        self.play(FadeIn(fire_group))
        self.wait(1)
        self.play(
            AnimationGroup(
                *scale_animation, rate_func=exponential_decay, run_time=6
            )
        )
        self.wait(1)
        self.play(FadeOut(fire_group), ReplacementTransform(box, box_burned), lag_ratio=0.5)
        self.add(box_burned)
        self.wait(1)
        self.play(FadeOut(box_burned, box, inb_legend_ring, fire_legend, tree_legend, inb_text, fire_text, tree_text, forest_text, numbering3))                 ## at the end the yellow box is not fading out?!
        self.wait(3)


class diffusion_rate_comparison(Scene):
    def construct(self):
        number1= Text('(1)', font_size=30, weight=SEMIBOLD).to_edge(LEFT, buff=0.5).shift(UP*1.5)
        number2= Text('(2)', font_size=30, weight=SEMIBOLD).to_edge(LEFT, buff=0.5).shift(DOWN*0.5)
        number3= Text('(3)', font_size=30, weight=SEMIBOLD).to_edge(LEFT, buff=0.5).shift(DOWN*2.5)

        frame1= inset_frame.copy().next_to(number1, buff=0.75)
        frame2= inset_frame.copy().next_to(number2, buff=0.75)
        frame3= inset_frame.copy().next_to(number3, buff=0.75)

        dif1= MathTex('D_I >> D_A', font_size=40).next_to(frame1, buff=2.5)
        dif2= MathTex('D_I \\approx D_A', font_size=40).next_to(frame2, buff=2.5)
        dif3= MathTex('D_I < D_A', font_size=40).next_to(frame3, buff=2.5)

        

        self.add(title_sub, number1, number2, number3, frame1, frame2, frame3,dif1, dif2, dif3)
        self.play(FadeIn(video1))
        self.wait(8)

        ##Trying to include a video segment in a scene - tried VideoMobject command (not available) and now trying creating individual frames