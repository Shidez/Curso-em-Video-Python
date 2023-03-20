lista = list()

c = 0
while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    c+=1
    cont = str(input('Deseja continuar [S/N]: ')).upper().strip()
    if cont == 'N':
        break

print(f'Foram digitados {c} números nesta lista.')
print(f'Lista em ordem decrescente: {sorted(lista,reverse=True)}')

if 5 in lista:
    print('O número 5 encontra-se na lista.')
else:
    print('O número 5 não esta na lista.')