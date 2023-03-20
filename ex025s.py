name = input('Digite o seu nome completo:').strip()
name = name.title()
name2= ('silva' in name.lower())
print('O seu nome {} tem a palavra Silva? {}'.format(name,name2))