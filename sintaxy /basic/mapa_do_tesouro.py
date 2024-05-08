print('''	A	B	C\n1	[]	[]	[]\n2	[]	[]	[]\n3	[]	[]	[]	''')

linha1= [" "," "," "]
linha2= [" "," "," "]
linha3= [" "," "," "]
mapa= [linha1,linha2,linha3]
print("Esconda seu tesouro!!!")
posi = input("Em que posição você quer colocar o tesouro? (Ex: A1)  ")
# transformamos a letra em minúsculo.
letra = posi[0].lower()
# criamos uma lista das letras
abc= ["a","b","c"]
# obtemos a posição onde a letra digitada está na lista.
letra_index = abc.index(letra)
# obtemos o número digitado e subtraimos para obter a posição correta na lista 
numero_index = int(posi[1]) - 1
# vai ser trocado o valor na posição do número pela letra  por x
mapa[numero_index][letra_index] = "x"
# apresentamos na tela.
print(f"{linha1}\n{linha2}\n{linha3}")
