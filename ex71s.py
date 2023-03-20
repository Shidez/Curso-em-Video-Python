
titulo = ('BANCO NACIONAL DA RUSSIA')
print('*'*80)
print(f'{titulo:^80}')
print('PEGUE EMPRESTIMO E NÃO PRECISA PAGAR PORQUE NÃO CONSEGUIMOS RECEBER DE VOLTA')
print('*'*80)
print('''SELECIONE A OPÇÃO DESEJADA:
 [1] SAQUE
 [2] DEPÓSITO
 [3] EXTRATO''')

um = dez = cinq = cem = 0
cont = 'S'
while True:
    n = int(input('Selecione a opção para continuar: '))
    if n == 1:
        print('''SAQUES
Disponiveis notas de:
R$ 1,00
R$ 10,00
R$ 50,00
R$ 100,00''')
        money = int(input('Digite o valor: '))
        money2 = money

        while money >=100:
            cem += 1
            money -= 100

        while money >= 50:
            cinq += 1
            money -= 50

        while money >= 10:
            dez += 1
            money -= 10

        while money >= 1:
            um += 1
            money -= 1

        print(f'O saque efetuado terá: {cem} notas de R$100,00,{cinq} notas de R$50,00,{dez} notas de R$10,00,{um} notas de R$1,00.')
        print(f'Totalizando R${money2:.2f}')
    if n == 2:
        print('Sistema indisponivel, tente mais tarde.')

    if n == 3:
        print('''Seu Saldo Total é de: R$ 5.000,00.
Temos programas de investimento, volte ao menu e saiba mais.''')
    cont = str(input('Deseja selecionar outra opção? [S/N]'))

    if cont in 'Nn':
        break

print('Obrigada por utilizar os nossos serviços! Volte sempre!')


