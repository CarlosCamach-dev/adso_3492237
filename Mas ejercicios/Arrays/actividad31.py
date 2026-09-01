numeros = []
mayor = 0
menor = 0
cant = int(input("Ingrese la cantidad de numeros que comparara: "))

for i in range(cant):
    numero = int(input("Ingrese un numero: "))
    numeros.append(numero)

for i in range(cant):
    if mayor < numeros[i]:
        mayor = numeros[i]

for i in range(cant):
    if menor < numeros[i]:
        menor = numeros[i]
print("Mayor:", mayor)
print("Menor:", menor)