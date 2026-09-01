listaMaterias = []

max = int(input("Ingrese la cantidad de materias: "))

for i in range(max):
    materia = input("Ingrese el nombre de la materia: ")
    listaMaterias.append(materia)

print("Las materias ingresadas son:")
for materia in listaMaterias:
    print(materia)