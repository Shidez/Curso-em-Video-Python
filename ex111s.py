from modulo_s2 import moeda2

p = moeda2.leiafloat('Digite um valor em reais: ')
x = int(input('Digite uma porcentagem de aumento: '))
y = int(input('Digite uma porcentagem de redução: '))
moeda2.resumo(p, x, y)
