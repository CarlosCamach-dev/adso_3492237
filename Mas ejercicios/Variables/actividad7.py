precio = int(input("Ingrese el precio del prodcucto: "))
descuento = int(input("Ingrese el descuento hacia el producto: "))

decimal = descuento / 100
descuento = precio * decimal
precioFinal = precio - descuento

print(f"Precio original: {precio:.0f}$")
print(f"Descuento aplicado: {descuento:.0f}$")
print(f"Precio Final: {precioFinal:.0f}$")