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
        self.state = 0
        self.tipo_acao = ""
        confirmacao = ["sim", "s", "ss", "positivo", "afirmativo"]

        def ver_estoque():
            self.pergunta.text = ""
            cores_no_db = session.query(Cores).all()
            for cor in cores_no_db:
                self.grid.add_widget(Label(
                    text=f"Cor: {cor.cor}\n Quantidade: {cor.quantidade_cor_kg}kg\n Disponível: {cor.disponivel}",
                    size_hint_y=None, height=140, color=(1, 1, 1, 1)
                ))

        def ao_enviar(instance):
            if self.tipo_acao == "add_cor":
                if self.state == 1:
                    self.nv_cor = self.entrada.text.strip().lower()  # padroniza 
                    if self.nv_cor == "":
                        self.pergunta.text = "Digite uma cor válida!"
                        return
                    existe = session.query(Cores).filter_by(cor=self.nv_cor).first()
                    if existe:
                        self.grid.add_widget(Label(
                            text="Cor já existe no sistema",
                            size_hint_y=None, height=30, color=(1, 1, 1, 1)
                        ))
                        self.tipo_acao = ""
                        self.state = 0
                        self.pergunta.text = ""
                        self.entrada.text = ""
                        return
                    self.entrada.text = ""
                    self.pergunta.text = "Digite quantos quilos desta cor (somente número):"
                    self.state = 2
                elif self.state == 2:
                    qnt_text = self.entrada.text.strip()
                    try:
                        self.qnt_cor = float(qnt_text)
                    except ValueError:
                        self.pergunta.text = "Quantidade inválida! Digite um número válido."
                        return
                    nova_cor = Cores(cor=self.nv_cor, quantidade_cor_kg=self.qnt_cor, disponivel=True)
                    session.add(nova_cor)
                    try:
                        session.commit()
                    except Exception as e:
                        session.rollback()
                        self.grid.add_widget(Label(
                            text=f"Erro ao adicionar cor: {e}",
                            size_hint_y=None, height=30, color=(1, 0, 0, 1)
                        ))
                        return
                    self.grid.add_widget(Label(
                        text=f"Cor '{self.nv_cor}' adicionada com {self.qnt_cor} kg.",
                        size_hint_y=None, height=30, color=(0, 1, 0, 1)
                    ))
                    self.state = 0
                    self.tipo_acao = ""
                    self.pergunta.text = ""
                    self.entrada.text = ""

            if self.tipo_acao == "prod_meia":
                if self.state == 1:
                    # Pergunta cores
                    self.pergunta.text = "Digite as cores a serem usadas (separe com vírgula):"
                    self.state = 2
                    return
                elif self.state == 2:
                    # Processa cores
                    cores_no_db = session.query(Cores.cor).all()
                    cores_disponiveis = [cor[0].lower() for cor in cores_no_db]
                    self.cores_escolhidas = [c.strip().lower() for c in self.entrada.text.split(',')]
                    cores_invalidas = [c for c in self.cores_escolhidas if c not in cores_disponiveis]
                    if cores_invalidas:
                        self.grid.add_widget(Label(
                            text=f"As seguintes cores não estão no banco de dados: {cores_invalidas}",
                            size_hint_y=None, height=30, color=(1,1,1,1)
                        ))
                        self.state = 0
                        self.tipo_acao = ""
                        return
                    self.pergunta.text = f"Tem certeza dessas cores {self.cores_escolhidas}? (sim/não)"
                    self.state = 3
                    return
                elif self.state == 3:
                    if self.entrada.text.lower() not in confirmacao:
                        self.grid.add_widget(Label(
                            text="Entendido, voltando ao menu principal",
                            size_hint_y=None, height=30, color=(1,1,1,1)
                        ))
                        self.state = 0
                        self.tipo_acao = ""
                        return
                    else:
                        self.pergunta.text = "Digite o gauge da agulha (84, 96, 108, 120, 144):"
                        self.state = 4
                        return
                elif self.state == 4:
                    try:
                        self.gauge_agulha = int(self.entrada.text)
                    except ValueError:
                        self.grid.add_widget(Label(
                            text="Valor inválido para gauge.",
                            size_hint_y=None, height=30, color=(1,1,1,1)
                        ))
                        return
                    if self.gauge_agulha not in [84, 96, 108, 120, 144]:
                        self.grid.add_widget(Label(
                            text="Gauge desconhecido",
                            size_hint_y=None, height=30, color=(1,1,1,1)
                        ))
                        return
                    self.pergunta.text = f"Será usado {self.gauge_agulha}G. Tem certeza? (sim/não)"
                    self.state = 5
                    return
                elif self.state == 5:
                    if self.entrada.text.lower() not in confirmacao:
                        self.grid.add_widget(Label(
                            text="Confirmação recusada. Voltando ao menu principal",
                            size_hint_y=None, height=30, color=(1,1,1,1)
                        ))
                        self.state = 0
                        self.tipo_acao = ""
                        return
                    self.pergunta.text = "Quantas meias deseja produzir?"
                    self.state = 6
                    return
                elif self.state == 6:
                    try:
                        quantidade_meias = int(self.entrada.text)
                    except ValueError:
                        self.grid.add_widget(Label(
                            text="Quantidade inválida",
                            size_hint_y=None, height=30, color=(1,1,1,1)
                        ))
                        return
                    # Cálculo de material
                    gauge_base = 96
                    consumo_base = 50
                    fator_consumo = gauge_base / self.gauge_agulha
                    material_total_por_cor = consumo_base * fator_consumo * quantidade_meias
                    for cor in self.cores_escolhidas:
                        self.grid.add_widget(Label(
                            text=f"→ Cor: {cor} será usado aproximadamente {material_total_por_cor:.2f}g de lã",
                            size_hint_y=None, height=30, color=(1, 1, 1, 1)
                        ))
                    # Atualiza banco
                    cores_no_db = session.query(Cores).all()
                    cores_disponiveis = {c.cor.lower(): c for c in cores_no_db}
                    for cor in self.cores_escolhidas:
                    	cor_obj = cores_disponiveis[cor]
                    	material_kg = material_total_por_cor / 1000
                    	if cor_obj.quantidade_cor_kg >= material_kg:
                    		cor_obj.quantidade_cor_kg -= material_kg
                    		self.grid.add_widget(Label(
                    		text=f"Produção estimada concluída para {cor}",
                    		size_hint_y=None,
                    		height=30,
                    		color=(0, 1, 0, 1)))
                    	else:
                    		self.grid.add_widget(Label(
                    		text=f"Não há lã suficiente para a cor {cor} (precisa de {material_kg:.2f}kg, disponível {cor_obj.quantidade_cor_kg:.2f}kg)",
                    		size_hint_y=None,
                    		height=30,
                    		color=(1, 0, 0, 1)
                    		))
                    		session.commit()
                    self.state = 0
                    self.tipo_acao = ""

            if self.tipo_acao == "atualizar":
                cores_no_db = session.query(Cores).all()
                cores_disponiveis = {cor.cor.lower(): cor for cor in cores_no_db}
                if self.state == 1:
                    self.pergunta.text = "remover ou renovar estoque:"
                    self.state = 2
                    return
                elif self.state == 2:
                    tipo_upt = self.entrada.text.lower()
                    if tipo_upt not in ("remover", "renovar"):
                        self.grid.add_widget(Label(
                            text="Opção inválida. Digite 'remover' ou 'renovar'",
                            size_hint_y=None, height=30, color=(1, 1, 1, 1)
                        ))
                        return
                    self.tipo_upt = tipo_upt  # guarda para próximo passo
                    self.pergunta.text = "Digite a cor da lã que será atualizada (1 por vez):"
                    self.state = 3
                    self.entrada.text = ""
                    return
                elif self.state == 3:
                    qual_upt = self.entrada.text.lower().strip()
                    if qual_upt not in cores_disponiveis:
                        self.grid.add_widget(Label(
                            text=f"Não foi encontrada a cor {qual_upt} no banco de dados",
                            size_hint_y=None, height=30, color=(1, 1, 1, 1)
                        ))
                        return
                    self.qual_upt = qual_upt
                    self.pergunta.text = "Digite o quanto será atualizado (em kg):"
                    self.state = 4
                    self.entrada.text = ""
                    return
                elif self.state == 4:
                    try:
                        qnt_upt = float(self.entrada.text)
                    except ValueError:
                        self.grid.add_widget(Label(
                            text="Valor inválido. Digite um número válido",
                            size_hint_y=None, height=30, color=(1, 1, 1, 1)
                        ))
                        return
                    cor_obj = cores_disponiveis[self.qual_upt]
                    if self.tipo_upt == "remover":
                        if cor_obj.quantidade_cor_kg - qnt_upt < 0:
                            self.grid.add_widget(Label(
                                text=f"Erro: Não é possível remover {qnt_upt} kg, só há {cor_obj.quantidade_cor_kg} kg no estoque",
                                size_hint_y=None, height=30, color=(1, 1, 1, 1)
                            ))
                            return
                        cor_obj.quantidade_cor_kg -= qnt_upt
                        self.grid.add_widget(Label(
                            text=f"Removido {qnt_upt} kg de {self.qual_upt}. Novo total: {cor_obj.quantidade_cor_kg:.2f}kg",
                            size_hint_y=None, height=30, color=(1, 1, 1, 1)
                        ))
                    elif self.tipo_upt == "renovar":
                        cor_obj.quantidade_cor_kg += qnt_upt
                        self.grid.add_widget(Label(
                            text=f"Adicionado {qnt_upt} kg da cor {self.qual_upt}. Novo total: {cor_obj.quantidade_cor_kg:.2f} kg",
                            size_hint_y=None, height=30, color=(1, 1, 1, 1)
                        ))
                    session.commit()
                    self.state = 0
                    self.tipo_acao = ""
                    self.pergunta.text = ""
                    self.entrada.text = ""
                    return
            elif self.tipo_acao == "remover_cor":
                if self.state == 1:
                    nv_cor = self.entrada.text.strip().lower()
                    cor_obj = session.query(Cores).filter_by(cor=nv_cor).first()
                    if not cor_obj:
                        self.grid.add_widget(Label(text=f"Cor «{nv_cor}» não encontrada no estoque",size_hint_y=None, height=30, color=(1, 1, 1, 1)
                        ))
                        self.state = 0
                        self.tipo_acao = ""
                        self.pergunta.text = ""
                        self.entrada.text = ""
                        return
                    else:
                        self.cor_para_remover = cor_obj
                        self.pergunta.text = f"Tem certeza que deseja remover a cor '{nv_cor}'? (sim/não)"
                        self.state = 2
                        self.entrada.text = ""
                        return
                elif self.state == 2:
                    if self.entrada.text.strip().lower() in confirmacao:
                        session.delete(self.cor_para_remover)
                        session.commit()
                        self.grid.add_widget(Label(text=f"Cor «{self.cor_para_remover.cor}» removida com sucesso!",size_hint_y=None, height=30, color=(0, 1, 0, 1)))
                    else:
                        self.grid.add_widget(Label(text="Remoção cancelada.",size_hint_y=None, height=30, color=(1, 1, 1, 1)
                        ))
                        self.state = 0
                        self.tipo_acao = ""
                        self.pergunta.text = ""
                        self.entrada.text = ""
                        return

        def add_cor():
            self.pergunta.text = "Digite a nova cor a ser adicionada:"
            self.tipo_acao = "add_cor"
            self.state = 1

        def remove_cor():
            self.pergunta.text = "Digite a nova cor a ser removida:"
            self.tipo_acao = "remover_cor"
            self.state = 1

        def produzir_meia():
            self.pergunta.text = "Digite as cores a serem usadas (separe com vírgula):"
            self.tipo_acao = "prod_meia"
            self.state = 1

        def upt_fio():
            self.pergunta.text = "remover ou renovar estoque:"
            self.tipo_acao = "atualizar"
            self.state = 1            

        altura = Window.height
        largura = Window.width
        layout = FloatLayout()

        with layout.canvas.before:
            Color(0.1, 0.1, 0.2, 1)
            self.bg_rect = Rectangle(pos=layout.pos, size=Window.size)

        def update_bg(*args):
            self.bg_rect.pos = layout.pos
            self.bg_rect.size = Window.size

        layout.bind(pos=update_bg, size=update_bg)

        # Botões
        self.estoque = Button(text='Ver estoque', size_hint=(None, None), size=(300, 100), background_normal="", background_color=(0.2, 0.6, 0.9, 1), pos=(0, altura / 2 + 200))
        self.add_cor = Button(text='Adicionar cor', size_hint=(None, None), size=(300, 100), background_normal="", background_color=(0.2, 0.6, 0.9, 1), pos=(0, altura / 2 + 80))
        self.remover_cor = Button(text='Remover cor', size_hint=(None, None), size=(300, 100), background_normal="", background_color=(0.2, 0.6, 0.9, 1), pos=(0, altura / 2 - 40))
        self.prod_meia = Button(text='Produzir meia', size_hint=(None, None), size=(300, 100), background_normal="", background_color=(0.2, 0.6, 0.9, 1), pos=(0, altura / 2 - 160))
        self.upt_cor = Button(text='Atualizar cor', size_hint=(None, None), size=(300, 100), background_normal="", background_color=(0.2, 0.6, 0.9, 1), pos=(0, altura / 2 - 280))
        self.enviar = Button(text='enviar', size_hint=(None, None), size=(300, 100), background_normal="", background_color=(0.2, 0.6, 0.9, 1), pos=(0, altura / 2 - 280))

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
        self.enviar.bind(on_press=ao_enviar)

        # Painel azul de fundo para scroll
        with layout.canvas.before:
            Color(0.1, 0.3, 0.8, 1)
            self.painel_fundo = Rectangle()

        self.scroll = ScrollView(size_hint=(None, None))
        self.grid = GridLayout(cols=1, size_hint_y=None, padding=10, spacing=10)
        self.grid.bind(minimum_height=self.grid.setter("height"))
        self.scroll.add_widget(self.grid)
        layout.add_widget(self.scroll)

        self.pergunta = Label(text="Pergunta:", size_hint=(None, None), color=(1, 1, 1, 1))
        layout.add_widget(self.pergunta)

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
        self.enviar.pos = (largura - 125, altura / 10)
        self.enviar.size = (100, altura / 10)
        self.pergunta.pos = (340, altura / 8)
        self.pergunta.size = (largura - 360, altura / 10 + 200)
        self.entrada.pos = (340, altura / 10)
        self.entrada.size = (largura - 460, altura / 10)
        scroll_y = self.entrada.pos[1] + self.entrada.height + 100
        scroll_height = altura - scroll_y - 80
        self.scroll.size = (largura - 360, scroll_height)
        self.scroll.pos = (340, scroll_y)
        self.painel_fundo.pos = self.scroll.pos
        self.painel_fundo.size = self.scroll.size

PrototipoApp().run()
