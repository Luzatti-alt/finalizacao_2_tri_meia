from db import *
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
        confirmacao = ["sim", "s", "ss", "positivo", "afirmativo"]
        def ver_estoque():
            cores_no_db = session.query(Cores).all()
            for cor in cores_no_db:
                self.grid.add_widget(Label(text=f"Cor: {cor.cor}\n Quantidade: {cor.quantidade_cor_kg}kg\n Disponível: {cor.disponivel}\n", size_hint_y=None, height=30, color=(1, 1, 1, 1)))
        def add_cor():
            self.pergunta = Label(text="Digite a nova cor a ser adicionada:", size_hint=(None, None), color=(1, 1, 1, 1))
            existe = session.query(Cores).filter_by(cor=nv_cor).first()
            self.pergunta = Label(text="Digite quantos kilos desta cor(somente o número):", size_hint=(None, None), color=(1, 1, 1, 1))
            if existe:
                self.grid.add_widget(Label(text="Cor já existe no sistema", size_hint_y=None, height=30, color=(1, 1, 1, 1)))
            else:
                session.add(Cores(cor=nv_cor, quantidade_cor_kg=qnt_cor, disponivel=True))
                session.commit()
                self.grid.add_widget(Label(text=f"adicionando a cor", size_hint_y=None, height=30, color=(1, 1, 1, 1)))
        def remove_cor():
            self.pergunta = Label(text="Digite a nova cor a ser removida:", size_hint=(None, None), color=(1, 1, 1, 1))
            print("removendo a cor")
            cor_obj = session.query(Cores).filter_by(cor=nv_cor).first()
            if not cor_obj:
                self.grid.add_widget(Label(text=f"Cor «{nv_cor}» não encontrada no estoque", size_hint_y=None, height=30, color=(1, 1, 1, 1)))
                return
            session.delete(cor_obj)
            session.commit()
        def produzir_meia():
            cores_no_db = session.query(Cores.cor).all()
            cores_disponiveis = [cor[0].lower() for cor in cores_no_db]
            gauges_possiveis = [84, 96, 108, 120, 144]
            self.pergunta = Label(text="Digite as cores a serem usadas (separe com vírgula):", size_hint=(None, None), color=(1, 1, 1, 1))
            cores = [cor.strip().lower() for cor in qnts_mats.split(',')]
            self.pergunta = Label(text=(f"Tem certeza dessas cores {cores}?(sim/não)"), size_hint=(None, None), color=(1, 1, 1, 1))
            cores_invalidas = [cor for cor in cores if cor not in cores_disponiveis]
            if cores_invalidas:
                self.grid.add_widget(Label(text=f"As seguintes cores não estão no banco de dados: {cores_invalidas}", size_hint_y=None, height=30, color=(1, 1, 1, 1)))
                return
            else:
                if qnts_mats_conf not in confirmacao:
                    self.grid.add_widget(Label(text=f"entendido, voltando ao menu principal", size_hint_y=None, height=30, color=(1, 1, 1, 1)))
                    return
                try:
                    self.pergunta = Label(text="Digite o gauge da agulha (84,96,108,120,144)", size_hint=(None, None), color=(1, 1, 1, 1))
                except ValueError:
                    self.grid.add_widget(Label(text="Valor inválido para gauge. Deve ser um número.", size_hint_y=None, height=30, color=(1, 1, 1, 1)))
                    return
                if gauge_agulha not in gauges_possiveis:
                    self.grid.add_widget(Label(text=f"gauge desconhecido", size_hint_y=None, height=30, color=(1, 1, 1, 1)))
                    return
                self.pergunta = Label(text=(f"Será usado {gauge_agulha}G. Tem certeza?(sim/não):"), size_hint=(None, None), color=(1, 1, 1, 1))
                if conf_gauge_agulha not in confirmacao:
                    self.grid.add_widget(Label(text=f"Confirmação recusada. Voltando ao menu principal", size_hint_y=None, height=30, color=(1, 1, 1, 1)))
                    return
                try:
                    self.pergunta = Label(text="Quantas meias deseja produzir?", size_hint=(None, None), color=(1, 1, 1, 1))
                except ValueError:
                    self.grid.add_widget(Label(text="Quantidade inválida", size_hint_y=None, height=30, color=(1, 1, 1, 1)))
                    return
                self.grid.add_widget(Label(text="iniciando produção da meia", size_hint_y=None, height=30, color=(1, 1, 1, 1)))
                # DADOS FIXOS
                gauge_base = 96
                consumo_base = 50
                fator_consumo = gauge_base / gauge_agulha
                material_total_por_cor = consumo_base * fator_consumo * quantidade_meias
                for cor in cores:
                    self.grid.add_widget(Label(text=f"→ Cor: {cor} será usado aproximadamente {material_total_por_cor:.2f}g de lã", size_hint_y=None, height=30, color=(1, 1, 1, 1)))
                self.pergunta = Label(text="Produção estimada concluída", size_hint=(None, None), color=(1, 1, 1, 1))
                cores_no_db = session.query(Cores).all()
                cores_disponiveis = {cor.cor.lower(): cor for cor in cores_no_db}
                for cor in cores:
                    cor_obj = cores_disponiveis[cor]
                    cor_obj.quantidade_cor_kg -= (material_total_por_cor / 1000)
                    self.grid.add_widget(Label(text=f"Cores {cor}: novo total - {cor_obj.quantidade_cor_kg:.2f} kg", size_hint_y=None, height=30, color=(1, 1, 1, 1)))
                    session.commit()
        def upt_fio():
            cores_no_db = session.query(Cores).all()
            cores_disponiveis = {cor.cor.lower(): cor for cor in cores_no_db}
            self.pergunta = Label(text="remover ou renovar estoque:", size_hint=(None, None), color=(1, 1, 1, 1))
            if tipo_upt not in ("remover", "renovar"):
                self.grid.add_widget(Label(text="Opção inválida. Digite 'remover' ou 'renovar'", size_hint_y=None, height=30, color=(1, 1, 1, 1)))
                return
            self.pergunta = Label(text="Digite a cor da lã que será atualizada (1 por vez):", size_hint=(None, None), color=(1, 1, 1, 1))
            if qual_upt not in cores_disponiveis:
                self.grid.add_widget(Label(text=f"Não foi encontrada a cor {qual_upt} no banco de dados", size_hint_y=None, height=30, color=(1, 1, 1, 1)))
                return
            try:
                self.pergunta = Label(text="Digite o quanto será atualizado(em kg):", size_hint=(None, None), color=(1, 1, 1, 1))
            except ValueError:
                self.grid.add_widget(Label(text="Valor inválido. Digite um número válido", size_hint_y=None, height=30, color=(1, 1, 1, 1)))
                return
            cor_obj = cores_disponiveis[qual_upt]
            if tipo_upt == "remover":
                if cor_obj.quantidade_cor_kg - qnt_upt < 0:
                    self.grid.add_widget(Label(text=f"Erro: Não é possível remover {qnt_upt} kg, só há {cor_obj.quantidade_cor_kg} kg no estoque", size_hint_y=None, height=30, color=(1, 1, 1, 1)))
                    return
                cor_obj.quantidade_cor_kg -= qnt_upt
                self.grid.add_widget(Label(text=f"Removido {qnt_upt} kg de {qual_upt}. Novo total: {cor_obj.quantidade_cor_kg:.2f}kg", size_hint_y=None, height=30, color=(1, 1, 1, 1)))
            elif tipo_upt == "renovar":
                cor_obj.quantidade_cor_kg += qnt_upt
                self.grid.add_widget(Label(text=f"Adicionado {qnt_upt} kg da cor {qual_upt}. Novo total: {cor_obj.quantidade_cor_kg:.2f} kg", size_hint_y=None, height=30, color=(1, 1, 1, 1)))
            session.commit()
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
        self.enviar = Button(
            text='enviar',
            size_hint=(None, None),
            size=(300, 100),
            background_normal="",
            background_color=(0.2, 0.6, 0.9, 1),
            pos=(0, altura / 2 - 280)
        )
        layout.add_widget(self.enviar)
        layout.add_widget(self.estoque)
        layout.add_widget(self.add_cor)
        layout.add_widget(self.remover_cor)
        layout.add_widget(self.prod_meia)
        layout.add_widget(self.upt_cor)
        self.estoque.bind(on_press=lambda instance: ver_estoque())
        self.add_cor.bind(on_press=lambda instance: add_cor())
        self.remover_cor.bind(on_press=lambda instance: remove_cor())
        self.prod_meia.bind(on_press=lambda instance: produzir_meia())
        self.upt_cor.bind(on_press=lambda instance: upt_fio())
        # Painel azul de fundo para scroll
        with layout.canvas.before:
            Color(0.1, 0.3, 0.8, 1)
            self.painel_fundo = Rectangle()
        # ScrollView com conteúdo
        self.scroll = ScrollView(size_hint=(None, None))
        self.grid = GridLayout(cols=1, size_hint_y=None, padding=10, spacing=10)
        self.grid.bind(minimum_height=self.grid.setter("height"))
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
        self.enviar.pos = (largura - 125,altura/10)
        self.enviar.size = (100,altura/10)
        self.pergunta.pos = (340, altura/8)
        self.pergunta.size = (largura - 360, altura/10+200)
        self.entrada.pos = (340, altura/10)
        self.entrada.size = (largura - 460, altura/10)
        # ScrollView
        scroll_y = self.entrada.pos[1] + self.entrada.height + 100
        scroll_height = altura - scroll_y - 80
        self.scroll.size = (largura - 360, scroll_height)
        self.scroll.pos = (340, scroll_y)
        # Painel de fundo azul atrás do scroll
        self.painel_fundo.pos = self.scroll.pos
        self.painel_fundo.size = self.scroll.size
PrototipoApp().run()
