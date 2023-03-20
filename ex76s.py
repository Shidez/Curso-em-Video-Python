listagem = ('Pão',1,'Leite', 3.50,'Calça', 199.99)

print('-'*52)
lista = 'LISTAGEM DE PREÇO'
print(f'{lista:^52}')
print('-'*52)

print(f'{listagem[0]:.<42} R$ {listagem[1]:>6.2f}')
print(f'{listagem[2]:.<42} R$ {listagem[3]:>6.2f}')
print(f'{listagem[4]:.<42} R$ {listagem[5]:>6.2f}')
print('-'*52)


for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<42}', end='')
    else:
        print(f' R$ {listagem[pos]:>6.2f}')
print('-'*52)

