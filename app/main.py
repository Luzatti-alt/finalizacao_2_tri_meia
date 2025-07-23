from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout  # Importando o layout
from kivy.core.window import Window
from kivy.graphics import Rectangle, Color#onde ficara o desing
#poder ter retangulo/caixas onde ficara a img e o desing
class DesenhoWidget(FloatLayout):
    def __init__(self, **kwargs):
        super(DesenhoWidget, self).__init__(**kwargs)
        altura = Window.height
        largura = Window.width

        # Usando o Canvas para desenhar o retângulo
        with self.canvas:
            Color(1, 1, 1)  # Define a cor branca (usando valores RGB entre 0 e 1)
            self.retangulo = Rectangle(pos=(100, 100), size=(200, 100))
class Prototipo(App):
    def build(self):
        altura = Window.height
        largura = Window.width
        layout = FloatLayout()
        # onde sera desenhada a img e componentes desta tela
        def draw():
            # Botão da IA para gerar imagem
            IA = Button(
                text='IA geradora de imagem',
                size_hint=(None, None),
                size=(200, 50),
                pos=(largura - 200, altura - 50)
            )
            IA.bind(on_press=self.gen_img)  # Ação ao pressionar o botão
            enviar = Button(
                text='Enviar design',
                size_hint=(None, None),  # Tamanho fixo, sem resize automático
                size=(200, 50),
                pos=(largura / 2 - 100, altura / 8 - 25)  # Corrigido para centralizar
            )
            desenho_widget = DesenhoWidget()
            layout.add_widget(desenho_widget)
            layout.add_widget(enviar)  # Adicionando o botão ao layout
            layout.add_widget(IA)  # Adicionando o botão IA ao layout
        draw()  # Chamando a função para desenhar os componentes

        return layout

    def gen_img(self, instance):
     print("temp para rodar funçao")
        # onde sera gerado a img por ia e componentes desta tela
Prototipo().run()
