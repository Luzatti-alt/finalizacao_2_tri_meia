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
    # INPUT cores
    qnts_mats = input("Digite as cores a serem usadas (separe com vírgula): ")
    cores = [cor.strip().lower() for cor in qnts_mats.split(',')]
    qnts_mats_conf = input(f"Tem certeza dessas cores: {cores}? (sim/não) ").lower()
    if qnts_mats_conf not in confirmacao:
        print("Algo inválido, voltando ao menu principal.")
        return
    # INPUT gauge
    try:
        gauge_agulha = int(input("Digite o gauge da agulha (ex: 84, 96, 108, 120, 144): "))
    except ValueError:
        print("Valor inválido para gauge. Deve ser um número.")
        return
    conf_gauge_agulha = input(f"Será usado {gauge_agulha}G. Tem certeza? (sim/não) ").lower()
    if conf_gauge_agulha not in confirmacao:
        print("Confirmação recusada. Voltando ao menu principal.")
        return
    # INPUT quantidade de meias
    try:
        quantidade_meias = int(input("Quantas meias deseja produzir? "))
    except ValueError:
        print("Quantidade inválida.")
        return
    print("\n Iniciando produção da meia...")
    # DADOS FIXOS
    gauge_base = 96       # base para calcular o fator de consumo
    consumo_base = 50     # gramas por meia com gauge_base
    # Cálculo do fator de consumo
    fator_consumo = gauge_base / gauge_agulha
    material_total_por_cor = consumo_base * fator_consumo * quantidade_meias
    # Simulação de gasto por cor
    for cor in cores:
        print(f"→ Cor '{cor}': será usado aproximadamente {material_total_por_cor:.2f}g de lã.")
    print("\n✅ Produção estimada concluída.")
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
