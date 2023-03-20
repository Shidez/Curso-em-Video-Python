#Palindromo com laço:

word = str(input('Digite uma frase: ')).lower().strip()
word1 = word.split()
word2 = ''.join(word1)
#word3 = word2[::-1]

if word2 == word3:
    print('PALINDROMO')

else:
   print('NÃO PALINDROMO')


#outras opçoes:
word = input()
if str(word) == "".join(reversed(word)) :
    print("Palindrome")
else:
    print("Not Palindrome")

#outra opção:
word = input()
    if str(word) == str(word)[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")

