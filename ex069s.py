
c = 0
s = 0
sf = 0

while True:
    idade = int(input('Insira sua idade: '))
    sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()
    cont = str(input('Deseja inserir outra? [S/N]:')).strip().upper()

    if idade >= 18:
        c += 1
    if sexo == 'M':
        s += 1
    if idade < 20:
        if sexo == 'F':
            sf += 1
    if cont == 'N':
        break

print(f'{c} pessoas, são maiores de 18 anos.')
print(f'{s} pessoas, são do sexo masculino.')
print(f'{sf} pessoas, são maiores mulheres e tem menos de 20 anos.')
