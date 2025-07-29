class Inventario:
    #atributos (variáveis) métodos (funções)
    #objetos são instâncias da classe
    tipo = ["verde","azul","vermelho"] #lista com as cores
    #fazer a lista/atributo herdar metodo
    def item(self,tipo_nome)->None:
        super().item(tipo_nome)
        self.tipo_nome = tipo_nome
        print(tipo_nome)
    def quantidade(self,qnt)->None:
        super().quantidade(qnt)#permitir a herança
        #valores no inventario
        self.qnt = qnt
        print(qnt)
    def controle(self):
        print("a")
        act = input("Digite a ação desejada")
        #temp
        while(True):
            act
            #sistema de controle teminal(dps vou fazer aparecer no kivy)
