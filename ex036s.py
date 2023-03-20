print('--'*30)
print('Empréstimos BOLSOLULA, consiga sua casa pagando quase nada!')
print('--'*30)

v1= float(input('Qual o valor da minha casa, minha vida:' ))
s1: float = float(input('Qual a sua renda? '))
a1= int(input('Em quantos anos deseja pagar?'))

ano = a1*12
parcela= (v1/ano)

if parcela <= s1*30/100:
    print('Empréstimo aprovado, suas parcelas em {} anos, serão de R${:.2f}.'.format(a1,parcela))

else:
    print('Você é muito pobre e não confiamos em você, arrume outro emprego e tente outra vez.')

