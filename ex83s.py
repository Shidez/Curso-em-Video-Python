
frase = str(input('Digite uma frase com (): '))
#if '(' or ')' in frase:
    #print(f' ( {frase.count("(")}')
    #print(f' ) {frase.count(")")}')

if frase.count('(') == frase.count(')'):
    print('parenteses ok')
else:
    print('parenteses errados')




