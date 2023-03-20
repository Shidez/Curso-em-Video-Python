from random import shuffle
n1 = input('Digite o nome do 1° aluno: ')
n2 = input('Digite o nome do 2° aluno: ')
n3 = input('Digite o nome do 3° aluno: ')
n4 = input('Digite o nome do 4° aluno: ')
lista_nomes=[n1,n2,n3,n4]
shuffle(lista_nomes)
print('A ordem dos alunos para apresentar será:')
print(lista_nomes)
