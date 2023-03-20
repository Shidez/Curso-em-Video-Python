nome = input('Qual o seu nome completo?')
print('Seu nome em letras maiúsculas é{}'.format(nome.upper()))
print('Seu nome em letras minuscúlas é{}'.format(nome.lower()))
print('O seu nome completo tem {} letras'.format(len(nome.replace(" ",""))))
print('O seu primeiro é {} e ele tem {} letras.'.format(nome.split()[0],len(nome.split()[0])))



