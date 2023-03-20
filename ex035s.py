a = int(input('Digite o comprimento da 1º reta: '))
b = int(input('Digite o comprimento da 2° reta: '))
c = int(input('Digite o comprimento da 3° reta: '))

if a + b > c or a + c > b or b + c > a:
    print('É possivel fazer um triangulo com as tres retas {},{} e {}'.format(a,b,c))
else:
    print('Não é possivel fazer um triangulo com as três retas {}, {} e {}.'.format(a,b,c))





