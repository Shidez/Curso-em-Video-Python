print ('CALCULE SEU IMC:')
p = float(input('Digite seu peso em kg: '))
a = float(input('Digite sua altura em m: '))

IMC = p/(a*a)
print('Seu IMC é {:.1f}'.format(IMC))

if IMC <= 18.5:
    print('Você está abaixo do peso.')

if 18.5 < IMC <= 25:
    print('Você está no peso ideal.')

if 25 < IMC <= 30:
    print('Você esta com sobrepeso.')

if 30 < IMC <= 40:
    print('Você esta Obeso.')

if IMC > 40:
    print('Você está com obesidade mórbida.')