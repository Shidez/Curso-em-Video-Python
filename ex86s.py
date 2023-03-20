listazero = [[0,0,0],[0,0,0],[0,0,0]]

for l in range(0,3):
    for c in range(0, 3):
        listazero[l][c] = (int(input(f'Digite um número para a posição [{l} {c}]: ')))

for l in range(0,3):
    for c in range(0, 3):
        print(f'[{listazero[l][c]:^5}]',end=' ')
    print()
