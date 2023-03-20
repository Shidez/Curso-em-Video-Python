from datetime import date
print('ALISTAMENTO MILITAR')
ano = int(input('Qual seu ano de nascimento? '))

ano1 = date.today().year
idade = ano1 - ano

if idade < 18:
    print('Você é muito jovem e deve aguardar {} anos para se alistar.'.format(18 - idade))

elif idade == 18:
    print('Está no ano do seu alistamento, clique no link abaixo e cadastre-se:')
    print('https://alistamento.eb.mil.br/')

else:
    print('Se você não se alistou ainda, está atrasado em {} anos, consulte o video abaixo e saiba mais:'.format(idade-18))
    print ('https://www.youtube.com/watch?v=rfQYaXMvgPM')