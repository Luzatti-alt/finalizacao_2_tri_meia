from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout  # Importando o layout
from kivy.core.window import Window

class Prototipo(App):
    def build(self):
        altura = Window.height
        largura = Window.width
        layout = FloatLayout()

        # Função para desenhar os componentes
        return layout

# Inicia o aplicativo
Prototipo().run()
