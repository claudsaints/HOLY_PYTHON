# pedra papel tesoura
# importe e crie as var das escolhas...
# coloque-as em uma lista(vetor)
import random
tesoura = ('''
 _	    
(_)#   @@@@@@@@
 _  @#@--------@>
(_)#   @@@@@@@@ ''')
    
pedra = (''' 
    ____
  _/ _@@\\
 / __@@@@\\
 \\@@@@@@@/   ''')
 
papel = ('''
   _____
  O-_____-O
  /      /
 /_____ /
O-_____-O ''')
escolhas = [pedra,papel,tesoura]
# exiba na tela o inicio...
# defina um input com escolhas baseado na lista...
# a var machine vai receber um número entre 0 e 2.
# após isso exiba na tela a escolha do jogador e da máquina.
# defina os casos.
print ('JoKenPo')
escolha = int(input('Digite [0] para pedra, [1] para papel ou [2] para tesoura...'))
machine = random.randint(0,2)
print (f'Sua escolha: {escolhas[escolha]}\n')
print (f' O computador escolheu: {escolhas[machine]}\n')
# primeiro verificamos se os números escolhido estão fo da range de escolha;
# após isso, vericamos o caso pedra e tesoura, da máquina e do jogador obtendo resultados diferentes;
# seguindo a análise vai ser apena do papel e tesoura; 
# caso a máquina escolha pedra e você papel, sua escolha vai ser maior resultando na vitória. do mesmo modo ao contrário;
# caso escolha papel e a máquina tesoura, a escolha da máquina vai ser maior logo você perdeu;
# e se escolher tesoura e a máquina papel vai resultar na vitória;
# e por fim caso escolha seja igual resulta em empate.
if escolha < 0 or escolha>=3:
	print('Você digitou um número invalido ')
elif escolha == 0 and machine == 2:
	print('Você Venceu!!!')
elif machine == 0 and escolha ==2:
	print('Você Perdeu!!')
elif machine > escolha:
	print('Você Perdeu!!')
elif escolha > machine:
	print('Você Venceu!!')
elif machine == escolha:
	print('Empate.')



