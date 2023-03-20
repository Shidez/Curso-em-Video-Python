
def fatorial (num, show):
    """ Programa Fatorial:
    num: o número a ser calculado
    show: opcional com False ou True - não mostra ou mostra a conta
    return: use o print para ver o número do fatorial."""
    num2 = num
    while num > 1:
        num -= 1
        num2 *= num
        if show:
            if num > 1:
                print(f'{num+1} x', end=' ')
            if num == 1:
                print(f'1 =', end=' ')
    return f'{num2}'

num = int(input('Digite um número inteiro: '))
print(fatorial(num, show=False))

help(fatorial)