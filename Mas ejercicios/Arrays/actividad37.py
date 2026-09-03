numeros = []

cant = int(input("Ingrese la cantidad de números: "))
for i in range(cant):
    num = int(input("Ingrese el número: "))
    numeros.append(num)
j = len(numeros) - 1
for i in range(len(numeros) - 1, -1, -1):
    if numeros[i] >= numeros[j]:
        numeros[i] = numeros[i]

print(numeros)