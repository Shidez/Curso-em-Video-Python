from datetime import date
print('ler a data de nascimento de 7 pessoas:')

count = 0
count2 = 0
ano1 = date.today().year

for c in range(0,7):
    ano = (int(input('Ano de nascimento: ')))
    if ano1 - ano >= 21:
        count += 1
    elif ano1 - ano < 21:
        count2 += 1
print('Neste grupo há {} maiores de idade e {} menores de idade'. format(count, count2))
