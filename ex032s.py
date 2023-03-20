#from datetime import date
#if ano == 0
    #ano=date.today().year

#if ano % 4 == 0 and ano % 100 !=0 or ano % 400 == 0

ano = int(input('Digite o ano e direi se é bisexto ou não: '))
if ano % 4 == 0 and ano % 100 != 0:
    print('O ano {} é bisexto.'.format(ano))

elif ano % 4 == 0 and ano % 100 == 0 and ano % 400 == 0:
    print('O ano {} é bisexto.'.format(ano))

else:
    print('O ano {} não é bisexto.'.format(ano))
