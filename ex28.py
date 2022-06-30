#Faça o PC pensar em numero entre 0 e 5 e peça pro usuario tentar acertar mostrando se acertou ou não

import random
n = int(input('Voce consegue acertar o numero que eu pensei? Digite-o: '))
x = (random.randint(0,5))
print('=~=' *20)
print ('O numero da vez é {}'.format(x))
print('=~=' *20)
if n == x:
    print('\033[1;35mPARABÉNS, você acertou!')
else:
    print ('\033[1;33mVocê errou, tente novamente!')
