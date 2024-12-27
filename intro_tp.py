from manim import *

class subtitle_intro_tp_scene(Scene):
    def construct(self):
        title_main = Text("1) Introduction to Turing Patterns", font_size=60)

        self.wait(1)
        self.play(Write(title_main))
        self.wait(1)
        self.play(FadeOut(title_main))
        self.wait(2)


class morphogenesis(Scene):
    def construct(self):
        box1 = Rectangle(height=2.5, width=3.5, stroke_color = WHITE).shift(1.5*UP+3*LEFT)
        box2 = Rectangle(height=2.5, width=3.5, stroke_color = WHITE).shift(1.5*UP+3*RIGHT)
        morph_text = Text("Morphogenesis", font_size=40).shift(2*DOWN+3*LEFT)
        q_mark = Text("?", font_size=40).shift(DOWN*2+LEFT*0.25)
        equal = Text("=", font_size=40).shift(DOWN*2+LEFT*0.25)
        pattern_text = Text("Pattern formation", font_size=40).shift(2*DOWN+3*RIGHT)

        before_text = MarkupText(f'''
                                homogenous,
                                uniform state
                                      ''', font_size=26).shift(LEFT*3+DOWN*2)
        after_text = MarkupText(f'''spatial pattern
                                      ''', font_size=26).shift(RIGHT*3+DOWN*2)
        arrow = Arrow(start=[-0.75,-2,0], end=[0.75,-2,0], buff=0.0)
        arrow_text = Text("time", font_size=20, slant=ITALIC).next_to(arrow, DOWN*0.75)

        definition = VGroup(before_text, after_text, arrow, arrow_text)
        brace = BraceBetweenPoints([-4.5,0,0], [4.5,0,0], sharpness=0.7).shift(UP*0.75)
        brace_text = Text("Spatio - temporal patterns", font_size=40).next_to(brace, DOWN*0.75)

        tp_text = MarkupText(f'Turing Patterns:', font_size=30).shift(LEFT*2+DOWN*2)
        conditions_text = MarkupText(f'''
                                      - emerge naturally
                                      - spatially non-uniform
                                      - steady over time
                                      ''', font_size=26).shift(RIGHT*2+DOWN*2)

        self.add(box1, box2)
        self.play(Write(morph_text), Write(q_mark), Write(pattern_text))
        self.wait(1)
        self.play(ReplacementTransform(q_mark, equal))
        self.wait(1)
        self.play(Indicate(equal))
        self.wait(1)
        self.play(ReplacementTransform(morph_text, before_text), ReplacementTransform(pattern_text, after_text), ReplacementTransform(equal, arrow), FadeIn(arrow_text))
        self.wait(2)
        self.play(FadeOut(box1, box2), definition.animate.shift(UP*3.5))
        self.wait(1)
        self.play(Create(brace), Create(brace_text))
        self.wait(2)
        self.play(Write(conditions_text), Write(tp_text))
        self.wait(2)
        self.play(FadeOut(definition, brace, brace_text, tp_text, conditions_text))
        self.wait(1)