#jogo adivinhação

from random import randint
nc2 = 2
n = 1
n1 = 0
while n != nc2:
    n = int(input('Digite um número inteiro de 0 até 10: '))
    nc2 = randint(0, 10)
    n1 += 1
    if n == nc2:
        print('ACERTOU, mas precisou de {} tentativas!'.format(n1))

    if n > 10:
        print('Este número não vale, tente novamente!')

    else:
        print('Errou, pensei no número {}.'.format(nc2))



