numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros.reverse() 
print(*numeros, sep=", ")
#El comando "reverse()" lo que hace es invertir el orden de la lista, es igual que el comando "lista.sort()" pero a la inversa o utilizando "lista.sort(reverse=True)" funciona igual, y el "*" lo que hace es que los valores de la lista se impriman sin corchetes ni comillas, porque el "*" seapra cada valor de la lista, y el "sep" lo que hace es colocar un separador entre los valores de la lista.