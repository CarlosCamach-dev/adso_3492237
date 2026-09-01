pares = []
impares = []
cant = int(input("Ingrese la cantidad de números: "))
for i in range(cant):
    num = int(input("Ingrese el número: "))
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print("Números pares:", len(pares))
print("Números impares:", len(impares))