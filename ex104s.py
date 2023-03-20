
def leiaInt(p):
    n = input(p)
    while True:
        if n.isnumeric() == True:
            return n
            break
        else:
            print('\033[31mErrado! Digite um número inteiro válido.\033[m')
            return leiaInt(p)



n = leiaInt('Digite um número: ')
print(f'Você digitou o número {n} e ele esta correto, porque é inteiro.')
