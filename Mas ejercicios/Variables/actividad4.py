notas = []
suma = 0
for i in range(5):
    nota = float(input(f"Ingrese la nota {i + 1}: "))
    notas.append(nota)
for nota in notas:
    suma += nota
    prom = suma / len(notas)

print(f"Promedio final: {prom}")
