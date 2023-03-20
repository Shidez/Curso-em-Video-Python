#Faça um programa que jogue par ou impar, o jogo para quando o jogador perder e mostra o número de vitorias consecutivas
#do jogador

import random

print('Vamos jogar PAR ou IMPAR? Só acaba quando você ganhar!!')

c = 0

while True:
    lado = str(input('Escolha PAR ou IMPAR?: ')).upper().strip()[0]
    jogador = int(input('Digite um número inteiro entre 1 e 10: '))
    comp = (random.randint(0,10))
    n2 = jogador + comp

    if n2 % 2 == 0 and lado == 'P':
        c += 1
        print(f' Eu escolhi {comp} e você {jogador} e a soma {n2} deu PAR, você ganhou. Vamos jogar de novo!')
    if n2 %2 == 0 and lado != 'P':
        print(f'Eu escolhi {comp} e você {jogador} e a soma {n2} deu PAR, você perdeu, mas teve {c} vitorias seguidas!')
        break
    if n2 % 2 != 0 and lado != 'P':
        c += 1
        print(f'Eu escolhi {comp} e você {jogador} e a soma {n2} deu IMPAR, você ganhou. Vamos jogar de novo!')
    if n2 % 2 != 0 and lado == 'P':
        print(f'Eu escolhi {comp} e você {jogador} e a soma {n2} deu IMPAR, você perdeu, mas teve {c} vitorias seguidas!')
        break


