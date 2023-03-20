n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número: '))

if n1>n2:
    print('o número {} é maior que o {}.'.format(n1,n2))

elif n1<n2:
    print('o número {} é maior que o {}.'.format(n2,n1))

else:
    print('o número {} é igual ao {}.'.format(n1,n2))
