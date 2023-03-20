salario = float(input('Digite o salário a ser calculado o aumento: '))

if salario <= 1250:
    print('O salário será de {:.2f} com aumento de 15%.'.format(salario*0.15 + salario))

else:
    print('O salário será de {:.2f} com aumento de 10%.'.format(salario*0.1 + salario))

