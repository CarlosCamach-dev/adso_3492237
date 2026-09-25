letras = {}
palabra = input("Ingrese una palabra: ")
for letra in palabra:
    letras[letra] = letras.get(letra, 0) + 1

print("Cantidad de letras en la palabra:")
for letra, cantidad in letras.items():
    print(f"{letra}: {cantidad}")