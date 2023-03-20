print('FIBONACCI')
seq = int(input('Digite quantas sequencias deseja ver: '))

c = 3
t1 = 0
t2 = 1

print (t1,'-',t2, end=' - ')
while c <= seq:      # o controle deve fazer o laço girar ate o valor da seq no input
     t3 = t1 + t2    # o número fibonacci faz a soma do número 1 com seu sucessor
     t1 = t2        # t1 assume valor de t2 no proximo laço
     t2 = t3        # t2 assume valor de t3 no proximo laço
     c += 1         # contador para girar o laço
     print(t3, end=' - ')




     #fn = (pow((1 + pow(5, 1 / 2)) / 2, n) - pow((1 - pow(5, 1 / 2)) / 2, n)) / (pow(5, 1 / 2))