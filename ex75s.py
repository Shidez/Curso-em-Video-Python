# 4 numeros pelo usuario e guarde-os em uma tupla
# qts vezes aparece o 9
# em que posiçao aparece o numero 3
# quais foram os numeros pares

num1 = int(input(f'Digite o 1º número: '))
num2 = int(input(f'Digite o 2º número: '))
num3 = int(input(f'Digite o 3º número: '))
num4 = int(input(f'Digite o 4º número: '))

tupla = (num1, num2, num3, num4)

print(f'Os números em tupla {tupla}.')
print(f'O número 9 aparece {tupla.count(9)} vezes nesta lista.')

if 3 in tupla:
    print(f'O número 3 aparece {tupla.index(3) + 1}º posição nesta lista.')
else:
    print('Não tem o número 3 na lista')

print(f'Os números pares são:',end=' ')
for i in tupla:
    if i % 2 == 0:
        print(i, end = ' ')