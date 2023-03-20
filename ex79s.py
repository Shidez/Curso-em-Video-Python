lista = list()

while True:
    num = int(input('Digite um número: '))

    if num not in lista:
        lista.append(num)
        print('Número adicionado com sucesso!')
    else:
        print('Número repetido, não será adicionado.')

    cont = str(input('Deseja continuar [S/N]: ')).upper().strip()
    if cont =='N':
        break

print(f'A lista selecionada é a : {sorted(lista)}.')

