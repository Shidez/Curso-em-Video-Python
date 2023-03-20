
print('-='*36)
print('Digite vários números para ver a soma entre eles, para parar digite 999:')
print('-='*36)
soma = count = n = 0
n = int(input('Digite um número: '))
while n != 999:
    count += 1
    soma += n
    n = int(input('Digite um número: '))
    if n == 999:
        break
print('-='*36)
resultado = f'A soma dos {count} números digitados é {soma}.'
print(resultado.center(36))
print('-='*36)
