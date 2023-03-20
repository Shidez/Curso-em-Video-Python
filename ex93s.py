gols_rodada = dict()
gols = []

gols_rodada['nome do jogador'] = str(input('Digite o nome do jogador: '))
gols_rodada['partidas'] = int(input(f'Digite a quantidade de partidas de {gols_rodada["nome do jogador"]}: '))

for c in range(0, gols_rodada['partidas']):
    gols.append(int(input(f'Quantos gols na partida {c+1}: ')))
    gols_rodada['gols'] = gols

print(gols_rodada)
print()

for k,v in gols_rodada.items():
    print(f'O campo {k} tem o valor {v}')
print()
print(f'O jogador {gols_rodada["nome do jogador"]} fez {gols_rodada["partidas"]} partidas. ')
print()


for c, gols in enumerate(gols_rodada['gols']):
    print(f'A partida {c+1} teve {gols} gols')

