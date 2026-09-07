numeros = []
mayor = 0
menor = 0
cant = int(input("Ingrese la cantidad de numeros que comparara: "))

for i in range(cant):
    numero = int(input("Ingrese un numero: "))
    numeros.append(numero)

mayor = max(numeros)
menor = min(numeros)
print("Mayor:", mayor)
print("Menor:", menor)