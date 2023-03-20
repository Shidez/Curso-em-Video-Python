num = int(input('Digite um número inteiro:'))
num2 = num % 2
if num2 ==0:
    print('O número {} é PAR.'.format(num))
else:
    print('O número {} é ÍMPAR.'.format(num))