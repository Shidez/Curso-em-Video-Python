from datetime import date

def voto():
    ano2 =date.today().year
    idade = ano2 - ano
    if 18 < idade < 70:
        return f'Com {idade} anos é OBRIGATÓRIO.'
    if 16 <= idade == 18:
        return f'Com {idade} anos é OPCIONAL.'
    if idade > 70:
        return f'Com {idade} anos é OPCIONAL.'
    if idade < 16:
        return f'Com {idade} anos NÃO PODE VOTAR.'


ano = int(input('Qual o seu ano de nascimento? '))
print(voto())

