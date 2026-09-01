listaNotas = []
suma = 0
cant = int(input("Ingrese la cantidad de notas: "))

for i in range(cant):
    notas = float(input(f"Ingrese la nota {i + 1}: "))
    listaNotas.append(notas)

for i in range(cant):
    suma += listaNotas[i]

promedio = suma / cant

print("Promedio:", promedio)