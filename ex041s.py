from datetime import date
print('Categorias da competição de Natação')
ano = int(input('Insira o ano em que você nasceu: '))
ano2 = date.today().year
idade = ano2 - ano
if idade <= 9:
    print('Sua categoria é a MIRIM.')
if 9 < idade <= 14:
    print('Sua categoria é a INFANTIL.')
if idade == 19:
    print('Sua categoria é a JUNIOR.')
if idade == 20:
    print('Sua categoria é a SENIOR.')
if idade > 20:
    print('Sua categoria é a MASTER.')

