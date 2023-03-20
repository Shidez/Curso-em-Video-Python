soma = 0
count = 0
for i in range(1, 500+1, 2):
        if i % 3 == 0:
                soma += i
                count += 1
print(' A soma dos {} números impares e múltiplos de 3 entre 0 e 500 é {}.'.format(count,soma))