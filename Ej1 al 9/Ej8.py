word = input('Ingrese palabra: ')

word = word.lower()
letters = list(word)
heterograma = True

for letter in letters:
    
    if letters.count(letter) > 1:
        heterograma = False
        break

if heterograma:
    print ('Es heterograma.')
else:
    print ('No es heterograma.')