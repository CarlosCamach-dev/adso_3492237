palabra = input("Ingrese una palabra: ")
vocales = 0
for letra in palabra:
    if letra.lower() in "aeiou" or letra.lower() in "áéíóú":
        vocales += 1

print(f"La palabra contiene {vocales} vocales.")