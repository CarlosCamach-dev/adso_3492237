valorCompra = float(input("Ingrese el valor total de la compra: "))
if valorCompra > 100000:
    valorfinal = valorCompra - (valorCompra * 0.2)
    print('-'*50)
    print(f"El valor total con el descuento es: {valorfinal}")
else:
    print(f"El valor total a comprar es: {valorCompra}")