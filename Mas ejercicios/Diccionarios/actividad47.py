vendedores = {}
cant = int(input("Ingrese la cantidad de vendedores: "))
for i in range(cant):
    nombre = input("Ingrese el nombre del vendedor: ")
    ventas = float(input("Ingrese el total de ventas del vendedor: "))
    vendedores[nombre] = ventas

print("Mayor vendedor:")
for nombre, ventas in vendedores.items():
    if ventas == max(vendedores.values()):
        print(f"{nombre} -> ${ventas:.0f}")