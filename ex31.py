d = float(input('Qual a distancia em km da sua viagem? '))
me = (d*0.5)
ma = (d*0.45)
if (d<=200):
    print('Sua viagem tem uma distancia de {}km, e custará R${:.2f}'.format(d,me))
else:
    print('Sua viagem tem uma distancia de {}km e custará R${:.2f}'.format(d,ma))
    
