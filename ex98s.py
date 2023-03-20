from time import sleep


def contador(inicio, fim, passo):
    print(f'{"Vamos contar números":=^50}')
    print(f'Contagem dos números de {inicio} à {fim}, indo de {passo} em {passo}: ')
    if inicio <= fim:
        for c in range(inicio, fim+1, passo):
            print(f'{c}', end=' ')
            sleep(0.3)
        print()

    if inicio >= fim:
        for c in range(inicio, fim+1, -passo):
            print(f'{c}', end=' ')
            sleep(0.3)
        print()

inicio = 1
fim = 10
passo = 1
contador(inicio, fim, passo)

inicio = 10
fim = 1
passo = 2
contador(inicio, fim, passo)



print(f'{"Personalizado":=^50}')
inicio = int(input('Digite o inicio do laço: '))
fim = int(input('Digite o fim do laço: '))
passo = int(input('Digite o passo do laço: '))
contador(inicio, fim, passo)