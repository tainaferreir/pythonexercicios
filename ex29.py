#Leia a velocidade um carro se ultrapassar 80km/h diga que foi multado e pagara uma multa de 7 reais por km
#Print do if escrito em vermelho 
#Print do else escrito em verde

km = int(input('Digite a velocidade em km/h: '))
print ('Sua velocidade é {}km/h'.format(km))
multa = ((km-80)*7)
if  km>=80 :
    print('Voce foi \033[1;31m MULTADO!, Sua multa tem o valor de: R${} \033[m'.format(multa))
else:
    print('\033[1;32m Voce estava dentro do limite!')
