numeros = []
j = 1
cant = int(input("Ingrese la cantidad de números: "))
for i in range(cant):
    num = int(input("Ingrese el número: "))
    numeros.append(num)

if i in range(len(numeros)- 1, -1, -1):
    if numeros[i] >= numeros[j]:
        numeros[i] = numeros[i+1]
    print(numeros)