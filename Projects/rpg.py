def limpatela():
	import os
	os.system('ols' if os.name == 'nt' else 'clear')

def	pausa():
	input('\033[1;33;47mEnter para continuar...\033[m')

def caminho1():
	limpatela()
	print(f'{img4}')
	print('Estranho, um cortador de grama sendo que não a ninguém morando aqui faz meses...\nAlgo está dentro da casa. Vamos entrar pelos fundos e usar o alvejante para eliminar o mal.')
	pausa(),limpatela()
	print(f'{img5}')
	print('você encontra a entidade de costas')
	final = str(input('Digite [1] para atirar ou [2] para não fazer nada'))
	if final == '1':
		print(f'{tiro}')
		pausa()
		limpatela()
		print('Vocês conseguiram eliminar o mal da face da terra, mas ainda temos que lidar com problemas diários\nNão sabemos até quando a paz vai durar, até lá continue dando o seu melhor.')
	elif final =='2':
		morte()
  
	
	
def morte():
	limpatela()
	print(f'{img3}')
	print('Game Over\nA entidade absorveu sua vida')
	
img1 = ('''                           
                                          .------.
                                         :|||"""`.`.
                                         :|||     7.`.
                      .===+===+===+===+===||`----L7'-`7`---.._
                      []                  || ==       |       """-.
                      []...._____.........||........../ _____ ____|
                     c\____/,---.\_       ||_________/ /,---.\_  _/
                      /_,-/ ,-. \ `._____|__________||/ ,-. \ \_[
                          /\ `-' /                    /\ `-' /
                            `---'                       `---' ''')
img2 = ('''
                   )
                 _(
             ___|_|_________
            /___|_|_________1
       ()  /_________________1
   `'.()))/___________________1'-.'`'.
  .,'(())()   ____     ____  |,.'     '-.
     )(()))  |)~~(|   |)~~(| |. '-. ()`'.
    ()()(()) ||__||   ||__|| | `'.,(())
   ())()(()))________________|___ ()))()
   ()((())()))| | | | | | | | | | (()()))
  ()))(()()())|_|_|_|_|_|_|_|_|_|)(()(()
  (()((())(()-------------------|(())(())
  ~^~ ^" ^"  ^~^   ^"   ~^~    ^~^~(()(()
  ^"     ^~^   ~^~   ^"    ^~^   ~~^~""^ ''')
img3 = ('''\033[31m
   .:'                                  `:.
  ::'                                    `::
 :: :.                                 .: ::
  `:. `:.             .             .:'  .:'
   `::. `::           !           ::' .::'
       `::.`::.    .' ! `.    .::'.::'
         `:.  `::::'':!:``::::'   ::'
         :'*:::.  .:' ! `:.  .:::*`:
        :: HHH::.   ` ! '   .::HHH ::
       ::: `H TH::.  `!'  .::HT H' :::
       ::..  `THHH:`:   :':HHHT'  ..::
       `::      `T: `. .' :T'      ::'
         `:. .   :         :   . .:'
           `::'               `::'
             :'  .`.  .  .'.  `:
             :' ::.       .:: `:
             :' `:::     :::' `:
              `.  ``     ''  .'
               :`...........':
               ` :`.     .': '
                `:  `"""'  :' ''')
img4 = ('''\033[32m
		
            ********
        ****************
      *******************
      ********************
       ********************
          ||   //  ********
           ||\//  *******
             ||\////
              |||//                       ,
              |||||                    __/
  ,,,,,,,,,,,//||||\,,,,,,,,,,,,,,,,,,o==o ''')
img5 = ('''\033[35m 
                              /^\/^|
                             \-----|
                         _---'---~~~~-_
                          ~~~|~  ~|~~~~
                             (/_  /~~--
                           \~ \  /  /~
                         __~\  ~ /   ~~----,
                         \    | |       /  z
                         /|   |/       |    |
                         | | | o  o     /~   |
                       _-~_  |        ||  \  /
                      (// )) | o  o    \z---'
                      //_- |  |          z
                     //   |____|\______\__z
                     ~      |   / |    |
                             |_ /   \ _|
                           /~___|  /____\       ''')
tiro= ('''\033[34m
                                                      ::
                                                    ::  ::_____
                                                      ::__     |\___
                                                          :: _ /    \   
  _ _  __________=__            _   ___        _   ___     |     ::\  \     
   zzz@([____]_____()  BANG!   |_| |___)      (_| |___)    ||\   ::::  \__     
  _/\|-[____]                                              | _           @|
 /____ /(( )                                                \   /----____|
 \___|'----'                                                 | | -\/|/|/|/         
                                                             |  \ |\|\|\|
	                                                           |    ______| ''')


print ('\033[1;33;41m RPG by:claudsaints, artes de: https://ascii.co.uk/art\33[m')
print (' Se a tela parar presione return, se digitar um comando errado deve-se reiniciar.Boa Jogatina. ')
print ('''\033[31m 
                            o
                            M   o     oM""""""""ooo
                            M   M   MM"           M
                           M"   M   MM  o"""""M   M
                          M"    M   MM  Mo    M   M
                      oM""      "M  MM    ""  M   M
                  ooM""          "M   ""Moooo"    M
                 M""              "Moooooo     oMM"
                 M                       """""""
                 M
                 M                           oooooooo
                 Moo                   oM"""""
                 oMMo               MM""
                oM  ""Mo        oooM""
               oM       """""""""
              M"
            MM"
          oM""
         o"                    
     ooo""
    ""
''')
pausa()
print('\033[1;30mSociedade das rosas 1999.\nCaptão você está bem?\nBom não importa, temos que investigar aquela casa.')
print('Você deve estar se perguntando, o que significa tudo isso... bom pelo visto está com falhas após à colisão...\nNo caminho lhe explico agora temos que ir.')
print(f'{img1}')
print('Somos investigadores paranormais, hoje foi reportado que um ser está atormentando uma família, você se lembra disso?\nDroga, ontem você foi espancado pelos ladrões... mas já resolvemos. Eles foram, se que você me entende "Pulverizados" . ')
pausa()
limpatela()
print(f'{img2}')
print('Chegamos, como você está no comando o que você vai fazer? ')
print('\033[1;33;41mDigite [1] para investigar ou [2] para entrar\033[m')
escolha = str(input(''))
if escolha == '1' :
	caminho1()
elif escolha =='2':
	morte()
else:
	print('\033[1;33;41mGame Over sua escolha não existe assim como você\033[m')
	
	




	
	
