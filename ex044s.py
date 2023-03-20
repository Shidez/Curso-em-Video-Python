print('{:^40}'.format('SD BOMBA PARALELINHOS'))
n = float(input('Insira o preço do paralelinho aqui R$: '))
print('''
Formas de pagamento:
1.Dinheiro ou cheque à vista
2.Cartão de crédito à vista
3.Em até 2x no cartão
4.Em 3x ou mais no cartão''')

pag = int(input('Escolha a forma de pagamento entre 1 e 4: '))

if pag == 1:
    print('Você ganhou desconto de 10%, o valor R${:.2f}, fica R${:.2f}.'.format(n,n-n*0.1))

if pag == 2:
    print('Você ganhou 5% de desconto e valor R${:.2f} fica R${:.2f}.'.format(n,n-n*5/100))

if pag == 3:
    print('O valor R${:.2f} fica com parcelas de R${:.2f} em 2x.'.format(n,n/2))

if pag == 4:
    parcelas = int(input ('Insira o número de parcelas de 3 ou mais: '))
    jur = n + n*20/100
    parc = ((n + n*20/100) / parcelas)
    print('O valor R${:.2f} com 20% de juros fica R${:.2f}\nParcelado em {}x fica R${:.2f}'.format(n,jur,parcelas,parc))

else:
    print('Esta opção não é válida!')
