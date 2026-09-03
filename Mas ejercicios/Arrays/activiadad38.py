lista1 = []
lista2 = []
listaCombinada = []
cant = int(input("Ingrese la cantidad de números: "))
for i in range(cant):
    num = int(input("Ingrese el número: "))
    lista1.append(num)
for i in range(cant):
    num = int(input("Ingrese el número: "))
    lista2.append(num)
listaCombinada = lista1 + lista2
print("Lista combinada:", listaCombinada)