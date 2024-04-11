# conditional statements, se e senão em português
# neste exemplo se a altura do usuário for maior que 1m e 20cm ele pode ir à montanha_russa
print ("Welcome to the rollercoaster!!")
height = int(input("what's your height in cm? "))
# if sempre necessita de um valor booleano true ou false.
# se o usuário pode andar no brinquedo, verificamos sua ídade para definir o pagamento...
if height > 120:
	print("you can ride the rollercoaster!")
	age = int(input("How odder are you? "))
	if age<12:
		print("Please, pay $5")
	elif age<=18:
		print("Please, pay $10")
	else:
		print("Plese, pay $20")
else: 
	print("Sorry,you can have to go taller before you can ride")  
clear()
print("Linguagem Definida como Português Brasil")
print("Após sair da montanha russa você ficou com fome.\nVamos comer um pizza!!!... \n Abaixo temos os valores e sabores... ")
print("Bem Vindo a Pizzaria!!!"),
print("Sabor 1: Mussarela Preço: R$ 20,00 \nSabor 2: Frango    Preço: R$ 25,00 \nSabor 3: Vegana    Preço: R$ 28,50 \nAdicionais: \nMulti Sabores de Queijos R$ 8,00 \nMolho especial R$ 10,50")
tipo = input("Qual Sabor Vocẽ Deseja?")
apagar= 0
if tipo=="Mussarela":
	apagar=20
elif tipo=="Frango":
	apagar=25
elif tipo=="Vegana":
	apagar=28.5
else:
	print("Não temos este Sabor")
if apagar!=0:
	tipo= input("Vai querer adicional? [S/N]")
if tipo=="S":
	tipo= input("Qual Adicional? [molho especial/multi queijos]")
	if tipo=="molho especial":
		apagar+=10.5
	elif tipo=="multi queijos":
		apagar+= 8
	else:
		print("Desculpe somente temos os dois tipos de adicionais")
print("O total à ser pago é: R$",apagar)
	
