# digitar o numero
#pegar esse numero e multi de 0 ate 10

c = 0
true = 'S'

while true == 'S':
    n = int(input('Digite um número:'))

    for c in range(0,10):
        c += 1
        n2 = c * n
        print(f'{c} x {n} = {n2}')

    if c == 10:
        true = str(input('Deseja continuar? [N/S]: ')).upper().strip()[0]
        if true == 'N':
            break
print('FIM')



