from datetime import date
aposenta = {}

anoatual = date.today().year

aposenta['Nome'] = str(input('Digite o nome: '))
aposenta['Ano'] = int(input('Digite o ano de nascimento: '))
aposenta['Carteira'] = int(input('Digite a carteira : '))
print(f'{"Dados coletados":=^30}')

aposenta['Idade'] = anoatual - aposenta['Ano']
del aposenta['Ano']

if aposenta['Carteira'] == 0:
    for k,v in aposenta.items():
        print(f'{k}: {v}')
else:
    aposenta['Ano contratação'] = int(input('Digite o ano de contratação: '))
    aposenta['Salário'] = float(input('Digite o salário R$: '))
    aposenta['Ano da aposentadoria'] = aposenta['Ano contratação'] + 34
    aposenta['Anos para aposentar'] = aposenta['Ano da aposentadoria'] - anoatual
    del aposenta['Ano da aposentadoria']
    for k,v in aposenta.items():
        print(f'{k}: {v}')





