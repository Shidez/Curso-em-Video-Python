from random import choice
from time import sleep
num = int(input('Tente ler a minha mente, vou escolher um número de 0 à 5, adivinhe qual é: '))
num2 = (choice([0,1,2,3,4,5]))

print('Carregando...')
sleep(2)
print('O número escolhido foi {}'.format(num2))
if num == num2:
    print('Agora você é um adivinho por acaso? PARA BEINS!')
else:
    print('Hahahaha como você é ruim, tente outra vez!')
