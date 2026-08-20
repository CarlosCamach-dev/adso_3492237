compra = float(input("Cuanto es el valor de la compra en total?"))
print('-'*50)

if compra > 100000:
        descuento = compra * 0.2
        total = compra - descuento

        print("Felicidades!! obtuviste un descuento de 20%, tu compra de valor de", compra ,f"queda en {total:.0f}")
else:
       print("No obtuviste descuento") 