listaMaterias = []
notas = []
max = int(input("Ingrese la cantidad de materias: "))

for i in range(max):
    materia = input("Ingrese el nombre de la materia: ")
    listaMaterias.append(materia)

for materia in listaMaterias:
    nota = float(input("Ingrese la nota de la materia " + materia + ": ")) #La "+" hace lo mismo que "," pero hace que la variable se vea más pegada al texto, sin espacio.
    notas.append(nota)

for i in range(max):
    print("La nota de la materia", listaMaterias[i], "es:", notas[i])