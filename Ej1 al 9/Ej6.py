phrase = input('Ingrese frase: ')
string = input ('Ingrese string: ')

phrase = phrase.split(' ')
counter = 0

for word in phrase:
    if word.lower() == string.lower():
        counter += 1

print (f'Resultado: ', counter)