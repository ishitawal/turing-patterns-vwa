from manim import *

title_rds = Text("Reaction-Diffusion System", font_size=40).shift(UP*3 + LEFT*3.5)
title_concept = Text("Key concepts of RDS", font_size=40).shift(UP*3 + LEFT*3.5)
sub_title1 = Text("1) Non - linearity:", font_size=30, weight=SEMIBOLD).shift(UP*2 + LEFT*3.5)
sub_title2 = Text("2) Inhibition of autocatalysis:", font_size=30, weight=SEMIBOLD).shift(UP*2 + LEFT*3)
sub_title3 = Text("3) Diffusion rates:", font_size=30, weight=SEMIBOLD).shift(UP*2 + LEFT*3.5)

class non_linearity(Scene):
    def construct(self):
        increase_formula = MathTex(r'\uparrow  [A]  ',r'  \Longrightarrow  ',r'  \frac{d[A]}{dt}  \uparrow').shift(UP)      #add --> non-linear process
                                                                                                                            # instead of longarrow write "+"? makes more sense... ask about it!!

        ax = Axes(
            x_range=[0, 5],
            y_range=[0, 3],
            tips=True
        )
        labels = ax.get_axis_labels(x_label='t', y_label='[A]')

        line = ax.plot(lambda x: min(0.3*x+0.2, 3), x_range=[0,5], color=BLUE_C)

        curve = ax.plot(lambda x: 0.2 * np.exp(0.6 * x), color=YELLOW)

        line_label = ax.get_graph_label(
            line,
            label = "linear",
            x_val=5,
            color=BLUE_C,
        ).shift(RIGHT)

        curve_label = ax.get_graph_label(
            curve,
            label = 'non-linear',
            x_val=4.5,
            color=YELLOW,
        ).shift(RIGHT*2+UP)

        explosion = Text("EXPLOSION", color=YELLOW).next_to(curve, UP, buff=0.5)

        graph = VGroup(ax, labels, line, curve, line_label, curve_label).scale(0.5).shift(DOWN*2)

        self.play(ReplacementTransform(title_rds,title_concept))
        self.wait(1)
        self.play(Write(sub_title1), FadeIn(increase_formula))
        self.wait(1)
        self.play(Indicate(increase_formula[0]))
        self.wait(1)
        self.play(Indicate(increase_formula[2]))
        self.wait(1)
        self.play(Create(ax), Create(labels))
        self.wait(1)
        self.play(Create(line), Create(line_label), lag_ratio=0.5)
        self.wait(1)
        self.play(Create(curve), Create(curve_label), Create(explosion), lag_ratio=0.5)
        self.wait(5)

        graph = VGroup(ax, labels, curve)
        curve_limit = ax.plot(lambda x: min(0.2 * np.exp(0.6 * x), 3), x_range=[0, 4.5], color=YELLOW).shift(LEFT*3)
        limit = Line([-0.5,0,0],[0.5,0,0], color=RED)
        limit_text = MarkupText('''
            Limitation:
                                
                - finit supply of reactants      
                - activator-inhibitor dynamic
        ''', font_size=24).shift(RIGHT*3.5+DOWN)

        self.play(ReplacementTransform(sub_title1, sub_title2), FadeOut(line, line_label, increase_formula, curve_label))
        self.wait(1)
        self.play(graph.animate.shift(LEFT*3))
        self.play(ReplacementTransform(curve, curve_limit), FadeIn(limit))
        self.play(Write(limit_text))
        self.wait(5)

        dif= MathTex('D_I > D_A', font_size=60)
        box = SurroundingRectangle(dif, buff = .5)

        self.play(ReplacementTransform(sub_title2, sub_title3), FadeOut(graph, limit, limit_text))
        self.wait(1)
        self.play(Write(dif))
        self.play(Create(box))
        self.wait(1)
        self.play(FadeOut(title_concept, sub_title3, dif, box))
        self.wait(5)