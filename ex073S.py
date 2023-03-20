times = ('Atlético', 'Flamengo', 'Palmeiras ', 'Fortaleza', 'Corinthians', 'Bragantino', 'Fluminense', 'América-MG',
         'Atletico-GO', 'Santos', 'Ceará', 'Internacional', 'São Paulo', 'Athletico-PR', 'Cuiabá',
         'Juventude', 'Grêmio', 'Bahia', 'Sport', 'Chapecoense')

print(f'Os cinco primeiros times do brasileirão 2021 são {times[:5]}')
print(f'Os quatro últimos times do brasileirão 2021 são {times[-4:]}')
print(f'Os times em ordem alfabética: {sorted(times)}')
print(f'O time da Chapecoense terminou na posição {times.index("Chapecoense")+1}ª da tabela de 2021.')