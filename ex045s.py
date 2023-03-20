from time import sleep
from random import choice
print('{:^65}'.format('\033[31;1mDo you wanna play a game?\033[m'))
sleep(1)
print('\033[31mSuA VidA eStÁ eM jOgO e AgOrA pArA SoBrEviVer VocÊ DevE gAnHar\033[m')
sleep(1)
print('#'*65)
sleep(1)
print(' Jokenpô '*7)
sleep(1)
print('#'*65)
jig = str(input('Escolha pedra, papel ou tesoura: ')).strip().lower()

p = 'pedra'
t = 'tesoura'
p1 = 'papel'

if jig == 'pedra':
    n2 = (choice([p,t,p1]))
    sleep(2)
    print('\033[33mSua vida está em minhas mãos!\033[m')
    sleep(1)
    print('Minha escolha foi {}!'.format(n2))

    if n2 == 'pedra':
        print('\033[31mEmpate, isso não é permitido, jogue novamente!\033[m')

    if n2 == 'tesoura':
        print('''\033[34mParabéns, sua pedra quebra minha tesoura!Depois de ver a morte de perto, 
você entende o valor real da vida!!\033[m''')

    if n2 == 'papel':
        print('\033[31mMeu papel embrulha sua pedra! Adeus!\033[m')

if jig == 'tesoura':
    n2 = (choice([p, t, p1]))
    sleep(2)
    print('\033[33mSua vida está em minhas mãos!\033[m')
    sleep(1)
    print('Minha escolha foi {}!'.format(n2))

    if n2 == 'tesoura':
        print('\033[31mEmpate, isso não é permitido, jogue novamente!\033[m')

    if n2 == 'pedra':
        print('\033[31mMinha pedra quebra sua tesoura! Adeus!\033[m')

    if n2 == 'papel':
        print('''\033[34mSua tesoura corta o meu papel! Até uma pessoa encarar a morte, 
é impossível dizer se ela tem o necessário para sobreviver.\033[m''')


if jig == 'papel':
    n2 = (choice([p, t, p1]))
    sleep(2)
    print('\033[33mSua vida está em minhas mãos!\033[m')
    sleep(1)
    print('Minha escolha foi {}!'.format(n2))

    if n2 == 'papel':
        print('\033[31mEmpate, isso não é permitido, jogue novamente!\033[m')

    if n2 == 'pedra':
        print('\033[34mSeu papel embrulha minha pedra, parabéns! É cruel, mas te ensina!\033[m')

    if n2 == 'tesoura':
        print('\033[31mMinha tesoura corta o seu papel! ADEUS!\033[m')









