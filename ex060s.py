#fatorial

num = int(input('Digite um número inteiro: '))
num2 = num

while num > 1:
#fazer o while contar ate chegar em 1
    num-= 1
# a variavel num2 deve assumir o resultado da ultima divisão antes de fazer a proxima
    num2 *= num

#mostrar o resultado da multiplicação quando a variavel chegar a 1
print('O resultado do fatorial é {}.'.format(num2))










