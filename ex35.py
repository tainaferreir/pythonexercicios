#Leia o comprimento de tres retas e diga se forma um triangulo ou não

a = float(input('Digite o primeiro segmento de reta: '))
b = float(input('Digite o segundo segmento de reta: '))
c = float(input('Digite o terceiro segmento de reta: '))

if a < c+b and b < a+c and c < a+b:
    print('O conjunto de retas {}, {} e {} \033[1;32m formam \033[m um triangulo'.format(a,b,c))
else:
    print('O conjunto de retas \033[1;32m não formam \033[m um triangulo')
