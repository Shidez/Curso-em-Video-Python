
tupla = ('arquivo', 'chave', 'casa', 'medo')

print('~'*40)
print(tupla)
print('~'*40)

for palavra in tupla:
    print(f'\nNa palavra {palavra} suas vogais são:', end = ' ')
    for letra in palavra:
        if letra in 'aeiou':
            print(f'{letra}', end = ' ')

