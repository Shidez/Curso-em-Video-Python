#sexo F ou M

r = 'S'
while r != 'N':
    sexo = str(input('Digite o sexo [F/M]: ')).upper().strip()

    if sexo == 'F':
        print('Sexo feminino')
    elif sexo == 'M':
        print('Sexo masculino')
    else:
        print('Sexo invalido, tente de novo.')

    r = str(input('Perguntar novamente [N/S]?')).upper().strip()

print('FIM')





