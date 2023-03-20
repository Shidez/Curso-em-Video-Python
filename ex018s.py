from math import cos, sin, tan, radians
ang = float(input('Digite o ângulo a ser calculado: '))
cosseno = (cos(radians(ang)))
seno = (sin(radians(ang)))
tangente = (tan(radians(ang)))
print('O valor do cosseno é {:.2f}, seno é {:.2f} e a tangente é {:.2f}.'.format(cosseno,seno,tangente))

