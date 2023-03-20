print('________' * 5)
print('          TIPOS DE TRIÂNGULOS')
print('________' * 5)

reta1 = float(input('Digite o tamanho da reta 1: '))
reta2 = float(input('Digite o tamanho da reta 2: '))
reta3 = float(input('Digite o tamanho da reta 3: '))

triangulo = reta1 + reta2 >= reta3 and reta1 + reta3 >= reta2 and reta2 + reta3 >= reta1

if triangulo:
    print('É possivel fazer um triangulo com essas retas.')

    if reta1 != reta2 != reta3 != reta1:
        print('Este é um triângulo Escaleno.')

    if reta1 == reta2 and reta1 != reta3 or reta2 == reta3 and reta2 != reta1 or reta3 == reta1 and reta3 != reta2:
        print('Este é um triangulo Isósceles.')

    else:
        print('Este é um triângulo é um Equilátero.')

else:
    print('Não é possivel formar um triângulo.')



