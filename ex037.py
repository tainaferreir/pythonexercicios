#Leia um numero inteiro e peça para o usuario escolher a base de conversão 1-binario, 2-octal e 3-hexadecimal

n = int(input('Digite um numero inteiro: '))
print('''Deseja converter esse numero para:
1- Binario 
2- Octal
3- Hexadecimal''')
c = int(input('Converter para: '))

if c == 1:
    print('Em binario seu numero {} fica {}'.format(n, bin(n)[2:])) #[2:] tira a indicação de binario que é 0b, pois começa na terceira variavel
elif c == 2:
    print('Em Octal seu numero {} fica {}'.format(n, oct(n)[2:]))
elif c == 3:
    print('Em Hexadecimal seu numero {} fica {}'.format(n, hex(n)[2:]))
    
