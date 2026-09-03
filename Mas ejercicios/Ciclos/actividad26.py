
cant = int(input("Ingrese la cantidad de números: "))
negativo = 0
positivo = 0
cero = 0
for i in range(cant):
    num = int(input("Ingrese el número: "))
    if num < 0:
        negativo += 1
    elif num > 0:
        positivo += 1
    elif num == 0:
        cero += 1

print(f"Cantidad de números negativos: {negativo}")
print(f"Cantidad de números positivos: {positivo}")
print(f"Cantidad de números cero: {cero}")