from time import sleep

def area(a,b):
    c = a * b
    print(f'A área do terreno {a}m largura e {b}m de comprimento é {c}m².')


while True:
    a = float(input(f'Largura (m): '))
    b = float(input(f'Comprimento (m): '))
    area(a,b)
    cont = str(input(f'Deseja calcular outra área [S/N]: ')).upper().strip()[0]
    if cont == 'N':
        break
sleep(1)
print('Finalizando o programa...')
sleep(1)
print('Programa encerrado!')