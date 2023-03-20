from random import sample
from time import sleep
titulo = ('Loteria da amizade!!')
print(titulo.center(30))
sleep(1)
lista = []
num = int(input('Digite quantos jogos você quer fazer: ' ))

nu = 0
for c in range(0,60):
    nu+=1
    lista.append(nu)

print('...Carregando...')
sleep(1)
for c in range(1,num+1):
    num2 = sample(lista,7)
    print(f'Jogo {c}: {sorted(num2)}')
    sleep(1)
print('Boa sorte!')
