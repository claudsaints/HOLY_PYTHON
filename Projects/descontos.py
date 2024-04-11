# Calcular dívidas e descontos
print("Bem vindo à Calculadora De Descontos!!!")
divida = float(input("Qual é o valor total de sua Dívida? R$"))
desconto = float(input("Qual o percentual de desconto? "))
desconto = desconto/100
div = int(input("Quantas pessoas vão pagar? "))
desc = divida - (divida*desconto)
print("O preço de sua dívida com desconto aplicado: R$", desc)
final = desc/div
print("O preço a ser pago por pessoa(", div, "): R$", final)





