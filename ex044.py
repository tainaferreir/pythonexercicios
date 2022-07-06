#Calcule o valor a ser pago pelo produto de acordo com a forma de pagamento

p = 599.90
print('Formas de pagamento: \n 1- Á vista \n 2- Á vista no cartão \n 3- 2x no cartão \n 4- 3x ou mais no cartão \n')
f = int(input('Qual a forma de pagamento? '))

if f == 1:
    print('O pagamento sendo a vista em dinheiro ou cheque temos um desconto de 10% ficando R${:.2f}.'.format(p - p*(10/100)))
elif f == 2:
    print('O pagamento sendo á vista no cartão temos um desconto de 5% ficando R${:.2f}.'.format(p - p*(5/100)))
elif f == 3:
    print('O pagamento feito em até 2x é cobrado o preço normal R${}.'.format(p))
elif f == 4:
    print('O valor em 3x ou mais no cartão é cobrado um acréscimo de 20% ficando R${:.2f}'.format(p + p*(20/100)))
    
