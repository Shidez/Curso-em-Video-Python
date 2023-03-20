print('TABUADA')

n=(int(input('Insira um número para saber sua tabuada: ')))

for c in range(0,11):
    print('{} x {} = {}'.format(c,n,c*n))