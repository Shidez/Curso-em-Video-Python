pessoa = {'Nome': "",'idade': []}
pessoas = []

while True:
    pessoa.clear()
    nome = pessoa['Nome'] = str(input('Digite o nome: '))
    idade = pessoa['idade'] = int(input('Digite a idade: '))
    pessoas.append(pessoa.copy())
    continuar = ' '
    while continuar not in 'SsNn':
        continuar = str(input('Deseja continuar? [S/N] '))
    if continuar in 'Nn':
        break
print(pessoas)

