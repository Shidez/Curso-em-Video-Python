numeros = ('zero','um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito','nove', 'dez',
           'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

conti = ' '
cont = 0

n = int(input('Digite um número de 0 até 20: '))

while True:
    cont += 1
    if cont == n:
        print(f'O número digitado foi {n} e seu nome por extenso é {numeros[n]}.')
        conti = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]

        if conti == 'S':
            n = int(input('Digite um número de 0 até 20: '))
        cont = 0

        if conti == 'N':
            break

    if n > 20 or n < 0:
        print('Número inválido')
        n = int(input('Digite um número de 0 até 20: '))




print('Programa encerrado.')


#for cont in range (0,len(numeros)):
    #n == cont
    #if n > 20:
        #print('Número inválido!')
        #n = int(input('Digite um número de 0 até 20: '))
#print(f'O número digitado foi {n} e seu nome por extenso é {numeros[n]}.')
