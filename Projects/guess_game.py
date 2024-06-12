from random import randint

EASY_LEVEL = 10
HARD_LEVEL = 5

# FUNÇÃO PARA CHECAR A ESCOLHA DA MAQUINA COM A RESPOSTA DO USUARIO 

def check_resposta(escolha,resposta,tentativa):
    if escolha > resposta:
        print("Muito Baixo")
        return tentativa - 1
    elif escolha < resposta:
        print("Muito Alto")
        return tentativa - 1
    else: 
        print(f'Você acertou. O número que era: {escolha}')

#Função para definir a dificuldade 

def difficulty():
    level = input("Escolha a Dificuldade Escreva 'facil' ou 'dificil' ")
    if level == 'facil':
        return EASY_LEVEL
    else:
        return HARD_LEVEL
    
def jogo():
  #Escolha um número de 0 a 100.
  print("Bem vindo a um jogo de adivinhação!!!")
  print("Eu estou pensando em um número entre 0 a 100")
  escolha = randint(1, 100)
  # teste print(f" {escolha}") 

  tentativas = difficulty()
  #Repitir em um loop 
  resposta = 0
  while resposta != escolha:
    print(f"Você tem {tentativas} tentativas restantes...")

    # Usuario faz uma escolha númerica.
    resposta = int(input("Faça um escolha: "))

    #Diminuir a quantidade das tentivas por um.
    tentativas = check_resposta(escolha, resposta, tentativas)
    if tentativas == 0:
      print("Você esgotou todas as tentativas, você perdeu.")
      return
    elif escolha != resposta:
      print("Tente novamente.")


jogo()
