nota = []
nome = []
alunos = []

while True:
    nome.append(str(input('Digite o nome: ')))
    nota.append(int(input('Digite nota 1: ')))
    nota.append(int(input('Digite nota 2: ')))
    nome.append(nota[:])
    alunos.append(nome[:])
    nota.clear()
    nome.clear()
    cont = str(input('Quer continuar? [N/S]: ')).upper().strip()[0]
    if cont == 'N':
        break


print(f'{"Matricula":<10}{"Nome":^10}{"Média":^10}')

c=0
for p in alunos:
    print(f'{c:^10}',end=' ')
    print(f'{p[0]:^9}',end=' ')
    media = (sum(p[1])/2)
    print(f'{media:^9}',end = ' ')
    c+=1
    print()

while True:
    matri = int(input('Digite a matrícula para ver as notas, se deseja sair digite 999: '))
    if matri != 999:
        print(f'As notas de {alunos[matri][0]} são {alunos[matri][1]}')
    if matri == 999:
        break
