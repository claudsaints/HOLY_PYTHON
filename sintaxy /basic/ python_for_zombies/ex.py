print('1 SOMA DE DOIS NÚMEROS ')
n1 = int(input('Digite um Número'))
n2 = int(input('Digite outro Número'))
print(' A soma Dos Dois Números é: ', n1+n2)

print('2 Digite um valor em Metros Assim Converteremos: ')
metro = float(input('Valor em Metros: '))
print(' A conversão em Milímetros é: ', metro*1000)

print(' 3 Conversão de segundos')
dia = float(input("Digite os dias: "))
hora = float(input("Digite Horas: "))
minu = float(input("Digite minutos: "))
segundos = float(input("Digite os segundos:"))
dia = (dia*86400)
print(dia)
hora = (hora*60**2)
print(hora)
minu = minu*60
print(minu)
totseg = segundos + dia + hora + minu
print('O total em segundos é: ', totseg)

print("4 calculo salárial")
sal = float(input("Digite o seu salário "))
jur = float(input("Digite a porcentagem de aumento: "))
fsal = sal+sal/jur
print(" Seu salário final é : R$ ", fsal)

print("5 calculo de desconto")
mer = float(input("Digite o preço de mercadoria: "))
desc = float(input(" Digite o percentual de desconto: "))
descend = mer - (mer*(desc/100))
print('O PREÇO DO PRODUTO FINAL É DE: R$', descend)

print("6 viagem de carro")
dist = int(input("Digite a ditância da viagem km: "))
veloc = int(input("Digite a velocia média esperada: "))
tempo = dist/veloc
print(" o tempo que será percorido é : ", tempo, "Horas")

print("7 celcios e fahrenheit ")
celcios = float(input("Digite a temperatura em celcios: "))
fah = (celcios*(9/5))+32
print(celcios, " celcios é ", fah, " fahrenheit")

print("8 Fahrenheit para celcios")
fah = float(input("Digite a temperatura em fahrenheit: "))
celcios = (fah-32)/1.8
print(fah, " fahrenheit são ", celcios, " celcios")
           
           
