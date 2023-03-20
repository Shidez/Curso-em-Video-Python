from random import randint
from time import sleep
jogos = dict()

print(f'{"JOGO DA AMIZADE":=^30}')
for c in range(1,5):
    jogos[f'jogador {c}'] = (randint(1,7))

for k,v in jogos.items():
    print(f'O {k} tirou: {v}')
    sleep(1)
print(f'{"RANKING DOS JOGADORES":=^30}')

n =1
for item in sorted(jogos, key=jogos.get, reverse=True):
    print(f'{n}° lugar = {item} com [{jogos[item]}]')
    n += 1
    sleep(1)


