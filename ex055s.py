lista = []
for c in range (0,5):
    n=int(input('Digite um peso: '))
    lista.append(n)
print('O maior peso é {}kg e o menor peso é {}kg.'.format(max(lista),min(lista)))
