
soma = 0
c = 0
menor = 0
barato = ''
c1 = 0

while True:
    produto = str(input('Insira o nome do produto: '))
    preço = float(input('Insira o preço do produto: '))
    cont = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    c1 += 1
    #soma do preço
    soma += preço

    # o produto mais barato
    if c1 == 1:
        menor = preço

    else:
        if preço < menor:
            barato = produto
            menor = preço


    #produtos acima de mil reais, usar o contador
    if preço > 1000:
        c += 1

    if cont == 'N':
        break

print(f'O gasto total da compra foi R${soma:.2f}.')
print(f'{c} produtos custam mais de R$ 1.000,00.')
print(f'O produto mais barato é o/a {barato} que custa R${menor:.2f}.')
