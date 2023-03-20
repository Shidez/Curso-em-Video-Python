gols_rodada = dict()
rodada = list()
gols = list()

while True:
    gols_rodada['nome'] = str(input('Digite o nome do jogador: ')).capitalize()
    gols_rodada['partidas'] = int(input(f'Digite o número de partidas de {gols_rodada["nome"]}: '))
    for c in range(0, gols_rodada['partidas']):
        gols.append(int(input(f'Digite o número de gols na {c + 1}° partida: ')))
        gols_rodada['gols'] = gols[:]
    rodada.append(gols_rodada.copy())
    gols.clear()
    cont = str(input('Deseja adicionar outro jogador? [S/N]: ')).upper().strip()[0]
    if cont == 'N':
        break
print('='*40)
print(f'{"Código":<5}{"Nome":^10}{"Gols":^15}{"Total de gols":^15}')
print('='*40)
for c, jogador in enumerate(rodada):
    print(f'{c:<5} {jogador["nome"]:^10} {str(jogador["gols"]):^15} {sum(jogador["gols"]):^15}')
print('='*40)

while True:
    dados = int(input('Dados jogador ou 999 sair: '))
    print('=' * 40)
    if dados == 999:
        break
    for v, jogador in enumerate(rodada):
        if dados == v:
            print(f' O levantamento do jogador {jogador["nome"]}:')
            v=0
            for i in jogador['gols']:
                v += 1
                print(f' => Na {v}° partida fez {(i)} gols.')

    if dados >= len(rodada):
        print('Número inválido!')

print('LEVANTAMENTO ENCERRADO')
