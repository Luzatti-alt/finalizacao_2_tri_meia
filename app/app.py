from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
class PrototipoApp(App):
    def build(self):
        altura = Window.height
        largura = Window.width
        layout = FloatLayout()
        # Fundo
        with layout.canvas.before:
            Color(0.1, 0.1, 0.2, 1)
            self.bg_rect = Rectangle(pos=layout.pos, size=Window.size)
        def update_bg(*args):
            self.bg_rect.pos = layout.pos
            self.bg_rect.size = Window.size
        layout.bind(pos=update_bg, size=update_bg)
        # Botões
        self.estoque = Button(
            text='Ver estoque',
            size_hint=(None, None),
            size=(300, 100),
            background_normal="",
            background_color=(0.2, 0.6, 0.9, 1),
            pos=(0, altura / 2 + 200)
        )
        self.add_cor = Button(
            text='Adicionar cor',
            size_hint=(None, None),
            size=(300, 100),
            background_normal="",
            background_color=(0.2, 0.6, 0.9, 1),
            pos=(0, altura / 2 + 80)
        )
        self.remover_cor = Button(
            text='Remover cor',
            size_hint=(None, None),
            size=(300, 100),
            background_normal="",
            background_color=(0.2, 0.6, 0.9, 1),
            pos=(0, altura / 2 - 40)
        )
        self.prod_meia = Button(
            text='Produzir meia',
            size_hint=(None, None),
            size=(300, 100),
            background_normal="",
            background_color=(0.2, 0.6, 0.9, 1),
            pos=(0, altura / 2 - 160)
        )
        self.upt_cor = Button(
            text='Atualizar cor',
            size_hint=(None, None),
            size=(300, 100),
            background_normal="",
            background_color=(0.2, 0.6, 0.9, 1),
            pos=(0, altura / 2 - 280)
        )
        layout.add_widget(self.estoque)
        layout.add_widget(self.add_cor)
        layout.add_widget(self.remover_cor)
        layout.add_widget(self.prod_meia)
        layout.add_widget(self.upt_cor)
        # Painel azul de fundo para scroll
        with layout.canvas.before:
            Color(0.1, 0.3, 0.8, 1)
            self.painel_fundo = Rectangle()
        # ScrollView com conteúdo
        self.scroll = ScrollView(size_hint=(None, None))
        self.grid = GridLayout(cols=1, size_hint_y=None, padding=10, spacing=10)
        self.grid.bind(minimum_height=self.grid.setter("height"))
        for i in range(20):
            self.grid.add_widget(Label(text=f"Linha de informação {i+1}", size_hint_y=None, height=30, color=(1, 1, 1, 1)))
        self.scroll.add_widget(self.grid)
        layout.add_widget(self.scroll)
        # Pergunta
        self.pergunta = Label(text="Pergunta:", size_hint=(None, None), color=(1, 1, 1, 1))
        layout.add_widget(self.pergunta)
        # Input
        self.entrada = TextInput(hint_text="Digite aqui...", size_hint=(None, None), background_color=(0, 0, 0, 1), foreground_color=(1, 1, 1, 1), cursor_color=(1, 1, 1, 1))
        layout.add_widget(self.entrada)
        Window.bind(size=self.reposicionar_elementos)
        self.reposicionar_elementos()
        return layout
    def reposicionar_elementos(self, *args):
        altura = Window.height
        largura = Window.width
        self.estoque.pos = (0, altura / 2 + 200)
        self.add_cor.pos = (0, altura / 2 + 80)
        self.remover_cor.pos = (0, altura / 2 - 40)
        self.prod_meia.pos = (0, altura / 2 - 160)
        self.upt_cor.pos = (0, altura / 2 - 280)
        # Pergunta e entrada lado a lado
        self.pergunta.pos = (340, altura/8)
        self.pergunta.size = (largura - 360, altura/10+200)
        self.entrada.pos = (340, altura/10)
        self.entrada.size = (largura - 360, altura/10)
        # ScrollView
        scroll_y = self.entrada.pos[1] + self.entrada.height + 100
        scroll_height = altura - scroll_y - 80
        self.scroll.size = (largura - 360, scroll_height)
        self.scroll.pos = (340, scroll_y)
        # Painel de fundo azul atrás do scroll
        self.painel_fundo.pos = self.scroll.pos
        self.painel_fundo.size = self.scroll.size
PrototipoApp().run()