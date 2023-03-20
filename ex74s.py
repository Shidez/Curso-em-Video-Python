# 5 numeros aleatorios em tuplas
#mostre a listagem
#mostre o menor e o maior

from random import randint
num = randint(1, 99),randint(1, 99),randint(1, 99),randint(1, 99),randint(1, 99)
num2 = sorted(num)
print(f'Os cinco números são: {num}.', end = ' ')
print(f'\nO menor número é o {num2[0]} e o maior é o {num2[-1]}.')


#n = tuple(randint(1, 15) for i in range(5)) - outra opção

