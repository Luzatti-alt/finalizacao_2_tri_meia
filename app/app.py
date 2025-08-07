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
                    size_hint_y=None, height=95, color=(1, 1, 1, 1)
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
                            self.grid.add_widget(Label(text="Cor já existe no sistema",
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

        def add_cor():
            self.pergunta.text = "Digite a nova cor a ser adicionada:"
            self.tipo_acao = "add_cor"
            self.state = 1

        def remove_cor():
            self.pergunta.text = "Digite a nova cor a ser removida:"
            nv_cor = self.entrada.text
            cor_obj = session.query(Cores).filter_by(cor=nv_cor).first()
            if not cor_obj:
                self.grid.add_widget(Label(text=f"Cor «{nv_cor}» não encontrada no estoque", size_hint_y=None, height=30, color=(1, 1, 1, 1)))
                return
            session.delete(cor_obj)
            session.commit()

        def produzir_meia():
            self.pergunta.text = "Digite as cores a serem usadas (separe com vírgula):"
            self.tipo_acao = "prod_meia"
            self.state = 1

        def upt_fio():
            self.pergunta.text = ""
            cores_no_db = session.query(Cores).all()
            cores_disponiveis = {cor.cor.lower(): cor for cor in cores_no_db}
            self.pergunta.text = "remover ou renovar estoque:"
            tipo_upt = self.entrada.text
            if tipo_upt not in ("remover", "renovar"):
                self.grid.add_widget(Label(text="Opção inválida. Digite 'remover' ou 'renovar'", size_hint_y=None, height=30, color=(1, 1, 1, 1)))
                return
            self.pergunta.text = "Digite a cor da lã que será atualizada (1 por vez):"
            qual_upt = self.entrada.text
            if qual_upt not in cores_disponiveis:
                self.grid.add_widget(Label(text=f"Não foi encontrada a cor {qual_upt} no banco de dados", size_hint_y=None, height=30, color=(1, 1, 1, 1)))
                return
            try:
                self.pergunta.text = "Digite o quanto será atualizado(em kg):"
                qnt_upt = float(self.entrada.text)
            except ValueError:
                self.grid.add_widget(Label(text="Valor inválido. Digite um número válido", size_hint altura / 8)
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