vel = float(input('Digite a velocidade registrada em km: '))
if vel <= 80:
    print('Você andou na velocidade permitida e não terá que pagar multa!')

else:
    print('Você estava acima do limite de velocidade de 80km e deverá pagar uma multa de R${:.2f}'.format((vel-80)*7))