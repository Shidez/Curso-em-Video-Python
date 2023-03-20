print('ler seis números inteiros pares e some, se for impar desconsidere.')
soma = 0
for c in range(1,7):
    num = (int(input('Insira um número:')))
    if num %2 == 0:
        soma += num
print('A soma dos números pares desses 6 é {}.'.format(soma))