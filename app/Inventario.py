class Inventario:
    #atributos (variáveis) métodos (funções)
    #objetos são instâncias da classe
    tipo = ["verde","azul","vermelho"] #lista com as cores
    #fazer a lista/atributo herdar metodo
    def item(self,tipo_nome)->None:
        super().item(tipo_nome)
        self.tipo_nome = tipo_nome
        print(tipo_nome)
    def quantidade_estoque(self,qnt)->None:
        super().quantidade_estoque(qnt)#permitir a herança
        #valores no inventario
        self.qnt = qnt
        print(qnt)
    def controle(self):
        act = input("Digite a ação desejada")
        #temp
        #fazer +- com o desing para ver qnt sera gasto
        while(True):
            match act:
                case add_cor:
                    print("adicionando cor")
                case remover_cor:
                    print("removendo cor")
                    #if remover_cor not in tipo: nn existe esta cor no estoque
                case restock:
                    print("restocando {o que sera restocado}")
                    #ver a qnt e qual cor
                    #add o restock de X itens de ____
                case venda:
                    print("foi vendido {} unidades atualizando valores")
                    #remover X do stock
            #sistema de controle teminal(dps vou fazer aparecer no kivy)
