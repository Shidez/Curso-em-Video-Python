km = float(input('Digite quantos km a viagem terá: '))
if km <= 200:
    print('Sua viagem de {:.1f}km custará R${:.2f}.'.format(km,km*0.50))
else:
    print('Sua viagem de {:.1f}km custará R$ {:.2f}.'.format(km,km*0.45))