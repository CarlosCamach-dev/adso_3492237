abecedario = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
for i in range(len(abecedario) - 1, -1, -1):
    if (i + 1) % 3 == 0:
        abecedario.pop(i)
        
print(abecedario)
#Len hace que se cuente la cantidad de elementos que hay en la lista, en este caso el abecedario. y range se puede dentro de su () colocar el inicio, el final y el paso, en este caso se hace un conteo regresivo desde la cantidad de elementos que hay en la lista hasta -1, y el paso es -1. que es pop? pop es una forma de eliminar elementos de una lista. tambien esta remove pero en este caso no se utilizo.