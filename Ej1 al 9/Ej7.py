import string

text = """La brecha salarial alcanzó el 27,7%: las mujeres ocupadas
debieron trabajar 8 días y 10 horas más que los varones ocupados para
ganar lo mismo que ellos en un mes. """

upper = 0
lower = 0
no_letter = 0
words = len(text.split())

for caracter in text:
    if caracter.isupper():
        upper += 1
    elif caracter.islower():
        lower += 1
    elif not caracter.isalpha() and not caracter.isspace():
        no_letter += 1

print (f'Mayusculas: ', upper)
print (f'Minusculas: ', lower)
print (f'Caracteres no letras: ', no_letter)
print (f'Cantidad de palabras: ', words)
