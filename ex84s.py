pessoas = []
pessoa = []
maior = 0
menor = 0
while True:
    pessoa.append(str(input(f'Digite o nome da {c}° pessoa: ')))
    pessoa.append(float(input(f'Digite o peso da {c}º pessoa: ')))
    print('='*30)
    cont = str(input('Deseja continuar? S/N: ')).upper().strip()[0]
    print('=' * 30)
    if len(pessoas) == 0:
        maior = menor = pessoa[1]
    else:
        if pessoa[1] > maior:
            maior = pessoa[1]
        if pessoa[1] < menor:
           menor = pessoa[1]
    pessoas.append(pessoa[:])
    pessoa.clear()
    if cont == 'N':
        break

print(f'No total, {len(pessoas)} pessoas foram cadastradas.')
print(f'O maior peso é: {maior} kg. E a/s pessoa/s chama/m: ',end = '')
for p in pessoas:
    if p[1] == maior:
        print(f'{p[0]}',end = ' ')
print()

print(f'O menor peso: {menor}kg. E a/s pessoa/s chama/m: ',end = ' ')
for p in pessoas:
    if p[1] == menor:
        print(f'{p[0]}',end = ' ')
print()

