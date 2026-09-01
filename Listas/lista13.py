numeros = []
suma = 0
promedio = 0
desviacionTipica = 0
cantidad = int(input("Ingrese la cantidad de numeros que ingresaras: "))
for i in range(cantidad):
    numero = float(input("Ingrese el numero que desees: "))
    numeros.append(numero)

for i in range(cantidad):
    suma = suma + numeros[i]

promedio = suma / cantidad
for i in range(cantidad):
    paso1 = promedio - numeros[i] ** 2
    paso2 = paso2 + paso1**2
    paso3 = 