

def notas(notas,situação):
    """

     :param notas: Notas dos alunos inseridas no sistema
     :param situação: opcinal para mostrar se o aluno foi aprovado ou não (False or True)
     :return: mostra o resultado com a quantidade de notas inseridas, maior e menor nota, média e situação em caso de True.

     """
    import numpy
    turma = {}
    nota_temp = []
    notas_dict = []

    while True:
        nota = (float(input('Insira a Nota: ')))
        if nota not in range(0,11):
            print('Número invalido!')
        else:
            nota_temp.append(float(nota))
            cont = str(input('Deseja continuar [S/N]: ')).upper().strip()
            notas_dict.append(nota_temp[:])
            nota_temp.clear()
            turma['Notas'] = notas_dict
            turma['Total'] = len(turma['Notas'])
            turma['Maior'] = max(turma["Notas"])
            turma['Menor'] = min(turma["Notas"])
            turma['calMed'] = numpy.mean(turma["Notas"])
            turma['Média'] = numpy.around(turma['calMed'], decimals=1)
            if situação:
                if turma['Média'] <=5.9:
                    turma['Situação'] =  'REPROVADO'
                elif turma['Média'] >= 7:
                    turma['Situação'] = 'APROVADO'
                else:
                    turma['Situação'] = 'RECUPERAÇÃO'
            del turma['Notas']
            del turma['calMed']
            if cont == 'N':
                break
    return turma

print(notas(notas,situação=False))






