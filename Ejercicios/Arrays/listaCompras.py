listaProductos = []
cant = int(input("Ingrese la cantidad de productos: "))
for i in range(cant):
    listaProductos.append(input("Ingrese el nombre del producto: "))

print("Lista de productos:")
for i,producto in enumerate(listaProductos, start=1):
    print(f"{i}. {producto}")
    #Enumerate permite enumerar cada indice de la lista, y el parámetro start=1 indica que la enumeración debe comenzar desde 1 en lugar de 0.