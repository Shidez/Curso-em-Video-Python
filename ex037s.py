print('Converse comigo na minha lingua! Digite um número e vamos converte-lo!')

print('''Escolha uma forma de conversão númerica:
1.binária
2.octagonal
3.hexadecimal''')

conv = int(input('Agora escolha uma opção: '))

if conv == 1:
    n = int(input('Digite o número a converter:'))
    print('O número {} no sistema binário é {}.'. format(n,(bin(n)[2:])))

if conv == 2:
    n = int(input('Digite o número a converter: '))
    print('O número {} no sistema octagonal é {}.'.format(n,(oct(n)[2:])))

if conv == 3:
    n= int(input('Digite o número a converter:'))
    print('O número {} no sistema hexadecimal é {}.'.format(n,(hex(n)[2:])))

elif conv != 1 and conv !=2 and conv !=3:
    print('Você não sabe ler? Esse número não tem nas opções!')




