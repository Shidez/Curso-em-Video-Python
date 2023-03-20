print ('Promoção, tudo com 5% de desconto:')
n1 = float(input('Digite o preço aqui: '))
n2 = n1*5/100
print ('Você irá pagar o total de: R$ {:.2f}\nEconomia de R$ {:.2f}'.format(n1-n2,n2))
