# calculadora do amor
# receber input de dois nome, calcular entre eles quantas vezes as letras de T R U E aparecem, repetir com L O V E e juntas strings da soma das ocorrências, assim obtendo o número de porcentagem...
print ("CALCULADORA DO AMOR S2")
nome1 = input("Digite O Seu Nome: ")
nome2= input("Digite O Nome Do Seu/Sua Paixão: ")
nomes= nome1+nome2
# definir os todas as letras em minúsculas para não ter erros de identificação 
m_nomes= nomes.lower()
# contar utilizando a function count as ocorrências
t = m_nomes.count("t")
r = m_nomes.count("r")
u =	m_nomes.count("u")
e = m_nomes.count("e")
soma_true =t + r + u + e
l =  m_nomes.count("l")
o =  m_nomes.count("o")
v =  m_nomes.count("v")
e =  m_nomes.count("e")
soma_love = l + o + v + e
amor= str(soma_true) + str (soma_love)
amor= int(amor)
# definir casos para o tamanho do amor...
if (amor < 15):
	print (f"O nivel de amor de vocês é {amor}%, parece que alguem precisa de um pouco de sorvete...") 
elif (amor < 50):
	print (f"O nivel de amor de vocês é {amor}%, parece que vocês são otimos amigos.")
elif (amor< 80):
	print (f"O nivel de amor de vocês é {amor}%, vocês formam um otimo casal S2.") 
else: 
	print (f"O nivel de amor de vocês é {amor}%, VOCÊS ESTÃO PERDIDAMENTES APAIXONADOS PORFAVOR CASEM LOGO!!!!")

print("Fim.")  
