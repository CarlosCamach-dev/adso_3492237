palabras = {}
frase = input("Ingrese una frase: ")
for palabra in frase.split():
    palabras[palabra] = palabras.get(palabra, 0) + 1
print("Cantidad de palabras en la frase:")
for palabra, cantidad in palabras.items():
    print(f"{palabra}: {cantidad}")
#split divide en caracteres una cadena.