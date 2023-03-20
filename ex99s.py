from time import sleep

def maior (*num):
    print('=' * 50)
    tam = (len(num))
    sleep(1)
    print('Analisando valores...')
    sleep(1)
    print(f'Os números são: ', end= ' ')
    for c in num:
        print(f'{c}', end = ' ')
        sleep(0.5)
    print()
    print(f'E foram digitados {tam} números ao todo.')
    print(f'O maior é o número {max(num)}.')
    sleep(1)
    print('='*50)



maior(0,1,2,3,4,5)

maior(5,7,8,3)

maior(0,1,5,8,9)

maior(0)





