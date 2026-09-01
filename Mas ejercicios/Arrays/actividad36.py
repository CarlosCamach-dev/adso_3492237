numeros = []
cant = int(input("Ingrese la cantidad de números: "))
for i in range(cant):
    num = int(input("Ingrese el número: "))
    numeros.append(num)

for i in range(len(numeros)-1, -1, -1):
    if numeros[i] != numeros[i-1]:
        pass
    else:
        numeros.remove(numeros[i])

print("Números sin repeticiones:", numeros)

