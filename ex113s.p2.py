def leiaInt(p):
    n = input(p)
    while True:
        if n.isnumeric() == True:
            return n
            break

        else:
            print('\033[31mErrado! Digite um número inteiro válido.\033[m')
            return leiaInt(p)



def leiafloat(x):
    y = input(x)
    while True:
        if y.replace('.', '').isdigit():
            return float(y)

        elif ',' in y:
            y.replace(',', '.')
            y = float(p)
            return p3

        else:
            print('\033[31mErrado! Digite um número válido.\033[m')
            return leiafloat(p3)




n = leiaInt('Digite um número inteiro: ')
print(f'Você digitou o número {n} e ele esta correto, porque é inteiro.')

x = leiafloat('Digite um número real: ')
print(f'Você digitou o número {x} e ele esta correto, porque é real.')