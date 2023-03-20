lista = list()
lista2 = [ ]
lista3 = [ ]
while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    cont = str(input('Deseja continuar [S/N]: ')).upper().strip()
    if num %2 ==0:
        lista2.append(num)
    else:
        lista3.append(num)
    if cont == 'N':
        break
print(f'A lista toda é {lista}')
print(f'A lista PAR é {lista2}')
print(f'A lista IMPAR é {lista3}')