cant = int(input("Ingrese la cantidad de notas: "))
for i in range(cant):
    nota = int(input(f"Ingrese la nota {i + 1}: "))
    notas += nota

promedio = notas / cant

print(f"El promedio de las notas es: {promedio}")
    