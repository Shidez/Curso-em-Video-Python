
soma = 0
c = 0
n = 0
stop = 'N' or 'S'

while n != 999 or stop == 'N':
        n = int(input('Digite um número: '))

        if n != 999:
            soma += n
            c += 1

        if n == 999:
            stop = str(input('Deseja parar [S/N]: ')).upper()

        if stop == 'S':
            print('A soma é {} e foram digitados {} numeros.'.format(soma, c))

print('FIM')







