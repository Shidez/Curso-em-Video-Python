print('Ler numero primo e ver se ele é primo ou não:')

n = int(input("Digite o número: "))
tot = 0
for c in range(1,n+1):
    if n % c == 0:
        tot = tot + 1

if tot == 2:
    print('primo')
else:
    print('não primo')

