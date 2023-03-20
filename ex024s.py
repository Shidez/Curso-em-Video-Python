cidade = input('Digite o nome de uma cidade:').strip()
cidade1 = cidade.capitalize()
num = (cidade1.split()[0] == "Santo")
print('A cidade digitada tem a primeira palavra Santo? {}'.format(num))