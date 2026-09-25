numeros = []
cant = int(input("Ingrese la cantidad de números: "))
for i in range(cant):
    num = int(input("Ingrese el número: "))
    numeros.append(num)

for num in numeros:
    if numeros.count(num) > 1:
        numeros.remove(num)

print("Números sin repeticiones:", numeros)

#Count sirve para contar cuantas veces hay un elemento en una lista.