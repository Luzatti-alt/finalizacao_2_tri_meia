from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout  # Importando o layout
from kivy.core.window import Window

class Prototipo(App):
    def build(self):
        altura = Window.height
        largura = Window.width

        layout = FloatLayout()
        IA = Button(
            text='IA geradora de imagem',
            size_hint=(None, None),  # Tamanho fixo, sem resize automático
            size=(200, 50),
            pos=(largura-200, altura-50)  # Corrigido para centralizar
        )

        # Criando o botão com a posição corrigida
        enviar = Button(
            text='Enviar design',
            size_hint=(None, None),  # Tamanho fixo, sem resize automático
            size=(200, 50),
            pos=(largura / 2 - 100, altura / 8 - 25)  # Corrigido para centralizar
        )

        layout.add_widget(enviar)  # Adicionando o botão ao layout
        layout.add_widget(IA)#botão da ia que gerar a img
        return layout

Prototipo().run()
