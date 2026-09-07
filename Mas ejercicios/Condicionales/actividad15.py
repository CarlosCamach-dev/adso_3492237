valorCompra = float(input("Ingrese el valor de la compra: "))
if valorCompra > 500000:
    descuento = valorCompra * 0.10
    totalPagar = valorCompra - descuento
    print(f"Descuento: ${descuento}")
else:
    totalPagar = valorCompra
    exit

print(f"Total a pagar: ${totalPagar}")
