listaNumeros = []
cant = int(input("Ingrese la cantidad de números: "))
for i in range(cant):
    num = int(input("Ingrese el número: "))
    listaNumeros.append(num)

buscador = int(input("Ingrese el número a buscar: "))
if buscador in listaNumeros:
    print(f"El numero {buscador} esta en la posición {listaNumeros.index(buscador) + 1}")