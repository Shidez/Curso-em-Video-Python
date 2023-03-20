print('\033[34;1mFaculdade IMPACTA - Média Anual:\033[m')
print('Matérias:\n1.Matematica\n2. Religião\n3. Português')

materia = int(input('Selecione a matéria desejada: '))
mat = ('Matematica')
reg = ('Religião')
port = ('Português')

if materia == 1:
        print(mat)
        notam = float(input('Qual a nota 1? '))
        notam2 = float(input('Qual a nota 2? '))
        media = float((notam + notam2) / 2)
        print('Sua média em Matemática é {}.'.format(media))
        if media >= 7:
                print('\033[36;4mParabéns, você está APROVADO!\033[m')
        elif media <5:
                print('\033[31;4mVocê está REPROVADO!\033[m')
        else:
                print('\033[35;4mVocê está de RECUPERAÇÃO!\033[m')



elif materia == 2:
        print(reg)
        notar = float(input('Qual a nota 1? '))
        notar2 = float(input('Qual a nota 2? '))
        media = float((notar + notar2) / 2)
        print('Sua média em Religião é {}.'.format(media))
        if media >= 7:
                print('\033[36;4mParabéns, você está APROVADO!\033[m')
        elif media < 5:
                print('\033[31;4mVocê está REPROVADO!\033[m')
        else:
                print('\033[35;4mVocê está de RECUPERAÇÃO!\033[m')

elif materia == 3:
        print(port)
        notap = float(input('Qual a nota 1? '))
        notap2 = float(input('Qual a nota 2? '))
        media = float((notap+notap2)/2)
        print ('Sua média em Portugues é {}.'.format(media))
        if media >= 7:
                print('\033[36;4mParabéns, você está APROVADO!\033[m')
        elif media < 5:
                print('\033[31;4mVocê está REPROVADO!\033[m')
        else:
                print('\033[35;4mVocê está de RECUPERAÇÃO!\033[m')
else:
        print('Esse número é uma opção invalida!')
