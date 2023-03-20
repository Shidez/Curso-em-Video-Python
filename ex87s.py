listazero = [[0,0,0],[0,0,0],[0,0,0]]

for l in range(0,3):
    for c in range(0, 3):
        listazero[l][c] = (int(input(f'Digite um número para a posição [{l} {c}]: ')))

for l in range(0,3):
    for c in range(0, 3):
        print(f'[{listazero[l][c]:^5}]',end=' ')
    print()

#maior valor da 2 linha
print(f'O maior número da 2° linha é o: {max(listazero[1])}.')

#soma dos valores da 3 coluna
soma = (listazero[0][2] + listazero[1][2] + listazero[2][2])
print(f'A soma dos valores da 3° coluna é {soma}.')

lista=[]
#soma dos pares
for p in listazero:
    for par in p:
         if par % 2 == 0:
            lista.append(int(par))

print(f'A soma dos números pares é : {sum(lista)}.')