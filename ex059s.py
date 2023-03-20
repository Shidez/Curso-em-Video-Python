#digitar dois numeros e selecionar no menu
soma = 1
choice = 0
mult = 1

while choice == 4 or choice != 5:
    n1 = int(input('Digite o primeiro número:'))
    n2 = int(input('Digite o segundo número:'))

    print('''Escolha uma opção:
    [1] somar
    [2] multiplicar
    [3] maior número
    [4] novos números
    [5] Sair do programa''')

    choice = int(input('Digite a opção de 1 a 5: '))
    if choice == 1:
        soma = n1 + n2
        print('A soma dos números é {}.'.format(soma))

    elif choice == 2:
        mult = n1 * n2
        print('A multiplicação dos números é {}.'.format(mult))

    elif choice == 3:
        if n1 > n2:
            print('O número {} é maior que o número {}.'.format(n1, n2))
        elif n2 > n1:
            print('O número {} é maior que o número {}.'.format(n2, n1))
        else:
            print( 'Os números são iguais.')

    if choice > 5:
        print('Opção invalida.')

    choice1 = str(input('Deseja x? [S/N]: ')).upper().strip()
    if choice1 == 'N':
        choice == 5
        break


print('FIM')











