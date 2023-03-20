num1 = [[],[]]
c = 1

for c in range(1,8):
    num = (int(input(f'Digite o {c}º número: ')))
    if num %2 == 0:
        num1[0].append(num)
    else:
        num1[1].append(num)


print(f'Par: {sorted(num1[0])}')
print(f'Impar: {sorted(num1[1])}')
print(f'A lista inteira: {sorted(num1)}')
