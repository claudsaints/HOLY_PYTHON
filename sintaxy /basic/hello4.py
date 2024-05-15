# loops 
#for variavel in algo à percorrer 
frutas = ['maça','banana','pera']
for fruta in frutas:
    print(fruta)
# exemplo com media de altura de pessoas
alt = input().split()
for a in range(0,len(alt)):
    alt[a] = int(alt[a])
# soma
alt_tot = 0
for altura in alt:
    alt_tot+= altura
#total
print(f' O total de altura é: {alt_tot}')
# pessoas
n_pessoas = 0
for n in alt:
    n_pessoas+= 1
print(f'O número de pessoas casdastradas é: {n_pessoas}')
# final
calc_final = round( alt_tot / n_pessoas)
print(f' a média das altura é: {calc_final}')
