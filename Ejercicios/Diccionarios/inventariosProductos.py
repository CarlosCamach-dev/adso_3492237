productos = {}
cant = int(input("Dime la cantidad de productos que hay: "))
for i in range(cant):
    producto = input("Ingrese el nombre del prodcuto: ")
    cantidad = input("Ingrese la cantidad del producto: ")
    productos[producto] = cantidad 

buscador = input("Ingrese el nombre del producto que quiere buscar: ")
if buscador in productos: 
    productos.get(buscador) 
    print(f"Cantidad disponible de {producto}: {cantidad}")
