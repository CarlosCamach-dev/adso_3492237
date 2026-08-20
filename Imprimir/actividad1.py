nombreProducto = input("Dime el nombre del producto:")
valorProducto =input("Dime el valor del producto:")
iva = 0

iva = float(valorProducto) * 0.19
total = float(valorProducto) + float(iva)

print("El valor total de tu compra de ", nombreProducto, "es:", total)