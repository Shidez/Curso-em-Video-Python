
termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))

limite = 10
c = 0

while c < limite:
    termo2 = termo + c * razao
    c += 1
    print(termo2, end=' ')

r = str(input('\nDeseja adicionar mais termos na PA? [S/N]: ')).upper()  # adicionar mais números no contador
while r == 'S':
    novolimite = int(input('\nDigite quantos números que adicionar: '))
    c = 0
    while c < novolimite:
        c += 1
        termo3 = termo2 + c * razao  # a conta deve x de onde parou o 10 termo
        print(termo3, end=' ')
print('\nFIM')
