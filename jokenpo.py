#Pedra, papel e tesoura com o computador

import random
from time import sleep
print('\033[1;30;45mVAMOS JOGAR JOKENPO? VAI, VOCE COMEÇA!\033[m')
op = ('PEDRA', 'PAPEL', 'TESOURA')
pc = (random.randint(0,2))
print('''Opções: 
0-PEDRA
1-PAPEL
2-TESOURA''')
j1 = int(input('Qual a sua jogada? '))
print('='*20)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
print ('='*20)
sleep(2)
print('VOCE JOGOU {}'.format(op[j1]))
print('EU JOGUEI {}'.format(op[pc]))
print('='*20)
sleep(1)

if pc == 0:
    if j1 == 0:
        print('VISH EMPATOU, VAMOS DENOVO?')
    elif j1 == 1:
        print('PAPEL EMBRULHA PEDRA, \033[1;31mVOCE GANHOU!')
    elif j1 == 2:
        print('PEDRA QUEBRA TESOURA,\033[1;31mEU GANHEI!')
elif pc == 1:
    if j1 == 0:
        print('PAPEL EMBRULHA PEDRA, \033[1;31mEU GANHEI! ')
    elif j1 == 1:
        print('VISH EMPATOU,VAMOS DENOVO?')
    elif j1 == 2:
        print('TESOURA CORTA PAPEL, \033[1;31mVOCE GANHOU!')
elif pc == 2:
    if j1 == 0:
        print('PEDRA QUEBRA TESOURA, \033[1;31mVOCE GANHOU!')
    elif j1 == 1:
        print('TESOURA CORTA PAPEL, \033[1;31mEU GANHEI!')
    elif j1 == 2:
        print('VISH EMPATOU, VAMOS DENOVO?')
