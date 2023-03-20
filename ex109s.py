from modulo_s import moeda

p = float(input(f'Digite o valor em reais: '))
print(f'Aumentando 10% temos {moeda.aumentar(p, 10, True)}')
print(f'Diminuindo 5% temos {moeda.diminuir(p, 5, True)}')
print(f'Metade de {p:.2f} é {moeda.metade(p, False)}')
print(f'Dobro de {p:.2f} é {moeda.dobro(p, True)}')

