lista = [ ]

for c in range(1,6):
    num = (int(input(f'Digite o número: ')))
    #contador = 1 ou num da lista na posição -1, se não tiver a posição -1 "definida", não funciona
    if c == 1 or num >= lista[-1]:
        lista.append(num) #adiciona o numero na lista
    #agora podemos comparar os numeros na lista:
    elif num <= lista[0]: # numero menor ou igual ao que esta na lista que é o 0 e -1 ao mesmo tempo
        lista.insert(0,num) #inserir na posição 0
    elif lista[0] <= num <=lista[1]:
        lista.insert(1, num)
    elif lista[1] <= num <= lista[2]:
        lista.insert(2, num)
    elif lista[2] <= num <= lista[3]:
        lista.insert(3, num)
    print(f'O número será adicionado na posição {lista.index(num)} da lista.') #index mostra a posição do número na lista
print(lista)