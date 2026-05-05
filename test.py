from test import *

class SomaBonita(Scene):
    def construct(self):
        # Criando os elementos separados
        um1 = MathTex("1").set_color(BLUE).shift(LEFT * 2)
        um2 = MathTex("1").set_color(GREEN).shift(RIGHT * 2)
        mais = MathTex("+").shift(UP * 0.5)

        # Aparecendo na tela
        self.play(FadeIn(um1), FadeIn(um2), FadeIn(mais))
        self.wait(1)

        # Movendo os números para o centro
        self.play(
            um1.animate.move_to(LEFT * 0.5),
            um2.animate.move_to(RIGHT * 0.5),
            run_time=1.5
        )

        self.wait(0.5)

        # Criando resultado
        resultado = MathTex("2").scale(1.5).set_color(YELLOW)

        # Transformação suave
        self.play(
            ReplacementTransform(VGroup(um1, um2, mais), resultado),
            run_time=1.5
        )

        self.wait(1)

        # Destaque final
        self.play(
            resultado.animate.scale(1.2),
            run_time=0.5
        )
        self.wait(2)