import random
# definição das listas
letras = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','Y','Z']
numeros = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','&','+','*']
# apresentação
print('Bem vindo, Vamos gerar sua senha?')
n_letras = int(input('Qual o número de letras você deseja? \n '))
n_simbo = int(input('Qual o número de símbolos você deseja?  \n'))
n_num = int(input('Quantos números você deseja? \n'))
#primeira geração
lista= []
#adiciona por sequência
for i in range(1 , n_letras+1):
    lista+= random.choice(letras)
for i in range(1 , n_simbo+1):
    lista+= random.choice(symbols)
for i in range(1 , n_num+1):
    lista+= random.choice(numeros)
#embaralha a lista
random.shuffle(lista)

#define senha vazia
password = ''

# loop onde char recebe cada valor da lista ate percorrer completamente 
for char in lista:
    password+= char
# mostrar a senha pro user
print(f'Sua senha é : {password}')


