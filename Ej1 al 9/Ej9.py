word = input('Ingrese palabra: ').lower()
points = 0

word = list(word)
valor1 = 'AEIOULNRST'
valor2 = 'DG'
valor3 = 'BCMP' 
valor4 = 'FHVWY'
valor5 = 'K'
valor8 = 'JX'
valor10 = 'QZ'

for letter in word:
    if letter in valor1.lower():
        points += 1
    elif letter in valor2.lower():
        points += 2
    elif letter in valor3.lower():
        points += 3
    elif letter in valor4.lower():
        points += 4
    elif letter in valor5.lower():
        points += 5
    elif letter in valor8.lower():
        points += 8
    else:
        points += 10
    
print (f'Valor: ', points)

