num = float(input("Ingrese un numero de 2 digitos: "))

unidad = num % 10
decena = num / 10

print(f"La decena del numero {num:.0f}", f"es {decena:.0f}", f"y la unidad es {unidad:.0f}")