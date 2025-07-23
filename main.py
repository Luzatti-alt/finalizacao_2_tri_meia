from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout  # Importando o layout
from kivy.core.window import Window

class Prototipo(App):
    def build(self):
        altura = Window.height
        largura = Window.width

        layout = FloatLayout()

        # Criando o botão com a posição corrigida
        botao = Button(
            text='Enviar design',
            size_hint=(None, None),  # Tamanho fixo, sem resize automático
            size=(200, 50),
            pos=(largura / 2 - 100, altura / 2 - 25)  # Corrigido para centralizar
        )

        layout.add_widget(botao)  # Adicionando o botão ao layout
        return layout

Prototipo().run()
