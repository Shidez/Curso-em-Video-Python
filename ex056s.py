maior = 0
soma = 0
count = 0
nome = ''

for p in range(1,5):
    pessoa = str(input('Digite o nome da {}ª pessoa: '.format(p)))
    idade = int(input('Digite a idade da {}ª pessoa: '.format(p)))
    sexo = str(input('Digite o sexo (F) ou (M) da {}ª pessoa: '.format(p)))
    print('_'*40)
    #media das idades
    soma += idade

    #O homem mais velho
    if sexo == 'M':
        if idade > maior:
            maior = idade
            nome = pessoa

    # mulheres com menos de 20 anos
    if idade < 20 and sexo == 'F':
        count += 1


print('A media das idades é de {:2} anos.'.format(soma/4))
print('O homem mais velho é o {} e ele tem {} anos.'.format(nome,maior))
print('Neste grupo, {} mulheres tem menos de 20 anos.'.format(count))






















