dados = dict()
dados2 = list()
c = 0
s = 0

while True:
    dados['Nome'] = str(input('Digite o nome: '))
    dados['Sexo'] = str(input('Digite o sexo [F/M]: ')).upper().strip()
    dados['Idade'] = int(input('Digite a idade: '))
    dados2.append(dados.copy())
    s += dados['Idade']
    c += 1

    cont = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    if cont == 'N':
        break

media = s / c
print(f'A quantidade de pessoas cadastradas: {c} pessoa(s).')
print(dados2)

print(f'As mulheres do grupo são: ',end = ' ')

for pessoas in dados2:
    if pessoas['Sexo'] == 'F':
        print(f'{pessoas["Nome"]}',end = ' ')

print()
print(f'A média da idade do grupo é {media:.0f}.')

print(f'As pessoas com idade maior que a média do grupo são: ',end = ' ')

for pessoas in dados2:
    if pessoas['Idade'] > media :
        print(f'{pessoas["Nome"]}',end = ' ')