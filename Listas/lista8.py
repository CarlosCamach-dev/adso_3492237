palindromo = input("Ingrese una palabra: ")
letras = list(palindromo) #Se puede agarrar una cadena y volverla en una lista, agarrando cada caracter en una posicion de la lista. por ejemplo, si se ingresa "hola", la lista seria ["h", "o", "l", "a"].
texto = "Es un palindromo"
cantidad = len(letras)
for i in range(cantidad):
    if palindromo[i] != palindromo[cantidad - 1 - i]: #El "!=" significa "diferente de", es decir, si la letra en la posición i es diferente a la letra en la posición opuesta (cantidad - 1 - i), entonces no es un palíndromo. Ademas, la posición opuesta se calcula restando 1 a la cantidad total de letras y luego restando i, para obtener el índice correspondiente desde el final de la lista.
        texto = "No es un palindromo"

print(texto)