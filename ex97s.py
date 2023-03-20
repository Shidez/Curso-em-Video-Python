def contador (frase):
    print('-' * len(frase))
    print(f'{frase}')
    print('-' * len(frase))

while True:
    frase = str(input('Digite uma frase: '))
    contador(frase)
    cont = str(input('Deseja digitar outra frase? ')).upper().strip()[0]
    if cont == 'N':
        break

print('Sem criatividade hein? Finalizado!')