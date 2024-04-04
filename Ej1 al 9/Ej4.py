word = input("Ingresá una palabra: ")

if "a" in word and 'n' in word:
    print("Hay al menos una letra a y una n.")
elif 'n' in word:
    print("Hay al menos una letra n en la palabra.")
elif 'a' in word:
    print("Hay al menos una letra a en la palabra.")
else:
    print("No hay ni letras n ni a en la palabra.")