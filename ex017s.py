from math import sqrt,ceil
x = float(input('Digite o valor do cateto oposto: '))
y = float(input('Digite o valor do cateto adjacente: '))
h = sqrt(x * x + y * y)
print ('A hipotenusa dos catetos acima é: {}'.format(ceil(h)))
