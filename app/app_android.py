from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
class PrototipoAndroid(App):
    def build(self):
        altura = Window.height
        largura = Window.width
        layout = FloatLayout()
        # Fundo com cor
        with layout.canvas.before:
            Color(0.1, 0.1, 0.2, 1)  # Fundo azul escuro
            self.bg_rect = Rectangle(pos=layout.pos, size=Window.size)
        def update_bg(*args):
            self.bg_rect.pos = layout.pos
            self.bg_rect.size = Window.size
        layout.bind(pos=update_bg, size=update_bg)
        # Botões posicionados manualmente
        estoque = Button(
            text='Ver estoque',
            size_hint=(None, None),
            size=(200, 100),
            background_normal="",
            background_color=(0.2, 0.6, 0.9, 1),
            pos=(0, altura / 2 + 200)
        )
        add_cor = Button(
            text='Adicionar cor',
            size_hint=(None, None),
            size=(200, 100),
            background_normal="",
            background_color=(0.2, 0.6, 0.9, 1),
            pos=(0, altura / 2 + 80)
        )
        remover_cor = Button(
            text='Remover cor',
            size_hint=(None, None),
            size=(200, 100),
            background_normal="",
            background_color=(0.2, 0.6, 0.9, 1),
            pos=(0, altura / 2 - 40)
        )
        prod_meia = Button(
            text='Produzir meia',
            size_hint=(None, None),
            size=(200, 100),
            background_normal="",
            background_color=(0.2, 0.6, 0.9, 1),
            pos=(0, altura / 2 - 160)
        )
        upt_cor = Button(
            text='Atualizar cor',
            size_hint=(None, None),
            size=(200, 100),
            background_normal="",
            background_color=(0.2, 0.6, 0.9, 1),
            pos=(0, altura / 2 - 280)
        )
        # Adicionando os botões ao layout
        layout.add_widget(estoque)
        layout.add_widget(add_cor)
        layout.add_widget(remover_cor)
        layout.add_widget(prod_meia)
        layout.add_widget(upt_cor)
        return layout
PrototipoAndroid().run()