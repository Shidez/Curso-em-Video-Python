lista = list()

for c in range(0,5):
    n = lista.append(int(input(f'Digite um número para a posição {c}: ')))

print(f'O maior número é o {max(lista)} na posição:',end=' ')
for c2, v in enumerate(lista):
    if v == max(lista):
        print(f'{c2}', end=' ')

print(f'\nO menor número é {min(lista)} na posição:',end=' ')
for c2, v in enumerate(lista):
    if v == min(lista):
        print(f'{c2}', end=' ')
