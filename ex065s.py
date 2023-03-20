choice = 'S'
maior = 0
menor = 0
soma = 0
c = 0 #sem o contador o python, o python não usa os itens da lista do laço de forma separada
while choice == 'S':
    n = int(input('Digite um número: '))
    soma += n
    c += 1
    choice = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]

    if c == 1: #deve-se inserir um contador para o python pesquisar entre todos os números da lista
        maior = n
        menor = n

    else:
        if n > maior:
            maior = n

        if n < menor:
            menor = n

print('A média dos números é {}, o menor é o número {} e o maior é o número {}.'.format(soma / 2, menor, maior))
