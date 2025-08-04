#public Controle_meia(): #array/lista de cores e atribuir essas cores como objs ou via json
import time
on = 1
#dps fazer/colocar em um db
cores = ["vermelho","verde","amarelo","azul"]
#comandos
lista_comandos = ["estoque","adicionar cor","remover cor","produzir meia","desligar"]
#afirmações
confirmacao = ["sim","s","ss","positivo","afirmativo"]
def ver_estoque():
  print("core disponiveis: \n")
  print(cores)
def add_cor():
  nv_cor = input("digite a nova cor a ser adicionada ")
  cores.append(nv_cor)
  print("adicionando a cor")
def remove_cor():
  nv_cor = input("digite a nova cor a ser adicionada ")
  cores.remove(nv_cor)
  print("removendo a cor")
def produzir_meia():
  qnt_mat = input("digite a quantidade de cores a ser usada: ")
  qnt_mat_conf = input(f"tem certeza dessa quantidade {qnt_mat}? ").lower()
  if qnt_mat_conf in confirmacao:
    tipo_agulha = input("digite o tipo de agulha que será usada na criação da meia")
    conf_tipo_agulha = input(f"será usada {tipo_agulha} tem certeza que o tipo certo está sendo utilizado")
    if conf_tipo_agulha in confirmacao:
      print("iniciando produção da meia")
      #ver o tipo de agulha e criara uma estimativa de material gasto
  else:
    print("voltando ao menu principal")
    #aqui tera o calculo de qnts de cada cor sera usada removera do valor do que tem
    #se passar do limite ele avisa que não sera possivel produzir a meia com a qnt de recurso atuais
def carregar():
  for i in range(0,5):
    print("\rcarregando dados.",end="")
    time.sleep(0.5)
    print("\rcarregando dados..",end="")
    time.sleep(0.5)
    print("\rcarregando dados...",end="")
    time.sleep(0.5)
def Controle_fios():
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
          print("encerrando o programa")
          exit()
          break
        case default:
          print("algo é invalido")                                                                                                                                                                                                                                                                                                                   #iniciar prototipo
if on == 1:
  Controle_fios()
