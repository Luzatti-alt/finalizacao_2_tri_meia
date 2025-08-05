from db import *
import time
on = 1
#comandos
lista_comandos = ["estoque","adicionar cor","remover cor","produzir meia","desligar"]
#afirmações
confirmacao = ["sim","s","ss","positivo","afirmativo"]
def ver_estoque():
  cores_no_db = session.query(Cores).all()
  for cor in cores_no_db:
   print(f"Cor: {cor.cor}\n Quantidade: {cor.quantidade_cor_kg}kg\n Disponível: {cor.disponivel}\n")
def add_cor():
  nv_cor = input("digite a nova cor a ser adicionada ")
  qnt_cor = input("digite quantos kilos desta cor(somente o número): ")
  print("adicionando a cor")
  cores = Cores(cor=nv_cor,quantidade_cor_kg=qnt_cor,disponivel=True)
  session.add(cores)
  session.commit()
def remove_cor():
  nv_cor = input("digite a nova cor a ser adicionada ")
  print("removendo a cor")
  cor_obj = session.query(Cores).filter_by(cor=nv_cor).first()
  if not cor_obj:
    print(f" Cor «{nv_cor}» não encontrada no estoque.")
    return
  session.delete(cor_obj)
  session.commit()
def produzir_meia():
  qnts_mats = input("digite a quantidade de cores a ser usada: ")
  qnts_mats_conf = input(f"tem certeza dessa quantidade {qnt_mat}? ").lower()
  if qnts_mats_conf in confirmacao:
    tipo_agulha = input("digite o tipo de agulha que será usada na criação da meia")
    conf_tipo_agulha = input(f"será usada {tipo_agulha} tem certeza que o tipo certo está sendo utilizado")
    if conf_tipo_agulha in confirmacao:
      print("iniciando produção da meia")
      mat_usado = ()#calculo
      #ver o tipo de agulha e criara uma estimativa de material gasto
  else:
    print("voltando ao menu principal")
    #aqui tera o calculo de qnts de cada cor sera usada removera do valor do que tem
    #se passar do limite ele avisa que não sera possivel produzir a meia com a qnt de recurso atuais
def carregar():
  for i in range(0,5):
    print("\rcarregando dados.",end="")
    time.sleep(0.3)
    print("\rcarregando dados..",end="")
    time.sleep(0.3)
    print("\rcarregando dados...",end="")
    time.sleep(0.3)
def Controle_fios():
  global on
  carregar()
  while True:
      esc = input("\nDados do estoque de meia carregado \n O que deseja fazer(digite help para ver a lista de comandos): ").lower()
      match esc:
        case "estoque":
          print("checkando o estoque\n")
          ver_estoque()
          break
        case "remover cor":
          remove_cor()
          break
        case "adicionar cor":
          add_cor()
          break
        case "help":
          print(lista_comandos)
        case "produzir meia":
          produzir_meia()
          break
        case "desligar":
          on = 0
          print("\n encerrando o programa")
          exit()
          break
        case default:
          print("algo é invalido")
while on ==1:
 Controle_fios()
