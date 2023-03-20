
def ficha (nome = '', gols = ''):
    if nome == '':
        nome = '<Desconhecido>'
    if gols == '':
        gols = '0'
    return f'O jogador {nome} fez {gols} gol(s).'

nome = (str(input('Digite o nome do jogador: '))).capitalize().strip()
gols = (str(input('Digite quantos gols: '))).strip()

print(ficha(nome,gols))

#função ficha
#nome =
#gols =

#mostrar a ficha do jogador