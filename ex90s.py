bolet = dict()
boletim = list()

bolet['Nome'] = str(input('Digite o nome do aluno: '))
bolet['Média'] = float(input(f'Digite a média de {bolet["Nome"]}: '))
if bolet['Média']<= 5.9:
    bolet['Situação'] = 'REPROVADO'
if bolet['Média'] == 6 <= 6.9:
    bolet['Situação'] = 'RECUPERAÇÃO'

else:
    bolet['Situação'] = 'APROVADO'
boletim.append(bolet.copy())

for c in boletim:
    for k,v in c.items():
        print(f'{k} é igual a {v}')

