print('\033[34m--\033[m'*20)
titulo = str('\033[34mAumento de sálario anual\033[m')
print(titulo.rjust(20))
print('\033[34m--\033[m'*20)
n1 = float(input('Digite o salário atual: R$'))
n2 = n1*15/100
print('O novo sálario será R${:.2f}, aumento de R$ {:.2f}'.format(n1+n2,n2))



















































