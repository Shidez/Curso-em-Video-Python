from random import choice
n1 = input('Digite o nome do 1° aluno: ')
n2 = input('Digite o nome do 2° aluno: ')
n3 = input('Digite o nome do 3° aluno: ')
n4 = input('Digite o nome do 4° aluno: ')
print('O aluno que deverá apagar a lousa hoje é: {}'.format(choice([n1,n2,n3,n4])))
