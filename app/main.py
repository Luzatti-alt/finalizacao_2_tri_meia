from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout  # Importando o layout
from kivy.core.window import Window
from kivy.graphics import Rectangle, Color  # Onde ficará o design

# Classe que cria o widget com o Canvas
class DesenhoWidget(FloatLayout):
    def __init__(self, **kwargs):
        super(DesenhoWidget, self).__init__(**kwargs)
        # Inicializar o retângulo
        self.retangulo = None
        self.redesenhar_retangulo()  # Redesenha o retângulo ao iniciar a classe

        # Conectar a função on_size à mudança de tamanho da janela
        Window.bind(on_resize=self.redesenhar_retangulo)

    def redesenhar_retangulo(self, *args):
        """Função que redesenha o retângulo quando a janela for redimensionada"""
        largura = Window.width
        altura = Window.height

        # Usando o Canvas para desenhar o retângulo
        with self.canvas:
            self.canvas.clear()  # Limpa o canvas antes de redesenhar
            Color(1, 1, 1)  # Define a cor branca (usando valores RGB entre 0 e 1)
            # Desenha o retângulo com as novas dimensões
            self.retangulo = Rectangle(pos=(100, 100), size=(largura / 1.35, altura / 1.35))

class Prototipo(App):
    def build(self):
        altura = Window.height
        largura = Window.width
        layout = FloatLayout()

        # Função para desenhar os componentes
        def draw():
            # Botão da IA para gerar imagem
            IA = Button(
                text='IA geradora de imagem',
                size_hint=(None, None),
                size=(200, 50),
                pos=(largura - 200, altura - 50)
            )
            IA.bind(on_press=self.gen_img)  # Ação ao pressionar o botão

            # Botão para enviar o design
            enviar = Button(
                text='Enviar design',
                size_hint=(None, None),
                size=(200, 50),
                pos=(largura / 2 - 100, altura / 8 - 75)  # Corrigido para centralizar
            )

            # Criando e adicionando o widget com o Canvas
            desenho_widget = DesenhoWidget()
            layout.add_widget(desenho_widget)  # Adicionando o widget de desenho ao layout
            layout.add_widget(enviar)  # Adicionando o botão de enviar ao layout
            layout.add_widget(IA)  # Adicionando o botão da IA ao layout

        draw()  # Chamando a função para desenhar os componentes

        return layout

    def gen_img(self, instance):
        altura = Window.height
        largura = Window.width
        layout = self.root  # Pegando o layout principal

        # Limpa todos os widgets da tela (remover tudo)
        layout.clear_widgets()

        # Após limpar a tela, cria um novo layout com o conteúdo desejado
        # Neste exemplo, só vou adicionar o botão "Enviar design" novamente.
        enviar = Button(
            text='Enviar design',
            size_hint=(None, None),
            size=(200, 50),
            pos=(largura / 2 - 100, altura / 8 - 25)
        )
        layout.add_widget(enviar)  # Adicionando o botão de enviar

        # Aqui você pode adicionar o conteúdo da função gen_img,
        # como desenhar novos gráficos, imagens ou outros widgets.

        # Para fins de exemplo, vou redesenhar o retângulo
        desenho_widget = DesenhoWidget()
        layout.add_widget(desenho_widget)  # Adiciona o novo conteúdo com o Canvas

# Inicia o aplicativo
Prototipo().run()
