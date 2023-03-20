from random import randint
from time import sleep

numeros = list()

print(f'{"Sorteio de números":^35}')


def sorteia(numeros):
    print('='*40)
    print(f'Sorteando os números:', end = ' ')
    for c in range (0,5):
        numeros.append(randint(0,30))
    for c in numeros:
        print(f'{c}',end = ' ')
        sleep(0.3)



def somapar(numeros):
    print()
    print(f'Os números pares são:', end=' ')
    s = 0
    for c in numeros:
        if c %2 == 0:
            print(f'{c}', end=' ')
            sleep(0.3)
            s += c
    print()
    sleep(0.3)
    print(f'A soma dos pares é {s}.')
    print('=' * 40)

sorteia(numeros)
somapar(numeros)
