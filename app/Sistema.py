from db import *
import time
on = 1
#comandos
lista_comandos = ["estoque","adicionar cor","remover cor","atualizar cor","produzir meia","desligar"]
#afirmações
confirmacao = ["sim","s","ss","positivo","afirmativo"]
def ver_estoque():
  cores_no_db = session.query(Cores).all()
  for cor in cores_no_db:
   print(f"Cor: {cor.cor}\n Quantidade: {cor.quantidade_cor_kg}kg\n Disponível: {cor.disponivel}\n")
def add_cor():
  nv_cor = input("digite a nova cor a ser adicionada ").lower()
  existe = session.query(Cores).filter_by(cor=nv_cor).first()
  qnt_cor = int(input("digite quantos kilos desta cor(somente o número): "))
  if existe:
    print("Cor já existe no sistema")
  else:
    session.add(Cores(cor=nv_cor,quantidade_cor_kg=qnt_cor,disponivel=True))
    session.commit()
    print("adicionando a cor")
      #criar função que atualize os valores
      #em produção descontar do db se for valido se for invalido vai avisar
def remove_cor():
  nv_cor = input("digite a nova cor a ser adicionada ")
  print("removendo a cor")
  cor_obj = session.query(Cores).filter_by(cor=nv_cor).first()
  if not cor_obj:
    print(f"Cor «{nv_cor}» não encontrada no estoque.")
    return
  session.delete(cor_obj)
  session.commit()
def produzir_meia():
  #tem que criar validação de ter essa cor começei a fazer
  cores_no_db = session.query(Cores.cor).all()
  cores_disponiveis = [cor[0].lower() for cor in cores_no_db]
  print(cores_no_db)
  gauges_possiveis = [84, 96, 108, 120, 144]  # valores inteiros, não string
  qnts_mats = input("Digite as cores a serem usadas (separe com vírgula): ")
  cores = [cor.strip().lower() for cor in qnts_mats.split(',')]
  qnts_mats_conf = input(f"Tem certeza dessas cores: {cores}? (sim/não) ").lower()
  cores_invalidas = [cor for cor in cores if cor not in cores_disponiveis]
  if cores_invalidas:
    print(f"As seguintes cores não estão no banco de dados: {cores_invalidas}")
    return
  else:
    if qnts_mats_conf not in confirmacao:
      print("entendido, voltando ao menu principal")
      return
    try:
      gauge_agulha = int(input("Digite o gauge da agulha (84, 96, 108, 120, 144): "))
    except ValueError:
      print("Valor inválido para gauge. Deve ser um número.")
      return
    if gauge_agulha not in gauges_possiveis:
      print("gauge desconhecido")
      return  # importante sair da função aqui
    conf_gauge_agulha = input(f"Será usado {gauge_agulha}G. Tem certeza? (sim/não) ").lower()
    if conf_gauge_agulha not in confirmacao:
      print("Confirmação recusada. Voltando ao menu principal.")
      return
    try:
      quantidade_meias = int(input("Quantas meias deseja produzir? "))
    except ValueError:
      print("Quantidade inválida.")
      return
    print("\nIniciando produção da meia...")
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
    #converter para kg e descontar do db
    material_total_kg = (material_total_por_cor/1000)
    cores_no_db = session.query(Cores).all()
    cores_disponiveis = {cor.cor.lower(): cor for cor in cores_no_db}
    for cor in cores:
        cor_obj = cores_disponiveis[cor]
        cor_obj.quantidade_cor_kg -= (material_total_por_cor / 1000)
        print(f"Cores '{cor}': novo total — {cor_obj.quantidade_cor_kg:.2f} kg")
        session.commit()
def upt_fio():
    cores_no_db = session.query(Cores).all()
    cores_disponiveis = {cor.cor.lower(): cor for cor in cores_no_db}
    tipo_upt = input("remover ou renovar estoque: ").strip().lower()
    if tipo_upt not in ("remover", "renovar"):
        print("Opção inválida. Digite 'remover' ou 'renovar'")
        return
    qual_upt = input("digite a cor da lã que será atualizada (1 por vez): ").strip().lower()
    if qual_upt not in cores_disponiveis:
        print(f"Não foi encontrada a cor '{qual_upt}' no banco de dados.")
        return
    try:
        qnt_upt = float(input("Digite o quanto será atualizado (em kg): "))
    except ValueError:
        print("Valor inválido. Digite um número válido.")
        return
    cor_obj = cores_disponiveis[qual_upt]
    if tipo_upt == "remover":
        if cor_obj.quantidade_cor_kg - qnt_upt < 0:
            print(f"Erro: não é possível remover {qnt_upt}kg — só há {cor_obj.quantidade_cor_kg}kg em estoque.")
            return
        cor_obj.quantidade_cor_kg -= qnt_upt
        print(f"Removido {qnt_upt}kg de '{qual_upt}'. Novo total: {cor_obj.quantidade_cor_kg:.2f}kg")
    elif tipo_upt == "renovar":
        cor_obj.quantidade_cor_kg += qnt_upt
        print(f"Adicionado {qnt_upt}kg à cor '{qual_upt}'. Novo total: {cor_obj.quantidade_cor_kg:.2f}kg")
    session.commit()
def carregar():
  for i in range(0,2):
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
        case "atualizar cor":
          upt_fio()
          break
        case "help":
          print(lista_comandos)
        case "produzir meia":
          produzir_meia()
          break
        case "desligar":
          on = 0
          print("\nencerrando o programa")
          exit()
          break
        case default:
          print("algo é invalido")
while on ==1:
 Controle_fios()
