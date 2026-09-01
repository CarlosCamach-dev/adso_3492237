palabra = input("Ingrese una palabra: ")
letras = list(palabra) #Lo que hace "List" es convertir una cadena de texto en una lista, donde cada caracter de la cadena se convierte en un elemento de la lista. Por ejemplo, si se ingresa "hola", la lista resultante sería ["h", "o", "l", "a"].
cantidad = 0
for i in range (len(letras)):
    if palabra[i] == 'a' or palabra[i] == 'e' or palabra[i] == 'i' or palabra[i] == 'o' or palabra[i] == 'u':
        cantidad = cantidad + 1

print("La cantidad de vocales en la palabra son:", cantidad)