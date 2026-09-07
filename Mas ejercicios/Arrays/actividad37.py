numeros = []
ordenados = []
cant = int(input("Ingrese la cantidad de números: "))
for i in range(cant):
    num = int(input("Ingrese el número: "))
    numeros.append(num)
for num in range(min(numeros), max(numeros) + 1):
    if num in numeros:
        ordenados.append(num)
print("lista ordenada: ")
for num in ordenados:
    print(num)
